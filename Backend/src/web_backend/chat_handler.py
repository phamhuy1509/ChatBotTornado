import json
from base_handler import BaseHandler
from huggingface_hub import AsyncInferenceClient, InferenceClient

def generate_bot_response(message):
    prompt_template=f'''You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.
### Instruction:
{message}
### Response:
'''
    client = InferenceClient(model="http://172.38.0.5:6884")
    generation_text = client.text_generation(prompt=prompt_template,
                                             max_new_tokens=1024,
                                             do_sample=True,
                                             temperature=0.2,
                                             top_k=50,
                                             top_p=0.1,
                                             repetition_penalty=1.2)
    return generation_text
class ChatHandler(BaseHandler):
    def post(self):
        # try:
        request_data = json.loads(self.request.body)
        message = request_data['message']
        bot_response = generate_bot_response(message)
        self.write(json.dumps({"bot_response": bot_response}))
        # except:
        #     self.write(json.dumps({"bot_response": "Error chatbot is not available at the moment."}))
