import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ["a","b","c"]
    values = [200,34,120]
    
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    #plt.show() no vamos solo a motrar 
    plt.savefig("pie.png")
    plt.close()