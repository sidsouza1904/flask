# Dicionário de permissões
mapping_roles = {
    # chave = rota, valor = lista de cargos que podem acessar esta rota
    'login': ['user', 'manager', 'admin', 'superuser'],
    'register': ['user', 'manager', 'admin', 'superuser'],
    'user_list': ['admin', 'superuser'],
    'user_create': ['admin', 'superuser'],
    'user_update': ['admin', 'superuser'],
    'user_delete': ['admin', 'superuser'],
    'home': ['user', 'manager', 'admin', 'superuser'],
}