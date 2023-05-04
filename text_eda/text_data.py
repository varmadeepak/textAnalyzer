# this script contains code for
# unstructured, text data analysis

import json
import text_eda.plots as plots 
import streamlit as st
import pandas as pd
import text_eda.preprocessor as pp
import streamlit.components.v1 as components
from PIL import Image
from helper_functions import *

def select_text_feature(df) -> pd.DataFrame :
    """
    this function selects the text feature from the uploaded csv file
    ----------
    df: A pandas Dataframe 
    """
    text_col = st.selectbox('Select the text column',(list(df.columns)))
    
    df = df[text_col]
    df =  pd.DataFrame(df)
        
    return df,text_col

def text_data_app():
    
    
    
    # Side panel setup
    # Step 1 includes Uploading and Preprocessing data (optional)
    display_app_header(main_txt = "Step 1",
                       sub_txt= "Upload data",
                       is_sidebar=True)
    
    data_input_mthd = st.sidebar.radio("Select Data Input Method",
                                       ('Copy-Paste text', 
                                       ))
    
    st.subheader('Choose data to analyse :alembic:')
    data,txt  = check_input_method(data_input_mthd)
    
    data,text_column = select_text_feature(data)
    
    display_app_header_1(sub_txt= "Preprocess data",
                       is_sidebar=True)
    
    clean_data_opt = st.sidebar.radio("Choose wisely",
                                      ('Skip preprocessing', 
                                       'Run preprocessing'))
    
    # clean data #######
    if clean_data_opt=='Skip preprocessing':
            st.subheader('Using Raw data :cut_of_meat:')  #Raw data header
            
            display_app_header(main_txt = "Step 2",
                   sub_txt= "Analyse data",
                   is_sidebar=True)
            
            selected_plot = st.sidebar.radio(
            "Choose ", ('Length of text', 
                            'Word count',
                            'Average word length',
                            'Unique word count',
                            # 'N-grams',
                            # 'Topic modelling',
                            'Wordcloud'
                           )
                            # 'NER',
                            # 'POS',
                            # 'Complexity Scores')
            )
            
    else:
            st.subheader('Using Clean Data :droplet:')  #Clean data header

            data = pp.clean_data(data,feature=text_column)
            st.success('Data cleaning successfuly done!')
            
            # image = Image.open("text_eda/pp.png")
            # st.image(image, caption='Preprocessing steps')
    
            display_app_header(main_txt = "Step 2",
                            sub_txt= "Analyse data",
                            is_sidebar=True)
                
            selected_plot = st.sidebar.radio(
            "Choose", ('Length of text', 
                            'Word count',
                            'Average word length',
                            'Unique word count',
                            # 'N-grams',
                            # 'Topic modelling',
                            'Wordcloud'
                            )
                            # 'NER',
                            # 'POS',
                            # 'Complexity Scores')
            )
            # final step
            st.download_button(
                label="Download clean data",
                data=data.to_csv().encode('utf-8'),
                file_name='clean_data.csv',
                mime='text/csv',
            )
                    
    st.subheader('A preview of input data is below, please select plot to start analysis :bar_chart:')
    st.write(data.head(5))
    
    plots.plot(selected_plot,
               data,
               text_column)