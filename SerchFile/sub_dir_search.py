# Sub Directory Search File
import sys, os
from errno import EACCES, EPERM, ENOENT
from sub_dir_move import mv

def search(src, movePath):
    try:
        fileNames = os.listdir(src)

        for fileName in fileNames:
            filePath = os.path.join(src, fileName)

            if os.path.isdir(filePath):
                search(filePath, movePath)
            else:
                ext = os.path.splitext(filePath)[1]
                mv(ext, src, fileName, movePath)
    except (IOError, OSError) as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fileName = os.getcwd() + "/" + os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print_error_message(e, fileName)
        pass

# def search(dirName):
#     try:
#         for (path, dir, files) in os.walk(dirName):
#             for fileName in files:
#                 ext = os.path.splitext(fileName)[-1]

#                 if ext == '.py':
#                     print("%s%s" % (path, fileName))
#     except (IOError, OSError) as e:
#         exc_type, exc_obj, exc_tb = sys.exc_info()
#         fileName = os.getcwd() + "/" + os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#         print_error_message(e, fileName)
#         pass

def print_error_message(e, file_name):
    #PermissionError
    if e.errno == EPERM or e.errno == EACCES:
        print("PermissionError error({0}): {1} for: {2}".format(e.errno, e.strerror, file_name))
    #FileNotFoundError
    elif e.errno==ENOENT:
        print("FileNotFoundError error({0}): {1} as: {2}".format(e.errno, e.strerror, file_name))
    elif IOError:
        print("I/O error({0}): {1} as: {2}".format(e.errno, e.strerror, file_name))
    elif OSError:
        print("OS error({0}): {1} as: {2}".format(e.errno, e.strerror, file_name))

# test path
#"/Users/sangyeon/python_study/SerchFile/"

path = sys.argv[1]
movePath = sys.argv[2]
if  os.path.isdir(path) and os.path.isdir(movePath):
    search(path, movePath)
else:
    print "Not found path Error"
