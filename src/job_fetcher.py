
import requests
import pandas as pd


API_URL = "https://www.arbeitnow.com/api/job-board-api"


def fetch_jobs():
    """
    Fetch real job vacancies from the Arbeitnow API.
    """
    try:
        response = requests.get(API_URL, timeout=30)
        response.raise_for_status()

        data = response.json()["data"]

        jobs = pd.DataFrame(data)

        return jobs

    except requests.RequestException as error:
        print(f"Error fetching jobs: {error}")
        return pd.DataFrame()

    except (ValueError, KeyError) as error:
        print(f"Error processing API response: {error}")
        return pd.DataFrame()


if __name__ == "__main__":
    jobs = fetch_jobs()

    print(f"\nTotal vacancies fetched: {len(jobs)}")

    if not jobs.empty:
        print("\nFirst 5 vacancies:")
        print(jobs[["title", "company_name", "location"]].head())
