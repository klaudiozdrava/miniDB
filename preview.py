import matplotlib.pyplot as plt
import os
import sys

def preview(dirname='dbdata', plot=False):
    labels = [name for name in os.listdir(dirname) if os.path.isdir(dirname+'/'+name)]
    sizes = []

    for db in labels:
        total_size = 0
        start_path = db
        for path, dirs, files in os.walk(dirname+'/'+start_path):
            for f in files:
                fp = os.path.join(path, f)
                total_size += os.path.getsize(fp)
        sizes.append(total_size)

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)

    plt.title('Total DB Size Distribution', fontsize=18)

    total_db = sum(sizes)
    plt.annotate('Total size', xy=(-0.29, -0.0), size=16, color='darkred')
    plt.annotate(str(int(round(total_db/1e6)))+' MB', xy=(-0.18,-0.15), size=15, color='#d62728')

    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.tight_layout()

    if plot:
        plt.savefig(plot)
    else:
        plt.show()

if __name__ == '__main__':
    preview(dirname=str(sys.argv[1]))