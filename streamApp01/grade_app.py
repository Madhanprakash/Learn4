import streamlit as st

st.title("Student Grade Tracker")

if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add", clear_on_submit=True):
    name = st.text_input("Name")
    mark = st.number_input("Mark", min_value=0, max_value=100)
    if st.form_submit_button("Add"):
        if name.strip():
            st.session_state.students.append({"Name": name.strip(), "Mark": mark})
            st.success(f"Added {name.strip()}.")
        else:
            st.error("Please enter a student name.")

if st.session_state.students:
    st.subheader("Students")
    st.table(st.session_state.students)

    average_mark = sum(student["Mark"] for student in st.session_state.students) / len(st.session_state.students)
    st.metric("Average mark", f"{average_mark:.1f}")
    st.metric("Total students", len(st.session_state.students))
    st.metric("Highest mark", max(student["Mark"] for student in st.session_state.students))
    st.metric("Lowest mark", min(student["Mark"] for student in st.session_state.students))
    