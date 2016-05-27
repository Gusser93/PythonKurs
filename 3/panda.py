import numpy as np
import matplotlib.pyplot as plt
import pandas as pa


def acc(data, class_attr):
    return float(sum(data[class_attr] == data["prediction"]))/float(data.shape[0])


def predict(t, data, attr1_name, attr2_name, pos, neg):
    threshold = t
    dft = data
    dft.loc[dft[attr1_name] > threshold, "prediction"] = pos
    dft.loc[dft[attr1_name] <= threshold, "prediction"] = neg

    return dft

n = 100
N = 1000
np.random.seed(1481)
x = np.random.normal(0, 0.5, N)
y = np.random.normal(0, 0.5, N)
# color = ["r" if -0.5 <= i <= 0.5 and -0.5 <= j <= 0.5 else "b" for i in x for j in y]
color = []
for i in range(N):
    if -0.5 <= x[i] <= 0.5 and -0.5 <= y[i] <= 0.5:
        color.append("r")
    else:
        color.append("b")

df = pa.DataFrame([x, y, color], ["x", "y", "color"]).transpose()
df["prediction"] = "NA"
accu = []
x_min = min(x)
x_max = max(x)
dx = (x_max - x_min) / n
x_acc = np.arange(x_min, x_max, dx)
best_t = 0
best_accu = 0

for i in x_acc:
    temp = predict(i, df, "x", "y", "r", "b")
    accuracy = acc(temp, "color")
    if max([-1] + accu) < accuracy:
        best_t = i
        best_accu = accuracy
    accu.append(accuracy)


print best_t
print best_accu
print predict(best_t, df, "x", "y", "r", "b")
plt.figure(1)
plt.plot(df[df.color == "r"].x, df[df.color == "r"].y, "ro")
plt.plot(df[df.color == "b"].x, df[df.color == "b"].y, "bo")
plt.plot([-0.5, -0.5], [-0.5, 0.5], "k-")
plt.plot([0.5, 0.5], [-0.5, 0.5], "k-")
plt.plot([-0.5, 0.5], [-0.5, -0.5], "k-")
plt.plot([0.5, -0.5], [0.5, 0.5], "k-")
plt.figure(2)
# plt.plot(x_acc, accu, "ko")
plt.plot(x_acc, accu, "k-")
plt.show()


