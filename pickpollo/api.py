from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field 
from App_PickPollo import validar_correo as validar_email 

app = FastAPI(title="pickpollo API", version="2.0") 


MENU_ITEMS = [
    "Pollo entero🐥​ ",
    "1/2 Pollo 🍗", 
    "1/4 Pollo🍗",
    "Papas fritas🍟​",
    "Gaseosa🍾"
]


class Registro(BaseModel):
    nombre: str = Field(min_length=1, description="Nombre del usuario")
    email: str = Field(min_length=5, description="Correo electronico a validar")

@app.get("/menu")
def get_menu():
    return {"menu": MENU_ITEMS}

@app.post("/registro")
def post_registro(data: Registro):
    if not validar_email(data.email):
        raise HTTPException(status_code=400, detail="correo electronico invalido")
    
    #! Aqui se podra guardar en una BD; por ahora devolvemos OK.
    return {"status": "ok", "mensaje": f"usuario '{data.nombre}' registrado con exito."}