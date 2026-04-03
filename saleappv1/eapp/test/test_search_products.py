from eapp.dao import load_products
from eapp.test.test_base import sample_products, test_app, test_session


def test_all(sample_products):
    actual_products = load_products()

    assert len(actual_products) == len(sample_products)

def test_kw(sample_products):
    actual_products = load_products(kw='iPhone')

    assert len(actual_products) == 3
    assert all('iPhone' in p.name for p in actual_products)

def test_cate(sample_products):
    actual_products = load_products(cate_id=2)

    assert len(actual_products) == 3
    assert all(p.category_id==2 for p in actual_products)

def test_kw_cate(sample_products):
    actual_products = load_products(kw='iPhone', cate_id=2)

    assert len(actual_products) == 2
    assert all(p.category_id == 2 and 'iPhone' in p.name for p in actual_products)

def test_paging(sample_products):
    actual_products = load_products(page=1)
    assert len(actual_products) == 2

    actual_products = load_products(page=3)
    assert len(actual_products) == 1

def test_kw_paging(sample_products):
    actual_products = load_products(kw='Galaxy', page=1)

    assert len(actual_products) == 1
    assert all('Galaxy' in p.name for p in actual_products)

    actual_products = load_products(kw='Galaxy', page=2)
    assert len(actual_products) == 0