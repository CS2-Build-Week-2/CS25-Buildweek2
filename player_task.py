import requests
from time import sleep
import json
import hashlib
import random
from decouple import config



api_key = config('API_key')



class Task:
    def __init__(self):
        self.current_room = {}
        self.wait = None



    def init_player(self):
        response = requests.get("https://lambda-treasure-hunt.herokuapp.com/api/adv/init/", headers={'Authorization': api_key}).json()
        self.wait = float(response.get('cooldown'))
        self.current_room = response
        sleep(response["cooldown"])
        return self.current_room

    def room_id(self):
        return self.current_room['room_id']



    def take(self):
        if len(self.current_room['items']) == 0:
            print('Nothing here to take')
            return None
        else:
            item = self.current_room['items']
            print(f'Taking {item}')
            response = requests.post("https://lambda-treasure-hunt.herokuapp.com/api/adv/take/",
            json={"name": item[0]}, headers={'Authorization': api_key}).json()
            sleep(response["cooldown"])

    def drop(self):
     if current_room['treasure'] == 0:
         print('droping {treasure}')
         response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/',
         json={"name": treasure[0]}, headers={'Authorization': api_key,}).json()
         sleep(response["cooldown"])
         print(res)


    def status(self):
        response = requests.post("https://lambda-treasure-hunt.herokuapp.com/api/adv/status/",
        headers={'Authorization': api_key}).json()
        print(response)
        sleep(response["cooldown"])


    def sell(self, item="treasure"):
        if self.current_room['title'] != 'Shop':
            print("You should go to the shop to sell")
        else:
            response1 = requests.post(" https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/",
            json={"name": item}, headers={'Authorization': api_key, "Content-Type": application/json}).json()
            print(response1)
            sleep(res1["cooldown"])
            response = requests.post(" https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/",
            json={"name": item, "confirm": "yes"}, headers={'Authorization': api_key}).json()
            print(response)
            sleep(response["cooldown"])



    def change_name(self, name):
        response = requests.post("https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/",
        json={"name": [name], "confirm": "Hello there"}, headers={'Authorization': api_key}).json()
        print("You shall be known as", str(name))
        print(response)
        return response


    def wallet(self):
        response = requests.get("https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/",
        headers={'Authorization': api_key}).json()
        print(response)
        sleep(response["cooldown"])

    # def move(self, direction):
    #     if direction not in self.current_room['exits']:
    #         print("You can't go that way")
    #         return
    #     else:
    #         response = requests.post("https://lambda-treasure-hunt.herokuapp.com/api/adv/move/",
    #         headers={'Authorization': api_key}).json()
    #         self.current_room = response
    #         sleep(response["cooldown"])
    #         return self.current_room


    # def transmogrify(self):
    #     response = requests.post("https://lambda-treasure-hunt.herokuapp.com/api/adv/transmogrify/",
    #     json= '{"name": "[NAME OF ITEM]"}', headers={'Authorization': api_key}).json()
    #     print(response)
    #     return response

ops = Task()
ops.wallet()
ops.status()



