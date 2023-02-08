import sys
import ac 
import acsys
import platform
import os

TopSpeed = 0
Top_speed = 0

CurrentSpeed = 0
Current_speed = 0


Units = True


if platform.architecture()[0] == "64bit":
  sysdir = "third_party/stdlib64"
else:
  sysdir = "third_party/stdlib"

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "TopSpeedTracker_lib", sysdir))
os.environ['PATH'] = os.environ['PATH'] + ";."

from third_party.sim_info import info


def acMain(ac_version):
    global Top_speed, Current_speed
    global Top_speed, Current_speed
    global UnitToggle
    appWindow = ac.newApp("Zad Test")
    ac.setSize(appWindow, 200, 200)
    ac.log("This is the log!")
    ac.console("This is the console!")

    Top_speed = ac.addLabel(appWindow, "Top Speed")
    Current_speed = ac.addLabel(appWindow, "Current Speed")


    UnitToggle = ac.addButton(appWindow, "")
    ac.setSize(UnitToggle, 50, 20)
    ac.setPosition(UnitToggle, 10, 100)
    ac.addOnClickedListener(UnitToggle, KPH)
    ac.setBackgroundOpacity(UnitToggle, 0.7)

    UnitToggle2 = ac.addButton(appWindow, "")
    ac.setSize(UnitToggle2, 50, 20)
    ac.setPosition(UnitToggle2, 60, 100)
    ac.addOnClickedListener(UnitToggle2, MPH)
    ac.setBackgroundOpacity(UnitToggle2, 0.7)

    ac.setText(UnitToggle, "KMH")
    ac.setText(UnitToggle2, "MPH")



    ac.setPosition(Top_speed, 10, 30)
    ac.setPosition(Current_speed, 10, 60)
    ac.log(ac.getDriverName(0) + " - " + ac.getCarName(0) + " - " + ac.getTrackName(0) + " " +str(TopSpeed) + " MPH")
    
    return "Top Speed Tracker"
     

    # ac.log(ac.getDriverState(0))

def KPH(*args):
    global Units
    if Units:
      converttoKMH()
    # converttoKMH()
    Units = False


def MPH(*args):
    global Units
    if not Units:
      converttoMPH()
    # converttoMPH()
    Units = True
    
def converttoMPH():
  global TopSpeed

  TopSpeed = round(TopSpeed / 1.609)

def converttoKMH():
  global TopSpeed

  TopSpeed = round(TopSpeed * 1.609)


def acUpdate(deltaT):
    global Top_speed, TopSpeed, Current_speed
    SpeedKMH = ac.getCarState(0, acsys.CS.SpeedKMH)
    SpeedMPH = ac.getCarState(0, acsys.CS.SpeedMPH)
    

    if Units:
      CurrentSpeed = round(SpeedMPH)
      if CurrentSpeed > TopSpeed:
        TopSpeed = CurrentSpeed
    else:
      CurrentSpeed = round(SpeedKMH)
      if CurrentSpeed > TopSpeed:
          TopSpeed = CurrentSpeed
    
    ac.setText(Top_speed, "Top Speed: {speed} {unit}".format(speed = TopSpeed, unit = "MPH" if Units else "KMH"))
    ac.setText(Current_speed, "Current Speed: {speed} {unit}".format(speed = CurrentSpeed, unit = "MPH" if Units else "KMH"))

 
