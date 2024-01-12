import os
import glob
from tqdm import tqdm

file_names = glob.glob("./*.ISF")
print("Found {} files".format(len(file_names)))
print("It will take a while to convert all files to 16 bit format. Please wait...")

for file_name in tqdm(file_names):
    command = f"cnvrtwfm -l -8- {file_name}"
    os.system(command)

print("Done! Converted all files to 16 bit format. Congratulations from ZJU(/doge)!")