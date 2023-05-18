---
title: "Sistema de diseño Fractal - Ignacio Pardo"
author: "Ignacio Pardo"
date: "`r Sys.Date()`"
output: pdf_document
---

# Sistema de diseño Fractal - Ignacio Pardo

## Links

[Repo de GitHub: https://github.com/IgnacioPardo/dataviz_apps](https://github.com/IgnacioPardo/dataviz_apps)
[Visualización y Demo Web: https://ignaciopardo-dataviz-apps-visualizer-x6avik.streamlit.app/#demo](https://ignaciopardo-dataviz-apps-visualizer-x6avik.streamlit.app/#demo)

## Apps y clasificación

Las aplicaciones que tenés en el celular son una ventana a tu personalidad. ¿Qué dicen sobre vos? 
Estas son 25 aplicaciones que tengo instaladas:

#### Comunication
 - Whatsapp
 - Discord
#### Social
 - Instagram
 - Twitter
 - Pinterest
#### Entertainment
 - Disney+
 - Netflix
 - Youtube
#### Music
 - Spotify
 - YouTube Music
 - GarageBand
#### Sports and Health
 - Adidas
 - SportClub
 - Fitness
 - Salud
#### Identity
 - MercadoPago
 - Mi Argentina
 - ACAMovil
 - Wallet
#### Productivity
 - Arc
 - Drive
 - Figma
 - Github
 - Visual Studio Code
 - Campus Di Tella

## Desarrollo de un pimer sistema de diseño a mano

### Referencia

<img width="669" alt="draw_ref" src="https://user-images.githubusercontent.com/65306107/238806695-d27da066-12c1-485c-87b8-ed53c8af3418.png">

### Resultado

<img width="673" alt="draw" src="https://user-images.githubusercontent.com/65306107/238806769-6046067f-ecfc-4431-a795-14e5af4f4eac.png">

## Un sistema de diseño parametrizado general

### Idea: Fractales

#### Mandelbrot Set

La idea de tener un sistema de diseño parametrizado es que podamos generar distintas imágenes a partir de distintos valores.

Para ello una primera idea fue el Mandelbroth Set, un fractal que se genera a partir de la siguiente fórmula:

$$
z_{n+1} = z_n^2 + c
$$

donde $z_0 = 0$ y $c$ es un número complejo.

![Mandelbrot Set](https://user-images.githubusercontent.com/65306107/238806904-a6db1db9-7a48-43de-9b05-8c8567e39f02.png)

Entonces podemos generar distintas imágenes a partir de distintos valores de $c$, y combinar otros factores, como el color de la imagen o la resolución del fractal para aprovechar en nuestro sistema de diseño.
![mandelbrot_sizes](https://user-images.githubusercontent.com/65306107/238807160-a7888c21-6456-4db7-b140-5fe134eb3345.png)

A partir de esto plantee un sistema de diseño parametrizado que nos permita generar distintas imágenes a partir de distintos valores de $C$.

![mandelbrot_design](https://user-images.githubusercontent.com/65306107/238807263-fee40c31-2fc7-4fec-87de-842964d419b2.png)

#### Sistema de Referencia para esta primera idea

##### El tamaño de la app afecta el tamaño del fractal

![mandelbrot_reference_size](https://user-images.githubusercontent.com/65306107/238807395-ef96d652-d078-4d0f-a187-24639875cda7.png)


##### La frecuencia de uso de la app afecta la cantidad de iteraciones del fractal

![mandelbrot_reference_use_frecuency](https://user-images.githubusercontent.com/65306107/238807719-7ebadf47-45e6-4817-adac-f7a9d5358287.png)

##### El "aprecio" por la app afecta el color del fractal

![mandelbrot_reference_likeability](https://user-images.githubusercontent.com/65306107/238807757-0196437a-857d-4077-958d-fbca8e514606.png)

### Ampliar el sistema de diseño

#### Otros tipos de fractales: Julia Set

El Mandelbrot Set es un ejemplo particular del Julia Set, por lo que además podríamos parametrizar el tipo de fractal que queremos generar.
Un ejemplo de un fractal generado por el Julia Set a partir de $$c = -0.1 + 0.65i$$
Aprovechando entonces el sistema de diseño que ya tenemos, podemos generar distintos fractales en función del tipo de app que queremos representar.

Para ello elegí diferentes números complejos y los asocié a distintos tipos de apps.    
| App | Número Complejo |
| --- | --- |
| Comunication | 0.285 + 0.01i |
| Entertainment | -0.8 + 0.156i |
| Identity | -0.4 + 0.6i |
| Music | -0.1 - 0.732i |
| Productivity | -0.9 + 0i |
| Social | -0.215 - 0.65i |
| Sports and Health | 0.73 - 0.73i |    

De esta forma llegamos a un sistema de diseño parametrizado que nos permite generar distintos fractales en función de distintos tipos de apps.

### Resultado: Sistema de diseño basado en fractales

![julia_design](https://user-images.githubusercontent.com/65306107/238807958-dd857f2d-d73d-4f62-8781-63c7cdd02894.png)

### Sistema de diseño final

#### Referencias

#### Clasificación de apps

El tipo de app afecta el número complejo que se usa para generar el fractal

![julia_types](https://user-images.githubusercontent.com/65306107/238808054-1049a269-1da3-40a1-82fc-af0ee7b55227.png)

##### Frecuencia de uso

La frecuencia de uso de la app afecta la cantidad de iteraciones del fractal

![julia_use_frecuency](https://user-images.githubusercontent.com/65306107/238808091-e33145e5-34f5-4134-abc3-fa8b16244143.png)

##### Tamaño y aprecio de la app

El tamaño y el aprecio de la app afectan el tamaño de la imagen, que se puede interpretar como la resolución del fractal en si.

![julia_size](https://user-images.githubusercontent.com/65306107/238808140-77ac0225-dc28-4e3e-b90c-c5e9a3b92a46.png)

##### Aprecio de la app
El aprecio de la app ademas determina el mapa de colores que se usa para generar el fractal.

![julia_likeability](https://user-images.githubusercontent.com/65306107/238808158-1ec9fb1b-a688-4d9d-a278-5e4f9aa561f1.png)

Finalmente, el sistema de diseño parametrizado desarrollado se puede expandir para infinitos valores para generar cualquier fractal del Julia Set para representar cualquier tipo de app.

Arme una [demo aca](https://ignaciopardo-dataviz-apps-visualizer-x6avik.streamlit.app/#demo)

[Link alternativo](https://datavizapps.ignaciopardo.repl.co/#demo)
