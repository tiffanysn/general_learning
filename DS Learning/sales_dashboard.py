
import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv('~/Projects/general_learning/Quantium/QVI_data.csv')
df.info()

st.write("""
# Sales Analysis

This app showing the sales changes over period
""")

df['year_month'] = pd.to_datetime(df['DATE']).dt.floor('d') - pd.offsets.MonthBegin(1)
df = df.groupby(["year_month", "LIFESTAGE"])["TOT_SALES"].sum().reset_index()

df = pd.pivot_table(df, values="TOT_SALES", index="LIFESTAGE", columns="year_month")

st.sidebar.header('Input Features')
st.sidebar.subheader('Choose PREMIUM_CUSTOMER')


stores = st.multiselect(
    "Choose Lifestages", list(df.index), ["YOUNG FAMILIES", "OLDER FAMILIES"]
)

data = df.loc[stores]
st.write("### Show Chosen Stores", data.sort_index())

data = data.T.reset_index()
data = pd.melt(data, id_vars=["year_month"])

chart = (
    alt.Chart(data)
    .mark_area(opacity=0.3)
    .encode(
        x="year_month:T",
        y=alt.Y("value:Q", stack=None),
        color="LIFESTAGE:N",
    )
)
st.altair_chart(chart, use_container_width=True)


