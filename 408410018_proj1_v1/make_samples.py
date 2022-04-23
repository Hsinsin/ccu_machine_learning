import numpy as np
import matplotlib.pyplot as plt

def make_samples(m, b, n_points):
    x_coors, y_coors, labels = np.array([]), np.array([]), np.array([])
    for i in range(n_points):
        tmp_x = np.random.randint(0, n_points)
        r = np.random.randint(1, n_points)
        tmp_y = m * tmp_x + b # get the dot(tmp_x, tmp_y)
        
        if i < n_points/2 : # get positive, negative. r is deviation.
            tmp_y = m * tmp_x + b + r
            labels = np.append(labels, 1)
        else:
            tmp_y = m * tmp_x + b - r
            labels = np.append(labels, -1)
    
        x_coors = np.append(x_coors, tmp_x)
        y_coors = np.append(y_coors, tmp_y)
    
    return x_coors, y_coors, labels

def print_plot(pos_num, x_coors, y_coors):
    plt.plot(x_coors[:pos_num], y_coors[:pos_num], 'o', color='blue') 
    plt.plot(x_coors[pos_num:], y_coors[pos_num:], 'o', color='red')
    plt.show()

if __name__ == '__main__':
    # y = mx + b
    m, b = 4, 17
    # samples' number
    n_points = 30
    
    pos_num = int(n_points/2)
    x = np.arange(n_points + 1)
    y = m * x + b
    plt.plot(x, y)
    x_coors, y_coors, labels = make_samples(m, b, n_points)
    
    plt.title("Sample", {'fontsize':15})
    print_plot(pos_num, x_coors, y_coors)

