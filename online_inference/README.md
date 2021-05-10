# ML in Production HW2

### Running
```
docker pull voiteshonok/online_inference:v5
docker run -p 8000:8000 -it voiteshonok/online_inference:v5
```

### Docker image optimizations
Here are the optimizations I've tried (blue text on the right of the screenshot describes changes to [the sample Dockerfile](https://github.com/made-ml-in-prod-2021/inference_examples/blob/main/online_inference/Dockerfile)).
requirements_dev.txt is a file produced with pip freeze, requirements.txt contains only the packages needed for inference.  
Compressed v5 image on docker hub is 216.54 MB.
![optimizations](optimizations.png)