from datetime import datetime

from modelos import Funcionario

func = Funcionario('walison filipe', 500)


def test_adicionar_pontos():
    func.adicionar_ponto('14:20', '16:50', datetime.now())
    func.adicionar_ponto('14:20', '16:50', datetime.now())
    assert len(func.pontos) == 2


def test_horas_trabalhadas():
    horas_trabalhadas = 2.5 * 2
    assert func.horas_trabalhadas == horas_trabalhadas


def test_calcular_salario():
    salario_mensal = 1250 * 2
    assert func.salario == salario_mensal


if __name__ == '__main__':
    test_adicionar_pontos()
    test_horas_trabalhadas()
    test_calcular_salario()
    print(func)
