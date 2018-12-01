class InventoryDAO:
    def __init__(self, dbConn):
        self.dbConn = dbConn
        self.cursor = dbConn.cursor()

    def getCategories(self, encrypt=False):
        categories = []
        query = '''
            SELECT category_id
                ,name
                ,description
            FROM categories
            ORDER BY name
        '''

        for row in self.cursor.execute(query):
            categories.append({
                'category_id': row['category_id'],
                'name': row['name'],
                'description': row['description']
            })

        return categories
