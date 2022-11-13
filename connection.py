import psycopg2

conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")

comando = conn.cursor()
comando.execute(""" create table produto (codigo int primary key not null,
nome text not null,
preco real not null,
precovenda real not null);
""")
conn.commit()

print("Tabela criada com sucesso no BD!!!")
conn.close()