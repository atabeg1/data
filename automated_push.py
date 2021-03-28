from shutil import copyfile
from datetime import datetime
import thingspeak  #pip3 install thingspeak
import os, inspect, json, threading
import git

channel_id = "1341788" # Kendi kanal ID'nizi yazınız
write_key  = "UGT4QQYNQMX13Q5V" # Kendi WRITE KEY değerinizi yazınız.
read_key    = "GKPNYYQMPOSSHAGO" # Kendi YOUR API KEY değerinizi yazınız.
channelRead = thingspeak.Channel(id=channel_id,api_key=read_key)
channelWrite = thingspeak.Channel(id=channel_id,api_key=write_key)

def getProjectDirectoryPath():
    # print (inspect.getfile(inspect.currentframe()))  # script filename (usually with path)
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))   # script directory

os.chdir(getProjectDirectoryPath())

def git_push():
    # repository = Repo.init(os.getcwd())
    # print(repository)

    repo = git.Repo()
    # print(repo)

    repo.git.add('--all')
    repo.git.commit('-m', 'commit message from python script', author='raspberry-omer <kralabitayfa2@gmail.com>')
    
    # repo.git.push()
    os.system("git push -u origin main") 
    print(datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "Push process is completed.")

def copy_log_to_dir():
    log_name = "binance-trader.log"
    if os.path.isfile(log_name):
        print(datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "File exist.")
        os.remove(log_name)
        print(datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "File is removed.")
    else:
        print(datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "File not exist.")

    copyfile("../../binance-trader/" + log_name  ,os.getcwd() + "/" + log_name)
    print(datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "File is copied.")

def writeZero():
    try:
        data = {
            "channel_id": channel_id,
            "field1": "0"
        }
        channelWrite.update(data)
        print(datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "Thingspeak flag is reset.")
    except:
        pass

def shouldPush():
    try:
        readFromTS = channelRead.get_field_last(field='field1')
        fieldDict = json.loads(readFromTS)
        fieldLast = int(fieldDict["field1"])

        if fieldLast == 1:
            print(datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "Request arrived.")
            copy_log_to_dir()
            git_push()
            writeZero()
        else:
            print(datetime.now().strftime("%m-%d-%Y %H:%M:%S"), "Waiting for request.")
    except:
        pass

def repeatShouldPush():
    shouldPush()
    threading.Timer(10, repeatShouldPush).start()

repeatShouldPush()