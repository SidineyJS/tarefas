import sqlite3
conexao = sqlite3.connect('db2.sqlite3')
cursor = conexao.cursor()

ID_tarefa = input('Marcar tarefa concluida? Digite a ID: ')
sql = '''
UPDATE tarefas
	SET status=1
	WHERE id=?
'''

valores = [ID_tarefa]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()