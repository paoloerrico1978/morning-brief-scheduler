import requests
import sys
import os

# ─── CREDENZIALI DA ENV (GitHub Actions secrets) ─────────
INSTANCE_ID = os.environ.get("GREEN_API_INSTANCE", "7107630046")
API_TOKEN = os.environ.get("GREEN_API_TOKEN", "2523aa736c424b70a30876baf58e384a0d2ad76c54114365b3")
GROUP_ID = os.environ.get("WA_GROUP_ID", "120363428668098354@g.us")
# ─────────────────────────────────────────────────────────

BRIEF_URL = "https://ai-morning.lovable.app/"

MESSAGGIO = f"""🤖 *Morning AI Brief — è online!*

L'intelligenza artificiale spiegata prima del caffè. ☕

👉 {BRIEF_URL}

_Buona giornata!_ 🚀"""


def send_whatsapp(message: str) -> bool:
    url = f"https://api.green-api.com/waInstance{INSTANCE_ID}/sendMessage/{API_TOKEN}"
    payload = {
        "chatId": GROUP_ID,
        "message": message
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "idMessage" in data:
            print(f"✅ Messaggio inviato! ID: {data['idMessage']}")
            return True
        else:
            print(f"❌ Risposta inattesa: {data}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Errore invio: {e}")
        return False


if __name__ == "__main__":
    print("📤 Invio Morning Brief al gruppo WA...")
    success = send_whatsapp(MESSAGGIO)
    sys.exit(0 if success else 1)
