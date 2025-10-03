<<<<<<< HEAD
# 🤖 Supervised Machine Learning Loyihasi ReadMe

## Loyihaning maqsadi 🎯  
Ushbu loyiha ma'lumotlar asosida **Supervised Machine Learning** usullarini qo‘llab, maqsadli o‘zgaruvchi — `num_orders` ustunini bashorat qilishga qaratilgan. Maqsad — modellarning aniqligi va ishonchliligini oshirish hamda `num_orders` qiymatlarini aniq oldindan aytish.

---

## Loyiha bosqichlari 🛠️

### 1. Ma'lumotlarni yig‘ish va tushunish 🗃️  
- Ma'lumotlar to‘plami o‘rganildi.  
- Target sifatida `num_orders` ustuni aniqlab olindi.  
- Ma'lumotlarning tuzilishi va turlari ko‘rib chiqildi.

### 2. Ma'lumotlarni tozalash va tayyorlash 🧹  
- Bo‘sh qiymatlar (missing values) aniqlanib to‘ldirildi yoki olib tashlandi.  
- Kategorik ma'lumotlar kodlash (encoding) yordamida raqamli ko‘rinishga keltirildi.  
- Keraksiz yoki noma'lum ustunlar olib tashlandi.  
- Ma'lumotlarda skewness va outlier’lar aniqlanib, zarur transformatsiyalar bajarildi.

### 3. Feature Engineering va Selection ⚙️  
- Yangi ustunlar yaratildi va mavjudlar orasidan `num_orders` bilan eng kuchli bog‘lanishlarga ega feature’lar tanlandi.  
- Target bilan korrelyatsiyaga qarab va redundant feature’lar olib tashlandi.

### 4. Ma'lumotlarni bo‘lish (Train/Test Split) 🔄  
- Modelni sinash uchun ma'lumotlar o‘rgatish (train) va test qilish (test) to‘plamlariga ajratildi.

### 5. Modellar qurish va tanlash 🏗️  
- Turli regressiya modellari (Linear Regression, Decision Tree, Random Forest, Gradient Boosting, SVR) sinovdan o‘tkazildi.  
- Modellar baholandi va `num_orders` ni bashorat qilishda eng yaxshi natijalar tanlandi.

### 6. Model baholash 📊  
- Asosiy regressiya metrikalari hisoblandi:  
  - MSE (Mean Squared Error)  
  - RMSE (Root Mean Squared Error)  
  - MAE (Mean Absolute Error)  
  - R² (Coefficient of Determination)  
- Natijalar vizualizatsiya qilindi.

### 7. Modelni yaxshilash va tuning 🛠️  
- Hyperparameter tuning (GridSearchCV, RandomizedSearchCV) usullari qo‘llanildi.  
- Model interpretatsiyasi uchun SHAP qiymatlaridan foydalanildi.

---

## Texnologiyalar va kutubxonalar 🧰  
- Python 3.x  
- Pandas, NumPy (ma'lumotlarni qayta ishlash uchun)  
- Scikit-learn (model qurish va baholash uchun)  
- Seaborn, Matplotlib, Plotly (vizualizatsiya uchun)  
- SHAP (model tushuntirish uchun)

---

## Loyihani ishga tushirish 💻  

1. Kerakli kutubxonalarni o‘rnatish:  
   ```bash
   pip install pandas numpy scikit-learn seaborn matplotlib plotly shap
=======
# 🤖 Supervised Machine Learning Loyihasi ReadMe

## Loyihaning maqsadi 🎯
Ushbu loyiha ma'lumotlar asosida **Supervised Machine Learning** usullarini qo‘llab, maqsadli o‘zgaruvchini (target) bashorat qilishga qaratilgan. Maqsad — modellarning aniqligi va ishonchliligini oshirish.

---

## Loyiha bosqichlari 🛠️

### 1. Ma'lumotlarni yig‘ish va tushunish 🗃️
- Ma'lumotlar to‘plami o‘rganildi.
- Ustunlar va target aniqlab olindi.
- Ma'lumotlarning tuzilishi va turlarini ko‘rib chiqildi.

### 2. Ma'lumotlarni tozalash va tayyorlash 🧹
- Bo‘sh qiymatlar (missing values) aniqlanib to‘ldirildi yoki olib tashlandi.
- Kategorik ma'lumotlar kodlash (encoding) usuli bilan raqamli ko‘rinishga keltirildi.
- Noma'lum va keraksiz ustunlar olib tashlandi.
- Skewness va outlier’lar aniqlanib, kerakli transformatsiyalar bajarildi.

### 3. Feature Engineering va Selection ⚙️
- Yangi ustunlar yaratildi va mavjudlar orasidan eng foydali feature’lar tanlandi.
- Target bilan va o‘zaro korrelyatsiyaga qarab filtrlash usullari qo‘llandi.
- Redundant (o‘xshash) feature’lar olib tashlandi.

### 4. Ma'lumotlarni bo‘lish (Train/Test Split) 🔄
- Modelni sinash uchun ma'lumotlar o‘rgatish (train) va test qilish (test) to‘plamlariga ajratildi.

### 5. Modellar qurish va tanlash 🏗️
- Turli regressiya modellari (Linear Regression, Decision Tree, Random Forest, Gradient Boosting, SVR) sinovdan o‘tkazildi.
- Modellar baholandi va eng yaxshi natijalar tanlandi.

### 6. Model baholash 📊
- Asosiy regressiya metrikalari hisoblandi:  
  - MSE (Mean Squared Error)  
  - RMSE (Root Mean Squared Error)  
  - MAE (Mean Absolute Error)  
  - R² (Coefficient of Determination)  
- Natijalar vizualizatsiya qilindi.

### 7. Modelni yaxshilash va tuning 🛠️
- Hyperparameter tuning (GridSearchCV, RandomizedSearchCV) usullari qo‘llanildi.
- Model interpretatsiyasi uchun SHAP qiymatlaridan foydalanildi.

---

## Texnologiyalar va kutubxonalar 🧰
- Python 3.x
- Pandas, NumPy (ma'lumotlarni qayta ishlash uchun)
- Scikit-learn (model qurish va baholash uchun)
- Seaborn, Matplotlib, Plotly (vizualizatsiya uchun)
- SHAP (model tushuntirish uchun)

---

## Loyihani ishga tushirish 💻

1. Kerakli kutubxonalarni o‘rnatish:  
   ```bash
   pip install pandas numpy scikit-learn seaborn matplotlib plotly shap

>>>>>>> c7df45d (addings6)
