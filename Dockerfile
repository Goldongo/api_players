FROM python:3-slim
WORKDIR /goldongo
COPY requirements.txt .
RUN pip3 install --no-input -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]