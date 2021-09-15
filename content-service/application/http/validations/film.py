create = {
      'name': {'type': 'string', 'required': True},
      'description': {'type':'string','required':True},
      'fragman':{'type':'string','required':True},
      'cover':{'type':'string','required':True},
      'year':{'type':'integer','required':True},
      'category_id':{'type':'integer','required':True},
}

show = {
      'slug': {'type': 'string', 'required': True}
}

delete = {
      'slug': {'type': 'string', 'required': True}
}

update = {
      'name': {'type': 'string', 'required': True},
      'description': {'type':'string','required':True},
      'fragman':{'type':'string','required':True},
      'cover':{'type':'string','required':True},
      'year':{'type':'integer','required':True},
      'category_id':{'type':'integer','required':True},
      'slug': {'type': 'string', 'required': True}
}

