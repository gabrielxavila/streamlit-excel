from numpy import number
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit.elements import image, slider 

st.set_page_config(page_title='Survery Stuff')
st.header('Survey Results and stuff 2022 😎👍🏼')
st.subheader('Was this helpful?')


### --- LOAD DATA FRAME
excel_file = 'Survey_results.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='B:D',
                        header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='F:G',
                                header=3)

df_participants.dropna(inplace=True)

# --- STREAMLIT SELECTION
deparment = df['Department'].unique().tolist()
age = df['Age'].unique().tolist()

# --- STREAMLIT SLIDER
age_slider = st.slider('Age:', 
                        min_value= min(age),
                        max_value= max(age),
                        value= (min(age),max(age)))

# --- STREAMLIT SELECTION
deparment_selection = st.multiselect('Deparment:',
                                deparment,
                                default=deparment)

st.dataframe(df)
# st.dataframe(df_participants)
pie_chart = px.pie(df_participants,
                        title='Total # of Peeps',
                        values='Participants',
                        names= 'Departments',)

# --- STREAMLIT FILTER
mask = (df['Age'].between(*age_slider)) & (df['Department'].isin(deparment_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Rating']).count()[['Age']]
df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Rating',
                   y='Votes',
                   text='Votes',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart, use_container_width=True)


st.plotly_chart(pie_chart,use_container_width=True)

image = Image.open('images/survey.jpg')
st.image(image,
        caption='Designed by Gabe',
        use_column_width=True)







# import pandas as pd
# import streamlit as st
# import plotly.express as px
# from PIL import Image

# st.set_page_config(page_title='Survey Results')
# st.header('Survey Results 2021')
# st.subheader('Was the tutorial helpful?')

# ### --- LOAD DATAFRAME
# excel_file = 'Survey_Results.xlsx'
# sheet_name = 'DATA'

# df = pd.read_excel(excel_file,
#                    sheet_name=sheet_name,
#                    usecols='B:D',
#                    header=3)

# df_participants = pd.read_excel(excel_file,
#                                 sheet_name= sheet_name,
#                                 usecols='F:G',
#                                 header=3)
# df_participants.dropna(inplace=True)

# # --- STREAMLIT SELECTION
# department = df['Department'].unique().tolist()
# age = df['Age'].unique().tolist()

# age_selection = st.slider('Age:',
#                         min_value= min(age),
#                         max_value= max(age),
#                         value=(min(age),max(age)))

# department_selection = st.multiselect('Department:',
#                                     department,
#                                     default=department)

# # --- FILTER DATAFRAME BASED ON SELECTION
# mask = (df['Age'].between(*age_selection)) & (df['Department'].isin(department_selection))
# number_of_result = df[mask].shape[0]
# st.markdown(f'*Available Results: {number_of_result}*')

# # --- GROUP DATAFRAME AFTER SELECTION
# df_grouped = df[mask].groupby(by=['Rating']).count()[['Age']]
# df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
# df_grouped = df_grouped.reset_index()

# # --- PLOT BAR CHART
# bar_chart = px.bar(df_grouped,
#                    x='Rating',
#                    y='Votes',
#                    text='Votes',
#                    color_discrete_sequence = ['#F63366']*len(df_grouped),
#                    template= 'plotly_white')
# st.plotly_chart(bar_chart)

# # --- DISPLAY IMAGE & DATAFRAME
# col1, col2 = st.beta_columns(2)
# image = Image.open('images/survey.jpg')
# print(image)
# col1.image(image,
#         caption='Designed by slidesgo / Freepik',
#         use_column_width=True)
# col2.dataframe(df[mask])

# # --- PLOT PIE CHART
# pie_chart = px.pie(df_participants,
#                 title='Total No. of Participants',
#                 values='Participants',
#                 names='Departments')

# st.plotly_chart(pie_chart)
