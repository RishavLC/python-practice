import time

questions = [
    {"q": "What is the capital of Nepal?", "options": ["Kathmandu", "Pokhara", "Lalitpur"], "answer": "Kathmandu"},
    {"q": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": "4"}
]

score = 0
start = time.time()

for i, q in enumerate(questions):
    print(f"\nQ{i+1}: {q['q']}")
    for opt in q['options']:
        print("-", opt)
    ans = input("Your answer: ")

    if ans.strip().lower() == q['answer'].lower():
        score += 1

end = time.time()
print(f"\n✅ You got {score}/{len(questions)} in {round(end - start, 2)} seconds.")
