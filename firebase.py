import pyrebase
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import tempfile

""""
firebaseConfig = {
  apiKey: "AIzaSyB6LXA-AbX4dweDjoYgH5Ljk8tKEhaNJl8",
  authDomain: "softdesk-9077d.firebaseapp.com",
  projectId: "softdesk-9077d",
  storageBucket: "softdesk-9077d.firebasestorage.app",
  messagingSenderId: "898489415204",
  appId: "1:898489415204:web:53c4c24cfd2f95db7d4ab1",
  measurementId: "G-LTPH6KRP65"
}
"""

config = {
  "apiKey": "AIzaSyB6LXA-AbX4dweDjoYgH5Ljk8tKEhaNJl8",
  "authDomain": "softdesk-9077d.firebaseapp.com",
  "databaseURL": "https://softdesk-9077d-default-rtdb.firebaseio.com/",
  "storageBucket": "softdesk-9077d.firebasestorage.app",    
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()
db = firebase.database()

def cadastroAluno(nome, email, password, cpf, matricula, bio):
    """
     cadastroAluno()
     -----
     Realiza o cadastro de um novo aluno no sistema. Isso envolve a criação de um usuário
     no Firebase Authentication e o armazenamento dos dados adicionais do aluno
     no Realtime Database.
    """
    try:
        # Tenta criar um novo usuário no Firebase Authentication com e-mail e senha fornecidos.
        user = auth.create_user_with_email_and_password(email, password)
        print("Usuário criado:", user)
    except Exception as e:
        """
        Em caso de erro na criação do usuário (ex: e-mail já cadastrado, senha fraca),
        imprime o erro e levanta uma exceção para ser tratada pela função chamadora.
        """
        print("Erro ao criar usuário:", e)
        raise Exception("Email já cadastrado ou senha inválida.")

    try:
        """
        Tenta enviar um e-mail de verificação para o usuário recém-criado.
        O 'idToken' é necessário para autenticar a solicitação de verificação.
        """
        auth.send_email_verification(user['idToken'])
    except KeyError:
        """
        Corrige: Verifica se o 'idToken' não foi retornado pelo Firebase,
        o que impediria o envio do e-mail de verificação.
        """
        raise Exception("Token de autenticação não retornado pelo Firebase.")
    
    # Prepara os dados adicionais do aluno para serem armazenados no Realtime Database.
    data = {
        "nome": nome,
        "email": email,
        "cpf": cpf,
        "matricula": matricula,
        "bio": bio,
        "tipo": "aluno"
    }
    """
    Armazena os dados do aluno no nó "usuarios" do Realtime Database,
    usando o 'localId' (UID do usuário no Firebase Authentication) como chave.
    """
    db.child("usuarios").child(user['localId']).set(data)

def cadastroDocente(nome, email, password, cpf, ocupacao, bio):
    """
    cadastroDocente()
    -----
    Realiza o cadastro de um novo docente no sistema, que inclui a criação de um usuário
    no Firebase Authentication e o armazenamento de seus dados adicionais
    no Realtime Database.
    """
    try:
        # Tenta criar um novo usuário no Firebase Authentication com o e-mail e senha fornecidos.
        user = auth.create_user_with_email_and_password(email, password)
        print("Usuário docente criado:", user)
    except Exception as e:
        """
        Em caso de falha na criação do usuário (ex: e-mail já existente, senha inadequada),
        imprime a mensagem de erro e propaga uma exceção.
        """
        print("Erro ao criar usuário:", e)
        raise Exception("Email já cadastrado ou senha inválida.")

    try:
        """
        Tenta enviar um e-mail de verificação para o usuário recém-criado,
        utilizando o 'idToken' para autenticação da requisição.
        """
        auth.send_email_verification(user['idToken'])
    except KeyError:
        """
        Corrige: Caso o 'idToken' não seja retornado pelo Firebase,
        impede o envio do e-mail de verificação e levanta uma exceção.
        """
        raise Exception("Token de autenticação não retornado pelo Firebase.")
    """
    Prepara um dicionário com os dados específicos do docente para serem salvos
    no Realtime Database.
    """
    data = {
        "nome": nome,
        "email": email,
        "cpf": cpf,
        "ocupacao": ocupacao,
        "bio": bio,
        "tipo": "docente"
    }
    """
    Armazena os dados do docente no nó "usuarios" do Realtime Database.
    O 'localId' do usuário no Firebase Authentication é usado como a chave única para este registro.
    """
    db.child("usuarios").child(user['localId']).set(data)
    
def loginfb(email, password):
    """
    loginfb()
    -----
    Tenta autenticar um usuário usando e-mail e senha no Firebase Authentication.
    Após a autenticação, verifica se o e-mail do usuário foi verificado.
    Se não for verificado, solicita o envio de um e-mail de verificação novamente.
    """
    try:
        # Tenta fazer login com o e-mail e senha fornecidos.
        user = auth.sign_in_with_email_and_password(email, password)
        # Obtém informações detalhadas da conta do usuário usando o ID Token.
        user_info = auth.get_account_info(user['idToken'])

        # Verifica o status de verificação do e-mail do usuário.
        email_verified = user_info['users'][0]['emailVerified']

        """
        Se o e-mail não estiver verificado, envia um novo e-mail de verificação
        e retorna uma mensagem indicando o status.
        """
        if not email_verified:
            auth.send_email_verification(user['idToken'])
            return {
                'success': False,
                'message': 'E-mail não verificado. Verifique sua caixa de entrada.',
                'user': None
            }
        # Se o login for bem-sucedido e o e-mail verificado, retorna sucesso.
        return {
            'success': True,
            'message': 'Login realizado com sucesso.',
            'user': user
        }

    except Exception as e:
        """
        Em caso de qualquer erro durante o processo de login (ex: credenciais inválidas),
        imprime o erro e retorna uma mensagem de falha.
        """
        
        print("Erro ao fazer login:", e)
        return {
            'success': False,
            'message': 'Email ou senha inválidos.',
            'user': None
        }
        
def atualizarAluno(user_id, dados):
    """ 
    atualizarAluno()
    -----
    Atualiza os dados de um aluno existente no Realtime Database do Firebase.
    Esta função recebe o ID do usuário e um dicionário com os dados a serem atualizados.
    """
    try:
        """
        Acessa o nó 'usuarios' no Realtime Database, seleciona o filho com o 'user_id' fornecido,
        e então utiliza o método 'update' para aplicar as alterações contidas no dicionário 'dados'.
        O método 'update' é ideal para modificar campos específicos sem sobrescrever o documento inteiro.
        """
        db.child("usuarios").child(user_id).update(dados)
        print("Dados atualizados com sucesso.")
    except Exception as e:
        """
        Captura qualquer exceção que ocorra durante o processo de atualização dos dados.
        Imprime o erro para depuração interna e levanta uma nova exceção genérica
        para ser tratada pela camada superior da aplicação, fornecendo uma mensagem mais amigável.
        """
        print("Erro ao atualizar dados:", e)
        raise Exception("Erro ao atualizar os dados do usuário.")
    

"""
UPLOAD_FOLDER = os.path.join('uploads', 'perfil_fotos')
-----
Define o caminho completo para a pasta onde as fotos de perfil serão armazenadas.
'os.path.join' é usado para construir caminhos de forma segura e compatível com diferentes sistemas operacionais.
"""
UPLOAD_FOLDER = os.path.join('uploads', 'perfil_fotos')
"""
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
-----
Cria o diretório especificado em UPLOAD_FOLDER se ele ainda não existir.
O parâmetro 'exist_ok=True' evita que um erro seja levantado caso a pasta já exista,
garantindo que a operação seja idempotente (pode ser executada múltiplas vezes sem efeitos colaterais indesejados após a primeira execução).
"""
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def salvarFotoPerfilLocal(user_id, foto_file):
    """
    salvarFotoPerfilLocal()
    -----
    Salva uma foto de perfil no sistema de arquivos local do servidor.
    O nome do arquivo é padronizado usando o ID do usuário para garantir unicidade.
    Retorna o caminho relativo da imagem para uso em URLs HTML.
    """
    if not foto_file:
        """
        Verifica se um arquivo de foto foi realmente enviado.
        Caso contrário, levanta uma exceção indicando a ausência do arquivo.
        """
        raise Exception("Nenhum arquivo enviado.")
    """
    Gera um nome de arquivo seguro para evitar problemas de segurança e padronização.
    Utiliza o user_id como base para o nome do arquivo, garantindo que cada usuário
    tenha um nome de arquivo de foto de perfil único (ex: 'user123.jpg').
    """
    filename = secure_filename(f"{user_id}.jpg")
    """
    Constrói o caminho relativo completo onde a foto será armazenada.
    'os.path.join' é usado para compatibilidade com diferentes sistemas operacionais.
    O caminho será algo como 'uploads/perfil_fotos/user_id.jpg'.
    """

    caminho_relativo = os.path.join('uploads', 'perfil_fotos', filename)

    """
    Constrói o caminho completo (absoluto) para salvar o arquivo no sistema de arquivos.
    'os.getcwd()' obtém o diretório de trabalho atual do script.
    """
    caminho_completo = os.path.join(os.getcwd(), caminho_relativo)
    
    # Salva o arquivo de foto no caminho completo especificado.
    foto_file.save(caminho_completo)
    """
    Retorna o caminho relativo da imagem formatado para ser usado como URL em HTML.
    'replace(os.sep, '/')' garante que as barras sejam sempre para a frente (/)
    para compatibilidade com URLs, independentemente do sistema operacional.
    """
    return f"/{caminho_relativo.replace(os.sep, '/')}"  # URL para uso no HTML

def criar_demanda(user_id, titulo, categoria, descricao):
    """
    criar_demanda()
    -----
    Cria uma nova demanda no banco de dados, associando-a a um usuário específico.
    Inclui o nome do usuário e a data de criação da demanda.
    """
    try:
        """
        Busca as informações do usuário no nó 'usuarios' do Realtime Database
        usando o 'user_id' fornecido.
        """
        usuario_info = db.child("usuarios").child(user_id).get().val()
        #Extrai o nome do usuário. Se o nome não for encontrado, define um valor padrão.
        nome_usuario = usuario_info.get("nome", "Usuário não encontrado")

        """
        Monta um dicionário com os detalhes da nova demanda.
        Inclui título, categoria, descrição, ID e nome do usuário criador,
        além da data e hora atuais no formato ISO 8601.
        """
        demanda = {
            "titulo": titulo,
            "categoria": categoria,
            "descricao": descricao,
            "usuario_id": user_id,
            "usuario_nome": nome_usuario,
            "data_criacao": datetime.now().isoformat()
        }
        """
        Envia a nova demanda para o nó 'demandas' no Realtime Database.
        O método 'push()' cria uma nova chave única para cada demanda,
        o que é ideal para listas de itens.
        """
        db.child("demandas").push(demanda)
        print("Demanda criada com sucesso!")
    except Exception as e:
        """
        Captura qualquer erro que ocorra durante o processo de criação da demanda.
        Imprime o erro para depuração e levanta uma exceção genérica para a camada superior.
        """
        print("Erro ao criar demanda:", e)
        raise Exception("Erro ao registrar a demanda.")
    
def get_todas_demandas():
    """
    get_todas_demandas()
    -----
    Busca e retorna todas as demandas registradas no banco de dados.
    Para cada demanda, formata a data de criação e adiciona o nome e ocupação do usuário.
    """
    try:
        # Recupera todos os dados do nó "demandas" do Firebase Realtime Database.
        demandas_raw = db.child("demandas").get()
        demandas = []
        
        # Verifica se há demandas para iterar. O método 'each()' retorna um iterador de objetos Firebase.
        if demandas_raw.each():
            for item in demandas_raw.each():
                dados = item.val()
                dados['id'] = item.key()

                # Formata data
                data = datetime.fromisoformat(dados.get('data_criacao', datetime.now().isoformat()))
                dados['data_formatada'] = data.strftime('%d/%m/%y')

                # Busca nome e ocupação do usuário
                usuario = db.child("usuarios").child(dados['usuario_id']).get().val()
                dados['nome'] = usuario.get('nome', 'Desconhecido')
                dados['ocupacao'] = usuario.get('ocupacao', 'Usuário')

                demandas.append(dados)
        return demandas
    except Exception as e:

        # Em caso de erro na busca das demandas, imprime o erro e retorna uma lista vazia.        
        print("Erro ao buscar demandas:", e)
        return []
    
def get_demandas_do_usuario(user_id):
    """get_demandas_do_usuario()
    -----
    Busca e retorna todas as demandas criadas por um usuário específico.
    Para cada demanda encontrada, formata a data de criação.
    """
    try:
        # Recupera todas as demandas do banco de dados.        
        demandas_raw = db.child("demandas").get()
        demandas = []

        if demandas_raw.each():
        # Verifica se há demandas para iterar.            
            for item in demandas_raw.each():
                dados = item.val()
                if dados.get('usuario_id') == user_id:
                    dados['id'] = item.key()

                    # Formatar data
                    data = datetime.fromisoformat(dados.get('data_criacao', datetime.now().isoformat()))
                    dados['data_formatada'] = data.strftime('%d/%m/%y')

                    demandas.append(dados)

        return demandas
    except Exception as e:
        # Em caso de erro na busca das demandas do usuário, imprime o erro e retorna uma lista vazia.        
        print("Erro ao buscar demandas do usuário:", e)
        return []

def logout():
    """
    logout()
    -----
    Realiza o logout do usuário, removendo a informação da sessão.    
    """
    from flask import session
    session.pop('user', None)
  
def recoverPassword(email):
  """
    recoverPassword()
    -----
    Envia um e-mail de redefinição de senha para o endereço de e-mail fornecido  
  """
  auth.send_password_reset_email(email)
  
  
  
def remove_pontos(texto):
  """
    remove_pontos()
    -----
    Substitui todos os pontos ('.') em uma string pelo caractere arroba ('@').
  """
  return texto.replace(".", "@")