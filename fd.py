import streamlit as st
from PIL import Image

st.set_page_config(page_title = "FD Calculator" , page_icon="📈")

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# img = Image.open("fd.png")

st.header("FD Calculator")

st.subheader("Developed by Mudit")

col1,col2 = st.columns([5,5])

with col1:
    principal = st.number_input("Total Investment", 1000, 1000000000)
    rate = st.number_input("Rate of interest (p.a)", 1.0, 15.0)
    time = st.number_input("Time period", 1, 100)
    compounded = st.number_input("Number of times compunded (p.a)", 1, 12)

amount = int(principal*(1+(rate/100)/compounded)**(compounded*time))

col3,col4,col5 = st.columns([2.5,2.5,5])

if(st.button("Calculate")):
    with col3:
        
        st.write("Invested Amount" + str(principal))
        st.write("Est. returns" + str(amount-principal))
        st.write("Total Value" + str(amount))


        




