from pydantic import BaseModel

class PokemonRequest(BaseModel):
    id: int