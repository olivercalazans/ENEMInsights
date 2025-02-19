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
        self._cien_naturais     = dict()
        self._cien_humanas      = dict()
        self._linguagens        = dict()
        self._matematica        = dict()
        self._faixa_etaria      = {chave: 0 for chave in self._dicionario["TP_FAIXA_ETARIA"]}
        self._sexo              = {chave: 0 for chave in self._dicionario["TP_SEXO"]}
        self._estado_civil      = {chave: 0 for chave in self._dicionario["TP_ESTADO_CIVIL"]}
        self._cor_raca          = {chave: 0 for chave in self._dicionario["TP_COR_RACA"]}
        self._conclusao_escola  = {chave: 0 for chave in self._dicionario["TP_ST_CONCLUSAO"]}
        self._ano_conclusao     = {chave: 0 for chave in self._dicionario["TP_ANO_CONCLUIU"]}
        self._tipo_escola       = {chave: 0 for chave in self._dicionario["TP_ESCOLA"]}
        self._status_redacao    = {chave: 0 for chave in self._dicionario["TP_STATUS_REDACAO"]}


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
        self._atualize_faixa_etaria(dados[0])
        self._atualize_sexo(dados[1])


    def _atualize_faixa_etaria(self, idade:str) -> None:
        self._faixa_etaria[idade] += 1

    def _atualize_sexo(self, sexo:str) -> None:
        self._sexo[sexo] =+ 1


if __name__ == '__main__':
    x = Main()
    x._execute()
