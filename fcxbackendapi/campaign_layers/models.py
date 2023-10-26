from django.db import models

# Create your models here.
   
class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class DOI(models.Model):
    long_name = models.CharField(max_length=100)
    instrument_short_name = models.CharField(max_length=100)
    doi_url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.short_name

class Legend(models.Model):
    instrument_short_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

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
    

class CampaignLayer(models.Model):
    title = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    link = models.ForeignKey(
        Link, related_name = 'campaign_layers', on_delete=models.CASCADE
    )
    doi = models.ForeignKey(
        DOI, related_name = 'campaign_layers', on_delete=models.CASCADE
    )
    legend = models.ForeignKey(
        Legend, related_name = 'campaign_layers', on_delete=models.CASCADE
    )
    instrument_layer = models.ForeignKey(
        InstrumentLayer, related_name = 'campaign_layers', on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title