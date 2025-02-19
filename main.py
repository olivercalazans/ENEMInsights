# MIT License
# Copyright (c) 2024 Oliver Ribeiro Calazans Jeronimo
# Repository: https://github.com/olivercalazans/ENEMInsights
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software...


import os
import pandas


class Main:

    def __init__(self):
        self._pessoas = dict()

    
    def _execute(self) -> None:
        try:
            self._ler_dados()
        except FileNotFoundError: print('Arquivo de dados não enontrado')

    
    def _ler_dados(self) -> None:
        FILE_PATH     = os.path.dirname(os.path.abspath(__file__))
        FILE_PATH     = os.path.join('dados_enem_23.csv')
        data_frame    = pandas.read_csv(FILE_PATH, encoding='utf-8')
        dados_dict    = data_frame.to_dict(orient='records')
        self._pessoas = dados_dict