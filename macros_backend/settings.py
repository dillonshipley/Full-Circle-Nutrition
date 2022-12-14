"""
Django settings for macros_backend project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import environ
import os

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(env("DEBUG_MODE"))

ALLOWED_HOSTS = ["*"]

# Logging Config

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname}\t[{asctime}] | {name} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname}\t[{asctime}] | {message}",
            "style": "{",
        },
        "test": {
            "format": "{levelname}\t[{asctime}] | Filename: {module} Test method: {funcName} Output: {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "test": {
            "class": "logging.FileHandler",
            "filename": "logs/test.log",
            "formatter": "test",
        },
        "recipes_admin": {
            "class": "logging.FileHandler",
            "filename": "logs/admin.log",
            "formatter": "verbose",
        },
        "recipes": {
            "class": "logging.FileHandler",
            "filename": "logs/recipes.log",
            "formatter": "simple",
        },
        "users": {
            "class": "logging.FileHandler",
            "filename": "logs/users.log",
            "formatter": "simple",
        },
        "ingredients": {
            "class": "logging.FileHandler",
            "filename": "logs/ingredients.log",
            "formatter": "simple",
        },
        "migrations": {
            "class": "logging.FileHandler",
            "filename": "logs/migrations.log",
            "formatter": "simple",
        },
    },
    "loggers": {
        "recipes": {"handlers": ["recipes"], "level": "DEBUG", "propagate": True},
        "users": {"handlers": ["users"], "level": "DEBUG", "propagate": True},
        "ingredients": {
            "handlers": ["ingredients"],
            "level": "DEBUG",
            "propagate": True,
        },
        "test": {"handlers": ["test"], "level": "DEBUG", "propagate": True},
        "recipe_admin": {
            "handlers": ["recipes_admin"],
            "level": "DEBUG",
            "propagate": True,
        },
        "migration_logs": {
            "handlers": ["migrations"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["migrations"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "recipes",
    "users",
    "ingredients",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "macros_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "macros_backend.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": f"{env('POSTGRES_USER')}",
        "PASSWORD": f"{env('POSTGRES_PASSWORD')}",
        "HOST": f"{env('POSTGRES_HOST')}",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
