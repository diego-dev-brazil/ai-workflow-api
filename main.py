from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime
from fastapi import HTTPException

app = FastAPI()
print("ARQUIVO CERTO CARREGADO")
class InputData(BaseModel):
    texto: str

def classificar_texto(texto):
    texto = texto.lower()

    if "erro" in texto or "problema" in texto:
        return "suporte"
    elif "pagamento" in texto or "boleto" in texto:
        return "financeiro"
    elif "comprar" in texto or "produto" in texto:
        return "vendas"
    else:
        return "geral"

def gerar_resumo(texto):
    frases = texto.split(".")
    return ". ".join(frases[:2]).strip()

def definir_acao(categoria):
    if categoria == "suporte":
        return "Encaminhar para equipe de suporte"
    elif categoria == "financeiro":
        return "Enviar para setor financeiro"
    elif categoria == "vendas":
        return "Encaminhar para CRM"
    else:
        return "Armazenar para análise"

def salvar_dados(dados):
    try:
        with open("dados.json", "r") as f:
            banco = json.load(f)
    except:
        banco = []

    banco.append(dados)

    with open("dados.json", "w") as f:
        json.dump(banco, f, indent=4)

@app.post("/webhook")
def processar_texto(data: InputData):
    if not data.texto.strip():
        raise HTTPException(status_code=400, detail="Texto não pode ser vazio")
    categoria = classificar_texto(data.texto)
    resumo = gerar_resumo(data.texto)
    acao = definir_acao(categoria)

    resultado = {
        "texto": data.texto,
        "categoria": categoria,
        "resumo": resumo,
        "acao": acao,
        "data": str(datetime.now())
    }

@app.get("/dados")
def listar_dados():
    try:
        with open("dados.json", "r") as f:
             return json.load(f)
    except:
        return []
        
@app.get("/teste")
def teste():
    return {"msg": "funcionando"}

    salvar_dados(resultado)

    return resultado