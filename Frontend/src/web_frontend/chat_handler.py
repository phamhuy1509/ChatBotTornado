import time
import json
import tornado.websocket
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
class ChatHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        ChatHandler.clients.add(self)

    async def on_message(self, message):
        request = HTTPRequest(url="http://54.169.203.68:6886/api/chat",
                              method="POST",
                              headers={"Content-Type": "application/json"},
                              body=json.dumps({"message": message}))
        response = await AsyncHTTPClient().fetch(request=request)
        time.sleep(3)
        bot_response = json.loads(response.body.decode())['bot_response']
        for client in self.clients:
            client.write_message(bot_response)

    def on_close(self):
        ChatHandler.clients.remove(self)
