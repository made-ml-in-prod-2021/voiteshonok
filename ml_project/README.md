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
Logs are configured in *conf/logging.conf* file. Logs are stored in *logs* directory.

### Useful commands

EDA report generation:

    python -m src.visualization.eda