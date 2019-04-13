#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time

R,G,B=15,18,14

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(R, RPi.GPIO.OUT)
RPi.GPIO.setup(G, RPi.GPIO.OUT)
RPi.GPIO.setup(B, RPi.GPIO.OUT)

pwmR = RPi.GPIO.PWM(R, 70)
pwmG = RPi.GPIO.PWM(G, 70)
pwmB = RPi.GPIO.PWM(B, 70)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

try:

    t = 0.4
    while True:
        # ��ɫ��ȫ�������ƣ��̵�ȫ������ɫ��
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

        # ��ɫ��ȫ������ƣ�����ȫ������ɫ��
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

        # ��ɫ��ȫ������ƣ��̵�ȫ������ɫ��
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        # ��ƣ��̵�ȫ��������ȫ������ɫ��
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

        # ��ƣ�����ȫ�����̵�ȫ�������ɫ��
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        # �̵ƣ�����ȫ�������ȫ������ɫ��
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        # ��ƣ��̵ƣ�����ȫ������ɫ��
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        # ����������LED�ĸ�����ɫ��������ϳ�������ɫ
        for r in xrange (0, 101, 20):
            pwmR.ChangeDutyCycle(r)
            for g in xrange (0, 101, 20):
                pwmG.ChangeDutyCycle(g)
                for b in xrange (0, 101, 20):
                    pwmB.ChangeDutyCycle(b)
                    time.sleep(0.01)

except KeyboardInterrupt:
    pass

pwmR.stop()
pwmG.stop()
pwmB.stop()

RPi.GPIO.cleanup()
