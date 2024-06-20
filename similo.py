import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import json
from streamlit_lottie import st_lottie

#Layout
st.set_page_config(
    page_title="SimiLo",
    layout="wide",
    initial_sidebar_state="expanded")

#Data Pull and Functions
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

@st.cache_data
def pull_clean():
    master_zip=pd.read_csv('MASTER_ZIP.csv',dtype={'ZCTA5': str})
    master_city=pd.read_csv('MASTER_CITY.csv',dtype={'ZCTA5': str})
    return master_zip, master_city



#Options Menu
with st.sidebar:
    selected = option_menu('SimiLo', ["Intro", 'Search','About'], 
        icons=['play-btn','search','info-circle'],menu_icon='intersect', default_index=0)
    lottie = load_lottiefile("similo3.json")
    st_lottie(lottie,key='loc')

#Intro Page
if selected=="Intro":
    #Header
    st.title('Welcome to SimiLo')
    st.subheader('*A new tool to find similar locations across the United States.*')

    st.divider()

    #Use Cases
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.header('Use Cases')
            st.markdown(
                """
                - _Remote work got you thinking about relocation?_
                - _Looking for a new vacation spot?_
                - _Conducting market research for product expansion?_
                - _Just here to play and learn?_
                """
                )
        with col2:
            lottie2 = load_lottiefile("place2.json")
            st_lottie(lottie2,key='place',height=300,width=300)

    st.divider()

    #Tutorial Video
    st.header('Tutorial Video')
    video_file = open('Similo_Tutorial3_compressed.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
#Search Page
if selected=="Search":

    st.subheader('Select Location')

    master_zip,master_city=pull_clean()
    master_zip.columns = master_zip.columns.str.upper()
    master_zip = master_zip.rename(columns={'ZCTA5': 'ZIP'})
    master_zip['ZIP'] = master_zip['ZIP'].astype(str).str.zfill(5)
    master_city.columns = master_city.columns.str.upper()

    loc_select=st.radio('Type',['Zip','City'],horizontal=True, label_visibility="collapsed")

    if loc_select=='City':
        city_select=st.selectbox(label='city',options=['City']+list(master_city['CITYSTATE'].unique()),label_visibility='collapsed')
        st.caption('Note: City is aggregated to the USPS designation which may include additional nearby cities/towns/municipalities')
        zip_select='Zip'
    if loc_select=='Zip':
        zip_select = st.selectbox(label='zip',options=['Zip']+list(master_zip['ZIP'].unique()),label_visibility='collapsed')

    with st.expander('Advanced Settings'):

        st.subheader('Filter Results')
        col1,col2=st.columns(2)
        states=sorted(list(master_zip['STATE_LONG'].astype(str).unique()))
        state_select=col1.multiselect('Filter Results by State(s)',states)
        count_select=col2.number_input(label='How many similar locations returned? (5-25)',min_value=5,max_value=25,value=10,step=5)
        st.subheader('Data Category Importance')
        st.caption('Lower values = lower importance, higher values = higher importnace, default = 1.0')
        people_select=st.slider(label='People',min_value=0.1, max_value=2.0, step=0.1, value=1.0)
        home_select=st.slider(label='Home',min_value=0.1, max_value=2.0, step=0.1, value=1.0)
        work_select=st.slider(label='Work',min_value=0.1, max_value=2.0, step=0.1, value=1.0)
        environment_select=st.slider(label='Environment',min_value=0.1, max_value=2.0, step=0.1, value=1.0)

    filt_master_zip=master_zip
    filt_master_city=master_city
    if len(state_select)>0:
        filt_master_zip=master_zip[master_zip['STATE_LONG'].isin(state_select)]
        filt_master_city=master_city[master_city['STATE_LONG'].isin(state_select)]

    #Benchmark
    if loc_select=='City':
        if city_select !='City':
            selected_record = master_city[master_city['CITYSTATE']==city_select].reset_index()
            selected_city=selected_record['CITYSTATE'][0]
            #selected_county=selected_record['County Title'][0]
            #Columns for scaling
            PeopleCols_sc=['MED_AGE_SC','PCT_UNDER_18_SC','MED_HH_INC_SC', 'PCT_POVERTY_SC','PCT_BACH_MORE_SC']
            HomeCols_sc=['HH_SIZE_SC','PCT_OWN_SC','MED_HOME_SC','PCT_UNIT1_SC','PCT_UNIT24_SC']
            WorkCols_sc=['MEAN_COMMUTE_SC','PCT_WC_SC','PCT_WORKING_SC','PCT_SERVICE_SC','PCT_BC_SC']
            EnvironmentCols_sc=['PCT_WATER_SC','ENV_INDEX_SC','PCT_TOPARK_ONEMILE_SC','POP_DENSITY_SC','METRO_INDEX_SC']
            
            st.header('Top '+'{}'.format(count_select)+' Most Similar Locations')
            #st.write('You selected zip code '+zip_select+' from '+selected_record['County Title'][0])
            # CSS to inject contained in a string
            hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

            # Inject CSS with Markdown
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            tab1,tab2=st.tabs(['Map','Data'])
            with tab2:
                with st.expander('Expand for Table Info'):
                    st.markdown(
                    """
                    - The values for OVERALL, PEOPLE, HOME, WORK, and ENVIRONMENT are scaled similarity scores for the respective categories with values of 0-100, where 100 represents a perfect match.
                    - Locations are ranked by their OVERALL score, which is a weighted average of the individual category scores.
                    - Save your research by checking locations in the SAVE column which will be added to csv for download.
                    """
                    )
                @st.cache_data
                def convert_df(df):
                    return df.to_csv().encode('utf-8')

            st.divider()

            st.header('Location Deep Dive')
                   
    if zip_select != 'Zip':
        selected_record = master_zip[master_zip['ZIP']==zip_select].reset_index()
        selected_zip=selected_record['ZIP'][0]
        selected_county=selected_record['COUNTY_NAME'][0]
        selected_state=selected_record['STATE_SHORT'][0]

        #Columns for scaling
        PeopleCols_sc=['MED_AGE_SC','PCT_UNDER_18_SC','MED_HH_INC_SC', 'PCT_POVERTY_SC','PCT_BACH_MORE_SC']
        HomeCols_sc=['HH_SIZE_SC','PCT_OWN_SC','MED_HOME_SC','PCT_UNIT1_SC','PCT_UNIT24_SC']
        WorkCols_sc=['MEAN_COMMUTE_SC','PCT_WC_SC','PCT_WORKING_SC','PCT_SERVICE_SC','PCT_BC_SC']
        EnvironmentCols_sc=['PCT_WATER_SC','ENV_INDEX_SC','PCT_TOPARK_ONEMILE_SC','POP_DENSITY_SC','METRO_INDEX_SC']


        #df_similarity['OVERALL_SIM']=df_similarity['PEOPLE_SIM','HOME_SIM','WORK_SIM','ENV_SIM'].mean(axis=1)
        weights=[people_select,home_select,work_select,environment_select]
        # Multiply column values with weights
        

        st.header('Top '+'{}'.format(count_select)+' Most Similar Locations')
        #st.write('You selected zip code '+zip_select+' from '+selected_record['County Title'][0])
        # CSS to inject contained in a string
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        tab1,tab2=st.tabs(['Map','Data'])
        with tab2:
            with st.expander('Expand for Table Info'):
                st.markdown(
                """
                - The values for OVERALL, PEOPLE, HOME, WORK, and ENVIRONMENT are scaled similarity scores for the respective categories with values of 0-100, where 100 represents a perfect match.
                - Locations are ranked by their OVERALL score, which is a weighted average of the individual category scores.
                - Save your research by checking locations in the SAVE column which will be added to csv for download.
                """
                )
            @st.cache_data
            def convert_df(df):
                return df.to_csv().encode('utf-8')

        st.divider()

        st.header('Location Deep Dive')
        rank_select=st.selectbox('Select from rankings above',list(df_top10['RANKING']))
        
#About Page
if selected=='About':
    st.title('Data')
    #st.subheader('All data for this project was publicly sourced from:')
    col1,col2,col3=st.columns(3)
    col1.subheader('Source')
    col2.subheader('Description')
    col3.subheader('Link')
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('census_graphic.png',width=150)
        col1.write(':blue[U.S. Census Bureau]')
        col2.write('Demographic, housing, industry at zip level')
        #col2.write('American Community Survey, 5-Year Profiles, 2021, datasets DP02 - DP05')
        col3.write('https://data.census.gov/')
    
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('cdc.png',width=150)
        col1.write(':blue[Centers for Disease Control and Prevention]')
        col2.write('Environmental factors at county level')
        col3.write('https://data.cdc.gov/')
    
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('hud.png',width=150)\
        col1.write(':blue[U.S. Dept Housing and Urban Development]')
        col2.write('Mapping zip to county')
        col3.write('https://www.huduser.gov/portal/datasets/')

    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('ods.png',width=150)
        col1.write(':blue[OpenDataSoft]')
        col2.write('Mapping zip to USPS city')
        col3.write('https://data.opendatasoft.com/pages/home/')
    
    st.divider()
    
    st.title('Creator')
    with st.container():
        col1,col2=st.columns(2)
        col1.write('')
        col1.write('')
        col1.write('')
        col1.write('**Name:**    Kevin Soderholm')
        col1.write('**Education:**    M.S. Applied Statistics')
        col1.write('**Experience:**    8 YOE in Data Science across Banking, Fintech, and Retail')
        col1.write('**Contact:**    kevin.soderholm@gmail.com or [linkedin](https://www.linkedin.com/in/kevin-soderholm-67788829/)')
        col1.write('**Thanks for stopping by!**')
        col2.image('kevin8.png')

