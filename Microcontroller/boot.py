# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine #uncomment
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc #uncomment
#import webrepl
#webrepl.start()
gc.collect() #uncomment

#import main #comment