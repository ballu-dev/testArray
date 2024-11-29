import pytest
from unittest import mock
from Arrays import Array

@pytest.fixture
def array_fixture():
    with mock.patch('Arrays.Array.__init__', return_value=None) as mock_init:
        with mock.patch('Arrays.Array.__str__', return_value='0 0 0 0 0') as mock_str:
            with mock.patch('Arrays.Array.__len__', return_value=5) as mock_len:
                with mock.patch('Arrays.Array.__getitem__', side_effect=lambda index: 0 if index < 5 else mock.DEFAULT) as mock_getitem:
                    with mock.patch('Arrays.Array.__setitem__', return_value=None) as mock_setitem:
                        with mock.patch('Arrays.Array.search', side_effect=lambda key: -1 if key == 99 else 2) as mock_search:
                            with mock.patch('Arrays.Array.insert', return_value=None) as mock_insert:
                                with mock.patch('Arrays.Array.delete', return_value=None) as mock_delete:
                                    yield {
                                        'mock_init': mock_init,
                                        'mock_str': mock_str,
                                        'mock_len': mock_len,
                                        'mock_getitem': mock_getitem,
                                        'mock_setitem': mock_setitem,
                                        'mock_search': mock_search,
                                        'mock_insert': mock_insert,
                                        'mock_delete': mock_delete,
                                        'array_instance': Array(5, int)
                                    }

# happy_path - test_init_int_array - Test that Array initializes with zeroes for int type
def test_init_int_array(array_fixture):
    array_instance = array_fixture['array_instance']
    array_fixture['mock_init'].assert_called_once_with(5, int)
    assert array_instance.arrayItems == [0, 0, 0, 0, 0]

# happy_path - test_init_float_array - Test that Array initializes with zeroes for float type
def test_init_float_array(array_fixture):
    with mock.patch('Arrays.Array.__init__', return_value=None) as mock_init:
        array_instance = Array(3, float)
        mock_init.assert_called_once_with(3, float)
        assert array_instance.arrayItems == [0.0, 0.0, 0.0]

# happy_path - test_str_representation - Test that __str__ returns correct string representation
def test_str_representation(array_fixture):
    array_instance = array_fixture['array_instance']
    assert str(array_instance) == '0 0 0'

# happy_path - test_len_function - Test that __len__ returns correct length of array
def test_len_function(array_fixture):
    array_instance = array_fixture['array_instance']
    assert len(array_instance) == 5

# happy_path - test_search_existing_element - Test that search finds existing element
def test_search_existing_element(array_fixture):
    array_instance = array_fixture['array_instance']
    assert array_instance.search(2) == 2

# happy_path - test_insert_element - Test that insert adds element at correct position
def test_insert_element(array_fixture):
    array_instance = array_fixture['array_instance']
    array_instance.insert(10, 3)
    array_fixture['mock_insert'].assert_called_once_with(10, 3)
    assert array_instance.arrayItems == [0, 0, 0, 10, 0]

# edge_case - test_search_non_existing_element - Test that search returns -1 for non-existing element
def test_search_non_existing_element(array_fixture):
    array_instance = array_fixture['array_instance']
    assert array_instance.search(99) == -1

# edge_case - test_insert_out_of_bounds - Test that insert handles out of bounds position
def test_insert_out_of_bounds(array_fixture, capsys):
    array_instance = array_fixture['array_instance']
    array_instance.insert(10, 10)
    captured = capsys.readouterr()
    assert captured.out == 'Array size is: 5\n'

# edge_case - test_delete_out_of_bounds - Test that delete handles out of bounds position
def test_delete_out_of_bounds(array_fixture, capsys):
    array_instance = array_fixture['array_instance']
    array_instance.delete(10, 10)
    captured = capsys.readouterr()
    assert captured.out == 'Array size is: 5\n'

# edge_case - test_getitem_negative_index - Test that __getitem__ raises IndexError for negative index
def test_getitem_negative_index(array_fixture):
    array_instance = array_fixture['array_instance']
    with pytest.raises(IndexError):
        _ = array_instance[-1]

# edge_case - test_setitem_negative_index - Test that __setitem__ raises IndexError for negative index
def test_setitem_negative_index(array_fixture):
    array_instance = array_fixture['array_instance']
    with pytest.raises(IndexError):
        array_instance[-1] = 10

