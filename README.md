# 🎨 Art Gallery Manager

A Django web application for managing art exhibits, artists, visitors, and reservation records. Built as a course project for CS348, this app demonstrates strong backend database integration, clean front-end interaction, and cloud deployment.

## 🌐 Live Demo

Visit the live site: [https://artgallerymanage.onrender.com](https://artgallerymanage.onrender.com)

## 📌 Features

- Dynamic dashboard displaying current exhibits and reservations.
- Add new exhibits with dynamic artist selection (existing or new).
- CRUD operations for exhibits and reservations.
- Raw SQL and Django ORM integration.
- Calendar date picker for exhibit scheduling.
- Deployed to Render for public access.

## 🗃️ Database Schema

- **Artists** (`artist_id`, `name`, `country`)
- **Exhibits** (`exhibit_id`, `title`, `date`, `description`, `capacity`, FK to Artist)
- **Visitors** (`visitor_id`, `name`, `email`)
- **Reservations** (`reservation_id`, `visitor_id`, `exhibit_id`, `reserve_date`, `status`)

### Indexes
Indexes were manually defined to optimize JOIN queries for reporting on exhibits and reservations.

## 🧾 Technologies Used

- Python 3.12
- Django 5.1.5
- SQLite3
- HTML/CSS (custom)
- Render (deployment)
- Gunicorn + Whitenoise (for static file handling)

## ⚙️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/JiinM/ArtGalleryManage.git
   cd ArtGalleryManage
