import pytest

from Tables.Building import Building
from Tables.TableDatabase import TableDatabase

# arg for other tests
@pytest.fixture
def empty_building():
    return Building()

# arg for other tests
@pytest.fixture
def building():
    return Building(street_name="street_name", name="name", number=1)

# arg for other tests
@pytest.fixture
def database():
    database = TableDatabase(":memory:")
    Building.create_tab(database)
    return database


def test_default_init_id():
    assert Building.status_id() == 0


def test_set_class_idx():
    Building.set_idx(10)
    assert Building.status_id() == 10
    Building.set_idx(0)


def test_get_first_empty_building_id(empty_building):
    assert empty_building.get_id() == 1
    Building.set_idx(0)


def test_get_name_empty_building(empty_building):
    assert empty_building.get_name() == ''
    Building.set_idx(0)


def test_get_street_name_empty_building(empty_building):
    assert empty_building.get_street_name() == ''
    Building.set_idx(0)


def test_get_number_empty_building(empty_building):
    assert empty_building.get_number() == ''
    Building.set_idx(0)


def test_get_first_building_id(building):
    assert building.get_id() == 1
    Building.set_idx(0)


def test_get_name_building(building):
    assert building.get_name() == "name"
    Building.set_idx(0)


def test_get_street_name_building(building):
    assert building.get_street_name() == "street_name"
    Building.set_idx(0)


def test_get_number_building(building):
    assert building.get_number() == 1
    Building.set_idx(0)


def test_set_id_building(building):
    assert building.get_id() == 1
    building.set_id(10)
    assert building.get_id() == 10
    Building.set_idx(0)


def test_set_name_building(building):
    assert building.get_name() == "name"
    building.set_name("new_name")
    assert building.get_name() == "new_name"
    Building.set_idx(0)


def test_set_street_name_building(building):
    assert building.get_street_name() == "street_name"
    building.set_street_name("new_street_name")
    assert building.get_street_name() == "new_street_name"
    Building.set_idx(0)


def test_insertion_building_to_db(database, building):
    building.insert(database)
    bud = [(
        building.get_id(),
        building.get_street_name(),
        building.get_name(),
        building.get_number()
    )]
    assert Building.select_all(database) == bud
    building.delete(database)
    Building.set_idx(0)


def test_deletion_building_from_db(database, building):
    building.insert(database)
    building.delete(database)
    assert Building.select_all(database) == []
    Building.set_idx(0)


def test_updation_building_in_db(database, building):
    building.insert(database)
    building.set_name("new_name")
    building.update(database)
    bud = [(
        building.get_id(),
        building.get_street_name(),
        building.get_name(),
        building.get_number()
    )]
    assert Building.select_all(database) == bud
    building.delete(database)
    building.set_idx(0)
