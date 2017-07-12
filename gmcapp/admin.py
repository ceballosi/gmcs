# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Gmc, Ldp

class GmcAdmin(admin.ModelAdmin):
    list_display = ('gmc_name',)
    list_filter = ('gmc_name',)
    search_fields = ['gmc_name',]

class LdpAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'ldp_code', 'gmc')
    list_filter = ('site_name', 'ldp_code', 'gmc')
    search_fields = ['site_name', 'ldp_code']
    


admin.site.register(Gmc, GmcAdmin)
admin.site.register(Ldp, LdpAdmin)
# admin.site.register(Ods, OdsAdmin)
# admin.site.register(LdapGroup)