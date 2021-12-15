class Ordenes:
    def __init__(self, Folio, PrecioTotal, Productos = ['Producto1', 'Producto2'], CantidadPorProducto = ['Precio1', 'Precio2']):
        self.Folio = int(Folio)
        self.Productos = Productos
        self.CantidadPorProducto = CantidadPorProducto
        self.PrecioTotal = float(PrecioTotal)
        self.__GuardadoDataBaseOrdenes

    def CrearBoleta(self) -> None:
        print('Empresa: LexuKu')
        print('Productos')
        for l1, l2 in zip(self.Productos, self.CantidadPorProducto):
            print(l1, l2)
        print('total:',self.PrecioTotal)

    def CrearOrdenProducto(self):
        pass

    def __GuardadoDataBaseOrdenes(self):
        pass