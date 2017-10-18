# Django OpenID Connect User

An extended User model that is designed to have the majority of the attributes of what the OpenID Connect specification mentions.

## How to install

Installation can be done with a single command:

```
$ pip install django-oidc-user
```

## How to use

Setup in your project is easy. Just add it to your installed apps:

```python
INSTALLED_APPS = [
    . . .
    'django_oidc_user',
]
```

And you will need to set it as your default User model, so add the following line to your settings:

```python
AUTH_USER_MODEL = 'django_oidc_user.User'
```

After you have done this make sure you **run migrations** using the following command:

```
$ python manage.py migrate django_oidc_user
```

You can import the model to use in your views like so:

```python
from django_oidc_user.models import User
```
