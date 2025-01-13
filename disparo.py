import json
import pandas as pd
from create_session import create_session
from send_message import send_message
from assing_label import assing_label
from send_message_with_file import send_message_with_file
import time
import random

def pega_telefone():
    # Especifica que a coluna TELEFONE deve ser lida como string
    tabela = pd.read_csv(
        #Caminho do arquivo dentro da máquina, ou de onde estiver armazendo
        '',
        #Deve ser passado para string o telefone
        dtype={'TELEFONE': str}
    )

    for linha in tabela.index:
        #Percorre o arquivo e mapeia das variavies para executar o disparo, seria bom implemetar funções assíncronas
        nome_cliente = tabela.loc[linha, 'NOME DO USUARIO']
        telefone = tabela.loc[linha, 'TELEFONE']
        data_criacao = tabela.loc[linha, 'DATA INICIO']

        #Cria a sessão no chatPro
        response = create_session(str(telefone))
        if(response.status_code != 201):
            continue

        response_body = json.loads(response.text)

        id_session = response_body["id"]
        lead_id = response_body["lead_id"]

        assing_label(lead_id)

        
        # result = send_message(id_session, nome_cliente, data_criacao)
        result = send_message(id_session)
        print(result.text)
        if(result.status_code != 200):
            continue
        
        time.sleep(random.randint(8,15))
        if linha == 100 or linha == 200 or linha == 300:
            time.sleep(1800)

pega_telefone()
