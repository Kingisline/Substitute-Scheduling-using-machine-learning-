import random

# Sample data
teachers = {
    "Teacher A": {"subject": "Math", "availability": True},
    "Teacher B": {"subject": "Science", "availability": False},
    "Teacher C": {"subject": "Math", "availability": True},
    "Teacher D": {"subject": "History", "availability": True}
}

# Function to assign substitute teacher
def assign_substitute(subject):
    available_teachers = [teacher for teacher, info in teachers.items() if info["subject"] == subject and info["availability"]]
    if available_teachers:
        return random.choice(available_teachers)
    else:
        return None

# Example usage
subject = "Math"
substitute = assign_substitute(subject)
if substitute:
    print(f"Substitute assigned: {substitute}")
else:
    print("No substitute available.")
