# My Django Blog

Welcome to My Django Blog! This is a personal blog application built using Django, showcasing articles, tutorials, and insights on various tech topics.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)

## Features

### User Features

- **Create Comments**: Users can comment on blog posts to share their thoughts.
- **Subscribe to Posts**: Users can subscribe to receive notifications for new updates on their favourite posts.
- **Bookmark Posts**: Users can bookmark posts to find and read them later easily.

### Admin Features

- **Post Management**: Admins can create, edit, and delete blog posts.
- **Comment Moderation**: Admins can delete inappropriate comments.
- **Subscriber Management**: Admins can view and delete subscribers to manage the audience effectively.
- **Tag Management**: Admins can add tags to posts for better organization and categorization.

## Technologies Used

- [Django](https://www.djangoproject.com/) - A high-level Python web framework.
- [PostgreSQL](https://www.postgresql.org/) - Database management system for the application.
- [AWS S3](https://aws.amazon.com/s3/) - For media file storage.
- [SendGrid](https://sendgrid.com/) - This is for email notifications to users.

## Installation

To get a local copy up and running, follow these simple steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git

   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo-name

   ```

3. Create a virtual environment:

   ```bash
   python -m venv myenv

   ```

4. Activate the virtual environment:
   On Windows:

   ```bash
    myenv\Scripts\activate

   On mac/OS/Linux:
   source myenv/bin/activate

   ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt

   ```

6. Run the development server:

   ```bash
   python manage.py runserver



   ```
