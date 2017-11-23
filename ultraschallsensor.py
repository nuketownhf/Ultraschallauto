import RPi.GPIO as GPIO
import time
 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO_TRIGGER = 16
GPIO_ECHO = 18
GPIO_BUZZER = 15
 

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_BUZZER, GPIO.OUT)
 
def distanz():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.000001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
 
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()
 
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
 

    TimeElapsed = StopZeit - StartZeit
    distanz = (TimeElapsed * 34300) / 2
 
    return distanz
abstand = distanz()
GPIO.output(GPIO_BUZZER, False)
if __name__ == '__main__':
    try:
        while True:
            if abstand <= 3:
                
                abstand = distanz()
                GPIO.output(GPIO_BUZZER, True)
                print ("Abstand = %.1f cm" % abstand)
                time.sleep(0.001)
                GPIO.output(GPIO_BUZZER, True)
                
                

            elif abstand < 5.0:
                
                abstand = distanz()
                print ("Abstand = %.1f cm" % abstand)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(0.04)
                GPIO.output(GPIO_BUZZER, True)
                time.sleep(0.1)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(0.001)
                pass
            elif abstand < 10.0:
                abstand = distanz()
                print ("Abstand = %.1f cm" % abstand)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(0.1)
                GPIO.output(GPIO_BUZZER, True)
                time.sleep(0.1)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(0.001)
                pass

            
            elif abstand < 15.0:
                abstand = distanz()
                print ("Abstand = %.1f cm" % abstand)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(0.3)
                GPIO.output(GPIO_BUZZER, True)
                time.sleep(0.2)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(0.001)
                pass
            elif abstand < 30.0:
                abstand = distanz()
                print ("Abstand = %.1f cm" % abstand)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(0.6)
                GPIO.output(GPIO_BUZZER, True)
                time.sleep(0.2)
                GPIO.output(GPIO_BUZZER, False)
                pass

            elif abstand < 40.0:
                abstand = distanz()
                print ("Abstand = %.1f cm" % abstand)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(1)
                GPIO.output(GPIO_BUZZER, True)
                time.sleep(0.3)
                GPIO.output(GPIO_BUZZER, False)
                pass

            elif abstand < 80.0:
                abstand = distanz()
                print ("Abstand = %.1f cm" % abstand)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(2)
                GPIO.output(GPIO_BUZZER, True)
                time.sleep(0.3)
                GPIO.output(GPIO_BUZZER, False)
                pass

            elif abstand < 300.0:
                abstand = distanz()
                print ("Abstand = %.1f cm" % abstand)
                GPIO.output(GPIO_BUZZER, False)
                time.sleep(2)
                GPIO.output(GPIO_BUZZER, True)
                time.sleep(0.3)
                GPIO.output(GPIO_BUZZER, False)
                pass

            else:
                abstand = distanz()
                GPIO.output(GPIO_BUZZER, False)
                
                print ("Abstand = %.1f cm, Messung: FEHLERHAFT" % abstand)
                time.sleep(1.2)
                
                pass
        
            
 
        
    except KeyboardInterrupt:
        print("Messung gestoppt")
        GPIO.cleanup()
