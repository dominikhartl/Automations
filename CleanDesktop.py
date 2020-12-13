import os
import shutil
import yaml

path = '/Users/hartdomi/Desktop/'
yml = '/Users/hartdomi/Code/Automations/DesktopAssignments.yml'

with open(yml) as file:
    assignment = yaml.load(file, Loader=yaml.FullLoader)

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

list_ = files(path)
for file_ in list_:
    try:
        for expr in assignment.keys():
            if expr in file_:
                shutil.move(path+file_,assignment[expr]+file_)
        else:
            pass
    except:
        pass
