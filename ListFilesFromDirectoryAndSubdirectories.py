import os

path = 'C:\\Users\\lmiller\\Documents\\Teaching\\Fall 2018\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
