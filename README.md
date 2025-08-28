# 🌍 Travel Lykke

A simple **travel booking web application** built with **Python (Django)** that allows users to view available travel options, book tickets, and manage their bookings. The frontend is developed using Django templates, with a responsive and user-friendly interface.

---

## 📌 Features

### 🔐 User Management

- User **registration**, **login**, and **logout** using Django’s built-in authentication system.
- Update and manage user profile information.

### 🚆 Travel Options

- Travel Options include:
  - **Travel ID**
  - **Type** (Flight ✈️, Train 🚆, Bus 🚌)
  - **Source & Destination**
  - **Date and Time**
  - **Price**
  - **Available Seats**
- Listing of available travel options with filters for:
  - Type
  - Source & Destination
  - Date

### 🧾 Booking

- Users can book travel options by selecting details and confirming.
- **Booking model** includes:
  - Booking ID
  - User (FK)
  - Travel Option (FK)
  - Number of Seats
  - Total Price
  - Booking Date
  - Status (**Confirmed/Cancelled**)

### 📅 View & Manage Bookings

- View **current** and **past bookings**.
- Cancel bookings from the dashboard.

### 🎨 Frontend

- Simple, responsive, and user-friendly pages built with **Django templates**.
- Pages for:
  - Registration & login
  - Profile management
  - Travel listings
  - Booking forms
  - Booking history with cancel option
- Styled using **CSS** (with optional **Bootstrap** for faster development).

---

## ✨ Bonus Features

- ✅ **MySQL** integration as the database.
- ✅ Input **validation** (number of seats, user input, etc.).
- ✅ **Search & filtering** for travel options.
- ✅ Unit tests for critical features.
- ✅ Cloud deployment support (AWS, PythonAnywhere, etc.).

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates, CSS, Bootstrap
- **Database:** MySQL (can also use SQLite for local development)

---

## 🚀 Getting Started (Local Setup)

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/travel-lykke.git
cd travel-lykke
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

- Create a **MySQL** database named `travel_lykke`.
- Update your `settings.py` or `.env` file with the following:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel_lykke',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

_(SQLite will work out of the box if you don’t configure MySQL.)_

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin Panel)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Now visit 👉 `http://127.0.0.1:8000/`

---

## 📂 Project Structure

```
travel-lykke/
├── travel_lykke/         # Main project settings
├── users/                # User authentication & profiles
├── travel_options/       # Travel options app
├── bookings/             # Booking management app
├── templates/            # Django templates
├── static/               # Static files (CSS, JS, images)
├── requirements.txt      # Python dependencies
└── manage.py             # Django entry point
```

---

## 🌐 Deployment

You can deploy the project on:

- **PythonAnywhere**
- **AWS (EC2/Elastic Beanstalk)**
- **Heroku** _(with MySQL add-ons)_

Make sure to:

- Configure environment variables for DB and secrets.
- Collect static files:

```bash
python manage.py collectstatic
```

---

## 📜 License

This project is licensed under the **MIT License**.

```

```
