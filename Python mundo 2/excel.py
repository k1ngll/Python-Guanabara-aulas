# Dados fictícios para recriar a planilha com base na imagem fornecida
import pandas as pd
import numpy as np
data_albert = {
    "Elemento": ["ITAÚ"] * 10,
    "Status": ["FINALIZADO", "FINALIZADO", "FINALIZADO", "FINALIZADO", "FINALIZADO", "FINALIZADO", "FINALIZADO", "EM ATENDIMENTO", "EM ATENDIMENTO", "EM ATENDIMENTO"],
    "Data": ["segunda-feira, 5 de agosto de 2024", "terça-feira, 6 de agosto de 2024", "quarta-feira, 7 de agosto de 2024", "quinta-feira, 8 de agosto de 2024", "sexta-feira, 9 de agosto de 2024", "segunda-feira, 12 de agosto de 2024", "terça-feira, 13 de agosto de 2024", "quarta-feira, 14 de agosto de 2024", "quinta-feira, 15 de agosto de 2024", "sexta-feira, 16 de agosto de 2024"],
    "Agência": ["1510"] * 10,
    "Data de Finalização": [np.nan] * 10,
    "Data p/ Recebimento": [np.nan] * 10,
    "Pagar": ["R$ 120,00"] * 5 + ["-R$ 120,00"] + ["R$ 120,00"] * 4
}

data_antonio = {
    "Elemento": ["ITAÚ"] * 10,
    "Status": ["FINALIZADO", "FINALIZADO", "FINALIZADO", "FINALIZADO", "FINALIZADO", "FINALIZADO", "FINALIZADO", "EM ATENDIMENTO", "EM ATENDIMENTO", "EM ATENDIMENTO"],
    "Data": ["segunda-feira, 5 de agosto de 2024", "terça-feira, 6 de agosto de 2024", "quarta-feira, 7 de agosto de 2024", "quinta-feira, 8 de agosto de 2024", "sexta-feira, 9 de agosto de 2024", "segunda-feira, 12 de agosto de 2024", "terça-feira, 13 de agosto de 2024", "quarta-feira, 14 de agosto de 2024", "quinta-feira, 15 de agosto de 2024", "sexta-feira, 16 de agosto de 2024"],
    "Agência": ["1510"] * 10,
    "Data de Finalização": [np.nan] * 10,
    "Data p/ Recebimento": [np.nan] * 10,
    "Pagar": ["R$ 120,00"] * 5 + ["-R$ 120,00"] + ["R$ 120,00"] * 4
}

# Criando os dataframes
df_albert = pd.DataFrame(data_albert)
df_antonio = pd.DataFrame(data_antonio)

# Salvando em um arquivo Excel com duas abas
file_path_recreated_filled = "C:/Users/anton/Downloads/Edge downloads/planidsnahas/minha.xlsx"
with pd.ExcelWriter(file_path_recreated_filled) as writer:
    df_albert.to_excel(writer, sheet_name="Atendimento Itaú Albert", index=False)
    df_antonio.to_excel(writer, sheet_name="Atendimento Itaú Antonio", index=False)

file_path_recreated_filled
