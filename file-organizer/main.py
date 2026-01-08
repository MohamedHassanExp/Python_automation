import os
import json
import time
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class SmartHandler(FileSystemEventHandler):
    def __init__(self, watch_path, extension_map):
        self.watch_path = watch_path
        self.extension_map = extension_map

    def on_modified(self, event):
        #triggers when a file is added to the downloads folder
        for filename in os.listdir(self.watch_path):
            source_path = os.path.join(self.watch_path, filename)
            
            if os.path.isdir(source_path): 
                continue #skip directories

            ext = os.path.splitext(filename)[1].lower()
            if ext in self.extension_map:
                des_dir_name = self.extension_map[ext]
                self.move_file(filename, source_path, des_dir_name)

    def move_file(self, filename, source_path, dest_dir_name):
        destination_dir = os.path.join(self.watch_path, dest_dir_name)
        os.makedirs(destination_dir, exist_ok=True)
        
        destination_path = os.path.join(destination_dir, filename)

        if os.path.exists(destination_path):
            name, ext = os.path.splitext(filename)
            destination_path = os.path.join(destination_dir, f"{name}_{int(time.time())}{ext}")

        try:
            time.sleep(1)
            shutil.move(source_path, destination_path)
            logging.info(f"Moved: {filename} -> {dest_dir_name}")
        except Exception as e:
            logging.error(f"Error moving {filename}: {e}")

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    config = load_config()
    watch_dir = os.path.abspath(config["watch_directory"])

    if not os.path.exists(watch_dir):
        print(f"ERROR: The path '{watch_dir}' does not exist. Check your config.json!")
        exit()

    ext_map = config["extension_map"]

    event_handler = SmartHandler(watch_dir, ext_map)
    observer = Observer()
    observer.schedule(event_handler, watch_dir, recursive=False)

    print(f"--- Monitoring: {watch_dir} ---")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n--- Monitoring Stopped ---")
    observer.join()