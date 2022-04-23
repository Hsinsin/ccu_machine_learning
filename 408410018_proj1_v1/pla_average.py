import numpy as np
import matplotlib.pyplot as plt
from make_samples import make_samples
from pla import pla
from pla import check_error

if __name__ == '__main__':
    m, b = 4, 5
    n_points = 50
    pos_num = int(n_points / 2)
    t_total = 0
    for j in range(3):
        x_coors, y_coors, labels = make_samples(m, b, n_points)

        dataset = []
        for i in range(len(x_coors)):
            dataset.append([(1, x_coors[i], y_coors[i]), labels[i]])

        w, t = pla(dataset)
        print("Iteration %d = " % j, t)
        
        t_total += t
        plt.subplot(3, 1, j+1)
        ps = [v[0] for v in dataset]
        plt.plot([v[1] for v in ps[:pos_num]], [v[2] for v in ps[:pos_num]], 'o', color='blue') 
        plt.plot([v[1] for v in ps[pos_num:]], [v[2] for v in ps[pos_num:]], 'o', color='red')
        x = np.arange(n_points + 1)
        y = -((w[1] * x + w[0]) / w[2])
        plt.plot(x, y)

    t_avg = t_total / 3
    print("Average isterations = ", t_avg)
    plt.title("Pocket %s" % str(j+1), {'fontsize':18})
    plt.show()
    
    

