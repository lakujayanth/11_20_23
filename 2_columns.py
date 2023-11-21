# import streamlit as st
# st.title('SF Trees')
# st.write(
#     """
#     This app analyses trees in San Francisco using
#     a dataset kindly provided by SF DPW.
#     """
# )
# first_width = st.number_input('First Width', min_value=1, value=1)
# second_width = st.number_input('Second Width', min_value=1, value=1)
# third_width = st.number_input('Third Width', min_value=1, value=1)
# col1, col2, col3 = st.columns(
#       (first_width,second_width,third_width))
# with col1:
#      st.write('First column')
# with col2:
#      st.write('Second column')
# with col3:
#      st.write('Third column')
# Joe PR test

import streamlit as st
import pandas as pd
st.title('SF Trees')
st.write(
    """
    This app analyses trees in San Francisco using
    a dataset kindly provided by SF DPW.
    """
)
trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)