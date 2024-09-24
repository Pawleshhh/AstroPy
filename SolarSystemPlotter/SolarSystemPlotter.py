from skyfield.api import load
from skyfield.framelib import ecliptic_frame
import matplotlib.pyplot as plt
import math as m

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Load the JPL ephemeris DE421 (covers 1900-2050).
solarSysObjects = load('de421.bsp')

sun = solarSysObjects['sun']
mercury = solarSysObjects['mercury']
venus = solarSysObjects['venus']
earth = solarSysObjects['earth']
mars = solarSysObjects['mars']
jupiter = solarSysObjects['jupiter barycenter']
saturn = solarSysObjects['saturn barycenter']
uranus = solarSysObjects['uranus barycenter']
neptun = solarSysObjects['neptune barycenter']

solarSysObjects = [mercury, venus, earth, mars,
           jupiter, saturn, uranus, neptun]

def getPosition(object, time = None):
    if (time is None):
        return sun.at(t).observe(object)
    
    return sun.at(time).observe(object)

def getCartesianPosition(eclipticPos):
    return eclipticPos.frame_xyz(ecliptic_frame).au

def getEclipticPos(object, time = None):
    pos = getPosition(object, time)
    return pos.frame_latlon(ecliptic_frame)

xs = []
ys = []
figure, axes = plt.subplots()

for o in solarSysObjects:
    lat, lon, distance = getEclipticPos(o)

    x = distance.au * m.cos(lon.radians)
    y = distance.au * m.sin(lon.radians)
    
    Drawing_uncolored_circle = plt.Circle((0, 0),
                                        distance.au,
                                        fill = False)
    
    axes.set_aspect(1)
    axes.add_patch(Drawing_uncolored_circle)
    
    plt.scatter(x, y)
    
 
plt.show()