# queue_time([10,2,3,3], 2)
# next time finished.
# t = 0
# [None, None]
# [10, None]
# [10, 2]
# should always add to queue? I think so
# t = 2
# [10, 5]
# t = 5
# [10] find min

def next_till(tills):
    for i in range(len(tills)):
        if tills[i] == float("inf"):
            return i
    return -1

def add_to_queue(curr_t, tills, queue):
    while True:
        if len(queue) == 0:
            return False
        n = next_till(tills)
        if n == -1:
            return True
        tills[n] = curr_t + queue[0]
        queue.pop(0)

def clear_tills(curr_t, tills):
    for i in range(len(tills)):
        if tills[i] == curr_t:
            tills[i] = float("inf")
    

def test(queue):
    queue.pop(0)

def main(num_tills, queue):
    tills = [float("inf")] * num_tills
    curr_t = 0
    while True:
        # print("tills before add to queue:", tills)
        # print("queue before add to queue:", queue)
        result = add_to_queue(curr_t, tills, queue)
        # print("tills after add to queue:", tills)
        # print("queue after add to queue:", queue)
        t = min(tills)
        # print("min t:", t)
        if t == float("inf"):
            return curr_t
        curr_t = t
        # print("tills before clear tills:", tills)
        clear_tills(curr_t, tills)
        # print("tills after clear tills:", tills)

n = 4
# ts1 = [float("inf")] * 4
q1 = list(range(1, 2*n+1))
q2 = [1,2,3,4,5]
q3 = [2,2,3,3,4,4]
# add_to_queue(10, ts1, q1)
print(main(2, q2))
# print(ts1)
# print(q1)
# print(q1)
# test(q1)
# print(q1)
