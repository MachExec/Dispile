import requests
import time

class dispile:
    def __init__(self,channel:str,token:str)->None:
        
        self.channel:str = channel
        self.token:str = token

        self.post_link:str = f"https://discord.com/api/v9/channels/{self.channel}/messages"
        self.get_link:str = f"{self.post_link}?limit=50"

        self.headers:dict = {"authorization": self.token} 
        self.start_time:float = time.time()




    def get_message(self)->None:
        
        message_content = requests.get(self.get_link,headers=self.headers)
        json_content = message_content.json()
        isolate_message = {}

        for index,item in enumerate(json_content):
            message = item.get("content")
            time = item.get("timestamp")
            isolate_message.append(message)

            if message == "53643tbnfjfefefefenhr":
                print("true")

        return isolate_message
    


    def compile(self)->str:
        
        message = "Hello"
        data = {"content": message}
        requests.post(self.post_link,headers=self.headers,json=data)

        return message

test_instance = dispile(channel="1167715294047899648",token="")
while(True):
    liust = test_instance.get_message()
