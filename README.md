# 🐦 Tweeter Project

A web application designed to mimic core features of a social media platform like Twitter (X), built using the **Django framework**. This project allows users to post "tweets" and interact with posts.

---

## 🚀 Features

* **User Authentication:** Secure sign-up, login, and logout functionality.
* **Tweet Posting:** Users can create, view, and delete their own posts (tweets).
* **User Profiles:** View individual user profiles with their bio and post history.
* **Timeline/Feed:** Displays a stream of tweets from the users the current user is following.
* **Dynamic Templates:** Utilizes Django's template engine for dynamic content rendering.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap (for responsive design/styling)
* **Database:** SQLite (default for development)
* **Tools:** VS Code, Git, GitHub

---

## 📂 Project Structure

```
Tweeter_Project/
│
├── tweeter/              # Main Django project configuration (settings.py, urls.py, wsgi.py, asgi.py)
├── tweet/                # Django app for core logic
├── static/               # Static files (CSS, JS)
├── templates/            # HTML templates
├── media/                # Directory for user-uploaded content (e.g., profile pictures, images in tweets)
├── db.sqlite3            # Default SQLite database
├── manage.py             # Django's command-line utility for administrative tasks
├── requirements.txt      # List of project dependencies (e.g., Django, pillow)
```
