if __name__ == '__main__':
    students = [] # lista que receberá diversas listas com nome e nota
    
    for _ in range(int(input())): # range será o numero 'n' de estudantes
        name = input()
        score = float(input())
        students.append([name, score]) # adiciona na lista o nome e a nota de cada estudante de uma vez
    
    # list comprehension que extrai as notas, retira as duplicadas e ordena
    students_grade = sorted(set([grade for name, grade in students]))

    # obtém a segunda maior nota dentre as notas da lista
    second_grade = students_grade[1]

    # list comprehension que busca apenas o nome dos alunos que tem a segunda maior nota
    students_name = [name for name, grade in students if grade == second_grade]

    # ordena os nomes em ordem alfabetica
    students_name.sort()

    for n in students_name:
        print(n)