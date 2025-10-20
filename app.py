from flask import Flask, render_template, request, session, flash, redirect, url_for
import random
import string
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-0219'

USERS_FILE = 'users.json'


def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return [
                {'username': 'admin', 'password': 'admin', 'role': 'admin'},
                {'username': 'user', 'password': 'user', 'role': 'user'}
            ]
    else:
        return [
            {'username': 'admin', 'password': 'admin', 'role': 'admin'},
            {'username': 'user', 'password': 'user', 'role': 'user'}
        ]


def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


# Декоратор для проверки аутентификации
def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Пожалуйста, войдите в систему', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/')
def root():
    return redirect(url_for('login'))

# Маршруты аутентификации
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()
        user_found = False
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = user['username']
                session['role'] = user.get('role', 'user')
                flash(f'Добро пожаловать, {username}!', 'success')
                user_found = True
                return redirect(url_for('index'))

        if not user_found:
            flash('Неверное имя пользователя или пароль', 'error')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Валидация
        if not username or not password:
            flash('Все поля обязательны для заполнения', 'error')
            return render_template('register.html')

        if password != confirm_password:
            flash('Пароли не совпадают', 'error')
            return render_template('register.html')

        if len(username) < 3:
            flash('Имя пользователя должно содержать минимум 3 символа', 'error')
            return render_template('register.html')

        if len(password) < 4:
            flash('Пароль должен содержать минимум 4 символа', 'error')
            return render_template('register.html')

        users = load_users()

        # Проверка на существующего пользователя
        for user in users:
            if user['username'] == username:
                flash('Пользователь с таким именем уже существует', 'error')
                return render_template('register.html')

        # Добавление нового пользователя
        new_user = {
            'username': username,
            'password': password,
            'role': 'user'
        }
        users.append(new_user)
        save_users(users)

        flash('Регистрация прошла успешно! Теперь вы можете войти в систему.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('login'))


# Главный маршрут - ТОЛЬКО ОДИН РАЗ ОПРЕДЕЛЕН
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    passwords = []
    length = 12
    complexity = "medium"

    if request.method == 'POST':
        try:
            length = int(request.form.get('length', 12))
            length = max(4, min(length, 50))  # Ограничение длины
        except (ValueError, TypeError):
            length = 12

        complexity = request.form.get('complexity', 'medium')
        # Генерируем 5 паролей
        passwords = [generate_password(length, complexity) for _ in range(5)]

    return render_template('index.html',
                           passwords=passwords,
                           length=length,
                           complexity=complexity,
                           username=session.get('username'))


# Дополнительные защищенные маршруты (пример)
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
                           username=session.get('username'),
                           role=session.get('role'))


@app.route('/admin')
@login_required
def admin():
    if session.get('role') != 'admin':
        flash('У вас нет прав для доступа к этой странице', 'error')
        return redirect(url_for('index'))
    return render_template('admin.html', username=session.get('username'))


def generate_password(length, complexity):
    length = max(4, min(length, 50))

    chars = {
        'easy': string.ascii_lowercase,
        'medium': string.ascii_letters + string.digits,
        'hard': string.ascii_letters + string.digits + "!@#$%^&*"
    }

    # Проверяем, что complexity существует, иначе используем 'medium'
    if complexity not in chars:
        complexity = 'medium'

    return ''.join(random.choice(chars[complexity]) for _ in range(length))


if __name__ == '__main__':
    app.run(debug=True)
