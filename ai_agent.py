
def ai_agent(user_input):
    if "sad" in user_input:
        return "It seems you're feeling sad. Try journaling your thoughts."
    elif "stress" in user_input:
        return "Take a deep breath and list your top 3 concerns."
    else:
        return "Reflect on your day and write key learnings."
