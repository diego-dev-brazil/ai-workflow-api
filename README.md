# AI Workflow API

API que simula automações com Inteligência Artificial, realizando:
- Classificação de textos
- Geração de resumos
- Roteamento automático (workflow)

## Tecnologias
- FastAPI
- Python
- JSON

## Funcionalidades
- POST /webhook → processa texto
- GET /dados → lista dados processados

## Conceitos aplicados
- Automação de processos
- Simulação de IA
- Integração via API
- Estrutura de workflows (No-Code)

## Como rodar
```bash
python -m uvicorn main:app --reload

## Exemplo de uso

POST /webhook

{
  "texto": "Estou com problema no pagamento"
}
