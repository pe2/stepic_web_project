import urlparse
def hello(environ, start_response):
	
	d = urlparse.parse_qs(environ["QUERY_STRING"])
	status = "200 OK"
	headers = [
		('Content-type', 'text/plain')
	]
	body = ""
	for k in sorted(d.iterkeys()):
		body += k + "="
		body += "=".join(d[k]) + "\n"
	start_response(status, headers)
	return [ body ]

