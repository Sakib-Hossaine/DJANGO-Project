# Django Project with WebRTC Integration

![image](https://github.com/user-attachments/assets/e69926e4-b83a-487f-8290-383e5735132a)


A Django web application with WebRTC functionality for real-time communication.

## Features

- Django backend with user authentication
- WebRTC integration for real-time video/audio communication
- Responsive frontend design
- Project showcase section with image upload capability

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- Node.js (LTS version)
- npm (comes with Node.js)
- Git

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Sakib-Hossaine/DJANGO-Project.git
cd DJANGO-Project

### 2. Set up Python environment
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux) 
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

### 3. Set up Django
```bash
python manage.py migrate
python manage.py createsuperuser 

### 4. Set up WebRTC Node.js server
```bash
install Node.js
cd webrtc-node-app
node server.js
