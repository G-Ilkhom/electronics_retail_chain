from django.contrib import admin
from network.models import Network, Contact, Product


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0.00)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "level", "supplier", "debt_to_supplier",)
    search_fields = ("name",)
    list_filter = ("supplier",)
    actions = [clear_debt]
    list_display_links = ["supplier"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "country", "city", "street", "house_number", "supplier",)
    search_fields = ("email",)
    list_filter = ("city",)
    list_display_links = ["supplier"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "model", "release_date", "supplier",)
    search_fields = ("name",)
    list_filter = ("release_date", "supplier",)
    list_display_links = ["supplier"]
