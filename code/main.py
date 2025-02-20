# MIT License
# Copyright (c) 2024 Oliver Ribeiro Calazans Jeronimo
# Repository: https://github.com/olivercalazans/ENEMInsights
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software...


import json, os, csv, sys


class Main:

    FILE_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self._dicionario         = self._ler_dicionario(self.FILE_PATH)
        self._contador           = 0
        self._dados_participante = list()
        self._maiores_notas      = list()
        self._menores_notas      = list()
        self._dados_gerais       = {
            'faixa_etaria':     self._criar_dicionario("TP_FAIXA_ETARIA"),
            'sexo':             self._criar_dicionario("TP_SEXO"),
            'estado_civil':     self._criar_dicionario("TP_ESTADO_CIVIL"),
            'cor_raca':         self._criar_dicionario("TP_COR_RACA"),
            'conclusao_escola': self._criar_dicionario("TP_ST_CONCLUSAO"),
            'ano_conclusao':    self._criar_dicionario("TP_ANO_CONCLUIU"),
            'tipo_escola':      self._criar_dicionario("TP_ESCOLA"),
            'status_redacao':   self._criar_dicionario("TP_STATUS_REDACAO")
        }


    @staticmethod
    def _ler_dicionario(FILE_PATH) -> dict:
        FILE_PATH = os.path.join(FILE_PATH, 'dicionario.json')
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)


    def _criar_dicionario(self, chave:str) -> dict:
        return {chave: 0 for chave in self._dicionario[chave]}


    def _execute(self) -> None:
        try:
            FILE_PATH = os.path.join(self.FILE_PATH, 'dados_enem_23.csv')
            with open(FILE_PATH, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for linha in reader:
                    self._dados_participante = linha[0].split(';')
                    self._processar_dados()
                    sys.stdout.write(f'\rLinhas processadas: {self._contador}')
                    sys.stdout.flush()
            print('\n')
            self._mostrar_dados()
        except FileNotFoundError: print('Arquivo de dados não encontrado')
        except MemoryError:       print('Memória insuficente para carregar os dados')
        except Exception as erro: print(f'Erro desconhecido:\n{erro}')


    def _processar_dados(self) -> None:
        self._atualize_dados_gerais()
        self._processe_se_houver_todas_as_notas()
        self._contador += 1


    def _atualize_dados_gerais(self) -> None:
        dados_gerais = [self._dados_participante[i] for i in [0, 1, 2, 3, 4, 5, 6, 11]]
        for tipo, valor in zip(self._dados_gerais, dados_gerais):
            self._dados_gerais[tipo][valor] += 1


    def _processe_se_houver_todas_as_notas(self) -> None:
        try:    notas = [float(self._dados_participante[i]) for i in [7, 8, 9, 10, 17]]
        except: pass
        else:   self._classifique_a_nota(notas)


    def _classifique_a_nota(self, notas:list) -> None:
        nota_geral = round(sum(notas) / 5, 1)
        self._dados_participante.append(nota_geral)
        if   nota_geral >= 800: self._maiores_notas.append(self._dados_participante)
        elif nota_geral <= 300: self._menores_notas.append(self._dados_participante)


    def _mostrar_dados(self) -> None:
        for dados in self._dados_gerais:
            for i in self._dados_gerais[dados]:
                print(f'{i} >> {self._dados_gerais[dados][i]}')

        print(len(self._maiores_notas))
        print(len(self._menores_notas))





if __name__ == '__main__':
    x = Main()
    x._execute()
