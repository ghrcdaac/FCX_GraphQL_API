from django.db import models

# Create your models here.

class CampaignLayer(models.Model):
    title = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
   
class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    campaign_layer = models.ForeignKey(
        CampaignLayer, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title

class DOI(models.Model):
    long_name = models.CharField(max_length=100)
    instrument_short_name = models.CharField(max_length=100)
    doi_url = models.CharField(max_length=100)
    campaign_layer = models.ForeignKey(
        CampaignLayer, on_delete=models.CASCADE, null=True
    )
    
    def __str__(self):
        return self.instrument_short_name

class Legend(models.Model):
    instrument_short_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    campaign_layer = models.ForeignKey(
        CampaignLayer, on_delete=models.CASCADE, null=True
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
    url = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    add_tick_event_listner = models.BooleanField()
    campaign_layer = models.ForeignKey(
        CampaignLayer, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.instrument_short_name

