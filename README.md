# Instructions for the coding test

## Introduction
Welcome to the coding test for the Nubovi internship. This test is designed to assess your ability to write clean, maintainable code. It is not designed to be difficult, but rather to give us an idea of how you approach problems and how you write code.

## Instructions
In order to complete the test, you will need to develop 5 APIs using Django Rest Framework. We have defined a couple of steps that will get you started. You can find the steps below. To read more about the django cookiecutter template you can review the following [documentation](https://cookiecutter-django.readthedocs.io/en/latest/index.html). Lastly, we are using Docker

### Data
The data for this test is based on the following [Kaggle dataset](https://www.kaggle.com/datasets/thedevastator/top-selling-nintendo-entertainment-system-games) and is located in an Azure Blob Storage container. The data is in the form of a CSV file. You can use the data to populate your database. Below you will find the URLs for the files:
- file_1: https://bluebase.blob.core.windows.net/internship/df_1.csv
- file_2: https://bluebase.blob.core.windows.net/internship/df_3.csv
- file_3: https://bluebase.blob.core.windows.net/internship/df_4.csv
- file_4: https://bluebase.blob.core.windows.net/internship/df_5.csv
- file_5: https://bluebase.blob.core.windows.net/internship/df_6.csv

### Steps to get started:
1. Clone and copy the contents of this repository into your own GitHub repository
2. `pip install virtualenv`
3. `virtualenv venv`
4. `source venv/bin/activate` (MacOS) or `venv\Scripts\activate` (windows)
5. `pip install -r requirements.txt`
6. `cookiecutter gh:cookiecutter/cookiecutter-django`
    - project_name: nintendo_drf
    - project_slug: nintendo_drf
    - description: "A Django REST Framework API for Nintendo games."
    - author_name: "Your Name"
    - domain_name: "nubovi.com"
    - email: "your-email.com"
    - version: "0.1.0"
    - timezone: "UTC"
    - windows: "n"
    - use_pycharm: "n"
    - **use_docker: "y" or "n"**
    - **postgresql_version: "13"**
    - cloud_provider: "None"
    - mail_service: "Other SMTP"
    - **use_async: "y"**
    - **use_drf: "y"**
    - frontend_pipeline: "None"
    - use_celery: "n"
    - use_mailhog: "n"
    - use_sentry: "n"
    - use_whitenoise: "n"
    - use_heroku: "n"
    - ci_tool: "None"
    - **keep_local_envs_in_vcs: "y"**
    - debug: "y"