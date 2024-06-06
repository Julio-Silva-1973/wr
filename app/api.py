from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/materiais')
def materiais():
    return render_template('materiais.html')
 
@app.route('/empresa')
def empresa():
    return render_template('empresa.html')


if __name__ == "__main__":
    app.run(debug=True)