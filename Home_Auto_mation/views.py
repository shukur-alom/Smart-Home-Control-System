from django.http import HttpResponse
from django.shortcuts import render
import RPi.GPIO as GPIO

led_1,led_2,led_3 = 15,18,14
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)


def ind(request):
    alart,light_status_1,light_status_2,light_status_3 = "Light","","",""
    light_1 = int(request.GET.get("signal_1",0))
    light_2 = int(request.GET.get("signal_2",0))
    light_3 = int(request.GET.get("signal_3",0))
    print(light_1,light_2,light_3)
    
    if light_1 == 1:
        light_status_1 = "checked"
        alart += " one" 
        GPIO.output(led_1, GPIO.HIGH)   
    if light_2 == 1:
        light_status_2 = "checked" 
        alart += " two" 
        GPIO.output(led_2, GPIO.HIGH)   
    if light_3 == 1:
        light_status_3 = "checked" 
        alart += " three"
        GPIO.output(led_3, GPIO.HIGH)   

    if light_1 == 0:GPIO.output(led_1, GPIO.LOW)       
    if light_2 == 0:GPIO.output(led_2, GPIO.LOW)   
    if light_3 == 0:GPIO.output(led_3, GPIO.LOW)   
    
    if light_1 == 1 or light_2 == 1 or light_3 == 1:alart+=' is ON'
    if light_1 == 0 and light_2 == 0 and light_3 == 0:alart ='All Lights is OFF'

    pass_={'alart_variable':alart,'light_status_1':light_status_1,'light_status_2':light_status_2,'light_status_3':light_status_3}
    return render(request,"Home_page.html",pass_)  

def about(request): return render(request, 'about.html')

#href="{% url 'about' %}"