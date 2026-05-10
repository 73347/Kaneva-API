import requests
import time

def test_bybit():
    url = "https://api.bybit.com/v5/market/tickers?category=spot"
    print(f"[{time.strftime('%H:%M:%S')}] Тест Bybit API...")
    try:
        r = requests.get(url, timeout=10)
        print(f"  Статус: {r.status_code}")
        data = r.json()
        if data.get("retCode") == 0:
            print(f"  Первый тикер: {data['result']['list'][0]['symbol']} = {data['result']['list'][0]['lastPrice']}")
        print(f"  Скорость: {r.elapsed.total_seconds():.2f} сек")
    except Exception as e:
        print(f"  Ошибка: {e}")

if __name__ == "__main__":
    test_bybit()
