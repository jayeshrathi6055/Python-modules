import collections

# # Use of chainmap-------------------------------------------------->

# a = {'a':'A','c':'C'}
# b = {'b':'B','d':'D'}

# m = collections.ChainMap(a,b)
# print('Individual Values')
# print('a = {}'.format(m['a']))
# print('b = {}'.format(m['b']))
# print('c = {}'.format(m['c']))
# print()

# print('Keys = {}'.format(list(m.keys())))
# print('Values = {}'.format(list(m.values())))
# print()

# print('Items:')
# for k, v in m.items():
#     print('{} = {}'.format(k, v))
# print()

# print('"d" in m: {}'.format(('d' in m)))

# print(m.maps)

# m.maps = list(reversed(m.maps))
# print(m.maps)

# m2 = m.new_child()
# print('m before:', m)
# print('m2 before:', m2)
# m2['c'] = 'E'
# print('m after:', m)
# print('m2 after:', m2)
# print()

# c = {'c':'E'}
# m2 = m.new_child(c)
# print('m["c"] = {}'.format(m['c']))
# print('m2["c"] = {}'.format(m2['c']))
# print()

# # Use of Counter----------------------------------------------------->

# print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
# print(collections.Counter({'a': 0, 'b': 3, 'c': 1}))
# print(collections.Counter(a=2, b=3, c=1))

# c = collections.Counter()
# print('Initial :', c)
# print()

# c.update('abcdaab')
# print('Sequence:', c)
# print()

# c.update({'a': 1, 'd': 5})
# print('Dict :', c)
# print()

# c = collections.Counter('abcdaab')
# for letter in 'abcde':
#     print('{} : {}'.format(letter, c[letter]))
# print()

# c = collections.Counter('extremely')
# c['z'] = 0
# print(c)
# print(list(c.elements()))
# print()

# print('Most common:')
# for letter, count in c.most_common(3):
#     print('{}: {:>7}'.format(letter, count))
# print()

# c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
# c2 = collections.Counter('alphabet')
# print('C1:', c1)
# print('C2:', c2)
# print('\nCombined counts:')
# print(c1 + c2)
# print('\nSubtraction:')
# print(c1 - c2)
# print('\nIntersection (taking positive minimums):')
# print(c1 & c2)
# print('\nUnion (taking maximums):')
# print(c1 | c2)

# # Use of defaultdict-------------------------------------------------->
# def default_factory():
#     return 'default value'

# d = collections.defaultdict(default_factory, foo='bar')
# print('d:', d)
# print('foo =>', d['foo'])
# print('bar =>', d['bar'])

# # Use of deque------------------------------------------------------------->

# d = collections.deque('abcdefg')
# print('Deque:', d)
# print('Length:', len(d))
# print('Left end:', d[0])
# print('Right end:', d[-1])
# d.remove('c')
# print('remove(c):', d)
# print()

# # Add to the right.
# d1 = collections.deque()
# d1.extend('abcdefg')
# print('extend :', d1)
# d1.append('h')
# print('append :', d1)
# print()

# # Add to the left.
# d2 = collections.deque()
# d2.extendleft(range(6))
# print('extendleft:', d2)
# d2.appendleft(6)
# print('appendleft:', d2)
# print()

# print('From the right:')
# d = collections.deque('abcdefg')
# while True:
#     try:
#         print(d.pop(), end='')
#     except IndexError:
#         break
# print()
# print('\nFrom the left:')
# d = collections.deque(range(6))
# while True:
#     try:
#         print(d.popleft(), end='')
#     except IndexError:
#         break
# print()

# # Use of Rotate
# d = collections.deque(range(10))
# print('Normal :', d)
# print()

# d = collections.deque(range(10))
# d.rotate(3)
# print('Right rotation:', d)
# print()

# d.rotate(-3)
# print('Left rotation :', d)
# print()

# # Use of namedtuple-------------------------------------------------------->

# Person = collections.namedtuple('Person', 'name age',)
# bob = Person(name='Bob', age=30)
# print('\nRepresentation:', bob)

# jane = Person(name='Jane', age=29)
# print('\nField by name:', jane.name)
# print()

# print('\nFields by index:')
# for p in [bob, jane]:
#     print('{} is {} years old'.format(*p))
# print()

# # use of _fields 

# Person = collections.namedtuple('Person', 'name age')
# bob = Person(name='Bob', age=30)
# print('Representation:', bob)
# print()
# print('Fields:', bob._fields)
# print()

# # use of _replace

# Person = collections.namedtuple('Person', 'name age')
# bob = Person(name='Bob', age=30)
# print('\nBefore:', bob)
# print()
# bob2 = bob._replace(name='Robert')
# print('After:', bob2)
# print()
# print('Same?:', bob is bob2)
# print()

# # Use of Ordereddict------------------------------------------------------>

# print('\nOrderedDict:')
# d = collections.OrderedDict()
# d['a'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'
# for k, v in d.items():
#     print(k, v)
# print()

# # equality
# print('OrderedDict:', end=' ')
# d1 = collections.OrderedDict()
# d1['a'] = 'A'
# d1['b'] = 'B'
# d1['c'] = 'C'
# d2 = collections.OrderedDict()
# d2['c'] = 'C'
# d2['b'] = 'B'
# d2['a'] = 'A'
# print(d1 == d2)
# print()

# # Reorder (use of move_to_end)
# d = collections.OrderedDict(
# [('a', 'A'), ('b', 'B'), ('c', 'C')]
# )
# print('Before:')
# for k, v in d.items():
#     print(k, v)

# d.move_to_end('b')
# print('\nmove_to_end():')
# for k, v in d.items():
#     print(k, v)

# d.move_to_end('b', last=False)
# print('\nmove_to_end(last=False):')
# for k, v in d.items():
#     print(k, v)
