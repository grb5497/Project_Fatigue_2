import sys
import matplotlib.pyplot as plt
import numpy as np

def plot_data(input_files,output_files,x_label,y_label):
    print('Plotting data...')
    plt.figure(figsize=(5,7))
    for file in input_files:
        data = np.loadtxt(file,delimiter=',')
        data_label = file[-6:-4]
        plt.plot(data[:,0],data[:,1],label=data_label)
    
    plt.yscale('log')
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(output_files)
    plt.show()
    

if __name__ == '__main__':

    input_files = sys.argv[1:-3]
    output_files = sys.argv[-3]
    x_label = sys.argv[-2]
    y_label = sys.argv[-1]

    plot_data(input_files,output_files,x_label,y_label)