class Productos:
    def __init__(self, CodigoBarra, NombreProducto, Categoria, Marca, PrecioUnitario, CantidadTotalAlmacen, StockCritico):
        self.CodigoBarra = CodigoBarra
        self.NombreProducto = NombreProducto
        self.Categoria = Categoria
        self.Marca = Marca
        self.PrecioUnitario = PrecioUnitario
        self.CantidadTotalAlmacen = CantidadTotalAlmacen
        self.StockCritico = StockCritico

    def ingresarProducto(self):
        pass

    def __GuardadoDataBaseProductos(self):
        pass