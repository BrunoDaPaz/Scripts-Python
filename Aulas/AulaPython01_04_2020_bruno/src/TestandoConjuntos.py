def main():

    a = set('abacate')
    b = set('abacaxi')

    print(a)
    print(b)
    print(a - b) # diferença, tem no a e não tem no b
    print(a | b) # união, tem no a e tem no b
    print(a & b) # interseção
    print(a & b) # diferença simétrica


if __name__ == "__main__":
    main()