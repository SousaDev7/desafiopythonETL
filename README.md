# 📊 Projeto ETL com IA Generativa — Santander Dev Week 2023

## 📌 Sobre o Projeto

Este projeto tem como objetivo aplicar na prática o conceito de **ETL (Extract, Transform, Load)** utilizando **Python** e **IA Generativa** para criar mensagens personalizadas sobre investimentos.

O projeto foi baseado no desafio da **Santander Dev Week 2023**, porém algumas adaptações foram necessárias porque a API oficial utilizada no desafio não estava disponível no momento do desenvolvimento.

---

## 🎯 Objetivo

- Ler dados de usuários a partir de um arquivo CSV  
- Gerar mensagens personalizadas utilizando IA Generativa  
- Salvar o resultado final em um arquivo JSON  

---

## 🛠️ Tecnologias Utilizadas

- Python  
- pandas  
- OpenAI API (modelo **gpt-4o-mini**)  
- python-dotenv  

---

## 📁 Estrutura do Projeto

```text
📁 desafioPythonETL
├── etl_santander_csv.py
├── SDW2023.csv
├── relatorio_final_openai.json
├── requirements.txt
├── .gitignore
└── README.md


---

## 🔄 Etapas do ETL

### 📥 Extract (Extração)

- Os dados são lidos a partir do arquivo `SDW2023.csv`
- O CSV contém informações básicas dos usuários
- Os dados são carregados em memória usando a biblioteca **pandas**

---

### 🧠 Transform (Transformação)

- Para cada usuário, é gerada uma mensagem personalizada sobre a importância dos investimentos
- As mensagens são criadas utilizando a **API da OpenAI**
- O nome do usuário é usado para personalizar o texto

---

### 📤 Load (Carregamento)

- Após a geração das mensagens, os dados finais são salvos em um arquivo JSON
- Arquivo gerado: `relatorio_final_openai.json`

---

## ▶️ Como Executar

1. Criar um ambiente virtual  
2. Instalar as dependências do projeto  
3. Configurar a variável de ambiente com a chave da OpenAI  
4. Executar o script Python  

---

## 📝 Observações

- A API original do desafio não estava disponível, por isso foi utilizado um arquivo CSV local
- O foco do projeto é demonstrar o funcionamento do ETL e o uso de IA Generativa

---

📌 **Autor:** Pedro Sousa  
🚀 **Status:** Projeto concluído
