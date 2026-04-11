# job-market-analyzer

Scalable data pipeline for collecting and analyzing job market data, extracting key skills, and providing insights into technology trends in Finland.
A data engineering project that collects, processes, and analyzes job market data to identify trends in skills, salaries, and demand.

 Overview

This project simulates a real-world data pipeline:

 Collect job postings from APIs
 Clean and normalize raw data
 Store structured data in a database
 Analyze job market trends
 Visualize insights
Architecture
Data Source → Ingestion → Processing → Storage → Analysis → Visualization
Tech Stack
Python (Pandas, Requests)
SQL (SQLite / PostgreSQL)
Docker
Pytest
Project Structure
job-market-analyzer/
│
├── src/job_market_analyzer/
│   ├── ingestion/       # Data collection
│   ├── processing/      # Cleaning & transformation
│   ├── storage/         # Database logic
│   ├── analysis/        # Data analysis
│   └── visualization/   # Charts and plots
│
├── scripts/             # Pipeline entrypoints
├── tests/               # Unit tests
├── data/                # Raw & processed data
└── README.md
How to Run
1. Clone repository
git clone https://github.com/your-username/job-market-analyzer.git
cd job-market-analyzer
2. Install dependencies
pip install -r requirements.txt
3. Run pipeline
python scripts/run_pipeline.py
 Example Insights
Most in-demand skills: Python, SQL, AWS
Salary distribution by role
Job trends over time

Testing

pytest

Docker

docker build -t job-analyzer .
docker run job-analyzer

Purpose

This project was built as part of my portfolio to showcase real-world data engineering skills.

It demonstrates mid-level data engineering skills, including:

Data pipeline design (ETL workflows)
Data cleaning and transformation
Database integration (SQL)
Modular and scalable project structure
Production-ready practices (testing, reproducibility)

Author

Data Engineer / Python Developer
Based in Helsinki

