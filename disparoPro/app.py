from flask import Flask, render_template, send_file, session
from werkzeug.utils import secure_filename
from flask import request
from services.chatPro.main import start as dispachStart
from db.sqlite import close_db
import os

app = Flask(__name__)

# Rota principal
@app.route("/")
def hello_world():
    return render_template('index.html', person="name")

# Rota para download do arquivo Excel
@app.route('/download-csv')
def download_csv():
    # Caminho relativo ao arquivo Excel
    caminho_arquivo = './base.xlsx'
    return send_file(caminho_arquivo, as_attachment=True)

# Configurações
UPLOAD_FOLDER = './services/chatPro'  # Pasta onde os arquivos serão salvos
ALLOWED_EXTENSIONS = {'xlsx'}  # Extensões permitidas

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Verifica se a extensão do arquivo é permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 

# Rota para upload de arquivos
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Verifica se o arquivo foi enviado
        if 'the_file' not in request.files:
            return "Nenhum arquivo enviado", 400

        file = request.files['the_file']

        # Verifica se o arquivo tem um nome válido
        if file.filename == '':
            return "Nome do arquivo inválido", 400

        # Verifica se a extensão é permitida
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Garante um nome de arquivo seguro
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Salva o arquivo
        else:
            return "Extensão de arquivo não permitida", 400

    # Exibe o formulário de upload (GET)
    return render_template('upload.html')

@app.route('/start')
def start():
    instance = session.get('instance', 'Nenhum nome definido')
    dispachStart(instance)
    return "Disparo iniciado com sucesso!"
    

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(
        debug=True,          # Ativa o modo de depuração
        port=5000,           # Define a porta
        use_reloader=True    # Recarrega o servidor automaticamente
    )
app.teardown_appcontext(close_db)