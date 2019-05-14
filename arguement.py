import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# 获取txt文件中的数据集，并将属性与标签分开
def get_dataset():
    data = np.loadtxt('./breast.txt')
    label = data[:,-1]
    data = np.delete(data,-1,axis=1)
    return data,label


def get_distance(p1,p2):
    dist = np.sqrt(np.sum(np.square(p1 - p2)))
    return dist


def get_distance_matrix(dataset):
    dist_matrix = []
    for i in range(len(dataset)):
        dist_list = []
        for j in range(len(dataset)):
            if i != j:
                dist_list.append(get_distance(dataset[i], dataset[j]))
        dist_list.sort()
        dist_matrix.append(dist_list)
    return np.array(dist_matrix)


def draw_scaatter_diagram(k_distancelist):
    plt.figure()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.scatter([i for i in range(len(k_distancelist))], np.sort(k_distancelist))
    plt.show()


# 观察k距离的矩阵得到k值
k = 120
data, label = get_dataset()
matrix = get_distance_matrix(data)
draw_scaatter_diagram(matrix[:,k-1])