import requests as req
import json

class Translation(object):
  """The translation object"""
  def __init__(self,dictionary):
    self.lang = dictionary['lang']
    self.tr = dictionary['text']
    self.original = dictionary['original']

def translate(text):
    response = req.get(f'https://bruhapi.xyz/translate/{text}')
    rej = json.loads(response.text)
    return Translation(rej)