import streamlit as st

st.title('testeTitle')
st.write('teste')

bandas = {
    "Rock": ["Kiss", "Linkin Park"],
    "Metal": ["Spliknot", "Papa Roach", "Slayer"],
    "Reggae": ["Cleiton Rasta", "Armandinho"],
    "Eletronica": ["Daft Punk", "Skrilex"],
    "Sertanejo": ["Leno Brega", "Chitãozinho e Xororó"]
}

genero = st.selectbox("Escoha o genero musical", bandas.keys())

banda_prediletas = st.selectbox('Escolha a sua banda predileta ai bobão', bandas[genero])

st.text(f'a melhor banda de {genero} é {banda_prediletas}')