#!/usr/bin/env python3
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Токены
TELEGRAM_TOKEN = "8228977740:AAGBCU376cZFLSa2uZ4NQfC5UE-et16Pyj4"

def send_message(chat_id, text):
    """Отправка сообщения в Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    
    try:
        response = requests.post(url, json=data, timeout=10)
        result = response.json()
        print(f"✅ Сообщение отправлено: {result.get('ok', False)}")
        return result
    except Exception as e:
        print(f"❌ Ошибка отправки: {e}")
        return {"ok": False, "error": str(e)}

@app.route("/webhook/telegram-webhook", methods=["POST"])
def telegram_webhook():
    """Обработка webhook от Telegram"""
    try:
        data = request.get_json()
        print(f"📨 Получено: {json.dumps(data, ensure_ascii=False, indent=2)}")
        
        # Проверяем наличие сообщения
        if "message" in data and "text" in data["message"]:
            message = data["message"]
            chat_id = message["chat"]["id"]
            user_text = message["text"]
            user_name = message["from"].get("first_name", "Клиент")
            
            print(f"👤 От {user_name} (ID: {chat_id}): {user_text}")
            
            # Формируем ответ
            if user_text.startswith("/start"):
                response_text = f"""Привет, {user_name}! 👋

Добро пожаловать в службу поддержки интернет-магазина подарков "Подарочный Мир"! 🎁

Я готов помочь с любыми вопросами о:
• Доставке и оплате
• Возврате товаров
• Ассортименте подарков
• Контактной информации

Просто напишите ваш вопрос!

---
💝 Команда поддержки "Подарочный Мир\""""
            else:
                response_text = f"""✅ Отлично, {user_name}!

Ваше сообщение "{user_text}" успешно получено магазином подарков "Подарочный Мир"! 

📞 Наши контакты:
• Телефон: +7 (800) 123-45-67
• Email: support@gift-world.ru
• Время: Пн-Пт 9:00-21:00

🎁 Спасибо за обращение!

---
💝 Команда поддержки "Подарочный Мир\""""
            
            # Отправляем ответ
            result = send_message(chat_id, response_text)
            print(f"📤 Результат: {result}")
            
        else:
            print("⚠️ Сообщение не содержит текста или некорректного формата")
        
        return jsonify({"status": "success", "message": "processed"})
        
    except Exception as e:
        print(f"❌ Ошибка в webhook: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/", methods=["GET"])
def health_check():
    """Проверка работоспособности"""
    return jsonify({
        "status": "running",
        "bot": "Gift Shop Support Bot",
        "version": "1.0",
        "webhook": "/webhook/telegram-webhook"
    })

if __name__ == "__main__":
    import os
    
    print("🚀 Запуск бота магазина подарков...")
    print("📡 Webhook endpoint: /webhook/telegram-webhook")
    print("🌐 Health check: /")
    
    # Для Render используем переменную окружения PORT
    port = int(os.environ.get("PORT", 8080))
    print(f"🏃 Запуск на порту {port}...")
    
    # Запускаем сервер
    app.run(host="0.0.0.0", port=port, debug=False)
