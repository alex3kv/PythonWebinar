from itertools import cycle

END = 15

def generate(value):
    i = 0
    for el in cycle(value):
        if i > END:
            break
        print(el)
        i += 1


if __name__ == "__main__":
    generate(["1", 2, True])
