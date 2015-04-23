var http = require('http')
var url = require('url')
var port = process.env.PORT || 8000

http.createServer(function (req, res) {
  var hello = {
    username: "codeart",
    permissions: ['create', 'update', 'list', 'read', 'delete'],
    groups: {group1: 'crlud', group2: 'cr', group3: 'crlu'}
  }

  var path = url.parse(req.url).pathname

  switch (path) {
  case '/json-response':
    res.writeHead(200, {'Content-Type': 'application/json; charset=UTF-8'})
    res.end(JSON.stringify(hello))
    break

  default:
    res.writeHead(501, {'Content-Type': 'text/plain; charset=UTF-8'})
    res.end("NOT IMPLEMENTED")
  }
}).listen(port, '127.0.0.1')