# Spam_crasher
A library made for stress testing a system based on specific circumstances.
# Description
spam crasher is library ment for stress testing different systems with different functions.
The library is in active state ov development and improvement and for now contains 4 basic functions.
# Functions
1. syscrash
    - ment for stressing the system untill it crashes.
    - the 2 required arguments are
        - range: how many times the system should be stressed
        - delay: the timer before launching the process
        - NOTE : you can change the process at any time, just by editing the system process line
1. pyspam
    - ment for stressing the system untill it crashes by opening many python process.
    - the 2 required arguments are
        - range: how many times the system should be stressed
        - delay: the timer before launching the process
        
1. sht
    - ment for shuting down the system with a timer.
    - the 2 required arguments are
        - timer: when to shuttdown the system
        - ost: the system type.
        anything else than linux or windows is considered as invalid argument
        
1. syskill
    - ment for killing the system permanently by deleting its file systems
    - WARNING : THE FUNCTION IS COMENTED SO IF YOU WANT TO USE IT YOU WIL HAVE TO UNCOMENT IT 
    - the 2 required arguments are
        - timer: when to shuttdown the system
        - sys_type: the system type.
        anything else than linux or windows is considered as invalid argument.
        if there is an error such as 'Not existind directory', simply put the path to the system files.
# conclusion
This library is ment for system testing and if you want to use it for bad purposes i am not taking any responsibility for your actions.
Be awared that the libray is getting constant updates and if there is something that isnt ok with the library, please consider comenting.
