import streamlit as st
from os import getenv
import dotenv
import requests


dotenv.load_dotenv()

API_KEY: str = getenv("API_KEY")
URL: str = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
FILE_PATH: str = "image.jpg"

def load_image() -> None:
    """
    Downloads the image using the URL and saves it to a file.
    """
    content: dict[str, any] = requests.get(URL).json()
    picture: str = content['hdurl']

    with open(FILE_PATH, 'wb') as f:
        f.write(requests.get(picture).content)

def main() -> None:
    """
    Main function that displays the image and description on a web page.
    """
    st.title("Astronomy Picture of the Day")
    content: dict[str, any] = requests.get(URL).json()
    picture: str = content['hdurl']
    description: str = content['explanation']

    st.image(picture)
    st.write("##")
    st.write(description)
    load_image()


if __name__ == '__main__':
    main()