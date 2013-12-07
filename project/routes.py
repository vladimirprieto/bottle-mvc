from project import app
from project.controllers import *

app.route('/', 'GET', printer.index)
app.route('/print', ['GET', 'POST'], printer.printer)

# static files
app.route('/:file#(favicon.ico|humans.txt)#', 'GET', static.favicon)
app.route('/:path#(images|css|js|fonts)\/.+#', 'GET', static.server_static)
