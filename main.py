
import os
import datetime
x = datetime.datetime.now()
folder_name = x.strftime("%Y_%m_%d-%H_%M_%S")
os.mkdir(os.environ['USERPROFILE'] + "\\Documents\\Automation\\screenshots\\{}".format(folder_name))
