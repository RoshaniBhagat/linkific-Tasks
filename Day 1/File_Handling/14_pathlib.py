from pathlib import Path

# Current folder

current = Path.cwd()

print("Current Folder:")
print(current)

# Create folder

new_folder = current / "Reports"

new_folder.mkdir(exist_ok=True)

print("\nFolder Created:", new_folder)

# List files

print("\nFiles in Current Folder:")

for file in current.iterdir():
    print(file)