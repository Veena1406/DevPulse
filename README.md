# 🚀 DevPulse

## Collaborative Real-Time Markdown Editor & Team Wiki

DevPulse is a web-based collaborative markdown editor that allows users to create, edit, organize, and manage markdown documents. It is developed using Flask and MongoDB with a simple and responsive user interface.

---

## 📌 Features

- User Registration
- User Login & Logout
- Secure Password Hashing
- User Dashboard
- User Profile
- Create Markdown Documents
- Edit Existing Documents
- Delete Documents
- Search Documents
- Live Markdown Preview
- User-wise Document Storage
- Responsive Bootstrap Interface

---

## 🛠 Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Flask

### Database
- MongoDB

### Libraries
- Flask-PyMongo
- PyMongo
- bcrypt
- markdown

---

## 📂 Project Structure

```
DevPulse/
│
├── app.py
├── config.py
├── requirements.txt
│
├── database/
│   └── mongodb.py
│
├── models/
│   ├── user.py
│   └── document.py
│
├── routes/
│   ├── auth.py
│   └── document.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── documents.html
│   ├── editor.html
│   └── profile.html
│
├── static/
│   └── style.css
│
└── utils/
    └── password.py
```

---

## ⚙ Installation

Clone the project.

```
git clone <repository-url>
```

Install the dependencies.

```
pip install -r requirements.txt
```

Run the Flask application.

```
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Modules

### Authentication
- Register
- Login
- Logout

### Dashboard
- User Home Page

### Document Management
- Create
- Edit
- Delete
- Search
- Live Preview

### User Profile
- View User Details

---

## 📈 Future Enhancements

- Real-time collaboration using Socket.IO
- Team Workspaces
- Comments on Documents
- Version History
- Export to PDF
- Dark Mode
- Document Sharing
- Email Notifications

---

## 🎯 Conclusion

DevPulse provides a simple and efficient platform for creating and managing markdown documents. It demonstrates authentication, CRUD operations, MongoDB integration, and responsive web design using Flask.

---

## 👩‍💻 Developed By

**Veena Munige**

Bachelor of Engineering

Department of Computer Science