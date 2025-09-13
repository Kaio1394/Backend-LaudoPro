# 🏗️ Laudos API - Backend para Laudos de Engenharia

API RESTful desenvolvida em **FastAPI** para criação, gestão e geração de laudos técnicos na área de engenharia.  
O projeto visa ser a base de um aplicativo completo voltado para engenheiros e técnicos, com foco em produtividade e padronização de documentos.

---

## 🚀 Funcionalidades

- ✅ Autenticação de usuários (JWT)
- 📄 CRUD de laudos técnicos
- 📤 Upload de arquivos e imagens
- 📎 Associação de anexos aos laudos
- 📑 Geração de laudo em PDF
- 📚 Documentação automática com Swagger

---

## 🧱 Tecnologias utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/) (ou SQLite para testes locais)
- [Alembic](https://alembic.sqlalchemy.org/) – Migrações
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI
- [WeasyPrint](https://weasyprint.org/) – Geração de PDF (ou ReportLab)

---

## 📁 Estrutura do Projeto