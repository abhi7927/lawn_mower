from interfaces import *
import time
#ultra = Ultrasonic()
blade = Blade()
#wheel = Wheel()
#gyro = Gyroscope()

stop_motor = True
stop_blade = True


try: 
    while True:
#        ultra.trig('M')
 #       distanceM = ultra.echo('M')
 #       print ("Middle Distance:",distanceM,"cm\n")
  #      time.sleep(0.005)
   #     ultra.trig('L')
    #    distanceL = ultra.echo('L')
     #   print ("Left Distance:",distanceL,"cm\n")
 #       time.sleep(0.005)
  #      ultra.trig('R')
   #     distanceR = ultra.echo('R')
 #       print ("Right Distance:",distanceR,"cm\n")
  #      time.sleep(0.005)
        
       
            
   #     if distanceL<=15 or distanceM<=15 or distanceR<=15:
    #        wheel.exe_motor('s')
     #   else:   
      #      wheel.exe_motor('r')
           
        time.sleep(1)     
        if stop_blade:
        blade.exe_blade('r')
        stop_blade=False
        
        
except KeyboardInterrupt:
    wheel.exe_motor('l')
    wheel.exe_motor('s')
    wheel.exe_motor('e')
    
    blade.exe_blade('l')
    blade.exe_blade('s')
    blade.exe_blade('e')
    
    
#    gyro.sense()
    
#    wheel.exe_motor('r')
#    if stop_motor:
#        wheel.accelerate()
#        stop_motor = False
    
#    blade.exe_blade('r')
#    if stop_blade:
#       blade.accelerate()
#        stop_blade = False
    
    
    
    
    
