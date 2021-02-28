from microbit import *
import neopixel

# define your variables
numled = 20 # total number of LEDs
offset = 20 # set the offset to bring the temperature within the range of your NeoPixels
strip = neopixel.NeoPixel(pin0, numled) #define our NeoPixel strip, (what pin and how many NeoPixels)
currentTemp = temperature() #Read the temperature from the microBit
max = currentTemp # set the initial variable value of the 'max' temperature
min = currentTemp # set the initial variable value for the 'min' temperature
wait_time = 1000 # set what the sleep time is
strip.clear() # clear down the NeoPixels Just in case
strip.show() # Show cleared NeoPixels

while True: # our loop
    display.set_pixel(0,0,5) #show a pixel - Blinking LED
    
    # Set the Man and Mix
    currentTemp = temperature()  # get the current temperature
    if currentTemp < min: #if the current temperature is less than our defined minimum do:
        min = currentTemp # set 'min' to be the new low.
    if currentTemp > max: # if the current temperature is more than our defined maximum do:
        max = currentTemp # set 'max' to be the new high.
    
    # Make the NeoPixels Work
    lednum = currentTemp-offset # LED number to be on, minus our offset
    for led in range (0,lednum): # for range 0 to our number do:
        strip[led] = (0,127,0) # (red, green, blue)
    for led in range (lednum, numled): # for range our number to last do:
        strip[led] = (0,0,0)
    strip.show() # show on NeoPixels
    
    if button_a.was_pressed(): # if button A has been pressed
        display.scroll(currentTemp) # scroll the current temperature
    if button_b.was_pressed(): # if button B has been pressed
            display.scroll(min) # scroll the minimum value
            display.scroll("-") # insert hyphen
            display.scroll(max) # scroll the max value
    
    sleep(wait_time) # sleep for a bit
    display.clear() # clear the screen
    sleep(wait_time/2) # sleep for a bit.