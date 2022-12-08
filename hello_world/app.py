import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function"""
    a=event['a']
    b=event['b']

    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b