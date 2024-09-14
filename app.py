from flask import Flask,redirect,url_for,render_template,request

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


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)