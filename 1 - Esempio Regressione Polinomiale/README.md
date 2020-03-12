### Esempio Regressione Polinomiale
di GIOVANNI PERON - venerdì, 11 ottobre 2019, 19:32
 
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