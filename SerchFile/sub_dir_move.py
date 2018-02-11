import os, shutil

# fileName = 'test.sangyeon'
# src = '/Users/sangyeon/python_study/SerchFile/'
# testDir = '/Users/sangyeon/python_study/SerchFile/test/'
testDir = '/Users/sangyeon/python_study/SerchFile/test'
docDir = '/Users/sangyeon/python_study/SerchFile/doc'
docxDir = '/Users/sangyeon/python_study/SerchFile/docx'
pptDir = '/Users/sangyeon/python_study/SerchFile/ppt'
pptxDir = '/Users/sangyeon/python_study/SerchFile/pptx'
xlsxDir = '/Users/sangyeon/python_study/SerchFile/xlsx'

def mv(ext, src, fileName):
    # shutil.move(src + fileName, testDir +fileName)
    # os.rename(src + fileName, testDir + fileName)
    moveDir = ''
    if ext == '.txt':
        poveDir = testDir
    elif ext == '.doc':
        oveDir = docDir
    elif ext == '.docx':
        oveDir = docxDir
    elif ext == '.ppt':
        oveDir = pptDir
    elif ext == '.pptx':
        moveDir = pptxDir
    elif ext == '.xlsx':
        moveDir = xlsxDir

    print 'Before Path: %s' % src
    print 'Move Path: %s ' % moveDir
    print 'file: %s' % fileName
    print '\n'
    command = "mv " + src + fileName + " " + moveDir
    os.system(command)