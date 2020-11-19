FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /home/etentlabs/Documents/cloudsigma/container2/
COPY requirements.txt 
RUN pip install -r requirements.txt
COPY . .