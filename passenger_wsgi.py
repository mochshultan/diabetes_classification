import os
import sys

# Menambahkan direktori proyek ke path
INTERP = os.path.expanduser("/home/mochshultan/venv/bin/python3.10")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Path ke direktori aplikasi
app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_dir)

# Import aplikasi Flask
from app import app as application
