#! /usr/bin/env python3
#SolTerraLuna v0.3
#SolTerraLuna is a simple playback script based upon crleblanc's code snippet

#Import serial to access the serial port, datetime for time, json to store data,
#and irtoy to actually do any important work what-so-ever. Thanks so much,
#crleblanc!
import serial
import datetime
import time
import json
import irtoy_nohs as pIRt
import shutil

#Import modules needed for Python version check, OS/host check
import sys
import math
import platform

#Setup terminal width to get footer/header padding correct
sugtsc = shutil.get_terminal_size().columns

#Setup header/footer formatting
header_none = ('-'*sugtsc)
footer_none = ('='*sugtsc)
footer_end = ('='*sugtsc+'\n')

#Setup Date/Time variables for usage
dnh = datetime.datetime.now().hour
dnm = datetime.datetime.now().minute
dns = datetime.datetime.now().second
dny = datetime.datetime.now().year
dnn = datetime.datetime.now().month
dnd = datetime.datetime.now().day

#Establish SolTerraLuna version.
STL_v = 'SolTerraLuna v0.3 | Compiled: 2018-02-18 00:50:23'

#Store results of version check
python_version = sys.version

#Print version of Nastynote & Python Version
print(python_version+'\n'+STL_v+footer_none, sep='')

run = 0

print(header_none)
print('[{:04,d}'.format(run),']',' SolTerraLuna - Started: ',dnh,':',dnm,':',dns,' | ',dny,'-',dnn,'-',dnd,' |', sep="")
print('[{:04,d}'.format(run),']',' Initializing brightness...', sep="")
print(footer_none)

#Open the default USB Serial port under Linux using with/as for safety
with serial.Serial('/dev/ttyACM0') as serialDevice:

    if dnh in [5,6,7,8,9,10,11,12]:
        bright = 'bright_down'
        steps = 9
        state = 'power_on'
        filen = 'color_white'

    elif dnh in [0,1,2,3,4,13,14,15,16,17,18,19,20,21,22,23]:
        bright = 'bright_up'
        steps = 9
        state = 'power_on'
        filen = 'color_white'
        
        # create a new instance of the IrToy class
        pIRT = pIRt.IrToy(serialDevice)

        # Note: this call will block (hang) until an IR code has been received.
        with open(filen, mode='r') as file:
            IRCode = json.load(file)

        # Note: this call will block (hang) until an IR code has been received.
        with open(state, mode='r') as file:
            IRStatus = json.load(file)

        # Note: this call will block (hang) until an IR code has been received.
        with open(bright, mode='r') as file:
            IRBright = json.load(file)

        stepssent=0

        # transmit the recorded signal back to the IR Toy
        pIRT.transmit(IRStatus)
        pIRT.transmit(IRCode)
        time.sleep(0.25)
        for i in range(steps):
            pIRT.transmit(IRBright)
            time.sleep(0.25)
            stepssent +=1

        #Print a message telling the user that the signal was repeated, and read it back
        #print('[{:04,d}'.format(run),']',' Sent signal: ',state,' + ',filen,' + [',stepssent,'] ',bright,' at ',dnh,':',dnm,':',dns,' | ',dny,'-',dnn,'-',dnd,' |', sep="")
        print('[{:04,d}'.format(run),']',' Sent signal: ',state,' + ',filen,' + [',stepssent,'] ',bright, sep="")
        print('[{:04,d}'.format(run),']',' Sleeping 1 second...', sep="")
        print(footer_end)    
        time.sleep(1)

dnh = datetime.datetime.now().hour
dnm = datetime.datetime.now().minute
dns = datetime.datetime.now().second
dny = datetime.datetime.now().year
dnn = datetime.datetime.now().month
dnd = datetime.datetime.now().day

print(header_none)
print('[{:04,d}'.format(run),']',' SolTerraLuna - Started: ',dnh,':',dnm,':',dns, ' | ',dny,'-',dnn,'-',dnd,' |', sep="")
print('[{:04,d}'.format(run),']',' Synchronizing brightness...', sep="")
print(footer_none)

#Open the default USB Serial port under Linux using with/as for safety
with serial.Serial('/dev/ttyACM0') as serialDevice:

    if dnh == 5:
        filen = 'color_red'
        bright = 'bright_up'
        steps = 1
        state = 'power_on'

    elif dnh == 6:
        filen = 'color_red_mix_green_1'
        bright = 'bright_up'
        steps = 2
        state = 'power_on'
        
    elif dnh == 7:
        filen = 'color_red_mix_green_2'
        bright = 'bright_up'
        steps = 3
        state = 'power_on'
                  
    elif dnh == 8:
        filen = 'color_red_mix_green_3'
        bright = 'bright_up'
        steps = 4
        state = 'power_on'
                   
    elif dnh == 9:
        filen = 'color_red_mix_green_4'
        bright = 'bright_up'
        steps = 5
        state = 'power_on'
                    
    elif dnh == 10:
        filen = 'color_white'
        bright = 'bright_up'
        steps = 6
        state = 'power_on'
        
    elif dnh == 11:
        filen = 'color_white'
        bright = 'bright_up'
        steps = 7
        state = 'power_on'
        
    elif dnh == 12:
        filen = 'color_white'
        bright = 'bright_up'
        steps = 8
        state = 'power_on'
        
    elif dnh == 13:
        filen = 'color_white'
        bright = 'bright_up'
        steps = 9
        state = 'power_on'
        
    elif dnh == 14:
        filen = 'color_red_mix_green_4'
        bright = 'bright_down'
        steps = 1
        state = 'power_on'

    elif dnh == 15:
        filen = 'color_red_mix_green_3'
        bright = 'bright_down'
        steps = 2
        state = 'power_on'
        
    elif dnh == 16:
        filen = 'color_red_mix_green_2'            
        bright = 'bright_down'
        steps = 3
        state = 'power_on'
        
    elif dnh == 17:
        filen = 'color_red_mix_green_1'
        bright = 'bright_down'
        steps = 4
        state = 'power_on'
        
    elif dnh == 18:
        filen = 'color_red'
        bright = 'bright_down'
        steps = 5
        state = 'power_on'
        
    elif dnh == 19:
        filen = 'color_blue_mix_red_4'
        bright = 'bright_down'
        steps = 6
        state = 'power_on'
        
    elif dnh == 20:
        filen = 'color_blue_mix_red_3'
        bright = 'bright_down'
        steps = 7
        state = 'power_on'
        
    elif dnh == 21:
        filen = 'color_blue_mix_red_2'
        bright = 'bright_down'
        steps = 8
        state = 'power_on'
        
    elif dnh == 22:
        filen = 'color_blue_mix_red_1'
        bright = 'bright_down'
        steps = 9
        state = 'power_on'
        
    elif dnh == 23:
        filen = 'color_blue'
        bright = 'bright_down'
        steps = 9
        state = 'power_on'
        
    elif dnh == 0:
        filen = 'color_blue'
        bright = 'bright_down'
        steps = 9
        state = 'power_on'

    elif dnh == 1:
        filen = 'color_blue'
        bright = 'bright_down'
        steps = 9
        state = 'power_on'

    elif dnh == 2:
        filen = 'color_blue'
        bright = 'bright_down'
        steps = 9
        state = 'power_on'

    elif dnh == 3:
        filen = 'color_blue'
        bright = 'bright_down'
        steps = 9
        state = 'power_on'

    elif dnh == 4:
        filen = 'color_blue'
        bright = 'bright_down'
        steps = 9
        state = 'power_on'
        
    else:
        filen = 'mode_strobe'
        bright = 'bright_up'
        steps = 9
        state = 'power_on'
        
    # create a new instance of the IrToy class
    pIRT = pIRt.IrToy(serialDevice)

    # Note: this call will block (hang) until an IR code has been received.
    with open(state, mode='r') as file:
        IRStatus = json.load(file)

    # Note: this call will block (hang) until an IR code has been received.
    with open(filen, mode='r') as file:
        IRCode = json.load(file)

    # Note: this call will block (hang) until an IR code has been received.
    with open(bright, mode='r') as file:
        IRBright = json.load(file)

    stepssent=0

    sleepx = ((60*(60-dnm))-dns)
    
    # transmit the recorded signal back to the IR Toy
    pIRT.transmit(IRStatus)
    pIRT.transmit(IRCode)
    for i in range(steps):
        pIRT.transmit(IRBright)
        time.sleep(0.25)
        stepssent +=1

#Print a message telling the user that the signal was repeated, and read it back
#print('[{:04,d}'.format(run),']',' Sent signal: ',state,' + ',filen,' + [',stepssent,'] ',bright,' at ',dnh,':',dnm,':',dns,' | ',dny,'-',dnn,'-',dnd,' |', sep="")
print('[{:04,d}'.format(run),']',' Sent signal: ',state,' + ',filen,' + [',stepssent,'] ',bright, sep="")
print('[{:04,d}'.format(run),']',' Sleeping ',sleepx//60,'m',sleepx%60,'s...', sep="")
print(footer_end)    
time.sleep(sleepx)

dnhold = dnh

while True:
    dnh = datetime.datetime.now().hour
    dnm = datetime.datetime.now().minute
    dns = datetime.datetime.now().second
    dny = datetime.datetime.now().year
    dnn = datetime.datetime.now().month
    dnd = datetime.datetime.now().day
    
    print(header_none)
    print('[{:04,d}'.format(run),']',' SolTerraLuna - Woke up: ',dnh,':',dnm,':',dns,' | ',dny,'-',dnn,'-',dnd,' |', sep="")
    print(footer_none)
    #Open the default USB Serial port under Linux using with/as for safety
    with serial.Serial('/dev/ttyACM0') as serialDevice:

        if dnh == 5:
            filen = 'color_red'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'

        elif dnh == 6:
            filen = 'color_red_mix_green_1'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'
            
        elif dnh == 7:
            filen = 'color_red_mix_green_2'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'
                      
        elif dnh == 8:
            filen = 'color_red_mix_green_3'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'
                       
        elif dnh == 9:
            filen = 'color_red_mix_green_4'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'
                        
        elif dnh == 10:
            filen = 'color_white'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'
            
        elif dnh == 11:
            filen = 'color_white'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'
            
        elif dnh == 12:
            filen = 'color_white'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'
            
        elif dnh == 13:
            filen = 'color_white'
            bright = 'bright_up'
            steps = 1
            state = 'power_on'
            
        elif dnh == 14:
            filen = 'color_red_mix_green_4'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'

        elif dnh == 15:
            filen = 'color_red_mix_green_3'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 16:
            filen = 'color_red_mix_green_2'            
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 17:
            filen = 'color_red_mix_green_1'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 18:
            filen = 'color_red'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 19:
            filen = 'color_blue_mix_red_4'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 20:
            filen = 'color_blue_mix_red_3'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 21:
            filen = 'color_blue_mix_red_2'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 22:
            filen = 'color_blue_mix_red_1'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 23:
            filen = 'color_blue'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 0:
            filen = 'color_blue'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 1:
            filen = 'color_blue'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 2:
            filen = 'color_blue'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 3:
            filen = 'color_blue'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        elif dnh == 4:
            filen = 'color_blue'
            bright = 'bright_down'
            steps = 1
            state = 'power_on'
            
        else:
            filen = 'mode_strobe'
            bright = 'bright_up'
            steps = 9
            state = 'power_on'
            
        # create a new instance of the IrToy class
        pIRT = pIRt.IrToy(serialDevice)

        # Note: this call will block (hang) until an IR code has been received.
        with open(state, mode='r') as file:
            IRStatus = json.load(file)

        # Note: this call will block (hang) until an IR code has been received.
        with open(filen, mode='r') as file:
            IRCode = json.load(file)

        # Note: this call will block (hang) until an IR code has been received.
        with open(bright, mode='r') as file:
            IRBright = json.load(file)

        stepssent = 0
        sleepx = ((60*(60-dnm))-dns)
        
        # transmit the recorded signal back to the IR Toy
        pIRT.transmit(IRStatus)
        pIRT.transmit(IRCode)
        if dnhold != dnh:
            for i in range(steps):
                pIRT.transmit(IRBright)
                time.sleep(0.25)
                stepssent += 1
                dnhold = dnh
                
    #Print a message telling the user that the signal was repeated, and read it back
    #print('[{:04,d}'.format(run),']',' Sent signal: ',state,' + ',filen,' + [',stepssent,'] ',bright, ' at ',dnh,':',dnm,':',dns,' | ',dny,'-',dnn,'-',dnd,' |', sep="")
    print('[{:04,d}'.format(run),']',' Sent signal: ',state,' + ',filen,' + [',stepssent,'] ',bright, sep="")
    print('[{:04,d}'.format(run),']',' Sleeping ',sleepx//60,'m',sleepx%60,'s...', sep="")
    print(footer_end)
    time.sleep(sleepx)
    run += 1
#And back around we go!
