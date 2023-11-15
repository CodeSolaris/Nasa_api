import streamlit as st
from os import getenv
import requests
from datetime import datetime, timedelta
def main():
    st.title("Nasa One day picture")
    today = datetime.now()
    yesterday = today - timedelta(days=1)

    API_KEY = getenv('API_KEY')
    URL = ""

if __name__ == '__main__':
    main()