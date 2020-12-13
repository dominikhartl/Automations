import os
import shutil
import yaml
import time
from watchdog.observers.fsevents import FSEventsObserver as Observer
from watchdog.events import FileSystemEventHandler

path = '/Users/hartdomi/Downloads/'
yml = '/Users/hartdomi/Code/Automations/DownloadAssignment.yml'

with open(yml) as file:
    assignment = yaml.load(file, Loader=yaml.FullLoader)

class movehandler(FileSystemEventHandler):
    def on_modified(self,event):
        print(event)
        list_ = os.listdir(path)
        #Traverses every file
        for file_ in list_:
            name,ext = os.path.splitext(file_)
            #Stores the extension type
            ext = ext[1:]
            while ext == "download":
                time.sleep(1)
                for file_ in list_:
                    name,ext = os.path.splitext(file_)
                    ext = ext[1:]
            
            #If it is directory, it forces the next iteration
            if ext in assignment.keys():
                shutil.move(path+'/'+file_,assignment[ext]+file_)
            else:
                pass

if __name__ == "__main__":
    try:
        event_handler = movehandler()
        observer = Observer()
        observer.schedule(event_handler,path,recursive=True)
        observer.start()
    except:
        print(Exception)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
