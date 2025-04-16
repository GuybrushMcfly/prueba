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


import random

st.header("📌 PRUEBA DE ESTADOS DE CURSOS")

# Cursos disponibles
cursos_disponibles = [f"CURSO{i}" for i in range(1, 9)]
estados = ["Preparación", "Cursada", "Asistencia y Evaluación", "Liquidación", "Finalizado"]

# Multiselect con límite de 5
seleccionados = st.multiselect(
    "Seleccioná hasta 5 cursos para visualizar su progreso:",
    cursos_disponibles,
    max_selections=5
)

if seleccionados:
    st.markdown("---")
    for curso in seleccionados:
        # Estado aleatorio (0-indexado)
        estado_actual = random.randint(0, len(estados) - 1)

        x_vals = list(range(len(estados)))
        y_val = 1

        fig = go.Figure()

        # Líneas entre pasos
        for i in range(len(estados) - 1):
            color = "#4DB6AC" if i < estado_actual else "lightgray"
            fig.add_trace(go.Scatter(
                x=[x_vals[i], x_vals[i+1]], y=[y_val, y_val],
                mode="lines",
                line=dict(color=color, width=8),
                showlegend=False
            ))

        # Círculos y textos
        for i, label in enumerate(estados):
            if i < estado_actual:
                #color = "green"
                color = "#4DB6AC"
                text_color = "white"
            elif i == estado_actual:
                #color = "deepskyblue"
                color = "#FF8A65"
                text_color = "white"
            else:
                color = "lightgray"
                text_color = "white"

            fig.add_trace(go.Scatter(
                x=[x_vals[i]], y=[y_val],
                mode="markers+text",
                marker=dict(size=45, color=color),
                text=[str(i+1)],
                textposition="middle center",
                textfont=dict(color="white", size=16),
                showlegend=False
            ))

            fig.add_trace(go.Scatter(
                x=[x_vals[i]], y=[y_val - 0.15],
                mode="text",
                text=[label],
                textposition="bottom center",
                textfont=dict(size=13, color=text_color),
                showlegend=False
            ))

        fig.update_layout(
            title=dict(text=f"📘 {curso}", x=0.02, xanchor="left", font=dict(size=18)),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.4, 1.2]),
            height=180,
            margin=dict(l=30, r=30, t=30, b=30),
        )

        st.plotly_chart(fig)
else:
    st.info("Seleccioná hasta 5 cursos para visualizar su progreso.")





import random
import streamlit as st
import plotly.graph_objects as go

st.header("📘 ESTADO DE CURSOS POR PROCESO")

# Cursos disponibles
cursos = ["HTML Y CSS", "INTRODUCCIÓN A R", "ENCUESTADORES IPC"]
curso_seleccionado = st.selectbox("Seleccioná una actividad:", cursos)

# Procesos y sus pasos
procesos = {
    "APROBACION ACTIVIDAD": [
        "Diseño", "Autorización INAP", "Carga SAI", "Tramitación Expediente",
        "Dictamen INAP", "Creación Comisión"
    ],
    "CAMPUS": [
        "Armado Aula", "Matriculación participantes", "Apertura Curso",
        "Cierre Curso", "Notas y Asistencia"
    ],
    "DICTADO COMISION": [
        "Difusión", "Asignación Vacantes", "Cursada",
        "Evaluación y Carga SAI", "Liquidación", "Finalizado"
    ]
}

# Simular estados actuales por proceso
estado_actual_procesos = {
    nombre: random.randint(0, len(pasos) - 1)
    for nombre, pasos in procesos.items()
}

# Colores
color_completado = "#4DB6AC"
color_actual = "#FF8A65"
color_pendiente = "#D3D3D3"

if curso_seleccionado:
    for nombre_proceso, pasos in procesos.items():
        x_vals = list(range(len(pasos)))
        y_val = 1
        estado_actual = estado_actual_procesos[nombre_proceso]

        fig = go.Figure()

        # Líneas
        for i in range(len(pasos) - 1):
            color = color_completado if i < estado_actual else color_pendiente
            fig.add_trace(go.Scatter(
                x=[x_vals[i], x_vals[i+1]], y=[y_val, y_val],
                mode="lines",
                line=dict(color=color, width=8),
                showlegend=False
            ))

        # Círculos y etiquetas
        for i, paso in enumerate(pasos):
            if i < estado_actual:
                color = color_completado
                text_color = "white"
            elif i == estado_actual:
                color = color_actual
                text_color = "white"
            else:
                color = color_pendiente
                text_color = "white"

            fig.add_trace(go.Scatter(
                x=[x_vals[i]], y=[y_val],
                mode="markers+text",
                marker=dict(size=45, color=color),
                text=[str(i+1)],
                textposition="middle center",
                textfont=dict(color="white", size=16),
                hovertext=[paso],
                hoverinfo="text",
                showlegend=False
            ))

            fig.add_trace(go.Scatter(
                x=[x_vals[i]], y=[y_val - 0.15],
                mode="text",
                text=[paso],
                textposition="bottom center",
                textfont=dict(size=13, color=text_color),
                showlegend=False
            ))

        fig.update_layout(
            title=dict(text=f"🔹 {nombre_proceso}", x=0.01, xanchor="left", font=dict(size=17)),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.3, 1.2]),
            height=200,
            margin=dict(l=20, r=20, t=30, b=0),
        )
        st.plotly_chart(fig)

