from sqlalchemy.orm import Session
from datetime import datetime

class BaseRepo(object):
    """Base repository class for all repositories to inherit from."""

    def __init__(self, model: object, db: Session):
        self.model = model
        self.db = db

    def get_all(self):
        """Get all objects from the database."""
        return self.db.query(self.model).all()
    
    def get_by_id(self, id):
        """Get an object from the database by id."""
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def create(self, obj_in):
        """Create an object in the database."""
        obj = self.model(**obj_in.dict())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def update(self, obj, obj_in):
        """Update an object in the database."""
        for field in obj_in.dict(exclude_unset=True):
            setattr(obj, field, getattr(obj_in, field))
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def delete(self, id):
        """Delete an object from the database by id."""
        obj = self.db.query(self.model).filter(self.model.id == id).first()
        self.db.delete(obj)
        self.db.commit()
        return True
    
    def soft_delete(self, obj):
        """Soft delete an object from the database."""
        obj.deleted_at = datetime.utcnow()
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
