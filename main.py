from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    if request.values:
        answer = eval(request.values.get('command'))
        return str(answer)
    return render_template('index.html')


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080, debug=True)
