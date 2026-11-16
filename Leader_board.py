# School gaming leaderboard
# Inputs
names = ["Abdo", "Adham", "Ali", "Bassem", "Gasser", "Omar", "Youssef"]
scores = [90, 95, 100, 70, 60, 65, 80]

# Decsending arrangement
for i in range(len(scores)) :
    for j in range(i + 1, len(scores)) :
        if scores[j] > scores[i] :
            scores[i], scores[j] = scores[j], scores[i]
            names[i], names[j] = names[j], names[i]

# Leaderboard
print("=== Leaderboard ===\n")

for i in range(len(names)) :
    print(i+1, "-", names[i], " : ", scores[i])

# Identifying first and last players
print("\n\n", names[0], " took the first place with score : ", scores[0])
print(names[-1], " took the last place with score : ", scores[-1])

# Final message
print("\n\n\n=== Summary ===\n")
print("The total number of players was : ", len(names))
