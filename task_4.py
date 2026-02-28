new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop()) # new_tasks = ['task_001', 'task_011', 'task_007', 'task_015']  completed_tasks = ['task_002', 'task_012', 'task_006', 'task_005']

new_tasks.remove('task_007') # new_tasks = ['task_001', 'task_011', 'task_015']

print(new_tasks[2])  
#print(new_tasks[len(new_tasks)-1])
#print(new_tasks[-1])

