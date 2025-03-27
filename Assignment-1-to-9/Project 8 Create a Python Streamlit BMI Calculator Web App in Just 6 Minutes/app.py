import streamlit as st  

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.markdown(
    """
    <style>
        /* Background Color */
        .stApp {
           background: linear-gradient(to right, #FFD1E3, #F4E2D8);
        }
        /* Main Card */
        .main-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
        }
        /* Title */
        .title {
            color: #FF5733;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        /* BMI Result */
        .bmi-result {
            font-size: 24px;
            font-weight: bold;
            color: #1E90FF;
            text-align: center;
            margin-top: 10px;
        }
        /* Footer */
        .footer {
            text-align: center;
            color: #808080;
            margin-top: 20px;
            font-size: 14px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 class='title'>BMI Calculator 🏋️‍♂️</h1>", unsafe_allow_html=True)

height = st.slider("📏 Enter your height (in cm):", 100, 250, 175)
weight = st.slider("⚖️ Enter your weight (in kg):", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.markdown(f"<p class='bmi-result'>Your BMI is {bmi:.2f}</p>", unsafe_allow_html=True)

if bmi < 18.5:
    st.warning("⚠️ Underweight: You may need to gain some weight for better health!")
    st.markdown("<p style='color: #FFA500; text-align: center;'>Consider a balanced diet! 🍎🥑</p>", unsafe_allow_html=True)

elif 18.5 <= bmi <= 24.9:
    st.success("✅ Normal Weight: Great! You are in a healthy range. 🎉")
    st.markdown("<p style='color: #2ECC71; text-align: center;'>Keep up your healthy lifestyle! 🏃‍♀️💪</p>", unsafe_allow_html=True)

elif 25 <= bmi <= 29.9:
    st.warning("⚠️ Overweight: You may need to manage your weight.")
    st.markdown("<p style='color: #FFA500; text-align: center;'>Consider regular exercise! 🚴‍♂️🏊</p>", unsafe_allow_html=True)

else:
    st.error("❗ Obesity: Higher health risks, consider consulting a doctor.")
    st.markdown("<p style='color: #FF4500; text-align: center;'>Focus on a healthier lifestyle! 🏥🥗</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p class='footer'>Made with ❤️ by Amna | Stay Healthy! 🌿</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
