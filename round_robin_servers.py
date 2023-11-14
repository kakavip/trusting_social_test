# Python code for the above approach
import heapq
import random


def get_server_index(n, arrival, burst_time):
    busy_servers = []
    avai_servers = list(range(1, n + 1))

    heapq.heapify(busy_servers)
    heapq.heapify(avai_servers)

    arrival_map = {}
    for i in range(len(arrival)):
        if arrival[i] not in arrival_map:
            arrival_map[arrival[i]] = []

        arrival_map[arrival[i]].append(i)

    n_arrival = list(set(arrival))
    sorted(arrival)

    busy_servers_map = {}

    result = [0] * len(arrival)
    for i in range(len(n_arrival)):
        c_time = n_arrival[i]

        while busy_servers and busy_servers[0] <= c_time:
            b = heapq.heappop(busy_servers)

            for server_idx in busy_servers_map[b]:
                heapq.heappush(avai_servers, server_idx)
            busy_servers_map[b] = []

        for j in range(len(arrival_map[c_time])):
            if len(avai_servers):
                server_idx = heapq.heappop(avai_servers)
                result[arrival_map[c_time][j]] = server_idx

                next_time = (
                    arrival[arrival_map[c_time][j]] + burst_time[arrival_map[c_time][j]]
                )
                if next_time not in busy_servers_map:
                    busy_servers_map[next_time] = []

                if not busy_servers_map[next_time]:
                    heapq.heappush(busy_servers, next_time)

                busy_servers_map[next_time].append(server_idx)
            else:
                result[arrival_map[c_time][j]] = -1

    return result


if __name__ == "__main__":
    # Given arrivalTime and processTime
    arrival_time = [random.randrange(1, 1_000_000) for _ in range(100_000)]
    process_time = [random.randrange(1, 1_000_000) for _ in range(100_000)]
    n = 20_000

    # print(arrival_time)
    # print(process_time)

    # # Function Call
    print(get_server_index(n, arrival_time, process_time))

# This code is contributed by sdeadityasharma
