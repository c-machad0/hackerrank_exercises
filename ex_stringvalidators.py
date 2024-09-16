def check_string(method, string): # recebe method e string como parametros
    # method é uma função que será passada e string é a string escrita pelo usuário
    # generator expression que retorna se, de acordo com o método passado
    # existe algum caracter que atenda ao método pedido
    # ex: se o metodo isalnum() for passado, o metodo any() buscará na string
    # se existe algum caracter que seja alfanumerico
    return any(method(char) for char in string)

if __name__ == '__main__':
    s = input() # string digitada pelo usuário
    
    # lista contendo todos os métodos de string
    methods = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

    # loop que itera sobre cada método, passando-o para a função,
    # juntamente com a string e verificando se é true ou false
    for i in methods:
        print(check_string(i, s))