from django.test import TestCase

# Create your tests here.
import requests
import json

URL = 'http://127.0.0.1:8000/trainerapi/'

def post_record():
    data = {
    'name':'mohan',
    'address':'hyd',
    'mail':'mohan@gmail.com',
    'age':42
    }

    jsondata = json.dumps(data)
    headers={'content-Type':'application/json'}
    r = requests.post(url=URL,headers=headers,data=jsondata)
    data = r.json()
    print(data)

# post_record()

def get_record(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    jsondata = json.dumps(data)
    headers={'content-Type':'application/json'}
    r = requests.get(url=URL,headers=headers,data= jsondata)
    data = r.json()
    print(data)
    
# get_record()


def update_record():
    data = {
        'id':1,
        'name':'ganesh',
        'address':'sr nagar',
        'mail':'ganesh@gmail.com',
        'age':21
    }
    jsondata  =json.dumps(data)
    headers={'content-Type':'application/json'}
    r = requests.put(url=URL,headers=headers,data=jsondata)
    data = r.json()
    print(data)


# update_record()

def delete_record():
    data = {'id':1}
    jsondata = json.dumps(data)
    headers={'content-Type':'application/json'}
    r = requests.delete(url=URL,headers=headers,data = jsondata)
    data =  r.json()
    print(data)

delete_record()

