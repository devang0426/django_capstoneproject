# 🥗 **Little Lemon API - Table Booking System**

This project is part of the **Meta Back-End Developer Capstone**. It provides a REST API for managing menu items and table bookings for the fictional restaurant **Little Lemon**.

---

## 🚀 **Project Overview**

The Little Lemon API is built using **Django** and **Django REST Framework (DRF)**. The API includes endpoints to perform CRUD operations on menu items and customer table bookings, with a MySQL database as the backend.

---

## 📚 **Features**

✅ **Menu Management:**  
- List all menu items  
- Add, update, and delete menu items  

✅ **Table Booking System:**  
- View all table bookings  
- Create, update, and cancel reservations  

✅ **User Authentication:**  
- Secure login and registration  
- Admin access to manage database models  

✅ **Unit Testing:**  
- Comprehensive unit tests for models and views  

✅ **API Documentation:**  
- Easily testable using tools like Insomnia or Postman  

---

## 🛠️ **Tech Stack**

- **Backend:** Django, Django REST Framework (DRF)  
- **Database:** MySQL  
- **Authentication:** Django’s built-in user authentication  
- **Testing:** Django Test Framework  

---
## 🔗 **API Endpoints**

### 1. **Menu Endpoints**
- `GET /api/menu/` – List all menu items  
- `POST /api/menu/` – Create a new menu item  
- `GET /api/menu/<id>/` – Retrieve a specific menu item  
- `PUT /api/menu/<id>/` – Update a menu item  
- `DELETE /api/menu/<id>/` – Delete a menu item  

### 2. **Table Booking Endpoints**
- `GET /api/tables/` – List all table bookings  
- `POST /api/tables/` – Create a new booking  
- `GET /api/tables/<id>/` – Retrieve booking details  
- `PUT /api/tables/<id>/` – Update booking  
- `DELETE /api/tables/<id>/` – Cancel a booking  

---

