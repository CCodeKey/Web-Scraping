# Projeto de altomação com Selenium

## Como utilizar
1. Criar o `virtualenv`
  ```bash
  python -m venv venv
  ```
2. Ativar o `virtualenv`
  - Windows
     ```bash
      venv/Scripts/activate.bat
      ```
  - Linux
    ```bash
    venv/Scripts/bin/activate
    ```
3. Instalar o Selenium com `pip`
  ```bash
  pip install selenium
  ```

---

## Oque o projeto faz

* Ao executar o script, é feito um processo de altomação, onde é aberto um navegador e em seguida é redirecionado para a página de curos do site do IFPB, onde captura as informações necessárias (Disciplina/ Carga horária/ Professor) e salva essas informações em uma planilha (disciplinas.xlsx)

## Tecnologias
* Python
* Selenium
* openpyxl
