from rest_framework.permissions import BasePermission, IsAuthenticated
from users.permissions import IsAdmin, IsAdminOrManager, IsAdminOrStaffOrManager

class GeneralPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create','delete','update','partial_update']:
            return IsAuthenticated().has_permission(request, view) and IsAdmin().has_permission(request, view)
        return IsAuthenticated().has_permission(request, view) and IsAdminOrManager().has_permission(request, view)
    
class StockFleetPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create','delete','update','partial_update']:
            return IsAuthenticated().has_permission(request, view) and IsAdminOrManager().has_permission(request, view)
        return IsAuthenticated().has_permission(request, view) and IsAdminOrStaffOrManager().has_permission(request, view)