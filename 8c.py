import os
# 1. List directories and files
print("Files and Directories:")
print(os.listdir())
# 2. Create a new directory
os.mkdir("ProjectFolder")
print("New directory created successfully.")
# 3. Rename a directory
os.rename("ProjectFolder", "MicrosoftProject")
print("Directory renamed successfully.")
# 4. Create a new file
with open("project.txt", "w") as f:
    f.write("Microsoft Project Files")
# 5. Rename a file
os.rename("project.txt", "project_details.txt")
print("File renamed successfully.")
# 6. Remove a file
os.remove("project_details.txt")
print("File removed successfully.")
# 7. Remove a directory
os.rmdir("MicrosoftProject")
print("Directory removed successfully.")
