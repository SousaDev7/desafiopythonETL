# ETL Santander Dev Week - CSV + OpenAI
# Autor: Pedro Sousa

import pandas as pd
import json
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# =========================
# CONFIGURAÇÃO
# =========================
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY não encontrada no .env")

client = OpenAI(api_key=OPENAI_API_KEY)

CSV_FILE = "SDW2023.csv"
OUTPUT_FILE = "relatorio_final_openai.json"
NEWS_ICON = "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg"

# =========================
# EXTRACT
# =========================
print("[EXTRACT] Lendo dados do CSV...")

users = pd.read_csv(CSV_FILE).to_dict(orient="records")

for user in users:
    user["news"] = []

print(f"[EXTRACT] {len(users)} usuários carregados.")

# =========================
# TRANSFORM
# =========================
def generate_ai_message(user):
    prompt = (
        f"Crie uma mensagem curta (máx. 100 caracteres) "
        f"sobre a importância dos investimentos para {user['name']}."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um especialista em marketing financeiro."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

print("\n[TRANSFORM] Gerando mensagens com IA...")

for i, user in enumerate(users, start=1):
    print(f"  [{i}/{len(users)}] Processando {user['name']}...")

    try:
        message = generate_ai_message(user)
    except Exception as e:
        print(f"    ⚠ Erro na IA ({e}). Usando mensagem padrão.")
        message = "Invista hoje para construir um futuro financeiro mais seguro."

    user["news"].append({
        "icon": NEWS_ICON,
        "description": message
    })

    time.sleep(1.2)  # evita erro 429

# =========================
# LOAD
# =========================
print("\n[LOAD] Salvando resultado final...")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print(f"[LOAD] Arquivo '{OUTPUT_FILE}' gerado com sucesso.")
print("\n✅ ETL CONCLUÍDO COM SUCESSO!")
