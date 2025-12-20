def replace_python_with_ai(text: str) -> str:
    return text.replace("Python", "AI")


text = input()
out = replace_python_with_ai(text)
print(out)