import requests
import json
import time

def test_coingecko():
    url = "https://api.coingecko.com/api/v3/ping"
    print(f"[{time.strftime('%H:%M:%S')}] Тест CoinGecko API...")
    try:
        r = requests.get(url, timeout=10)
        print(f"  Статус: {r.status_code}")
        print(f"  Ответ: {r.json()}")
        print(f"  Скорость: {r.elapsed.total_seconds():.2f} сек")
    except Exception as e:
        print(f"  Ошибка: {e}")

if __name__ == "__main__":
    test_coingecko()
