# AI Gumanizator - Matningizni AI bilan O'zgartiring

OpenAI ning GPT-3.5-turbo yordamida matnni turli uslublar va ohanglarga o'zgartirish uchun kuchli Django veb-ilovasi. Kontent yaratuvchilari, yozuvchilar, marketing mutaxassislari va matnni turli auditoriyalar uchun moslashtirishga muhtoj bo'lgan har kim uchun ideal.

## 🌟 Xususiyatlar

### 🤖 AI Asosidagi Matn O'zgartirish
- **Akademik Uslub**: Rasmiy, ilmiy yozuv uslubi
- **Oddiy Ton**: Qulay, suhbatdosh til
- **Emotsional Ifoda**: His-tuyg'ularni uyg'otadigan jonli, tavsiflovchi til
- **Marketing Matn**: Kuchli so'zlar va chaqiruvlar bilan ishonchli kontent
- **Hikoya Qilish**: Tavsiflovchi tafsilotlar bilan jalb qiluvchi hikoya
- **Soddalashtirilgan Matn**: Umumiy auditoriya uchun aniq, tushunarli til

### 🌍 Ko'p Tillilik Qo'llab-quvvatlash
- **Ingliz tili (EN)** - Asosiy til
- **Rus tili (RU)** - Русский интерфейс
- **O'zbek tili (UZ)** - O'zbek tilida interfeys

### 📊 Sessiya Asosidagi Foydalanuvchi Boshqaruvi
- Brauzer sessiyalari asosida avtomatik foydalanuvchi yaratish
- Sahifa yangilanishlaridan keyin ham saqlanadigan tarix
- Foydalanuvchi faoliyatini kuzatish va tahlil qilish

### 💾 Ma'lumotlar Bazasi Integratsiyasi
- Barcha so'rovlar SQLite ma'lumotlar bazasiga saqlanadi
- Ishlash vaqtini kuzatish va uning tezligini o'lchash
- Ma'lumotlarni boshqarish uchun admin interfeysi
- Eski ma'lumotlarni avtomatik tozalash

## 🚀 Tezkor Boshlash

### Talablar
- Python 3.8+
- Django 5.2+
- OpenAI API kaliti

### O'rnatish

1. **Repozitoriyani klonlash**
   ```bash
   git clone <repository-url>
   cd AI-Humanizer
   ```

2. **Virtual muhit yaratish**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows da: venv\Scripts\activate
   ```

3. **Qaramliklarni o'rnatish**
   ```bash
   pip install -r requirements.txt
   ```

4. **Muhit o'zgaruvchilarini sozlash**
   ```bash
   export OPENAI_API_KEY="sizning-openai-api-kalitingiz"
   ```

5. **Migratsiyalarni ishga tushirish**
   ```bash
   python manage.py migrate
   ```

6. **Superuser yaratish (ixtiyoriy)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Rivojlanish serverini ishga tushirish**
   ```bash
   python manage.py runserver
   ```

8. **Brauzeringizni oching**
   `http://localhost:8000` ga o'ting

## 🛠️ Sozlash

### Muhit O'zgaruvchilari
```bash
# Majburiy
OPENAI_API_KEY=sizning-openai-api-kalitingiz

# Ixtiyoriy
DEBUG=True
SECRET_KEY=sizning-maxfiy-kalitingiz
DATABASE_URL=sizning-ma'lumotlar-bazasi-url
```

### Sozlamalar
Ilova Django ning standart sozlamalaridan foydalanadi, quyidagi maxsus o'zgarishlar bilan:
- Statik fayllar konfiguratsiyasi
- Media fayllar bilan ishlash
- Sessiya boshqaruvi
- OpenAI integratsiyasi

## 📁 Loyiha Tuzilishi

```
AI-Humanizer/
├── app/
│   ├── models.py          # Foydalanuvchi va So'rov modellari
│   ├── views.py           # API endpointlari
│   ├── openai.py          # OpenAI integratsiyasi
│   ├── utils.py           # Prompt shablonlari
│   ├── admin.py           # Admin interfeysi
│   └── management/        # Maxsus buyruqlar
├── config/
│   ├── settings.py        # Django sozlamalari
│   └── urls.py           # URL konfiguratsiyasi
├── templates/
│   └── index.html         # Asosiy frontend
├── static/               # Statik fayllar
├── media/                # Media fayllar
└── requirements.txt      # Qaramliklar
```

## 🔧 API Endpointlari

### POST `/api/humanize/`
AI yordamida matnni o'zgartirish
```json
{
    "text": "Sizning matningiz",
    "mode": "casual"
}
```

**Javob:**
```json
{
    "original_text": "Sizning matningiz",
    "humanized_text": "Salom! Demak sizning matningiz",
    "mode": "casual",
    "processing_time": 1.23
}
```

### GET `/api/history/`
Foydalanuvchining so'nggi tarixini olish
```json
{
    "history": [
        {
            "original_text": "Namuna matn",
            "humanized_text": "O'zgartirilgan matn",
            "mode": "academic",
            "timestamp": 1640995200,
            "created_at": "2022-01-01T00:00:00Z"
        }
    ]
}
```

## 🎨 Frontend Xususiyatlari

### Interaktiv Interfeys
- **Real vaqtda matn o'zgartirish** typewriter effekti bilan
- **Til o'zgartirish** sahifani qayta yuklamasdan
- **Har bir rejim uchun namuna matn**
- **Tarix boshqaruvi** bosish-orqaga qaytarish bilan
- **Barcha qurilmalar uchun responsive dizayn**

### Foydalanuvchi Tajribasi
- **Yuklash holatlari** vizual feedback bilan
- **Xatoliklarni boshqarish** foydalanuvchi-do'st xabarlar bilan
- **Natijalarni nusxalash** funksiyasi
- **Silliq animatsiyalar** va o'tishlar

## 🗄️ Ma'lumotlar Bazasi Modellari

### Foydalanuvchi Modeli
```python
class User(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
```

### So'rov Modeli
```python
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    humanized_text = models.TextField()
    mode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    processing_time = models.FloatField(null=True, blank=True)
```

## 🔧 Boshqarish Buyruqlari

### Eski Ma'lumotlarni Tozalash
```bash
# 30 kundan eski ma'lumotlarni olib tashlash
python manage.py cleanup_old_data

# 7 kundan eski ma'lumotlarni olib tashlash
python manage.py cleanup_old_data --days 7

# Nima o'chirilishini oldindan ko'rish
python manage.py cleanup_old_data --dry-run
```

## 🚀 Deploy Qilish

### Production Sozlamalari
1. `DEBUG=False` ni o'rnating
2. To'g'ri ma'lumotlar bazasini sozlang (PostgreSQL tavsiya etiladi)
3. Statik fayllarni xizmat qilishni sozlang
4. Muhit o'zgaruvchilarini sozlang
5. SSL/HTTPS ni sozlang

### Docker Deploy (Ixtiyoriy)
```dockerfile
FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 📊 Monitoring va Tahlil

### Admin Interfeysi
- Superuser hisob ma'lumotlari bilan `/admin/` da kirish
- Foydalanuvchi faoliyati va so'rov statistikalarini ko'rish
- Ishlash vaqtini va uning tezligini kuzatish
- Ma'lumotlarni qidirish va filtrlash

### Asosiy Metrikalar
- Jami foydalanuvchilar va so'rovlar
- O'rtacha ishlash vaqti
- Eng mashhur o'zgartirish rejimlari
- Foydalanuvchi faoliyat naqshlari

## 🛡️ Xavfsizlik Xususiyatlari

- **Barcha formalar uchun CSRF himoyasi**
- **Sessiya asosidagi** foydalanuvchi identifikatsiyasi
- **Kirish ma'lumotlarini tekshirish** va sanitizatsiya
- **Ma'lumotlar ta'sirini ko'rsatmasdan xatoliklarni boshqarish**
- **Tezlik cheklovlari** (qo'shilishi mumkin)

## 🤝 Hissa Qo'shish

1. Repozitoriyani fork qiling
2. Feature branch yarating
3. O'zgarishlaringizni qiling
4. Agar kerak bo'lsa, testlar qo'shing
5. Pull request yuboring

## 📝 Litsenziya

Bu loyiha MIT Litsenziyasi ostida litsenziyalangan - batafsil ma'lumot uchun LICENSE faylini ko'ring.

## 🆘 Yordam

### Keng Tarqalgan Muammolar

**OpenAI API Xatolari:**
- API kalitingizning to'g'riligini tekshiring
- Yetarli kreditlaringiz borligini ta'minlang
- API kaliti muhit o'zgaruvchilarida o'rnatilganligini tekshiring

**Ma'lumotlar Bazasi Muammolari:**
- `python manage.py migrate` ni ishga tushiring
- Ma'lumotlar bazasi ruxsatlarini tekshiring
- Ma'lumotlar bazasi ulanish sozlamalarini tekshiring

**Statik Fayllar Yuklanmayapti:**
- `python manage.py collectstatic` ni ishga tushiring
- Statik fayllar konfiguratsiyasini tekshiring
- Fayl ruxsatlarini tekshiring

### Yordam Olish
- Django hujjatlarini tekshiring
- OpenAI API hujjatlarini ko'rib chiqing
- GitHub da issue oching
- Rivojlanish jamoasi bilan bog'laning

## 🔮 Kelajakdagi Yaxshilanishlar

- [ ] Foydalanuvchi autentifikatsiya tizimi
- [ ] Maxsus prompt shablonlari
- [ ] Batch matn qayta ishlash
- [ ] Eksport funksiyasi
- [ ] Kengaytirilgan tahlil dashboardi
- [ ] API tezlik cheklovlari
- [ ] Keshlash tizimi
- [ ] Ko'p tilli matn qo'llab-quvvatlash

---

**Django va OpenAI yordamida ❤️ bilan yaratilgan**
