
import streamlit as st

from src.job_fetcher import fetch_jobs


st.set_page_config(
    page_title="European Job Market Analyzer",
    page_icon="📊",
    layout="wide",
)

st.title("European Job Market Analyzer")
st.write("Explore real job vacancies from the Arbeitnow API.")

# Load real job vacancies
with st.spinner("Loading real job vacancies..."):
    jobs = fetch_jobs()

if jobs.empty:
    st.error("No job data available. Please try again later.")

else:
    st.subheader("Job Market Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total vacancies", len(jobs))

    with col2:
        st.metric("Companies", jobs["company_name"].nunique())

    with col3:
        st.metric("Locations", jobs["location"].nunique())

    st.subheader("Filter Vacancies")

    locations = sorted(
        jobs["location"].dropna().unique().tolist()
    )

    selected_location = st.selectbox(
        "Select location",
        ["All locations"] + locations
    )

    if selected_location != "All locations":
        filtered_jobs = jobs[
            jobs["location"] == selected_location
        ]
    else:
        filtered_jobs = jobs

    st.write(f"Showing {len(filtered_jobs)} vacancies")


    st.subheader("Most In-Demand Skills")

    skill_tags = jobs["tags"].dropna().explode()
    skill_tags = skill_tags.astype(str).str.strip()
    skill_tags = skill_tags[skill_tags != ""]

    skill_counts = skill_tags.value_counts().head(10)

    if not skill_counts.empty:
        st.bar_chart(skill_counts)
    else:
        st.info("No skill tags available.")


    st.subheader("Job Listings")

    st.dataframe(
        filtered_jobs[
            ["title", "company_name", "location", "remote", "url"]
        ],
        width="stretch",
        column_config={
            "url": st.column_config.LinkColumn("Job application")
        },
        hide_index=True,
    )
