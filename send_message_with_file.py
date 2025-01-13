import requests
import enviroment_variables

def send_message_with_file(sessionId):
  url = "https://sparks.chatpro.com.br/messages/sendFileFromUrl"  

  payload = {
      "sessionId": sessionId,
      "instanceId": enviroment_variables.instanceId,
      "url": enviroment_variables.fileURL,
      "provider": "whatsapp",
      "caption": f'''
'''
  }
  headers = {
      "accept": "application/json",
      "instance-token": enviroment_variables.token_instance,
      "content-type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)

  return response
