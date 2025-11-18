def calculate_price(item_price, item_quantity):
    # La variable 'TAX' no se usa, SonarQube lo detectará como código muerto.
    TAX = 0.16 
    
    # El número '10' es un 'Magic Number' que SonarQube puede señalar.
    if item_quantity > 10: 
        final_discount = 0.05
    else:
        final_discount = 0.00
        
    total = item_price * item_quantity * (1 - final_discount)
    
    # Las funciones 'print' en código de producción a veces son señaladas.
    print(f"Calculando total: {total}")
    return total

# Ejecutamos la función
calculate_price(50, 20)
