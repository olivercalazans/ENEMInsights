# MIT License
# Copyright (c) 2024 Oliver Calazans, Joan Mateus, Gleyka Rocha
# Repository: https://github.com/olivercalazans/ENEMInsights
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software...


import csv, os

ARQUIVO_ENTRADA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_ENTRADA = os.path.join(ARQUIVO_ENTRADA, 'MICRODADOS_ENEM_2023.csv')
ARQUIVO_SAIDA   = 'novo_arquivo.csv'

colunas_desejadas = 'TP_FAIXA_ETARIA;TP_SEXO;TP_ESTADO_CIVIL;TP_COR_RACA;TP_ST_CONCLUSAO;TP_ANO_CONCLUIU;TP_ESCOLA;NU_NOTA_CN;NU_NOTA_CH;NU_NOTA_LC;NU_NOTA_MT;NU_NOTA_REDACAO;Q001;Q002;Q006;Q019;Q022;Q024;Q025'
colunas_desejadas = colunas_desejadas.split(';')

with open(ARQUIVO_ENTRADA, mode='r', encoding='ISO-8859-1') as arquivo_entrada, \
     open(ARQUIVO_SAIDA, mode='w', encoding='utf-8', newline='') as arquivo_saida:

    leitor = csv.DictReader(arquivo_entrada, delimiter=';')
    escritor = csv.DictWriter(arquivo_saida, fieldnames=colunas_desejadas, delimiter=';')

    escritor.writeheader()
    for linha in leitor:
        dados_filtrados = {coluna: linha[coluna] for coluna in colunas_desejadas if coluna in linha}
        escritor.writerow(dados_filtrados)

print("Novo arquivo CSV criado com sucesso!")