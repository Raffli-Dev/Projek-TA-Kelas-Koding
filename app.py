from flask import Flask,redirect,url_for,render_template,request
import socket
from pymongo import MongoClient
from flask_wtf.csrf import CSRFProtect

client = MongoClient('localhost', 27017)
db = client['db_Projek']

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/kelas',methods=['GET'])
def Tentang(name_kelas):
    return render_template('kelasTersedia.html')

@app.route('/visi-misi',methods=['GET'])
def Syarat():
    return render_template('visiMisi.html')

@app.route('/',methods=['GET'])
def Contact():
    return render_template('stater-page.html')

@app.route('/login',methods=['GET'])
def Login():
    return render_template('/login/login.html')

@app.route("/check_login", methods=["POST"])
def login_check():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if email == 'admin@domain.com' and password == 'admin':
            return redirect(url_for('dashUser'))
        else:
            return redirect(url_for('Login'))
        
@app.route("/home",methods=['GET'])
def dashUser():
    return render_template('/dashUsers/dashUser.html')

@app.route('/register',methods=['GET'])
def Regiter():
    return render_template('/login/register.html')

@app.route("/regUsers/members",methods=['POST'])
def regMember():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        db.users.insert_one({
            'name': name,
            'email': email,
            'password': password
        })
        return redirect(url_for('Login'))

def generate_port(mulai_port):
    port = mulai_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:  
                return port  
            port += 1 

if __name__ == '__main__':
    mulai_port = 5000  
    port = generate_port(mulai_port)
    app.run(port=port, debug=True)
    print(f'Flask running di port {port}')