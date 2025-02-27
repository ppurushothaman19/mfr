import streamlit as st
from streamlit_option_menu import option_menu

import pyautogui as pt
import webbrowser
import time

with st.sidebar:
    st.title("Future Capabilities Chennai")
    app_mode = option_menu(None, ["Home","Excel Data Download From MFR","Add Others"],
                        icons=['home','kanban','sliders'],
                        menu_icon="app-indicator", default_index=0,
                        styles={
        "container": {"padding": "5!important", "background-color": "#f0f2f6"},
        "icon": {"color": "orange", "font-size": "28px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#2C3845"},
    }
    )


#st.balloons()

if app_mode == "Home":
    st.subheader("Welcome To Future Capabilities Chennai Website")

if app_mode == "Excel Data Download From MFR":

    st.subheader('Data Download from MFR')
    st.image('st_mfr.png')
    st.checkbox("Please select the following option","P&L Glance")
    if st.button('Click To Dow'):
        url = "https://app.powerbi.com/groups/me/apps/62a2c8f6-a529-4b77-87b6-1676d50e4d56/reports/21d21bbd-bde2-4e5c-8d3e-5f570a6040e6?experience=power-bi"
        webbrowser.open(url)

        test = "no"
        while test == "no":    

            try:
                x, y = pt.locateCenterOnScreen("m_mfr.png", confidence=0.8)
            except:
                x = "no_img"

            if x != "no_img":    
                test = "yes"


        test = "no"
        while test == "no":    
            try:
                x, y = pt.locateCenterOnScreen("m_p&l.png", confidence=0.8)
            except:
                x = "no_img"

            if x != "no_img":    
                pt.moveTo(x,y,1)
                pt.leftClick()
                test = "yes"

        test = "no"
        while test == "no":    
            try:
                x, y = pt.locateCenterOnScreen("m_p&l_glance.png", confidence=0.8)
            except:
                x = "no_img"

            if x != "no_img":    
                pt.moveTo(x,y,1)
                pt.leftClick()
                test = "yes"

        time.sleep(1)
        pt.moveTo(1507, 838,1)
        pt.leftClick()

        test = "no"
        while test == "no":    
            try:
                x, y = pt.locateCenterOnScreen("m_option1.png", confidence=0.8)
            except:
                x = "no_img"

            if x != "no_img":    
                pt.moveTo(x+40,y,1)
                pt.leftClick()
                test = "yes"


        test = "no"
        while test == "no":    
            try:
                x, y = pt.locateCenterOnScreen("m_export.png", confidence=0.8)
            except:
                x = "no_img"

            if x != "no_img":    
                pt.moveTo(x+40,y,1)
                pt.leftClick()
                test = "yes"

        test = "no"
        while test == "no":    
            try:
                x, y = pt.locateCenterOnScreen("m_export2.png", confidence=0.8)
            except:
                x = "no_img"

            if x != "no_img":    
                pt.moveTo(x+40,y,1)
                pt.leftClick()
                test = "yes"
        st.success("Completed Successfully")

if option_menu == "Add Others":
    st.write("Under Development")