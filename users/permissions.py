from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    '''Allow access only to admin users'''
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"
    
class IsManager(BasePermission):
    '''Allow access only to manager users'''
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "manager"
    
class IsStaff(BasePermission):
    '''Allow access only to staff users'''
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "staff"
    
class IsAdminOrStaffOrManager(BasePermission):
    '''Allow access to admin, staff, or manager users'''
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["admin", "staff", "manager"]

class IsAdminOrManager(BasePermission):
    '''Allow access to admin and manager users'''
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["admin", "manager"]