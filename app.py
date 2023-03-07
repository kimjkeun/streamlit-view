import streamlit as st
view = [100, 150, 40, 50, 100]
view
st.write("Youtube view")
st.write("# Youtube view")
st.bar_chart(view)

import pandas as pd

sview = pd.Series(view)
sview