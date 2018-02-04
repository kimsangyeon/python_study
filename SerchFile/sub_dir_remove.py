import os

# fileName = 'test.sangyeon'
# src = '/Users/sangyeon/python_study/SerchFile/'

def rm(src, fileName):
    # os.remove(src + fileName)

    command = "rm -rf " + src + fileName
    os.system(command)