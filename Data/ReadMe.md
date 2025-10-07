# 📊 Data Preprocessing ReadMe

## Dataset haqida umumiy ma’lumotlar 🗂️
- Datasetda turli turdagi ustunlar mavjud: `id`, `week`, `center_id`, `meal_id`, `checkout_price`, `base_price`, `emailer_for_promotion`, `homepage_featured`, `num_orders`, `category`, `cuisine`, `price_diff`, `price_diff_ratio`, `season` va boshqalar.
- Target ustun: `num_orders` 🎯
- Ma'lumotlar o'lchami: **train** va **test** uchun bo'lingan.  
- Skewness tekshirilgan — ayrim ustunlarda notekis taqsimot aniqlangan 📉.

---

## Data Preprocessing jarayoni 🧹

### 1. Missing Value larni tozalash ❌
- Datasetdagi bo‘sh qiymatlar (`NaN`) aniqlanib, mos usul bilan to‘ldirildi yoki o‘chirib tashlandi.
- Ustunlar bo‘yicha ma'lumot to‘liqligi tekshirildi.

### 2. Encoding 🔤
- Kategorik ustunlar (`category`, `cuisine`) **One-Hot Encoding** yoki **Label Encoding** usuli bilan raqamli ko‘rinishga keltirildi.
- Bu mashina o‘rganish modellariga moslash uchun muhim.

### 3. Feature Engineering ⚙️
- Yangi ustunlar yaratildi:  
  - `price_diff` = `checkout_price` - `base_price`  
  - `price_diff_ratio` = `price_diff` / `base_price`  
- Log va sqrt transformatsiyalar orqali taqsimotlarni normallashtirishga harakat qilindi (masalan, `num_orders_log`, `price_diff_log`).

### 4. Scaling ⚖️
- `checkout_price`, `base_price`, `num_orders` kabi sonli ustunlar **MinMaxScaler** yoki **StandardScaler** bilan o'lchami moslashtirildi.
- Bu modellarning yaxshi o‘rganishi uchun zarur.

### 5. Skewness va Outliers bilan ish 🕵️
- Skewness darajasi yuqori bo‘lgan ustunlarda log-transformatsiya qo‘llandi.
- Chuqur analiz qilib, yuqori korrelyatsiyaga ega feature juftliklari aniqlandi va redundant ustunlarni olib tashlash uchun tayyorlik qilindi.

### 6. Feature Selection ✅
- Target ustun bilan 0.02 dan yuqori absolute korrelyatsiyaga ega feature'lar tanlandi.
- Yuqori o‘zaro korrelyatsiya bo‘lgan ustunlar aniqlanib, redundant ma’lumotlar kamaytirildi.

### 7. Train/Test split 🔄
- Ma'lumotlar **train** va **test** to‘plamlarga bo‘lindi (masalan, 80/20 nisbatda).
- Modellashtirish uchun tayyor holatga keltirildi.

---

## Foydali linklar va keyingi qadamlar 🔗

- [Model tanlash va baholash](#) — regressiya modellarini sinash va baholash.
- [SHAP tushunchalari](#) — model interpretatsiyasi uchun SHAP qiymatlari.
- [Hyperparameter tuning](#) — model optimallashtirish uchun GridSearchCV va RandomizedSearchCV.

---

## Xulosa 🎉  
Data preprocessing jarayoni — samarali model qurish uchun eng muhim qadam. Yuqoridagi bosqichlar ma'lumotni tozalash, transformatsiya qilish va tanlashni o‘z ichiga oladi. Har bir bosqichda ehtiyotkorlik bilan ish olib borish, keyingi modeling bosqichlarining muvaffaqiyatiga ta'sir qiladi.

---

