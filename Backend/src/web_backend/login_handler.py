import json
from base_handler import BaseHandler
class LoginHandler(BaseHandler):
    async def post(self):
        request_data = json.loads(self.request.body)
        username = request_data['username']
        password = request_data['password']
        if username=="admin" and password=="admin":
            self.set_status(200)
            self.write(json.dumps({'X-Xsrftoken': f"{self.request.headers.get('X-Xsrftoken')}"}))
        else:
            self.set_status(400)
            self.write(json.dumps({'message': "Login failed"}))
