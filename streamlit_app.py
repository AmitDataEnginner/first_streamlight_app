import streamlit
import pandas
streamlit.title("My parent's new healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3 and blueberry Oatmeal.")
streamlit.text("🥗Kale, Spinach and rocket smoothie.")
streamlit.text("🐔Hard boiled free-range Egg.")
streamlit.text("🥑🍞Avocado Toast.")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
