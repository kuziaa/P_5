import os

def my_wrapper(path_generator):
    for dir in path_generator:
        for file in dir[2]:
            yield dir[0] + "\\" + file


x = my_wrapper(os.walk("f:\\Task_0"))

for _ in x:
    print(_)