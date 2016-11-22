urlpatterns = patterns('qa.views',
	url(r'^$','test', name='root'),
	url(r'^login/.*$','test', name='login'),
)
