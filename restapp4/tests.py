from django.test import TestCase

# Create your tests here.
import requests
import json

URL = 'http://127.0.0.1:8000/employee/'

def post_record():
    data = {
    'name':'skishore',
    'address':'hyd',
    'mail':'kishore@gmail.com',
    'age':25
    }

    jsondata = json.dumps(data)
    r = requests.post(url=URL,data=jsondata)
    data = r.json()
    print(data)

post_record()

def get_record(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    jsondata = json.dumps(data)
    r = requests.get(url=URL,data= jsondata)
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
    r = requests.put(url=URL,data=jsondata)
    data = r.json()
    print(data)


# update_record()

def delete_record():
    data = {'id':1}
    jsondata = json.dumps(data)
    r = requests.delete(url=URL,data = jsondata)
    data =  r.json()
    print(data)

# delete_record()

