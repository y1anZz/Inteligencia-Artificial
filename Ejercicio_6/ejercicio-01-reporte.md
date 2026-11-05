# Reporte del ejercicio 01: más capas en el perceptrón multicapa

## Configuración

Se prepararon dos copias de las notebooks para comparar las arquitecturas
`4 x 3 x 3` y `4 x 3 x 3 x 3 x 3` sobre Iris:

- sigmoide en todas las capas;
- error MSE;
- SGD con `learning_rate = 0.03`;
- 500 épocas;
- 4 entradas y 3 salidas one-hot.

Archivos de trabajo:

- `Notebooks/04 Multilayer perceptron - ejercicio-01.ipynb`
- `Notebooks/05 Keras - multilayer perceptron - iris - ejercicio-01.ipynb`

## Implementación manual

La corrida profunda usa cuatro matrices de pesos y guarda una activación por
capa durante el forward. El backpropagation calcula el delta de la salida y
recorre las capas restantes desde la salida hacia la entrada:

```text
4 -> 3 -> 3 -> 3 -> 3
```

Los pesos de la capa siguiente se usan para propagar el error hacia atrás,
ignorando su término de bias. La notebook imprime el error inicial y final y
grafica la curva MSE de las 500 épocas.

## Implementación con Keras

La copia de Keras conserva la corrida original con dos capas `Dense(3)` y
agrega una segunda corrida con cuatro capas `Dense(3)`. En ambas se usan
sigmoide, MSE, SGD y 500 épocas. `model.summary()` y `deep_model.summary()`
permiten comprobar la cantidad de capas y parámetros, y la última celda
superpone las dos curvas de pérdida.

## Análisis

La profundidad no garantiza una menor pérdida en este caso. Iris es un
conjunto pequeño y una red `4 x 3 x 3` ya tiene capacidad suficiente; las dos
capas adicionales hacen más difícil la optimización. Además, al apilar
sigmoides, las derivadas pueden ser pequeñas y producir desvanecimiento del
gradiente durante el backpropagation.

Las curvas manual y de Keras pueden diferir aunque tengan la misma topología,
porque sus inicializaciones, orden de actualización, representación de los
pesos y convenciones para calcular el promedio del MSE no tienen que ser
idénticos. Por eso la comparación debe considerar la tendencia y la pérdida
final dentro de cada implementación.

Las celdas de ambas copias imprimen los valores numéricos necesarios para
completar la tabla de resultados después de ejecutar las notebooks en Colab.
También deben conservarse las capturas de las cuatro curvas, los dos
`model.summary()` y el entorno de Colab como evidencia de ejecución.
