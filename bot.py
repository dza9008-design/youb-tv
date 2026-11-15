from datetime import datetime, timedelta
import json
import os


def fetch_matches():
  print("[*] جاري توليد جدول المباريات المتوافق مع الواجهة...")

  # حساب التواريخ بدقة مطابقة لما يبحث عنه الموقع
  today = datetime.now().strftime("%Y-%m-%d")
  yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
  tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

  # الهيكل المدعوم بالكامل بواسطة صفحة العرض
  matches_data = {
      "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "dates": {"yesterday": yesterday, "today": today, "tomorrow": tomorrow},
      "matches": {
          # مباريات الأمس
          yesterday: [
              {
                  "time": "21:00",
                  "competition": "تصفيات كأس أمم أفريقيا",
                  "stadium": "ملعب الشهداء",
                  "home_team": "الجزائر",
                  "away_team": "توجو",
                  "home_flag": "🇩🇿",
                  "away_flag": "🇹🇬",
                  "score": "1 - 0",
                  "status": "انتهت",
                  "channel": "بي إن سبورت 1",
                  "commentator": "حاج عيسى",
              }
          ],
          # مباريات اليوم (تاريخ اليوم الحقيقي لكي تظهر تلقائياً)
          today: [
              {
                  "time": "20:00",
                  "competition": "الدوري الإسباني - كلاسيكو الأرض",
                  "stadium": "سانتياغو برنابيو",
                  "home_team": "ريال مدريد",
                  "away_team": "برشلونة",
                  "home_flag": "🇪🇸",
                  "away_flag": "🇪🇸",
                  "score": "1 - 2",
                  "status": "الشوط الثاني",
                  "channel": "بي إن سبورت 2",
                  "commentator": "عصام الشوالي",
              }
          ],
          # مباريات الغد
          tomorrow: [
              {
                  "time": "21:00",
                  "competition": "دوري أبطال أوروبا",
                  "stadium": "أنفيلد",
                  "home_team": "ليفربول",
                  "away_team": "ريال مدريد",
                  "home_flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
                  "away_flag": "🇪🇸",
                  "score": "0 - 0",
                  "status": "قريباً",
                  "channel": "بي إن سبورت 1",
                  "commentator": "حفيظ دراجي",
              }
          ],
      },
  }

  with open("matches.json", "w", encoding="utf-8") as f:
    json.dump(matches_data, f, ensure_ascii=False, indent=4)
  print("[+] تم تحديث matches.json بنجاح بالتواريخ المتطابقة.")


def fetch_news():
  news_data = {
      "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "articles": [
          {
              "title": (
                  "المنتخب الجزائري يواصل تحضيراته بقوة وبتركيز كبير من اللاعبين"
              ),
              "time": datetime.now().strftime("%H:%M"),
              "content": (
                  "تحديث آلي عبر نظام YOUB TV الذكي لجلب آخر المستجدات"
                  " الرياضية."
              ),
          }
      ],
  }

  with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news_data, f, ensure_ascii=False, indent=4)
  print("[+] تم تحديث news.json بنجاح.")


if __name__ == "__main__":
  fetch_matches()
  fetch_news()
