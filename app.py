
import streamlit as st
import joblib

# Load model and column names
model = joblib.load("house_price_model.pkl")
columns = joblib.load("model_columns.pkl")

# Page UI
st.title("🏠 : House Price Prediction App")
st.write("Enter house details to predict the price")

# Input fields
area = st.number_input("Area (in sq ft)", 500, 10000, step=100)
bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
stories = st.selectbox("Stories", [1, 2, 3, 4])
mainroad = st.selectbox("Main Road", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwater = st.selectbox("Hot Water Heating", ["Yes", "No"])
aircon = st.selectbox("Air Conditioning", ["Yes", "No"])
parking = st.selectbox("Parking Spaces", [0, 1, 2, 3])
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])
furnishing = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# Convert inputs
def encode_yes_no(val): return 1 if val == "Yes" else 0

input_data = {
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "mainroad": encode_yes_no(mainroad),
    "guestroom": encode_yes_no(guestroom),
    "basement": encode_yes_no(basement),
    "hotwaterheating": encode_yes_no(hotwater),
    "airconditioning": encode_yes_no(aircon),
    "parking": parking,
    "prefarea": encode_yes_no(prefarea),
    "furnishingstatus_semi-furnished": 0,
    "furnishingstatus_unfurnished": 0
}

# Set furnishing values
if furnishing == "semi-furnished":
    input_data["furnishingstatus_semi-furnished"] = 1
elif furnishing == "unfurnished":
    input_data["furnishingstatus_unfurnished"] = 1

# Final input for prediction
final_input = [input_data[col] if col in input_data else 0 for col in columns]

# Predict
if st.button("Predict Price"):
    prediction = model.predict([final_input])[0]
    st.success(f"Estimated House Price: ₹ {round(prediction, 2)}")
