#Exercício 3: Atualizar valores de células

import openpyxl

# Carregar a planilha existente
wb = openpyxl.load_workbook('exercicio1.xlsx')
ws = wb.active

# Atualizar valores de células
ws['B3'] = 33

# Salvar a planilha atualizada
wb.save('exercicio3.xlsx')

# Fechar a planilha
wb.close()
