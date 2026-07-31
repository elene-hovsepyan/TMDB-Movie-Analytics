# TMDB Movie Analytics

## Overview

TMDB Movie Analytics is a Python-based data analysis project built on the TMDB movie dataset containing approximately one million movie and television records.

The project combines data cleaning, exploratory analysis, visualization, and interactive querying to provide insights into movies, genres, languages, ratings, and production information.

Originally developed as a Programming for Data Science course project at the American University of Armenia.

---

## Features

- Dataset cleaning and preprocessing
- Duplicate removal
- Missing value handling
- Movie lookup
- IMDb ID retrieval
- Genre exploration
- Language filtering
- Runtime filtering
- Similar movie recommendations
- Interactive movie information retrieval
- Exploratory Data Analysis
- R visualizations

---

## Technologies

- Python
- pandas
- Jupyter Notebook
- R
- R Markdown

---

## Dataset

The project uses the TMDB Movie Dataset containing approximately one million movie and television records.

The cleaning pipeline:

- removes duplicate movies
- removes incomplete records
- standardizes column types
- exports a cleaned dataset

---

## Repository Structure

```
data/
notebooks/
r/
src/
README.md
requirements.txt
```

---

## Interactive Tools

The repository contains several standalone scripts that allow users to query the cleaned dataset.

Examples include:

- Search by IMDb ID
- Search by genre
- Search by language
- Search by runtime
- Retrieve movie information
- Recommend similar movies

---

## Running the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python src/Movie_Info.py
```

or execute any of the other query scripts.

---

## Authors

Developed by

- Elene Hovsepyan
- Anna Khurshudyan
- Tigran Atayan
- Nane Sarukhanyan
