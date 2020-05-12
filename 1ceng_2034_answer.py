import os
import platform
import requests
import threading
import urllib.request
import multiprocessing


print("------------First Question---------------")
print(" PID is:",os.getpid())

platfrom_name=platform.platform()

platfrom_name=platfrom_name.lower()

load_one_min, load_five_min, load_15_min= os.getloadavg()

if platfrom_name.find("linux")!=-1:

 print("---------Second Question:Load Average----------")

print("Load Average Over the last 1 min:", load_one_min)

print("Load Average Over the last 5 min:", load_five_min)

print("Load Average Over the last 15 min:", load_15_min)

print("----------Third Question:-------------------")



cpu_count=os.cpu_count()

print("Numbers of CPUs in the system is :", cpu_count)

print("Load average over the last 5 minute:", load_five_min)

print("----------Fourth Question:-------------------")


def check_url(response_status_code):
    print("checking url: " + response_status_code)
    response = 0
    try:
        response = requests.get(response_status_code)
    except:
        print("No response code, output was an error.")
        return
    if (response.status_code == 200):
        print("Code " + str(response.status_code) + " is successful")
    elif (response.status_code == 400):
        print("Bad Request")
    elif (response.status_code == 500):
        print("Internal Server Error")
    else:
        print("Code " + str(response.status_code) + " is failed")


array_of_url = ["https://api.github.com", "http://bilgisayar.mu.edu.tr/",
                "https://www.python.org/", "http://akrepnalan.com/ceng2034",
                "https://github.com/caesarsalad/wow"]

for i in range(len(array_of_url)):
    threads = threading.Thread(target=check_url, args=(array_of_url[i],))
    threads.start()
    threads.join()
print("End of Script")