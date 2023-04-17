import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df=pd.read_csv('india.csv')

states=list(df['State'].unique())
states.insert(0,'overall India')

st.sidebar.title("India's data visualization" )

selected_state=st.sidebar.selectbox('Select a state',states)

primary=st.sidebar.selectbox('select primary parameter',sorted(df.columns[5:]))

secondary=st.sidebar.selectbox('select secondary parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('plot graph')

if plot:
    st.text('size represents primary parameter')
    st.text('color reppresent secondary parameter')
    if selected_state == 'overall India':
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,color=secondary,size_max=35,
                              zoom=3,mapbox_style='carto-positron',width=1200,height=700,
                              hover_name='District',color_continuous_scale=px.colors.cyclical.IceFire)
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=df[df['State']==selected_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, size_max=35,
                                zoom=6, mapbox_style='carto-positron', width=1200, height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
