# 🔐 Password Generator - Генератор Паролей

<div align="center">

!Python
!Flask

**Мощный генератор безопасных паролей на Flask**

</div>

## 🌟 О проекте

**Генератор паролей** — веб-приложение для создания надежных, безопасных паролей. Простой и интуитивно понятный интерфейс на русском языке.

## ✨ Возможности

### 🔧 Основные функции
- **Генерация нескольких паролей** — создавайте 5 паролей одновременно
- **Настройка длины** — от 4 до 50 символов
- **Уровни сложности** — простой, средний, сложный
- **Выбор типов символов**:
  - Прописные буквы (A-Z)
  - Цифры (0-9)
  - Специальные символы (!@#$%^&*)

## 🚀 Быстрый старт

### Установка и запуск

bash
# Клонирование репозитория
git clone https://github.com/your-username/password-generator.git
cd password-generator

# Создание виртуального окружения
python -m venv venv

# Активация окружения
# Linux/MacOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск приложения
python app.py

Приложение будет доступно по адресу: `http://localhost:5000`

### requirements.txt
Flask==2.3.3
WerkzОткройте## 🎮 Использование

1. **Выберитериложение в браузере
2. **ВыбеУстановитетво паролей (1-20)
3. **УВыберитедлину (8-64 символа)
4Нажмитее** уровень сложности
5. **Кликнитегенерировать пароли"
6. **Кликните** на любой пароль чтобы выделить его

### Уровни сложности
- **Простой**: Буквы и цифры
- **Средний**: Буквы, цифры, базовые символы
- **Сложный**: Все типы символов

## 📸 Скриншоты

### Главная страница
html
<form method="POST">
    <div class="input-group">
        <label for="length">Длина пароля</label>
        <input type="number" id="length" name="length" min="8" max="64" value="12">
    </div>
    <div class="input-group">
        <label>Уровень сложности</label>
        <div class="radio-group">
            <!-- Радиокнопки выбора сложности -->
        </div>
    </div>
    <button type="submit">Сгенерировать 5 паролей</button>
</form>

### Результаты генерации
html
{% if passwords %}
<div class="result">
    <h3>Сгенерированные пароли</h3>
    <div class="passwords-list">
    {% for password in passwords %}
    <div class="password-item">
        <input type="text" value="{{ password }}" readonly onclick="this.select()">
    </div>
    {% endfor %}
    </div>
</div>
{% endif %}

**Безопасность:**
- Модуль `secrets` для криптографически безопасной генерации
- Модуль `string` для работы с символами

## 🐳 Docker запуск

bash
docker build -t password-generator .
docker run -p 5000:5000 password-generator

## 🤝 Разработка

### Запуск для разработки
bash
export FLASK_ENV=development
flask run --debug
`
### Внесение изменений
1. Форкните репозиторий
2. Создайте ветку для функции (git checkout -b feature/AmazingFeature)
3. Закоммитьте изменения (git commit -m 'Add AmazingFeature')
4. Запушьте ветку (git push origin feature/AmazingFeature)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Смотрите файл LICENSE для подробностей.

## 👨‍💻 Автор

Ваше Имя
- GitHub: @your-username
- Email: your.email@example.com

---

<div align="center">

### ⭐ Не забудьте поставить звезду репозиторию!

*Если этот проект был полезен для вас, поставьте звезду ⭐ на GitHub!*

</div>
`

Просто скопируйте этот текст и вставьте в файл `README.md` в вашем репозитории GitHub. Не забудьте заменить `your-username` на ваш реальный GitHub username и добавить скриншоты в папку проекта.
