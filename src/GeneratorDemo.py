from collections import Iterator

# 迭代函数的好处就是不需要分配大量的内存来存储集合，所以集合数量量大的话，建议使用迭代的方式。
def generator_function():
    for x in range(0, 10):
        yield x


print type(range(0, 10))

print type(xrange(0, 10))

assert isinstance(generator_function(), Iterator)

if __name__ == '__main__':
    for i in generator_function():
        print i
