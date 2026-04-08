# Import python packages.
import streamlit as st

from snowflake.snowpark.functions import col
import requests  

# Write directly to the app.
st.title(f"Zena's Amazing Athleisure Catalog")
st.write(
  """Pick a sweatsuit color or style:
  """
)

cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("ZENAS_ATHLEISURE_DB.products.views.catalog_for_website").select(col('color_or_style')))

colors_list = st.multiselect(
    'Pick a sweatsuit color or style:'
    , my_dataframe 
    , max_selections = 1
)

#if colors_list:
    

#st.dataframe(data=my_dataframe, use_container_width=True)
#st.stop()

