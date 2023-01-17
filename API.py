import pyodbc
import pandas as pd

connection = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=server;'
                            'DATABASE=database;'
                            'UID=user;'
                            'PWD=password')

def create_data(nome, idade, cidade, telefone, profissao):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Pessoa (Nome, idade, cidade, telefone, profissao) VALUES (?,?,?,?,?)", nome, idade, cidade, telefone, profissao)
    connection.commit()
    print("Pessoa registrada com sucesso!")

def read_data():
    query = "SELECT * FROM Pessoa"
    data = pd.read_sql(query, connection)
    return data



def update_data(nome, idade, cidade, telefone, profissao, id):
    cursor = connection.cursor()
    cursor.execute("UPDATE Pessoa SET nome=?, idade=?, cidade=?, telefone=?, profissao=? WHERE ID=?", nome, idade, cidade, telefone, profissao, id)
    connection.commit()
    print("Pessoa Atualizada com sucesso")

def delete_data(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Pessoa WHERE ID=?", id)
    connection.commit()
    print("Pessoa deletada com sucesso")

