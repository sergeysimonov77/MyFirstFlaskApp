
#pip install flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    res = '''
    <!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title></title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
 <a href="https://google.com">Гугл</a><br><br>
 <a href="https://yandex.ru">Яндекс</a>
 <img src="https://i.playground.ru/p/1h0LXc77AbN5FT1bDDCCFA.jpeg">
</body>
</html>
    '''
    return res

@app.route('/first/')
def first():
    return 'Первый'

@app.route('/second/')
def second():
    return 'Второй'


if __name__ == "__main__":
    app.run()