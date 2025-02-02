import os

# Current folder name with hyphens
old_folder_name = "src/Chicken-Disease--classification-project"
# New folder name with underscores
new_folder_name = "src/chicken_disease_classification_project"

# Renaming the folder
os.rename(old_folder_name, new_folder_name)

print(f"Folder renamed from '{old_folder_name}' to '{new_folder_name}' successfully.")
