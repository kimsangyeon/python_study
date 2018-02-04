import os, shutil

# fileName = 'test.sangyeon'
# src = '/Users/sangyeon/python_study/SerchFile/'
# testDir = '/Users/sangyeon/python_study/SerchFile/test/'

def cp(src, fileName, copyDir):
    # shutil.move(src + fileName, testDir +fileName)
    # os.rename(src + fileName, testDir + fileName)
    
    command = "cp " + src + fileName + " " + copyDir
    os.system(command)