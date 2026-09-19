# Biz499 DRF Lead Webhook

Endpoint:
POST /api/leads/webhook/

Expected Authorization header:
Bearer <value of DRF_WEBHOOK_TOKEN>

The token is configured in `.env`, not hard-coded in Django source.

## Local setup

1. Create and activate a virtual environment.
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Set `DRF_WEBHOOK_TOKEN` to your own long random secret.
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py createsuperuser`
8. `python manage.py runserver`

## Node.js bot

Set the same token in your Node project:

const DRF_API_TOKEN = "Bearer YOUR_SAME_TOKEN";

Keep the token secret and do not commit `.env` or real tokens to Git.
