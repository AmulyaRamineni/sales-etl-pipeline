# Sales ETL Pipeline (Postgres + Docker)

This is a small end‑to‑end ETL pipeline I built to practice core data engineering skills. It takes raw e‑commerce sales data from CSV files, cleans and transforms it with Python, and loads it into a PostgreSQL database running in Docker.

## Why I built this

I’m learning data engineering and wanted a hands‑on project that touches real tools instead of just theory. In this project I practiced working with raw data, cleaning it, designing simple tables, and running everything in a reproducible Docker setup.

## Tech stack

- Python for the ETL logic  
- Pandas for data cleaning and transformations  
- PostgreSQL as the target database  
- Docker and Docker Compose to run the database locally  
- Git & GitHub for version control and project hosting  

## What the pipeline does

- Reads raw e‑commerce transaction data from CSV files in the `data` folder.  
- Cleans and transforms the data (fixes types, handles missing values, does basic validations).  
- Loads the cleaned data into PostgreSQL tables running inside a Docker container.  
- Makes it easy to rerun the pipeline from scratch on any machine with Docker and Python installed.  

## Project structure

```text
sales-etl-pipeline/
├── data/
│   ├── raw/          # Raw CSV input files
│   └── processed/    # (Optional) Processed/intermediate files
├── src/
│   ├── etl/          # ETL modules (extract, transform, load)
│   └── main.py       # ETL entrypoint script
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md

## **What I learned**

- How to design a simple analytical schema for sales reporting.
- How to build an end-to-end ETL pipeline in Python using Pandas.
- How to run PostgreSQL in Docker and connect to it from Python.
- How to structure and document a data engineering project for GitHub.

