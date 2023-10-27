import graphene
from graphene_django import DjangoObjectType

from fcx_backend_api.campaign_layers.models import CampaignLayer, Link, DOI, Legend, InstrumentLayer

class CampaignLayerType(DjangoObjectType):
    class Meta:
        model = CampaignLayer
        fields = ("id", "title", "logo_url", "description", "links", "dois", "legends", "instrumentlayers")

class LinkType(DjangoObjectType):
    class Meta:
        model = Link
        fields = ("id", "title", "url", "campaign_layer")

class DOIType(DjangoObjectType):
    class Meta:
        model = DOI
        fields = ("id", "long_name", "instrument_short_name", "doi_url", "campaign_layer")

class LegendType(DjangoObjectType):
    class Meta:
        model = Legend
        fields = ("id", "instrument_short_name", "url", "color", "campaign_layer")

class InstrumentLayerType(DjangoObjectType):
    class Meta:
        model = InstrumentLayer
        fields = ("id", "layer_id", "date", "instrument_short_name", "display_name", "type", "platform", "display_mechanism", "url", "unit", "add_tick_event_listner", "campaign_layer")

class Query(graphene.ObjectType):
    campaign_layers = graphene.List(CampaignLayerType)
    links = graphene.List(LinkType)
    dois = graphene.List(DOIType)
    legends = graphene.List(LegendType)
    instrument_layers = graphene.List(InstrumentLayerType)

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

schema = graphene.Schema(query=Query)