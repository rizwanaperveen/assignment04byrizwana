import streamlit as st
import requests


def fetch_data(country_name):
    url = f"https://restcountries.com/v3/name/{country_name}"

    response = requests.get(url, verify=False)


    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country-data["name"]["common"]
        capital = country_data["capital"][0]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currencies"]
        region = country_data["region"]

        return name, capital, population, area, currency, region
    else:
        return None


def main():
    st.title("Country Information")

    country_name = st.text_input("Enter a country name:")

    if country_name:
        country_info = fetch_data(country_name)

        if country_info:
            name, capital, population, area, currency, region = country_info
            st.write(f"Name: {name}")
            st.write(f"Capital: {capital}") 
            st.write(f"Population: {population}")
            st.write(f"Area: {area}")
            st.write(f"Currency: {currency}")
            st.write(f"Region: {region}")
        else:
            st.write("Country not found.")                              
if __name__ == "__main__":
    main()