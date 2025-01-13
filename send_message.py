import requests
import enviroment_variables

def send_message(sessionId):
  url = "https://sparks.chatpro.com.br/messages/sendMessage"

  payload = {
      "sessionId": sessionId,
      "instanceId": enviroment_variables.instanceId,
      "provider": "whatsapp",
      "message": f'''
'''
  }
  headers = {
      "accept": "application/json",
      "instance-token": enviroment_variables.token_instance,
      "content-type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)

  return response
