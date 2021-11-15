from pynput import keyboard
import RPi.GPIO as GPIO
from time import sleep

class roboArm:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)

    signal = GPIO.PWM(18,50)
    basey = GPIO.PWM(23,50)
    army = GPIO.PWM(25,50)
    clawx = GPIO.PWM(24,50)
    claw = GPIO.PWM(17,50)

    def __init__(self):
        self.oc=1
        self.baseNum=90
        
        self.servos= [basey, signal, army, clawx]

    def move(servo,pos):
        if(servo !=claw):
            
            pos =pos/18+2
            servo.ChangeDutyCycle(pos)

        elif(servo ==claw):
            servo.ChangeDutyCycle(pos)
        else:
            print("Invalid servo option")

    def stop():
        signal.stop()
        basey.stop()
        army.stop()
        clawx.stop()
        claw.stop()

    def onPress(key):
        self.baseNum = baseNum
        self.oc= oc
        #moving the base left with arrow keys       
        if(key == keyboard.Key.left):
            if(self.baseNum !=0):
                self.baseNum -= 5
                move(signal,self.baseNum)
                print("moving left 1 degree")
            else:
                self.baseNum =0
                move(signal,self.baseNum)
            
        elif(key == keyboard.Key.right):#moving base right with arrow keys
            if(self.baseNum !=180):
                self.baseNum = self.baseNum+5
                move(signal,self.baseNum)
                print("moving right 1 degree")
            else:
                self.baseNum =180
                move(signal,self.baseNum)
              
        elif(key == http://keyboard.Key.space):#controlling the claw
            self.oc +=1
            if(self.oc%2==0):
                move(claw,7)
                print("closing claw")
            else:
                move(claw,2)
                print("opening claw")
        
        else: #throwing false keys
            print("invalid key")

    def onRelease(key):
        if(key ==keyboard.Key.esc):#stopping the program
            stop()
            print("released")
            return False
    def main(self):
        self.servos =servos
        #initialization of arm and putting in neutral pos
        basey.start(0)
        army.start(0)
        clawx.start(0)
        claw.start(0)
        signal.start(0)
        for i in servos:
        
            i.ChangeDutyCycle(7)
            
        move(claw,2)
           
        with keyboard.Listener(on_press=onPress, on_release=onRelease) as listener:
            
            listener.join()

if __name__ == "__main__":
    aye=roboArm()
    aye.main()
