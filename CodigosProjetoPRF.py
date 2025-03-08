'''Atribui os IDS a um aplanilha com base em outra'''

import pandas as pd

# Carregar os arquivos 
planilha1 = pd.read_excel(r"C:\Users\Power BI\Desktop\Pessoal\ProjetoPrf\Tabelas dimensão\D08_PERIODO_SEMANA.xlsx")  # Contém ID,
planilha2 = pd.read_excel(r"C:\Users\Power BI\Desktop\Pessoal\ProjetoPrf\IDSAtribuidos\PessoaIdade.xlsx")  # Precisa receber os IDs

#Passar colunas pertinenetes da primeira planilha
planilha1 = planilha1[['IDPeriodoSemana','PeriodoSemana']]  

#Faz o merge adicionando a coluna de ID através de uma coluna em comum
#Passar coluna "chave" a qual o codigo vai buscar para atribuir o ID
planilha2 = planilha2.merge(planilha1, on=['PeriodoSemana'], how='left')

# Salvar o resultado
planilha2.to_excel("PessoaPeriodoSemana.xlsx", index=False)


# Salvar no caminho desejado
caminho_saida = r"C:/Users/Power BI/Desktop/Pessoal/ProjetoPrf/IDSAtribuidos/PessoaPeriodoSemana.xlsx"
planilha2.to_excel(caminho_saida, index=False)


print(f"Arquivo salvo em: {caminho_saida}")
print("Processo concluído! A nova planilha foi salva")


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''Atribuição dos IDs conforme faixa de Hora'''
planilha1 = pd.read_excel(r"C:\Users\Power BI\Desktop\Pessoal\ProjetoPrf\Tabelas dimensão\D08_PERIODO_SEMANA.xlsx")  # Contém ID,
planilha2 = pd.read_excel(r"C:\Users\Power BI\Desktop\Pessoal\ProjetoPrf\IDSAtribuidos\PessoaIdade.xlsx")  # Precisa receber os IDs


def atribuir_faixa_horario(horario):
    if "00:00:00" <= horario <= "06:00:00":
        return 1
    elif "06:01:00" <= horario <= "12:00:00":
        return 2
    elif "12:01:00" <= horario <= "18:00:00":
        return 3
    elif "18:01:00" <= horario <= "23:59:59":
        return 4
    else:
        return None  # Para valores inválidos

# Converte a coluna de horário para formato datetime
planilha2['Horario'] = pd.to_datetime(planilha2['Horario'], format='%H:%M:%S').dt.time

# Aplica a função para atribuir os IDs de faixa horária
planilha2['IDFaixaHorario'] = planilha2['Horario'].apply(lambda x: atribuir_faixa_horario(str(x)))

# Salva o resultado
caminho_saida = r"C:/Users/Power BI/Desktop/Pessoal/ProjetoPrf/IDSAtribuidos/PessoaIdade.xlsx"
planilha2.to_excel(caminho_saida, index=False)

print(f"Arquivo salvo em: {caminho_saida}")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""Função para atribuir as faixas de hora"""
def atribuir_faixa_horario(horario):
    if "00:00:00" <= horario <= "04:00:00":
        return 1
    elif "04:01:00" <= horario <= "08:00:00":
        return 2
    elif "08:01:00" <= horario <= "12:00:00":
        return 3
    elif "12:01:00" <= horario <= "16:00:00":
        return 4
    elif "16:01:00" <= horario <= "20:00:00":
        return 5
    elif "20:01:00" <= horario <= "24:00:00":
        return 6
    else:
        return None  # Para valores inválidos