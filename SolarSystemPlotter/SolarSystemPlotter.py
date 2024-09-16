from skyfield.api import load
from skyfield.framelib import ecliptic_frame
import matplotlib.pyplot as plt

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

solarSysObjects = [sun, mercury, venus, earth, mars,
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
labels = ['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
dists = []
for o in solarSysObjects:
    lat, lon, distance = getEclipticPos(o)
    
    xs.append(lat.degrees)
    ys.append(lon.degrees)
    dists.append(distance.au)
    
plt.scatter(xs, ys)
plt.show()