import streamlit as st
import requests

def fetch_data(country_name):
    url = f"https://countryapi.io/api/name/{country_name}"
    
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        st.error(f"Request failed: {e}")
        return None
    
    data = response.json()
    if data:
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        currencies = country_data.get("currencies", {})
        currency = ', '.join([f"{v['name']} ({k})" for k, v in currencies.items()]) if currencies else "N/A"
        region = country_data.get("region", "N/A")

        return name, capital, population, area, currency, region
    
    return None

def main():
    st.title("Country Information")
    
    country_name = st.text_input("Enter a country name:")
    
    if country_name:
        country_info = fetch_data(country_name.strip())
        
        if country_info:
            name, capital, population, area, currency, region = country_info
            st.write(f"**Name:** {name}")
            st.write(f"**Capital:** {capital}") 
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area} km²")
            st.write(f"**Currency:** {currency}")
            st.write(f"**Region:** {region}")
        else:
            st.warning("Country not found.")

if __name__ == "__main__":
    main()
