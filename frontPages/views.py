from django.shortcuts import render
from .models import (
    HeroSection,
    SectionData,
    CountSection,
    SkillSwap,
    WhyChooseUs,
    CtaModel,
)

def home(request):
    hero_section = HeroSection.objects.first()
    section_data = SectionData.objects.all()
    count_sections = CountSection.objects.all()
    skill_swaps = SkillSwap.objects.all()
    why_choose_us = WhyChooseUs.objects.all()
    cta_model = CtaModel.objects.first()

    context = {
        "hero_section": hero_section,
        "section_data": section_data,
        "count_sections": count_sections,
        "skill_swaps": skill_swaps,
        "why_choose_us": why_choose_us,
        "cta_model": cta_model,
    }
    return render(request, "pages/home.html", context)