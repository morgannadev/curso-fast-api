from sqlalchemy import select

from fast_zero.models import User


# o pytest sabe fazer sozinho a conexão entre esse teste criado e o conftest.py
def test_create_user(session):
    new_user = User(username='alice', password='secret', email='test@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'
