# European Job Market Analyzer

A Python-based project for collecting and exploring job vacancies through a public job board API.

The project demonstrates practical skills in Python, data collection, data analysis, and interactive dashboard development.

## Overview

European Job Market Analyzer retrieves current job vacancy data from the [Arbeitnow Job Board API](https://www.arbeitnow.com/api/job-board-api) and presents it in an interactive Streamlit dashboard.

The goal is to explore available job listings and identify patterns in job titles, locations, companies, and vacancy tags.

## Current Features

- Fetches live job vacancy data from the Arbeitnow API
- Displays the total number of vacancies
- Shows the number of companies and locations
- Filters job listings by location
- Visualizes the most frequent vacancy tags
- Displays job listings in an interactive table
- Provides direct links to job applications

## Technology Stack

- Python
- Pandas
- Requests
- Streamlit
- Git and GitHub

## Project Structure

```text
job-market-analyzer/
│
├── app.py                  # Streamlit dashboard
├── requirements.txt        # Project dependencies
├── data/
│   └── sample_jobs.csv     # Sample job vacancy data
│
└── src/
    ├── __init__.py
    ├── analyzer.py         # Analysis of sample job data
    └── job_fetcher.py      # Fetches live data from the API
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/novaheyday/job-market-analyzer.git
cd job-market-analyzer
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the dashboard

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## Data Source and Limitations

The dashboard currently uses the public Arbeitnow Job Board API.

Please note:

- The available vacancies depend on the API response at the time of retrieval.
- The returned listings may be concentrated in particular countries or regions, including Germany.
- The API data does not currently provide a reliable salary field for this project.
- Location values may represent cities or other location descriptions rather than standardized countries.
- Vacancy tags are supplied by the source and may include categories beyond technical skills.
- An internet connection and API availability are required to fetch live data.

The `data/sample_jobs.csv` file contains sample data for local analysis. It is separate from the live API data used by the dashboard.

## Project Status

This is an independent portfolio project under active development.

Planned improvements include:

- Data cleaning and standardization
- More detailed analysis of job requirements
- Better geographical analysis across European markets
- Historical data collection and trend analysis

## Author

Independent Python Developer

Helsinki, Finland

