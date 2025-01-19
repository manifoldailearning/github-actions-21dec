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

```json

{
  "sepal_length": 2,
  "sepal_width": 3,
  "petal_length": 5,
  "petal_width": 4
}

```

```bash
python main.py

```

mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlruns \
    --host 0.0.0.0 \
    --port 5000