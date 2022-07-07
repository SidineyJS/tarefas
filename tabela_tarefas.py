import sqlite3
conexao = sqlite3.connect('db2.sqlite3')

sql = '''
	CREATE TABLE tarefas (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"data" TEXT(20) NOT NULL,
	id_categoria INTEGER,
	tarefa TEXT(250),
	prioridade INTEGER
	CONSTRAINT tarefas_FK_1 FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);
'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()