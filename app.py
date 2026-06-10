from pathlib import Path

file_path = "sample_document.txt"

with open(file_path, "r") as f:
    text = f.read()

print("Document Loaded")
print("----------------")
print(text)

if "$2500" in text:
    print("\nValidation Passed")
else:
    print("\nValidation Failed")
