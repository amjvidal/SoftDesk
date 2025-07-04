import pyrebase

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
  
def recoverPassword(email):
  auth.send_password_reset_email(email)
  
  
  
def remove_pontos(texto):
  return texto.replace(".", "@")