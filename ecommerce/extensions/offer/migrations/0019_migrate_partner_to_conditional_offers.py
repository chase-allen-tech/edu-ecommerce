# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 11:25


from django.db import migrations


def add_partner_to_conditional_offers(apps, schema_editor):
    ConditionalOffer = apps.get_model("offer", "ConditionalOffer")

    for conditional_offer in ConditionalOffer.objects.all():
        site_configuration = conditional_offer.site.siteconfiguration if conditional_offer.site else None
        if site_configuration:
            conditional_offer.partner = site_configuration.partner
            conditional_offer.save()


def reverse_add_partner_to_conditional_offers(apps, schema_editor):
    ConditionalOffer = apps.get_model("offer", "ConditionalOffer")

    for conditional_offer in ConditionalOffer.objects.all():
        site_configuration = conditional_offer.site.siteconfiguration if conditional_offer.site else None
        if site_configuration and conditional_offer.partner != site_configuration.partner:
            site_configuration.partner = conditional_offer.partner
            site_configuration.save()


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0018_conditionaloffer_partner'),
    ]

    operations = [
        migrations.RunPython(add_partner_to_conditional_offers, reverse_add_partner_to_conditional_offers),
    ]