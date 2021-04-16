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

### Configuration and logging
The project is configured with [Hydra](https://hydra.cc/). You can find configs in *conf* directory.
All Hydra configs should be described as dataclasses in *src/config*.  
Logs are configured in *conf/logging.conf* file. Logs are stored in *logs* directory.

### Testing
We use [pytest](https://docs.pytest.org/) as a framework for testing. You can run tests with the following command:

    pytest tests

### Useful commands

EDA report generation:

    python -m src.visualization.eda