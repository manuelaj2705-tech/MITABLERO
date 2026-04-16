import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Fuente divertida desde Google Fonts
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Título centrado con tipografía estilo niños
st.markdown("""
<h1 style='text-align: center; font-family: "Comic Neue", cursive; color: #FF6F61;'>
🎨 Tablero para dibujo
</h1>
""", unsafe_allow_html=True)

# Texto centrado
st.markdown("""
<p style='text-align: center; font-size:18px;'>
En este tablero puedes dejar volar tu imaginación sin límites. 
Cada trazo, forma y color es una oportunidad para expresar tus ideas, 
crear lo que quieras y darle vida a tu creatividad.
</p>
""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Propiedades del Tablero")

    # Canvas dimensions
    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Drawing mode selector
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Stroke width slider
    stroke_width = st.slider("Selecciona el ancho de línea:", 1, 30, 15)

    # Stroke color picker
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")

    # Background color
    bg_color = st.color_picker("Color de fondo", "#000000")

# Canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)
