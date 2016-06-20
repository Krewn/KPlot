#  given n Points in spherical cords where m is constant find a new point p 
#  the best meeting place.

# The Ovbious aproach :: Take the mean of the longitudes and the mean of the laditudes.

# This means that if you have 3 people in new york and 2 in sanfransisco you end up meeting
# in the middle of the country.

# The less ovbious aproach:

# Take the spacial average of the points and project that to the surface...

# What does this mean? The east west movment points in the set is no longer represented 
# disproportionatly for small changes in position near the poles.

def method1(plist): # The average way
	lon = sum([x[0] for x in plist])/len(plist)
	lat = sum([x[1] for x in plist])/len(plist)
	return((lon,lat))

	
# fi = 90 - latitude
# theta = longitude

# (radius = 1 earth radius...)

# cart(1,0,0) = sph(1,0,pi/2) = null island = lonlat(0,0)

# x = cos(theta)sin(fi)
# y = sin(theta)sin(fi)
# z = cos(fi) 

# r = (x**2+y**2+z**2)**0.5
# theta = = tan**-1(y/x)
# fi = cos**-1(z/r)

import math as m
def p(d): # Rads -> pis
	return(d if d == 0 else m.pi*(d/180.))

def dp(d): # Pi's to rads
	return(d*180./(m.pi))

def method2(plist): # The other average way, demonstration of the non linearity of longitude latitude.
	x = sum([m.cos(p(-1.*k[0]))*m.sin(p(90.-k[1])) for k in plist])/len(plist)
	y = sum([m.sin(p(-1.*k[0]))*m.sin(p(90.-k[1])) for k in plist])/len(plist)
	z = sum([m.cos(p(90.-k[1])) for k in plist])/len(plist)
	r = (x**2.+y**2.+ z**2.)**0.5
	theta = m.atan(y/x)
	fi = m.acos(z/r)
	latitude = 90-dp(fi)
	longitude = -1.*dp(theta)
	return((longitude,latitude))

def test(plist):
	print "given:"+str(plist)
	print "meetAt:"
	print str(method1(plist))
	print str(method2(plist))
	
#test([(0,0)])
#test([(0,89),(0,0)])
#test([(90,89),(0,0)])

def cordToEuc(lon,lat,r=1.0):
	x = m.cos(p(-1.*lon))*m.sin(p(90.-lat))*r
	y = m.sin(p(-1.*lon))*m.sin(p(90.-lat))*r
	z = m.cos(p(90.-lat))
	return(x,y,z)

def eucToCord(x,y,z):
	r = (x**2.+y**2.+ z**2.)**0.5
	theta = m.atan(y/x)
	fi = m.acos(z/r)
	latitude = 90-dp(fi)
	longitude = -1.*dp(theta)
	return(longitude,latitude)
	

# Notice method 2 accounts for spherical distortion.
