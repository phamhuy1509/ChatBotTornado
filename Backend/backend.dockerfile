FROM python:3.10
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6886
CMD [ "python", "src/web_backend/chatbot.py" ]