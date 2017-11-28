catalog = self.sq_connect.connect_api('/v2/catalog/list')
		catalog_data = catalog.json()
		data = [item for item in catalog_data['objects'] if 'category_data' in item]
		category_data = {}

		for i in range(len(data)):
			category_data[i] = { 'name': data[i]['category_data']['name'], 'id': data[i]['id'], 'updated': data[i]['updated_at']}

		print(category_data[0]['name'], category_data[0]['id'], category_data[0]['updated'])