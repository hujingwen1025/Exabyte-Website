from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/mslcTransfer/<path:mslcURL>')
def mslcTransfer(mslcURL):
    try:
        code = request.args.get('code')
        return redirect(str(mslcURL) + f'?code={code}')
    except:
        return "There was an error with the redirect URL. We don't know where to redirect you. Please return to the page you came from manually."

if __name__ == '__main__':
    app.run(debug=False, port=80, host='0.0.0.0')
