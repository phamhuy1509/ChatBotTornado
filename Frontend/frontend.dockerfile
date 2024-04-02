FROM python:3.10
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6885
CMD [ "python", "src/web_frontend/chatbot.py" ]