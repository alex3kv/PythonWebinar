from itertools import count

END = 15


def generate(start):
    for el in count(start):
        if el > END:
            break
        print(el)


if __name__ == "__main__":
    generate(2)
