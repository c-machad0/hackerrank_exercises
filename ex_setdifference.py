n_eng = int(input())

english_students = set(map(int, input().split()))

n_fre = int(input())

french_students = set(map(int, input().split()))

print(len(english_students - french_students))