from prjct import schema as prjct_schema
import graphene


class Query(
        prjct_schema.Query,
        graphene.ObjectType):
    pass
 
class Mutation(
    prjct_schema.Mutation,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
