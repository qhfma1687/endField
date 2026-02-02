from pydantic import BaseModel
from typing import Dict


class OptimizeRequest(BaseModel):
    user_level: int
    minerals: Dict[str, float]  # {"Ferrium Ore": 100}
