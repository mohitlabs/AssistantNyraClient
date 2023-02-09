FROM python:3
WORKDIR /AssistantNyraClient
COPY ./requirements.txt ./
COPY ./src ./src
COPY ./audio ./audio
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "src/main.py"]
