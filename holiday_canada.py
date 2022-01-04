#!/usr/bin/env python


from datetime import date

from pymeeus.Sun import Sun

from paper_cal import (closest_day, SUN, MON, TUE, SAT, WEEK1, WEEK2, WEEK3,
                       JAN, FEB, MAY, JUL, AUG, SEP, OCT, NOV, DEC)


def main():

    # https://en.wikipedia.org/wiki/Public_holidays_in_Canada
    # https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada

    for year in (2022, 2023):
        # New Year's Day is January 1st
        #   https://en.wikipedia.org/wiki/New_Year's_Day
        #   https://fr.wikipedia.org/wiki/Jour_de_l%27an
        print(f'{date(year, JAN, 1)} New Year\'s Day')
        # Jour de l'an
        if date.weekday(date(year, JAN, 1)) == SAT \
                or date.weekday(date(year, JAN, 1)) == SUN:
            print(f'{closest_day(MON, date(year, JAN, 1))} New Year\'s Day (observed)')
            # Jour de l'an (observé)

        # Groundhog Day is February 2nd
        #   https://en.wikipedia.org/wiki/Groundhog_Day
        #   https://fr.wikipedia.org/wiki/Jour_de_la_marmotte
        print(f'{date(year, FEB, 2)} Groundhog Day')
        # Jour de la marmotte

        # National Flag of Canada Day is February 15th
        #   https://en.wikipedia.org/wiki/National_Flag_of_Canada_Day
        #   https://fr.wikipedia.org/wiki/Jour_du_drapeau_national_du_Canada
        print(f'{date(year, FEB, 15)} National Flag of Canada Day')
        # Jour du drapeau national du Canada

        # The 3rd Monday in February is observed in 8 provinces and 0
        # territories...
        #     CA-AB:  Family Day;  statutory
        #     CA-BC:  Family Day;  statutory
        #     CA-MB:  Louis Riel Day;  statutory
        #     CA-NB:  Family Day;  statutory
        #     CA-ON:  Family Day;  statutory
        #     CA-NS:  Heritage Day;  ?
        #     CA-PE:  Islander Day;  statutory
        #     CA-SK:  Family Day;  statutory
        #   https://en.wikipedia.org/wiki/Family_Day
        #   https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
        print(f'{closest_day(MON, date(year, FEB, WEEK3))} Family Day')
        # Fête de la famille
        # Journée Louis Riel (CA-MB)
        # Fête des Insulaires (CA-PE)
        # Fête du Patrimoine (CA-NS)

        # March break
        # Congé de mars

        #   https://en.wikipedia.org/wiki/Spring_break
        # Spring break
        # Congé de printemps

        spring_equinox = Sun.get_equinox_solstice(year, target='spring')
        summer_solstice = Sun.get_equinox_solstice(year, target='summer')
        autumn_equinox = Sun.get_equinox_solstice(year, target='autumn')
        winter_solstice = Sun.get_equinox_solstice(year, target='winter')

        _, temp_month, temp_day, _, _, _ = spring_equinox.get_full_date()
        print(f'{date(year, temp_month, temp_day)} First day of Spring')
        _, temp_month, temp_day, _, _, _ = summer_solstice.get_full_date()
        print(f'{date(year, temp_month, temp_day)} First day of Summer')
        _, temp_month, temp_day, _, _, _ = autumn_equinox.get_full_date()
        print(f'{date(year, temp_month, temp_day)} First day of Fall')
        _, temp_month, temp_day, _, _, _ = winter_solstice.get_full_date()
        print(f'{date(year, temp_month, temp_day)} First day of Winter')

        # Easter is the 1st Sunday after the 1st full moon after the Spring
        # equinox
        # (min:  March 22nd, max:  April 25th)
        #   https://en.wikipedia.org/wiki/Ecclesiastical_full_moon#Paschal_full_moon
        #   https://en.wikipedia.org/wiki/Computus
        #   https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques
        #   https://en.wikipedia.org/wiki/Shrove_Tuesday
        #   https://fr.wikipedia.org/wiki/Mardi_gras
        #   https://en.wikipedia.org/wiki/Ash_Wednesday
        #   https://fr.wikipedia.org/wiki/Mercredi_des_Cendres
        #   https://en.wikipedia.org/wiki/Palm_Sunday
        #   https://fr.wikipedia.org/wiki/Dimanche_des_Rameaux
        #   https://en.wikipedia.org/wiki/Maundy_Thursday
        #   https://fr.wikipedia.org/wiki/Jeudi_saint
        #   https://en.wikipedia.org/wiki/Good_Friday
        #   https://fr.wikipedia.org/wiki/Vendredi_saint
        #   https://en.wikipedia.org/wiki/Easter
        #   https://fr.wikipedia.org/wiki/P%C3%A2ques
        #   https://en.wikipedia.org/wiki/Feast_of_the_Ascension
        #   https://fr.wikipedia.org/wiki/Ascension_(f%C3%AAte)
        #   https://en.wikipedia.org/wiki/Pentecost
        #   https://fr.wikipedia.org/wiki/Pentec%C3%B4te
        # REM  [trigger(easter-47)] +1 PRIORITY 1000 \
        #   MSG %"[babel("Shrove/Pancake Tuesday", "Mardi Gras")]%" %b%
        # REM  [trigger(easter-46)] +1 PRIORITY 1000 \
        #   MSG %"[babel("Ash Wednesday", "Mercredi des Cendres")]%" %b%
        # REM  [trigger(easter-7)]  +1 PRIORITY 1000 \
        #   MSG %"[babel("Palm Sunday", "Dimanche des Rameaux")]%" %b%
        # REM  [trigger(easter-3)]  +1 PRIORITY 1000 \
        #   MSG %"[babel("Maundy Thursday", "Jeudi saint")]%" %b%
        # OMIT [trigger(easter-2)]  +1 PRIORITY 1000 \
        #   MSG %"[babel("Good Friday", "Vendredi saint")]%" %b%
        # OMIT [trigger(easter)]    +1 PRIORITY 1000 \
        #   MSG %"[babel("Easter Sunday", "Le dimanche de Pâques")]%" %b%
        # REM  [trigger(easter+1)]  +1 PRIORITY 1000 \
        #   MSG %"[babel("Easter Monday", "Le lundi de Pâques")]%" %b%
        # REM  [trigger(easter+39)] +1 PRIORITY 1000 \
        #   MSG %"[babel("Ascension", "Ascension")]%" %b%
        # REM  [trigger(easter+49)] +1 PRIORITY 1000 \
        #   MSG %"[babel("Pentecost", "Pentecôte")]%" %b%

        # Victoria Day is the Monday on or before May 24th
        # (or the last Monday preceeding May 25th)
        #   https://en.wikipedia.org/wiki/Victoria_Day
        #   https://en.wikipedia.org/wiki/National_Patriots%27_Day
        #   https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Reine_(Canada)
        print(f'{closest_day(MON, date(year, MAY, 21))} Victoria Day')
        # Fête de la Reine
        # Fête de Victoria
        # Journée nationale des patriotes (CA-QC)

        # Canada Day is July 1st
        #   https://en.wikipedia.org/wiki/Canada_Day
        #   https://fr.wikipedia.org/wiki/F%C3%AAte_du_Canada
        print(f'{date(year, JUL, 1)} Canada Day')
        # Fête du Canada
        if date.weekday(date(year, JUL, 1)) == SAT \
                or date.weekday(date(year, JUL, 1)) == SUN:
            print(f'{closest_day(MON, date(year, JUL, 1))} Canada Day (observed)')
            # Fête du Canada (observé)

        # The 1st Monday in August is a quasi-semi-poly-un-statutory holiday,
        # kinda...
        #     CA-AB:  Heritage Day;  optional, formerly statutory
        #     CA-BC:  British Columbia Day;  statutory
        #     CA-MB:  Civic Holiday;  non-statutory
        #     CA-NB:  New Brunswick Day;  statutory
        #     CA-NL:  not observed
        #     CA-NS:  Natal Day;  non-statutory
        #     CA-NT:  Civic Holiday;  statutory
        #     CA-NU:  Civic Holiday;  statutory
        #     CA-ON:  Civic Holiday and Simcoe Day;  non-statutory
        #     CA-PE:  Civic Holiday;  statutory or non-statutory
        #     CA-QC:  not observed
        #     CA-SK:  Saskatchewan Day;  statutory
        #     CA-YT:  not observed
        #   https://en.wikipedia.org/wiki/Civic_Holiday
        #   https://en.wikipedia.org/wiki/Public_holidays_in_Canada
        #   https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
        print(f'{closest_day(MON, date(year, AUG, WEEK1))} August Civic Holiday')
        # Premier lundi d'août
        # Longue fin de semaine d'aôut

        # Labour Day is the 1st Monday in September
        #   https://en.wikipedia.org/wiki/Labour_Day
        #   https://fr.wikipedia.org/wiki/F%C3%AAte_du_Travail
        print(f'{closest_day(MON, date(year, SEP, WEEK1))} Labour Day')
        # Fête du Travail

        # Canadian Thanksgiving is the 2nd Monday in October
        #   https://en.wikipedia.org/wiki/Thanksgiving#Canada
        #   https://fr.wikipedia.org/wiki/Action_de_gr%C3%A2ce_(Canada)
        print(f'{closest_day(MON, date(year, OCT, WEEK2))} Thanksgiving Day')
        # Action de Grâce

        # Rememberance Day is November 11th
        #   https://en.wikipedia.org/wiki/Remembrance_Day
        #   https://fr.wikipedia.org/wiki/Jour_du_Souvenir
        print(f'{date(year, NOV, 11)} Rememberance Day')
        # Jour du Souvenir

        # Christmas Eve is December 24th
        print(f'{date(year, DEC, 24)} Christmas Eve')
        # Veille de Noël

        # Christmas Day is December 25th
        #   https://en.wikipedia.org/wiki/Christmas
        #   https://fr.wikipedia.org/wiki/No%C3%ABl
        # Boxing Day is December 26th
        #   https://en.wikipedia.org/wiki/Boxing_Day
        #   https://fr.wikipedia.org/wiki/Boxing_Day
        print(f'{date(year, DEC, 25)} Christmas Day')
        # Noël
        print(f'{date(year, DEC, 26)} Boxing Day')
        # Lendemain de Noël
        # Le jour des boîtes
        # Après-Noël
        if date.weekday(date(year, DEC, 25)) == SAT:
            print(f'{closest_day(MON, date(year, DEC, 25))} Christmas Day (observed)')
            print(f'{closest_day(TUE, date(year, DEC, 26))} Boxing Day (observed)')
        if date.weekday(date(year, DEC, 25)) == SUN:
            print(f'{closest_day(TUE, date(year, DEC, 25))} Christmas Day (observed)')

        # New Year's Eve is December 31st
        #   https://en.wikipedia.org/wiki/New_Year's_Eve
        #   https://fr.wikipedia.org/wiki/R%C3%A9veillon_de_la_Saint-Sylvestre
        print(f'{date(year, DEC, 31)} New Year\'s Eve')
        # XXX FIXME TODO Get a better name in French
        # Veille du Nouvel An


if __name__ == '__main__':
    main()
