import os             
import shutil         
import subprocess     
import platform       
from datetime import datetime 


path = os.path.expanduser("~/Downloads")

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python": [".py"]
}

print("Сортировка")


for file in os.listdir(path):
    file_path = os.path.join(path, file)
    
    if os.path.isdir(file_path): 
        continue
        
    ext = os.path.splitext(file)[1].lower()

    for folder, extensions in folders.items():
        if ext in extensions:
            date_folder = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m')
            
            target_dir = os.path.join(path, folder, date_folder)
            
            os.makedirs(target_dir, exist_ok=True)
            
            shutil.move(file_path, os.path.join(target_dir, file))
            print(f"Перемещено: {file}")


if platform.system() == "Windows":
   os.startfile(path)
elif platform.system() == "Darwin": # macOS
    subprocess.Popen(["open", path])
else: # Linux
    subprocess.Popen(["xdg-open", path])





