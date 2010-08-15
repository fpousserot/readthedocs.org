from django.conf.urls.defaults import *

urlpatterns = patterns('watching.views',
    url(r'^$',
        'project_index',
        name='projects_list'
    ),
    url(r'^tags/$',
        'tag_index',
        name='project_tag_list',
    ),
    url(r'^search/',
        'search',
        name='search',
    ),
    url(r'^tags/(?P<tag>\w+)/$',
        'project_index',
        name='project_tag_detail',
    ),
    url(r'^projects/(?P<username>\w+)/(?P<project_slug>[-\w]+)/$',
        'project_detail',
        name='projects_detail'
    ),
    url(r'^(?P<username>\w+)/$',
        'project_index',
        name='projects_user_list'
    ),
)