import os 
import datetime
today = datetime.date.today()
folder_name = f"log_{today}"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
current_dir = os.getcwd()
print(current_dir)