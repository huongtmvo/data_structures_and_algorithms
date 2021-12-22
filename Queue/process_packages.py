# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.started_at = 0
        self.queue = deque([])

    def process(self, req):
        if len(self.queue) == 0 :
            self.queue.append(req.arrived_at + req.time_to_process)
            return Response(False, req.arrived_at)

        if len(self.queue) < self.size:
            # calculate started_at 
            started_at = max(req.arrived_at, self.queue[-1])
            self.queue.append(started_at + req.time_to_process)
            return Response(False, started_at)

        if self.queue[0] <= req.arrived_at:
            started_at = max(req.arrived_at, self.queue[-1])
            self.queue.popleft()
            self.queue.append(started_at + req.time_to_process)
            return Response(False, started_at)
        else:
            return Response(True, -1)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
