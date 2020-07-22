
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Member
from .models import Stuff
import graphene

class MemberType(DjangoObjectType):
    class Meta: 
        model= Member

class StuffType(DjangoObjectType):
    class Meta:
        model= Stuff

class Query(ObjectType):
    get_members= graphene.List(MemberType)
    get_member=graphene.Field(MemberType,id = graphene.Int(required= True))
    get_stuffs = graphene.List(StuffType)            
    get_stuff  = graphene.Field(StuffType,id=graphene.Int(required= True))

    def resolve_get_member(self, info, **kwargs):
        id= kwargs.get('id')
        return Member.objects.get(pk=id) 
    
    def resolve_get_members(self, info, **kwargs):
        return Member.objects.all()
    
    def resolve_get_stuff(self,info,**kwargs):
        id = kwargs.get('id')
        return Stuff.objects.get(pk=id)

    def resolve_get_stuffs(self,info,**kwargs):
        return Stuff.objects.all()

class MemberInput(graphene.InputObjectType):
    firstname = graphene.String()
    lastname = graphene.String()
    phonenumber = graphene.String()

class createMember(graphene.Mutation):
    class Arguments:
        data = MemberInput(required = True)
    
    Member = graphene.Field(MemberType)

    @staticmethod
    def mutate(root,info,**kwargs):
        data = kwargs.get('data')
        member_instance = Member(
            firstname = data.firstname,
            lastname = data.lastname,
            phonenumber = data.phonenumber
        )
        member_instance.save()
        return createMember(Member = member_instance)


class deleteMember(graphene.Mutation):
    class Arguments:
        id= graphene.Int(required = True)
        
    Member = graphene.Field(MemberType)
    
    @staticmethod
    def mutate(root, info,**kwargs):
        id=kwargs.get('id')
        member_instance = Member.objects.get(pk=id)
        member_instance.delete()
        return deleteMember(Member=None)

class updateMember(graphene.Mutation):
    class Arguments:
        id= graphene.Int(required = True)
    Member = graphene.Field(MemberType)

    @staticmethod
    def mutate (root,info,**kwargs):
        id= kwargs.get('id')
        member_instance = Member.objects.get(pk =id)
          member_instance = Member(
            firstname = data.firstname,
            lastname = data.lastname,
            phonenumber = data.phonenumber
        )
        if member_instance.firstname =! None
           firstname=member_instance.firstname
        if member_instance.lastname =! None
           lastname=member_instance.lastname
        if member_instance.phonenumber =! None
           phonenumber=member_instance.phonenumber
return deleteMember(Member=None)


class Mutation(graphene.ObjectType):
  create_member=createMember.Field()
  delete_member = deleteMember.Field()
    
schema= graphene.Schema(query=Query,mutation=Mutation)
