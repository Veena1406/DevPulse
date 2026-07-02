# 🚀 DevPulse

## Collaborative Real-Time Markdown Editor & Team Wiki

DevPulse is a web-based Markdown Editor developed using **Python Flask** and **MongoDB**. It allows users to securely create, edit, preview, search, and manage markdown documents through a clean and responsive interface.

This project was developed as an internship project to demonstrate full-stack web development using Flask, MongoDB, Bootstrap, and Python.

---

## 📌 Features

- 🔐 User Registration & Login
- 🔒 Secure Password Encryption (bcrypt)
- 👤 User Profile
- 📝 Create Markdown Documents
- ✏️ Edit Documents
- 👀 Live Markdown Preview
- 📂 View All Documents
- 🔍 Search Documents
- 🗑️ Delete Documents
- 📱 Responsive Bootstrap UI
- 🔑 Session-Based Authentication

---

## 🛠️ Technologies Used

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
- Flask
- Flask-PyMongo
- PyMongo
- bcrypt
- markdown
- python-dotenv

---

## 📁 Project Structure

```
DevPulse/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
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
│   ├── profile.html
│   ├── documents.html
│   ├── editor.html
│   └── view_document.html
│
├── static/
│   ├── css/
│   └── js/
│
└── utils/
    └── password.py
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/devpulse.git
```

Move into the project folder.

```bash
cd devpulse
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python app.py
```

Open your browser.

```
http://127.0.0.1:5000
```

---

## 📖 Usage

1. Register a new account.
2. Login using your credentials.
3. Open the Dashboard.
4. Create a new markdown document.
5. Write markdown content.
6. View the live preview.
7. Save the document.
8. Edit or delete documents anytime.
9. Search documents by title.
10. Logout securely.

---

## 📷 Screenshots

Add screenshots of the following pages.

- Home Page
- Registration
- Login
- Dashboard
- User Profile
- My Documents
- Markdown Editor
- Live Preview
- Search Documents
- MongoDB Collections

---

## 🔒 Security Features

- Password Hashing using bcrypt
- Secure User Authentication
- Session Management
- User-Specific Document Access
- Protected Routes

---

## 📈 Future Enhancements

- Real-Time Collaboration
- Version History
- PDF Export
- Dark Mode
- Document Sharing
- Comments
- Notifications
- Rich Text Editor
- Cloud Deployment
- AI Writing Assistant

---

## 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

- Flask Routing
- MongoDB Integration
- CRUD Operations
- Session Management
- Password Encryption
- Bootstrap UI Design
- Markdown Rendering
- Project Structure Organization
- User Authentication

---

## 👩‍💻 Developer

**Veena Munige**

Department of Computer Science and Engineering

University College of Engineering and Technology for Women

Kakatiya University

---

## 🏢 Internship Details

**Company:** EduExpose

**Industry Mentor:** Santhoshi

**Duration:** May 1 – June 30

---

## 📄 License

This project was developed for educational and internship purposes.
