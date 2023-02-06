import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout='wide')
final_df  = pd.read_csv("India_census.csv")

list_of_states = list(final_df['State'].unique())
list_of_states.insert(0,"Overall india")
primary_list = sorted(['Population','literacy_rate','sex_ratio','Housholds_with_Electric_Lighting','Households_with_Internet'])


st.sidebar.title("INDIA'S DATA VIZ")
selected_state = st.sidebar.selectbox("select a state",list_of_states)
primary = st.sidebar.selectbox("select primary parameter",primary_list)
secondary = st.sidebar.selectbox("select secondary parameter",primary_list)

plot  = st.sidebar.button("Plot Graph")


if plot:
    if selected_state=='Overall india':
        #plot for india
        fig = px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude",size=primary,
                                color=secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire,
                                size_max=35, zoom=3,
                                mapbox_style="carto-positron",width=1200,height=700)
        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot for state
        state_df = final_df[final_df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",size=primary,
                                color=secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire,
                                size_max=25, zoom=3,
                                mapbox_style="carto-positron",width=1200,height=700)
        st.plotly_chart(fig,use_container_width=True)