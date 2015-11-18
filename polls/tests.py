from django.test import TestCase


# Create your tests here.
def t():
    print(1 >= 2 - 1)
    return 1 >= 2 - 1

r = t()

print(r)
