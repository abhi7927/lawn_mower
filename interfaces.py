import RPi.GPIO as GPIO
#from mpu6050 import mpu6050
import time

GPIO.setmode(GPIO.BCM)

class Ultrasonic:
    def __init__(self):
        self.TRIGL = 23 
        self.ECHOL = 24

        self.TRIGR = 17
        self.ECHOR = 21

        self.TRIGM = 25
        self.ECHOM = 26
        
        self.pulse_start_L=0
        self.pulse_end_L=0
        self.pulse_duration_L=0
        self.distanceL=0
        
        self.pulse_start_M=0
        self.pulse_end_M=0
        self.pulse_duration_M=0
        self.distanceM=0
        
        self.pulse_start_R=0
        self.pulse_end_R=0
        self.pulse_duration_R=0
        self.distanceR=0
        
        self.setup()
          
        
    def setup(self):  
        GPIO.setup(self.TRIGL,GPIO.OUT)          #Setup input and outputs 
        GPIO.setup(self.ECHOL,GPIO.IN)

        GPIO.setup(self.TRIGR,GPIO.OUT)
        GPIO.setup(self.ECHOR,GPIO.IN)

        GPIO.setup(self.TRIGM,GPIO.OUT)          
        GPIO.setup(self.ECHOM,GPIO.IN)
        
        GPIO.output(self.TRIGL, False)           #Make sensors off 
        GPIO.output(self.TRIGR, False)
        GPIO.output(self.TRIGM, False)
        time.sleep(2)

    def trig(self,val):
        if val=='L':
            GPIO.output(self.TRIGL, True)
            time.sleep(0.00001)
            GPIO.output(self.TRIGL, False)
            
        elif val=='M':
            GPIO.output(self.TRIGM, True)
            time.sleep(0.00001)
            GPIO.output(self.TRIGM, False)
            
        else:
            GPIO.output(self.TRIGR, True)
            time.sleep(0.00001)
            GPIO.output(self.TRIGR, False)
            
    def echo(self,val):
        if val=='L': 
            while GPIO.input(self.ECHOL)==0:
                self.pulse_start_L = time.time()

            while GPIO.input(self.ECHOL)==1:
                self.pulse_end_L = time.time()
                
            self.pulse_duration_L = self.pulse_end_L - self.pulse_start_L
              
            self.distanceL = self.pulse_duration_L * 17150

            self.distanceL= round(self.distanceL, 2)
            print ("Left Distance:",self.distanceL,"cm\n")
            
            return self.distanceL

        elif val=='M':
            while GPIO.input(self.ECHOM)==0:
                self.pulse_start_M = time.time()

            while GPIO.input(self.ECHOM)==1:
                self.pulse_end_M = time.time()
            self.pulse_duration_M = self.pulse_end_M - self.pulse_start_M
            
            self.distanceM = self.pulse_duration_M * 17150

            self.distanceM = round(self.distanceM, 2)
            print ("Middle Distance:",self.distanceM,"cm\n")
            
            return self.distanceM
 
        else:
            while GPIO.input(self.ECHOR)==0:
                self.pulse_start_R = time.time()

            while GPIO.input(self.ECHOR)==1:
                self.pulse_end_R = time.time()

            self.pulse_duration_R = self.pulse_end_R - self.pulse_start_R
            self.distanceR = self.pulse_duration_R * 17150

            self.distanceR = round(self.distanceR, 2)
            print ("Right Distance:",self.distanceR,"cm\n")
            
            return self.distanceR
            
class Wheel:
    def __init__(self):
        self.in1 = 4
        self.in2 = 13
        self.ena = 16

        self.in3 = 18
        self.in4 = 19
        self.enb = 20
        
        self.temp1=1
        self.setup()
    
    def setup(self):
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.ena,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        self.m1=GPIO.PWM(self.ena,1000)

        self.m1.start(25)

        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.enb,GPIO.OUT)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)
        self.m2=GPIO.PWM(self.enb,1000)

        self.m2.start(25)
        
    def accelerate(self):
        self.exe_motor('l')
        time.sleep(0.1)
        self.exe_motor('m')
        time.sleep(0.1)
        self.exe_motor('h')
        time.sleep(0.1)
        
    def exe_motor(self,x):
        if x=='r':
            print("run")
            if(self.temp1==1):
                GPIO.output(self.in1,GPIO.HIGH)
                GPIO.output(self.in2,GPIO.LOW)
                GPIO.output(self.in3,GPIO.HIGH)
                GPIO.output(self.in4,GPIO.LOW)
                print("forward")
                x='z'
            else:
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.HIGH)
                GPIO.output(self.in3,GPIO.LOW)
                GPIO.output(self.in4,GPIO.HIGH)
                print("backward")
                x='z'


        elif x=='s':
            print("stop")
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.LOW)
            GPIO.output(self.in3,GPIO.LOW)
            GPIO.output(self.in4,GPIO.LOW)
            x='z'

        elif x=='f':
            print("forward")
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            GPIO.output(self.in3,GPIO.HIGH)
            GPIO.output(self.in4,GPIO.LOW)
            self.temp1=1
            x='z'

        elif x=='b':
            print("backward")
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            GPIO.output(self.in3,GPIO.LOW)
            GPIO.output(self.in4,GPIO.HIGH)
            self.temp1=0
            x='z'
        
        elif x=='lt':
            if(self.temp1==1):
                print("Forward left")
                GPIO.output(self.in1,GPIO.HIGH)
                GPIO.output(self.in2,GPIO.LOW)
                GPIO.output(self.in3,GPIO.LOW)
                GPIO.output(self.in4,GPIO.LOW)
                x='z'
            else:
                print("Backward left")
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.HIGH)
                GPIO.output(self.in3,GPIO.LOW)
                GPIO.output(self.in4,GPIO.LOW)
                x='z'
            
        elif x=='rt':
            if(self.temp1==1):
                print("Forward right")
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.LOW)
                GPIO.output(self.in3,GPIO.HIGH)
                GPIO.output(self.in4,GPIO.LOW)
                x='z'
            else:
                print("Backward right")
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.LOW)
                GPIO.output(self.in3,GPIO.LOW)
                GPIO.output(self.in4,GPIO.HIGH)
                x='z'

        elif x=='l':
            print("low")
            self.m1.ChangeDutyCycle(25)
            self.m2.ChangeDutyCycle(25)
            x='z'

        elif x=='m':
            print("medium")
            self.m1.ChangeDutyCycle(50)
            self.m2.ChangeDutyCycle(50)
            x='z'

        elif x=='h':
            print("high")
            self.m1.ChangeDutyCycle(100)
            self.m2.ChangeDutyCycle(100)
            x='z'
        
        elif x=='e':
            GPIO.cleanup()
            print("GPIO Clean up")
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
            
class Blade:
    def __init__(self):
        self.in1 = 6
        self.in2 = 12
        self.ena = 5

        self.temp1=1
        
        self.setup()
        
    def setup(self):
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.ena,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        self.m3=GPIO.PWM(self.ena,100)

        self.m3.start(5)
        
    def accelerate(self):
        self.exe_blade('l')
        time.sleep(0.1)
        '''self.exe_blade('m')
        time.sleep(0.1)
        self.exe_blade('h')
        time.sleep(0.1)'''
        
    def exe_blade(self,x):
        if x=='r':
            print("run")
            if(self.temp1==1):
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.HIGH)
                print("forward")
                x='z'
            else:
                GPIO.output(self.in1,GPIO.HIGH)
                GPIO.output(self.in2,GPIO.LOW)
                print("backward")
                x='z'


        elif x=='s':
            print("stop")
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.LOW)
            x='z'

        elif x=='f':
            print("forward")
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            self.temp1=1
            x='z'        

        elif x=='l':
            print("low")
            self.m3.ChangeDutyCycle(35)
            x='z'
        elif x=='m':
            print("medium")
            self.m3.ChangeDutyCycle(60)
            x='z'

        elif x=='h':
            print("high")
            self.m3.ChangeDutyCycle(95)
            x='z'
        
        elif x=='e':
            GPIO.cleanup()
            print("GPIO Clean up")
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
            
'''class Gyroscope:
    def __init__(self):
        self.mpu = mpu6050(0x68)
        self.accel_data = 0
        self.gyro_data = 0
        
    def sense(self):
        print("Temp : "+str(self.mpu.get_temp()))
        print()

        self.accel_data = self.mpu.get_accel_data()
        print("Acc X : "+str(self.accel_data['x']))
        print("Acc Y : "+str(self.accel_data['y']))
        print("Acc Z : "+str(self.accel_data['z']))
        print()

        self.gyro_data = self.mpu.get_gyro_data()
        print("Gyro X : "+str(self.gyro_data['x']))
        print("Gyro Y : "+str(self.gyro_data['y']))
        print("Gyro Z : "+str(self.gyro_data['z']))
        print()
        print("-------------------------------")
        time.sleep(1)'''


