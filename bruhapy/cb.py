import requests as req
import json

class Response(object):
  """The translation object"""
  def __init__(self,dictionary):
    self.res = dictionary['res']
    self.query = dictionary['query']

def cb(text):
    response = req.get(f'https://bruhapi.xyz/cb/{text}')
    rej = json.loads(response.text)
    return Response(rej)