import streamlit as st
import requests

BASE_URL = "http://localhost:5000/reviews"

st.title("🎬 Movie Review App")

# ---------- Add New Review ----------
st.header("➕ Add a New Review")
with st.form("add_review_form"):
    movie_title = st.text_input("🎞️ Movie Title")
    reviewer = st.text_input("🧑 Your Name")
    rating = st.slider("⭐ Rating", 0.0, 5.0, 3.0, 0.1)
    review = st.text_area("📝 Your Review")
    submitted = st.form_submit_button("Submit Review")

    if submitted:
        data = {
            "movie_title": movie_title,
            "reviewer": reviewer,
            "rating": rating,
            "review": review
        }
        res = requests.post(BASE_URL, json=data)
        if res.status_code == 201:
            st.success("✅ Review added successfully!")
        else:
            st.error("❌ Failed to add review.")

# ---------- View and Manage Reviews ----------
st.header("📋 All Reviews")

response = requests.get(BASE_URL)
if response.ok:
    reviews = response.json()

    for r in reviews:
        with st.expander(f"🎬 {r['movie_title']} — {r['rating']}⭐ by {r['reviewer']}"):
            st.write(f"💬 {r['review']}")

            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("🗑️ Delete", key=f"del_{r['id']}"):
                    delete = requests.delete(f"{BASE_URL}/{r['id']}")
                    if delete.status_code == 200:
                        st.success("✅ Review deleted!")
                        st.experimental_rerun()

            with col2:
                if st.button("✏️ Edit", key=f"edit_{r['id']}"):
                    st.session_state["edit_id"] = r["id"]
                    st.session_state["edit_data"] = r

# ---------- Edit Review ----------
if "edit_id" in st.session_state:
    st.header("✏️ Edit Review")

    r = st.session_state["edit_data"]
    with st.form("edit_form"):
        new_title = st.text_input("Movie Title", r["movie_title"])
        new_reviewer = st.text_input("Your Name", r["reviewer"])
        new_rating = st.slider("Rating", 0.0, 5.0, float(r["rating"]), 0.1)
        new_review = st.text_area("Your Review", r["review"])
        update_btn = st.form_submit_button("Update Review")

        if update_btn:
            new_data = {
                "movie_title": new_title,
                "reviewer": new_reviewer,
                "rating": new_rating,
                "review": new_review
            }
            update = requests.put(f"{BASE_URL}/{st.session_state['edit_id']}", json=new_data)
            if update.status_code == 200:
                st.success("✅ Review updated!")
                st.session_state.pop("edit_id")
                st.experimental_rerun()
            else:
                st.error("❌ Failed to update review.")
