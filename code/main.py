# MIT License
# Copyright (c) 2024 Oliver Ribeiro Calazans Jeronimo
# Repository: https://github.com/olivercalazans/ENEMInsights
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software...


import json, os, csv


class Main:

    FILE_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self._dicionario        = self._ler_dicionario(self.FILE_PATH)
        self._maiores_notas     = dict()
        self._menores_notas     = dict()
        self._melhores_redacoes = dict()
        self._dados_gerais      = {
            'faixa_etaria':     {chave: 0 for chave in self._dicionario["TP_FAIXA_ETARIA"]},
            'sexo':             {chave: 0 for chave in self._dicionario["TP_SEXO"]},
            'estado_civil':     {chave: 0 for chave in self._dicionario["TP_ESTADO_CIVIL"]},
            'cor_raca':         {chave: 0 for chave in self._dicionario["TP_COR_RACA"]},
            'conclusao_escola': {chave: 0 for chave in self._dicionario["TP_ST_CONCLUSAO"]},
            'ano_conclusao':    {chave: 0 for chave in self._dicionario["TP_ANO_CONCLUIU"]},
            'tipo_escola':      {chave: 0 for chave in self._dicionario["TP_ESCOLA"]},
            'status_redacao':   {chave: 0 for chave in self._dicionario["TP_STATUS_REDACAO"]}
        }


    @staticmethod
    def _ler_dicionario(FILE_PATH) -> dict:
        FILE_PATH = os.path.join(FILE_PATH, 'dicionario.json')
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)


    def _execute(self) -> None:
        try:
            FILE_PATH = os.path.join(self.FILE_PATH, 'dados_enem_23.csv')
            with open(FILE_PATH, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for linha in reader:
                    dados = linha[0].split(';')
                    print(dados)
                    #self._processar_dados(dados)
        except FileNotFoundError: print('Arquivo de dados não enontrado')
        except MemoryError:       print('Memória insuficente para carregar os dados')


    def _processar_dados(self, dados:list) -> None:
        dados_gerais = [dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[11]]
        self._atualize_dados_gerais()


    def _atualize_dados_gerais(self, dados_gerais:list) -> None:
        for tipo, valor in zip(self._dados_gerais, dados_gerais):
            self._dados_gerais[tipo][valor] += 1


if __name__ == '__main__':
    x = Main()
    x._execute()
