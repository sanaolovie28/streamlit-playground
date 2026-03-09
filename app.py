import streamlit as st
from datetime import date

st.set_page_config(page_title="PhotoDiary", layout="wide")

st.title("MEMONTIA PHOTODIARY")

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Create Entry", "My Diary", "Mood Tracker", "About"]
)

#HOME
if page == "Home":
    st.header("Welcome to PhotoDiary! ^^")
    name = st.text_input("Enter your name")

    mood = st.radio(
        "How are you feeling today?",
        ["Happy", "Calm", "Excited", "Sad"]
    )

    rating = st.slider("Rate your day", 1, 10)

    st.metric("Mood Score", rating)

#CREATE ENTRY
elif page == "Create Entry":

    st.header("Create a New Diary Entry")

    diary_date = st.date_input("Select Date", date.today())

    time = st.time_input("Time of memory")

    photo = st.file_uploader("Upload a Photo")

    camera = st.camera_input("Or take a photo")

    caption = st.text_area("Write a caption")

    tags = st.multiselect(
        "Tags",
        ["Friends", "School", "Family", "Travel", "Food"]
    )

    color = st.color_picker("Mood color")

    favorite = st.checkbox("Mark as favorite")

    if st.button("Save Entry"):
        st.success("Diary entry saved!")

#DIARY
elif page == "My Diary":

    st.header("My Photo Gallery")

    tab1, tab2 = st.tabs(["Photos", "Summary"])

    with tab1:
        st.image(
            "492406368_986084790401678_8352782846114806558_n.jpg",
            caption="Sample Memory"
        )

    with tab2:
        st.progress(80)
        st.write("You had a productive day!")

#MOOD TRACKER
elif page == "Mood Tracker":

    st.header("Mood Tracker")

    col1, col2 = st.columns(2)

    col1.metric("Happy Days", "5")
    col2.metric("Average Mood", "8/10")

#ABOUT
elif page == "About":

    st.header("About This App")

    st.write("""
    PhotoDiary is a simple digital journal where users can capture
    memories using photos and notes.

    Target Users:
    Students and individuals who want to document daily moments.

    Inputs Collected:
    Name, mood, photos, captions, tags, and date.

    Outputs:
    Displayed photo entries, mood tracking, and diary summaries.
    """)

    st.caption("Built with Streamlit.")
