streamlit.title('🥗My Parents New healthy Dinner')
streamlit.header('🥑 Breakfast Meenu')
streamlit.text('🍞 Monday - Biled Egg')
streamlit.text('Tuesday - Banana')
streamlit.text('Wed - Fish')
streamlit.text('Thus - Veg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')     

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

           
