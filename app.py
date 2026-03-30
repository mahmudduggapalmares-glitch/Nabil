import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Feliz Cumpleaños Nabil", page_icon="🎂")

# Efecto de globos al cargar
st.balloons()

# Título principal con estilo
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>¡Feliz Cumpleaños, Nabil! 🎈</h1>", unsafe_allow_html=True)

# Espaciador
st.write("---")

# Mensaje principal
st.subheader("Un mensaje especial para ti:")
st.info("""
Que cumplas muchísimos años más llenos de salud y alegría. 
Recuerda siempre que nunca estarás solo; aquí estamos todos para apoyarte. 
Tu familia, tus amigos y todos los que te queremos estaremos contigo en cada paso que des.
""")

# Sección interactiva: Mensajes de la familia
st.markdown("### 👨‍👩‍👦‍👦 De parte de todos nosotros")
col1, col2 = st.columns(2)

with col1:
    st.success("✨ ¡Eres una persona increíble!")
    st.success("🌟 Que este nuevo año de vida sea el mejor.")

with col2:
    st.success("💪 Siempre adelante, Nabil.")
    st.success("❤️ Aquí tienes a tu gente para lo que sea.")

# Un detalle interactivo (Generador de deseos)
st.write("---")
if st.button("Haz clic para recibir un deseo de cumpleaños"):
    deseos = [
        "¡Que todos tus proyectos se cumplan!",
        "¡Mucha salud y éxito en todo lo que hagas!",
        "¡Que nunca te falte una razón para sonreír!",
        "¡Disfruta tu día al máximo con los que más quieres!"
    ]
    st.balloons()
    st.header(f"🎉 {random.choice(deseos)}")

# Pie de página
st.write("---")
st.caption("Creado con mucho cariño para Nabil en su día especial.")
