import sys
sys.path.insert(0, './db/')

from user import User

a = User(["Abhishek", "17BCS1612", "LOL"])

print(a)
print(a.user)