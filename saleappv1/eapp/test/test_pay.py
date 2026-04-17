from flask_login import user_unauthorized

from eapp.test.test_base import test_client, test_app, test_session
from eapp.models import User, Product, Receipt, ReceiptDetails

def test_pay_success(test_client, mocker):
    class FakeUser:
        is_authenticated = True

    mocker.patch('flask_login.utils._get_user', return_value=FakeUser())

    with test_client.session_transaction() as sess:
        sess['cart'] = {
            "1": {
                "id": "1",
                "name": "aaaa",
                "price": 123,
                "quantity": 2
            }
        }

    mocker.patch('eapp.dao.add_receipt')

    res = test_client.post('/api/pay')

    data = res.get_json()

    assert data['status'] == 200
    with test_client.session_transaction() as sess:
        assert 'cart' not in sess

def test_pay_fail(test_client, mocker):
    class FakeUser:
        is_authenticated = True

    mocker.patch('flask_login.utils._get_user', return_value=FakeUser())

    with test_client.session_transaction() as sess:
        sess['cart'] = {
            "1": {
                "id": "1",
                "name": "aaaa",
                "price": 123,
                "quantity": 2
            }
        }

    mocker.patch('eapp.dao.add_receipt', side_effect=Exception('db error'))

    res = test_client.post('/api/pay')

    data = res.get_json()

    assert data['status'] == 400
    assert data['err_msg'] == 'db error'
    with test_client.session_transaction() as sess:
        assert 'cart' in sess

def test_all(test_session, test_client, mocker):
    u = User(username='demo', password='123', name='admin')
    test_session.add(u)

    p = Product(name='A', price=10, category_id=1)
    p1 = Product(name='B', price=10, category_id=2)
    test_session.add(p)
    test_session.add(p1)
    test_session.commit()

    test_client.post('/api/carts', json={
        'id': 1,
        'name': 'A',
        'price': 10
    })
    test_client.post('/api/carts', json={
        'id': 1,
        'name': 'A',
        'price': 10
    })
    test_client.post('/api/carts', json={
        'id': 2,
        'name': 'B',
        'price': 10
    })

    class FakeUser:
        is_authenticated = True

    mocker.patch('flask_login.utils._get_user', return_value=FakeUser())
    mocker.patch('eapp.dao.current_user', new=u)

    res = test_client.post('/api/pay')

    data = res.get_json()

    assert data['status'] == 200
    with test_client.session_transaction() as sess:
        assert 'cart' not in sess

    r = Receipt.query.first()
    assert r is not None
    assert r.user_id == 1

    assert ReceiptDetails.query.count() == 2