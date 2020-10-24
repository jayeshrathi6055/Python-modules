import zipfile

# # Use of is_zipfile()------------------------------------------------------------------>

# for filename in ['README.txt', 'example.zip','bad_example.zip', 'notthere.zip']:
#     print(zipfile.is_zipfile(filename))

# # Use of Zipfile()------------------------------------------------------------------>

# with zipfile.ZipFile('example.zip', 'r') as zf:
#     print(zf.namelist())

# # Get Information of zipfile()------------------------------------------------------------------>

# zf = zipfile.ZipFile('example.zip')
# for info in zf.infolist():
#     print(info.filename)
#     print(info.comment)
#     print(info.create_version)
#     print(info.compress_size,'bytes')
#     print(info.file_size,'bytes')

# # Use of getinfo()-------------------------------------------------------------------------------->

# zf = zipfile.ZipFile('example.zip')
# filename = ['readme.txt','notthere.txt']
# for files in filename:
#     try:
#         zf.getinfo(files)
#     except KeyError:
#         print(f"{files} not present")
#     else:
#         print(f"{files} is there")

# # Read the data-------------------------------------------------------------------------------->

# zf = zipfile.ZipFile('example.zip')
# data = zf.read('readme.txt')
# print(data)

# # Whole information of zipfile----------------------------------------------------------------->

# zf = zipfile.ZipFile('example.zip')
# zi = zf.infolist()
# print(zi)
