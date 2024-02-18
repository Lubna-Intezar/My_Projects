def greet_user():
    """Greets the user by name."""
    name = input("Hi there! What's your name? ")
    print(f"Hi {name}, welcome to UniBuddy! I'm here to help you navigate your university journey.")

def collect_info():
    """Collects personal information from the user."""
    favorite_color = input("What's your favorite color? ")
    age = input("How old are you? (Optional) ")
    return favorite_color, age

def answer_questions():
    """Answers predetermined questions from the user."""
    questions = {
        "What are some resources for new students?": "There are many resources available to help you succeed at university. You can visit the student orientation website, talk to your advisors, or join student clubs and organizations.",
        "Where can I find information about my courses?": "You can find information about your courses on the university website or in the course syllabus. You can also talk to your professors or teaching assistants.",
        "How do I make friends at university?": "There are many ways to make friends at university. You can join clubs and organizations, attend social events, or simply talk to people in your classes or residence hall.",
        "What should I do if I'm feeling overwhelmed?": "It's normal to feel overwhelmed during your first semester at university. There are many resources available to help you, such as counseling services, academic support services, and peer mentoring programs."
    }

    while True:
        user_question = input("Ask me anything or type 'quit' to exit: ")
        if user_question.lower() == "quit":
            break
        elif user_question in questions:
            print(questions[user_question])
        else:
            print("I'm still learning, but I don't have an answer for that yet. Perhaps you can ask a human counselor or advisor.")

if __name__ == "__main__":
    greet_user()
    favorite_color, age = collect_info()
    print(f"That's a cool color, {favorite_color}! (Optional: You're {age} years old, is that right?)")
    answer_questions()