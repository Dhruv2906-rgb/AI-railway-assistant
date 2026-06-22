import requests
import streamlit as st

st.set_page_config(
    page_title="AI Railway Assistant",
    page_icon="🚆"
)

st.title("🚆 AI Railway Assistant")

source = st.text_input("Source Station")

destination = st.text_input("Destination Station")

budget = st.number_input(
    "Budget (₹)",
    min_value=100,
    value=1000
)

date = st.text_input(
    "Travel Date",
    placeholder="Tomorrow"
)

if st.button("Generate Travel Plan"):

    if not source or not destination:
        st.warning("Please enter source and destination.")
    else:

        payload = {
            "source": source,
            "destination": destination,
            "budget": budget,
            "date": date
        }

        try:

            response = requests.post(
                "http://127.0.0.1:8000/plan",
                json=payload
            )

            result = response.json()

            st.success("Travel Plan Generated")

            st.markdown(result["response"])

        except Exception as e:
            st.error(f"Error: {e}")