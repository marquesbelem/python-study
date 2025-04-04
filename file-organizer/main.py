import os 
import shutil
from datetime import datetime

origin_folder = "D:\TesteOrganizador"

target_folder = {
    "DocumentsPy": [".pdf", ".docx", ".txt", ".doc", ".pptx", ".ppt"],
    "ImagesPy": [".jpg", ".jpeg", ".png", ".gif"],
    "ArchivesPy": [".zip", ".rar", ".tar", ".gz", ".exe"],
    "AudioPy": [".mp3", ".wav", ".flac"],
}

for folder in target_folder:
    folder_path = os.path.join(origin_folder, folder)
    os.makedirs(folder_path, exist_ok=True)
    
for file in os.listdir(origin_folder):
    path_file = os.path.join(origin_folder, file)
    
    if os.path.isfile(path_file):
        extension = os.path.splitext(file)[1].lower()

        for folder in target_folder.keys():
            extensions = target_folder[folder]
            if extension in extensions:
                new_folder = os.path.join(origin_folder, folder)
                shutil.move(path_file, new_folder)

                log_path = os.path.join(origin_folder, "log.txt")
                with open(log_path, "a") as log:
                    log.write(f"{datetime.now()} - {file} -> {folder}\n")
                
                break
