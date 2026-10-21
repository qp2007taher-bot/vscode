BAT  =25    #battery
wifi =False
MoDa =False #mobileDate

if BAT >= 15 and wifi :

    WaYo = True
    WoYoRe = "All conditions met."
    
elif BAT < 15 and wifi :

    WaYo = False
    WoYoRe = f"Battery level is low ({battery}%). Minimum required is 15%."

else :

    WaYo = False
    WoYoRe = "Not connected to Wi-Fi."    

if BAT >= 50 and wifi :

    LoSe = True
    LoSeRe = "All conditions met for a long session."
    
elif BAT < 50 and wifi :

    LoSe = False
    LoSeRe = f"Battery ({battery}%) is too low for a long session (minimum 50%)."

else :
 
    LoSe = False
    LoSeRe = "No internet connection available (Wi-Fi or Mobile Data)."

print("=== Usage Status Report ===")
print(f"Watch YouTube : {WaYo} | Reason: {WoYoRe}")
print(f"Long Session  : {LoSe} | Reason: {LoSeRe}")
