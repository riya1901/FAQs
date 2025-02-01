# 🚀 FAQ Management System – Multilingual & Scalable API  
> A powerful **FAQ (Frequently Asked Questions) Management System** designed to handle multilingual queries with **optimized caching** for seamless performance.


---

## 🚀 Features
- **Multilingual Support:** Manage FAQs in multiple languages (`question_hi`, `question_bn`, etc.)
- **WYSIWYG Editor Integration:** **django-ckeditor** is used to allow rich text formatting for answers.
- **API for FAQ Management:** Create, Read, Update, Delete FAQs via a **REST API** with language-specific querying.
- **Efficient Caching:** Utilizes **Redis(DOCKer)** to cache translated FAQ data and improve API performance.
- **Automatic Translation:** Supports automatic translation via **Google Translate API** (or `googletrans`).
- **User-Friendly Admin Interface:** Easily manage FAQs from the Django Admin Panel.
- **Code Quality & Unit Tests:** Follows **PEP8** guidelines, and includes **unit tests** with **pytest**.
---

## 🚀 How Does It Work?  
1. **User requests an FAQ with a language parameter** (e.g., `?lang=bn` for Bengali).  
2. The system **checks Redis cache** to see if the translated FAQ exists.  
3. If cached, it **returns the stored translation instantly**.  
4. If not cached, it **fetches the original question**, translates it dynamically, and caches it for future use.  
5. The response is sent back **in the requested language only**, ensuring a clean user experience.  

### 📌 Example API Calls  
```sh

GET /api/faqs/?lang=hi  # Fetch FAQs in Hindi
     [
    {
        "question": "आपका क्या नाम है?",
        "answer": "मेरा नाम रिया है।"
    }
]

GET /api/faqs/?lang=bn
[
    {
        "question": "তোমার নাম কি?",
        "answer": "আমার নাম রিয়া।"
    }
]

POST /api/faqs/
 {
    "question": "What is your name?",
    "answer": "My name is Riya.",
    "question_hi": "आपका क्या नाम है?",
    "question_bn": "তোমার নাম কি?",
    "question_es": "¿cómo te llamas?"
}
```

### 🛠 Tech Stack
- **Backend:** Django, Django Rest Framework (DRF)
- **Database:**  SQLite
- **Caching:** Redis
- **Translation:** deepTranslator
- **Rich Text Editor:** Django CKEditor
- **API Testing:**  Browsable API

---
### 🧑‍💻 Installation
- **Run Server**: `python manage.py runserver`
- **Virtual Environment**: `venv\Scripts\activate`
- **Git Code**:
  ```sh
  # Initialize the Git repository
  git init
  
  # Add your files
  git add .
  
  # Commit your changes
  git commit -m "Initial commit for FAQ project"
  
  # Link your local repo
  git remote add origin https://github.com/riya1901/FAQs.git
  
  # To Push
  git push -u origin branch  # according to branch


