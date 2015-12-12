from django.contrib import admin


class NotebookAdmin(admin.ModelAdmin):
    fields = ['konkrnote', 'konkruser', 'zakaz']
