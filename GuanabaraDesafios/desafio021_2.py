'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame
import tkinter as tk
from tkinter import filedialog
import os

# Inicializa o mixer do pygame
pygame.mixer.init()

# Função para reproduzir o arquivo MP3
def reproduzir_mp3(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return

    # Carrega o arquivo MP3
    pygame.mixer.music.load(caminho_arquivo)
    
    # Inicia a reprodução
    pygame.mixer.music.play()
    
    print(f"Reproduzindo '{caminho_arquivo}'... Pressione 'Enter' para parar a reprodução.")
    
    # Mantém o programa em execução até o usuário pressionar Enter
    input()
    
    # Para a reprodução
    pygame.mixer.music.stop()

# Função para abrir a caixa de diálogo de seleção de arquivos
def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo MP3",
        filetypes=[("Arquivos MP3", "*.mp3")]
    )
    if caminho_arquivo:
        reproduzir_mp3(caminho_arquivo)
    else:
        print("Nenhum arquivo selecionado.")

# Chama a função para selecionar o arquivo
selecionar_arquivo()
