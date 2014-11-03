from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'l4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Films.views.GetMain'),
    url(r'^select/film/$', 'Films.views.GetAllFilm'),
    url(r'^select/cinema/$', 'Films.views.GetAllCinema'),
    url(r'^select/session/$', 'Films.views.GetAllSession'),
    url(r'^update/film/(\d*)/$',    'Films.views.UpdateFilm'),
    url(r'^update/cinema/(\d*)/$',    'Films.views.UpdateCinema'),
    url(r'^update/session/(\d*)/$',    'Films.views.UpdateSession'),
    url(r'^delete/film/(\d*)/$', 'Films.views.DeleteFilm'),
    url(r'^delete/cinema/(\d*)/$', 'Films.views.DeleteCinema'),
    url(r'^delete/session/(\d*)/$', 'Films.views.DeleteSession'),
    url(r'^add/film/$', 'Films.views.CreateFilm'),    
    url(r'^add/cinema/$', 'Films.views.CreateCinema'),    
    url(r'^add/session/$', 'Films.views.CreateSession'),   
    url(r'^film/(\d*)/$', 'Films.views.GetFilmInfo'),    
    url(r'^cinema/(\d*)/$', 'Films.views.GetCinemaInfo'),    
    url(r'^session/(\d*)/$', 'Films.views.GetSessionInfo'),     
)
