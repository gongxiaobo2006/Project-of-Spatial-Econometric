import numpy as np
from openpyxl import load_workbook
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
longtitudeList = []
latitudeList = []
prpList = []
book = load_workbook('dongguan.xlsx')
sheet1 = book["经纬度"]
sheet2 = book["data"]
for i in range(1,34):
    lo = sheet1["B{}".format(i)].value
    la = sheet1["C{}".format(i)].value
    density = sheet2["H{}".format(i+1)].value
    longtitudeList.append(lo)
    latitudeList.append(la)
    prpList.append(density)
X = np.array(longtitudeList)
Y = np.array(latitudeList)
prpArray = np.array(prpList)
x = np.column_stack((X,X**0.5,X**2,X**3,Y,Y**0.5,Y**2,Y**3,X*Y,(X*Y)**0.5))
model = sm.OLS(prpArray,sm.add_constant(x))
results = model.fit()
c,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10 = results.params[0],results.params[1],results.params[2],results.params[3],results.params[4],results.params[5],results.params[6],results.params[7],results.params[8],results.params[9],results.params[10]
X1 = np.arange(113.6,114.2,0.01)
X2 = np.arange(22.75,23.10,0.01)
X1,X2 = np.meshgrid(X1,X2)
Z = c+a1*X1+a2*(X1**0.5)+a3*(X1**2)+a4*(X1**3)+a5*X2+a6*(X2**0.5)+a7*(X2**2)+a8*(X2**3)+a9*X1*X2+a10*((X1*X2)**0.5)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X1,X2,Z)
plt.savefig('常住人口密度.png',dpi=300)
plt.show()
