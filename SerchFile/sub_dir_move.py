import os, shutil

# fileName = 'test.sangyeon'
# src = '/Users/sangyeon/python_study/SerchFile/'
# testDir = '/Users/sangyeon/python_study/SerchFile/test/'

def mv(src, fileName, moveDir):
    # shutil.move(src + fileName, testDir +fileName)
    # os.rename(src + fileName, testDir + fileName)
    
    command = "mv " + src + fileName + " " + moveDir
    os.system(command)