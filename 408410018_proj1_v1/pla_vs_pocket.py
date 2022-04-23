import numpy as np
import matplotlib.pyplot as plt
from make_samples import make_samples
#from pla import pla
#from pla import check_error
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

if __name__ == '__main__':
    m, b = 4, 5
    n_points = 1000
    pos_num = int(n_points / 2)
    iteration = 500
    x_coors, y_coors, labels = make_samples(m, b, n_points)

    dataset = []
    for i in range(len(x_coors)):
        dataset.append([(1, x_coors[i], y_coors[i]), labels[i]])

    pla_start = time.time()
    w_pla, t_pla = pla(dataset)
    pla_end = time.time()

    pocket_start = time.time()
    w_pocket, t_pocket = pocket(dataset, iteration)
    pocket_end = time.time()

    print("Iteration of PLA = ", t_pla)
    if t_pocket != iteration:
        print("Iteration of the pocket algorithm = ", t_pocket)
    else:
        print("Pocket algorithm overflow!!!")

    print("Running time of PLA = ", pla_end - pla_start)
    print("Running time of the pocket algorithm = ", pocket_end - pocket_start)

    plt.subplot(2, 1, 1)

    ps = [v[0] for v in dataset]
    plt.plot([v[1] for v in ps[:pos_num]], [v[2] for v in ps[:pos_num]], 'o', color='blue') 
    plt.plot([v[1] for v in ps[pos_num:]], [v[2] for v in ps[pos_num:]], 'o', color='red')
    x_pla = np.arange(n_points + 1)
    y_pla = -((w_pla[1] * x_pla + w_pla[0]) / w_pla[2])
    plt.plot(x_pla, y_pla)
    plt.title("PLA", {'fontsize':18})

    plt.subplot(2, 1, 2)

    ps = [v[0] for v in dataset]
    plt.plot([v[1] for v in ps[:pos_num]], [v[2] for v in ps[:pos_num]], 'o', color='blue') 
    plt.plot([v[1] for v in ps[pos_num:]], [v[2] for v in ps[pos_num:]], 'o', color='red')
    x_pocket = np.arange(n_points + 1)
    y_pocket = -((w_pocket[1] * x_pocket + w_pocket[0]) / w_pocket[2])
    plt.plot(x_pocket, y_pocket)
    plt.title("Pocket", {'fontsize':18})
    plt.show()
    
    
    
    
