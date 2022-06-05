FROM python:3.7-slim
RUN apt install libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
WORKDIR /app/
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]