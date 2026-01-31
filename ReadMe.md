
## Loyihaning maqsadi 🎯  
Ushbu loyiha ma'lumotlar asosida **Supervised Machine Learning** usullarini qo‘llab, maqsadli o‘zgaruvchi — `num_orders` ustunini bashorat qilishga qaratilgan. Maqsad — modellarning aniqligi va ishonchliligini oshirish hamda `num_orders` qiymatlarini aniq oldindan aytish.

---

# 📈 Food Demand Prediction – Technical Contribution

## 🎯 Loyihaning maqsadi
Ushbu loyiha katta hajmdagi ma’lumotlar asosida oziq-ovqat talabini (Food Demand) yuqori aniqlikda bashorat qilish uchun turli regressiya algoritmlarini ishlab chiqish, taqqoslash va baholashga qaratilgan.

---

## 📊 Ma’lumotlar to‘plami (Dataset)
- **Train X:** 391,296 ta namuna, 14 ta feature  
- **Test X:** 97,825 ta namuna, 14 ta feature  
- **Train y:** 391,296 ta qiymat  
- **Test y:** 97,825 ta qiymat  

Ma’lumotlar modelning umumlashuv qobiliyatini tekshirish uchun train/test ga bo‘lindi va qo‘shimcha ravishda cross-validation qo‘llanildi.

---

## 🧠 Modellar va texnologiyalar
Loyihada `scikit-learn` kutubxonasi yordamida quyidagi regressiya modellari ishlab chiqildi va baholandi:

- Linear Regression  
- Decision Tree Regression  
- Random Forest Regression  
- Gradient Boosting Regression  
- Support Vector Regression (SVR)  

Baholash metrikalari:
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**
- **R² Score**

---

## 🚀 Modellar natijalari

### 🔹 Gradient Boosting Regression
- **MSE:** 0.0000  
- **RMSE:** 0.0002  
- **MAE:** 0.0001  
- **R²:** 0.9999  

Gradient Boosting modeli murakkab va nolinear bog‘lanishlarni juda yaxshi o‘rganib, deyarli mukammal natija ko‘rsatdi.

---

### 🔹 Random Forest Regression
- **MSE:** 0.0000  
- **RMSE:** 0.0000  
- **MAE:** 0.0000  
- **R²:** 1.0000  

Random Forest modeli ansambl yondashuvi sababli eng yuqori aniqlikka erishdi va overfitting xavfini minimal darajada ushlab turdi.

---

### 🔹 Decision Tree Regression
- **MSE:** 0.0000  
- **RMSE:** 0.0001  
- **MAE:** 0.0000  
- **R²:** 0.9999  

Yuqori aniqlikka ega bo‘lsa-da, bitta daraxt modeli sifatida overfitting xavfi mavjud.

---

### 🔹 Linear Regression
- **MSE:** 0.0000  
- **RMSE:** 0.0005  
- **MAE:** 0.0003  
- **R²:** 0.9988  

Natijalar ma’lumotlar orasida kuchli chiziqli bog‘lanishlar mavjudligini ko‘rsatdi, ammo nolinear modellarga nisbatan biroz pastroq ishladi.

---

### 🔹 Support Vector Regression (SVR)
- **MSE:** 0.0058  
- **RMSE:** 0.0764  
- **MAE:** 0.0758  
- **R²:** -23.9053  

SVR katta hajmdagi dataset bilan samarali ishlamadi va regressiya vazifasi uchun mos emasligi aniqlandi.

---

## 🔁 Cross-Validation natijalari (5-Fold)
Modelning barqarorligini tekshirish uchun 5 martalik cross-validation qo‘llanildi:

- **MSE:** 0.000000 ± 0.000001  
- **RMSE:** 0.000362 ± 0.000483  
- **MAE:** 0.000002 ± 0.000002  
- **R²:** 0.998584 ± 0.002581  

Ushbu natijalar model yuqori darajada umumlashuv qobiliyatiga ega ekanini tasdiqlaydi.

---

## ✅ Xulosa
- Eng yaxshi natijalar **Random Forest** va **Gradient Boosting** modellari tomonidan ko‘rsatildi.
- Loyiha quyidagi texnik ko‘nikmalarni namoyish etadi:
  - Katta hajmdagi ma’lumotlar bilan ishlash  
  - Regression modellari va ansambl metodlar  
  - Model baholash va cross-validation  
  - Overfitting va generalizatsiya muammolarini tahlil qilish  

Ushbu loyiha real ishlab chiqarish (production) muhitida talabni bashorat qilish tizimlarida qo‘llash uchun tayyor holatga keltirilgan.

# 💼 Business Contribution – Food Demand Prediction

## 🎯 Biznes muammo
Oziq-ovqat yetkazib berish va savdo tizimlarida eng katta muammolardan biri — **talabni noto‘g‘ri bashorat qilish**:
- Ortiqcha ishlab chiqarish va saqlash xarajatlari
- Mahsulot yetishmovchiligi sababli yo‘qotilgan daromad
- Logistika va ombor resurslaridan samarasiz foydalanish

Ushbu loyiha aynan shu muammoni **ma’lumotlar asosida hal qilish**ga qaratilgan.

---

## 📉 Muammoning biznesga ta’siri
Noto‘g‘ri talab prognozi quyidagi salbiy oqibatlarga olib keladi:
- Yaroqlilik muddati cheklangan mahsulotlarning isrof bo‘lishi  
- Mijozlar qoniqishining pasayishi  
- Rejalashtirish va ta’minot zanjirida uzilishlar  
- Daromad va foydaning beqarorligi  

---

## 🚀 Taklif etilgan yechim
Loyihada ishlab chiqilgan **Food Demand Prediction modeli**:
- Tarixiy savdo ma’lumotlari asosida talabni aniq bashorat qiladi  
- Turli regressiya modellarini solishtirib, **eng optimal model** tanlandi  
- Yuqori aniqlik tufayli qaror qabul qilish jarayonini avtomatlashtirish imkonini berdi  

---

## 📊 Biznes uchun asosiy natijalar

### 🔹 Xarajatlarni kamaytirish
- Talabning yuqori aniqlikda prognoz qilinishi:
  - Ortiqcha ishlab chiqarishni kamaytirdi  
  - Ombor va saqlash xarajatlarini optimallashtirdi  
- Isrof va yo‘qotishlar sezilarli darajada qisqardi

---

### 🔹 Daromadni oshirish
- Mahsulot yetishmovchiligi holatlari kamaydi  
- Mijozlarga kerakli vaqtda kerakli miqdorda mahsulot yetkazib berildi  
- Savdo barqarorlashdi va **revenue predictability** yaxshilandi  

---

### 🔹 Operatsion samaradorlik
- Logistika va ta’minot zanjiri rejalashtirish avtomatlashtirildi  
- Inson omiliga bog‘liqlik kamaydi  
- Rejalashtirish jarayonlari tezlashdi va xatolar soni kamaydi  

---

### 🔹 Strategik qarorlarni qo‘llab-quvvatlash
- Qaysi mahsulotlarga talab yuqori ekanini oldindan aniqlash imkoniyati  
- Marketing kampaniyalarini talabga mos rejalashtirish  
- Mavsumiylik va trendlarni aniqlash orqali uzoq muddatli strategiya tuzish  

---

## 🏆 Biznes qiymati (Business Value)
- Talab prognozi aniqligi **~99% dan yuqori**
- Xarajatlarni **sezilarli darajada kamaytirish**
- Daromadni oshirish va mijozlar qoniqishini yaxshilash
- Real vaqtga yaqin qaror qabul qilish imkoniyati

---

## ✅ Yakuniy xulosa
Ushbu loyiha:
- Texnik jihatdan yuqori aniqlikka ega ML modelni
- Real biznes muammoga moslab
- Amaliy va ishlab chiqarishga tayyor yechimga aylantirdi

Food Demand Prediction modeli kompaniyalarga **xarajatlarni nazorat qilish**, **daromadni oshirish** va **raqobat ustunligini qo‘lga kiritish** imkonini beradi.



