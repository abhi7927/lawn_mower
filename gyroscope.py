import MPU6050
import time

mpu=MPU6050.MPU6050()
accel = [0]*3
gyro =[0]*3

def setup():
    mpu.dmp.initialize()

def loop():
    while(1):
        accel = mpu.get_acceleration()
        gyro = mpu.get_rotation()
        print("a/g:%d \t %d \t %d \t %d \t %d \t %d"%(accel[0],accel[1],accel[2],gyro[0],gyro[1],gyro[2]))
        print("HI")
        time.sleep()
    
if __name__=="__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        pass
    