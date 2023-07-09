import streamlit
streamlit.title('🥗My Parents New healthy Dinner')
streamlit.header('🥑 Breakfast Meenu')
streamlit.text('🍞 Monday - Biled Egg')
streamlit.text('Tuesday - Banana')
streamlit.text('Wed - Fish')
streamlit.text('Thus - Veg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')     

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruit-",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list) 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
