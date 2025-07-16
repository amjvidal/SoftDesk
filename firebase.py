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
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Usuário criado:", user)
    except Exception as e:
        print("Erro ao criar usuário:", e)
        raise Exception("Email já cadastrado ou senha inválida.")

    try:
        auth.send_email_verification(user['idToken'])
    except KeyError:
        raise Exception("Token de autenticação não retornado pelo Firebase.")

    data = {
        "nome": nome,
        "email": email,
        "cpf": cpf,
        "matricula": matricula,
        "bio": bio,
        "tipo": "aluno"
    }
    db.child("usuarios").child(user['localId']).set(data)

def cadastroDocente(nome, email, password, cpf, ocupacao, bio):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Usuário docente criado:", user)
    except Exception as e:
        print("Erro ao criar usuário:", e)
        raise Exception("Email já cadastrado ou senha inválida.")

    try:
        auth.send_email_verification(user['idToken'])
    except KeyError:
        raise Exception("Token de autenticação não retornado pelo Firebase.")

    data = {
        "nome": nome,
        "email": email,
        "cpf": cpf,
        "ocupacao": ocupacao,
        "bio": bio,
        "tipo": "docente"
    }

    db.child("usuarios").child(user['localId']).set(data)
    
def loginfb(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        user_info = auth.get_account_info(user['idToken'])

        email_verified = user_info['users'][0]['emailVerified']

        if not email_verified:
            auth.send_email_verification(user['idToken'])
            return {
                'success': False,
                'message': 'E-mail não verificado. Verifique sua caixa de entrada.',
                'user': None
            }

        return {
            'success': True,
            'message': 'Login realizado com sucesso.',
            'user': user
        }

    except Exception as e:
        print("Erro ao fazer login:", e)
        return {
            'success': False,
            'message': 'Email ou senha inválidos.',
            'user': None
        }
        
def atualizarAluno(user_id, dados):
    try:
        db.child("usuarios").child(user_id).update(dados)
        print("Dados atualizados com sucesso.")
    except Exception as e:
        print("Erro ao atualizar dados:", e)
        raise Exception("Erro ao atualizar os dados do usuário.")
    


UPLOAD_FOLDER = os.path.join('uploads', 'perfil_fotos')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def salvarFotoPerfilLocal(user_id, foto_file):
    if not foto_file:
        raise Exception("Nenhum arquivo enviado.")

    filename = secure_filename(f"{user_id}.jpg")
    caminho_relativo = os.path.join('uploads', 'perfil_fotos', filename)
    caminho_completo = os.path.join(os.getcwd(), caminho_relativo)

    foto_file.save(caminho_completo)

    return f"/{caminho_relativo.replace(os.sep, '/')}"  # URL para uso no HTML

def criar_demanda(user_id, titulo, categoria, descricao):
    try:
        # Buscar o nome do usuário no banco de dados
        usuario_info = db.child("usuarios").child(user_id).get().val()
        nome_usuario = usuario_info.get("nome", "Usuário não encontrado")

        # Monta a demanda com o nome do usuário
        demanda = {
            "titulo": titulo,
            "categoria": categoria,
            "descricao": descricao,
            "usuario_id": user_id,
            "usuario_nome": nome_usuario,
            "data_criacao": datetime.now().isoformat()
        }

        db.child("demandas").push(demanda)
        print("Demanda criada com sucesso!")
    except Exception as e:
        print("Erro ao criar demanda:", e)
        raise Exception("Erro ao registrar a demanda.")
    
def get_todas_demandas():
    try:
        demandas_raw = db.child("demandas").get()
        demandas = []

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
        print("Erro ao buscar demandas:", e)
        return []
    
def get_demandas_do_usuario(user_id):
    try:
        demandas_raw = db.child("demandas").get()
        demandas = []

        if demandas_raw.each():
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
        print("Erro ao buscar demandas do usuário:", e)
        return []

def logout():
    from flask import session
    session.pop('user', None)
  
def recoverPassword(email):
  auth.send_password_reset_email(email)
  
  
  
def remove_pontos(texto):
  return texto.replace(".", "@")