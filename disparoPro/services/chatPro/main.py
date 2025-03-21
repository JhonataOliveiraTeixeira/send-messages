import json
import pandas as pd
from services.chatPro.create_session import create_session
from services.chatPro.send_message import send_message
from services.chatPro.assing_label import assing_label
from services.chatPro.send_message_with_file import send_message_with_file
import db.sqlite
import time
import random

def start(instance):
    # Especifica que a coluna TELEFONE deve ser lida como string
    tabela = pd.read_excel(
        #Caminho do arquivo dentro da máquina, ou de onde estiver armazendo
        './base.xlsx',
        #Deve ser passado para string o telefone
        dtype={'TELEFONE': str}
    )
    db.sqlite.init()

    for linha in tabela.index:
        #Percorre o arquivo e mapeia das variavies para executar o disparo, seria bom implemetar funções assíncronas
        nome_cliente = tabela.loc[linha, 'var1']
        telefone = tabela.loc[linha, 'telefone']
        data_criacao = tabela.loc[linha, 'var2']
        data_criacao = tabela.loc[linha, 'var3']

        #Cria a sessão no chatPro
        response = create_session(str(telefone))
        if(response.status_code != 201):
            db.sqlite.insert_error(instance, nome_cliente, telefone, response.text)
            continue

        response_body = json.loads(response.text)

        id_session = response_body["id"]
        lead_id = response_body["lead_id"]

        response = assing_label(lead_id)
        if(response.status_code != 201):
            db.sqlite.insert_error(instance, nome_cliente, telefone, response.text)
            continue

        
        # result = send_message(id_session, nome_cliente, data_criacao)
        result = send_message(id_session)
        print(result.text)
        if(result.status_code != 200):
            db.sqlite.insert_error(instance, nome_cliente, telefone, response.text)
            continue
        
        # time.sleep(random.randint(8,15))
        if linha == 100 or linha == 200 or linha == 300:
            time.sleep(1800)
    print("Os contatos que houve erros foram:")
    errors = db.sqlite.view_errors(instance)
    return errors


