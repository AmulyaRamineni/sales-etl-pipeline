# Sales ETL Pipeline (Postgres + Docker)

This is a small end‑to‑end ETL pipeline I built to practice core data engineering skills. It takes raw e‑commerce sales data from CSV files, cleans and transforms it with Python, and loads it into a PostgreSQL database running in Docker.

## Why I built this

I’m learning data engineering and wanted a hands‑on project that touches real tools instead of just theory. In this project I practiced working with raw data, cleaning it, designing simple tables, and running everything in a reproducible Docker setup.[web:193][web:199]

## Tech stack

- Python for the ETL logic
- Pandas for data cleaning and transformations
- PostgreSQL as the target database
- Docker and docker-compose to run the database locally

## What the pipeline does

- Reads raw e‑commerce transaction data from CSV files in the `data` folder.
- Cleans and transforms the data (fixes types, handles missing values, does basic validations).
- Loads the cleaned data into PostgreSQL tables running inside a Docker container.
- Makes it easy to rerun the pipeline from scratch on any machine with Docker and Python installed.[web:197][web:199]

## Project structure

- `src/` – ETL code (extract, transform, load).
- `data/` – raw (and optionally processed) CSV files.
- `docker-compose.yml` – spins up PostgreSQL using Docker.
- `requirements.txt` – Python dependencies for the project.
- `README.md` – documentation and project overview.[web:197][web:199]

## How to run the project

1. Clone this repository.
2. Create and activate a virtual environment.
3. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
