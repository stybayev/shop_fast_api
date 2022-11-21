from fastapi import APIRouter
from type.routes import Query, Mutation
from strawberry.asgi import GraphQL
import strawberry
shop = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

shop.add_route("/graphql", graphql_app)
