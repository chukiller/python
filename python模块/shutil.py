# shutil 封装了文件的操作

import shutil

# 移动文件
shutil.move('./python模块/a.txt', './python基础/')

# 复制
shutil.copyfileobj('file_obj1', 'file_obj2')

# 复制文件内容
shutil.copyfile('filepath1', 'filepath2')

# 复制文件内容和权限
shutil.copy('file1', 'file2')

# 复制文件内容和权限和修改时间
shutil.copy2('file1', 'file2')

# 修改时间，权限的复制，不复制内容
shutil.copystat('file1', 'file2')

# 只复制权限
shutil.copymode('file1', 'file2')

# 复制文件夹
shutil.copytree('path1', 'path2')

# 删除文件夹
shutil.rmtree('path')