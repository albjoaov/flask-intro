# Passo a passo

1. Criação do ambiente virtual
2. Ativação do ambiente virtual
3. Instalação das minhas dependendências

## Trabalhando com Flask

1. Como inicializar um servidor com Flask
2. Diferenças do ambiente local para o ambiente de produção
3. Como criar uma rota

Extra
- Definição da variavel especial `__name__`
- Para que serve o `if __name__ == "__main__":`

## Principais funcionalidades do Flask

- Request e Response
  - Lidando com variáveis no caminho da requisição
    - Query param
    - Body
    - Path
  - Erros (segurança e tipo de renderização)
  - Tipo de método e template

## Lidando com o banco de dados

- Driver: psycopg2
  - Instalação: `pip install psycopg2`
    - ou `pdm add psycopg2`
- ORM: SQLAlchemy

- Instalando o Bcrypt: `pip install bcrypt`
- SQL Injection: https://www.hacksplaining.com/exercises/sql-injection

## Desafios:

1. Paginação
2. O que são e como fazer operações de JOIN
3. Entender a abertura e fechamento de conexões. Pesquisar pool de conexões. Como criá-las?
4. Criar uma operação de CRUD com o ORM do SQLAlchemy
