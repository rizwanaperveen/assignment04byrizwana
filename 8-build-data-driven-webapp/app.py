import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ("🏠 Home", "📖 About", "📬 Contact","🤖 Projects"))

# Home Page
if page.startswith("🏠"):
    st.title("Welcome to My Portfolio 👋")
    st.write("""
    Hi! I'm **Rizwana Perveen**, a passionate developer/designer/content creator.
    Explore the sections to know more about me!
    """)
    st.image("mydoll.jpeg",caption="Hi, I'm [Rizwana Perveen](https://www.linkedin.com/in/rizwana-perveen/]!", width=300)

# About Page
elif page.startswith("📖"):
    st.title("About Me 📘")
    st.write("""
    I'm skilled in:
    - 🔹 Full-stack development
    - 🔹 UI/UX Design
    - 🔹 Python, JavaScript, HTML, CSS
    - 🔹 Tools like Figma, Streamlit, Canva

    I'm passionate about building impactful web applications and creative designs.
    """)

# Contact Page
elif page.startswith("📬"):
    st.title("Get in Touch ✉️")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thanks for reaching out! I'll get back to you soon.")
# Project page
elif page.startswith("🤖"):
    st.title("Projects 📬")
    st.subheader("My Projects")

    # Define projects as a list of tuples: (image_path, caption, link_text, link_url)
    projects = [
        ("unit.png", "Unit Converter", "⚖️ Unit Converter", "https://unit-converter101-rizwana.streamlit.app/"),
        ("password.png", "Password Generator", "🔑 Password Generator", "https://password-generate.streamlit.app/"),
        ("joke.png", "Joke Generator", "🤣 Joke Generator", "https://joke-generate-madeby-rizwana.streamlit.app/"),
        ("library.png", "Library Manager", "📚 Library Manager", "https://librarymadebyrizwana.streamlit.app/")
    ]

    # Loop through projects and display them two per row
    for i in range(0, len(projects), 2):
        cols = st.columns(2)
        for col, project in zip(cols, projects[i:i+2]):
            img, caption, link_text, url = project
            col.image(img, caption=caption, width=250)
            col.markdown(f"- [{link_text}]({url})")


# Footer (Optional)
st.markdown("""<hr style="height:1px;border:none;color:#ccc;background-color:#ccc;" />""", unsafe_allow_html=True)
st.markdown("© 2025 RIZWANA PERVEEN | Built with ❤️ using Streamlit", unsafe_allow_html=True)
