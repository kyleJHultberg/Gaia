class Body():
    def __init__(self):
        pass

    def createViewsDotPy(self):
        return """
from www import app
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def store():
    return render_template('index.html')
"""

    def createInitDotPy(self):
        return """
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MYSECRETKEY'

from .views import views

app.register_blueprint(views, url_prefix='/')
"""

    def createIndexDotHtml(self):
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
"""

    def createMainDotPy(self):
        return """
from www import app

if __name__ == '__main__':
    app.run(debug=True)
"""