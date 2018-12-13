from django_hosts import host, patterns

host_patterns = patterns(
    '',
    host(r'portal', 'portal.urls', name='portal'),
    host(r'forms', 'forms.urls', name='forms'),
)
