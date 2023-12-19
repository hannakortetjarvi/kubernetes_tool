FROM python:latest
WORKDIR /ui
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /ui
CMD ["python", "src/main.py"]