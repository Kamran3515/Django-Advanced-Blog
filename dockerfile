FROM python:3.12-slim

# تنظیم محیط
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ایجاد پوشه پروژه
WORKDIR /app

# کپی کردن فایل‌های وابستگی
COPY requirements.txt /app/

# نصب پکیج‌های پایتون
RUN pip install --no-cache-dir -r requirements.txt

# کپی کل سورس کد پروژه
COPY ./core /app/