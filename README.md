
# Web Scraping
Ao executar o script, é feito um processo de altomação, onde é aberto um navegador e em seguida é carregado á página de curos do site do IFPB, onde captura as informações necessárias (Disciplina/ Carga horária/ Professor) e salva essas informações em uma planilha (disciplinas.xlsx). Todo esse processo foi desenvolvido em Python utilziando  o framework de teste de automação de código aberto (Selenium).
## Tirar
## Autores 
- [@Gabriel Tertuliano](https://www.github.com/ccodekey)
- [@Hellen Lima](https://www.github.com/hellenilda)
- [@Victor Pereira](https://www.instagram.com/victorpereiragomes/)
- [@Juliana](https://www.instagram.com/jullis_august/)
## Estrutura do Projeto

```bash
├── app/             
    ├── main.py                      # Script de altomação 
    └── tabelas/
        └── disciplinas.xlsx         # Planilha onde serão salvo os dados
├── README.md                        # Documentação do projeto 
└── requirements.txt                 # Dependências necessárias 
```

## Como executar

- Criar o `virtualenv`
  ```bash
  python -m venv venv
  ```
- Ativar o `virtualenv`
  - Windows
     ```bash
      .\venv/Scripts/Activate.ps1
      ```
  - Linux
    ```bash
    source venv/Scripts/bin/activate
    ```
- Instalar o Selenium com `pip`
  ```bash
  pip install selenium
  ```
## Stack utilizada
- Python
- Selenium
- os
- openpyxl