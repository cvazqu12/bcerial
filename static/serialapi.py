import serial
import time
from static import ubersmithapi

def cerial():
    ser =serial.Serial('/dev/ttyUSB0', 115200) #Initialize the RS232 Connection

    print(" ")
    print("I will use the following:")
    print(" ")
    print("IP="+ubersmithapi.ipmi_address)
    print("Subnet="+ubersmithapi.subnet)
    print("Gateway="+ubersmithapi.gateway)
    print(" ")
    
    # These are the steps
    command_list = [
    b'map -r\r',    # Map out the Filesystems
    b'fs0:\r',      # Select FS0:
    b'IPMICFG.efi\r',   #Initialize IPMICFG.efi
    b'IPMICFG -m '+ubersmithapi.ipmi_address.encode('utf-8')+b'\r', #Requires 9-10 seconds
    b'IPMICFG -k '+ubersmithapi.subnet.encode('utf-8')+b'\r', #Requires 9-10 seconds
    b'IPMICFG -g '+ubersmithapi.gateway.encode('utf-8')+b'\r', #Requires 9-10 seconds
    ]

    """
    Since the user will not see what's happening on the console screen, 
    these prints below can at least show where the program is at in each step of the process.
    """
    
    command_print_list = [
        "Mapping...",
        "Filesysteming...",
        "Initializing...",
        "IPMI-ing...",
        "Subnetting...",
        "Gatwaying...",
    ]

    # Tracking progress in While Loop
    command_print_list_index = 0
    command_list_index = 0

    while True:
        ser.reset_input_buffer()
        ser.write(command_list[command_list_index])
        print(command_print_list[command_print_list_index])

        #Ultimately, this is a temporary hard-code fix until I can figure how to read responses correctly.
        if command_list_index >= 3:
            # IP Configuration takes slightly less than 10 seconds.
            time.sleep(10)
        else:
            # This allows for a speedy process for the first three commands.
            time.sleep(1)


        print("Done") 
        command_list_index += 1
        command_print_list_index += 1
        time.sleep(0.01) #Allows to print "Done" before going on to next command

        # When all steps are complete:
        if command_list_index >= len(command_list):
            break

    ser.write(b'reset\r') #Restart the computer to save changes
    ser.close() # Terminate the RS232 Connection
    

cerial()

