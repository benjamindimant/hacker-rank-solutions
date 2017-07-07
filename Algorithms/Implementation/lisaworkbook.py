n, k = map(int, input().strip().split(' '))
t = list(map(int, input().strip().split(' ')))

count = 0
page = 1
for chapter_problem in t:
    for current_problem in range(1, chapter_problem + 1):
        if(page == current_problem):
            count = count + 1
        if ((current_problem % k == 0) or current_problem == chapter_problem):
            page = page + 1
        
print(count)
