"""Database Models - Auto-generated"""
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class 1.**employeesTable**(Base):
    """Model for 1. **Employees Table**"""
    __tablename__ = "1._**employees_table**"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    role = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class 2.**leaveApplicationsTable**(Base):
    """Model for 2. **Leave Applications Table**"""
    __tablename__ = "2._**leave_applications_table**"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    leave_type = Column(String(255))
    status = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class 3.**leavePoliciesTable**(Base):
    """Model for 3. **Leave Policies Table**"""
    __tablename__ = "3._**leave_policies_table**"
    
    id = Column(Integer, primary_key=True, index=True)
    policy_name = Column(String(255))
    leave_type = Column(String(255))
    duration = Column(String(255))
    accrual_rate = Column(Float)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class 4.**leaveBalancesTable**(Base):
    """Model for 4. **Leave Balances Table**"""
    __tablename__ = "4._**leave_balances_table**"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    leave_type = Column(String(255))
    balance = Column(Float)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class 5.**leaveApprovalsTable**(Base):
    """Model for 5. **Leave Approvals Table**"""
    __tablename__ = "5._**leave_approvals_table**"
    
    id = Column(Integer, primary_key=True, index=True)
    leave_application_id = Column(Integer)
    manager_id = Column(Integer)
    approval_status = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class 6.**hrmsEmployeesTable**(Base):
    """Model for 6. **Hrms Employees Table**"""
    __tablename__ = "6._**hrms_employees_table**"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    hrms_data = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

