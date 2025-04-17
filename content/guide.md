---
title: راهنما
order: 2
---

# Bookane - کتابانه

یک سیستم مدیریت محتوا برای کتاب‌های الکترونیکی با پشتیبانی از زبان‌های فارسی و انگلیسی.

## ویژگی‌ها

- پشتیبانی از محتوای دو زبانه (فارسی و انگلیسی)
- پشتیبانی از جهت‌های مختلف متن (RTL و LTR)
- ساختار کتاب‌مانند با فصل‌ها و زیرفصل‌ها
- ناوبری پیشرفته بین صفحات
- رابط کاربری زیبا و واکنش‌گرا
- پشتیبانی از فرمت Markdown برای محتوا

## نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.8 یا بالاتر
- pip (مدیر بسته Python)

### مراحل نصب

1. مخزن را کلون کنید:

   ```bash
   git clone https://github.com/arazshah/bookane.git
   cd bookane
   ```

2. وابستگی‌ها را نصب کنید:

   ```bash
   pip install -r requirements.txt
   ```

3. برنامه را اجرا کنید:

   ```bash
   python app.py
   ```

4. در مرورگر خود به آدرس `http://localhost:5000` بروید.

## ساختار پروژه

```
bookane/
├── app.py                  # فایل اصلی برنامه
├── requirements.txt        # وابستگی‌های پروژه
├── static/                 # فایل‌های استاتیک
│   ├── style.css           # استایل‌های CSS
│   └── script.js           # اسکریپت‌های JavaScript
├── templates/              # قالب‌های HTML
│   ├── index.html          # صفحه اصلی
│   └── navigation.html     # قالب ناوبری
└── content/                # محتوای کتاب
    ├── intro.md            # مقدمه
    ├── chapter1/           # فصل اول
    │   ├── section1.md     # بخش اول
    │   └── section2.md     # بخش دوم
    └── chapter2/           # فصل دوم
        └── section1.md     # بخش اول
```

## نحوه نوشتن محتوا

### ساختار فایل‌های Markdown

هر فایل Markdown باید دارای frontmatter باشد که اطلاعات متا را مشخص می‌کند:

```yaml
---
title: عنوان بخش
parent: chapter1  # برای زیرفصل‌ها
order: 1          # ترتیب نمایش
---
```

### پشتیبانی از محتوای انگلیسی (LTR)

برای نوشتن محتوای انگلیسی در متن فارسی، از بلوک کد با شناسه `ltr` استفاده کنید:

````markdown
```ltr
## Section Title
1. First item
2. Second item with **bold text**
```
````

این بلوک‌ها به صورت خودکار با جهت LTR و زبان انگلیسی نمایش داده می‌شوند.

### مثال کامل

```markdown
---
title: مقدمه
order: 1
---

# مقدمه

این یک متن فارسی است که از راست به چپ نوشته شده است.

```ltr
## Introduction

This is an English text that is written from left to right.

1. First point
2. Second point with **bold text**
```

```

## توسعه و سفارشی‌سازی

### افزودن فصل جدید

1. یک فایل Markdown جدید در پوشه `content` ایجاد کنید.
2. frontmatter مناسب را اضافه کنید.
3. محتوای خود را بنویسید.

### سفارشی‌سازی استایل‌ها

استایل‌های CSS را در فایل `static/style.css` ویرایش کنید.

### افزودن ویژگی‌های جدید

برای افزودن ویژگی‌های جدید، فایل `app.py` را ویرایش کنید.

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.
