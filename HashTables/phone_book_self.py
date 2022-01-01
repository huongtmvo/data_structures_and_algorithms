class PhoneBook:
    def __init__(self):
        self.book = [None] * 10000000

    def add(self, number, name):
        self.book[number] = name

    def delete(self, number):
        if self.book[number] is not None:
            self.book[number] = None

    def find(self, number):
        if self.book[number] is None:
            return "not found"
        return self.book[number]


def process_queries(queries):
    for query in queries:
        q = query.split()
        cmd = q[0]
        number = int(q[1])
        if cmd == "add":
            phonebook.add(number, q[2])
        elif cmd == "find":
            print(phonebook.find(number))
        elif cmd == "del":
            phonebook.delete(number)


if __name__ == "__main__":
    phonebook = PhoneBook()

    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)