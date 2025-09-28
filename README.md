# 🎁 Telegram Bot для магазина подарков

## 📋 Описание
Telegram бот для службы поддержки интернет-магазина подарков "Подарочный Мир".

## 🚀 Быстрый старт на Render

### 1. Регистрация
- Идите на https://render.com
- Войдите через GitHub

### 2. Создание Web Service
- New + → Web Service
- Environment: **Python 3**
- Build Command: `pip install -r requirements.txt`
- Start Command: `python simple_bot.py`

### 3. Переменные окружения
Добавьте в Environment Variables:
```
TELEGRAM_TOKEN = 8228977740:AAGBCU376cZFLSa2uZ4NQfC5UE-et16Pyj4
```

### 4. После деплоя
Обновите webhook (замените URL):
```bash
curl -X POST "https://api.telegram.org/bot8228977740:AAGBCU376cZFLSa2uZ4NQfC5UE-et16Pyj4/setWebhook" \
  -d "url=https://ваш-url.onrender.com/webhook/telegram-webhook"
```

## ✅ Готово!
Бот будет работать 24/7 на Render!
