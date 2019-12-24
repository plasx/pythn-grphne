import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info, limit=None):
        return [
            User(id="1", username="Fredrico", created_at=datetime.now()),
            User(id="2", username="Essentia", created_at=datetime.now()),
        ][:limit]



schema = graphene.Schema(query=Query)
result = schema.execute(
    '''
    {
        users {
            id
            username
            createdAt
        }
    }
    '''
)

dictResult= dict(result.data.items())
print(json.dumps(dictResult, indent=2))
