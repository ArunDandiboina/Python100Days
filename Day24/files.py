# write a file.

with open('test.txt', 'w') as f:
    f.write('This is a test file\n')
    
with open('test.txt', 'r') as f:
    a = f.read()
    print(a)
    
    
# file paths - absolute and relative
# absolute path is the full path to the file - C:\Users\User\OneDrive\Desktop\work\Python100\Day24\test.txt
# relative path is the path relative to the current 
# working directory - ./test.txt or ../test.txt
