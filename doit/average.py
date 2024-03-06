n = int(input())
l = list(map(int, input().split()))

max_score = max(l)

new_scores = []
for i in l:
    new_scores.append(i / max_score * 100)

cnt = len(new_scores)

print(sum(new_scores) / cnt)
