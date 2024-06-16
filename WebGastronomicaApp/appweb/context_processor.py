def costo_total_carro(request):
    total=0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total=total+(int(value["precio"]))
    
    return {"costo_total_carro":total}




