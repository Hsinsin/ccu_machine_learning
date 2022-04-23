import numpy as np
import matplotlib.pyplot as plt
from make_samples import make_samples
from pla import check_error

def pocket(dataset, iteration):
    t = 0
    w, tmp_w = np.zeros(3), np.zeros(3)
    while check_error(w, dataset) is not None:
        x, label = check_error(w, dataset)
        tmp_w += label * x
        if cal_accurancy(tmp_w, dataset) > cal_accurancy(w, dataset):
            w = tmp_w
        t += 1
        if t >= iteration:
            break
    return w, t

def cal_accurancy(w, dataset):
    a = 0
    for x, label in dataset:
        if int(np.sign(w.dot(x))) == label:
            a += 1
    return a

if __name__ == '__main__':
    m, b = 4, 5
    n_points = 50
    iteration = 500
    x_coors, y_coors, labels = make_samples(m, b, n_points)

    dataset = []
    for i in range(len(x_coors)):
        dataset.append([(1, x_coors[i], y_coors[i]), labels[i]])

    w, t = pocket(dataset, iteration)
    if t != iteration:
        print("Iteration of the pocket algorithm = ", t)
    else:
        print("Pocket algorithm overflow!!!")

    ps = [v[0] for v in dataset]
    plt.plot([v[1] for v in ps[:25]], [v[2] for v in ps[:25]], 'o', color='blue') 
    plt.plot([v[1] for v in ps[25:]], [v[2] for v in ps[25:]], 'o', color='red')
    x = np.arange(n_points + 1)
    y = -((w[1] * x + w[0]) / w[2])
    plt.plot(x, y)
    accurancy = cal_accurancy(w, dataset) / n_points
    print(accurancy)
    plt.title("POCKET", {'fontsize': 18})
    plt.show()
    
    
