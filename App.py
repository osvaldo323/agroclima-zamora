app.py

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("Plataforma Agroclimática Zamora - FAO 56")

st.subheader("Simulación horaria")

# Datos simulados
horas = np.arange(0, 24)

temp = np.random.uniform(15, 30, 24)
hr = np.random.uniform(40, 90, 24)
viento = np.random.uniform(0.5, 3, 24)

# Cálculo presión vapor saturación
es = 0.6108 * np.exp((17.27 * temp) / (temp + 237.3))
ea = es * (hr / 100)
vpd = es - ea

df = pd.DataFrame({
    "Hora": horas,
    "Temp (°C)": temp,
    "HR (%)": hr,
    "VPD (kPa)": vpd,
    "Viento (m/s)": viento
})

st.line_chart(df.set_index("Hora"))

st.write("Datos numéricos")
st.dataframe(df)
