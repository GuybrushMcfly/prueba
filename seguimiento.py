import streamlit as st
import plotly.graph_objects as go

st.title("📊 Seguimiento de Trámites")

# Estados unificados
estados = ["Preparación", "Cursada", "Asistencia y Evaluación", "Liquidación", "Finalizado"]

# Selector de gráfico
opcion = st.selectbox("Elegí el estilo de gráfico:", [
    "Gráfico 1: Esquema simple",
    "Gráfico 2: Barra moderna horizontal",
    "Gráfico 3: Estilo Stepper UI"
])

# GRÁFICO 1: Esquema simple
if opcion == "Gráfico 1: Esquema simple":
    tramites = ['Trámite 1', 'Trámite 2', 'Trámite 3']
    estado_actual = [1, 3, 4]  # 0-indexado

    fig1 = go.Figure()
    for i, tramite in enumerate(tramites):
        y = len(tramites) - i
        for j, estado in enumerate(estados):
            if j < estado_actual[i]:
                color = 'green'
            elif j == estado_actual[i]:
                color = 'deepskyblue'
            else:
                color = 'lightgray'
            fig1.add_trace(go.Scatter(
                x=[j], y=[y],
                mode='markers+text',
                marker=dict(size=25, color=color),
                text=[estado],
                textfont=dict(color="white", size=12),
                textposition="top center",
                showlegend=False
            ))
            if j > 0:
                fig1.add_trace(go.Scatter(
                    x=[j-1, j], y=[y, y],
                    mode='lines',
                    line=dict(color='gray', width=2),
                    showlegend=False
                ))

    fig1.update_layout(
        yaxis=dict(tickvals=list(range(1, len(tramites)+1)), ticktext=tramites),
        xaxis=dict(tickvals=list(range(len(estados))), ticktext=estados),
        margin=dict(l=100, r=20, t=20, b=20),
        height=300,
    )
    st.plotly_chart(fig1)

# GRÁFICO 2: Barra moderna horizontal
elif opcion == "Gráfico 2: Barra moderna horizontal":
    tramites = ['Trámite A', 'Trámite B']
    estado_actual = {'Trámite A': 2, 'Trámite B': 4}

    fig2 = go.Figure()

    for idx, tramite in enumerate(tramites):
        y = len(tramites) - idx
        for i, estado in enumerate(estados):
            if i < estado_actual[tramite]:
                color = 'green'
                border_color = 'darkgreen'
            elif i == estado_actual[tramite]:
                color = 'deepskyblue'
                border_color = 'navy'
            else:
                color = 'lightgray'
                border_color = 'gray'

            fig2.add_trace(go.Scatter(
                x=[i], y=[y],
                mode='markers+text',
                marker=dict(size=30, color=color, line=dict(width=2, color=border_color)),
                text=[estado],
                textfont=dict(color="white", size=12),
                textposition="bottom center",
                showlegend=False
            ))
            if i > 0:
                line_color = 'deepskyblue' if i <= estado_actual[tramite] else 'lightgray'
                fig2.add_trace(go.Scatter(
                    x=[i-1, i], y=[y, y],
                    mode='lines',
                    line=dict(color=line_color, width=8),
                    showlegend=False
                ))

    fig2.update_layout(
        xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        yaxis=dict(tickvals=list(range(1, len(tramites)+1)), ticktext=tramites, showgrid=False),
        height=300,
        margin=dict(l=40, r=40, t=30, b=30)
    )
    st.plotly_chart(fig2)

# GRÁFICO 3: Stepper UI
elif opcion == "Gráfico 3: Estilo Stepper UI":
    estado_actual = 3  # paso actual (0-indexado)

    x_vals = list(range(len(estados)))
    y_val = 1

    fig3 = go.Figure()

    for i in range(len(estados) - 1):
        color = "green" if i < estado_actual else "lightgray"
        fig3.add_trace(go.Scatter(
            x=[x_vals[i], x_vals[i+1]], y=[y_val, y_val],
            mode="lines",
            line=dict(color=color, width=8),
            showlegend=False
        ))

    for i, label in enumerate(estados):
        if i < estado_actual:
            color = "green"
            text_color = "white"
        elif i == estado_actual:
            color = "deepskyblue"
            text_color = "white"
        else:
            color = "lightgray"
            text_color = "white"

        fig3.add_trace(go.Scatter(
            x=[x_vals[i]], y=[y_val],
            mode="markers+text",
            marker=dict(size=45, color=color),
            text=[str(i+1)],
            textposition="middle center",
            textfont=dict(color="white", size=16),
            showlegend=False
        ))

        fig3.add_trace(go.Scatter(
            x=[x_vals[i]], y=[y_val - 0.15],
            mode="text",
            text=[label],
            textposition="bottom center",
            textfont=dict(size=13, color=text_color),
            showlegend=False
        ))

    fig3.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.4, 1.2]),
        height=250,
        margin=dict(l=40, r=40, t=20, b=20),
    )
    st.plotly_chart(fig3)
