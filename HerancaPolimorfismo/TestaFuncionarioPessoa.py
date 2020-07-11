from src.HerancaPolimorfismo.Pessoa import Pessoa
from src.HerancaPolimorfismo.Funcionario import Funcionario

def main():

    pessoa = Pessoa('Fulano', '47 3329-4356', 17)
    funcionario = Funcionario('Bruno', '47 3304-9394', 20, 2000, 'bruno.paz', 'bruno123')

    pessoa.validaIdade(pessoa.idade)
    funcionario.validaIdade(funcionario.idade)

if __name__ == '__main__':
    main()