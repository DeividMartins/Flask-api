from flask import Flask, jsonify, request

app = Flask(__name__);

@app.route("/", methods=['GET', 'POST'])
def ola():
    return 'Olá mundo!'

@app.route('/parametro/<int:numero>/')
def parametro(numero):
    print(numero)
    return 'Olá mundo! {}'.format(numero)

@app.route('/parametro/<int:numero1>/<int:numero2>/')
def soma(numero1, numero2):
 
    return jsonify({'A soma dos valores {} e {}:'.format(numero1, numero2): numero1 + numero2})

@app.route('/usuario', methods=['POST'])
def postUsuario():
    usuario = request.data
    return (usuario)

if __name__ == "__main__":
    app.run(debug=True)




