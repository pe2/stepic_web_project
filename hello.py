def hello(environ, start_respopnse):
	
	status = "200 OK"
	headers = [
		('Content-type', 'text/plain')
	]
	body = "Hello world"
	start_response(status, headers)
	return [ body ]

