monto_compra = 1000.0  # Monto de la compra
recargo_porcentaje = 0.3  # Porcentaje de recargo
descuento_porcentaje = 0.5 # Porcentaje de descuento

precio_recargo = monto_compra * recargo_porcentaje
precio_descuento = monto_compra * descuento_porcentaje

monto_final = (monto_compra + precio_recargo) - precio_descuento

print(monto_final)