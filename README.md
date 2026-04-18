#  Web-Based Facial Authentication System

## Project Overview
This project is a **web-based facial recognition authentication system** developed as part of a security course.  
It allows users to **register (enroll)** their face and later **authenticate** using a webcam.

The system extracts facial features, converts them into numerical representations (face embeddings), and compares them with stored data to verify identity.

---

##  Objectives
- Implement a secure **biometric authentication system**
- Apply **Identity and Access Management (IAM)** principles
- Demonstrate **face recognition using computer vision**
- Build a complete system from design → implementation → deployment

---

##  How It Works

### 1. Enrollment
- User enters a username
- Webcam captures facial image
- System extracts facial embedding
- Embedding is stored in the database

### 2. Authentication
- User enters username
- Webcam captures face again
- System compares embeddings
- Access is granted or denied

---

##  Project Structure
web-facial-auth-system/
│
├── app/
│ ├── main.py
│ ├── database.py
│ ├── routes/
│ ├── services/
│ ├── templates/
│ ├── static/
│ └── instance/
│
├── data/
├── models/
├── tests/
├── screenshots/
├── docs/
├── requirements.txt
└── README.md


---

##  Technologies Used

- Python 3.10
- Flask (Web Framework)
- OpenCV (Computer Vision)
- face_recognition (Facial Recognition)
- SQLite (Database)
- NumPy

---

##  Installation & Setup

### 1. Clone the repository
git clone https://github.com/Haitham920/web-facial-auth-system.git

cd web-facial-auth-system
### 2. Create virtual environment
python -m venv venv

**Activate it:**

venv\Scripts\activate
### 3. Install dependencies
pip install -r requirements.txt
### 4. Run the application
python app/main.py

Open in browser: 

http://127.0.0.1:5000

---

## Usage
### Enroll a user
i) Go to: 
http://127.0.0.1:5000/enroll 
ii) Enter username 
iii) Capture face
### Login
i) Go to:
http://127.0.0.1:5000
ii) Enter username
iii) Capture face
iv) Access granted/denied

---

## Screenshots

Screenshots are available in the screenshots/ folder, including:

Login page
Enrollment page
Successful authentication
Failed authentication

---

## Security Features
Biometric authentication using facial recognition
User-specific identity binding
Default-deny access model
Logging of authentication attempts

---

## Limitations
Depends on lighting conditions
Single-factor biometric authentication
Not production-ready (development server)

---

## Future Improvements
Multi-factor authentication (MFA)
Liveness detection (anti-spoofing)
Improved UI/UX
Deployment on cloud
Real-time video authentication

---

## Authors
### Haitham Maatar
### Mohamed Ben Arbia
