import time

def mission_timer(func):
    def wrapper(*args,**Kwargs):
        print("3...")
        print("2...")
        print("1...")
        start = time.time()
        func(*args,**Kwargs)
        print("Mission Duration :")
        print(func.__name__,time.time()-start)
        print("\n")
    return wrapper

@mission_timer
def launch_probe(target):
    print(f"Launching probe toward {target}...")
    time.sleep(1)

@mission_timer
def deploy_satellite(orbit_type, altitude_km):
    print(f"Deploying satellite into {orbit_type} orbit at {altitude_km} km...")
    time.sleep(2)

launch_probe("Mars")
deploy_satellite("polar", 800)
deploy_satellite(orbit_type="geostationary", altitude_km=35786)