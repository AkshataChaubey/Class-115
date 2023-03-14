import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/chaub/Downloads"
to_dir="C:/Users/chaub/OneDrive/Desktop/Document_Files"
dir_tree = { "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], 
            "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
             "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], 
             "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg','.webp'] }
class files(FileSystemEventHandler):
    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for i,j in dir_tree.items():
            time.sleep(1)
            if extension in j:
                file_name=os.path.basename(event.src_path)
                print("File is Downloaded")
                path1=from_dir+'/'+file_name
                path2=to_dir+'/'+i
                path3=to_dir+'/'+i+'/'+file_name
                if os.path.exists(path2):
                    print("Directory exists")
                    print("Moving "+file_name)
                    shutil.move(path1,path3)
                    time.sleep(2)
                else:
                    print("Creating a Directory")
                    os.makedirs(path2)
                    print("Moving "+file_name)
                    shutil.move(path1,path3)
                    time.sleep(1)
moving=files()
myobserver=Observer()
myobserver.schedule(moving,from_dir,recursive=True)     
myobserver.start()               
try:
    while True:
        time.sleep(2)
        print("Running")



except KeyboardInterrupt:
    print("Stopped")
    myobserver.stop()    
