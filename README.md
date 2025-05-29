# Django Online Store

## Опис

Це простий онлайн-магазин на Django з налаштованим CI/CD за допомогою GitHub Actions.

## Запуск локально

```bash
git clone <repo-url>
cd online_store
python -m venv env
source env/bin/activate  # або .\env\Scripts\activate на Windows
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
