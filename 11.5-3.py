import sys
import math

RADIUS = 0.5

def read_data():
    data = int(sys.stdin.read().strip())
    return data

def get_sequence(n: int,first_node :float):
    seq = [0.0,first_node]
    distance = RADIUS * RADIUS
    for i in range(1,n):
        sk = seq[i]
        sk_1 = seq[i-1]
        if sk_1 > RADIUS or sk > RADIUS:
            return None
        fsk_1 = math.sqrt(distance - sk_1 * sk_1)
        fsk = math.sqrt(distance - sk * sk)
        next = sk + (fsk_1 - fsk)* fsk /sk
        seq.append(next)
    return seq

def search_first(n:int):
    low = 1e-15
    high = RADIUS - 1e-15
    bestdiff = float('inf')
    best_sequence : list[float]
    for i in range(200):
        mid = (low + high) / 2
        sequence = get_sequence(n,mid)
        if sequence is None:
            high = mid
            continue
        current_diff =abs(sequence[-1] - RADIUS)
        if current_diff < bestdiff:
            bestdiff = current_diff
            best_sequence = sequence
        if sequence[-1] < RADIUS:
            low = mid
        elif sequence[-1] > RADIUS:
            high = mid
        else:
            return best_sequence
    best_sequence[-1] = RADIUS
    return best_sequence

def compute_area(m: int):
    n = (m+1)//2
    distance = RADIUS * RADIUS
    sequence = search_first(n)
    area =0.0
    for i in range(1,n+1):
        height = sequence[i] - sequence[i-1]
        width = math.sqrt(distance - sequence[i-1] * sequence[i-1])
        area += height * width
    return area * 4.0

data = read_data()
area = compute_area(data)
print(round(area,4))
