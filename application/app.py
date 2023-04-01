import mathtools.functions as functions
from flask import Flask, request, jsonify

def create_app(config_file=None):
    app = Flask(__name__, config_file)
    return app

app = create_app()

def math_fun_request_handler(request, func):
    try:
        lhs = request.args.get("lhs")
        rhs = request.args.get("rhs")
        if not lhs or not rhs:
            raise ValueError("Provide 'lhs' and 'rhs' parameters in request")
        result = func(float(lhs), float(rhs))
        return jsonify({
            "result": result
        })
    except (TypeError, ValueError) as e:
        return jsonify({
            "error": str(e)
        }), 400

@app.route("/api/sub")
def sub():
    return math_fun_request_handler(request, functions.sub)

@app.route("/api/multiply")
def multiply():
    return math_fun_request_handler(request, functions.multiply)

@app.route("/api/divide")
def divide():
    return math_fun_request_handler(request, functions.divide)

if __name__ == "__main__":
    app.run()