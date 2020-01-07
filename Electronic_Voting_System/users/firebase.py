import pyrebase

config = {
    'apiKey': "AIzaSyA-67sjYXQyNFSSs1S5oJbLRMroGw1Y4AI",
    'authDomain': "electronic-voting-system-ae9ff.firebaseapp.com",
    'databaseURL': "https://electronic-voting-system-ae9ff.firebaseio.com",
    'projectId': "electronic-voting-system-ae9ff",
    'storageBucket': "electronic-voting-system-ae9ff.appspot.com",
    'messagingSenderId': "208439755365",
    'appId': "1:208439755365:web:4f5f97bfd04cb64f243c8c",
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()
