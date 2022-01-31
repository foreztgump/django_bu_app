from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
from myapp_bless.constants import W_GEAR_SCORES, OH_GEAR_SCORES, HEAD_GEAR_SCORES, CHEST_GEAR_SCORES, \
    PANTS_GEAR_SCORES, BOOTS_GEAR_SCORES, GLOVES_GEAR_SCORES, SHOULDER_GEAR_SCORES, BELT_GEAR_SCORES
from myapp_bless.forms import GearscoreForm, GearRunesForm, BaseATKForm


class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, "app/home.html")


class GSPage(TemplateView):
    template_name = "app/gs.html"

    def get(self, request, *args, **kwargs):
        form_class = GearscoreForm()
        return render(request, self.template_name, {'form': form_class})

    def post(self, request):
        form_class = GearscoreForm(request.POST)
        w_gear_score = 0
        if form_class.is_valid():
            w_gear_rank = form_class.cleaned_data['w_gear_rank']
            w_fort_rank = form_class.cleaned_data['w_fort_rank']
            w_fort_level = form_class.cleaned_data['w_fort_level']

            off_gear_rank = form_class.cleaned_data['off_gear_rank']
            off_fort_rank = form_class.cleaned_data['off_fort_rank']
            off_fort_level = form_class.cleaned_data['off_fort_level']

            head_gear_rank = form_class.cleaned_data['head_gear_rank']
            head_fort_rank = form_class.cleaned_data['head_fort_rank']
            head_fort_level = form_class.cleaned_data['head_fort_level']

            chest_gear_rank = form_class.cleaned_data['chest_gear_rank']
            chest_fort_rank = form_class.cleaned_data['chest_fort_rank']
            chest_fort_level = form_class.cleaned_data['chest_fort_level']

            pants_gear_rank = form_class.cleaned_data['pants_gear_rank']
            pants_fort_rank = form_class.cleaned_data['pants_fort_rank']
            pants_fort_level = form_class.cleaned_data['pants_fort_level']

            gloves_gear_rank = form_class.cleaned_data['gloves_gear_rank']
            gloves_fort_rank = form_class.cleaned_data['gloves_fort_rank']
            gloves_fort_level = form_class.cleaned_data['gloves_fort_level']

            boots_gear_rank = form_class.cleaned_data['boots_gear_rank']
            boots_fort_rank = form_class.cleaned_data['boots_fort_rank']
            boots_fort_level = form_class.cleaned_data['boots_fort_level']

            shoulder_gear_rank = form_class.cleaned_data['shoulder_gear_rank']
            shoulder_fort_rank = form_class.cleaned_data['shoulder_fort_rank']
            shoulder_fort_level = form_class.cleaned_data['shoulder_fort_level']

            belt_gear_rank = form_class.cleaned_data['belt_gear_rank']
            belt_fort_rank = form_class.cleaned_data['belt_fort_rank']
            belt_fort_level = form_class.cleaned_data['belt_fort_level']


            if 'calculate' in request.POST:
                # Weapon GS
                if int(w_gear_rank) == 1:
                    if int(w_fort_rank) == 1:
                        w_gear_score = W_GEAR_SCORES[int(w_fort_level)]
                    else:
                        w_gear_score = W_GEAR_SCORES[int(w_fort_level) + 6]
                elif int(w_gear_rank) == 0:
                    w_gear_score = 0
                else:
                    if int(w_fort_rank) == 1:
                        w_gear_score = W_GEAR_SCORES[int(w_fort_level) + 12]
                    else:
                        w_gear_score = W_GEAR_SCORES[int(w_fort_level) + 18]

                #Off-Hand GS
                if int(off_gear_rank) == 1:
                    if int(off_fort_rank) == 1:
                        oh_gear_score = OH_GEAR_SCORES[int(off_fort_level)]
                    else:
                        oh_gear_score = OH_GEAR_SCORES[int(off_fort_level) + 6]
                elif int(off_gear_rank) == 0:
                    oh_gear_score = 0
                else:
                    if int(off_fort_rank) == 1:
                        oh_gear_score = OH_GEAR_SCORES[int(off_fort_level) + 12]
                    else:
                        oh_gear_score = OH_GEAR_SCORES[int(off_fort_level) + 18]

                #Head GS
                if int(head_gear_rank) == 1:
                    if int(head_fort_rank) == 1:
                        head_gear_score = HEAD_GEAR_SCORES[int(head_fort_level)]
                    else:
                        head_gear_score = HEAD_GEAR_SCORES[int(head_fort_level) + 6]
                elif int(head_gear_rank) == 0:
                    head_gear_score = 0
                else:
                    if int(head_fort_rank) == 1:
                        head_gear_score = HEAD_GEAR_SCORES[int(head_fort_level) + 12]
                    else:
                        head_gear_score = HEAD_GEAR_SCORES[int(head_fort_level) + 18]

                #Chest GS
                if int(chest_gear_rank) == 1:
                    if int(chest_fort_rank) == 1:
                        chest_gear_score = CHEST_GEAR_SCORES[int(chest_fort_level)]
                    else:
                        chest_gear_score = CHEST_GEAR_SCORES[int(chest_fort_level) + 6]
                elif int(chest_gear_rank) == 0:
                    chest_gear_score = 0
                else:
                    if int(head_fort_rank) == 1:
                        chest_gear_score = CHEST_GEAR_SCORES[int(chest_fort_level) + 12]
                    else:
                        chest_gear_score = CHEST_GEAR_SCORES[int(chest_fort_level) + 18]

                #Pants GS
                if int(pants_gear_rank) == 1:
                    if int(pants_fort_rank) == 1:
                        pants_gear_score = PANTS_GEAR_SCORES[int(pants_fort_level)]
                    else:
                        pants_gear_score = PANTS_GEAR_SCORES[int(pants_fort_level) + 6]
                elif int(pants_gear_rank) == 0:
                    pants_gear_score = 0
                else:
                    if int(head_fort_rank) == 1:
                        pants_gear_score = PANTS_GEAR_SCORES[int(pants_fort_level) + 12]
                    else:
                        pants_gear_score = PANTS_GEAR_SCORES[int(pants_fort_level) + 18]

                #Boots GS
                if int(boots_gear_rank) == 1:
                    if int(boots_fort_rank) == 1:
                        boots_gear_score = BOOTS_GEAR_SCORES[int(boots_fort_level)]
                    else:
                        boots_gear_score = BOOTS_GEAR_SCORES[int(boots_fort_level) + 6]
                elif int(boots_gear_rank) == 0:
                    boots_gear_score = 0
                else:
                    if int(head_fort_rank) == 1:
                        boots_gear_score = BOOTS_GEAR_SCORES[int(boots_fort_level) + 12]
                    else:
                        boots_gear_score = BOOTS_GEAR_SCORES[int(boots_fort_level) + 18]

                #Gloves GS
                if int(gloves_gear_rank) == 1:
                    if int(gloves_fort_rank) == 1:
                        gloves_gear_score = GLOVES_GEAR_SCORES[int(gloves_fort_level)]
                    else:
                        gloves_gear_score = GLOVES_GEAR_SCORES[int(gloves_fort_level) + 6]
                elif int(gloves_gear_rank) == 0:
                    gloves_gear_score = 0
                else:
                    if int(head_fort_rank) == 1:
                        gloves_gear_score = GLOVES_GEAR_SCORES[int(gloves_fort_level) + 12]
                    else:
                        gloves_gear_score = GLOVES_GEAR_SCORES[int(gloves_fort_level) + 18]

                #Shoulder GS
                if int(shoulder_gear_rank) == 1:
                    if int(shoulder_fort_rank) == 1:
                        shoulder_gear_score = SHOULDER_GEAR_SCORES[int(shoulder_fort_level)]
                    else:
                        shoulder_gear_score = SHOULDER_GEAR_SCORES[int(shoulder_fort_level) + 6]
                elif int(shoulder_gear_rank) == 0:
                    shoulder_gear_score = 0
                else:
                    if int(head_fort_rank) == 1:
                        shoulder_gear_score = SHOULDER_GEAR_SCORES[int(shoulder_fort_level) + 12]
                    else:
                        shoulder_gear_score = SHOULDER_GEAR_SCORES[int(shoulder_fort_level) + 18]

                #Belt GS
                if int(belt_gear_rank) == 1:
                    if int(belt_fort_rank) == 1:
                        belt_gear_score = BELT_GEAR_SCORES[int(belt_fort_level)]
                    else:
                        belt_gear_score = BELT_GEAR_SCORES[int(belt_fort_level) + 6]
                elif int(belt_gear_rank) == 0:
                    belt_gear_score = 0
                else:
                    if int(head_fort_rank) == 1:
                        belt_gear_score = BELT_GEAR_SCORES[int(belt_fort_level) + 12]
                    else:
                        belt_gear_score = BELT_GEAR_SCORES[int(belt_fort_level) + 18]

                result = (w_gear_score + oh_gear_score + head_gear_score + chest_gear_score + pants_gear_score +
                        boots_gear_score + gloves_gear_score + shoulder_gear_score + belt_gear_score)


            #form_class = GearscoreForm()
            # return redirect ('home:home')

        args = {'form': form_class, 'w_gear_score': w_gear_score, 'oh_gear_score': oh_gear_score,
                'head_gear_score': head_gear_score, 'chest_gear_score': chest_gear_score,
                'pants_gear_score': pants_gear_score, 'boots_gear_score': boots_gear_score,
                'gloves_gear_score': gloves_gear_score, 'shoulder_gear_score': shoulder_gear_score,
                'belt_gear_score': belt_gear_score, 'result':result}
        return render(request, self.template_name, args)


class SkillProgression(TemplateView):
    template_name = "app/skill_pro.html"

    def get(self, request, *args, **kwargs):
        return render(request, "app/skill_pro.html")


class RuneDreaming(TemplateView):
    template_name = "app/rune_dreaming.html"

    def get(self, request, *args, **kwargs):
        form_class = GearRunesForm()
        return render(request, self.template_name, {'form': form_class})

    def post(self, request):
        form_class = GearRunesForm(request.POST)
        result_purple = 0
        result_white = 0
        result_yellow = 0
        result_green = 0
        result_red = 0
        if form_class.is_valid():
            w_rune_1 = form_class.cleaned_data['w_rune_1']
            w_rune_2 = form_class.cleaned_data['w_rune_2']
            w_rune_3 = form_class.cleaned_data['w_rune_3']
            w_rune_4 = form_class.cleaned_data['w_rune_4']
            w_rune_5 = form_class.cleaned_data['w_rune_5']

            off_rune_1 = form_class.cleaned_data['off_rune_1']
            off_rune_2 = form_class.cleaned_data['off_rune_2']
            off_rune_3 = form_class.cleaned_data['off_rune_3']
            off_rune_4 = form_class.cleaned_data['off_rune_4']
            off_rune_5 = form_class.cleaned_data['off_rune_5']

            head_rune_1 = form_class.cleaned_data['head_rune_1']
            head_rune_2 = form_class.cleaned_data['head_rune_2']
            head_rune_3 = form_class.cleaned_data['head_rune_3']
            head_rune_4 = form_class.cleaned_data['head_rune_4']
            head_rune_5 = form_class.cleaned_data['head_rune_5']

            chest_rune_1 = form_class.cleaned_data['chest_rune_1']
            chest_rune_2 = form_class.cleaned_data['chest_rune_2']
            chest_rune_3 = form_class.cleaned_data['chest_rune_3']
            chest_rune_4 = form_class.cleaned_data['chest_rune_4']
            chest_rune_5 = form_class.cleaned_data['chest_rune_5']

            pants_rune_1 = form_class.cleaned_data['pants_rune_1']
            pants_rune_2 = form_class.cleaned_data['pants_rune_2']
            pants_rune_3 = form_class.cleaned_data['pants_rune_3']
            pants_rune_4 = form_class.cleaned_data['pants_rune_4']
            pants_rune_5 = form_class.cleaned_data['pants_rune_5']

            gloves_rune_1 = form_class.cleaned_data['gloves_rune_1']
            gloves_rune_2 = form_class.cleaned_data['gloves_rune_2']
            gloves_rune_3 = form_class.cleaned_data['gloves_rune_3']
            gloves_rune_4 = form_class.cleaned_data['gloves_rune_4']
            gloves_rune_5 = form_class.cleaned_data['gloves_rune_5']

            boots_rune_1 = form_class.cleaned_data['boots_rune_1']
            boots_rune_2 = form_class.cleaned_data['boots_rune_2']
            boots_rune_3 = form_class.cleaned_data['boots_rune_3']
            boots_rune_4 = form_class.cleaned_data['boots_rune_4']
            boots_rune_5 = form_class.cleaned_data['boots_rune_5']

            shoulder_rune_1 = form_class.cleaned_data['shoulder_rune_1']
            shoulder_rune_2 = form_class.cleaned_data['shoulder_rune_2']
            shoulder_rune_3 = form_class.cleaned_data['shoulder_rune_3']
            shoulder_rune_4 = form_class.cleaned_data['shoulder_rune_4']
            shoulder_rune_5 = form_class.cleaned_data['shoulder_rune_5']

            belt_rune_1 = form_class.cleaned_data['belt_rune_1']
            belt_rune_2 = form_class.cleaned_data['belt_rune_2']
            belt_rune_3 = form_class.cleaned_data['belt_rune_3']
            belt_rune_4 = form_class.cleaned_data['belt_rune_4']
            belt_rune_5 = form_class.cleaned_data['belt_rune_5']

            if 'calculate' in request.POST:
                all_runes = []
                all_runes.append(int(w_rune_1))
                all_runes.append(int(w_rune_2))
                all_runes.append(int(w_rune_3))
                all_runes.append(int(w_rune_4))
                all_runes.append(int(w_rune_5))

                all_runes.append(int(off_rune_1))
                all_runes.append(int(off_rune_2))
                all_runes.append(int(off_rune_3))
                all_runes.append(int(off_rune_4))
                all_runes.append(int(off_rune_5))

                all_runes.append(int(head_rune_1))
                all_runes.append(int(head_rune_2))
                all_runes.append(int(head_rune_3))
                all_runes.append(int(head_rune_4))
                all_runes.append(int(head_rune_5))

                all_runes.append(int(chest_rune_1))
                all_runes.append(int(chest_rune_2))
                all_runes.append(int(chest_rune_3))
                all_runes.append(int(chest_rune_4))
                all_runes.append(int(chest_rune_5))

                all_runes.append(int(pants_rune_1))
                all_runes.append(int(pants_rune_2))
                all_runes.append(int(pants_rune_3))
                all_runes.append(int(pants_rune_4))
                all_runes.append(int(pants_rune_5))

                all_runes.append(int(gloves_rune_1))
                all_runes.append(int(gloves_rune_2))
                all_runes.append(int(gloves_rune_3))
                all_runes.append(int(gloves_rune_4))
                all_runes.append(int(gloves_rune_5))

                all_runes.append(int(boots_rune_1))
                all_runes.append(int(boots_rune_2))
                all_runes.append(int(boots_rune_3))
                all_runes.append(int(boots_rune_4))
                all_runes.append(int(boots_rune_5))

                all_runes.append(int(shoulder_rune_1))
                all_runes.append(int(shoulder_rune_2))
                all_runes.append(int(shoulder_rune_3))
                all_runes.append(int(shoulder_rune_4))
                all_runes.append(int(shoulder_rune_5))

                all_runes.append(int(belt_rune_1))
                all_runes.append(int(belt_rune_2))
                all_runes.append(int(belt_rune_3))
                all_runes.append(int(belt_rune_4))
                all_runes.append(int(belt_rune_5))

                for x in all_runes:
                    if x == 1:
                        result_purple += 1
                        result_white += 1
                        result_yellow += 1
                        result_green += 1
                        result_red += 1
                    elif x == 2:
                        result_red += 1
                    elif x == 3:
                        result_white += 1
                    elif x == 4:
                        result_yellow += 1
                    elif x == 5:
                        result_green += 1
                    elif x == 6:
                        result_purple += 1

        args = {'form': form_class, 'result_purple': result_purple, 'result_white': result_white,
                'result_yellow': result_yellow, 'result_green': result_green,
                'result_red': result_red}
        return render(request, self.template_name, args)


class BaseAtkCal(TemplateView):
    template_name = "app/baseatk.html"

    def get(self, request, *args, **kwargs):
        form_class = BaseATKForm()
        return render(request, self.template_name, {'form': form_class})

    def post(self, request):
        form_class = BaseATKForm(request.POST)
        result_attack = 0
        result_attack_output = 0
        result_attack_e_1_output = 0
        result_attack_e_2_output = 0
        result_attack_buff_output = 0
        result_attack_e_1 = 0
        result_attack_e_2 = 0
        result_cr_e_1 = 0
        result_cr_e_2 = 0
        result_cd_e_1 = 0
        result_cd_e_2 = 0
        result_ad_e_1 = 0
        result_ad_e_2 = 0
        result_attack_buff_plus = 0
        result_cr_buff_plus = 0
        result_cd_buff_plus = 0
        result_attack_buff = 0
        result_cr_buff = 0
        result_cd_buff = 0

        if form_class.is_valid():
            elixir = form_class.cleaned_data['elixir']
            panacea = form_class.cleaned_data['panacea']
            food = form_class.cleaned_data['food']
            base_atk = form_class.cleaned_data['base_atk']
            atk_bonus = form_class.cleaned_data['atk_bonus']
            crit_rate = form_class.cleaned_data['crit_rate']
            crit_dmg = form_class.cleaned_data['crit_dmg']
            all_dmg = form_class.cleaned_data['all_dmg']
            plus_atk_1 = form_class.cleaned_data['plus_atk_1']
            plus_atk_pct_1 = form_class.cleaned_data['plus_atk_pct_1']
            plus_cr_1 = form_class.cleaned_data['plus_cr_1']
            plus_cd_1 = form_class.cleaned_data['plus_cd_1']
            plus_all_dmg_1 = form_class.cleaned_data['plus_all_dmg_1']
            plus_atk_2 = form_class.cleaned_data['plus_atk_2']
            plus_atk_pct_2 = form_class.cleaned_data['plus_atk_pct_2']
            plus_cr_2 = form_class.cleaned_data['plus_cr_2']
            plus_cd_2 = form_class.cleaned_data['plus_cd_2']
            plus_all_dmg_2 = form_class.cleaned_data['plus_all_dmg_2']

            if 'calculate' in request.POST:
                result_attack = base_atk*(1+(atk_bonus/100))
                result_attack= round(result_attack, 1)
                result_attack_output = (result_attack*(1-(crit_rate/100))+result_attack*((crit_rate/100)*(crit_dmg/100)))*(1+(all_dmg/100))
                result_attack_output= round(result_attack_output, 1)

                result_attack_e_1 = (abs(base_atk)+plus_atk_1)*(1+(plus_atk_pct_1/100)+abs((atk_bonus/100)))
                result_attack_e_1 = round(result_attack_e_1, 1)
                result_cr_e_1 = abs(crit_rate)+plus_cr_1
                result_cd_e_1 = abs(crit_dmg)+plus_cd_1
                result_ad_e_1 = all_dmg+plus_all_dmg_1
                result_attack_e_1_output = (result_attack_e_1*(1-(result_cr_e_1/100))+result_attack_e_1*((result_cr_e_1/100)*(result_cd_e_1/100)))*(1+(result_ad_e_1/100))
                result_attack_e_1_output = round(result_attack_e_1_output, 1)

                result_attack_e_2 = (abs(base_atk) + plus_atk_2) * (1 + (plus_atk_pct_2/100) + abs((atk_bonus/100)))
                result_attack_e_2 = round(result_attack_e_2, 1)
                result_cr_e_2 = abs(crit_rate) + plus_cr_2
                result_cd_e_2 = abs(crit_dmg) + plus_cd_2
                result_ad_e_2 = all_dmg + plus_all_dmg_2
                result_attack_e_2_output = (result_attack_e_2 * (1 - (result_cr_e_2 / 100)) + result_attack_e_2 * (
                            (result_cr_e_2 / 100) * (result_cd_e_2 / 100))) * (1 + (result_ad_e_2 / 100))
                result_attack_e_2_output= round(result_attack_e_2_output, 1)

                if int(elixir) == 1:
                    result_attack_buff_plus += 15
                elif int(elixir) == 2:
                    result_cr_buff_plus += 4
                elif int(elixir) == 3:
                    result_cd_buff_plus += 18

                if int(panacea) == 1: #Blade
                    result_attack_buff_plus += 15
                elif int(panacea) == 2: #Superior Blade
                    result_attack_buff_plus += 20
                elif int(panacea) == 3: #Destruction
                    result_cd_buff_plus += 30
                elif int(panacea) == 4: #Superior Destruction
                    result_cd_buff_plus += 36
                elif int(panacea) == 5: #Hunter
                    result_cr_buff_plus += 6
                elif int(panacea) == 6: #Superior Sharpness
                    result_cr_buff_plus += 7.5

                if int(food) == 1: #Beef Curry
                    result_cd_buff_plus += 24
                elif int(food) == 2: #Tiger Shrimp
                    result_cr_buff_plus += 4.5

                result_attack_buff = abs(base_atk)*(1+(result_attack_buff_plus/100)+(atk_bonus/100))
                result_attack_buff = round(result_attack_buff, 1)
                result_cr_buff = abs(crit_rate) + result_cr_buff_plus
                result_cd_buff = abs(crit_dmg) + result_cd_buff_plus
                result_attack_buff_output = (result_attack_buff*(1-(result_cr_buff/100))+result_attack_buff*((result_cr_buff/100)*(result_cd_buff/100)))*(1+(all_dmg/100))
                result_attack_buff_output = round(result_attack_buff_output, 1)

            args = {'form': form_class, 'result_attack': result_attack, 'result_attack_output': result_attack_output,
                    'result_attack_e_1_output': result_attack_e_1_output, 'result_attack_e_2_output': result_attack_e_2_output,
                    'result_attack_buff_output': result_attack_buff_output, 'result_attack_e_1': result_attack_e_1,
                    'result_attack_e_2': result_attack_e_2, 'result_cr_e_1': result_cr_e_1, 'result_cd_e_2': result_cd_e_2,
                    'result_cr_e_2': result_cr_e_2, 'result_ad_e_1': result_ad_e_1, 'result_ad_e_2': result_ad_e_2,
                    'result_attack_buff_plus': result_attack_buff_plus, 'result_cr_buff_plus': result_cr_buff_plus,
                    'result_cd_buff_plus': result_cd_buff_plus, 'result_attack_buff': result_attack_buff,
                    'result_cr_buff': result_cr_buff, 'result_cd_buff': result_cd_buff, 'result_cd_e_1': result_cd_e_1}
            return render(request, self.template_name, args)