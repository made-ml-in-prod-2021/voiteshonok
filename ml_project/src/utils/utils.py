import hydra
import os


def get_path_from_root(path):
    root = hydra.utils.get_original_cwd()
    return os.path.join(root, path)
