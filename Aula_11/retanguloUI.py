import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculos com Retângulo")
        b = st.text_input("Base")
        h = st.text_input("Altura")
        if st.button("Calcular"):
            x = Retangulo(float(b), float(h))
            st.write(x)
            st.write(f"Área = {x.calc_area()}")
            st.write(f"Diagonal = {x.calc_diagonal()}")