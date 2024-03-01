import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Simulasikan DataFrame day_df
day_df = pd.DataFrame({
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'bike_count': [100, 120, 90, 150, 80]
})

# Urutkan DataFrame berdasarkan rata-rata penggunaan sepeda
sorted_day_df = day_df.sort_values(by='bike_count', ascending=False)

# Tambahkan gambar header
header_image = "bike_dash.jpg"  # Ganti dengan URL gambar Anda
st.image(header_image, use_column_width=True)

import streamlit as st

# Tampilkan judul di tengah dengan gaya kreatif
st.markdown(
    """
    <div style='text-align:center'>
        <h1 style='color: #2f5d62; font-size: 2.5em;'>🚴‍♂️ Bike Dashboard 🚴‍♀️</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Bar Chart
st.subheader('Average Bike Usage by Day')
st.bar_chart(sorted_day_df.set_index('day'))

# Tambahkan teks inspiratif
st.subheader('Motivational Quote')
st.markdown("> \"Life is like riding a bicycle. To keep your balance, you must keep moving.\" - Albert Einstein")

# Visualisasi boxplot
st.subheader('Distribution of Bike Usage by Day')
box_plot = px.box(day_df, x='bike_count', orientation='h', labels={'bike_count': 'Bike Count'})
st.plotly_chart(box_plot)

# Menampilkan statistik deskriptif
st.subheader('Descriptive Statistics')
st.dataframe(day_df.describe())

# Menambahkan elemen interaktif
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.dataframe(day_df)
