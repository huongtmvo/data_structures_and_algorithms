class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in a dictionary
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            if query.ind in self.elems:
                # use reversed order, because we append the last strings to the end
                # self.write_chain(cur for cur in reversed(self.elems[query.ind]))
                self.write_chain(cur for cur in self.elems[query.ind][::-1])
            else:
                print(' ')
        else:
            idx = self._hash_func(query.s)

            if query.type == 'find':
                self.write_search_result(idx in self.elems and query.s in self.elems[idx])
            elif query.type == 'add':
                if idx not in self.elems:
                    self.elems[idx] = [query.s]
                else:
                    if query.s not in self.elems[idx]:
                        self.elems[idx].append(query.s)
            else:
                if idx in self.elems and query.s in self.elems[idx]:
                    self.elems[idx].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
