my_dict = {
    'tuple': (1, 'hello', True, 3.14, [1, 2]),
    'list': ['apple', 'banana', 'orange', 'grape', 'mango'],
    'dict': {
        'name': 'John',
        'age': 25,
        'city': 'New York',
        'job': 'developer',
        'hobby': 'reading'
    },
    'set': {1, 'python', ('a', 'b'), 3.14, 'programming'}
}
print("Last element for a 'tuple' key:", my_dict['tuple'][-1])

my_dict['list'].append('pear')
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'tuple key value'
del my_dict['dict']['age']

my_dict['set'].add('new element')
my_dict['set'].remove(1)

print("\nFinal Dictionary:")
print(my_dict)
