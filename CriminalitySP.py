#https://www.youtube.com/watch?v=KlillpfYK6g
import streamlit as st
import  pandas   as pd
import  pydeck   as pdk
st.set_page_config(page_title='SP', page_icon='🔫', layout='wide', initial_sidebar_state='expanded')
# DATA:
@st.cache_data
def load_data():
    df      = pd.read_csv('datasets/CriminalidadeSP2.csv')
    return    df
df          = load_data()
df['time']  = pd.to_datetime(df['time'])
ocorrencias = df['time'].dt.year.value_counts().sort_index()
# SIDE:
st.sidebar.title    ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider  (                     )
st.sidebar.title    ('DashBoard'          )
st.sidebar.bar_chart(ocorrencias, height=200, color='#00BFFF')
st.sidebar.write    ('Map Options:'       )
D3          = st.sidebar.empty()
D2          = st.sidebar.empty()
ano         = st.sidebar.slider('Year:',     2010, 2018, 2014)
FilteredDF  = df[(df.time.dt.year == ano)]
st.sidebar.info( ' {} Registries'.format(FilteredDF.shape[0]))
table       = st.sidebar.empty()
st.sidebar.divider (           )
st.sidebar.markdown( '''Source: [GeoSpatial Sao Paulo Crime DataBase](https://www.kaggle.com/datasets/danlessa/geospatial-sao-paulo-crime-database/data)''')
st.sidebar.divider (           )
st.sidebar.markdown('''
![2023.10.13](  https://img.shields.io/badge/2023.10.13-000000)

[![GitHub      ](https://img.shields.io/badge/GitHub-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium      ](https://img.shields.io/badge/Medium-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn    ](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python      ](https://img.shields.io/badge/Python3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

[![License     ](https://img.shields.io/badge/Apache--2.0-D22128?&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71)](https://www.apache.org/licenses/LICENSE-2.0)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&logoColor=0065FF&label=&copy;2023&labelColor=0065FF)](https://datavision.one/)
                    ''')
# MAIN:
st.divider(                               )
st.title(    '   Criminality in Sao Paulo')
st.divider(                               )
st.markdown('''
**Criminality** is a recurring problem in major Brazilian cities, even though there is a constant effort to solve this matter.
Data Science technics may help to better understand the situation at hand, generating insights to direct public policy to fight crime.
            ''')
st.divider(                               )
if   D3.checkbox( '3D', value=True):
     st.subheader('3D MAP')
     st.pydeck_chart(pdk.Deck(initial_view_state=pdk.ViewState(longitude=-46.65,
                                                               latitude =-23.55,
                                                               zoom     =  8   ,
                                                               min_zoom = None ,
                                                               max_zoom = None ,
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
     st.divider(          )
if   D2.checkbox( '2D'):
     st.subheader('2D MAP')
     st.map(FilteredDF)
     st.divider(      )
if   table.checkbox('DataFrame', value=True):
     st.subheader(       'DATA'            )
     st.markdown(f'''➡️  Showing {'**{}** ocurrences'.format(FilteredDF.shape[0])} in **{ano}**:''')
     st.write(FilteredDF)
     st.divider(        )
st.toast('Crime!', icon='🔫')
