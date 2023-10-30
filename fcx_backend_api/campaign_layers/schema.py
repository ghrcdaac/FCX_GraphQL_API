import graphene
from graphene_django import DjangoObjectType

from fcx_backend_api.campaign_layers.models import CampaignLayer, Link, DOI, Legend, InstrumentLayer

class CampaignLayerType(DjangoObjectType):
    class Meta:
        model = CampaignLayer
        fields = ("id", "name", "title", "logo_url", "description", "links", "dois", "legends", "instrumentlayers")

class LinkType(DjangoObjectType):
    class Meta:
        model = Link
        fields = ("id", "title", "url", "campaign_layer")

class DOIType(DjangoObjectType):
    class Meta:
        model = DOI
        fields = ("id", "long_name", "instrument_short_name", "url", "campaign_layer")

class LegendType(DjangoObjectType):
    class Meta:
        model = Legend
        fields = ("id", "instrument_short_name", "url", "color", "campaign_layer")

class InstrumentLayerType(DjangoObjectType):
    class Meta:
        model = InstrumentLayer
        fields = ("id", "layer_id", "date", "instrument_short_name", "display_name", "type", "platform", "display_mechanism", "url", "unit", "variable_name", "add_tick_event_listner", "field_campaign_name", "campaign_layer")

class Query(graphene.ObjectType):
    # Query Fields, which are the endpoints that we can use to query the data
    # To list all. (/list)
    campaign_layers = graphene.List(CampaignLayerType)
    links = graphene.List(LinkType)
    dois = graphene.List(DOIType)
    legends = graphene.List(LegendType)
    instrument_layers = graphene.List(InstrumentLayerType)
    # To get specific (/get)
    campaign_layer_by_name = graphene.Field(CampaignLayerType, name=graphene.String(required=True))
    instrument_layer_by_name = graphene.Field(InstrumentLayerType, name=graphene.String(required=True))
    instrument_layer_by_type = graphene.List(InstrumentLayerType, type=graphene.String(required=True))
    instrument_layer_by_platform = graphene.List(InstrumentLayerType, platform=graphene.String(required=True))

    # Resolvers, which are functions that tell graphene where to get the data from
    def resolve_campaign_layers(root, info):
        return CampaignLayer.objects.all()

    def resolve_links(root, info):
        return Link.objects.select_related("campaign_layer").all()

    def resolve_dois(root, info):
        return DOI.objects.select_related("campaign_layer").all()

    def resolve_legends(root, info):
        return Legend.objects.select_related("campaign_layer").all()

    def resolve_instrument_layers(root, info):
        return InstrumentLayer.objects.select_related("campaign_layer").all()

    def resolve_campaign_layer_by_name(root, info, name):
        try:
            return CampaignLayer.objects.get(name=name)
        except CampaignLayer.DoesNotExist:
            return None

    def resolve_instrument_layer_by_name(root, info, name):
        try:
            return InstrumentLayer.objects.get(instrument_short_name=name)
        except InstrumentLayer.DoesNotExist:
            return None

    def resolve_instrument_layer_by_type(root, info, type):
        try:
            return InstrumentLayer.objects.filter(type=type)
        except InstrumentLayer.DoesNotExist:
            return None

    def resolve_instrument_layer_by_platform(root, info, platform):
        try:
            return InstrumentLayer.objects.filter(platform=platform)
        except InstrumentLayer.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)