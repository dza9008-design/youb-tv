import json
from datetime import datetime, timedelta
import requests

# وظيفة جلب البيانات الحية للمباريات (البارحة، اليوم، الغد)
def fetch_matches():
    today = datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    
    print(f"[*] جاري جلب مباريات تواريخ: {yesterday}, {today}, {tomorrow}...")
    
    # [ملاحظة]: ضع هنا رابط الـ API أو السورس الذي تسحب منه المباريات فعلياً
    # كمثال افتراضي لهيكل البيانات الذي سيحفظ في matches.json:
    matches_data = {
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "yesterday": [],
        "today": [],
        "tomorrow": []
    }
    
    # يمكنك إضافة منطق السحب (Scraping/API Requests) هنا لملء القوائم
    
    with open('matches.json', 'w', encoding='utf-8') as f:
        json.dump(matches_data, f, ensure_ascii=False, indent=4)
    print("[+] تم تحديث matches.json بنجاح.")

# وظيفة جلب آخر الأخبار الرياضية
def fetch_news():
    print("[*] جاري جلب أحدث الأخبار الرياضية...")
    news_data = {
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "articles": [
            {
                "title": "تحديث تلقائي من منصة YOUB TV",
                "time": "الآن",
                "content": "تم جلب أحدث الأخبار والمباريات بنجاح في الخلفية."
            }
        ]
    }
    
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=4)
    print("[+] تم تحديث news.json بنجاح.")

if __name__ == "__main__":
    fetch_matches()
    fetch_news()
