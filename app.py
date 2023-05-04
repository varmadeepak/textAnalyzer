
import streamlit as st
from PIL import Image
from helper_functions import *
from text_eda.text_data import *

from text_eda.text_data import  text_data_app;

# app setup 
try:

    # create ss object
    if 'data' not in st.session_state:
        st.session_state.data = None

    # app design
    # app_meta('📚')
    # set_bg_hack('dqw_background.png')

    # set logo in sidebar using PIL
    logo = Image.open('logo.png')
    st.sidebar.image(logo, 
                        use_column_width=True)
    
    # hide warning for st.pyplot() deprecation
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    # Main panel setup
    display_app_header(main_txt='Text Analyszer',
                       sub_txt='')

    st.markdown("""---""")
    # provide options to user to navigate to other dqw apps
    
    text_data_app()

except KeyError:
    st.error("Please select a key value from the dropdown to continue.")
    
except ValueError:
    st.error("Oops, something went wrong. Please check previous steps for inconsistent input.")
    
except TypeError:
    st.error("Oops, something went wrong. Please check previous steps for inconsistent input.")
