# Movie Rating App

## Live 
https://movie-rating-frontend-chi.vercel.app/

## Overview
Movie Rating App is a web-based platform that allows users to browse, rate, and manage movies. It features user authentication, movie listing, rating functionality, and movie management capabilities.

## Features
- User Authentication (Login/Register)
- List of Movies
- Add, Edit, and Delete Movies
- Rate Movies
- Secure API with Token-based Authentication
- Responsive UI

## Technologies Used
### Frontend
- React (with Vite)
- React Hooks
- React Cookie
- FontAwesome Icons

### Backend
- Django REST Framework (API)
- Token-based Authentication

## Installation
### Prerequisites
Ensure you have the following installed:
- Node.js
- Python & Django

### Backend Setup
1. Clone the backend repository:
   ```bash
   git clone https://github.com/yourusername/movie-rating-backend.git
   cd movie-rating-backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # For Mac/Linux
   env\Scripts\activate  # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the backend server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Clone the frontend repository:
   ```bash
   git clone https://github.com/yourusername/movie-rating-frontend.git
   cd movie-rating-frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```



## Troubleshooting
### Common Issues & Fixes
- **Blank screen after login**: Ensure the token is stored properly and API calls are successful.
- **Cannot fetch movies**: Check API URL and authentication token.
- **Login issue (Invalid Credentials)**: Ensure correct username/password and API response handling.

## Contribution
Feel free to fork this repository and submit pull requests.



