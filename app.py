import streamlit as st
import pandas as pd

st.set_page_config(page_title="LabSync MVP")

st.title("LabSync – Minimal MVP")
st.write("AI-assisted Lab Reallocation (Proof of Concept)")

data = {
    "lab_id": ["Lab-A", "Lab-B", "Lab-C"],
    "capacity": [60, 40, 50],
    "is_placement": [True, False, False]
}

df = pd.DataFrame(data)

st.subheader("Input: Simulated Lab Schedules")
st.dataframe(df)

placement_lab = df[df["is_placement"]]

if not placement_lab.empty:
    required_capacity = placement_lab.iloc[0]["capacity"]

    alternatives = df[
        (df["is_placement"] == False) &
        (df["capacity"] >= required_capacity - 20)
    ].copy()

    alternatives["score"] = alternatives["capacity"] / required_capacity
    alternatives = alternatives.sort_values("score", ascending=False)
    alternatives["rank"] = range(1, len(alternatives) + 1)

    st.subheader("Detected Conflict")
    st.write(f"{placement_lab.iloc[0]['lab_id']} is used for placement")

    st.subheader("Recommended Alternative Labs")
    st.dataframe(alternatives)
else:
    st.success("No conflicts detected")