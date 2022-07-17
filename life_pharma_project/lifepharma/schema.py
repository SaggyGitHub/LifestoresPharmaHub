from pyexpat import model
import graphene
from graphene_django import DjangoObjectType
from .models import Pharma

class PharmaType(DjangoObjectType):
    class Meta:  
        model = Pharma 
        fields = (
            'name', 'description', 'sku', 'price', 'image'
        )

class Query(graphene.ObjectType):
    pharmas = graphene.List(PharmaType)

    def resolve_pharmas(root, info, **kwargs):

        return Pharma.objects.all()

schema = graphene.Schema(query=Query)