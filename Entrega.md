---
title: "Sistema de diseño Fractal - Ignacio Pardo"
author: "Ignacio Pardo"
output: pdf_document
---

# Sistema de diseño Fractal - Ignacio Pardo

## Links

[Repo de GitHub: https://github.com/IgnacioPardo/dataviz_apps](https://github.com/IgnacioPardo/dataviz_apps)

[Visualización y Demo Web: https://ignaciopardo-dataviz-apps-visualizer-x6avik.streamlit.app/#demo](https://ignaciopardo-dataviz-apps-visualizer-x6avik.streamlit.app/#demo)

## Objetivos

- Aprender a ver nuestro entorno
- Observar, recopilar, dibujar
- Desarrollar un lenguaje visual propio

\newpage

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

\newpage

## Desarrollo de un primer sistema de diseño a mano

### Referencia

![Draw Ref]("draw_ref.png")

\newpage

### Resultado

![Draw]("draw.png")

\newpage

## Un sistema de diseño parametrizado general

### Idea: Fractales

#### Mandelbrot Set

La idea de tener un sistema de diseño parametrizado es que podamos generar distintas imágenes a partir de distintos valores.

Para ello una primera idea fue el Mandelbrot Set, un fractal que se genera a partir de la siguiente fórmula:

$$
z_{n+1} = z_n^2 + c
$$

donde $z_0 = 0$ y $c$ es un número complejo.

![Mandelbrot Set]("mandelbrot.png")

Entonces podemos generar distintas imágenes a partir de distintos valores de $c$, y combinar otros factores, como el color de la imagen o la resolución del fractal para aprovechar en nuestro sistema de diseño.

![mandelbrot_sizes]("mandelbrot_sizes.png")

\newpage

A partir de esto plantee un sistema de diseño parametrizado que nos permita generar distintas imágenes a partir de distintos valores de $C$.

![mandelbrot_design]("mandelbrot_design.png")

\newpage

### Sistema de Referencia para esta primera idea

#### El tamaño de la app afecta el tamaño del fractal

![mandelbrot_reference_size]("mandelbrot_reference_size.png")

####  La frecuencia de uso de la app afecta la cantidad de iteraciones del fractal

![mandelbrot_reference_use_frecuency]("mandelbrot_reference_use_frecuency.png")

####  El "aprecio" por la app afecta el color del fractal

![mandelbrot_reference_likeability]("mandelbrot_reference_likeability.png")

\newpage

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

\newpage

### Resultado: Sistema de diseño basado en fractales

![julia_design]("julia_design.png")

\newpage

### Sistema de diseño final: Referencias

**Clasificación de apps** 
El tipo de app afecta el número complejo que se usa para generar el fractal

![]("julia_types.png")

**Frecuencia de uso** 
La frecuencia de uso de la app afecta la cantidad de iteraciones del fractal

![]("julia_use_frecuency.png")

**Tamaño y aprecio de la app** 
El tamaño y el aprecio de la app afectan el tamaño de la imagen, que se puede interpretar como la resolución del fractal en si.

![]("julia_size.png")

**Aprecio de la app** 
El aprecio de la app ademas determina el mapa de colores que se usa para generar el fractal.

![]("julia_likeability.png")

Finalmente, el sistema de diseño parametrizado desarrollado se puede expandir para infinitos valores para generar cualquier fractal del Julia Set para representar cualquier tipo de app.

Arme una [demo aca](https://ignaciopardo-dataviz-apps-visualizer-x6avik.streamlit.app/#demo) para que puedan probar el sistema de diseño generando distintos fractales para distintas apps.

[Link alternativo](https://datavizapps.ignaciopardo.repl.co/#demo)
