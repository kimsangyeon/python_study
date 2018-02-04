import os, shutil

# fileName = 'test.sangyeon'
# src = '/Users/sangyeon/python_study/SerchFile/'
# testDir = '/Users/sangyeon/python_study/SerchFile/test/'

def cp(src, fileName, copyDir):
    # shutil.copy(src + fileName, testDir +fileName)
    
    command = "cp " + src + fileName + " " + copyDir
    os.system(command)