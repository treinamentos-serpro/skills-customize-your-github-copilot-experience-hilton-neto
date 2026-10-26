# 📘 Atividade: Testes Automatizados com pytest

## 🎯 Objetivo

Aprenda a escrever e executar testes automatizados para funções Python usando pytest. Você vai verificar resultados esperados, testar casos de limite e confirmar que entradas inválidas produzem erros apropriados.

## 📝 Tarefas

### 🛠️ Preparar o ambiente e testar uma função

#### Descrição
Instale o pytest e prepare os arquivos para executar testes. Renomeie o arquivo baixado `starter-code.py` para `starter_code.py` e crie ao lado dele um arquivo chamado `test_starter_code.py`. Comece testando a função `is_even`.

#### Requisitos
O programa concluído deve:

- Instalar pytest com `python -m pip install pytest`.
- Criar `test_starter_code.py` no mesmo diretório de `starter_code.py`.
- Escrever testes que confirmem que `is_even` retorna `True` para um número par e `False` para um ímpar.
- Incluir um teste para o valor zero e executar os testes com `python -m pytest -v`.

### 🛠️ Testar cálculos e casos de limite

#### Descrição
Adicione testes para `calculate_total` e `apply_discount`, verificando tanto entradas comuns quanto limites válidos das funções.

#### Requisitos
O programa concluído deve:

- Confirmar que `calculate_total` soma corretamente uma lista com vários preços.
- Confirmar que `calculate_total` retorna zero para uma lista vazia.
- Verificar que `apply_discount` calcula corretamente um desconto parcial e um desconto de 100%.
- Executar todos os testes e confirmar que passam.

### 🛠️ Verificar entradas inválidas

#### Descrição
Use `pytest.raises` para testar os erros previstos para valores inválidos em `apply_discount`.

#### Requisitos
O programa concluído deve:

- Confirmar que um preço negativo causa `ValueError`.
- Confirmar que uma porcentagem de desconto menor que 0 ou maior que 100 causa `ValueError`.
- Executar a suíte completa com `python -m pytest -v` e confirmar que todos os testes passam.
