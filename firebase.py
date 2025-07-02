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

