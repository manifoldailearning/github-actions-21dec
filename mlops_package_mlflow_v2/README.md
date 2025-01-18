```json

{
  "data": [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2]
  ]
}

```

# Docker Commands

```bash
docker build -t streamlit-demo . 
docker run -p 8501:8501 streamlit-demo
```

# Commands for MLFlow

```
mlflow ui 

mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlruns \
    --host 0.0.0.0 \
    --port 5001

```