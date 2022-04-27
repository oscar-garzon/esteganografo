# LSB Esteganógrafo

Este repositorio contiene el segundo proyecto para la clase de Modelado y Programación de la Fac. de Ciencias de la UNAM.


## Descripción

Se tiene que realizar un esteganógrafo. El cual va tomar un texto y lo oculta en el arreglo de una imagen. El punto clave es que el esteganógrafo puede develar el texto oculto en la imagen.


### Correr programa

Despues de desempacar la carpeta Tarea2 te posicionas en la carpeta lsb_steganography/
Las imágenes tienen que estar en la carpeta lsb_steganography/textos.
Los textos tienen que estar en la carpeta lsb_steganography/imagenes.
El nombre de la imagen y del texto en la línea de llamada es el nombre solo. Es decir, sin incluir lsb_steganography/textos o lsb_steganography/imagenes.

```
$ cd lsb_steganography/

Ocultar:
$ python src/main.py h [archivo con texto(.txt) a ocultar] [imagen(.png)] [nombre de imagen con texto a ocultar (.png)]

Develar:
$ python src/main.py u [imagen(.png) con texto oculto] [nombre de archivo(.txt) para guardar el texto]

```

### Correr todos los tests
```
$ python -m test
```
