import requests
import time
from datetime import datetime

class dispile:
    def __init__(self,channel:str,token:str)->None:
        
        #defines USER SPECIFIC inputs 
        self.channel:str = channel
        self.token:str = token

        #Post and get link
        self.post_link:str = f"https://discord.com/api/v9/channels/{self.channel}/messages"
        self.get_link:str = f"{self.post_link}?limit=100"

        #headers and other useful constant variables
        self.headers:dict = {"authorization": self.token} 
        self.start_time:float = time.time()




    def get_message(self)->dict:
        
        message_content = requests.get(self.get_link,headers=self.headers)#get request
        json_content:list = message_content.json()#converts get request into json
        isolate_message:dict = {}#stores useful information from json into dict

        for index,item in enumerate(json_content): #iterates through json 

            time:str = item.get("timestamp") #gets time message was sent
            date_format:str = "%Y-%m-%dT%H:%M:%S.%f%z" #formatted discord date
            send_time:int = datetime.strptime(time,date_format).timestamp()

            if send_time > self.start_time:

                message:str = item.get("content") #gets message content
                isolate_message[message] = send_time
            

        return isolate_message
    


    def compile(self)->str:
        
        while(True):
            msg_sent = self.get_message()
            
        #function is not finished. For now, just requests a post message.
        #data = {"content": "Hello"}
        #requests.post(self.post_link,headers=self.headers,json=data)




test_instance = dispile(channel="1167715294047899648",token="")

while True:
    dict_ = test_instance.get_message()
    print(dict_)


