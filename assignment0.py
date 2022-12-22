import streamlit as st
import pandas as pd
import altair as alt
# from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

#Steam = pd.read_csv('Steam.csv')
#st.set_page_config(
#  page_title="pages",
#)

page = st.sidebar.selectbox("Choose a page", ["Introduction", "Scatter and Line", "Pie and area chart and bar"])
if page == "Introduction":
  Steam = pd.read_csv('Steam.csv')
  # title
  st.title('Steam Games Application')
  st.sidebar.success("Select a page above.")
  st.markdown('Introduction')
  st.text('The dataset includes information on the games')
  st.text('Metacritic score')
  st.text('price')
  st.text('number of recommendations')
  st.text('Using this data you can analyze which games are the most popular on Steam')
  st.text('and compare their prices and Metacritic scores')
  st.text('You can also use the data to find games that are recommended by other Steam users')
  st.text('Recently some players used to get bored or confused which game to play or invest their time or money in')
  st.text('so using the following informations will make the choices easier')
  st.markdown('Findings')
  st.write('The games counter strike and half time are the most played of all time and have the highest recommendations numbers.')
  def convert_df(df):
    return df.to_csv().encode('utf-8')
  csv = convert_df(Steam)
  st.download_button(
    label="Download dataset as CSV",
    data=csv,
    file_name='steamgames_dataset.csv',
    mime='text/csv',)

if page == "Scatter and Line":
  Steam = pd.read_csv('Steam.csv')
  games_name = st.selectbox("Select your game",Steam['ResponseName'].unique())
  st.write(games_name)
  plot_type=st.checkbox("plot type scatter")
  plot_type1=st.checkbox("plot type line")
  if plot_type:
    pl = alt.Chart(Steam[Steam['ResponseName']==games_name]).mark_circle().encode(
      x = 'ResponseName',
      y ='PriceInitial',
      color = 'ResponseName',
      tooltip = ['ResponseName','PriceInitial']
  ).interactive()
    st.altair_chart(pl)
  if plot_type1:
    pl = alt.Chart(Steam.head(10)).mark_line().encode(
      x = 'ResponseName',
      y ='PriceInitial',
      color = 'ResponseName',
      tooltip = ['ResponseName','PriceInitial']
  ).interactive()
    st.altair_chart(pl)

if page == "Pie and area chart and bar":
  Steam = pd.read_csv('Steam.csv')

  # 2. horizontal menu
  # selected2 = option_menu(None, ["area_chart/pie", "Bar"], 
    # menu_icon="cast", default_index=0, orientation="horizontal")

  option = ['Bar Chart','Area chart & Pie Chart']
  selected_option = st.multiselect("Select any chart to see", option)

  for o in selected_option:
    if o == "Area chart & Pie Chart":
      plot_type=st.radio("select the plot type",['area_chart','pie'])
      if plot_type == 'area_chart':
        st.area_chart(data=Steam.head(10), x='PriceInitial', y='ResponseName')
      if plot_type == 'pie':
        st.subheader('Pie chart')
        f1, ax1 = plt.subplots()
        ax1.pie(Steam['PriceInitial'].head(10), labels=Steam['ResponseName'].head(10), autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(f1)    
    if o == 'Bar Chart':
      pl = alt.Chart(Steam.head(10)).mark_bar().encode(
      x = 'Metacritic',
      y = 'PriceInitial',
      color = 'ResponseName',
      tooltip = ['Metacritic','PriceInitial']
      ).interactive()
      st.altair_chart(pl)
