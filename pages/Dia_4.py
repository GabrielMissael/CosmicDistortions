import streamlit as st

st.set_page_config(layout="wide", page_title="GTO2", page_icon="🌠")

st.header("Contenidos del día 4")

cols = st.columns(2)

cols[0].subheader("Notebook para redes neuronales convolucionales")

cols[0].markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GabrielMissael/CosmicDistortions/blob/day1/notebooks/Redes_neuronales_convolucionales_CdeC_2025_GTO2.ipynb)")

cols[1].subheader("Notebook para simular lente con tu propia imágen")

cols[1].markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GabrielMissael/CosmicDistortions/blob/day1/notebooks/Simulando_un_lente.ipynb)")
