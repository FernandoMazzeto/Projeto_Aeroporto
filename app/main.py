from fastapi import FastAPI
from app.routers import usuario, sessao, aeroporto, voo, compra
from app.database import criar_tabelas

app = FastAPI(
    title="API de Venda de Passagens Aéreas",
    version="1.0.0"
)

# Criação das tabelas no banco de dados ao iniciar
criar_tabelas()

# Registro das rotas
app.include_router(usuario.router)
app.include_router(sessao.router)
app.include_router(aeroporto.router)
app.include_router(voo.router)
app.include_router(compra.router)
