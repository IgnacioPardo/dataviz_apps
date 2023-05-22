import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

st.set_page_config(page_title="Sistema de diseño Fractal", page_icon="🎨", layout="wide")

st.title("Sistema de diseño Fractal - Ignacio Pardo")

intro_tab, mandelbrot_tab, julia_tab, system_tab, demo_tab = st.tabs(
    [
        "Introducción",
        "Fractal Mandelbrot Set",
        "Fractal Julia Set",
        "Design System",
        "Demo",
    ]
)

apps = {
    "Whatsapp": {
        "size": 10,
        "use_frecuency": 10,
        "likeability": 8,
        "type": "Comunication",
    },
    "Discord": {
        "size": 3,
        "use_frecuency": 4,
        "likeability": 4,
        "type": "Comunication",
    },
    "Instagram": {"size": 10, "use_frecuency": 10, "likeability": 8, "type": "Social"},
    "Twitter": {"size": 3, "use_frecuency": 10, "likeability": 9, "type": "Social"},
    "Pinterest": {"size": 3, "use_frecuency": 7, "likeability": 9, "type": "Social"},
    "Disney+": {
        "size": 6,
        "use_frecuency": 7,
        "likeability": 9,
        "type": "Entertainment",
    },
    "Netflix": {
        "size": 8,
        "use_frecuency": 8,
        "likeability": 7,
        "type": "Entertainment",
    },
    "Youtube": {
        "size": 10,
        "use_frecuency": 10,
        "likeability": 10,
        "type": "Entertainment",
    },
    "Spotify": {"size": 10, "use_frecuency": 10, "likeability": 10, "type": "Music"},
    "YouTube Music": {"size": 3, "use_frecuency": 7, "likeability": 9, "type": "Music"},
    "GarageBand": {"size": 3, "use_frecuency": 3, "likeability": 6, "type": "Music"},
    "Adidas": {
        "size": 3,
        "use_frecuency": 3,
        "likeability": 7,
        "type": "Sports and Health",
    },
    "SportClub": {
        "size": 3,
        "use_frecuency": 9,
        "likeability": 7,
        "type": "Sports and Health",
    },
    "Fitness": {
        "size": 2,
        "use_frecuency": 9,
        "likeability": 10,
        "type": "Sports and Health",
    },
    "Salud": {
        "size": 2,
        "use_frecuency": 9,
        "likeability": 10,
        "type": "Sports and Health",
    },
    "MercadoPago": {
        "size": 4,
        "use_frecuency": 8,
        "likeability": 8,
        "type": "Identity",
    },
    "Mi Argentina": {
        "size": 3,
        "use_frecuency": 2,
        "likeability": 0,
        "type": "Identity",
    },
    "ACAMovil": {"size": 3, "use_frecuency": 2, "likeability": 0, "type": "Identity"},
    "Wallet": {"size": 2, "use_frecuency": 8, "likeability": 8, "type": "Identity"},
    "Arc": {"size": 3, "use_frecuency": 10, "likeability": 10, "type": "Productivity"},
    "Drive": {"size": 10, "use_frecuency": 8, "likeability": 8, "type": "Productivity"},
    "Figma": {
        "size": 3,
        "use_frecuency": 10,
        "likeability": 10,
        "type": "Productivity",
    },
    "Github": {
        "size": 3,
        "use_frecuency": 10,
        "likeability": 10,
        "type": "Productivity",
    },
    "Visual Studio Code": {
        "size": 3,
        "use_frecuency": 10,
        "likeability": 10,
        "type": "Productivity",
    },
    "Campus Di Tella": {
        "size": 3,
        "use_frecuency": 6,
        "likeability": 4,
        "type": "Productivity",
    },
}

# Add cmap value based on likeability

# cmaps_dict = {
#     0: "Greys",
#     1: "Greens",
#     2: "YlGn",
#     3: "OrRd",
#     4: "Reds",
#     5: "Oranges",
#     6: "Purples",
#     7: "PuBu",
#     8: "Blues",
#     9: "BuPu",
#     10: "PuRd",
# }

# generator function


def gen_cmap(cmap_name, n):
    cmap = mpl.colormaps[cmap_name]
    for i in range(0, n):
        partition = cmap(np.linspace(0, (i+1)/n, 256//n))
        split_cmap = mpl.colors.ListedColormap(partition, name=f'{cmap_name}_{n}')
        yield split_cmap

# Add cmap value based on likeability


n = 18
cmap_name = 'magma'
cmap_name = 'gnuplot2'
cmaps_dict = {i : cmap for i, cmap in enumerate(gen_cmap(cmap_name, n))}

for app in apps:
    apps[app]['cmap'] = cmaps_dict[apps[app]['likeability'] + 2]

types = set([app["type"] for app in apps.values()])

with intro_tab:

    st.write("## Apps y clasificación")

    """
    Las aplicaciones que tenés en el celular son una ventana a tu personalidad. ¿Qué dicen sobre vos?
    Estas son 25 aplicaciones que tengo instaladas:
    """

    group_by_type = {}

    for app_name, app in apps.items():
        group_by_type.setdefault(app["type"], []).append(app_name)

    cols = st.columns(len(group_by_type))

    for i, (app_type, app_list) in enumerate(group_by_type.items()):

        cols[i].write(f"#### {app_type}")
        subapp_list = "\n - ".join(app_list)
        cols[i].write(f" - {subapp_list}")

    """
        ## Desarrollo de un pimer sistema de diseño a mano

        ### Referencia
        """

    st.image("draw_ref.png")

    """
        ### Resultado
        """
    st.image("draw.png")

    """
    Este sistema de diseño es muy simple, por lo que muchas de las apps resultan en representaciónes similares.
    
    Para expandir esta idea se me ocurrió pensar en un sistema de diseño parametrizado, donde cada app se represente como combinación de sus componentes.
    """

with mandelbrot_tab:
    """
    ## Un sistema de diseño parametrizado general

    """

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Idea: Fractales")
        st.write("#### Mandelbrot Set")
        """

        La idea de tener un sistema de diseño parametrizado es que podamos generar distintas imágenes a partir de distintos valores.

        Para ello una primera idea fue el Mandelbroth Set, un fractal que se genera a partir de la siguiente fórmula:

        $$
        z_{n+1} = z_n^2 + c
        $$

        donde $z_0 = 0$ y $c$ es un número complejo.

        De esta forma podríamos generar distintos fractales a partir de números complejos distintos.
        """
        pass

    # A simple mandelbrot set generator

    def mandelbrot(h, w, maxit=20) -> np.ndarray:
        """Returns an image of the Mandelbrot fractal of size (h,w)."""
        y, x = np.ogrid[-1.4 : 1.4 : h * 1j, -2 : 0.8 : w * 1j]
        c = x + y * 1j
        z = c
        divtime = maxit + np.zeros(z.shape, dtype=int)

        for i in range(maxit):
            z = z**2 + c
            diverge = z * np.conj(z) > 2**2  # who is diverging
            div_now = diverge & (divtime == maxit)  # who is diverging now
            divtime[div_now] = i  # note when
            z[diverge] = 2  # avoid diverging too much

        return divtime

    # Generate design system based on:

    # - App Size: Small, Medium, Large (0, 10)
    # - App Type: Social, Productivity, Entertainment, etc.
    # - App Frequency of use: Daily, Weekly, Monthly (0, 10)
    # - App Likeability: (0, 10)

    def gen_mandelbrot_item(
        size: int, use_frecuency: int, likeability: int, type: str
    ) -> np.ndarray:
        """_summary_

        Args:
                size (int): Maps to mandelbrot size (h,w)
                use_frecuency (int): maps to mandelbrot maxit
                likeability (int): maps to color map
                type (str): maps to rotation of image
        """

        return mandelbrot(size * size, size * size, use_frecuency)

    #plt.imshow(mandelbrot(400, 400))
    #plt.axis("off")

    #plt.savefig("mandelbrot.png", dpi=300, bbox_inches="tight")

    col2.image("mandelbrot.png", caption="Mandelbrot Set")

    """
        Entonces podemos generar distintas imágenes a partir de distintos valores de $c$, y combinar otros factores, como el color de la imagen o la resolución del fractal para aprovechar en nuestro sistema de diseño.
"""

    #fig, ax = plt.subplots(1, 5, figsize=(20, 20))
#
    #for i, size in enumerate([10, 50, 100, 200, 500]):
    #    ax[i].imshow(mandelbrot(size, size, 500), cmap="hot")
    #    ax[i].set_title(f"{size}")
    #    ax[i].axis("off")
#
    #fig.savefig("mandelbrot_sizes.png", dpi=300, bbox_inches="tight", pad_inches=3)
    #fig.tight_layout()

    st.image("mandelbrot_sizes.png")

    """
        A partir de esto plantee un sistema de diseño parametrizado que nos permita generar distintas imágenes a partir de distintos valores de $c$.
        """

    #for app in apps:
    #    apps[app]["cmap"] = cmaps_dict[apps[app]["likeability"]]
#
    ## Generate every app image
#
    #for app in apps:
    #    apps[app]["mandelbrot"] = gen_mandelbrot_item(
    #        apps[app]["size"],
    #        apps[app]["use_frecuency"],
    #        apps[app]["likeability"],
    #        apps[app]["type"],
    #    )

    # Plot every app image

    # 3 row of 6 images
    # plus 1 row of 7 images

    # 25 images in total

    #fig, axs = plt.subplots(4, 7, figsize=(20, 20))
#
    #for i, app in enumerate(apps):
    #    axs[i // 7, i % 7].imshow(apps[app]["mandelbrot"], cmap=apps[app]["cmap"])
    #    axs[i // 7, i % 7].axis("off")
    #    axs[i // 7, i % 7].set_title(app)
#
    #axs[3, 4].axis("off")
    #axs[3, 4].set_title("")
    #axs[3, 5].axis("off")
    #axs[3, 5].set_title("")
    #axs[3, 6].axis("off")
    #axs[3, 6].set_title("")
    #fig.tight_layout()
#
    #fig.savefig("mandelbrot_design.png", dpi=300)

    st.image("mandelbrot_design.png")

    """
        #### Sistema de Referencia para esta primera idea

        ##### El tamaño de la app afecta el tamaño del fractal
        """

    # Reference system

    # Plot an example of a mandelbrot image for reference

    # Size affects the number of iterations

    #fig, ax = plt.subplots(1, 9, figsize=(20, 20))
    #for s in range(2, 11):
    #    ax[s - 2].imshow(gen_mandelbrot_item(s, 10, 10, "Reference"), cmap="Greys")
    #    ax[s - 2].axis("off")
    #    ax[s - 2].set_title(f"Size {s}")
#
    #fig.tight_layout()
#
    #fig.savefig(
    #    "mandelbrot_reference_size.png", dpi=300, bbox_inches="tight", pad_inches=2
    #)

    st.image("mandelbrot_reference_size.png")

    """
        ##### La frecuencia de uso de la app afecta la cantidad de iteraciones del fractal
        """

    # Use frecuency affects the number of iterations

    #fig, ax = plt.subplots(1, 10, figsize=(20, 20))
#
    #for f in range(1, 11):
    #    ax[f - 1].imshow(gen_mandelbrot_item(7, f, 10, "Reference"), cmap="Greys")
    #    ax[f - 1].axis("off")
    #    ax[f - 1].set_title(f"Use frecuency {f}")
#
    #fig.tight_layout()
#
    #fig.savefig(
    #    "mandelbrot_reference_use_frecuency.png",
    #    dpi=300,
    #    bbox_inches="tight",
    #    pad_inches=2,
    #)

    st.image("mandelbrot_reference_use_frecuency.png")

    """
        ##### El "aprecio" por la app afecta el color del fractal
        """

    # Likeability affects the color map

    #fig, ax = plt.subplots(1, 11, figsize=(20, 20))
#
    #for l in range(0, 11):
    #    ax[l].imshow(gen_mandelbrot_item(7, 10, l, "Reference"), cmap=cmaps_dict[l])
    #    ax[l].axis("off")
    #    ax[l].set_title(f"Likeability {l}")
#
    #fig.tight_layout()
#
    #fig.savefig(
    #    "mandelbrot_reference_likeability.png",
    #    dpi=300,
    #    bbox_inches="tight",
    #    pad_inches=2,
    #)

    st.image("mandelbrot_reference_likeability.png")

types = {a["type"] for a in apps.values()}


with julia_tab:
    """

    ## Ampliar el sistema de diseño
    """

    # Julia Set

    def julia_set_fractal(c, n=100, thresh=50):
        """
        Copy-pasted from https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html#sphx-glr-gallery-lines-bars-and-markers-fill-py
        """

        def julia(z, c):
            return z**2 + c

        m = np.zeros((n, n))
        for i, x in enumerate(np.linspace(-2, 2, n)):
            for j, y in enumerate(np.linspace(-2, 2, n)):
                z = complex(x, y)
                t = 0
                while abs(z) < thresh and t < n:
                    z = julia(z, c)
                    t += 1
                m[j, i] = t

        return m

    # Generate design system based on:

    # - App Size: Small, Medium, Large (0, 10)
    # - App Type: Social, Productivity, Entertainment, etc.
    # - App Frequency of use: Daily, Weekly, Monthly (0, 10)
    # - App Likeability: (0, 10)

    def gen_julia_item(
        size: int, use_frecuency: int, likeability: int, t: str
    ) -> np.ndarray:
        """_summary_

        Args:
                size (int): Maps to mandelbrot size (h,w)
                use_frecuency (int): maps to mandelbrot maxit
                likeability (int): maps to color map
                type (str): maps to the type of fractal
        """

        # return mandelbrot(size * size, size * size, use_frecuency)

        complex_types = {
            "Comunication": complex(0.285, 0.01),
            "Entertainment": complex(-0.8, 0.156),
            "Identity": complex(-0.4, 0.6),
            "Music": complex(-0.1, -0.732),
            "Productivity": complex(-0.9, 0),
            "Social": complex(-0.215, -0.65),
            "Sports and Health": complex(0.73, -0.73),
        }

        complex_n = complex_types[t]

        return julia_set_fractal(
            complex_n,
            n=size * size + (likeability * likeability if likeability else 1),
            thresh=use_frecuency,
        )

    # plot an example

   #fig, ax = plt.subplots()
   #ax.imshow(julia_set_fractal(complex(-0.1, 0.65)))
   #ax.axis("off")
   ## ax.set_title("Julia Set Example")
   #fig.savefig("julia_set.png", dpi=300, bbox_inches="tight")

    # Columns

    col1, col2 = st.columns(2)

    col1.write("### Idea: Otros tipos de fractales")
    col1.write("#### Julia Set")

    col1.write(
        "El Mandelbrot Set es un ejemplo particular del Julia Set, por lo que además podríamos parametrizar el tipo de fractal que queremos generar."
    )
    col1.write(
        "Un ejemplo de un fractal generado por el Julia Set a partir de $$c = -0.1 + 0.65i$$"
    )
    col2.image("julia_set.png", use_column_width=True, caption="Julia Set Example")

    with col1:
        """
        Aprovechando entonces el sistema de diseño que ya tenemos, podemos generar distintos fractales en función del tipo de app que queremos representar.
        """
        pass

    """
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
    """

    #for app in apps:
    #    apps[app]["julia"] = gen_julia_item(
    #        apps[app]["size"],
    #        apps[app]["use_frecuency"],
    #        apps[app]["likeability"],
    #        apps[app]["type"],
    #    )

    # Plot every app image

    # 3 row of 6 images
    # plus 1 row of 7 images

    # 25 images in total

    #fig, axs = plt.subplots(4, 7, figsize=(20, 20))
#
    #for i, app in enumerate(apps):
    #    axs[i // 7, i % 7].imshow(apps[app]["julia"], cmap=apps[app]["cmap"])
    #    axs[i // 7, i % 7].axis("off")
    #    axs[i // 7, i % 7].set_title(app)
#
    #axs[3, 4].axis("off")
    #axs[3, 4].set_title("")
    #axs[3, 5].axis("off")
    #axs[3, 5].set_title("")
    #axs[3, 6].axis("off")
    #axs[3, 6].set_title("")
    #fig.tight_layout()
#
    #fig.savefig("julia_design.png", dpi=300, bbox_inches="tight", pad_inches=1)

    st.write("### Resultado: Sistema de diseño basado en fractales")
    st.image("julia_design.png")

    # Generate the design system

    # The type of the app affects de complex number

    complex_types = {
        "Comunication": complex(0.285, 0.01),
        "Entertainment": complex(-0.8, 0.156),
        "Identity": complex(-0.4, 0.6),
        "Music": complex(-0.1, -0.732),
        "Productivity": complex(-0.9, 0),
        "Social": complex(-0.215, -0.65),
        "Sports and Health": complex(0.73, -0.73),
    }

    #fig, ax = plt.subplots(1, 7, figsize=(20, 20))
#
    #for i, t in enumerate(complex_types):
    #    ax[i].imshow(julia_set_fractal(complex_types[t]), cmap="gray")
    #    ax[i].axis("off")
    #    ax[i].set_title(t)
#
    #fig.tight_layout()
#
    #fig.savefig("julia_types.png", dpi=300, bbox_inches="tight", pad_inches=1)

with system_tab:
    """
    ### Sistema de diseño

    #### Referencias

    ##### Clasificación de apps

    El tipo de app afecta el número complejo que se usa para generar el fractal
    """

    st.image("julia_types.png")

    # The use frecuency of the app affects the max iterations of the fractal

    #fig, ax = plt.subplots(1, 11, figsize=(20, 20))
#
    #for i, s in enumerate(range(0, 11)):
    #    ax[i].imshow(
    #        julia_set_fractal(complex_types["Social"], n=100, thresh=(s + 1)),
    #        cmap="gray",
    #    )
    #    ax[i].axis("off")
    #    ax[i].set_title(s)
#
    #fig.tight_layout()
#
    #fig.savefig("julia_use_frecuency.png", dpi=300, bbox_inches="tight", pad_inches=1)

    """

    #### Frecuencia de uso

    La frecuencia de uso de la app afecta la cantidad de iteraciones del fractal

    """

    st.image("julia_use_frecuency.png")

    # The size and the likeablility of the app affect the size of the image

    #fig, ax = plt.subplots(1, 11, figsize=(20, 20))
#
    #for i, s in enumerate(range(0, 11)):
    #    ax[i].imshow(
    #        julia_set_fractal(complex_types["Social"], n=(s + 2) ** 2), cmap="gray"
    #    )
    #    ax[i].axis("off")
    #    ax[i].set_title(s)
#
    #fig.tight_layout()
#
    #fig.savefig("julia_size.png", dpi=300, bbox_inches="tight", pad_inches=1)

    """

    #### Tamaño y aprecio de la app

    El tamaño y el aprecio de la app afectan el tamaño de la imagen, que se puede interpretar como la resolución del fractal en si.

    """

    st.image("julia_size.png")

    # The likeability of the app affects the color map

    #fig, ax = plt.subplots(1, 11, figsize=(20, 20))
#
    #for i, s in enumerate(range(0, 11)):
    #    ax[i].imshow(
    #        julia_set_fractal(complex_types["Social"], n=100, thresh=100),
    #        cmap=cmaps_dict[s],
    #    )
    #    ax[i].axis("off")
    #    ax[i].set_title(s)
#
    #fig.tight_layout()
#
    #fig.savefig("julia_likeability.png", dpi=300, bbox_inches="tight", pad_inches=1)

    # close all the figures

    plt.close("all")

    """

        #### aprecio de la app

        El aprecio de la app ademas determina el mapa de colores que se usa para generar el fractal.

        """

    st.image("julia_likeability.png")

    """
        Finalmente, el sistema de diseño parametrizado desarrollado se puede expandir para infinitos valores para generar cualquier fractal del Julia Set para representar cualquier tipo de app.
    """


with demo_tab:

    """

    ### Demo

    """

    col1, col2 = st.columns(2)

    with col1:
        # El usuario ingresa el nombre de su app

        st.write("Ingrese los datos de su app")

        usr_app_name = st.text_input("Nombre de la app", "Instagram")

        # El usuario ingresa el tipo de su app

        usr_app_type = st.selectbox(
            "Tipo de la app",
            [
                "Comunication",
                "Entertainment",
                "Identity",
                "Music",
                "Productivity",
                "Social",
                "Sports and Health",
            ],
        )

        # El usuario ingresa la frecuencia de uso de su app

        usr_app_use_frecuency = st.slider(
            "Frecuencia de uso de la app (0: Nunca, 10: Todo el tiempo)",
            min_value=0,
            max_value=10,
            value=5,
            step=1,
        )

        usr_app_size = st.slider(
            "Tamaño de la app", min_value=0, max_value=10, value=5, step=1
        )

        # El usuario ingresa el aprecio de su app

        usr_app_likeability = st.slider(
            "aprecio de la app (0: No me gusta, 10: Me encanta)",
            min_value=0,
            max_value=10,
            value=5,
            step=1,
        )

        usr_app_likeability += 2
        usr_app_size += 2
        usr_app_use_frecuency += 2

        if usr_app_likeability > 10:
            usr_app_likeability = 10

    with col2:

        img = gen_julia_item(
            usr_app_size,
            usr_app_use_frecuency,
            usr_app_likeability,
            usr_app_type,
        )

        plt.close("all")

        plt.figure(figsize=(30, 30))
        plt.imshow(img, cmap=cmaps_dict[usr_app_likeability])
        plt.axis("off")

        plt.savefig("julia_gen_item.png", dpi=300, bbox_inches="tight", pad_inches=1)

        st.image(
            "julia_gen_item.png", caption="Generated Julia Set Fractal: " + usr_app_name
        )
