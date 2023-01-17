import streamlit as st
from API import create_data, read_data, update_data, delete_data
import json
import pandas as pd


st.set_page_config(
    page_title="CRUD API",
    layout="centered",
)



st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
        body {
            font-family: 'VT323', monospace;
        }
        h1 {
            text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #ff00de, 0 0 70px #ff00de, 0 0 80px #ff00de, 0 0 100px #ff00de;
        }
    </style>
    """, unsafe_allow_html=True)


st.title("---CRUD API COM SQL SERVER---")



col1, col2, col3, col4 = st.columns(4)

with col1:
    criar = st.button("Create", key= 'create')
    nome = st.text_input("Nome", key='nome')
    idade = st.text_input("Idade", key='idade')
    cidade = st.text_input('Cidade', key='cidade')
    telefone = st.text_input('Telefone', key='telefone', help='Adicionar DDD (exp = 011)')
    profissao = st.text_input('Profissão', key='profissao')
    if criar:
        create_data(nome, idade, cidade, telefone, profissao)
        st.success("Pessoa criada com sucesso")
            
with col2:            
    if st.button("Read", key="read"):
        data = read_data()
        st.write(data)
        
with col3:
    atualizar = st.button("Update", key= 'update')
    id = st.text_input("Informe o id para atualizar:")
    nome = st.text_input("Nome")
    idade = st.text_input("Idade")
    cidade = st.text_input('Cidade')
    telefone = st.text_input('Telefone', help='Adicionar DDD (exp = 011)')
    profissao = st.text_input('Profissão')
    if atualizar:
        update_data(nome, idade, cidade, telefone, profissao, id)
        st.success("Pessoa atualizada com sucesso!")
        
with col4:        
    deletar = st.button("Delete", key="delete")
    id = st.text_input("Passe o ID",)
    if deletar and id != " ":
        delete_data(id)
        st.success("Pessoa deletada com sucesso!")
