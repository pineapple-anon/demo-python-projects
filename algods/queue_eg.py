from collections import deque

def execute(program: list[str]) -> deque[int]:
    # initialize a deque representing a queue
    queue: deque[int] = deque()
    for instruction in program:
        if instruction == "peek":
            # print out the first item in queue if it is not empty
            # print warning message if queue is empty
            print(queue[0]) if queue else print("Queue is empty!")
        elif instruction == "pop":
            # check if queue is empty
            if queue:
                # pop the first item in queue
                queue.popleft()
            else:
                # print message if queue is empty
                print("Queue is empty!")
        else:
            # get the data in the "push" instruction
            data = int(instruction[5:])
            # push data to the end of queue
            queue.append(data)
    return queue

if __name__ == "__main__":
    program = [input() for _ in range(int(input()))]
    res = execute(program)
    print(" ".join(map(str, res)))