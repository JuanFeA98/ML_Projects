def calc_detail_cabin(x, position):
    # Divides la cadena en subcadenas utilizando '/' como separador y devuelve el primer elemento
    try:
        return x.split('/')[position]        
    # Si ocurre algún error al intentar dividir la cadena, se devuelve la cadena original
    except:
        return x