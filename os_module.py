import os.path
import time

PATHS = [
'/one/two/three',
'/one/two/three/',
'/',
'.',
'',
]
# # Use of os.path.split()------------------------------------------------------>

# # It will not split that part('/____/') and other parts will be split.
# for path in PATHS:
#     print(os.path.split(path))

# # Use of os.path.basename()------------------------------------------------------>

# # It will show which part is splitted
# for path in PATHS:
#     print(os.path.basename(path))

# # Use of os.path.dirname()------------------------------------------------------>

# # It will show which part is not splitted
# for path in PATHS:
#     print(os.path.dirname(path))

PATHS = [
'filename.txt',
'filename',
'/path/to/filename.txt',
'/',
'',
'my-archive.tar.gz',
'no-extension.',
]

# # Use of os.path.splitext()------------------------------------------------------>

# # It will not split that part('___.') and after with dot will be split.
# for path in PATHS:
#     print(os.path.splitext(path))

paths = ['/one/two/three/four',
'/one/two/threefold',
'/one/two/three/',
]

# # Use of os.path.commonprefix()------------------------------------------------------>

# # It will give common prefix in whole list
# print('PREFIX:', os.path.commonprefix(paths))

# # Use of os.path.commonpath()------------------------------------------------------>

# # It will give common path in whole list
# print('PREFIX:', os.path.commonpath(paths))

PATHS = [
('one', 'two', 'three'),
('/', 'one', 'two', 'three'),
('/one', '/two', '/three'),
]

# # Use of os.path.join()------------------------------------------------------>

# # It will join split part
# for parts in PATHS:
#     print(os.path.join(*parts))

# # Use of os.path.expanduser()------------------------------------------------------>

# # It will connect to the path
# for user in ['', 'dhellmann', 'nosuchuser']:
#     lookup = '~' + user                       # ~ -----> necessary
#     print('{} : {}'.format(lookup, os.path.expanduser(lookup)))

PATHS = [
'one//two//three',
'one/./two/./three',
'one/../alt/two/three',
]

# # Use of os.path.normpath()------------------------------------------------------>

# # It will remove unwanted parts
# for path in PATHS:
#     print(os.path.normpath(path))

PATHS = [
'.',
'..',
'./one/two/three',
'../one/two/three',
]

# # Use of os.path.abspath()------------------------------------------------------>

# # It will automatically connect with working directory
# for path in PATHS:
#     print('{!r:>21} : {!r}'.format(path, os.path.abspath(path)))

# # File Times-------------------------------------------------------------------->
# print('File :', __file__)   # __file__  ------> It will take current file
# print('Access time :', time.ctime(os.path.getatime(__file__)))
# print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# print('Change time :', time.ctime(os.path.getctime(__file__)))
# print('Size :', os.path.getsize(__file__))

# # Testing files----------------------------------------------------------------->
# file = __file__
# print('File : {!r}'.format(file))
# print('Absolute :', os.path.isabs(file))
# print('Is File? :', os.path.isfile(file))
# print('Is Dir? :', os.path.isdir(file))
# print('Is Link? :', os.path.islink(file))
# print('Mountpoint? :', os.path.ismount(file))
# print('Exists? :', os.path.exists(file))
# print('Link Exists?:', os.path.lexists(file))
# print()
