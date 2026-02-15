from django.test import TestCase

# Create your tests here.
import requests

URL = 'http://127.0.0.1:8000/emp/2'

r = requests.get(url=URL)
emp_data = r.json()
print(emp_data)
