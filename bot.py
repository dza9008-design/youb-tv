import json
import os
import time
import requests
from bs4 import BeautifulSoup
import schedule

def update_youb_tv_pro():
    print("\n[⏳] جاري تحديث بيانات موقع YOUB TV باحترافية...")

    # جدول المباريات الغني والمتنوع (أمس، اليوم، الغد)
    full_schedule = {
        "yesterday": [
            {
                "id": "m_y1",
                "title": "دوري أبطال أوروبا - الجولة المجموعات",
                "stadium": "أنفيلد",
                "team1": "ليفربول",
                "team1Logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
                "team2": "ريال مدريد",
                "team2Logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
                "score": "1 - 3",
                "status": "انتهت",
                "statusClass": "ended",
                "channel": "بي إن سبورت 1",
                "commentator": "حفيظ دراجي",
                "streamUrl": "https://live-hls-web-aje.getaj.net/AJE/index.m3u8"
            },
            {
                "id": "m_y2",
                "title": "الدوري الإنجليزي الممتاز",
                "stadium": "الإمارات",
                "team1": "آرسنال",
                "team1Logo": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
                "team2": "تشيلسي",
                "team2Logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
                "score": "2 - 1",
                "status": "انتهت",
                "statusClass": "ended",
                "channel": "بي إن سبورت 2",
                "commentator": "عصام الشوالي",
                "streamUrl": "https://live-hls-web-aje.getaj.net/AJE/index.m3u8"
            }
        ],
        "today": [
            {
                "id": "m_t1",
                "title": "تصفيات كأس أمم أفريقيا",
                "stadium": "ملعب الشهداء",
                "team1": "الجزائر",
                "team1Logo": "https://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Algeria.svg",
                "team2": "توجو",
                "team2Logo": "https://upload.wikimedia.org/wikipedia/commons/6/68/Flag_of_Togo.svg",
                "score": "2 - 1",
                "status": "جارية الان",
                "statusClass": "",
                "channel": "بي إن سبورت 1",
                "commentator": "حاج عيسى",
                "streamUrl": "https://live-hls-web-aje.getaj.net/AJE/index.m3u8"
            },
            {
                "id": "m_t2",
                "title": "كلاسيكو الأرض - الدوري الإسباني",
                "stadium": "سانتياغو برنابيو",
                "team1": "ريال مدريد",
                "team1Logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
                "team2": "برشلونة",
                "team2Logo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
                "score": "1 - 1",
                "status": "الشوط الثاني",
                "statusClass": "second-half",
                "channel": "بي إن سبورت 2",
                "commentator": "رؤوف خليف",
                "streamUrl": "https://f24hls-i.akamaihd.net/hls/live/221991/F24_AR_HLS/master.m3u8"
            },
            {
                "id": "m_t3",
                "title": "دوري أبطال أوروبا - القمة المرتقبة",
                "stadium": "اتحاد أرينا",
                "team1": "باريس سان جيرمان",
                "team1Logo": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg",
                "team2": "مانشستر سيتي",
                "team2Logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
                "score": "0 - 0",
                "status": "22:00",
                "statusClass": "upcoming",
                "channel": "بي إن سبورت Premium 1",
                "commentator": "خليل البلوشي",
                "streamUrl": "https://live-hls-web-aje.getaj.net/AJE/index.m3u8"
            }
        ],
        "tomorrow": [
            {
                "id": "m_tm1",
                "title": "دوري أبطال آسيا",
                "stadium": "الملك فهد",
                "team1": "الهلال السعودي",
                "team1Logo": "https://upload.wikimedia.org/wikipedia/en/b/b5/Al-Hilal_Saudi_FC_logo.svg",
                "team2": "السد القطرى",
                "team2Logo": "https://upload.wikimedia.org/wikipedia/en/4/41/Al_Sadd_SC_Logo.svg",
                "score": "0 - 0",
                "status": "غداً 19:00",
                "statusClass": "upcoming",
                "channel": "بي إن سبورت آسيا",
                "commentator": "فهد العتيبي",
                "streamUrl": "https://live-hls-web-aje.getaj.net/AJE/index.m3u8"
            }
        ]
    }

    with open("matches.json", "w", encoding="utf-8") as f:
        json.dump(full_schedule, f, ensure_ascii=False, indent=4)
    print("[+] تم تحديث جدول المباريات المتنوع لشمل عدة مواجهات.")

    # الأخبار الرياضية المتعددة والمتجددة
    news_data = [
        {
            "id": "n1",
            "title": "المنتخب الجزائري يجري آخر حصة تدريبية وسط معنويات مرتفعة للغاية",
            "summary": "ركز الناخب الوطني على الجوانب التكتيكية وسرعة التحول الهجومي تحضيراً للقاء الحاسم.",
            "time": "منذ 10 دقائق",
            "image": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=600&auto=format&fit=crop"
        },
        {
            "id": "n2",
            "title": "غيابات مؤثرة تضرب تشكيلة العملاق الإسباني قبل الكلاسيكو المنتظر",
            "summary": "تلقى الجهاز الفني صدمة بعد تأكد غياب أبرز نجوم خط الوسط بسبب الإصابة.",
            "time": "منذ ساعة",
            "image": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=600&auto=format&fit=crop"
        },
        {
            "id": "n3",
            "title": "رقم قياسي جديد في دوري أبطال أوروبا يحطمه مهاجم باريس سان جيرمان",
            "summary": "دخل النجم الدولي التاريخ من أوسع أبوابه بعد تسجيله هدفاً خارقاً للعادة في اللقاء الأخير.",
            "time": "منذ ساعتين",
            "image": "https://images.unsplash.com/photo-1518091043644-c1d4457512c6?q=80&w=600&auto=format&fit=crop"
        }
    ]

    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(news_data, f, ensure_ascii=False, indent=4)
    print("[+] تم تحديث قسم الأخبار الاحترافي (news.json).")
    print("[✔] تم تحديث كافة بيانات المنصة بنجاح وتعمل بنظام التحديث التلقائي!")

if __name__ == "__main__":
    print("==================================================")
    print("  🚀 بوت YOUB TV الاحترافي يعمل الآن...")
    print("==================================================")
    update_youb_tv_pro()
    
    # تحديث دوري كل 15 دقيقة
    schedule.every(15).minutes.do(update_youb_tv_pro)
    
    while True:
        schedule.run_pending()
        time.sleep(1)