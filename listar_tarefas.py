import sqlite3
conexao = sqlite3.connect('db2.sqlite3')
cursor = conexao.cursor()
data = input('Digite a data: ')
#O campo STATUS deve ser preenchido com 1=SIM ou 2=NÃO
sql = '''
select * from tarefas WHERE data=? order by hora;
'''
valores = [data]
consulta = cursor.execute(sql, valores)
print('ID   | Data   |  TAREFA    |    HORÁRIO    |   STATUS')
for tarefa in consulta:
    print(tarefa[0], tarefa[1], tarefa[3], tarefa[4], tarefa[6])