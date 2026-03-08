import time

def mission(func):
    def wrapper():
        print("3...")
        print("2...")
        print("1...")
        start = time.time()
        func()
        print("Mission Duration :")
        print(func.__name__,time.time()-start)
        print("\n")
    return wrapper

@mission
def launch_probe():
    print("Launching probe...")
    time.sleep(1)

@mission
def deploy_satellite():
    print("Deploying satellite...")
    time.sleep(2)

launch_probe()
deploy_satellite()