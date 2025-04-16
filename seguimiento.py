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



import streamlit as st
import plotly.graph_objects as go

# Datos de ejemplo
tramites = ['Trámite A', 'Trámite B']
estados = ['Order Placed', 'Order Confirmed', 'In Production', 'Final Production', 'Shipped']
colores = ['lightgray', 'lightgray', 'lightgray', 'lightgray', 'lightgray']

# Estado actual de cada trámite (índice del estado actual, 0-indexado)
estado_actual = {
    'Trámite A': 1,  # Está en "Order Confirmed"
    'Trámite B': 3   # Está en "Final Production"
}

# Crear figura
fig = go.Figure()

for idx, tramite in enumerate(tramites):
    y = len(tramites) - idx  # verticalmente invertido
    for i, estado in enumerate(estados):
        # Color si el estado está alcanzado
        color = 'deepskyblue' if i <= estado_actual[tramite] else 'lightgray'
        border_color = 'navy' if i == estado_actual[tramite] else 'gray'

        fig.add_trace(go.Scatter(
            x=[i], y=[y],
            mode='markers+text',
            marker=dict(size=30, color=color, line=dict(width=2, color=border_color)),
            text=[estado],
            textposition="bottom center",
            showlegend=False
        ))

        # Línea entre puntos
        if i > 0:
            line_color = 'deepskyblue' if i <= estado_actual[tramite] else 'lightgray'
            fig.add_trace(go.Scatter(
                x=[i-1, i], y=[y, y],
                mode='lines',
                line=dict(color=line_color, width=8),
                showlegend=False
            ))

fig.update_layout(
    xaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False
    ),
    yaxis=dict(
        tickvals=list(range(1, len(tramites)+1)),
        ticktext=tramites,
        showgrid=False
    ),
    height=300,
    margin=dict(l=40, r=40, t=30, b=30)
)

st.plotly_chart(fig)


import streamlit as st
import plotly.graph_objects as go

# Etapas del proceso
etapas = ["Create Account", "Login", "Payment", "Confirm"]
estado_actual = 2  # índice 0-indexado (0=primero, 3=último)

# Posición horizontal de cada etapa
x_vals = list(range(len(etapas)))
y_val = 1

# Crear figura
fig = go.Figure()

# Líneas entre los pasos
for i in range(len(etapas) - 1):
    color = "limegreen" if i < estado_actual else "lightgray"
    fig.add_trace(go.Scatter(
        x=[x_vals[i], x_vals[i+1]], y=[y_val, y_val],
        mode="lines",
        line=dict(color=color, width=10),
        showlegend=False
    ))

# Círculos y textos
for i, label in enumerate(etapas):
    if i < estado_actual:
        color = "limegreen"
        text_color = "green"
    elif i == estado_actual:
        color = "deepskyblue"
        text_color = "blue"
    else:
        color = "lightgray"
        text_color = "gray"

    fig.add_trace(go.Scatter(
        x=[x_vals[i]], y=[y_val],
        mode="markers+text",  # <- Corregido
        marker=dict(size=60, color=color),
        text=[str(i+1)],
        textposition="middle center",
        customdata=[[label]],
        textfont=dict(color="white", size=20),
        showlegend=False
       
    ))

    # Texto debajo
    fig.add_trace(go.Scatter(
        x=[x_vals[i]], y=[y_val - 0.3],
        mode="text",
        text=[label],
        textposition="bottom center",
        textfont=dict(size=14, color=text_color),
        showlegend=False
    ))

# Ajustes de layout
fig.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    height=200,
    margin=dict(l=40, r=40, t=20, b=20),
)

st.plotly_chart(fig)




