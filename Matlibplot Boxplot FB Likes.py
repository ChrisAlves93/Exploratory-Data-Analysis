import matplotlib.pyplot as plt

#Facebook Likes

data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,33,36,37,38,41,42,45,47,51,56,58,60,64,103,144,146,372]

plt.boxplot(data)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Facebook Data Set Box Chart")

plt.show()