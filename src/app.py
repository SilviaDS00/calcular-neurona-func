import streamlit as st
from clase_neuron import Neuron

st.text("Made by Silvia Donaire Serrano")

st.image("https://cdn.pixabay.com/photo/2014/03/25/15/20/neuron-296581_1280.png", width=400)

st.title("Simulador de neurona")

num_entradas = st.slider("Elige el número de entradas/pesos que tendrá la neurona", 1, 10, 1)

# Crear listas vacías para los pesos y las entradas
pesos = []
entradas = []

# Capturar los valores de los pesos y las entradas
st.subheader("Pesos")
columnas_pesos = st.columns(num_entradas)
for i in range(num_entradas):
    with columnas_pesos[i]:
        peso = st.number_input(f"w{i}", key=f"w{i}")
        pesos.append(peso)
st.text(f"w = {pesos}")

st.subheader("Entradas")
columnas_entradas = st.columns(num_entradas)
for i in range(num_entradas):
    with columnas_entradas[i]:
        entrada = st.number_input(f"x{i}", key=f"x{i}")
        entradas.append(entrada)
st.text(f"s = {entradas}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Sesgo")
    sesgo = st.number_input("Introduzca un valor para el sesgo")
with col2:
    st.subheader("Función de activación")
    tipo_activacion = st.selectbox("Elige una función de activación", ["reLU","Sigmoide", "Tangente hiperbólica"])

if st.button("Calcular la salida"):
    # Crear un diccionario para mapear los nombres de las funciones de activación con las funciones de la clase Neuron
    activation_functions = {
            "reLU": "relu",
            "Sigmoide": "sigmoid",
            "Tangente hiperbólica": "tanh"
        }
    # Obtener la función de activación
    activation_function = activation_functions[tipo_activacion]
    # Crear la neurona
    neurona = Neuron(pesos, sesgo, activation_function)
    # Calcular la salida
    salida_sin_activacion = neurona.run(entradas)
    
    st.write(f"La salida de la neurona después de la función de activación ({tipo_activacion}) es {salida_sin_activacion}")
