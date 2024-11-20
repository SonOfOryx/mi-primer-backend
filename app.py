from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery.html')
def projects():
    return render_template('gallery.html')

@app.route('/3D.html')
def Vr():
    return render_template('3D.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/HangMan.html')
def HangMan():
    return render_template('HangMan.html')

@app.route('/presentación.html')
def Presentations():
    return render_template('presentación.html')

@app.route('/index.html')
def IMS():
    return render_template('index.html')

@app.route('/PrimerRepo.html')
def Primero():
    return render_template('PrimerRepo.html')

@app.route('/MODEVA.html')
def MODEVA():
    return render_template('MODEVA.html')

if __name__ == '__main__':
    app.run(port=8000,debug=True)