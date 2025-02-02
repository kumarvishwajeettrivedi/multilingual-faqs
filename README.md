# FAQ Management System

A Django-based application to manage FAQs with multi-language translation support and WYSIWYG editor integration.

## Video Reference

You can view the demo of the project in action by clicking the link below:

[Watch the demo](https://www.loom.com/share/dbf7d0b684334003b7112267db36dfcb?sid=a0749575-d94e-46a9-94b8-d60a4d779cf5)


## Features
- **Multilingual FAQ Management:** Store and retrieve FAQs in multiple languages with automated translations.
- **WYSIWYG Editor Integration:** Format FAQ answers with `django-ckeditor`.
- **REST API:** Efficiently manage FAQs with support for language-specific queries.
- **Caching:** Boost performance with Redis-based caching for translations.
- **Admin Interface:** User-friendly admin panel for managing FAQs.
- **Unit Testing:** Comprehensive tests to ensure reliability.

## Tech Stack
- **Backend:** Django, Django Rest Framework
- **Database:** PostgreSQL
- **Cache:** Redis
- **Translation:** `googletrans` or Google Translate API
- **Editor:** django-ckeditor

---

## Installation

### Prerequisites
- Python 3.9+
- Django 4.0+
- Redis


### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/faq-management-system.git
   cd faq-management-system

2. install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Redis:
   - Install Redis: [Redis Installation Guide](https://redis.io/docs/getting-started/installation/)
   - Start the Redis server.

4. Set up environment variables in `.env`:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   REDIS_URL=redis://localhost:6379/0
   ```

5. Apply migrations and run the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## API Usage

### Fetch FAQs
- **Default (English):**
  ```bash
  curl http://localhost:8000/api/faqs/
  ```
- **Specific Language:**
  ```bash
  curl http://localhost:8000/api/faqs/?lang=hi
  ```

### Add FAQ (Admin Panel)
- Navigate to `/admin` and add FAQs with translations.

---


## Testing
1. Run unit tests:
   ```bash
   pytest
   ```

2. Check code quality:
   ```bash
   flake8
   ```

---

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes with clear messages (`git commit -m "feat: Add new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.
