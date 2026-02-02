from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Blueprint
from services.optimizer import optimize_production
from schemas import OptimizeRequest

router = APIRouter()


@router.post("/optimize")
def run_optimization(data: OptimizeRequest, db: Session = Depends(get_db)):

    blueprints = db.query(Blueprint).all()

    result = optimize_production(
        blueprints=blueprints,
        user_minerals=data.minerals,
        user_level=data.user_level
    )

    return result
