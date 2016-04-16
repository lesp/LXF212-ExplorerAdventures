import explorerhat
from time import sleep
from random import randint

def alarm(channel, event):
    duration = randint(1,10)
    print(duration)
    explorerhat.light.red.blink(0.1,0.1)
    explorerhat.light.blue.blink(0.2,0.2)
    explorerhat.output.one.pulse(0.30,0.30,0.10,0.10)
    sleep(duration)
    explorerhat.light.off()
    explorerhat.output.one.off()


def lightsequence(channel, event):
    for i in range(4):
        explorerhat.light.blue.blink(0.1,0.1)
        sleep(1)
        explorerhat.light.yellow.blink(0.1,0.1)
        sleep(1)
        explorerhat.light.red.blink(0.1,0.1)
        sleep(1)
        explorerhat.light.green.blink(0.1,0.1)
        sleep(1)
        explorerhat.light.off()

explorerhat.touch.eight.pressed(alarm)
explorerhat.touch.one.pressed(lightsequence)
