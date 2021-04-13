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

### Useful commands

All commands are configured with [Hydra](https://hydra.cc/). You can find configs in *conf* directory.

EDA report generation:

    python -m src.visualization.eda