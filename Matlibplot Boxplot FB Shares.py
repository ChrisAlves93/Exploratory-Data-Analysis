import matplotlib.pyplot as plt

#Facebook Shares

data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,60,61,63,64,68,70,74,76,77,78,79,80,83,83,84,90,95,97,98,99,102,121,122,123,128]

plt.boxplot(data)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Facebook Data Set Box Chart")

plt.show()