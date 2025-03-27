import streamlit as st
import pandas as pd

st.markdown("""
    <style>
        .stApp {
            background-color: #f4f4f4;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #4CAF50;
            font-size: 36px;
            text-align: center;
            font-weight: bold;
        }
        .subheader {
            color: #333;
            font-size: 22px;
            font-weight: bold;
            margin-top: 20px;
        }
        .dataframe {
            background-color: white;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #008CBA !important;
            color: white !important;
            padding: 10px 20px !important;
            font-size: 18px !important;
            border-radius: 8px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📊 Simple Data Dashboard</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.markdown("<div class='subheader'>🔍 Data Preview</div>", unsafe_allow_html=True)
    st.markdown("<div class='dataframe'>", unsafe_allow_html=True)
    st.write(df.head())
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>📊 Data Summary</div>", unsafe_allow_html=True)
    st.markdown("<div class='dataframe'>", unsafe_allow_html=True)
    st.write(df.describe())
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>🎯 Filter Data</div>", unsafe_allow_html=True)
    columns = df.columns.tolist()
    selected_column = st.selectbox("🔹 Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("🔹 Select Value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.markdown("<div class='dataframe'>", unsafe_allow_html=True)
    st.write(filtered_df)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>📈 Plot Data</div>", unsafe_allow_html=True)
    x_column = st.selectbox("🛠 Select x-axis column", columns)
    y_column = st.selectbox("🛠 Select y-axis column", columns)

    if st.button("📌 Generate Plot"):
        if filtered_df.empty:
            st.error("❌ Error: No data available after filtering! Please select a different filter.")
        else:
            filtered_df[x_column] = filtered_df[x_column].astype(str)
            filtered_df[y_column] = pd.to_numeric(filtered_df[y_column], errors="coerce")

            filtered_df = filtered_df.set_index(x_column)
            st.line_chart(filtered_df[y_column])

else:
    st.write("👀 Waiting for a CSV file upload...")
