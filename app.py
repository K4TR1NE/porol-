from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(length, complexity):
    length = max(4, min(length, 50))

    chars = {
        'easy': string.ascii_lowercase,
        'medium': string.ascii_letters + string.digits,
        'hard': string.ascii_letters + string.digits + "!@#$%^&*"
       }

    return ''.join(random.choice(chars[complexity]) for _ in range(length))


@app.route('/', methods=['GET', 'POST'])
def index():
    passwords = []
    length = 12
    complexity = "medium"

    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        complexity = request.form.get('complexity', 'medium')
        # Генерируем 5 паролей
        passwords = [generate_password(length, complexity) for _ in range(5)]

    return render_template('index.html',
                           passwords=passwords,
                           length=length,
                           complexity=complexity)


if __name__ == '__main__':
    app.run(debug=True)
