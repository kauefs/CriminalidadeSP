#https://www.youtube.com/watch?v=KlillpfYK6g
import  pandas   as pd
import  pydeck   as pdk
import streamlit as st
st.set_page_config(page_title='SP', page_icon='🔫')
@st.cache_data
def load_data():
    df      = pd.read_csv('datasets/CriminalidadeSP2.csv')
    return df
df          = load_data()
st.title(    '   Criminality in Sao Paulo')
st.markdown('''**Criminality** is a recurring problem in major Brazilian cities,
                 even though there is a constant effort to solve this matter.
                 Data Science technics may help to better understand the situation at hand,
                 generating insights to direct public policy to fight crime.''')
df.time     =  pd.to_datetime(df.time)
st.sidebar.title('DashBoard')
ocorrencias = df.time.dt.year.value_counts().sort_index()
st.sidebar.bar_chart(ocorrencias, height=200, color='#00BFFF')
ano         =  st.sidebar.slider('Choose Year:', 2010, 2018, 2014)
FilteredDF  =  df[(df.time.dt.year == ano)]
st.sidebar.info( ' {} Registros'.format(FilteredDF.shape[0]))
if   st.sidebar.checkbox('Data Table', value=True):
     st.subheader(       'Data:')
     st.markdown( '''     Source: [GeoSpatial Sao Paulo Crime DataBase](https://www.kaggle.com/datasets/danlessa/geospatial-sao-paulo-crime-database/data)''')
     st.markdown(f'''➡️ Showing {'**{}** ocurrences'.format(FilteredDF.shape[0])} em **{ano}**:''')
     st.write(FilteredDF)
st.sidebar.write('Map Options:')
if   st.sidebar.checkbox('3D', value=True):
     st.subheader('       3D Map:')
     st.pydeck_chart(pdk.Deck(initial_view_state=pdk.ViewState(longitude=-46.65,
                                                               latitude =-23.55,
                                                               zoom     =  8   ,
                                                               min_zoom =  None,
                                                               max_zoom =  None,
                                                               pitch    = 50   ,
                                                               bearing  = 50)  ,
                                          layers=[pdk.Layer('HexagonLayer'     ,
                                            data           = FilteredDF,
                                            get_position   = '[longitude,latitude]',
                                            auto_highlight = True,
                                            elevation_scale= 50,
                                            elevation_range=[ 0,2750],
                                            pickable=True,
                                            extruded=True,
                                            coverage=1)],
                                          views=[{'@@type':'MapView', 'controller':True}],
                                          map_style   ='dark',
                                          api_keys    = None ,
                                          width       ='100%',
                                          height      = 500  ,
                                          tooltip     = True ,
                                          description ='Sao Paulo Criminality',
                                          effects     = None ,
                                          map_provider='carto',
                                          parameters  = None))
if   st.sidebar.checkbox('2D'):
     st.subheader('       2D Map:')
     st.map(FilteredDF)
st.sidebar.divider()
with st.sidebar.container():
     C1,  C2,  C3 = st.columns(3)
     with C1:st.empty()
     with C2:st.markdown('''©2023™''')
     with C3:st.empty()
st.toast('Crime!', icon='🔫')
