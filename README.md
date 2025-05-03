# Django Project with WebRTC Integration

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin: 30px 0;">
  <img src="https://github.com/user-attachments/assets/e69926e4-b83a-487f-8290-383e5735132a" alt="Main Interface" style="width: 45%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <img src="https://github.com/user-attachments/assets/036f6b0b-1805-4cb6-8ca2-3a58957435c5" alt="WebRTC Demo" style="width: 45%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <img src="https://github.com/user-attachments/assets/84af8000-b319-4612-91fb-781b13aa01cc" alt="Mobile View" style="width: 45%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <img src="https://github.com/user-attachments/assets/977e9f15-0abd-4c7a-8474-107b3c3bfcdc" alt="Admin Panel" style="width: 45%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

A Django web application with WebRTC functionality for real-time communication.

## ✨ Features

- 🛠 Django backend with user authentication
- 📹 WebRTC integration for real-time video/audio communication
- 📱 Responsive frontend design
- 🖼 Project showcase section with image upload capability
- 🔒 Secure signaling server with Node.js

## 🚀 Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- Node.js (LTS version)
- npm (comes with Node.js)
- Git

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Sakib-Hossaine/DJANGO-Project.git
cd DJANGO-Project

2. Set up Python environment
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux) 
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

3. Set up Django
# Apply database migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Follow prompts to create admin account

4. Set up WebRTC Node.js server
cd webrtc-node-app
npm install
node server.js

🏃 Running the Project

Django Development Server:
python manage.py runserver

WebRTC Signaling Server (in separate terminal):
cd webrtc-node-app
node server.js
