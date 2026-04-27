
def reflection_tree(mood, energy, goal):
    mood = mood.lower()
    energy = energy.lower()
    goal = goal.lower()

    if mood == "sad" and energy == "low":
        return "Write 3 things you are grateful for."

    elif mood == "stressed" and energy == "high":
        return "Go for a walk and do breathing exercises."

    elif mood == "happy":
        return "Write today's achievements."

    elif goal == "self-growth":
        return "Read a book or learn something new."

    elif goal == "relaxation":
        return "Listen to music or meditate."

    else:
        return "Take rest and reflect calmly."


# User Input
mood = input("Enter Mood (Happy/Sad/Stressed): ")
energy = input("Enter Energy (High/Low): ")
goal = input("Enter Goal (Productivity/Relaxation/Self-growth): ")

# Output
result = reflection_tree(mood, energy, goal)
print("\nSuggestion:", result)
