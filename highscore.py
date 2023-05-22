
high_scores = []

def add(name, total):
    global high_scores
    high_scores.append((name, total))
    high_scores.sort(key=lambda x: x[1])
    print("High Scores:")
    for i, (name, total) in enumerate(high_scores):
        print(f"{i+1}. {name}: {total} seconds")
