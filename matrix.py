import threading

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]

def compute(i, j):
    result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

threads = []
for i in range(2):
    for j in range(2):
        t = threading.Thread(target=compute, args=(i, j))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

print("Result:", result)
