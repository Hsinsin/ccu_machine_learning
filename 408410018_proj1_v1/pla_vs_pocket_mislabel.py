import numpy as np
import matplotlib.pyplot as plt
from make_samples import make_samples
from pocket import pocket
from pocket import cal_accurancy
import time

def pla(dataset):
    t = 0
    w = np.zeros(3)
    while check_error(w, dataset) is not None:
        x, label = check_error(w, dataset)
        w += label * x
        t += 1        
    return w, t

def check_error(w, dataset):
    result = None
    for x, label in dataset:
        x = np.array(x)
        if int(np.sign(w.dot(x))) != label:
            result =  x, label            
    return result

def _wrong_label(dataset):
    for i in range(50):
        dataset[i][1] = -1
        dataset[i+1000][1] = 1
    return dataset

if __name__ == '__main__':
    m, b = 4, 5
    n_points = 1000
    pos_num = int(n_points / 2)
    iteration = 500
    x_coors, y_coors, labels = make_samples(m, b, n_points)

    dataset = []
    for i in range(len(x_coors)):
        dataset.append([(1, x_coors[i], y_coors[i]), labels[i]])

    dataset = _wrong_label(dataset)

    pocket_start = time.time()
    w_pocket, t_pocket = pocket(dataset, iteration)
    pocket_end = time.time()

    ps = [v[0] for v in dataset]
    plt.plot([v[1] for v in ps[49:pos_num]], [v[2] for v in ps[49:pos_num]], 'o', color='blue') 
    plt.plot([v[1] for v in ps[pos_num + 49:]], [v[2] for v in ps[pos_num + 49:]], 'o', color='red')
    plt.plot([v[1] for v in ps[:49]], [v[2] for v in ps[0:49]], 'o', color='red') 
    plt.plot([v[1] for v in ps[pos_num:pos_num + 49]], [v[2] for v in ps[pos_num:pos_num + 49]], 'o', color='blue')
    x_pocket = np.arange(n_points + 1)
    y_pocket = -((w_pocket[1] * x_pocket + w_pocket[0]) / w_pocket[2])
    plt.plot(x_pocket, y_pocket, color = 'green')
    plt.title("Pocket", {'fontsize':18})

    accurancy = cal_accurancy(w, dataset) / n_points
    
    if t_pocket != iteration:
        print("Iteration of the pocket algorithm = ", t_pocket)
    else:
        print("Pocket algorithm overflow!!!")

    print("Running time of the pocket algorithm = ", pocket_end - pocket_start)
    print("accurancy = ", accurancy)
    plt.show()

   


