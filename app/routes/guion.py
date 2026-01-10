
from fastapi import APIRouter, Query
from app.utils.guion import generar_guion
from app.utils.config import configurar_gemini, cargar_estructura


router = APIRouter()


@router.get("/guion")
def crear_guion(
    tema: str = Query(..., description="Palabra o frase para el guion"),
    cantidad_palabras: int = Query(200, description="Cantidad de palabras del guion"),
):
    client = configurar_gemini()
    estructura = cargar_estructura()
    guion = generar_guion(client=client, tema=tema, cantidad_palabras=cantidad_palabras, estructura=estructura)
    return {"guion": guion}
