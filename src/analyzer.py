
import pandas as pd


def load_jobs(file_path="data/sample_jobs.csv"):
    """
    Load job vacancies from a CSV file.
    """
    try:
        jobs = pd.read_csv(file_path)
        return jobs
    except FileNotFoundError:
        print("Error: Job data file was not found.")
        return pd.DataFrame()


def jobs_by_country(jobs):
    """
    Count job vacancies by country.
    """
    return jobs["country"].value_counts()


def average_salary(jobs):
    """
    Calculate average salary by country.
    """
    return jobs.groupby("country")["salary"].mean().sort_values(
        ascending=False
    )


def popular_skills(jobs):
    """
    Identify the most frequently requested skills.
    """
    skills = jobs["skills"].dropna().str.split(",")
    skills = skills.explode().str.strip()

    return skills.value_counts()


if __name__ == "__main__":
    jobs = load_jobs()

    if not jobs.empty:
        print("\n=== EUROPEAN JOB MARKET ANALYZER ===")

        print("\nJob vacancies by country:")
        print(jobs_by_country(jobs))

        print("\nAverage salary by country:")
        print(average_salary(jobs))

        print("\nMost popular skills:")
        print(popular_skills(jobs))
