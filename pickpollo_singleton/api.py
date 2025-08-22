from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from App_PickPollo import validar_correo, app_state

app = FastAPI(title="pickpollo API", version="2.0")

class Registro(BaseModel):
    nombre: str = Field(min_length=1, description="Nombre del usuario")
    email: str = Field(min_length=5, description="Correo electronico a validar")

class Pedido(BaseModel):
    email: str
    producto: str
    cantidad: int

@app.get("/menu")
def get_menu():
    return {"menu": list(app_state.obtener_productos().keys())}

@app.get("/precios")
def get_precios():
    return {"precios": app_state.obtener_productos()}

@app.post("/registro")
def post_registro(data: Registro):
    if not validar_correo(data.email):
        raise HTTPException(status_code=400, detail="correo electronico invalido")
    
    if app_state.usuario_existe(data.email):
        raise HTTPException(status_code=400, detail="usuario ya existe")
    
    app_state.agregar_usuario(data.email, data.nombre)
    return {"status": "ok", "mensaje": f"usuario '{data.nombre}' registrado con exito"}

@app.post("/pedido")
def post_pedido(pedido: Pedido):
    if not app_state.usuario_existe(pedido.email):
        raise HTTPException(status_code=400, detail="usuario no registrado")
    
    productos = app_state.obtener_productos()
    if pedido.producto not in productos:
        raise HTTPException(status_code=400, detail="producto no existe")
    
    pedido_data = {
        "email": pedido.email,
        "producto": pedido.producto,
        "cantidad": pedido.cantidad,
        "precio_unitario": productos[pedido.producto],
        "total": productos[pedido.producto] * pedido.cantidad
    }
    
    app_state.agregar_pedido(pedido_data)
    return {"status": "ok", "pedido": pedido_data}

@app.get("/estadisticas")
def get_estadisticas():
    return {
        "total_usuarios": len(app_state.usuarios_registrados),
        "total_pedidos": len(app_state.obtener_pedidos()),
        "usuarios": app_state.usuarios_registrados
    }