import json
import tornado
from base_handler import BaseHandler
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
class LoginHandler(BaseHandler):
    def get(self):
        self.render("../web_ui/login.html")
    async def post(self):
        self.check_xsrf_cookie()
        username = self.get_argument("input_username")
        password = self.get_argument("input_password")
        data_send = {
            "username": username,
            "password": password
        }
        if username=="" or password=="":
            self.write("Username or password is empty")
        else:
            request = HTTPRequest(url="http://127.0.0.1:6886/login", 
                                  method="POST", 
                                  headers={"Content-Type": "application/json",
                                           "X-Xsrftoken": self.get_argument("_xsrf")},
                                  body=json.dumps(data_send))
            response = await AsyncHTTPClient().fetch(request=request)
            reponse_format = response.body.decode()
            if response.code == 200:
                self.set_secure_cookie("_xsrf", json.loads(reponse_format)['X-Xsrftoken'])
                self.redirect("/chatform")
            else:
                self.write(json.loads(reponse_format)['message'])
