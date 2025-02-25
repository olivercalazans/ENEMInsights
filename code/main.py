# MIT License
# Copyright (c) 2024 Oliver Calazans, Joan Mateus, Gleyka Rocha
# Repository: https://github.com/olivercalazans/ENEMInsights
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software...


import json, os, csv, sys, tkinter
import tkinter.filedialog


# 0 TP_FAIXA_ETARIA         # 10 NU_NOTA_MT
# 1 TP_SEXO                 # 11 NU_NOTA_REDACAO
# 2 TP_ESTADO_CIVIL         # 12 Q001
# 3 TP_COR_RACA             # 13 Q002
# 4 TP_ST_CONCLUSAO         # 14 Q006
# 5 TP_ANO_CONCLUIU         # 15 Q019
# 6 TP_ESCOLA               # 16 Q022
# 7 NU_NOTA_CN              # 17 Q024
# 8 NU_NOTA_CH              # 18 Q025
# 9 NU_NOTA_LC

class Main:

    def __init__(self):
        self._dicionario:dict         = self._ler_dicionario(os.path.dirname(os.path.abspath(__file__)))
        self._dados_melhores:dict     = self._criar_dicionario()
        self._dados_piores:dict       = self._criar_dicionario()
        self._dados_participante      = list()
        self._contador:int            = 0
        self._numero_notas_altas:int  = 0
        self._numero_notas_baixas:int = 0


    @staticmethod
    def _ler_dicionario(FILE_PATH) -> dict:
        FILE_PATH = os.path.join(FILE_PATH, 'dicionario.json')
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)


    def _criar_dicionario(self, CHAVES=None) -> dict:
        if not CHAVES: CHAVES = list(self._dicionario.keys())
        return {x: {chave: 0 for chave in self._dicionario[x]} for x in CHAVES}


    def _execute(self) -> None:
        try:
            self._processe_base_de_dados()
            self._crie_arquivos('dados_melhores', self._numero_notas_altas, self._dados_melhores)
            self._crie_arquivos('dados_piores', self._numero_notas_baixas, self._dados_piores)
        except FileNotFoundError: print('Arquivo de dados não encontrado')
        except MemoryError:       print('Memória insuficente para carregar os dados')
        except Exception as erro: print(f'\nErro desconhecido:\n{erro}')


    def _processe_base_de_dados(self) -> None:
        COLUNAS_DESEJADAS  = 'TP_FAIXA_ETARIA;TP_SEXO;TP_ESTADO_CIVIL;TP_COR_RACA;TP_ST_CONCLUSAO;TP_ANO_CONCLUIU;TP_ESCOLA;NU_NOTA_CN;NU_NOTA_CH;NU_NOTA_LC;NU_NOTA_MT;NU_NOTA_REDACAO;Q001;Q002;Q006;Q019;Q022;Q024;Q025'
        COLUNAS_DESEJADAS  = COLUNAS_DESEJADAS.split(';')
        ARQUIVO_DE_ENTRADA = self._escolher_arquivo()

        with open(ARQUIVO_DE_ENTRADA, mode='r', encoding='ISO-8859-1') as ARQUIVO_DE_ENTRADA:
            leitor = csv.DictReader(ARQUIVO_DE_ENTRADA, delimiter=';')

            for linha in leitor:
                self._dados_participante = [linha[coluna] for coluna in COLUNAS_DESEJADAS if coluna in linha]
                self._processe_se_houver_todas_as_notas()
                self._contador += 1
                sys.stdout.write(f'\rLinhas processadas: {self._contador}')
                sys.stdout.flush()


    @staticmethod
    def _escolher_arquivo() -> str:
        root = tkinter.Tk()
        root.withdraw()
        return tkinter.filedialog.askopenfilename(title="Selecione um arquivo")


    def _atualize_valores(self, dicionario:dict, indices:list) -> None:
        dados = [self._dados_participante[i] for i in indices]
        for tipo, valor in zip(dicionario, dados):
           dicionario[tipo][valor] += 1


    def _processe_se_houver_todas_as_notas(self) -> None:
        try:    notas = [float(self._dados_participante[i]) for i in [7, 8, 9, 10, 11]]
        except: pass
        else:   self._classifique_a_nota(notas)


    def _classifique_a_nota(self, notas:list) -> None:
        INDICES    = [0, 1, 2, 3, 4, 5, 6, -7, -6, -5, -4, -3, -2, -1]
        nota_geral = round(sum(notas)/5, 1)
        if nota_geral >= 800:
            self._numero_notas_altas += 1
            self._atualize_valores(self._dados_melhores, INDICES)
        elif nota_geral <= 400:
            self._numero_notas_baixas += 1
            self._atualize_valores(self._dados_piores, INDICES)


    def _crie_arquivos(self, nome_do_arquivo:str, numero_participantes:int, dicionario:dict) -> None:
        # ARQUIVO CSV
        with open(nome_do_arquivo + '.csv', mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';')
            escritor.writerow(['total', 'total de participantes', numero_participantes])
            for classe in dicionario:
                for chave in dicionario[classe]:
                    descricao = self._dicionario[classe][chave]
                    escritor.writerow([classe, descricao, dicionario[classe][chave]])

        # ARQUIVO JSON
        with open(nome_do_arquivo + '.json', 'w') as arquivo:
            json.dump(dicionario, arquivo, indent=4)

        print(f'Arquivos {nome_do_arquivo}.csv e {nome_do_arquivo}.json criados')




if __name__ == '__main__':
    x = Main()
    x._execute()