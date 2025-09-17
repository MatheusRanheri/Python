from flask import Flask, request, jsonify
import function_calculos as calc

app = Flask(__name__)

@app.route("/soma")
def soma():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify(resultado=calc.soma(a, b))

@app.route("/subtrair")
def subtrair():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify(resultado=calc.subtrair(a, b))

@app.route("/multiplicar")
def multiplicar():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify(resultado=calc.multiplicar(a, b))

@app.route("/dividir")
def dividir():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify(resultado=calc.dividir(a, b))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)