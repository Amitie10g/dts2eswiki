# dts2eswiki
 Este proyecto pretende crear una serie de códigos para convertir contenidos com la plantilla [{{dts}}](https://en.wikipedia.org/wiki/Template:Dts] de la [Wikipedia en inglés](https://en.wikipedia.org) (y otras) a [Wikipedia en español](https://es.wikipedia.org).
 
Por el momento, solo tengo un script en Python de uso local, pero prefiero dejar esa tarea a un bot ya existente en Wikipedia en español, explinado en el Café cómo proceder. Pienso portar el código a Powershell.

## Requisitos
* Python3
* [timestring](https://pypi.org/project/timestring/)

## Uso
``python dts.eswiki.py data``

donde "data" es un archivo que contiene el código que queremos analizar. Una vez ejecutado, el programa sobreescribe el archivo dado, y se puede volver a pegar en el artículo a arreglar.
