import os
import shutil
import random
from datetime import datetime, timedelta
import time
import threading
from logging_config import logger

def delete_old_video_folders(base_path):
    """
    Delete video folders that are from the previous month.
    
    :param base_path: The base directory where video folders are stored
    """
    today = datetime.now()
    first_day_of_current_month = today.replace(day=1)
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
    print(last_day_of_previous_month)
    
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            try:
                # Assuming folder names are in 'YYYY-MM-DD' format
                folder_date = datetime.strptime(folder_name, '%Y-%m-%d')
                if folder_date <= last_day_of_previous_month:
                    shutil.rmtree(folder_path)
                    logger.info(f"Deleted folder: {folder_path}")
            except ValueError:
                # If the folder name is not in the expected date format, skip it
                logger.error(f"Skipping folder with invalid date format: {folder_name}")
                


def create_test_video_folders():
    """
    Create folders for each day from May to July and populate them with random files.
    
    :param base_path: The base directory where folders will be created
    """
    start_date = datetime(2024, 5, 1)  # May 1, 2024
    end_date = datetime(2024, 7, 31)   # July 31, 2024
    base_path = r"E:\Projects\Logging\Result\Videos"
    current_date = start_date
    # while current_date <= end_date:
    while True:
        print("Create Video funciton started..")
        # Create folder for the day
        folder_name = current_date.strftime('%Y-%m-%d')
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # Create random number of files (1 to 5) in the folder
        num_files = random.randint(1, 5)
        for i in range(num_files):
            file_name = f"video_{i+1}.mp4"
            file_path = os.path.join(folder_path, file_name)
            
            # Create an empty file (you can modify this to create actual video files if needed)
            with open(file_path, 'w') as f:
                f.write("This is a placeholder for a video file.")
        
        logger.info(f"Created folder {folder_name} with {num_files} files.")
        
        # Move to the next day
        current_date += timedelta(days=1)
        time.sleep(5)
        
def delete_old_video_folders_fun():
    while True:
        logger.info("Delete folder thread called")
        delete_old_video_folders(r"E:\Projects\Logging\Result\Videos")
        time.sleep(10)

# Usage
base_directory = r"E:\Projects\Logging\Result\Videos"


create_thread = threading.Thread(target=create_test_video_folders)
delete_thread = threading.Thread(target=delete_old_video_folders_fun)
create_thread.start()
delete_thread.start()
# delete_old_video_folders(base_directory)