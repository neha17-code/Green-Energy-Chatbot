import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Green Energy Awareness Chatbot",
    page_icon="🌱",
    layout="centered"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🌱 Green Energy Awareness Chatbot")
st.write("Ask about renewable energy subsidies, ROI, carbon savings, and government schemes.")

# -----------------------------
# CHAT LOGIC FUNCTION
# -----------------------------
def chatbot_response(user_input):

    user_input = user_input.lower()

    # Solar Subsidy
    if "solar subsidy" in user_input:
        return "In India, rooftop solar systems are eligible for government subsidies under the PM Surya Ghar scheme. Residential users can get up to 40% subsidy depending on system capacity."

    # ROI
    elif "roi" in user_input or "return on investment" in user_input:
        return "Rooftop solar systems typically recover investment in 4–6 years. After that, electricity savings become profit."

    # Carbon Savings
    elif "carbon" in user_input:
        return "Installing 1 kW of solar can reduce approximately 1–1.5 tons of CO₂ emissions per year."

    # Wind Energy
    elif "wind" in user_input:
        return "Wind energy is suitable for high-wind regions. It is widely used for commercial and large-scale power generation."

    # Government Scheme
    elif "government scheme" in user_input or "scheme" in user_input:
        return "India promotes renewable energy through schemes like PM Surya Ghar Yojana, National Solar Mission, and state-level subsidy programs."

    # Installation Cost
    elif "cost" in user_input:
        return "Rooftop solar installation costs range from ₹45,000 to ₹60,000 per kW before subsidy."

    # Default reply
    else:
        return "I'm here to help with renewable energy information. Please ask about solar subsidy, ROI, carbon savings, cost, or government schemes."


# -----------------------------
# INPUT BOX
# -----------------------------
user_question = st.text_input("Enter your question:")

# -----------------------------
# BUTTON ACTION
# -----------------------------
if st.button("Ask"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = chatbot_response(user_question)
        st.success(response)