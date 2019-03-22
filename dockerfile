FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3-pip
ADD requirements.txt /
RUN pip3 install -r requirements.txt
ADD server.py /
EXPOSE  8000
CMD ["python3", "server.py"]
