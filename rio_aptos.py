import streamlit as sl
import pandas as pd

sl.title('Apartamento na Cidade de Rio de Janeiro')

table = pd.read_csv("https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv")

# sl.dataframe(table)

bairro = sl.multiselect('Seleciona o bairro ae mano', table["bairro"].unique())

bairro_escolhido = table[table["bairro"].isin(bairro)]

menor_preco = bairro_escolhido["preco"].min()
maior_preco = bairro_escolhido["preco"].max()

if bairro:
    

    sl.write(menor_preco)
    sl.write(maior_preco)

    valor = sl.slider('Faixa em realzão', menor_preco, maior_preco, (menor_preco, maior_preco))

    sl.data_editor(bairro_escolhido[(bairro_escolhido["preco"] >= valor[0]) & (bairro_escolhido["preco"] <= valor[1])])



    sl.write(valor)

