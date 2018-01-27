import shutil

fileName = 'test.sangyeon'
src = '/Users/sangyeon/python_study/SerchFile/'
testDir = '/Users/sangyeon/python_study/SerchFile/test/'

shutil.move(src + fileName, testDir +fileName)


