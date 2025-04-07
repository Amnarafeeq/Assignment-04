import streamlit as st
import requests

st.markdown("""
    <style>
    .stApp {
        background-color: #e6f2ff;
    }

    .main {
        padding: 30px;
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }

    h1 {
        color: #0066cc;
        text-align: center;
        font-weight: 700;
        font-size: 40px;
        margin-bottom: 30px;
    }

    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #333333;
        border: 2px solid #66b3ff;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
        transition: all 0.3s ease-in-out;
    }

    .stTextInput > div > div > input:focus {
        border-color: #3399ff;
        outline: none;
        box-shadow: 0 0 10px rgba(51, 153, 255, 0.3);
    }

    .stSubheader {
        color: #004d99;
        font-size: 26px;
        font-weight: 600;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .stMarkdown {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #cce6ff;
        box-shadow: 0 2px 10px rgba(0, 102, 204, 0.1);
        font-size: 18px;
        margin-bottom: 10px;
    }

    .stError {
        color: #cc0000;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        region = country_data.get("region", "N/A")

        currencies = country_data.get("currencies", {})
        if currencies:
            currency_name = list(currencies.values())[0]["name"]
        else:
            currency_name = "N/A"

        return name, capital, population, area, currency_name, region
    else:
        return None

def main():
    st.title("Country Information App")   

    country_name = st.text_input("Enter a country name:") 
    if country_name:
        country_name_check = country_name.strip().lower()
        country_info = fetch_country_data(country_name_check)
        if country_info:
            name, capital, population, area, currency, region = country_info

            st.subheader("Country Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area} km²")
            st.write(f"**Currency:** {currency}")
            st.write(f"**Region:** {region}")

        else:
            st.error("❌ Error: Country data not found")

if __name__ == "__main__":
    main()
