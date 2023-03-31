from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Criar o banco de dados
def iniciar_banco_de_dados():
    engine = create_engine('sqlite:///tarefas.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

# Definindo a Base
class Base(DeclarativeBase):
    pass

# Criar a classe game para instanciar objetos
class Games(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    plat = Column(String)
    preco = Column(String)
    qnt = Column(String)
    descricao = Column(String)

# Funcoes para adicionar e listar os games
def adicionar_games(session, name, plat, preco, qnt):
    novo_game = Games(name=name, plat=plat, preco=preco, qnt=qnt)
    session.add(novo_game)
    session.commit()

def listar_games(session):
    return session.query(Games).all()