import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔒 Password Strength Checker")

# Take password input
password = st.text_input("Enter Your Password", type="password")
feedback = []
score = 0

# Check only if user enters a password
if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase + Lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Special character check
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%&*).")

    # Final rating
    if score == 4:
        feedback.append("✔️ Your password is strong! 🎉")
    elif score == 3:
        feedback.append("🟠 Your password is medium strength. It could be stronger.")
    else:
        feedback.append("🟡 Your password is weak. Please make it stronger.")

    # Show feedback
    st.markdown("## 🔍 Feedback & Suggestions")
    for tip in feedback:
        st.write(tip)

else:
    st.info("Please enter your password above to get started.")
