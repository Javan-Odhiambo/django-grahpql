from apps.accounts import schema as accounts_schema
import strawberry

@strawberry.type
class Query(accounts_schema.Query):
    pass


@strawberry.type
class Mutation(accounts_schema.Mutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
