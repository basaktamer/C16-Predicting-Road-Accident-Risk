import streamlit as st
import pandas as pd
import joblib

# Set Page Config
st.set_page_config(page_title="Road Accident Risk Predictor", layout="centered")

# Load Model and Feature list
@st.cache_resource
def load_assets():
    model = joblib.load('accident_risk_model.pkl')
    features = joblib.load('features.pkl')
    return model, features

model, model_features = load_assets()

st.title("🚗 Road Accident Risk Assessment")
st.write("Enter the environmental and road conditions to predict the accident risk index.")

# Create Form for Input
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        road_type = st.selectbox("Road Type", options=["highway", "rural", "urban"])
        num_lanes = st.number_input("Number of Lanes", min_value=1, max_value=10, value=2)
        speed_limit = st.slider("Speed Limit (km/h)", 30, 140, 70)
        lighting = st.selectbox("Lighting Conditions", options=["daylight", "dim", "night"])
        time_of_day = st.selectbox("Time of Day", options=["morning", "afternoon", "evening"])
    
    with col2:
        weather = st.selectbox("Weather", options=["clear", "foggy", "rainy"])
        curvature = st.number_input("Road Curvature Index", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        num_reported = st.number_input("Historically Reported Accidents", min_value=0, value=5)
        
        # Booleans
        signs = st.checkbox("Road Signs Present")
        public = st.checkbox("Public Road")
        holiday = st.checkbox("Holiday")
        season = st.checkbox("School Season")

    submit = st.form_submit_button("Predict Risk Score")

if submit:
    # 1. Manual Mapping (Must match your training logic exactly)
    mapping = {
        'road_type': {'highway': 0, 'rural': 1, 'urban': 2},
        'lighting': {'daylight': 0, 'dim': 1, 'night': 2},
        'weather': {'clear': 0, 'foggy': 1, 'rainy': 2},
        'time_of_day': {'morning': 0, 'afternoon': 1, 'evening': 2}
    }

    # 2. Build Input Dataframe
    input_data = pd.DataFrame({
        'road_type': [mapping['road_type'][road_type]],
        'num_lanes': [num_lanes],
        'curvature': [curvature],
        'speed_limit': [speed_limit],
        'lighting': [mapping['lighting'][lighting]],
        'weather': [mapping['weather'][weather]],
        'road_signs_present': [int(signs)],
        'public_road': [int(public)],
        'time_of_day': [mapping['time_of_day'][time_of_day]],
        'holiday': [int(holiday)],
        'school_season': [int(season)],
        'num_reported_accidents': [num_reported]
    })

    # 3. Ensure column order matches training
    input_data = input_data[model_features]

    # 4. Predict
    prediction = model.predict(input_data)[0]
    
    # 5. Display Results
    st.markdown("---")
    st.subheader(f"Predicted Accident Risk: `{prediction:.4f}`")
    
    if prediction > 0.7:
        st.error("Warning: High Risk Level")
    elif prediction > 0.4:
        st.warning("Caution: Moderate Risk Level")
    else:
        st.success("Safe: Low Risk Level")