#Podemos utilizar todas las otras estructuras de datos para combinarlas de forma de representar información más compleja.


recipes_book= {

    "-Cocadas-": {
        "ingredients": ["Galletas", "Manjar", "Coco rallado"],
        "steps":
        "Paso 1: En un bol poner las galletas molidas. Ir agregando el manjar, poco a poco. La cantidad necesaria para que quede una pasta manejable. Poner el coco en un plato. Paso 2: Con las manos formar pelotitas del tamaño de una nuez. Pasar por el coco rallado varias veces para que queden bien cubiertas. Poner en cápsulas de papel\n",
    },
    "-Pollo arverjado-": {
        "ingredients": ["Cebolla", "Zanahorias", "Pimentón", "Tutos de pollo", "Ajo", "Vino blanco"],
        "steps":
        "Paso1: Comenzamos cortando la cebolla en corte pluma, la zanahoria en rodajas y el pimentón en cuadritos pequeños. Paso2: En una olla grande calentar un chorro de aceite y sellar nuestros tutos de Pollo Super Pollo, por todos sus lados (aproximadamente 2 minutos por lado) y los dejamos reposar en un plato. Paso3: En la misma olla, dorar la cebolla y agregar la zanahoria, el pimentón y el ajo. Salpimentar a gusto. Regresamos los tutos a la olla, agregamos 1 taza de agua por cada 4 presas, el vino blanco, el orégano y la salsa de tomates. Tapamos y dejamos cocinar durante 25 minutos. Incorporamos las arvejas congeladas y dejamos cocinar durante 5 minutos más. Paso 4: Servimos y disfrutamos con arroz preparado al gusto.\n",
    },
    "-Compota de frutas-":{
      "ingredients": ["Manzanas", "Peras"],
      "steps":
     "Pela las manzanas y las peras y córtalas en gajos. En un bol, pon tres cucharadas de agua, el azúcar, la canela, la ralladura de limón y los anises, y mezcla todo bien. Luego, añade los orejones cortados en tiras, las ciruelas sin hueso y el resto de frutas y remueve lentamente. Mete el bol en el microondas durante dos minutos a potencia media. Cuando esté listo, saca el recipiente, remueve la compota para que se mezcle bien y vuelve a meterlo otros dos minutos en el microondas. Deja que se enfríe fuera de la nevera y luego refrigéralo."   
    }
    
    
  }



meals = recipes_book.keys()

for meal in meals:
    print("---------------------")
    print(f"{meal.title()}")
    print("---------------------")
    ingredients = recipes_book[meal]["ingredients"]
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print(recipes_book[meal]["steps"])
