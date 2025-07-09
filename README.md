# E-commerce Product Catalog API (Django REST Framework)

A robust RESTful API for managing an e-commerce product catalog, built with Django and Django REST Framework. Features include product/category management, user authentication (JWT), and role-based authorization.

## Features

- **Product Management:** CRUD operations for products (name, description, price, stock, images, category).
- **Category Management:** CRUD operations for product categories.
- **User Authentication:** Secure JWT (JSON Web Token) authentication for user login and protected endpoints.
- **User Registration:** API endpoint for new user sign-ups.
- **Role-Based Authorization:**
  - **Admin Users:** Full CRUD access to Categories and Products.
  - **Seller Users:** CRUD access to Products, read-only for Categories.
  - **Customer Users:** Read-only access to Products and Categories.
- **Advanced Product Features:**
  - **Pagination:** Efficiently retrieve large lists of products.
  - **Filtering:** Filter products by category, price range, and stock quantity.
  - **Searching:** Search products by name and description.
- **API Documentation:** Interactive API documentation using `drf-spectacular` (Swagger UI).
- **Database:** PostgreSQL for robust data storage.
- **Environment Variables:** Secure configuration management using `python-dotenv`.
- **Version Control:** Managed with Git and hosted on GitHub.

## Technologies Used

- Python 3.x
- Django
- Django REST Framework
- `djangorestframework-simplejwt` (for JWT authentication)
- `drf-spectacular` (for OpenAPI/Swagger documentation)
- `django-filter` (for robust filtering)
- `psycopg2-binary` (PostgreSQL adapter)
- `dj-database-url` & `python-dotenv` (for environment management)
- PostgreSQL
- Git / GitHub

## Setup and Installation

Follow these steps to get the project up and running locally:

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/itimpk/django-ecommerce-api.git (https://github.com/itimpk/django-ecommerce-api.git)
    cd ecommerce_api_django
    ```

2.  **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up PostgreSQL Database:**

    - Ensure PostgreSQL is installed and running on your system.
    - Create a dedicated database and user for the project:
      ```sql
      CREATE DATABASE ecommerce_db;
      CREATE USER ecommerce_user WITH PASSWORD 'your_strong_password';
      ALTER ROLE ecommerce_user SET client_encoding TO 'utf8';
      ALTER ROLE ecommerce_user SET default_transaction_isolation TO 'read committed';
      ALTER ROLE ecommerce_user SET timezone TO 'UTC';
      GRANT ALL PRIVILEGES ON DATABASE ecommerce_db TO ecommerce_user;
      ```
      _Replace `your_strong_password` with a strong, unique password._

5.  **Configure Environment Variables:**

    - Create a `.env` file in the root of the project directory (same level as `manage.py`).
    - Add the following variables, filling in your specific details:
      ```
      DJANGO_SECRET_KEY=your_generated_secret_key
      DJANGO_DEBUG=True
      DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
      DATABASE_URL=postgres://ecommerce_user:your_strong_password@localhost:5432/ecommerce_db
      ```
      _Generate a new `DJANGO_SECRET_KEY` using `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`_

6.  **Run Database Migrations:**

    ```bash
    python manage.py migrate
    ```

7.  **Create a Superuser (for Admin Access):**

    ```bash
    python manage.py createsuperuser
    ```

    _Follow the prompts to create an admin user._

8.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

The API will be accessible at `http://127.0.0.1:8000/api/`.

## API Endpoints

- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **API Documentation (Swagger UI):** `http://127.0.0.1:8000/api/docs/`
- **JWT Token Obtain:** `POST /api/auth/token/`
  - Body: `{ "username": "your_username", "password": "your_password" }`
  - Response: `{ "access": "...", "refresh": "..." }`
- **JWT Token Refresh:** `POST /api/auth/token/refresh/`
- **User Registration:** `POST /api/auth/register/`
  - Body: `{ "username": "new_user", "email": "new@example.com", "password": "pass", "password2": "pass" }`
- **Product Endpoints:**
  - `GET /api/products/` (List all products, with pagination, filtering, searching, and ordering)
  - `GET /api/products/{id}/` (Retrieve a single product)
  - `POST /api/products/` (Create a new product - Seller/Admin only)
  - `PUT /api/products/{id}/` (Update a product - Seller/Admin only)
  - `PATCH /api/products/{id}/` (Partially update a product - Seller/Admin only)
  - `DELETE /api/products/{id}/` (Delete a product - Seller/Admin only)
- **Category Endpoints:**
  - `GET /api/categories/` (List all categories)
  - `GET /api/categories/{id}/` (Retrieve a single category)
  - `POST /api/categories/` (Create a new category - Admin only)
  - `PUT /api/categories/{id}/` (Update a category - Admin only)
  - `PATCH /api/categories/{id}/` (Partially update a category - Admin only)
  - `DELETE /api/categories/{id}/` (Delete a category - Admin only)

## How to Test Permissions

Use Postman or a similar tool.

1.  **Register a `customer` user:** Use `POST /api/auth/register/`.
2.  **Log in as `customer`:** Get a JWT token from `POST /api/auth/token/`. Use this token for `GET` requests (e.g., `/api/products/`). `POST/PUT/DELETE` will be forbidden (403).
3.  **Promote `customer` to `seller`:** Log into `http://127.0.0.1:8000/admin/` with your superuser. Edit the `customer` user and check "Staff status".
4.  **Log in again as `seller` (to get a new token).** Now, `POST/PUT/DELETE` to `/api/products/` will work, but `POST/PUT/DELETE` to `/api/categories/` will still be forbidden (403).
5.  **Log in as `superuser` (admin).** All operations should work.

---

Follow these steps to set up and run the project locally using Docker Compose.

### Running the Application with Docker Compose

1.  **Ensure Docker is Running:** Make sure Docker Desktop (or your Docker daemon) is running on your machine.
2.  **Navigate to the project root:** Open your terminal and change directory to the root of this project (where `docker-compose.yml` is located).
3.  **Build and Run:** Execute the following command to build the images and start the services:
    ```bash
    docker compose up --build
    ```
    This command will:
    - Build the `web` service's Docker image.
    - Start the `db` (PostgreSQL) service.
    - The `web` service will wait for the `db` service to be ready.
    - Run Django database migrations.
    - Start the Django development server.

### Post-Setup & Initial Configuration

After your Docker containers are running, complete these steps to finish setting up your Django application:

1. **Create a Superuser:**

    Open a new terminal window (leave `docker compose up` running) and run:

    ```bash
    docker compose exec web python manage.py createsuperuser
    ```

    Follow the prompts to create your admin credentials.

2. **Access the Django Admin Panel:**

    - Go to [http://localhost:8000/admin/](http://localhost:8000/admin/) in your browser.
    - Log in with the superuser credentials you just created.
    - You should see your Django models (e.g., Categories, Products) listed.

3. **Add Initial Data via API:**

    Use Postman, Insomnia, or VS Code REST Client to add data through the API endpoints:

    - **Categories:** `http://localhost:8000/api/categories/`
    - **Products:** `http://localhost:8000/api/products/`

    Send `POST` requests with the appropriate JSON payloads to create categories and products.

4. **Explore API Documentation:**

    If API documentation is enabled, view it at:

    - **Swagger UI:** `http://localhost:8000/api/schema/swagger-ui/`
    - **Redoc:** `http://localhost:8000/api/schema/redoc/`
