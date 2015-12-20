FROM python:2

COPY ssws.py /ssws.py

EXPOSE 80

CMD ["python", "/ssws.py"]
