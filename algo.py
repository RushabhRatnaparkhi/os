def fcfs(processes):
    print("\nFCFS:")
    wait = 0
    for p in processes:
        print(f"Process {p[0]} waited {wait}")
        wait += p[1]

def sjf(processes):
    print("\nSJF:")
    processes.sort(key=lambda x: x[1])
    fcfs(processes)

def priority_sched(processes):
    print("\nPriority Scheduling:")
    processes.sort(key=lambda x: x[2])
    fcfs(processes)

# Format: [PID, Burst, Priority]
procs = [['P1', 4, 2], ['P2', 2, 1], ['P3', 5, 3]]
fcfs(procs)
sjf(procs.copy())
priority_sched(procs.copy())
