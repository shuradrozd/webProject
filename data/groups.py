# import random
# import string

from models.group import Group

testdata = [Group(name="name1"),
                Group(name="name2")
                ]

# def random_string(prefix, maxLen):
#     symbols = string.ascii_letters + string.digits + " " * 2
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxLen))])
#
#
# test_data = [Group(name="")] + [Group(name=random_string("name", 10))
#                                 for i in range(5)
#                                 ]
