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

# -------------------
# GRÁFICO 2: Barra moderna horizontal
# -------------------
elif opcion == "Gráfico 2: Barra moderna horizontal":
    tramites2 = ['Trámite A', 'Trámite B']
    estados2 = ['Order Placed', 'Order Confirmed', 'In Production', 'Final Production', 'Shipped']
    estado_actual2 = {'Trámite A': 1, 'Trámite B': 3}

    fig2 = go.Figure()

    for idx, tramite in enumerate(tramites2):
        y = len(tramites2) - idx
        for i, estado in enumerate(estados2):
            color = 'deepskyblue' if i <= estado_actual2[tramite] else 'lightgray'
            border_color = 'navy' if i == estado_actual2[tramite] else 'gray'
            fig2.add_trace(go.Scatter(
                x=[i], y=[y],
                mode='markers+text',
                marker=dict(size=30, color=color, line=dict(width=2, color=border_color)),
                text=[estado],
                textposition="bottom center",
                showlegend=False
            ))
            if i > 0:
                line_color = 'deepskyblue' if i <= estado_actual2[tramite] else 'lightgray'
                fig2.add_trace(go.Scatter(
                    x=[i-1, i], y=[y, y],
                    mode='lines',
                    line=dict(color=line_color, width=8),
                    showlegend=False
                ))

    fig2.update_layout(
        xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        yaxis=dict(tickvals=list(range(1, len(tramites2)+1)), ticktext=tramites2, showgrid=False),
        height=300,
        margin=dict(l=40, r=40, t=30, b=30)
    )
    st.plotly_chart(fig2)

# -------------------
# GRÁFICO 3: Stepper UI
# -------------------
elif opcion == "Gráfico 3: Estilo Stepper UI":
    etapas = ["Create Account", "Login", "Payment", "Confirm"]
    estado_actual3 = 2  # paso actual (0-indexado)

    x_vals = list(range(len(etapas)))
    y_val = 1

    fig3 = go.Figure()

    for i in range(len(etapas) - 1):
        color = "limegreen" if i < estado_actual3 else "lightgray"
        fig3.add_trace(go.Scatter(
            x=[x_vals[i], x_vals[i+1]], y=[y_val, y_val],
            mode="lines",
            line=dict(color=color, width=10),
            showlegend=False
        ))

    for i, label in enumerate(etapas):
        if i < estado_actual3:
            color = "limegreen"
            text_color = "green"
        elif i == estado_actual3:
            color = "deepskyblue"
            text_color = "blue"
        else:
            color = "lightgray"
            text_color = "gray"

        fig3.add_trace(go.Scatter(
            x=[x_vals[i]], y=[y_val],
            mode="markers+text",
            marker=dict(size=60, color=color),
            text=[str(i+1)],
            textposition="middle center",
            textfont=dict(color="white", size=20),
            showlegend=False
        ))

        fig3.add_trace(go.Scatter(
            x=[x_vals[i]], y=[y_val - 0.3],
            mode="text",
            text=[label],
            textposition="bottom center",
            textfont=dict(size=14, color=text_color),
            showlegend=False
        ))

    fig3.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=200,
        margin=dict(l=40, r=40, t=20, b=20),
    )
    st.plotly_chart(fig3)
