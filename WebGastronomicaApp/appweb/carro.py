class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}
        
        self.carro=carro

    def agregar(self, plato):
        
        if(str(plato.ID_Plato) not in self.carro.keys()):
            self.carro[plato.ID_Plato]={
                "plato_id":plato.ID_Plato,
                "nombre":plato.Nombre,
                "precio":str(plato.Costo),
                "preciop":str(plato.Costo),
                "cantidad":1,
                "imagen":plato.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(plato.ID_Plato):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=int(value["precio"])+plato.Costo
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, plato):
        plato.id=str(plato.ID_Plato)
        if plato.id in self.carro:
            del self.carro[plato.id]
            self.guardar_carro()

    def restar_plato(self, plato):
        
        for key, value in self.carro.items():
            if key==str(plato.ID_Plato):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=int(value["precio"])-plato.Costo
                if value["cantidad"]<1:
                    self.eliminar(plato)
                break
        
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True