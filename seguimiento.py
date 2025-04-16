import streamlit as st
import plotly.graph_objects as go

# Datos de ejemplo
tramites = ['Trámite 1', 'Trámite 2', 'Trámite 3']
estados = ['Estado 1', 'Estado 2', 'Estado 3']
estado_actual = [1, 2, 3]  # Estado en el que está cada trámite (1-indexado)

fig = go.Figure()

for i, tramite in enumerate(tramites):
    y = len(tramites) - i  # Invertir eje y para que Trámite 1 quede arriba
    for j, estado in enumerate(estados):
        color = 'green' if j + 1 <= estado_actual[i] else 'lightgray'
        fig.add_trace(go.Scatter(
            x=[j], y=[y],
            mode='markers+text',
            marker=dict(size=20, color=color),
            text=[estado],
            textposition="top center",
            showlegend=False
        ))
        # Conectar con líneas entre puntos
        if j > 0:
            fig.add_trace(go.Scatter(
                x=[j-1, j], y=[y, y],
                mode='lines',
                line=dict(color='gray', width=2),
                showlegend=False
            ))

fig.update_layout(
    yaxis=dict(tickvals=list(range(1, len(tramites)+1)), ticktext=tramites),
    xaxis=dict(tickvals=list(range(len(estados))), ticktext=estados),
    margin=dict(l=100, r=20, t=20, b=20),
    height=300,
)

st.plotly_chart(fig)
