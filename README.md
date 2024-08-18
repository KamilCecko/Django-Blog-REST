# Django Blog REST

A Django application for creating and managing blogs with REST framework support.

## Requirements

- Python 3.8+
- Django 5.1

## Dependencies

- `Django` 5.1
- `django-ckeditor` 6.7.1
- `django-js-asset` 2.2.0
- `djangorestframework` 3.15.2
- `djangorestframework-simplejwt` 5.3.1
- `pillow` 10.4.0
- `PyJWT` 2.9.0
- `sqlparse` 0.5.1
- `tzdata` 2024.1
- `asgiref` 3.8.1

## Project Overview

### 1. `member` Application

- **Purpose**: Manages user accounts.
- **Features**:
  - Account creation.
  - Data updates.
  - Password changes.
  - Profile management.
  - Authentication via JSON Web Tokens (JWT) or session authentication.

### 2. `theblog` Application

- **Purpose**: Manages blogs and related features.
- **Features**:
  - Blog creation and editing.
  - Category management.
  - Commenting on blogs.
  - Storage of static files and user-uploaded images.

The project is designed to be fully interactive through APIView, providing comprehensive API endpoints for interaction.
## Installation


1. **Clone the repository**:
   ```bash
   git clone https://github.com/KamilCecko/Django-Blog.git
   
2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```
