FROM python:3.7-slim-stretch
COPY . .
RUN pip install -r requirements.txt

ENV PATH_TO_MODEL="model.pickle"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]