# Import python packages.
import streamlit as st

from snowflake.snowpark.functions import col
import requests  

# Write directly to the app.
st.title(f"Zena's Amazing Athleisure Catalog")

cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("ZENAS_ATHLEISURE_DB.products.catalog_for_website").select(col('color_or_style'))

color = st.multiselect(
    'Pick a sweatsuit color or style:'
    , my_dataframe 
    , max_selections = 1
)

st.write(color)

my_dataframe = session.table("ZENAS_ATHLEISURE_DB.products.catalog_for_website")
pd_df = my_dataframe.to_pandas()

if color:
    file_url = pd_df.loc[pd_df['color_or_style'] == color, 'FILE_URL'].iloc[0]
    st.write('The file url for ', color,' is ', file_url, '.')

    url_response = requests.get(file_url)  
    st.text(url_response.json())
    sf_df = st.dataframe(data=url_response.json(), use_container_width=True)
    st.write("""Our warm, comfortable, {color} sweatsuit!""")



#st.dataframe(data=my_dataframe, use_container_width=True)
#st.stop()

