# Django Closest Points App

This Django application provides an API that receives a set of points on a grid as semicolon-separated values and finds the points that are closest to each other. The received set of points and the closest points are stored in a database.

## Prerequisites

- Python 3.7 or later
- Django 3.2 or later

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mosesbabu/koa_test.git
cd koa_test
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
# For Linux/Mac
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Perform the database migrations:

```bash
python manage.py migrate
```

## Usage

1. Start the development server:

```bash
python manage.py runserver
```

2. Open your web browser and navigate to `http://localhost:8000/api/closest-points/`.

3. Send a POST request to the API endpoint with the set of points as semicolon-separated values in the following format:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"points": "2,2;-1,30;20,11;4,5"}' http://localhost:8000/api/closest-points/
```

4. The API will return the closest points as a response, and they will be stored in the database.

5. To view the stored points, you can access the Django admin interface by navigating to `http://localhost:8000/admin/` in your browser. Log in using your superuser credentials, and you will find the "Points" model where you can view and manage the stored points.

## Testing

To run the unit tests for the application, execute the following command:

```bash
python manage.py test api.tests
```

## Configuration

- The Django settings can be found in the `closestpoints/settings.py` file. Modify this file to adjust any desired configurations, such as database settings, allowed hosts, or secret key.

## License

This project is licensed under the [MIT License](LICENSE).

