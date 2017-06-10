from datetime import datetime, timedelta
from collections import namedtuple
from functools import reduce

Ponto = namedtuple('Ponto', ['dia', 'entrada', 'saida'])


class Funcionario(object):
    def __init__(self, nome, salario_hora):
        self.nome = nome
        self.salario_hora = salario_hora
        self.pontos = []

    @property
    def salario(self) -> float:
        return self.horas_trabalhadas * self.salario_hora

    @property
    def horas_trabalhadas(self) -> float:
        aux = timedelta(hours=0)
        for p in self.pontos:
            aux += (p.saida - p.entrada)
        horas = aux.total_seconds() / 3600
        return horas

    def adicionar_ponto(self, hora_entrada, hora_saida, dia=None):
        entrada = datetime.strptime(hora_entrada, '%H:%M')
        saida = datetime.strptime(hora_saida, '%H:%M')
        ponto = Ponto(dia, entrada, saida)
        self.pontos.append(ponto)

    def tem_pontos(self) -> bool:
        return len(self.pontos) != 0

    def __str__(self):
        if self.tem_pontos:
            horas_em_minutos = self.horas_trabalhadas * 60
            hora, minutos = divmod(horas_em_minutos, 60)
            return f'''
                nome: {self.nome}
                horas trabalhadas: {hora:2.0f}h e {minutos:2.0f}min
                salario/h: {self.salario_hora}
                salario: {self.salario}'''
        return f'{self.nome}'
