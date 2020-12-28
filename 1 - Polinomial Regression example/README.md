### Polinomial Regression example
###### by GIOVANNI PERON - friday, 11 october 2019, 19:32

I tried to write a script with another dataset, applying the polinomial regression method. 

I attach the script and the used dataset found on kaggle (https://www.kaggle.com/murderaccountability/homicide-reports), and then converted into a csv file in order to obtain data adequate for the script's purpose.

The script is executable through the command
'''
python3 PolRegExample.py <alpha>
'''
specifying instead of <alpha> the desidered parameter's value.

You will get a chart where it will be possible to notice the behavior of the applied method when the polinomial grade changes. In particular I noticed:

- increasing the polinomial's grade, it will better approximate the data trend;  

- increasing alpha the curve become simplier, so the trend of simple data is approximated better, decreasing alpha the curve tend to represent also values that are out of the average but the general approximation become worst.

Hoping all that could be useful, regards.

Giovanni

---

### Esempio Regressione Polinomiale
###### di GIOVANNI PERON - venerdì, 11 ottobre 2019, 19:32
 
Ho provato a scrivere uno script con un altro dataset, applicando il metodo della regressione polinomiale.

Allego lo script e il dataset utilizzato prelevato da kaggle (https://www.kaggle.com/murderaccountability/homicide-reports), e successivamente trasformato in un file csv per ottenere dei dati che potessero prestarsi allo scopo dello script.

Lo script è eseguibile tramite il comando:
'''
python3 PolRegExample.py <alpha>
'''
specificando al posto di <alpha> il valore desiderato per il parametro.

Si otterà un grafico dove sarà possibile notare il comportamento del metodo applicato al variare del grado del polinomio. In particolare ho notato:

- aumentando il grado del polinomio questo approssimerà in modo migliore l'andamento dei dati;

- aumentando alpha la curva viene semplificata viene seguito meglio l'andamento dei dati più semplici, diminuendolo la curva tenta di rappresentare anche valori al di fuori della media ma l'approssimazione generale peggiora.

Spero che tutto ciò possa essere utile.

Giovanni
