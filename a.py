import os, inspect
import git

def getProjectDirectoryPath():
    # print (inspect.getfile(inspect.currentframe()))  # script filename (usually with path)
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))   # script directory

os.chdir(getProjectDirectoryPath())

# repository = Repo.init(os.getcwd())
# print(repository)

repo = git.Repo()
# print(repo)

repo.git.add('--all')
repo.git.commit('-m', 'commit message from python script', author='raspberry-omer <kralabitayfa2@gmail.com>')
 
repo.git.push()
