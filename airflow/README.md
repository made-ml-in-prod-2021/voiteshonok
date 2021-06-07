# ML in Production HW3

### Running airflow

To run airflow you'll need Docker. First, go to airflow folder and set the environmental variable with your current path:
```
cd airflow

# for Windows
set HOST_DATA_DIR=%cd%\data
# for Linux 
HOST_DATA_DIR="$(pwd)"/data
```

Then, if you run for the first time, initialize airflow database:
```
docker-compose up airflow-init
```

Finally, you can run the app with the following command:
```
docker-compose up --build
```

Airflow should now be available at *http://localhost:8080/*, with login = airflow and password = airflow.

### Working with code locally
If you need to work with code locally (e.g. test or modify it), please use Python3.6 and install packages from requirements_dev.txt.
```
pip install -r requirements_dev.txt
```

### Testing code
You can test code inside images by running 
```
pytest images
```

### Formatting and linter
The code is formatted with black and checked by flake8 linter. 
To run them locally, use the following commands:
```
flake8
black images
black dags
```
