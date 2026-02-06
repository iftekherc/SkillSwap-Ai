from django.contrib import admin
from .models import (
    HeroSection,
    SectionData,
    CountSection,
    SkillSwap,
    WhyChooseUs,
    CtaModel,
)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "tagline")
    search_fields = ("title", "tagline")
    list_filter = ("title",)


@admin.register(SectionData)
class SectionDataAdmin(admin.ModelAdmin):
    list_display = ("section_name", "title")
    search_fields = ("section_name", "title")
    list_filter = ("section_name",)


@admin.register(CountSection)
class CountSectionAdmin(admin.ModelAdmin):
    list_display = ("count_number", "count_text")
    search_fields = ("count_text",)


class CardModelAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(SkillSwap)
class SkillSwapAdmin(CardModelAdmin):
    pass


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(CardModelAdmin):
    pass


@admin.register(CtaModel)
class CtaModelAdmin(admin.ModelAdmin):
    list_display = ("title", "button_text")
    search_fields = ("title", "button_text")
