from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Constantes
HOST = 'localhost'
USER = 'root'
PASSWORD = 'ceub123456'
DB = 'db_central_servicos'
PORT = 3306

engine = create_engine(f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}?charset=utf8')

# Usando inspect para obter os nomes das tabelas
inspector = inspect(engine)
table_names = inspector.get_table_names()

print("Tabelas no esquema:", DB)
for table_name in table_names:
    print(table_name)

# Auto mapeando as tabelas tt_setor (Tabela Tradicional) e tb_servico (Tabela Forte)
base = automap_base()
base.prepare(autoload_with=engine)

tt_setor = base.classes.tt_setor
tb_servico = base.classes.tb_servico

# Listando os campos das tabelas mapeadas
print('-' * 30)
print("Campos da tabela tt_setor:")
for column in tt_setor.__table__.columns:
    print(f"{column.name} ({column.type})")

print('-' * 30)
print("Campos da tabela tb_servico:")
for column in tb_servico.__table__.columns:
    print(f"{column.name} ({column.type})")


# Implementando CRUD de tt_setor
def listar_setores():
    with Session(engine) as session:
        setores = session.query(tt_setor).all()
        print("\nLista de Setores:")
        for setor in setores:
            print(
                f"Sigla: {setor.sgl_setor}, Nome: {setor.nme_setor}, Email: {setor.eml_setor}, Status: {setor.sts_setor}")


def consultar_setor():
    sigla = input("Digite a sigla do setor a consultar: ")
    with Session(engine) as session:
        setor = session.query(tt_setor).filter(tt_setor.sgl_setor == sigla).first()
        if setor:
            print(
                f"Sigla: {setor.sgl_setor}, Nome: {setor.nme_setor}, Email: {setor.eml_setor}, Status: {setor.sts_setor}")
        else:
            print("Setor não encontrado.")


def incluir_setor():
    sgl_setor = input("Digite a sigla do setor: ")
    nme_setor = input("Digite o nome do setor: ")
    eml_setor = input("Digite o email do setor: ")
    with Session(engine) as session:
        novo_setor = tt_setor(sgl_setor=sgl_setor, nme_setor=nme_setor, eml_setor=eml_setor, sts_setor='A')
        session.add(novo_setor)
        session.commit()
        print("Setor incluído com sucesso! ID: ", novo_setor.idt_setor)


def alterar_setor():
    sigla = input("Digite a sigla do setor a alterar: ")
    with Session(engine) as session:
        setor = session.query(tt_setor).filter(tt_setor.sgl_setor == sigla).first()
        if setor:
            print(
                f"Sigla: {setor.sgl_setor}, Nome: {setor.nme_setor}, Email: {setor.eml_setor}, Status: {setor.sts_setor}")
            setor.sgl_setor = input("Digite a nova sigla do setor: ")
            setor.nme_setor = input("Digite o novo nome do setor: ")
            setor.eml_setor = input("Digite o novo email do setor: ")
            session.commit()
            print("Setor alterado com sucesso!")
        else:
            print("Setor não encontrado.")


def excluir_setor():
    sigla = input("Digite a sigla do setor a excluir: ")
    with Session(engine) as session:
        setor = session.query(tt_setor).filter(tt_setor.sgl_setor == sigla).first()
        if setor:
            print(
                f"Sigla: {setor.sgl_setor}, Nome: {setor.nme_setor}, Email: {setor.eml_setor}, Status: {setor.sts_setor}")
            session.delete(setor)
            session.commit()
            print("Setor excluído com sucesso!")
        else:
            print("Setor não encontrado.")


def menu():
    while True:
        print("\n--- Menu Setores ---")
        print("1. Listar Setores")
        print("2. Consultar Setor")
        print("3. Incluir Setor")
        print("4. Alterar Setor")
        print("5. Excluir Setor")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_setores()
        elif opcao == '2':
            consultar_setor()
        elif opcao == '3':
            incluir_setor()
        elif opcao == '4':
            alterar_setor()
        elif opcao == '5':
            excluir_setor()
        elif opcao == '0':
            engine.dispose()
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
