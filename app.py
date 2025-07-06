from flask import Flask, request

app = Flask(__name__)

@app.route('/mslcTransfer/<path:mslcURL>')
def mslcTransfer(mslcURL):
    try:
        code = str(request.args.get('code'))
        return redirect(str(mslcURL) + f'?code={code}')
    except:
        return "There was an error with the redirect URL. We don't know where to redirect you. Please return to the page you came from manually."

if __name__ == '__main__':
    app.run(debug=False, port=80, host='0.0.0.0')
