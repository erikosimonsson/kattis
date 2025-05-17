from collections import Counter
i = input().split()
words = int(i[0])
jobs = int(i[1])
job = {}
for _ in range(words):
    word, value = input().split()
    job[word] = int(value)
for _ in range(jobs):
    job_t = []
    line = input()
    while line != '.':
        job_t.extend(line.split())
        line = input()
    word_c = Counter(job_t)
    salary = sum(job[word] * count 
            for word, count in word_c.items() 
            if word in job)
    print(salary)
