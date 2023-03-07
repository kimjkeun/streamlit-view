import streamlit as st
import pandas as pd
view = [100, 150, 40, 50]
view
st.write("Youtube view")
st.write("# Youtube view")
st.write("# Youtube view")
st.write("# Youtube view")
st.bar_chart(view)

import pandas as pd

sview = pd.Series(view)
sview

table = pd.read_excel('dashboard.xlsx')
table