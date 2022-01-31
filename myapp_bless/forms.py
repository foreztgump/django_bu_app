from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import BaseFormSet, formset_factory

from bootstrap5.widgets import RadioSelectButtonGroup

from myapp_bless.constants import FORT_RANK_CHOICE, FORT_LEVEL_CHOICE, GEAR_RANK_CHOICE, RUNE_COLORS_CHOICE, \
    ELIXIR_CHOICE, PANACEA_CHOICE, FOOD_CHOICE


class GearscoreForm(forms.Form):
    w_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    w_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    w_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)
    off_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    off_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    off_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)
    head_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    head_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    head_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)
    chest_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    chest_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    chest_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)
    pants_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    pants_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    pants_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)
    gloves_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    gloves_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    gloves_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)
    boots_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    boots_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    boots_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)
    shoulder_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    shoulder_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    shoulder_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)
    belt_gear_rank = forms.ChoiceField(choices=GEAR_RANK_CHOICE, initial=0)
    belt_fort_rank = forms.ChoiceField(choices=FORT_RANK_CHOICE, initial=0)
    belt_fort_level = forms.ChoiceField(choices=FORT_LEVEL_CHOICE, initial=0)


class GearRunesForm(forms.Form):
    w_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    w_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    w_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    w_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    w_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    off_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    off_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    off_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    off_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    off_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    head_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    head_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    head_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    head_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    head_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    chest_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    chest_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    chest_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    chest_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    chest_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    pants_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    pants_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    pants_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    pants_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    pants_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    gloves_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    gloves_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    gloves_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    gloves_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    gloves_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    boots_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    boots_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    boots_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    boots_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    boots_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    shoulder_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    shoulder_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    shoulder_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    shoulder_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    shoulder_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    belt_rune_1 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    belt_rune_2 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    belt_rune_3 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    belt_rune_4 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)
    belt_rune_5 = forms.ChoiceField(choices=RUNE_COLORS_CHOICE, initial=0)


class BaseATKForm(forms.Form):
    elixir = forms.ChoiceField(choices=ELIXIR_CHOICE, initial=0)
    panacea = forms.ChoiceField(choices=PANACEA_CHOICE, initial=0)
    food = forms.ChoiceField(choices=FOOD_CHOICE, initial=0)
    base_atk = forms.FloatField(initial=0.0)
    atk_bonus = forms.FloatField(initial=0.0)
    crit_rate = forms.FloatField(initial=0.0)
    crit_dmg = forms.FloatField(initial=0.0)
    all_dmg = forms.FloatField(initial=0.0)
    plus_atk_1 = forms.FloatField(initial=0.0)
    plus_atk_pct_1 = forms.FloatField(initial=0.0)
    plus_cr_1 = forms.FloatField(initial=0.0)
    plus_cd_1 = forms.FloatField(initial=0.0)
    plus_all_dmg_1 = forms.FloatField(initial=0.0)
    plus_atk_2 = forms.FloatField(initial=0.0)
    plus_atk_pct_2 = forms.FloatField(initial=0.0)
    plus_cr_2 = forms.FloatField(initial=0.0)
    plus_cd_2 = forms.FloatField(initial=0.0)
    plus_all_dmg_2 = forms.FloatField(initial=0.0)