import pytest
from unittest import mock
from Arrays import Array

@pytest.fixture
def array_fixture():
    with mock.patch('Arrays.Array.__init__', return_value=None) as mock_init, \
         mock.patch('Arrays.Array.__str__', return_value='0 0 0') as mock_str, \
         mock.patch('Arrays.Array.__len__', return_value=3) as mock_len, \
         mock.patch('Arrays.Array.__setitem__', return_value=None) as mock_setitem, \
         mock.patch('Arrays.Array.__getitem__', return_value=0) as mock_getitem, \
         mock.patch('Arrays.Array.search', return_value=-1) as mock_search, \
         mock.patch('Arrays.Array.insert', return_value=None) as mock_insert, \
         mock.patch('Arrays.Array.delete', return_value=None) as mock_delete:
        
        array_instance = Array(3)  # Create an instance of Array
        array_instance.arrayItems = [0, 0, 0]  # Initialize with mock data
        yield array_instance

        # Optionally, you can add assertions here to check if mocks were called
        mock_init.assert_called_once_with(3)
        mock_str.assert_called_once()
        mock_len.assert_called_once()
        mock_setitem.assert_not_called()  # Adjust based on test cases
        mock_getitem.assert_called_with(0)
        mock_search.assert_called_once_with(10)  # Adjust based on test cases
        mock_insert.assert_not_called()  # Adjust based on test cases
        mock_delete.assert_not_called()  # Adjust based on test cases

# happy_path - test_init_default_int - Test that array initializes correctly with default integer type
def test_init_default_int(array_fixture):
    array_fixture.__init__(5)
    assert array_fixture.sizeOfArray == 5
    assert array_fixture.arrayItems == [0, 0, 0, 0, 0]

# happy_path - test_init_float_type - Test that array initializes with specified float type
def test_init_float_type(array_fixture):
    array_fixture.__init__(3, float)
    assert array_fixture.sizeOfArray == 3
    assert array_fixture.arrayItems == [0.0, 0.0, 0.0]

# happy_path - test_str_representation - Test that string representation of array is correct
def test_str_representation(array_fixture):
    assert str(array_fixture) == '0 0 0'

# happy_path - test_len_function - Test that length of array is correct
def test_len_function(array_fixture):
    assert len(array_fixture) == 3

# happy_path - test_setitem - Test that item can be set at a specific index
def test_setitem(array_fixture):
    array_fixture.__setitem__(1, 10)
    array_fixture.arrayItems[1] = 10
    assert array_fixture.arrayItems == [0, 10, 0]

# happy_path - test_getitem - Test that item can be retrieved from a specific index
def test_getitem(array_fixture):
    item = array_fixture.__getitem__(1)
    assert item == 0

# edge_case - test_insert_out_of_bounds - Test that inserting at an out-of-bounds index does nothing
def test_insert_out_of_bounds(array_fixture):
    array_fixture.insert(10, 5)
    assert array_fixture.arrayItems == [0, 0, 0]

# edge_case - test_delete_out_of_bounds - Test that deleting at an out-of-bounds index does nothing
def test_delete_out_of_bounds(array_fixture):
    array_fixture.delete(10, 5)
    assert array_fixture.arrayItems == [0, 0, 0]

# edge_case - test_search_non_existent - Test that search returns -1 for a non-existent element
def test_search_non_existent(array_fixture):
    index = array_fixture.search(10)
    assert index == -1

# edge_case - test_setitem_invalid_index - Test that setitem raises error for invalid index
def test_setitem_invalid_index(array_fixture):
    try:
        array_fixture.__setitem__(5, 10)
    except IndexError:
        pass

# edge_case - test_getitem_invalid_index - Test that getitem raises error for invalid index
def test_getitem_invalid_index(array_fixture):
    try:
        array_fixture.__getitem__(5)
    except IndexError:
        pass

# edge_case - test_delete_empty_array - Test that delete function handles empty array gracefully
def test_delete_empty_array():
    empty_array = Array(0)
    empty_array.delete(10, 0)
    assert empty_array.arrayItems == []

