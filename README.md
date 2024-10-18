
# Project Title

Coastal Peace Hotel Booking



## Details
This is a Hotel Booking Management web application API where general users can create their own accounts and book hotels through API. Below are the features of this API listed:

→ Users can create an account, log in, log out, update their password, and update their profile.

→ They can view various hotels, along with a detailed view.

→ Users can send hotel booking requests.

→ They can deposit into a dummy account.

→ From the history section, users can view all their booking history, as well as check-in, check-out, or cancel bookings.

→ Users can request to become an admin while creating an account.

→ Admins can confirm or cancel booking requests and can promote any user to admin or demote admins back to regular users. Admins can also approve or cancel admin requests.

→ You can visit my web application to explore these features and more.
Link: https://main--enchanting-nougat-9e6718.netlify.app/
## Technology
Django,Django Rest Framework
## Installed Packages
asgiref,
certifi,
charset-normalizer,
dj-database-url,
Django,
django-cors-headers,
django-environ,
django-filter,
djangorestframework,
idna,
packaging,
pillow,
pip,
pipenv,
psycopg2-binary,
requests,
setuptools,
sqlparse,
tzdata,
urllib3,
virtualenv,
whitenoise,
## API Reference

#### Get all hotels

```http
  GET /api/hotel/list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get single hotel

```http
  GET /api/hotel/list/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of hotel to fetch |


#### Get all Booking

```http
  GET /api/booking/list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get single hotel

```http
  GET /api/booking/list/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of booking to fetch |


## Run Locally

Clone the project

```bash
  git clone https://github.com/Sadid205/coastal-peace-hotel-booking-django-final-exam.git
```

Go to the project directory


Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

