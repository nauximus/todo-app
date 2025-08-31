import pytest
from app import app, db
from models import Task

@pytest.fixture
def client():
    # Test ortamı
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():  # creating context
        db.create_all()
        yield app.test_client()  # test client
        db.drop_all()  # close when test is finished

def test_add_task(client):
    response = client.post('/add', data={'content': 'Test task'}, follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        task = Task.query.first()
        assert task.content == 'Test task'

def test_complete_task(client):
    with app.app_context():
        task = Task(content='Incomplete')
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    client.get(f'/complete/{task_id}', follow_redirects=True)

    with app.app_context():
        task = Task.query.get(task_id)
        assert task.completed == True

def test_delete_task(client):
    with app.app_context():
        task = Task(content='Delete Me')
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    client.get(f'/delete/{task_id}', follow_redirects=True)

    with app.app_context():
        task = Task.query.get(task_id)
        assert task is None
