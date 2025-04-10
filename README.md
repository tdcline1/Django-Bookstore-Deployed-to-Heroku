# 📚 Django Bookstore App

A fully-featured Django bookstore web application with custom user authentication, PostgreSQL database integration, image uploads, reviews, and production deployment using Docker and Heroku. Built to demonstrate best practices in Django development, security, and performance optimization.

---

## 🚀 Features

- Custom user model with registration, login, logout, and email-based authentication (via `django-allauth`)
- Secure file and image uploads
- Book and review management
- Search functionality
- Permissions and access control
- Static and media file management
- PostgreSQL database support
- Dockerized local and production environments
- Deployment to Heroku with Gunicorn and Whitenoise

---

## 🛠️ Tech Stack

- **Backend:** Django, PostgreSQL
- **Frontend:** HTML, CSS, Bootstrap
- **Authentication:** Django Allauth
- **Database:** PostgreSQL (local via Docker, Heroku Postgres in production)
- **Media Storage:** Local filesystem (with Django-Storages setup for S3 compatibility)
- **Deployment:** Docker, Gunicorn, Whitenoise, Heroku
- **Testing:** Django's built-in test framework
- **Environment Variables:** `environs`

---

## 🧰 Setup Instructions (Local)
