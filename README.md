# 📝 Task Manager (Python + CustomTkinter)

A simple yet functional **Task Manager application** built using Python.
This project demonstrates **user authentication, task management, file handling**, and a **GUI using CustomTkinter**.

---

## 🚀 Features

### 🔐 User Authentication

* User Registration with unique username
* Secure password storage using hashing (SHA-256)
* Login validation system

### 📋 Task Management

* Add new tasks with unique Task IDs
* View all tasks (with status and timestamp)
* Mark tasks as **Completed**
* Delete tasks with confirmation
* Search tasks by keyword

### 💾 Data Persistence

* Uses **JSON file handling**
* Separate task file per user
* No database dependency (lightweight)

### 🎨 GUI

* Built using **customtkinter**
* Clean and interactive menu-driven interface

---

## 📂 Project Structure

```
task-manager/
│
├── main.py              # Entry point
├── ui.py                # GUI logic
├── auth.py              # Authentication logic
├── tasks.py             # Task operations
├── storage.py           # File handling
├── requirements.txt
├── README.md
│
├── data/                # Stores JSON files
│   ├── users.json
│   └── tasks_<user>.json
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

---

## 🧠 How It Works

* Users register/login → credentials stored in `users.json`
* Each user has a separate task file:

  ```
  tasks_<username>.json
  ```
* Tasks contain:

  * ID
  * Description
  * Status (Pending/Completed)
  * Timestamp

---

## 📌 Future Enhancements

* SQLite database integration
* Task priorities & deadlines
* Improved UI (sidebar/dashboard layout)
* REST API backend (Django/FastAPI)

---

## 👨‍💻 Tech Stack

* Python
* CustomTkinter
* JSON (File Handling)

---

## 📄 License

This project is for educational purposes.
