import streamlit as st

def calcular_salida(w, x, sesgo):
    return sum(w_i * x_i for w_i, x_i in zip(w, x)) + sesgo

def funcion_activacion(valor, tipo):
    if tipo == "Sigmoide":
        return 1 / (1 + 2.71828**(-valor))
    elif tipo == "ReLU":
        return max(0, valor)
    elif tipo == "Tangente hiperbólica":
        return (2 / (1 + 2.71828**(-2 * valor))) - 1

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
    tipo_activacion = st.selectbox("Elige una función de activación", ["Sigmoide", "ReLU", "Tangente hiperbólica"])

if st.button("Calcular la salida"):
    salida_sin_activacion = calcular_salida(pesos, entradas, sesgo)
    salida_con_activacion = funcion_activacion(salida_sin_activacion, tipo_activacion)
    
    st.write(f"La salida de la neurona antes de la función de activación es {salida_sin_activacion}")
    st.write(f"La salida de la neurona después de la función de activación ({tipo_activacion}) es {salida_con_activacion}")
