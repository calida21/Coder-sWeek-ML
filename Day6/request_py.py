# -*- coding: utf-8 -*-
"""request.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BtO0AD6aJkv8a9ShuR0Udr_s8u4J0wfu
"""

import requests

url = 'http://localhost:5000/predict_purchase'
r = requests.post(url,json={'Age':2, 'EstimatedSalary':9})

print(r.json())