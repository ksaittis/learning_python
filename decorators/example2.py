from functools import wraps
from unittest import TestCase


def list_helper(function):
    @wraps(function)
    def inner(values):
        """This is the inner function"""
        if isinstance(values, list):
            return [function(value) for value in values]
        else:
            return function(values)

    return inner


@list_helper
def convert_to_camelcase(s) -> str:
    """This function convert a snakecase to camelcase"""
    return ''.join([s.capitalize() for s in s.split('_')])


if __name__ == '__main__':
    values_list = ['hello_world', 'foo_bar']
    print(convert_to_camelcase('hello_world'))
    print(convert_to_camelcase.__doc__)


class MinorTest(TestCase):

    def test_it_should_be_able_to_handle_both_strings_and_lists(self):
        values_list = ['hello_world', 'foo_bar']
        print('damn')
        self.assertEquals(convert_to_camelcase('hello_world'), 'HelloWor ld')
        self.assertEquals(list_helper(convert_to_camelcase)(values_list), convert_to_camelcase(values_list))
