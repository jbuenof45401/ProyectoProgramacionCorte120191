def calcular_precio_producto(coste_producto):
    '''
    (num) -> float: valor del producto

    calcular el coste del producto aumentando el 50% de su valor como comision

    >>> calcular_precio_producto(5000)
    7500.0

    >>> calcular_precio_producto(1000)
    1500.0

    :param coste_producto: representa el coste del producto
    :return: valor del producto
    '''
    return coste_producto + (coste_producto * 0.5)


def calcular_precio_servicio(cantidad_horas):
    '''
    (num) -> num: precio por horas trabajadas

    >>> calcular_precio_servicio(5)
    500000

    >>> calcular_precio_servicio(4)
    400000

    :param cantidad_horas: horas de servicio prestado
    :return: valor de las horas prestadas
    '''

    return cantidad_horas * 100000


def calcular_precio_servicio_extras(cantidad_horas):
    '''
    (num) -> float

    recibe las horas extra trabajadas, devuelve el valor por las horas extra

    >>> calcular_precio_servicio_extras(1)
    125000.0
    >>> calcular_precio_servicio_extras(2)
    250000.0

    :param cantidad_horas: cantidad de horas extra trabajadas
    :return: valor de las horas extra
    '''

    precio_hora_normal = calcular_precio_servicio(cantidad_horas)

    return precio_hora_normal + (precio_hora_normal*0.25)


def calcular_costo_envio(kilometros):
    '''
    (num) -> num

    recibe las horas extra trabajadas, devuelve el valor por las horas extra

    >>> calcular_costo_envio(2)
    230

    >>> calcular_costo_envio(3)
    345

    :param kilometros: cantidad de kilometros recorridos
    :return: valor por los kilometros recorridos
    '''

    return  kilometros * 115

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    '''
    (num:,num) -> num

    Calcular el costo del producto mas los kilometros recorridos.

    >>> calcular_precio_producto_fuera(1000,2)
    1730.0

    >>> calcular_precio_producto_fuera(2000,1)
    3115.0


    :param coste_producto: num: costo del producto para jose
    :param kilometros: num: kilometros recorridos por jose
    :return: float: precio del producto mas recargo de envio
    '''

    return calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)




def calcular_iva_producto(coste_producto, tasa):
    '''
    (num, float)->  float

    >>> calcular_iva_producto(500,0.19)
    142.25

    >>> calcular_iva_producto(1000,0.19)
    285.0
    :param coste_producto: Costo bruto del producto
    :param tasa:
    :return: float: iva del producto
    '''
    return calcular_precio_producto(coste_producto) * tasa;


def calcular_iva_servicio(cantidad_horas, tasa):
    '''
    (num, float) -> float

    Iva de las horas trabajadas

    >>> calcular_iva_servicio(2,0.19)
    38000.0
    >>> calcular_iva_servicio(4,0.19)
    76000.0

    :param cantidad_horas: num: cantidad de horas de trabajo
    :param tasa: float: tasa de iva a aplicar
    :return: float: iva de las horas trabajadas
    '''
    return calcular_precio_servicio(cantidad_horas)*tasa


def calcular_iva_envio(kilometros, tasa):
    '''
    (num, float) -> float

    Calcula el iva del envio

    >>> calcular_iva_envio(1,0.19)
    21.85

    >>> calcular_iva_envio(2,0.19)
    43.7

    :param kilometros: num: kilometros recorridos
    :param tasa: float: iva a aplicar
    :return: float: el iva aplicado al envio
    '''

    return calcular_costo_envio(kilometros) * tasa


def calcular_iva_servicio_extra(cantidad_horas, tasa):
    '''
    (num,float)-> float

    Calcula el iva de las horas extra

    >>> calcular_iva_servicio_extra(2,0.19)
    47500.0

    >>> calcular_iva_servicio_extra(3,0.19)
    71250.0

    :param cantidad_horas: Cantidad de horas trabajadas
    :param tasa: Tasa de iva a aplicar
    :return: el iva por la cantidad de horas trabajadas
    '''

    return calcular_precio_servicio_extras(cantidad_horas) * tasa



def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    '''
    (num,num,num) -> num

    Calcular recuaudo por la venta de 3 productos

    >>> calcular_recaudo_locales(1000,2000,3000)
    9000.0

    >>> calcular_recaudo_locales(2000,3000,4000)
    13500.0

    :param coste_producto_1: Costo del producto 1
    :param coste_producto_2: Costo del producto 2
    :param coste_producto_3: Costo del producto 3
    :return: recaudo total de los productos
    '''
    recaudo = 0
    recaudo += calcular_precio_producto(coste_producto_1)
    recaudo += calcular_precio_producto(coste_producto_2)
    recaudo += calcular_precio_producto(coste_producto_3)

    return recaudo


def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    '''
    (num,num,num,num) -> num

    Calcula el recaudo de las horas de servicio

    >>> calcular_recaudo_horas_extra(1,2,3,4)
    1250000.0

    >>> calcular_recaudo_horas_extra(2,3,4,5)
    1750000.0

    :param horas_1: horas trabajadas 1
    :param horas_2: horas trabajadas 2
    :param horas_3: horas trabajadas 3
    :param horas_4: horas trabajadas 4
    :return: recuado por el total de las horas trabajadas
    '''
    recaudo=0

    recaudo += calcular_precio_servicio_extras(horas_1)
    recaudo += calcular_precio_servicio_extras(horas_2)
    recaudo += calcular_precio_servicio_extras(horas_3)
    recaudo += calcular_precio_servicio_extras(horas_4)

    return recaudo



def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    '''
    (num,num,num,num) -> num

    Calcula el recaudo de los productos vendidos y las horas de servicio prestado

    >>> calcular_recaudo_mixto_local(1000,2000,1,2)
    304500.0

    >>> calcular_recaudo_mixto_local(2000,3000,2,3)
    507500.0

    :param coste_producto_1: Costo del producto 1
    :param coste_producto_2: Costo del producto 2
    :param horas_1: Horas de servicio 1
    :param horas_2: horas de servico 2
    :return: reacudo total
    '''
    recaudo=0
    recaudo+=calcular_precio_producto(coste_producto_1)
    recaudo+=calcular_precio_producto(coste_producto_2)
    recaudo+=calcular_precio_servicio(horas_1)
    recaudo+=calcular_precio_servicio(horas_2)

    return  recaudo