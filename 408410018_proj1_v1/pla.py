import numpy as np
import matplotlib.pyplot as plt
from make_samples import make_samples

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
    n_points = 50
    pos_num = int(n_points / 2)
    x_coors, y_coors, labels = make_samples(m, b, n_points)
    
    dataset = []
    for i in range(len(x_coors)):
        dataset.append([(1, x_coors[i], y_coors[i]), labels[i]])

    w, t = pla(dataset)
    print("Iteration = ", t)
    ps = [v[0] for v in dataset]
    plt.plot([v[1] for v in ps[:pos_num]], [v[2] for v in ps[:pos_num]], 'o', color='blue') 
    plt.plot([v[1] for v in ps[pos_num:]], [v[2] for v in ps[pos_num:]], 'o', color='red')
    x = np.arange(n_points + 1)
    y = -((w[1] * x + w[0]) / w[2])
    plt.plot(x, y)
    plt.title("PLA", {'fontsize':18})
    plt.show()


