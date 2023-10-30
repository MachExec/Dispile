import requests

class dispile:
    def __init__(self,c,t)->None:
        
        self.channel = c
        self.token = t
        self.link = f"https://discord.com/api/v9/channels/{self.channel}/messages"

    def compile(self):
        headers = {"authorization": self.token} 
        message = "Hello"
        data = {"content": message}
        requests.post(self.link,headers=headers,json=data)


