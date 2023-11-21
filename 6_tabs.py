import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
st.title("SF Trees")
st.write(
    """
    This app analyses trees in San Francisco using
    a dataset kindly provided by SF DPW.
    """
)
trees_df = pd.read_csv("trees.csv")
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]
tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
    st.line_chart(df_dbh_grouped)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Column 1")
    with col2:
        st.write("Column 2")
    with col3:
        st.write("Column 3")
with tab2:
    st.bar_chart(df_dbh_grouped)
with tab3:
    st.area_chart(df_dbh_grouped)

# Add in a sidebar

# import pandas as pd
# import streamlit as st
# st.title("SF Trees")
# st.write(
#     """
#     This app analyses trees in San Francisco using
#     a dataset kindly provided by SF DPW.
#     """
# )
# trees_df = pd.read_csv("trees.csv")
# owners = st.sidebar.multiselect(
#     "Tree Owner Filter",
#     trees_df["caretaker"].unique())
# if owners:
#     trees_df = trees_df[
# trees_df["caretaker"].isin(owners)]
# df_dbh_grouped = pd.DataFrame(
# trees_df.groupby(["dbh"]).count()["tree_id"])
# df_dbh_grouped.columns = ["tree_count"]
# st.line_chart(df_dbh_grouped)