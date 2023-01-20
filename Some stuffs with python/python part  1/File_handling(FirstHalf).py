from pathlib import Path, os
myfiles = ['games','pictures','videos']
for file in myfiles:
    print(f" C:// This pc// {file}")

print(
    Path.home()
)

#Making directory from os function, it can make several directories at once
# os.makedirs("C:/Users/Asus/Desktop/The folder created by Python")

#Making directory with path function
# Path("C:/Users/Asus/Desktop/Folder created from path function").mkdir()

#Knowing whether the path is absolute or relative
print(
    Path().cwd()
) 
print(
Path().cwd().is_absolute()
)
print(
    Path("Desktop/The folder created by Python").is_absolute()
)
#Getting the parts of the file
path1 = "C:/Users\Asus/Desktop/Python practice/Automate the Boring stuff with python"
print(
    Path().cwd().parents[4]
)
realpath = path1 + "/" +"File_handling(FirstHalf).py"
  #Getting path base name
print(
    os.path.basename(realpath)
)
  #Getting both basename and directory name of the file
print(
    os.path.split(realpath)
)
#Getting the file size
print(
os.path.getsize(realpath)
)
#Getting the list of each file in particular directory
print(
    os.listdir(path1)
)
#Getting the total size of directory
totalsize = 0
for filesize in os.listdir(path1):
    totalsize =totalsize + os.path.getsize(filesize)
print(totalsize)

#Glob Method
p = Path(path1)
   #listing path of all files of directory
print (list(p.glob("*")))
   #listing all only text files of directory
print(list(p.glob("*.txt")))
   #listing all python files of directory
print(list(p.glob("*.py")))
