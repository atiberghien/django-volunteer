from django.contrib import admin
from .models import Event, EventSlot, Volunteer
from django_mailman.models import List


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    
    csv_record_limit = 1000
    
    extra_csv_fields = ('first_name', 'last_name', 'email', 'phone')
    
    def get_actions(self, request):
        actions = self.actions if hasattr(self, 'actions') else []
        actions.append('csv_export')
        actions = super(VolunteerAdmin, self).get_actions(request)
        return actions
    
    def get_extra_csv_fields(self, request):
        return self.extra_csv_fields
    
    def csv_export(self, request, qs=None, *args, **kwargs):
        import csv
        from django.http import HttpResponse
        from django.template.defaultfilters import slugify

        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(self.model.__name__)
        headers = list(self.get_extra_csv_fields(request))
        writer = csv.DictWriter(response, headers)
        
        # Write header.
        header_data = {}
        print headers
        for name in headers:
            header_data[name] = name
        print header_data
        writer.writerow(header_data)
        
        # Write records.
        for r in qs[:self.csv_record_limit]:
            data = {}
            for name in headers:
                if hasattr(r, name):
                    data[name] = getattr(r, name)
                elif hasattr(self, name):
                    data[name] = getattr(self, name)(r)
                else:
                    raise Exception, 'Unknown field: %s' % (name,)
                    
                if callable(data[name]):
                    data[name] = data[name]()
            writer.writerow(data)
        return response
    csv_export.short_description = 'Exported selected %(verbose_name_plural)s as CSV'

admin.site.register(Event)
admin.site.register(EventSlot)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(List)