from django.contrib import admin
from myapp.models import (
    Movie, 
    Food, 
    TeamMember, 
    Product, 
    Department, 
    Studio, 
    InquiryLogForm,
)

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "year",
        "genre",
        "director",
        "rating",
        "description",
        "image",
    ]

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "image",
    ]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
    ]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "age",
        "role",
        "is_active",
        "department",
    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "price",
        "description",
        "image",
    ]

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "city",
        "specialty",
        "description",
        "created_at",
    ]

    search_fields = ("name", "city")

@admin.register(InquiryLogForm)
class InquiryLogFormAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "is_success",
        "is_error",
        "submitted_at",
    ]

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False