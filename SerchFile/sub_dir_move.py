import os, shutil
from sub_dir_mkdir import mkdir

# fileName = 'test.sangyeon'
# src = '/Users/sangyeon/python_study/SerchFile/'
# testDir = '/Users/sangyeon/python_study/SerchFile/test/'

def mv(ext, src, fileName, movePath):
    # shutil.move(src + fileName, testDir +fileName)
    # os.rename(src + fileName, testDir + fileName)
    moveDir = ''
    if ext == '.doc':
        if os.path.isdir(movePath + 'doc') is not True:
            mkdir(movePath + 'doc')
        moveDir = movePath + 'doc'
    elif ext == '.docx':
        if os.path.isdir(movePath + 'docx') is not True:
            mkdir(movePath + 'docx')
        moveDir = movePath + 'docx'
    elif ext == '.ppt':
        if os.path.isdir(movePath + 'ppt') is not True:
            mkdir(movePath + 'ppt')
        moveDir = movePath + 'ppt'
    elif ext == '.pptx':
        if os.path.isdir(movePath + 'pptx') is not True:
            mkdir(movePath + 'pptx')
        moveDir = movePath + 'pptx'
    elif ext == '.xlsx':
        if os.path.isdir(movePath + 'xlsx') is not True:
            mkdir(movePath + 'xlsx')
        moveDir = movePath + 'xlsx'
    else:
        return

    print 'Before Path: %s' % src
    print 'Move Path: %s ' % moveDir
    print 'file: %s' % fileName
    print '\n'
    command = "mv " + src + fileName + " " + moveDir
    os.system(command)