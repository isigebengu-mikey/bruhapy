import requests as req
import json

def joke(text):
    response = req.get(f'https://bruhapi.xyz/cb/{text}')
    rej = json.loads(response.text)
    return rej['res']