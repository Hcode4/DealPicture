#coding:utf-8

import os
import hashlib

def getmd5(filename):
    file_txt = open(filename,'rb').read()
    m = hashlib.md5(file_txt)
    return m.hexdigest()
def main(path):
    all_size = {}
    total_file = 0
    total_delete = 0
    for root,dirs,files in os.walk(path):
        for file in files:
            real_path = os.path.join(root,file)
            total_file += 1
            if os.path.isfile(real_path):
                size = os.stat(real_path).st_size
                name_and_md5 = [real_path, '']
                if size in all_size.keys():
                    new_md5 = getmd5(real_path)
                    if all_size[size][1] == '':
                        all_size[size][1] = getmd5(all_size[size][0])
                    if new_md5 in all_size[size]:
                        os.remove(real_path)
                        print('删除', file)
                        total_delete += 1
                    else:
                        all_size[size].append(new_md5)
                else:
                    all_size[size] = name_and_md5
    print ('文件个数：', total_file)
    print ('删除个数：', total_delete)
                
#    for file in os.listdir(path):
#        total_file += 1
#        real_path = os.path.join(path, file)
#        if os.path.isfile(real_path) == True:
#            size = os.stat(real_path).st_size
#            name_and_md5 = [real_path, '']
#            if size in all_size.keys():
#                new_md5 = getmd5(real_path)
#                if all_size[size][1] == '':
#                    all_size[size][1] = getmd5(all_size[size][0])
#                if new_md5 in all_size[size]:
#                    os.remove(path+file)
#                    print('删除', file)
#                    total_delete += 1
#                else:
#                    all_size[size].append(new_md5)
#            else:
#                all_size[size] = name_and_md5
#    print ('文件个数：', total_file)
#    print ('删除个数：', total_delete)
if __name__ == '__main__':
    main("E:\Picture")
#    for root,dirs,files in os.walk("E:\Picture",'r'):  
#        for dir in dirs:
#            dir = os.path.join(root,dir)
#            dirfile = dir + "\\"
#            print(dirfile)
#            main(dir)
#n = 0 
#for root,dirs,files in os.walk("E:\Picture",'r'):
#    for file in files:
#        filedir = os.path.join(root,file)
#        n += 1
#        print(os.path.isfile(filedir))
#        print(filedir)
#print(n)