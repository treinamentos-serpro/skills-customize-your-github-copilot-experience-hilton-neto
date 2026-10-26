# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST para gerenciar tarefas usando FastAPI. Pratique rotas HTTP, validação de dados com Pydantic, operações CRUD e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Iniciar a aplicação FastAPI

#### Descrição
Instale FastAPI e Uvicorn, renomeie `starter-code.py` para `main.py`, prepare a aplicação e crie uma rota para confirmar que a API está funcionando. Execute o servidor localmente e explore a documentação interativa gerada pelo FastAPI.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `pip install fastapi uvicorn`.
- Criar uma aplicação FastAPI disponível na variável `app`.
- Responder a uma requisição `GET /` com uma mensagem indicando que a API está ativa.
- Iniciar o servidor com `uvicorn main:app --reload` e disponibilizar a documentação em `/docs`.

### 🛠️ Criar e listar tarefas

#### Descrição
Implemente os endpoints para criar tarefas e consultar a coleção. Cada tarefa deve ter um título, uma descrição e um identificador gerado pela API. Os dados podem permanecer em memória enquanto o servidor estiver em execução.

#### Requisitos
O programa concluído deve:

- Definir modelos Pydantic para validar os dados de entrada e representar uma tarefa com identificador.
- Implementar `GET /tasks` para retornar todas as tarefas.
- Implementar `POST /tasks` para criar uma tarefa e retornar o recurso criado com status `201 Created`.
- Atribuir um identificador único a cada tarefa criada.

### 🛠️ Completar as operações da API

#### Descrição
Adicione a consulta, atualização e remoção de uma tarefa individual. Use a documentação interativa em `/docs` para testar os endpoints com identificadores existentes e inexistentes.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa pelo identificador.
- Implementar `PUT /tasks/{task_id}` para atualizar o título e a descrição de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente.
- Retornar status `404 Not Found` quando o identificador solicitado não existir e `204 No Content` ao remover uma tarefa com sucesso.
