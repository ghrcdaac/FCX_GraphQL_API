from django.db import models

# Create your models here.

class CampaignLayer(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    logo_url = models.URLField(max_length=2049)
    description = models.TextField()

    def __str__(self):
        return self.title
   
class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=2049)
    campaign_layer = models.ForeignKey(
        CampaignLayer, related_name="links", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title

class DOI(models.Model):
    long_name = models.CharField(max_length=100)
    instrument_short_name = models.CharField(max_length=100)
    url = models.URLField(max_length=2049)
    campaign_layer = models.ForeignKey(
        CampaignLayer, related_name="dois", on_delete=models.CASCADE, null=True
    )
    
    def __str__(self):
        return self.instrument_short_name

class Legend(models.Model):
    instrument_short_name = models.CharField(max_length=100)
    url = models.URLField(max_length=2049)
    color = models.CharField(max_length=100)
    campaign_layer = models.ForeignKey(
        CampaignLayer, related_name="legends", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.instrument_short_name

class InstrumentLayer(models.Model):
    layer_id = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    instrument_short_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100) # multiple level attribute
    platform = models.CharField(max_length=100) # multiple level attribute
    display_mechanism = models.CharField(max_length=100) # multiple level attribute
    url = models.URLField(max_length=2049)
    unit = models.CharField(max_length=100)
    variable_name = models.CharField(max_length=500, null=True)
    field_campaign_name = models.CharField(max_length=100)
    add_tick_event_listner = models.BooleanField()
    campaign_layer = models.ForeignKey(
        CampaignLayer, related_name="instrumentlayers", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.instrument_short_name

