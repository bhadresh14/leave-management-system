"""API Routes - Auto-generated with full CRUD"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db, Base, engine
from app.models.models import *
from app.schemas.schemas import *

# Create all tables
Base.metadata.create_all(bind=engine)

router = APIRouter()


# ==================== 1. **EMPLOYEES TABLE** ROUTES ====================

@router.get("/1.-**employees-table**", response_model=List[1.**employeesTable**Response], tags=["1. **Employees Table**"])
def get_all_1._**employees_table**(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all 1. **Employees Table** records"""
    items = db.query(1.**employeesTable**).offset(skip).limit(limit).all()
    return items

@router.get("/1.-**employees-table**/{id}", response_model=1.**employeesTable**Response, tags=["1. **Employees Table**"])
def get_1._**employees_table**(id: int, db: Session = Depends(get_db)):
    """Get a single 1. **Employees Table** by ID"""
    item = db.query(1.**employeesTable**).filter(1.**employeesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="1. **Employees Table** not found")
    return item

@router.post("/1.-**employees-table**", response_model=1.**employeesTable**Response, status_code=status.HTTP_201_CREATED, tags=["1. **Employees Table**"])
def create_1._**employees_table**(data: 1.**employeesTable**Create, db: Session = Depends(get_db)):
    """Create a new 1. **Employees Table**"""
    item = 1.**employeesTable**(**data.model_dump(exclude_unset=True))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/1.-**employees-table**/{id}", response_model=1.**employeesTable**Response, tags=["1. **Employees Table**"])
def update_1._**employees_table**(id: int, data: 1.**employeesTable**Create, db: Session = Depends(get_db)):
    """Update a 1. **Employees Table**"""
    item = db.query(1.**employeesTable**).filter(1.**employeesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="1. **Employees Table** not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/1.-**employees-table**/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["1. **Employees Table**"])
def delete_1._**employees_table**(id: int, db: Session = Depends(get_db)):
    """Delete a 1. **Employees Table**"""
    item = db.query(1.**employeesTable**).filter(1.**employeesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="1. **Employees Table** not found")
    db.delete(item)
    db.commit()
    return None

# ==================== 2. **LEAVE APPLICATIONS TABLE** ROUTES ====================

@router.get("/2.-**leave-applications-table**", response_model=List[2.**leaveApplicationsTable**Response], tags=["2. **Leave Applications Table**"])
def get_all_2._**leave_applications_table**(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all 2. **Leave Applications Table** records"""
    items = db.query(2.**leaveApplicationsTable**).offset(skip).limit(limit).all()
    return items

@router.get("/2.-**leave-applications-table**/{id}", response_model=2.**leaveApplicationsTable**Response, tags=["2. **Leave Applications Table**"])
def get_2._**leave_applications_table**(id: int, db: Session = Depends(get_db)):
    """Get a single 2. **Leave Applications Table** by ID"""
    item = db.query(2.**leaveApplicationsTable**).filter(2.**leaveApplicationsTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="2. **Leave Applications Table** not found")
    return item

@router.post("/2.-**leave-applications-table**", response_model=2.**leaveApplicationsTable**Response, status_code=status.HTTP_201_CREATED, tags=["2. **Leave Applications Table**"])
def create_2._**leave_applications_table**(data: 2.**leaveApplicationsTable**Create, db: Session = Depends(get_db)):
    """Create a new 2. **Leave Applications Table**"""
    item = 2.**leaveApplicationsTable**(**data.model_dump(exclude_unset=True))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/2.-**leave-applications-table**/{id}", response_model=2.**leaveApplicationsTable**Response, tags=["2. **Leave Applications Table**"])
def update_2._**leave_applications_table**(id: int, data: 2.**leaveApplicationsTable**Create, db: Session = Depends(get_db)):
    """Update a 2. **Leave Applications Table**"""
    item = db.query(2.**leaveApplicationsTable**).filter(2.**leaveApplicationsTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="2. **Leave Applications Table** not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/2.-**leave-applications-table**/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["2. **Leave Applications Table**"])
def delete_2._**leave_applications_table**(id: int, db: Session = Depends(get_db)):
    """Delete a 2. **Leave Applications Table**"""
    item = db.query(2.**leaveApplicationsTable**).filter(2.**leaveApplicationsTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="2. **Leave Applications Table** not found")
    db.delete(item)
    db.commit()
    return None

# ==================== 3. **LEAVE POLICIES TABLE** ROUTES ====================

@router.get("/3.-**leave-policies-table**", response_model=List[3.**leavePoliciesTable**Response], tags=["3. **Leave Policies Table**"])
def get_all_3._**leave_policies_table**(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all 3. **Leave Policies Table** records"""
    items = db.query(3.**leavePoliciesTable**).offset(skip).limit(limit).all()
    return items

@router.get("/3.-**leave-policies-table**/{id}", response_model=3.**leavePoliciesTable**Response, tags=["3. **Leave Policies Table**"])
def get_3._**leave_policies_table**(id: int, db: Session = Depends(get_db)):
    """Get a single 3. **Leave Policies Table** by ID"""
    item = db.query(3.**leavePoliciesTable**).filter(3.**leavePoliciesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="3. **Leave Policies Table** not found")
    return item

@router.post("/3.-**leave-policies-table**", response_model=3.**leavePoliciesTable**Response, status_code=status.HTTP_201_CREATED, tags=["3. **Leave Policies Table**"])
def create_3._**leave_policies_table**(data: 3.**leavePoliciesTable**Create, db: Session = Depends(get_db)):
    """Create a new 3. **Leave Policies Table**"""
    item = 3.**leavePoliciesTable**(**data.model_dump(exclude_unset=True))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/3.-**leave-policies-table**/{id}", response_model=3.**leavePoliciesTable**Response, tags=["3. **Leave Policies Table**"])
def update_3._**leave_policies_table**(id: int, data: 3.**leavePoliciesTable**Create, db: Session = Depends(get_db)):
    """Update a 3. **Leave Policies Table**"""
    item = db.query(3.**leavePoliciesTable**).filter(3.**leavePoliciesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="3. **Leave Policies Table** not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/3.-**leave-policies-table**/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["3. **Leave Policies Table**"])
def delete_3._**leave_policies_table**(id: int, db: Session = Depends(get_db)):
    """Delete a 3. **Leave Policies Table**"""
    item = db.query(3.**leavePoliciesTable**).filter(3.**leavePoliciesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="3. **Leave Policies Table** not found")
    db.delete(item)
    db.commit()
    return None

# ==================== 4. **LEAVE BALANCES TABLE** ROUTES ====================

@router.get("/4.-**leave-balances-table**", response_model=List[4.**leaveBalancesTable**Response], tags=["4. **Leave Balances Table**"])
def get_all_4._**leave_balances_table**(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all 4. **Leave Balances Table** records"""
    items = db.query(4.**leaveBalancesTable**).offset(skip).limit(limit).all()
    return items

@router.get("/4.-**leave-balances-table**/{id}", response_model=4.**leaveBalancesTable**Response, tags=["4. **Leave Balances Table**"])
def get_4._**leave_balances_table**(id: int, db: Session = Depends(get_db)):
    """Get a single 4. **Leave Balances Table** by ID"""
    item = db.query(4.**leaveBalancesTable**).filter(4.**leaveBalancesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="4. **Leave Balances Table** not found")
    return item

@router.post("/4.-**leave-balances-table**", response_model=4.**leaveBalancesTable**Response, status_code=status.HTTP_201_CREATED, tags=["4. **Leave Balances Table**"])
def create_4._**leave_balances_table**(data: 4.**leaveBalancesTable**Create, db: Session = Depends(get_db)):
    """Create a new 4. **Leave Balances Table**"""
    item = 4.**leaveBalancesTable**(**data.model_dump(exclude_unset=True))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/4.-**leave-balances-table**/{id}", response_model=4.**leaveBalancesTable**Response, tags=["4. **Leave Balances Table**"])
def update_4._**leave_balances_table**(id: int, data: 4.**leaveBalancesTable**Create, db: Session = Depends(get_db)):
    """Update a 4. **Leave Balances Table**"""
    item = db.query(4.**leaveBalancesTable**).filter(4.**leaveBalancesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="4. **Leave Balances Table** not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/4.-**leave-balances-table**/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["4. **Leave Balances Table**"])
def delete_4._**leave_balances_table**(id: int, db: Session = Depends(get_db)):
    """Delete a 4. **Leave Balances Table**"""
    item = db.query(4.**leaveBalancesTable**).filter(4.**leaveBalancesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="4. **Leave Balances Table** not found")
    db.delete(item)
    db.commit()
    return None

# ==================== 5. **LEAVE APPROVALS TABLE** ROUTES ====================

@router.get("/5.-**leave-approvals-table**", response_model=List[5.**leaveApprovalsTable**Response], tags=["5. **Leave Approvals Table**"])
def get_all_5._**leave_approvals_table**(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all 5. **Leave Approvals Table** records"""
    items = db.query(5.**leaveApprovalsTable**).offset(skip).limit(limit).all()
    return items

@router.get("/5.-**leave-approvals-table**/{id}", response_model=5.**leaveApprovalsTable**Response, tags=["5. **Leave Approvals Table**"])
def get_5._**leave_approvals_table**(id: int, db: Session = Depends(get_db)):
    """Get a single 5. **Leave Approvals Table** by ID"""
    item = db.query(5.**leaveApprovalsTable**).filter(5.**leaveApprovalsTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="5. **Leave Approvals Table** not found")
    return item

@router.post("/5.-**leave-approvals-table**", response_model=5.**leaveApprovalsTable**Response, status_code=status.HTTP_201_CREATED, tags=["5. **Leave Approvals Table**"])
def create_5._**leave_approvals_table**(data: 5.**leaveApprovalsTable**Create, db: Session = Depends(get_db)):
    """Create a new 5. **Leave Approvals Table**"""
    item = 5.**leaveApprovalsTable**(**data.model_dump(exclude_unset=True))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/5.-**leave-approvals-table**/{id}", response_model=5.**leaveApprovalsTable**Response, tags=["5. **Leave Approvals Table**"])
def update_5._**leave_approvals_table**(id: int, data: 5.**leaveApprovalsTable**Create, db: Session = Depends(get_db)):
    """Update a 5. **Leave Approvals Table**"""
    item = db.query(5.**leaveApprovalsTable**).filter(5.**leaveApprovalsTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="5. **Leave Approvals Table** not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/5.-**leave-approvals-table**/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["5. **Leave Approvals Table**"])
def delete_5._**leave_approvals_table**(id: int, db: Session = Depends(get_db)):
    """Delete a 5. **Leave Approvals Table**"""
    item = db.query(5.**leaveApprovalsTable**).filter(5.**leaveApprovalsTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="5. **Leave Approvals Table** not found")
    db.delete(item)
    db.commit()
    return None

# ==================== 6. **HRMS EMPLOYEES TABLE** ROUTES ====================

@router.get("/6.-**hrms-employees-table**", response_model=List[6.**hrmsEmployeesTable**Response], tags=["6. **Hrms Employees Table**"])
def get_all_6._**hrms_employees_table**(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all 6. **Hrms Employees Table** records"""
    items = db.query(6.**hrmsEmployeesTable**).offset(skip).limit(limit).all()
    return items

@router.get("/6.-**hrms-employees-table**/{id}", response_model=6.**hrmsEmployeesTable**Response, tags=["6. **Hrms Employees Table**"])
def get_6._**hrms_employees_table**(id: int, db: Session = Depends(get_db)):
    """Get a single 6. **Hrms Employees Table** by ID"""
    item = db.query(6.**hrmsEmployeesTable**).filter(6.**hrmsEmployeesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="6. **Hrms Employees Table** not found")
    return item

@router.post("/6.-**hrms-employees-table**", response_model=6.**hrmsEmployeesTable**Response, status_code=status.HTTP_201_CREATED, tags=["6. **Hrms Employees Table**"])
def create_6._**hrms_employees_table**(data: 6.**hrmsEmployeesTable**Create, db: Session = Depends(get_db)):
    """Create a new 6. **Hrms Employees Table**"""
    item = 6.**hrmsEmployeesTable**(**data.model_dump(exclude_unset=True))
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/6.-**hrms-employees-table**/{id}", response_model=6.**hrmsEmployeesTable**Response, tags=["6. **Hrms Employees Table**"])
def update_6._**hrms_employees_table**(id: int, data: 6.**hrmsEmployeesTable**Create, db: Session = Depends(get_db)):
    """Update a 6. **Hrms Employees Table**"""
    item = db.query(6.**hrmsEmployeesTable**).filter(6.**hrmsEmployeesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="6. **Hrms Employees Table** not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/6.-**hrms-employees-table**/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["6. **Hrms Employees Table**"])
def delete_6._**hrms_employees_table**(id: int, db: Session = Depends(get_db)):
    """Delete a 6. **Hrms Employees Table**"""
    item = db.query(6.**hrmsEmployeesTable**).filter(6.**hrmsEmployeesTable**.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="6. **Hrms Employees Table** not found")
    db.delete(item)
    db.commit()
    return None


# ==================== DASHBOARD ====================

@router.get("/dashboard/stats", tags=["Dashboard"])
def get_dashboard_stats(db: Session = Depends(get_db)):
    """Get dashboard statistics"""
    stats = {}
    stats["1._**employees_table**_count"] = db.query(1.**employeesTable**).count()
    stats["2._**leave_applications_table**_count"] = db.query(2.**leaveApplicationsTable**).count()
    stats["3._**leave_policies_table**_count"] = db.query(3.**leavePoliciesTable**).count()
    stats["4._**leave_balances_table**_count"] = db.query(4.**leaveBalancesTable**).count()
    stats["5._**leave_approvals_table**_count"] = db.query(5.**leaveApprovalsTable**).count()
    stats["6._**hrms_employees_table**_count"] = db.query(6.**hrmsEmployeesTable**).count()
    return stats
