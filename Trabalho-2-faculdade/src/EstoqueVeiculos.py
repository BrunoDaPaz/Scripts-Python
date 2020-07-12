from src.Veiculo import Veiculo

class EstoqueVeiculos:

    veiculos = [
        Veiculo('X5', 0, 'ABC1234', 'BMW', 'Vermelho', 'Esportivo', 2020, 4, 1),
        Veiculo('Sandero', 0, 'ABC1234', 'Renault', 'Vermelho', 'Sedan', 2014, 4, 1),
        Veiculo('Duster', 0, 'ABC1234', 'Renault', 'Vermelho', 'Camioneta', 2010, 4, 0),
        Veiculo('Opala', 0, 'ABC1234', 'Chevrolet', 'Vermelho', 'Sedan', 2010, 4, 1),
        Veiculo('Chevette', 0, 'ABC1234', 'Chevrolet', 'Vermelho', 'Sendan', 2015, 4, 1),
        Veiculo('Fusca', 0, 'ABC1234', 'Volkswagen', 'Vermelho', 'Sendan', 1998, 4, 1),
        Veiculo('Palio', 0, 'ABC1234', 'FIAT', 'Vermelho', 'Sendan', 2009, 4, 1),
        Veiculo('Gol', 0, 'ABC1234', 'Volkswagen', 'Vermelho', 'Sendan', 2011, 4, 1),
        Veiculo('Saveiro', 0, 'ABC1234', 'Volkswagen', 'Vermelho', 'caminhonete', 2014, 4, 1),
        Veiculo('Montana', 0, 'ABC1234', 'Volkswagen', 'Vermelho', 'caminhonete', 2010, 4, 1)
    ]

    for carros in veiculos:
        if carros.ano < 2010:
            print(carros.nome)
            break