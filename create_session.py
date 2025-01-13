
import requests
from enviroment_variables import instanceId,token_instance


def create_session(number):

  url = "https://sparks.chatpro.com.br/sessions/getOrCreateByNumber"

  payload = {
      "instanceId": instanceId,
      "provider": "whatsapp",
       "number": number
  }
  headers = {
      "accept": "application/json",
      "instance-token": token_instance,
      "content-type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)


  return response