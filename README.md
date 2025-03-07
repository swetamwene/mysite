## Django REST API for Blog Posts

This is a Django REST framework-based API for managing blog posts. It provides endpoints for creating, reading, updating, and deleting blog posts. The project follows **RESTful principle**s and can be easily extended with authentication, pagination, and more.

---

## 🚀 Features
- ✅ Create, Read, Update, Delete (CRUD) for blog posts  
- ✅ Django REST framework-based  
- ✅ JSON response format  
- ✅ Extensible and customizable  
- ✅ Supports authentication (optional)  

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/django-blog-api.git
cd django-blog-api
```

### **2. Create a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Apply Migrations**
```sh
python manage.py migrate
```

### **5. Run the Development Server**
```sh
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/api/posts/` in your browser or use Postman.

---

## 📌 **API Endpoints**
| Method | Endpoint           | Description          |
|--------|-------------------|----------------------|
| GET    | `/api/posts/`      | List all posts      |
| POST   | `/api/posts/`      | Create a new post   |
| GET    | `/api/posts/{id}/` | Get post details    |
| PUT    | `/api/posts/{id}/` | Update a post       |
| DELETE | `/api/posts/{id}/` | Delete a post       |

---

## 🔧 **Configuration**
- Update `ALLOWED_HOSTS` in `settings.py`:
  ```python
  ALLOWED_HOSTS = ['localhost', '127.0.0.1']
  ```
- If using **SQLite**, no additional setup is required.
- For **MySQL/PostgreSQL**, update `DATABASES` in `settings.py`.

---

## ⚡ **Contributing**
Feel free to fork the repository and submit pull requests. Contributions are welcome! 🚀  

---

Would you like any additional customization? 😊
