import json
import pandas as pd
import requests


if __name__ == "__main__":
    df = pd.read_csv("data/archive.zip").drop("target", axis=1).sample(frac=1)
    df["id"] = range(len(df))
    data = df.to_dict("records")
    print(f"Data sample: {data[0]}")
    response = requests.post("http://localhost:8000/predict", data=json.dumps(data))
    print(f"Status code: {response.status_code}")
    print(f"Response samples: {response.json()[:20]}")
