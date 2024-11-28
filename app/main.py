import os
import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get('https://estudante.ifpb.edu.br/cursos/13/')

semestres = ['#semestre1', '#semestre2', '#semestre3', '#semestre4', '#semestre5', '#semestre6']
tabs = driver.find_elements(By.CSS_SELECTOR, '#maisinfo li a')
dados = []

action = ActionChains(driver)

for semestre, tab in zip(semestres, tabs):
    sleep(5)
    tab.click()

    sleep(5)

    linhas = driver.find_elements(By.CSS_SELECTOR, semestre + ' .disciplinas tbody tr')
    print("\n\n" + semestre)

    # Localizar as linhas na tabela
    for linha in linhas:
        nome_disciplina = linha.find_element(By.CSS_SELECTOR, 'td:nth-child(1) a').text
        carga_horaria = linha.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
        nome_professor = linha.find_element(By.CSS_SELECTOR, 'td:nth-child(3) a').text
        print("Disciplina: " + nome_disciplina)
        dados.append([nome_disciplina, carga_horaria, nome_professor])

# Criar um arquivo Excel
arquivo_excel = openpyxl.Workbook()
planilha = arquivo_excel.active
planilha.title = "Disciplinas"

# Adicionar cabeçalhos
planilha.append(['Disciplinas', 'Carga horária', 'Professor'])

# Adicionar os dados extraídos
for linha in dados:
    planilha.append(linha)

# Salvar o arquivo Excel em tabelas/
if not os.path.exists('tabelas'):
    os.makedirs('tabelas')

arquivo_excel.save('tabelas/disciplinas.xlsx')

print('Dados salvos no arquivo disciplinas.xlsx')

# Fechar o navegador
driver.quit()