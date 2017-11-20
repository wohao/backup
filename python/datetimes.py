from datetime import datetime
dt = datetime(2015,6,21,12,30)
print(dt)

d = dt.timestamp()

print(datetime.fromtimestamp(d))

print(datetime.now().strftime("%a,%b %d %H:%M"))

from collections import namedtuple

point = namedtuple('Point',['x','y'])

p = point(1,2)

print(p.x)

print(isinstance(p,point))