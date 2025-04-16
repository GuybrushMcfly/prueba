import streamlit as st
import plotly.graph_objects as go

st.title("📊 Visualización de Trámites")

# Selector de gráfico
opcion = st.selectbox("Elegí el estilo de gráfico:", [
    "Gráfico 1: Esquema simple",
    "Gráfico 2: Barra moderna horizontal",
    "Gráfico 3: Estilo Stepper UI"
])

# -------------------
# GRÁFICO 1: Esquema simple
# -------------------
if opcion == "Gráfico 1: Esquema simple":
    tramites = ['Trámite 1', 'Trámite 2', 'Trámite 3']
    estados = ['Estado 1', 'Estado 2', 'Estado 3']
    estado_actual = [1, 2, 3]

    fig1 = go.Figure()
    for i, tramite in enumerate(tramites):
        y = len(tramites) - i
        for j, estado in enumerate(estados):
            color = 'green' if j + 1 <= estado_actual[i] else 'lightgray'
            fig1.add_trace(go.Scatter(
                x=[j], y=[y],
                mode='markers+text',
                marker=dict(size=20, color=color),
                text=[estado],
                textposition="top center",
                showlegend=False
            ))
            if j
