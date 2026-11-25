"""The Funniest Sick-Day Excuse — entry for make.fun.

Writes one line to /output/entry.txt. The line is the funniest sick-day excuse, under 200 characters.
"""
import os

LINE = "Sorry, I cannot come in today — my bed has filed a formal complaint against my alarm clock, and HR says I have to side with the bed."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
