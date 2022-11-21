import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header(f"Prashun, Master's in Data science and Mathematics")

st.info('python enthusiast, working on web-framework, trying to build something new in UI modes with an interest in Data Science')

icon_size = 20

st_button('medium', 'https://medium.com/@prasun.ssvm', 'Read my Blogs', icon_size)
st_button('Github', 'https://github.com/prashun-creator', 'Follow me on Github', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/prashun-chauhan-687a04a4/', 'Follow me on LinkedIn', icon_size)
st_button('tableau', 'https://public.tableau.com/app/profile/prashun5508/viz/DiscountmartsalesAnalyticsUSdata/Dashboard1', 'tableau Data visualization', icon_size)
