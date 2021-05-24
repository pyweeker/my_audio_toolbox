import os

cwd = os.getcwd()


files = [f for f in os.listdir(cwd) if os.path.isfile(f)]


print(files)

for file in files:
    if file.endswith('.mid'):

        
        filename, file_extension = os.path.splitext(file)

        print(f" filename {filename}")
        #print(f" file_extension {file_extension}")


        #os.rename(filename, filename[2:-2])
        os.rename(filename+'.mid', filename[2:-2]+'.mid')


       
