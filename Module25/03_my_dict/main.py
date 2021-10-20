class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


my_dict = MyDict()
print(my_dict)
my_dict[1] = 'a'
my_dict[2] = 'б'
my_dict[3] = 'в'
print(my_dict)
print(my_dict.get(3))
print(my_dict.get(4))
