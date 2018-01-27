import os, shutil

fileName = 'test.sangyeon'
src = '/Users/sangyeon/python_study/SerchFile/'
testDir = '/Users/sangyeon/python_study/SerchFile/test/'

# shutil.move(src + fileName, testDir +fileName)

command = "mv " + src + fileName + " " + testDir
os.system(command)
