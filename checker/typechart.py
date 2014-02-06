from pokedex.db import connect, tables, util
session = connect()
query = session.query(tables.Type)
print type(query)
for (i, type) in enumerate(query):
    effs = type.damage_efficacies
    print i, type.name
#    print effs[type.id].target_type.name
#    print effs[0].damage_type.name
#    print effs[0].target_type.name
#    print effs[0].damage_factor
#    print '{0} {1}'.format(type.name, #
