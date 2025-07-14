
import streamlit as st
from PIL import Image

# Logo e título
col1, col2 = st.columns([1, 6])
with col1:
    st.image("logo.png", width=80)
with col2:
    st.markdown("# Simulador Tributário")
    st.markdown("### Cálculo da CBS – Contribuição sobre Bens e Serviços")

st.markdown("---")

# Entradas
regime = st.selectbox("Regime Tributário", ["Lucro Real", "Lucro Presumido", "Simples Nacional"])
aliquota = st.number_input("Alíquota CBS (%)", min_value=0.0, max_value=100.0, value=9.0, step=0.01)
receita = st.number_input("Receita Tributável (R$)", min_value=0.0, value=0.0, step=100.0)
despesas = st.number_input("Despesas com Crédito (R$)", min_value=0.0, value=0.0, step=100.0)

# Cálculo
base_calculo = receita - despesas
cbs = (aliquota / 100) * base_calculo if base_calculo > 0 else 0

# Resultado
st.markdown("## Resultado da Simulação")
st.write(f"Base de Cálculo: R$ {base_calculo:,.2f}")
st.write(f"Valor da CBS a pagar: R$ {cbs:,.2f}")
