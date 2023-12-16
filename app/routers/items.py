
from fastapi import APIRouter, HTTPException
from .. import schemas, models, dependencies
from sqlalchemy.orm import Session
from fastapi import Depends

router = APIRouter()

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(dependencies.get_db)):
    db_item = models.Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
