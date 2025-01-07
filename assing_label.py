import requests
import enviroment_variables


def assing_label(leadID):
  url = "https://sparks.chatpro.com.br/leads/assignLabel"

  payload = {
      "instanceId": enviroment_variables.instaceId,
      "leadId": leadID,
      "labelId": enviroment_variables.tagId
  }
  headers = {
      "accept": "application/json",
      "instance-token": enviroment_variables.token_instance,
      "content-type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)
  return response
