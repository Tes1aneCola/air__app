from modeltranslation.translator import translator, TranslationOptions
from .models import *


class PropertyTranslationOptions(TranslationOptions):
    fields = ('description', )

translator.register(Property, PropertyTranslationOptions)

