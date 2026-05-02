# ---------------------------------------------------------
# Mercari JP Simple Scraper
# ---------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import time

class MercariScraper:
    def __init__(self):
        # 標準的なヘッダー
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        self.base_url = "https://jp.mercari.com/search"

    def search(self, keyword):
        """
        検索キーワードから商品一覧を取得する
        """
        print(f"[*] Searching for: {keyword}...")
        
        params = {"keyword": keyword}
        try:
            
            response = requests.get(self.base_url, params=params, headers=self.headers, timeout=10)
            
            if response.status_code == 403:
                print("[!] ERROR: Access Denied (403 Forbidden).")
                print("[!] Mercari's anti-bot system detected this request.")
                print("[!] Suggestion: Use MCGN API to bypass this block.")
                return []

            
            soup = BeautifulSoup(response.text, 'html.parser')
            # ...パース処理（省略）...
            
            return [{"name": "Sample Item", "price": "1200"}]
            
        except Exception as e:
            print(f"[!] Error occurred: {e}")
            return []

if __name__ == "__main__":
    scraper = MercariScraper()
    scraper.search("pikachu card")
