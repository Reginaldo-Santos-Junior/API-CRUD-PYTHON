import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DESKTOP-server;'
                            'DATABASE=database;'
                            'UID=user;'
                            'PWD=password')

def create_data(nome, idade, cidade, telefone, profissao):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Pessoa (Nome, idade, cidade, telefone, profissao) VALUES (?,?,?,?,?)", nome, idade, cidade, telefone, profissao)
    connection.commit()
    print("Pessoa registrada com sucesso!")

def read_data():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Pessoa")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

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

