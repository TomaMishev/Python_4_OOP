# You are provided with a class IntegerList. It should only store integers. The initial integers should be set by the
# constructor. They are stored as a list. IntegerList has a functionality to add, remove_index, get, insert,
# get the biggest number, and get the index of an element. Your task is to test the class. Note: You are not allowed
# to change the structure of the provided code Constraints •	add operation, should add an element and returns the
# list. o	If the element is not an integer, a ValueError is thrown •	remove_index operation removes the element on
# that index and returns it. o	If the index is out of range, an IndexError is thrown •	__init__ should only take
# integers, and store them •	get should return the specific element o	If the index is out of range,
# an IndexError is thrown •	insert o	If the index is out of range, IndexError is thrown o	If the element is not
# an integer, ValueError is thrown •	get_biggest •	get_index Hint Do not forget to test the constructor


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):
    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_type_date(self):
        integer = IntegerList("asd", 5.6, 10.2)
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_int_data(self):
        integer = IntegerList(5, "asd")
        self.assertEqual([5], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5, "asd")
        self.assertEqual([5], integer._IntegerList__data)

        result = integer.get_data()

        self.assertEqual([5], result)

    def test_add_method_incorrect_data_raises(self):

        integer = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            integer.add("asd")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_correct_data_adds_element(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

        integer.add(10)

        self.assertEqual([5, 10], integer._IntegerList__data)

    def test_remove_el_removes_the_element(self):
        integer = IntegerList(5)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)

    def test_remove_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_returns_el_at_removed_index(self):
        integer = IntegerList(5)
        result = integer.remove_index(0)

        self.assertEqual(5, result)

    def test_get_with_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_with_equal_length_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.get(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_return_the_correct_element(self):
        integer = IntegerList(5)

        result = integer.get(0)

        self.assertEqual(5, result)

    def test_insert_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_invalid_element_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, "asd")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_inset_adds_element(self):
        integer = IntegerList(5)

        integer.insert(0, 6)

        self.assertEqual([6, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5, -2, 100, 0, 50, 101)
        result = integer.get_biggest()
        self.assertEqual(101, result)

    def test_get_index(self):
        integer = IntegerList(5, -2, 100, 0, 50, 101)
        result = integer.get_index(-2)
        self.assertEqual(1, result)



if __name__ == "__main__":
    main()
