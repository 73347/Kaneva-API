import requests
import time

def test_cryptocompare():
    api_key = "54c69a67adfc783963d3589c5a08a40a5d123b10bcab93b3b4b1eebf10c5b65e"
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    headers = {"authorization": f"Apikey {api_key}"}
    print(f"[{time.strftime('%H:%M:%S')}] Тест CryptoCompare API...")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        print(f"  Статус: {r.status_code}")
        print(f"  Ответ: {r.json()}")
        print(f"  Скорость: {r.elapsed.total_seconds():.2f} сек")
    except Exception as e:
        print(f"  Ошибка: {e}")

if __name__ == "__main__":
    test_cryptocompare()
