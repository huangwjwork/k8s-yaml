FROM python:3.6
RUN python3 -m pip install prometheus_client
COPY test_exporter.py /bin/test_exporter.py
EXPOSE 10000
CMD python3 /bin/test_exporter.py
# docker build -t test_exporter:v0.1 .
