def main():

    pessoa = {'nome':'João', 'idade':25, 'cidade':'São Paulo'}
    print(type(pessoa))
    print(pessoa)

    ##print(pessoa[0]) não acessa assim

    print(pessoa['nome'])
    print(pessoa['idade'])
    print(pessoa['cidade'])

    pessoa['pais'] = 'Brasil'
    print(pessoa['nome'])
    print(pessoa['idade'])
    print(pessoa['cidade'])
    print(pessoa['pais'])

if __name__ == "__main__":
    main()