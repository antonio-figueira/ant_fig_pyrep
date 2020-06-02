#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# programa de desencriptação de PDF protegidos por parlavra-passe por tentativa e erro
# DISCLAIMER - desencriptar PDFs ou qualquer outro tipo de informação protegida constitui crime informático punível por lei
# os ficheiros PDF usados pelo autor do programa são da sua autoria ou de pass_word conhecida pelo mesmo
# este programa é só uma "brincadeira" para testar a capacidade de leitura de PDF pelo módulo pikepdf
# este programa ainda está em optimização

# importar o módulo de leitura e gestão de documentos pdf, pikepdf [1] e numpy
import pikepdf
import numpy as np

# definir função de desencriptação (pdf_decrypt)
def pdf_decrypt(file_name, max_key_number): # max_key_number é o número máximo de caracteres que a pass poderá ter (quanto maior for, mais tempo demora o programa a correr)
    
    # textos para o programa
    intro = """\033[1m\nEste programa desencripta/abre PDFs protegidos por palavras-passe em algumas horas. Caso o algoritmo falhe
considere a possibilidade da palavra-passe conter elementos de texto de tipo especial ou do tipo não-ASCII 
(como, por exemplo, caractéres de escrita oriental, sinais de pontuação, entre outros).\033[0m

-- António Figueira (2020) \n"""
    print(intro)
    output_str = "O programa terminou a busca por palavras-passe, tendo identificado o seguinte resultado:"

    # caractéres que podem ser utilizados na pass-word (ASCII)
    keys = ["", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z", "A", "B", "C", "D", "E", "_", "F", "G", "H", "I",
            "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "ç", "Ç", "-"]
        
    # main loop do programa, no qual as palavras-passe serão testadas com combinações de keys
    run = True
    while run:            
        try:
            pass_query = np.random.choice(keys, size = max_key_number)
            pass_query_str = "".join(pass_query)
            pikepdf.Pdf.open(file_name, password = pass_query_str)
            print(output_str, pass_query_str)
            run = False
        except pikepdf.PasswordError:
            continue 
                
# aplicar a função
file_name = "simples.pdf"
pdf_decrypt(file_name, 4)

# by António Figueira, 2020
# refs: [1] - James R. Barlow, pikepdf Python library (Release 1.13.0)

