# Repair Management System (Django)

A full-featured Repair Management System built using Django.  
This application allows users to submit repair requests for electronic devices, track repair status, receive admin updates, and manage payments.

---

## 🚀 Key Features

### 👤 User Management
- Django built-in authentication
- Extended user profile with phone, address, and profile picture
- One-to-one relationship between User and UserProfile

### 🛠 Repair Request Management
- Submit repair requests with detailed device information
- Multiple problem type selection (hardware, software, screen, battery, etc.)
- Service options: Bring to Shop / Pickup Service
- Repair lifecycle tracking (Pending, In Progress, Completed, Cancelled)
- Repair history with timestamps

### 💬 Admin Communication
- Admin can send messages related to a repair request
- Charges and tax can be attached to admin messages
- Automatic total amount calculation

### 💳 Payment Management
- One-to-one payment per repair request
- Repair charge, pickup charge, and tax handling
- Auto-calculated total amount
- Payment status tracking (Pending, Paid, Failed)

---

## 🧱 Data Models Overview

### UserProfile
- Extends Django User model using OneToOneField
- Stores contact details and profile picture

### RepairRequest
- Core model of the application
- Stores device details, problem types, service preferences, and repair status
- Supports multiple boolean-based problem indicators for easy filtering

### Payment
- One-to-one relationship with RepairRequest
- Handles billing logic and auto-calculates total amount

### AdminMessage
- Allows admin-to-user communication
- Supports attaching repair charges and tax
- Auto-calculates total amount on save

---

## 🛠 Tech Stack

- Backend: Python, Django
- Database: SQLite
- Frontend: HTML, CSS, Bootstrap
- Authentication: Django Auth
- Version Control: Git, GitHub

---



## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/AthiraRagini/Django-projects.git
