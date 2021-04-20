# ML in Production HW1
Python version used: 3.7.9

Installation (for Windows):  

    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install -r requirements.txt

Installation (for Linux):  

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

### Data
Dataset is [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci). Download zip archive and put it to data/raw.

### Configuration and logging
The project is configured with [Hydra](https://hydra.cc/). You can find configs in *conf* directory.
All Hydra configs should be described as dataclasses in *src/config*.  
Logs are configured in *conf/logging.conf* file. Logs are stored in *logs* directory.

### Testing
We use [pytest](https://docs.pytest.org/) as a framework for testing. You can run tests with the following command:

    pytest tests


### Code formatting
Code in this repository is automatically formatted with [Black](https://github.com/psf/black). 
Moreover, compliance with Black formatting rules is tested in *tests* module.  

Check for Black formatting proposals:

    black --diff path_to_code

Format code automatically:

    black path_to_code

### Useful commands

EDA report generation:

    python -m src.visualization.eda

Run training pipeline:

    python -m src.model.train_pipeline

Get predictions:
    
    python -m src.model.predict --data_path *path_to_data* 
                                --model_path *path_to_model* 
                                --output_path *path_to_save_predictions*

### Project structure
Some of the directories listed are in .gitignore, so you don't find them in the repository.  
They either should be created (e.g. data folder) or will be generated when you run the commands.


    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── conf               <- Configuration files.
    │
    ├── data
    │   ├── preds          <- Predictions from the model.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── logs               <- Logs go here.
    │
    ├── models             <- Trained and serialized models.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── outputs            <- Outputs from hydra.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── eda            <- EDA reports
    │   └── experiments    <- Configs, metrics and model dumps for conducted experiments.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment.
    │
    └── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── config         <- configuration dataclasses for type checking
    │   │
    │   ├── data           <- code to download or generate data
    │   │
    │   ├── features       <- code to turn raw data into features for modeling
    │   │
    │   ├── model          <- code to train models and then use trained models to make predictions
    │   │
    │   ├── utils          <- miscellaneous util functions
    │   │
    │   └── visualization  <- code for eda generation
    │
    └── tests              <- unit tests for project modules