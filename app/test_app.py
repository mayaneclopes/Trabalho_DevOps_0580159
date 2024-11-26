import pytest
from app import app, db, Aluno
@pytest.fixture
def client():
    app.config['TESTING'] = True 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()  

@pytest.fixture(scope="module")
def init_db():
    yield db
    db.drop_all()

def test_cadastro_aluno(client, init_db):
    response = client.post('/cadastro', data={'nome': 'Mayane Lopes', 'ra': '0580159'})
    assert response.status_code == 201
    aluno = Aluno.query.filter_by(ra='0580159').first()
    assert aluno is not None
    assert aluno.nome == 'Mayane Lopes'
