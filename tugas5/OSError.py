import os

try:
    os.mkdir('/mydirectory')
except OSError as e:
    print("Failed to create directory: ", e)