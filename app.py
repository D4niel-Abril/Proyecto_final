from flask import Flask, render_template, request

app = Flask(__name__)

#temporal
productos = [
    {"nombre": "MOTOROLA Edge 50 Fusion 256GB Verde", "precio": "999.900", "tienda": "Ktronix", "url": "https://www.ktronix.com/celular-motorola-edge-50-fusion-256gb-verde/p/840023261879?fuente=google&medio=cpc&campaign=KT_COL_MAX_PEF_CPC_AON_CEL_TLP_Celulares_PAC&keyword=&gad_source=4&gclid=CjwKCAiAnpy9BhAkEiwA-P8N4gCdUfePxTRUR2jTviNPDOLQsQ1jiobWWPVdn4Z8gf5JXcgtwbQ24BoCSbUQAvD_BwE"},
    {"nombre": "Celular Motorola Edge 50 Fusion 256GB | 8GB RAM", "precio": "990.900", "tienda": "falabella", "url": "https://www.falabella.com.co/falabella-co/product/72967063/Celular-Motorola-Edge-50-Fusion-256GB-8GB-RAM-Camara-posterior-50MP-Camara-frontal-32MP-Pantalla-6.7-pulgadas-+-Qualcomm-Snapdragon-6-Gen-1/72967064?kid=shopp201fa&gad_source=1&gclid=CjwKCAiAnpy9BhAkEiwA-P8N4j5qN4b6EOWli2pE-hAz7G3TZC4bhjAhwHg7hSFProu4w2vNLmHiuBoCICcQAvD_BwE"},
    {"nombre": "Motorola Edge 50 Fusion 5G 256 GB Azul Oscuro 8 GB RAM", "precio": "1.049.900", "tienda": "mercado libre", "url": "https://www.mercadolibre.com.co/motorola-edge-50-fusion-5g-256-gb-azul-oscuro-8-gb-ram/p/MCO36687684#polycard_client=search-nordic&searchVariation=MCO36687684&position=2&search_layout=stack&type=product&tracking_id=186f87ae-fe2f-4dca-b489-62936db07de5&wid=MCO1503103091&sid=search"},
    {"nombre": "Apple iPhone 13 (128 GB) - Blanco estelar", "precio": "3'479.990", "tienda": "mercado libre", "url": "https://www.mercadolibre.com.co/apple-iphone-13-128-gb-blanco-estelar-distribuidor-autorizado/p/MCO1018500855#polycard_client=search-nordic&searchVariation=MCO1018500855&position=1&search_layout=stack&type=product&tracking_id=1dd6f184-785e-4f8d-b29b-5c30d43b39ab&wid=MCO2774838810&sid=search"},
    {"nombre": "iPhone 13 128Gb", "precio": "$2.757.990", "tienda": "Apple Store", "url": "https://www.tiendaapple.store/iphone-13-128gb?srsltid=AfmBOoq-g-7XBi0UoqHVeZcCn4NpmOEYeMTgZ8IUa3gj25wg9knI3a86"},
    {"nombre": "iPhone 13 128GB Blanco Estrella", "precio": "$2.869.010", "tienda": "Ktronix", "url": "https://www.ktronix.com/iphone13-128gb-blanco-estrella/p/194252707432?algEvent=eyJvYmplY3RJZCI6IjE5NDI1MjcwNzQzMiIsImluZGV4Ijoia3Ryb25peEluZGV4QWxnb2xpYVBSRCIsImFjdGlvbiI6InZpZXciLCJxdWVyeUlEIjoiODBjM2M3YTRiYjhiNmY5MDM5NDQ4OGEyZGJjYzg4MDkifQ=="},
    {"nombre": "TV 55 Pulgadas OLED - OLED55B4PSA ", "precio": "3.999.901", "tienda": "lg", "url": "https://www.lg.com/co/tvs-y-barras-de-sonido/oled/oled55b4psa/"},
    {"nombre": "Televisor LG 55 pulgadas OLED Uhd4K Smart TV OLED55B4PSA", "precio":" 3.599.900", "tienda": "exito", "url": "https://www.exito.com/televisor-lg-55-pulgadas-oled-uhd-4k-smart-tv-oled55b4psa-3162669/p"},
    {"nombre": "TV LG 55 Pulgadas 140 Cm OLED55B4 4K-UHD OLED Smart TV", "precio": "3.999.900", "tienda": "Ktronix", "url": "https://www.ktronix.com/tv-lg-55-pulgadas-140-cm-oled55b4-4k-uhd-oled-smart-tv/p/8806091983398"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods=["POST"])
def buscar():
    consulta = request.form["producto"].lower()
    resultados = [p for p in productos if consulta in p["nombre"].lower()]
    return render_template("resultados.html", productos=resultados, consulta=consulta)

if __name__ == "__main__":
    app.run(debug=True)
