import graphene
import cms.schema


class Query(cms.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
