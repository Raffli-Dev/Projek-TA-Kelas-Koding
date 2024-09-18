from flask import Flask,redirect,url_for,render_template,request
import socket

app=Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/kelas-tersedia',methods=['GET'])
def Tentang():
    return render_template('kelasTersedia.html')

@app.route('/visi-misi',methods=['GET'])
def Syarat():
    return render_template('visiMisi.html')

@app.route('/',methods=['GET'])
def Contact():
    return render_template('stater-page.html')

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