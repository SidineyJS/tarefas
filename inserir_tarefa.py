import sqlite3
conexao = sqlite3.connect('db2.sqlite3')
cursor = conexao.cursor()

sql1 = '''
select * from categoria
'''
consulta = cursor.execute(sql1)
print('ID |  CATEGORIAS')
for categoria in consulta:
    print(categoria[0], categoria[1])

data = input('Digite a data: ')
id_cat = int(input('Qual a id da categoria? '))
tarefa = input('Digite a atividade: ')
hora = input('Digite o horário: ')
prioridade = input('Digite a prioridade: ')

sql = '''
    INSERT into tarefas ('data', id_categoria, tarefa, hora, prioridade) values (?,?,?,?,?);
'''
valores = [data, id_cat, tarefa, hora, prioridade]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()