import sys, bottle, sqlite3, json

sys.path.insert(0, 'classes')
from inventorydao import InventoryDAO

# Turn on debug mode - templates will not be cached
bottle.debug(True)

# This tells Bottle where to find the views
bottle.TEMPLATE_PATH.append('views')

# Data
dbConn = sqlite3.connect('data/database.db')
dbConn.row_factory = sqlite3.Row

# Data Abstraction Objects
invDAO = InventoryDAO(dbConn)
categories = invDAO.getCategories()

# Routing
@bottle.get('/static/<filepath:path>')
def static(filepath):
    return bottle.static_file(filepath, root='static')

@bottle.get('/')
def index():
    return bottle.template('index', {
        'categories': invDAO.getCategories()
    })

bottle.run()
