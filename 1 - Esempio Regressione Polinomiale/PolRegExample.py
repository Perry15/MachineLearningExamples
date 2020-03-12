# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sys import argv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def data_getter():
    with open("mydataset.csv", "r") as file:
        csv = pd.read_csv(file, sep=";")
    return [[i] for i in csv["x"]], [[i] for i in csv["y"]]

def main(alpha: float):
    x_all,y_all = data_getter() 
    data = pd.DataFrame(np.column_stack([y_all,x_all]),columns=['y','x']) # creo un dataframe

    for i in range(2,6): # modifico il dataframe creando una matrice con righe del tipo [x,x^2,...,x^degree]
        data['x^%d'%i] = data['x']**i
    
    x_train, x_test, y_train, y_test = train_test_split(data.iloc[:,1:6], data['y'], test_size=0.2, random_state=1)
    #riordino in base alle x per poter poi fare il plot
    train=pd.concat([y_train,x_train],axis=1).sort_values(by=['x'])
    test=pd.concat([y_test,x_test],axis=1).sort_values(by=['x'])
    #stampo i punti di test
    plt.scatter(test['x'], test['y'],  color='black', s=5, marker='o', label="test points")
    colors = ['blue', 'orange', 'green', 'purple', 'red']
    #stampo diversi tentativi variando il grado
    for i, degree in enumerate([1,2,3,4,5]):
        model = make_pipeline(PolynomialFeatures(degree=degree), Ridge(alpha=alpha))
        model.fit(train.iloc[:,1:degree+1], train['y']) 
        y_p=model.predict(test.iloc[:,1:degree+1])
        plt.plot(test['x'], y_p, color=colors[i], linewidth=2, label="degree %d" % degree)
    plt.legend(loc='lower left')
    plt.show()

if __name__ == "__main__":
    main(float(argv[1]))
