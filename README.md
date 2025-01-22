# User Signup System

This project is a Django-based user signup system with role-based redirection and a Bootstrap-powered user interface. The application allows users to sign up and login with roles (`Normal User`, `Hotel Admin`, `Main Admin`) and redirects them to their respective dashboards.

## Features

- **Role-Based Redirection**:
  - `Normal User`: Redirected to the Home page.
  - `Hotel Admin`: Redirected to the Hotel Admin Dashboard.
  - `Main Admin`: Redirected to the Main Admin Dashboard.
- **User Authentication**:
  - Secure signup and login using Django's built-in authentication system.
  - Password validation and hashed storage.
- **Bootstrap Integration**:
  - Clean and responsive user interface.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: Bootstrap (HTML, CSS)
- **Database**: SQLite (default Django DB, can be replaced with PostgreSQL, MySQL, etc.)
- **Supabase**: Used for additional database functionality.

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd user-login-management-system
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure the Supabase settings:
   - Add your Supabase project URL and API key to the settings file.

6. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage
- Register a new account.
- Log in using your credentials.
- Access and update your user profile.

## Contribution
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to reach out with any questions or suggestions!


