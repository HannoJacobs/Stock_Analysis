from matplotlib import pylab
import numpy
import dateutil
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

y=[129.000, 128.000, 140.000, 150.000]
xStrings=["1/2018", "2/2018", "3/2018", "4/2018"]

# Convert strings to datetime objects,and then to Matplotlib date numbers
dates = [dateutil.parser.parse(x) for x in xStrings]
x = mdates.date2num(dates)

# plot the data itself
pylab.plot(x,y,'o')

# calc the trendline (it is simply a linear fitting)
z = numpy.polyfit(x, y, 1)
p = numpy.poly1d(z)

polyX = numpy.linspace(x.min(), x.max(), 100)
pylab.plot(polyX,p(polyX),"r")
# the line equation:
print("y=%.6fx+(%.6f)"%(z[0],z[1]))

# Show X-axis major tick marks as dates
loc= mdates.AutoDateLocator()
plt.gca().xaxis.set_major_locator(loc)
plt.gca().xaxis.set_major_formatter(mdates.AutoDateFormatter(loc))
plt.gcf().autofmt_xdate()

pylab.show()