# MIT License
# Copyright (c) 2024 Oliver Ribeiro Calazans Jeronimo
# Repository: https://github.com/olivercalazans/ENEMInsights
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software...


import os, csv


class Main:

    def __init__(self):
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

    
    def _execute(self) -> None:
        try:
            self._ler_dados()
        except MemoryError:       print('Memória insuficente para carregar os dados')
        except FileNotFoundError: print('Arquivo de dados não enontrado')

    
    def _ler_dados(self) -> None:
        FILE_PATH     = os.path.dirname(os.path.abspath(__file__))
        FILE_PATH     = os.path.join('dados_enem_23.csv')
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for linha in reader: print(linha, type(linha))
