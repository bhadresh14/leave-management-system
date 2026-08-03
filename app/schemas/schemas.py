"""Pydantic Schemas - Auto-generated"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date

class 1.**employeesTable**Base(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None

class 1.**employeesTable**Create(1.**employeesTable**Base):
    pass

class 1.**employeesTable**Response(1.**employeesTable**Base):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class 2.**leaveApplicationsTable**Base(BaseModel):
    employee_id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    leave_type: Optional[str] = None
    status: Optional[str] = None

class 2.**leaveApplicationsTable**Create(2.**leaveApplicationsTable**Base):
    pass

class 2.**leaveApplicationsTable**Response(2.**leaveApplicationsTable**Base):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class 3.**leavePoliciesTable**Base(BaseModel):
    policy_name: Optional[str] = None
    leave_type: Optional[str] = None
    duration: Optional[str] = None
    accrual_rate: Optional[float] = None

class 3.**leavePoliciesTable**Create(3.**leavePoliciesTable**Base):
    pass

class 3.**leavePoliciesTable**Response(3.**leavePoliciesTable**Base):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class 4.**leaveBalancesTable**Base(BaseModel):
    employee_id: Optional[int] = None
    leave_type: Optional[str] = None
    balance: Optional[float] = None

class 4.**leaveBalancesTable**Create(4.**leaveBalancesTable**Base):
    pass

class 4.**leaveBalancesTable**Response(4.**leaveBalancesTable**Base):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class 5.**leaveApprovalsTable**Base(BaseModel):
    leave_application_id: Optional[int] = None
    manager_id: Optional[int] = None
    approval_status: Optional[str] = None

class 5.**leaveApprovalsTable**Create(5.**leaveApprovalsTable**Base):
    pass

class 5.**leaveApprovalsTable**Response(5.**leaveApprovalsTable**Base):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class 6.**hrmsEmployeesTable**Base(BaseModel):
    employee_id: Optional[int] = None
    hrms_data: Optional[str] = None

class 6.**hrmsEmployeesTable**Create(6.**hrmsEmployeesTable**Base):
    pass

class 6.**hrmsEmployeesTable**Response(6.**hrmsEmployeesTable**Base):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

