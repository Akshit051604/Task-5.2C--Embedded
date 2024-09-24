import RPi.GPIO as GPIO
import tkinter as tk

# Define GPIO pins for the LEDs
Green_led_pin = 27
Red_led_pin = 22
White_led_pin = 17

# Function to initialize GPIO
def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Green_led_pin, GPIO.OUT)
    GPIO.setup(Red_led_pin, GPIO.OUT)
    GPIO.setup(White_led_pin, GPIO.OUT)

# Function to update LED intensity based on slider values
def update_led_intensity(Green_value, Red_value, White_value):
    GPIO.output(Green_led_pin, GPIO.HIGH if Green_value > 0 else GPIO.LOW)
    GPIO.output(Red_led_pin, GPIO.HIGH if Red_value > 0 else GPIO.LOW)
    GPIO.output(White_led_pin, GPIO.HIGH if White_value > 0 else GPIO.LOW)
    pwm_Green.ChangeDutyCycle(Green_value)
    pwm_Red.ChangeDutyCycle(Red_value)
    pwm_White.ChangeDutyCycle(White_value)

# Restart a button
def reset_leds():
    GPIO.output(red_led_pin, GPIO.LOW)
    GPIO.output(green_led_pin, GPIO.LOW)
    GPIO.output(blue_led_pin, GPIO.LOW)
    slider_red.set(0)
    slider_green.set(0)
    slider_blue.set(0)

# Create the GUI window
window = tk.Tk()
window.title("LED Intensity Control")

# Create slider widgets
slider_Green = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: update_led_intensity(value, slider_Red.get(), slider_White.get()))
slider_Red = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: update_led_intensity(slider_Green.get(), value, slider_White.get()))
slider_White = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: update_led_intensity(slider_Green.get(), slider_Red.get(), value))

# Place sliders on the window
slider_Green.pack()
slider_Red.pack()
slider_White.pack()

# Initialize GPIO and start the GUI event loop
initialize_gpio()
window.mainloop()

# Clean up GPIO
GPIO.cleanup()
