import os 
import shutil
import time
start = time.perf_counter()
# folder we'll be organizeing
folder = "messy_folder"
os.makedirs(folder, exist_ok=True)
# create some dummy files 
dummy_files = ["photos.zip", "document.docx", "presentation.pptx", "notes.txt", "archive.tar.gz"]
for filename in dummy_files:
    with open(os.path.join(folder, filename), "w") as f:
        f.write("This is a dummy file.")
# now i am going to define its categories
categories = {
    "Documents": [".docx", ".txt", ".pptx"],
    "Archives": [".zip", ".tar.gz"]
}
# adding a loop through the files in the folder
for filename in os.listdir(folder):  # ← loop goes HERE!
    if filename.endswith(".tar.gz"):
        ext = ".tar.gz"
    else:
        ext = os.path.splitext(filename)[1]
    # Now i am going to move files into subfolders 
    for category, extensions in categories.items():
        if ext in extensions:
            category_folder = os.path.join(folder, category)
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(os.path.join(folder, filename), os.path.join(category_folder, filename))
            print(f"Moved {filename} to {category_folder}")
            break
end = time.perf_counter()
print(f"Organized files in {end - start:.6f} seconds.")
        