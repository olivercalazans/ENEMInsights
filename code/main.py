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
        self._melhores_refacoes = dict()
        self._faixa_etaria      = dict()
        self._sexo              = dict()
        self._estado_civil      = dict()
        self._cor_raca          = dict()
        self._conclusao_escola  = dict()
        self._ano_conclusao     = dict()
        self._tipo_escola       = dict()
        self._cien_naturais     = dict()
        self._cien_humanas      = dict()
        self._linguagens        = dict()
        self._matematica        = dict()
        self._status_redacao    = dict()
        self._renda             = dict()


    @staticmethod
    def _ler_dicionario(FILE_PATH) -> dict:
        FILE_PATH = os.path.join(FILE_PATH, 'dicionario.json')
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)


    def _execute(self) -> None:
        try:
            FILE_PATH = os.path.join('dados_enem_23.csv')
            with open(FILE_PATH, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for linha in reader: print(linha, type(linha))
        except MemoryError:       print('Memória insuficente para carregar os dados')
        except FileNotFoundError: print('Arquivo de dados não enontrado')



if __name__ == '__main__':
    x = Main()
    x._execute()
