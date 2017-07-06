# Instalação do OpenCV

A maneira mais fácil de instalar o OpenCV é através do Anaconda, que pode ser baixado em https://www.continuum.io/downloads#windows, após baixado e instalado, podem ser efetuadas as instalações do Phyton, através do comando:

```
conda install python=3.5
```

E do OpenCV, através do comando:

```
conda install -c menpo opencv3
```

Para testar a instalação basta criar o arquivo `main.py` e executar o comando `python main.py`.

```python
import cv2

print(cv2.__version__)
```

# Arquivos de treinamento

Os arquivos de treinamento contém os padrões para reconhecimento de objetos, no [diretório do OpenCV](https://github.com/opencv/opencv/tree/master/data/haarcascades) existem arquivos de treinamento pré-cadastrados.

# Resultados dos testes

Foram efetuados os testes utilizando os arquivos de treinamento pre cadastrados `haarcascade_fullbody.xml` e `haarcascade_upperbody.xml`, sendo que foram encontrados muitos falsos positivos conforme imagens `Test1.PNG` e `Test2.PNG`.