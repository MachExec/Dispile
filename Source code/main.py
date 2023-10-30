import requests

class dispile:
    def __init__(self,c,t)->None:
        self.channel = c
        self.token = t

    def compile(self):
        pass



link = "https://discord.com/api/v9/channels/1167715294047899648/messages"
token = ""

headers = {"authorization": token} 
message = "Hello"
data = {"content": message}


requests.post(link,headers=headers,json=data)
