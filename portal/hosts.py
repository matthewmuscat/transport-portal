from django_hosts import host, patterns

host_patterns = patterns(
    '',
    host(r'portal', 'portal.urls', name='portal'),
    host(r'forms', 'driver_forms.urls', name='forms'),
)
