import streamlit as st

st.set_page_config(layout="wide", page_title="GTO2", page_icon="🌠")

st.header("Contenidos del día 3")

cols = st.columns(2)

cols[0].subheader("Notebook para perceptrones")

cols[0].markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GabrielMissael/CosmicDistortions/blob/day1/notebooks/CdeCMx2025_GT02_Introduccion_redes_neuronales.ipynb)")

cols[1].subheader("Notebook para lentes gravitacionales")

cols[1].markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GabrielMissael/CosmicDistortions/blob/day1/notebooks/CdeCMx2025_GT02_simulando_lentes_gravitacionales.ipynb)")
