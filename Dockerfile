FROM python:3.10.4-alpine

WORKDIR /app
COPY . /app

COPY root /var/spool/cron/crontabs/root

RUN pip install -r requirements.txt

RUN chmod +x /app/update.py
CMD crond -l 2 -f 

# CMD ["python3", "update.py"]