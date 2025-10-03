# 🤖 Modellar Bo‘limi ReadMe

## Maqsad 🎯
Bu bo‘limda turli regression modellari yordamida maqsadli qiymatni (target) bashorat qilish amalga oshiriladi. Har bir model ma’lumotlar to‘plamiga moslashtiriladi va samaradorligi baholanadi.

---

## Qo‘llanilgan modellar 🛠️

| Model nomi             | Tavsif                                                       |
|-----------------------|--------------------------------------------------------------|
| Linear Regression      | Oddiy chiziqli regressiya, asosiy va eng sodda model         |
| Decision Tree          | Qaror daraxti regressiyasi, murakkab qaror qabul qiladi       |
| Random Forest          | Ko‘p qaror daraxtlarining ansambli, yuqori aniqlik beradi    |
| Support Vector Regression (SVR) | Qattiq margin bilan regressiya, noaniq ma’lumotlarga bardoshli  |
| Gradient Boosting      | Bosqichma-bosqich kamchiliklarni tuzatadigan ansambl modeli |

---

## Modellarni o‘rgatish va baholash ⚙️

- Ma’lumotlar trening va test to‘plamlariga bo‘linadi (masalan, 80/20).
- Har bir model trening ma’lumotlari bilan o‘rgatiladi.
- Test ma’lumotlari yordamida bashoratlar olinadi.
- Quyidagi metrikalar bo‘yicha natijalar baholanadi:
  - **MSE** (Mean Squared Error)
  - **RMSE** (Root Mean Squared Error)
  - **MAE** (Mean Absolute Error)
  - **R² Score** (Aniqlik koeffitsienti)

---

## Natijalar 📊

| Model nomi           | MSE   | RMSE  | MAE   | R²    |
|----------------------|-------|-------|-------|-------|
| Linear Regression    | 0.xxx | 0.xxx | 0.xxx | 0.xxx |
| Decision Tree        | 0.xxx | 0.xxx | 0.xxx | 0.xxx |
| Random Forest        | 0.xxx | 0.xxx | 0.xxx | 0.xxx |
| SVR                  | 0.xxx | 0.xxx | 0.xxx | 0.xxx |
| Gradient Boosting    | 0.xxx | 0.xxx | 0.xxx | 0.xxx |

> *Eng yaxshi natija beruvchi model: Random Forest (misol uchun)*

---

## Modelni tanlashda e'tibor beriladigan jihatlar 🤔

- **Aniqlik:** R² qiymati yuqori va xatolar past bo‘lishi kerak.
- **Hisoblash resurslari:** Ba’zi modellar murakkab va ko‘p vaqt talab qilishi mumkin.
- **Model interpretatsiyasi:** Oddiy modellar ko‘proq tushunarli, murakkablar esa aniqroq natija beradi.
- **Overfitting:** Ansambl modellari (Random Forest, Gradient Boosting) ko‘pincha yaxshi umumlashtiradi.

---


