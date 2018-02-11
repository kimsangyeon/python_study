import os, shutil

# fileName = 'test.sangyeon'
# src = '/Users/sangyeon/python_study/SerchFile/'
# testDir = '/Users/sangyeon/python_study/SerchFile/test/'

def mkdir(mkDir):
    # shutil.copy(src + fileName, testDir +fileName)
    
    command = "mkdir " + mkDir
    os.system(command)