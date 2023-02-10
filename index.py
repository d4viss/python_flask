from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def main():
    return "Hola soy davison"

@app.route('/contacto')
def contacto():
    return "esta es la pagina de contacto"
"""

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lenguajes')
def lenguajes():
    misLenguajes = ("PHP", "python", "Java", "C#", "JavaScrpt", "Perl", "Ruby", "Rust")
    return render_template('lenguajes.html', lenguajes = misLenguajes)

if __name__ == '__main__':
    app.run(debug = True)