from shutil import copyfile
import thingspeak  #pip3 install thingspeak
import os, inspect
import git

def getProjectDirectoryPath():
    # print (inspect.getfile(inspect.currentframe()))  # script filename (usually with path)
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))   # script directory

os.chdir(getProjectDirectoryPath())

# repository = Repo.init(os.getcwd())
# print(repository)

def git_push():
    repo = git.Repo()
    # print(repo)

    repo.git.add('--all')
    repo.git.commit('-m', 'commit message from python script', author='raspberry-omer <kralabitayfa2@gmail.com>')
    
    # repo.git.push()
    os.system("git push -u origin main") 

def copy_log_to_dir():
    log_name = "binance-trader.log"
    if os.path.isfile(log_name):
        print ("File exist")
        os.remove(log_name)
        print ("File is removed")
    else:
        print ("File not exist")

    copyfile("../../binance-trader/" + log_name  ,os.getcwd() + "/" + log_name)
    print ("File is copied")

copy_log_to_dir()
git_push()