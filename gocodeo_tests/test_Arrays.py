import pytest
from unittest import mock
from Arrays import Array

@pytest.fixture
def array_fixture():
    with mock.patch('Arrays.Array.__init__', return_value=None) as mock_init, \
         mock.patch('Arrays.Array.__str__', return_value='0 0 0') as mock_str, \
         mock.patch('Arrays.Array.__len__', return_value=5) as mock_len, \
         mock.patch('Arrays.Array.__setitem__') as mock_setitem, \
         mock.patch('Arrays.Array.__getitem__', return_value=0) as mock_getitem, \
         mock.patch('Arrays.Array.search', return_value=-1) as mock_search, \
         mock.patch('Arrays.Array.insert') as mock_insert, \
         mock.patch('Arrays.Array.delete') as mock_delete:
        
        # Initialize the Array object
        array_instance = Array(5, int)
        
        # Set up the mock return values
        mock_init.assert_called_once_with(5, int)
        mock_str.assert_called_once()
        mock_len.assert_called_once()
        
        yield array_instance, mock_setitem, mock_getitem, mock_insert, mock_delete, mock_search

# Example of how to use the fixture in a test
def test_array_initialization(array_fixture):
    array_instance, _, _, _, _, _ = array_fixture
    assert len(array_instance) == 5
    assert str(array_instance) == '0 0 0

# happy_path - test_init_array_with_zeroes - Test that array is initialized with zeroes of correct size.
def test_init_array_with_zeroes(array_fixture):
    array_instance, _, _, _, _, _ = array_fixture
    assert array_instance.arrayItems == [0, 0, 0, 0, 0]

# happy_path - test_str_representation - Test that string representation of array is correct.
def test_str_representation(array_fixture):
    array_instance, _, _, _, _, _ = array_fixture
    assert str(array_instance) == '0 0 0'

# happy_path - test_len_of_array - Test that length of array is correct.
def test_len_of_array(array_fixture):
    array_instance, _, _, _, _, _ = array_fixture
    assert len(array_instance) == 5

# happy_path - test_set_item - Test that item can be set at a specific index.
def test_set_item(array_fixture):
    array_instance, mock_setitem, _, _, _, _ = array_fixture
    array_instance[2] = 5
    mock_setitem.assert_called_once_with(2, 5)

# happy_path - test_get_item - Test that item can be retrieved from a specific index.
def test_get_item(array_fixture):
    array_instance, _, mock_getitem, _, _, _ = array_fixture
    item = array_instance[3]
    mock_getitem.assert_called_once_with(3)
    assert item == 0

# happy_path - test_insert_item - Test that item is inserted at correct position.
def test_insert_item(array_fixture):
    array_instance, _, _, mock_insert, _, _ = array_fixture
    array_instance.insert(7, 2)
    mock_insert.assert_called_once_with(7, 2)

# edge_case - test_search_non_existent_item - Test that searching for a non-existent item returns -1.
def test_search_non_existent_item(array_fixture):
    array_instance, _, _, _, _, mock_search = array_fixture
    index = array_instance.search(10)
    mock_search.assert_called_once_with(10)
    assert index == -1

# edge_case - test_insert_full_array - Test that inserting into a full array does not crash.
def test_insert_full_array(array_fixture):
    array_instance, _, _, mock_insert, _, _ = array_fixture
    array_instance.insert(8, 5)
    mock_insert.assert_called_once_with(8, 5)

# edge_case - test_delete_empty_position - Test that deleting from an empty position does not crash.
def test_delete_empty_position(array_fixture):
    array_instance, _, _, _, mock_delete, _ = array_fixture
    array_instance.delete(0, 5)
    mock_delete.assert_called_once_with(0, 5)

# edge_case - test_set_item_invalid_index - Test that setting an item at an invalid index raises an error.
def test_set_item_invalid_index(array_fixture):
    array_instance, mock_setitem, _, _, _, _ = array_fixture
    with pytest.raises(IndexError):
        array_instance[6] = 5
    mock_setitem.assert_not_called()

# edge_case - test_get_item_invalid_index - Test that getting an item from an invalid index raises an error.
def test_get_item_invalid_index(array_fixture):
    array_instance, _, mock_getitem, _, _, _ = array_fixture
    with pytest.raises(IndexError):
        _ = array_instance[6]
    mock_getitem.assert_not_called()

# edge_case - test_delete_non_existent_item - Test that deleting a non-existent item does not affect the array.
def test_delete_non_existent_item(array_fixture):
    array_instance, _, _, _, mock_delete, _ = array_fixture
    array_instance.delete(10, 2)
    mock_delete.assert_called_once_with(10, 2)
    assert array_instance.arrayItems == [0, 0, 0, 0, 0]

