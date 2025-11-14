# Django Portfolio Website

This is a fully customizable portfolio website built with Django. You can manage the content of your portfolio through the Django admin panel, making it easy to update your projects, skills, hobbies, and personal information without touching the code.

## Features

*   **Dynamic Content Management:** Almost every part of the portfolio is editable through the Django admin panel.
    *   Update your name, email, and social media links.
    *   Add, edit, and delete projects, skills, hobbies, and blog posts.
    *   Change the "About Me" section.
*   **Project and Blog Detail Pages:** Each project and blog post has its own dedicated page.
*   **Responsive Design:** The portfolio is designed to look great on all devices, from desktops to mobile phones.
*   **PWA Ready:** The portfolio can be installed as a Progressive Web App (PWA).
*   **Sidebar Navigation:** A modern sidebar navigation that is responsive.

## Setup and Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage the project's dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```
*(Note: You may need to create a `requirements.txt` file first by running `pip freeze > requirements.txt` after installing the necessary packages like `Django` and `Pillow`)*

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory by copying the example file:

```bash
cp env.example .env
```

Now, open the `.env` file and fill in the required values, such as your database credentials and a new `DJANGO_SECRET_KEY`.

### 5. Run Database Migrations

Apply the database migrations to create the necessary tables.

```bash
python manage.py migrate
```

### 6. Create a Superuser

Create a superuser account to access the Django admin panel.

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin username and password.

### 7. Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
```

The portfolio will be available at `http://127.0.0.1:8000`.

## Customizing Your Portfolio

To customize your portfolio, navigate to the Django admin panel at `http://127.0.0.1:8000/<your-admin-url>/` and log in with the superuser account you created.

Here's what you can customize:

*   **Site Settings:** Change your name, email, and social media links.
*   **About:** Edit the content of the "About Me" section.
*   **Projects:** Add new projects with titles, descriptions, images, and tags.
*   **Skills:** Add or remove skills and set your proficiency level.
*   **Hobbies:** Add or remove hobbies with emojis and descriptions.
*   **Blogs:** Write and publish blog posts.

## Environment Variables

The following environment variables are used in this project. They should be defined in a `.env` file in the project root.

*   `DEBUG`: Set to `True` for development, `False` for production.
*   `DJANGO_SECRET_KEY`: A strong, unique secret key for Django.
*   `DJANGO_ALLOWED_HOSTS`: A comma-separated list of hosts that this Django site can serve.
*   `CSRF_TRUSTED_ORIGINS`: A comma-separated list of trusted origins for CSRF protection.
*   `DJANGO_ADMIN_URL`: The URL for the Django admin interface (e.g., `admin/`).
*   `DB_NAME`: The name of your database.
*   `DB_USER`: The username for your database.
*   `DB_PASSWORD`: The password for your database.
*   `DB_HOST`: The host of your database (e.g., `localhost`).
*   `DB_PORT`: The port of your database (e.g., `5432` for PostgreSQL).

---

Happy customizing!