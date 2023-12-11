FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]


