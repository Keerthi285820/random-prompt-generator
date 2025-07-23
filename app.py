import streamlit as st
import json
import random

# Load prompts
def load_prompts():
    with open("prompts.json", "r") as f:
        return json.load(f)

# Get unique categories
def get_categories(prompts):
    return sorted(set(p["category"] for p in prompts))

# UI
st.set_page_config(page_title="Random Prompt Generator", layout="centered")
st.title("🎲 Random Prompt Generator")

# Load prompts
prompts = load_prompts()
categories = get_categories(prompts)

# Category filter
selected_category = st.selectbox("Choose a Category", ["All"] + categories)

# Button to generate
if st.button("Get Prompt"):
    if selected_category == "All":
        prompt = random.choice(prompts)
    else:
        filtered = [p for p in prompts if p["category"] == selected_category]
        prompt = random.choice(filtered) if filtered else {"prompt": "No prompt found."}
    
    st.markdown(f"### ✏️ Prompt:\n**{prompt['prompt']}**")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
