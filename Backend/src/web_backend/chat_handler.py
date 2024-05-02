import json
from base_handler import BaseHandler
from huggingface_hub import AsyncInferenceClient

class ChatHandler(BaseHandler):
    async def post(self):
        request_data = json.loads(self.request.body)
        message = request_data['message']
        prompt_template=f'''You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.
### Instruction:
{message}
### Response:
'''     
        client = AsyncInferenceClient(model="http://172.38.0.5/6884")
        async for token in await client.text_generation(prompt=prompt_template,
                                                        max_new_tokens=1024,
                                                        do_sample=True,
                                                        temperature=0.2,
                                                        top_k=50,
                                                        top_p=0.3,
                                                        repetition_penalty=1.2,
                                                        stream=True):
            self.write(json.dumps({"bot_response": token}))
