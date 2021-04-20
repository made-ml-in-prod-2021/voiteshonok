import pickle
import hydra
import logging.config
import typing
import yaml
import os

from omegaconf import OmegaConf
from src.config import Config, SimpleSplitConfig, SaveModelConfig
from src.data import read_data, split_train_val_data
from src.features import separate_target, HeartDatasetTransformer
from src.utils import get_path_from_root
from sklearn.metrics import classification_report
from typing import Any
from datetime import datetime
from pathlib import Path


logging.config.fileConfig("conf/logging.conf")
logger = logging.getLogger("mlProject.train_pipeline")


def track_experiment(model: Any, cfg: Config, metrics: dict) -> None:
    saving_path = get_path_from_root(
        os.path.join(
            cfg.main.track.experiment_data_dir,
            datetime.now().strftime(cfg.main.track.experiment_dir_name_format),
        )
    )
    Path(saving_path).mkdir(parents=True)
    with open(
        os.path.join(saving_path, cfg.main.track.metrics_file_name), "w"
    ) as metrics_file:
        metrics_file.write(yaml.dump(metrics))
    with open(
        os.path.join(saving_path, cfg.main.track.config_file_name), "w"
    ) as config_file:
        config_file.write(OmegaConf.to_yaml(cfg))
    if cfg.main.track.save_model_weights:
        with open(
            os.path.join(saving_path, cfg.main.track.model_weights_file_name), "wb"
        ) as weights_file:
            pickle.dump(model, weights_file)


def save_model(model: Any, cfg: SaveModelConfig):
    saving_path = get_path_from_root(cfg.model_dir)
    Path(saving_path).mkdir(parents=True, exist_ok=True)
    with open(
        os.path.join(saving_path, cfg.model_weights_file_name), "wb"
    ) as weights_file:
        pickle.dump(model, weights_file)


@hydra.main(config_path="../conf", config_name="config")
def main(cfg: Config):
    logger.info("Started train pipeline")
    logger.debug(f"App config: \n{OmegaConf.to_yaml(cfg)}")
    data = read_data(get_path_from_root(cfg.main.input_data_path))
    logger.debug(f"Data shape is {data.shape}")
    if cfg.split.name == "simple_split":
        train_data, val_data = split_train_val_data(
            data, typing.cast(SimpleSplitConfig, cfg.split)
        )
    else:
        error_msg = f"Wrong split strategy {cfg.split.name}"
        logger.error(error_msg)
        raise ValueError(error_msg)

    train_features, train_target = separate_target(train_data, cfg.main.target_name)
    val_features, val_target = separate_target(val_data, cfg.main.target_name)

    logger.info(f"Started transforming data")
    transformer = HeartDatasetTransformer(cfg=cfg.transformer).fit(
        train_features, train_target
    )
    train_features, train_target = transformer.transform(train_features, train_target)
    val_features, val_target = transformer.transform(val_features, val_target)
    logger.debug(
        "Transformed data shape\n"
        f"train_features: {train_features.shape}\n"
        f"train_target: {train_target.shape}\n"
        f"val_features: {val_features.shape}\n"
        f"val_target: {val_target.shape}"
    )
    logger.info(f"Finished transforming data")

    logger.info("Started training a classifier")
    classifier = hydra.utils.instantiate(cfg.model).fit(train_features, train_target)
    logger.info("Finished training a classifier")

    logger.info("Started evaluating the classifier")
    val_predictions = classifier.predict(val_features)
    metrics = classification_report(val_target, val_predictions, output_dict=True)
    logger.debug(f"Metrics: \n{yaml.dump(metrics)}")
    logger.info("Finished evaluating the classifier")

    if cfg.main.track.track_experiment:
        logger.info("Start saving experiment info")
        track_experiment(classifier, cfg, metrics)
        logger.info("Finished saving experiment info")

    if cfg.main.save_model.overwrite_main_model:
        logger.info("Start saving model")
        save_model(classifier, cfg.main.save_model)
        logger.info("Finished saving model")

    logger.info("Finished train pipeline")


if __name__ == "__main__":
    main()
