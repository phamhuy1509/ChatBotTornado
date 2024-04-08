import json
import time
import random
from base_handler import BaseHandler

def generate_bot_response(message):
    responses = [
        "Chào bạn, tôi có thể giúp gì được cho bạn",
        "Rất vui khi được gặp bạn",
        "for i in range(1, 101):\n\tif i % 2 == 0 and (i % 3 != 0 or i % 5 != 0):\n\t\tprint(i)",
        "def square(n):\n\treturn n ** 2\nfor i in range(10):\n\tprint(i, square(i))",
        "Dưới đây là một đoạn code python: <<python>> def square(n):\n\treturn n ** 2\nfor i in range(10):\n\tprint(i, square(i)) <</python>>"
    ]
    return random.choice(responses)
class ChatHandler(BaseHandler):
    def post(self):
        request_data = json.loads(self.request.body)
        message = request_data['message']
        bot_response = generate_bot_response(message)
        time.sleep(2)
        self.write(json.dumps({"bot_response": bot_response}))
