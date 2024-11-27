# django-crud
eva2

## Setting up the development environment

1. Clone the repository:
   ```sh
   git clone https://github.com/brypro/django-crud.git
   cd django-crud
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Django application

1. Apply the migrations:
   ```sh
   python manage.py migrate
   ```

2. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

3. Run the development server:
   ```sh
   python manage.py runserver
   ```

4. Open your web browser and go to `http://127.0.0.1:8000/products` to see the application running.

## Using Docker and Docker Compose

1. Build and start the containers:
   ```sh
   docker-compose up --build
   ```

2. Apply the migrations:
   ```sh
   docker-compose exec app python manage.py migrate
   ```

3. Create a superuser:
   ```sh
   docker-compose exec app python manage.py createsuperuser
   ```

4. Open your web browser and go to `http://127.0.0.1:8000/products` to see the application running.
