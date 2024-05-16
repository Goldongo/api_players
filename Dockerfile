FROM python:3-slim
WORKDIR /goldongo
RUN pip3 install --no-input -r req.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
