from django.test import TestCase

# Create your tests here.
import requests
import json

URL = 'http://127.0.0.1:8000/manager/'

def post_record():
    data = {
    'name':'sai',
    'address':'hyderabad',
    'mail':'sai@gmail.com',
    'age':33
    }

    jsondata = json.dumps(data)
    r = requests.post(url=URL,data=jsondata)
    data = r.json()
    print(data)

# post_record()

def get_record(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    jsondata = json.dumps(data)
    r = requests.get(url=URL,data= jsondata)
    data = r.json()
    print(data)
    
get_record(1)


def update_record():
    data = {
        'id':1,
        'name':'rajesh',
        'address':'sr nagar',
        'mail':'rajesh@gmail.com',
        'age':30
    }
    jsondata  =json.dumps(data)
    r = requests.put(url=URL,data=jsondata)
    data = r.json()
    print(data)


# update_record()

def delete_record():
    data = {'id':2}
    jsondata = json.dumps(data)
    r = requests.delete(url=URL,data = jsondata)
    data =  r.json()
    print(data)

# delete_record()

