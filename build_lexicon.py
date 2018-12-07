#!/usr/bin/env python3
#
# Copyright (c) 2018 Sascha Brawer <sascha@brawer.ch>
# SPDX-License-Identifier: MIT-0

import codecs


def main():
    print('# Licensed under the Creative Commons Zero v1.0 Universal Public Domain Dedication')
    print('# SPDX-License-Identifier: CC0-1.0')
    print()
    generate_verb_forms()


def generate_verb_forms():
    for line in codecs.open('data/verbs.txt', 'r', encoding='utf-8'):
        if line.strip() and line[0] != '#':
            verb, klass = [column.strip() for column in line.split()]
            print('---')
            print('- Lexeme:')
            print('    Lemma: ' + verb)
            print('    POS: VERB')
            print('    Forms:')
            forms = inflect_verb(verb, klass)
            for key in sorted(forms.keys(), key=get_form_sort_key):
                for form in forms[key]:
                    print('        - Form: ' + form)
                    for value in key.split('-'):
                        print('          %s: %s' % (FEATURE_KEY[value], value))
                    print()


def inflect_verb(verb, klass):
    assert klass in {'1', '1e', '4', '4e'}, klass
    if verb.endswith('ar') or verb.endswith('ir'):
        stem = verb[:-2]
    else:
        assert False, verb
    if klass == '1':
        return {
            'Fin-Ind-Pres-Sing-1': [stem + 'el'],    # jeu admirel
            'Fin-Ind-Pres-Sing-2': [stem + 'as'],    # ti admiras
            'Fin-Ind-Pres-Sing-3': [stem + 'a'],     # el/ella admira
            'Fin-Ind-Pres-Plur-1': [stem + 'ein'],   # nus admirein
            'Fin-Ind-Pres-Plur-2': [stem + 'eis'],   # vus admireis
            'Fin-Ind-Pres-Plur-3': [stem + 'an'],    # els/ellas admiran

            'Fin-Ind-Past-Sing-1': [stem + 'avel'],  # jeu admiravel
            'Fin-Ind-Past-Sing-2': [stem + 'avas'],  # ti admiravas
            'Fin-Ind-Past-Sing-3': [stem + 'ava'],   # el/ella admirava
            'Fin-Ind-Past-Plur-1': [stem + 'avan'],  # nus admiravan
            'Fin-Ind-Past-Plur-2': [stem + 'avas'],  # vus admiravas
            'Fin-Ind-Past-Plur-3': [stem + 'avan'],  # els/ellas admiravan

            'Fin-Sub-Pres-Sing-1': [stem + 'i'],     # jeu admiri
            'Fin-Sub-Pres-Sing-2': [stem + 'ies'],   # ti admiries
            'Fin-Sub-Pres-Sing-3': [stem + 'i'],     # el/ella admiri
            'Fin-Sub-Pres-Plur-1': [stem + 'eien'],  # nus admireien
            'Fin-Sub-Pres-Plur-2': [stem + 'eies'],  # vus admireies
            'Fin-Sub-Pres-Plur-3': [stem + 'ien'],   # els/ellas admirien

            'Fin-Sub-Past-Sing-1': [stem + 'avi'],    # jeu admiravi
            'Fin-Sub-Past-Sing-2': [stem + 'avies'],  # ti admiravies
            'Fin-Sub-Past-Sing-3': [stem + 'avi'],    # el/ella admiravi
            'Fin-Sub-Past-Plur-1': [stem + 'avien'],  # nus admiravien
            'Fin-Sub-Past-Plur-2': [stem + 'avies'],  # vus admiravies
            'Fin-Sub-Past-Plur-3': [stem + 'avien'],  # els/ellas admiravien
        }
    elif klass == '4e':
        assert verb.endswith('ir'), verb
        return {
            'Inf': [verb],                             # capir

            'Fin-Ind-Pres-Sing-1': [stem + 'eschel'],  # jeu capeschel
            'Fin-Ind-Pres-Sing-2': [stem + 'eschas'],  # ti capeschas
            'Fin-Ind-Pres-Sing-3': [stem + 'escha'],   # el/ella capescha
            'Fin-Ind-Pres-Plur-1': [stem + 'in'],      # nus capin
            'Fin-Ind-Pres-Plur-2': [stem + 'is'],      # vus capis
            'Fin-Ind-Pres-Plur-3': [stem + 'eschan'],  # els/ellas capeschan

            'Fin-Ind-Past-Sing-1': [stem + 'evel'],    # jeu capevel
            'Fin-Ind-Past-Sing-2': [stem + 'evas'],    # ti capevas
            'Fin-Ind-Past-Sing-3': [stem + 'eva'],     # el/ella capeva
            'Fin-Ind-Past-Plur-1': [stem + 'evan'],    # nus capevan
            'Fin-Ind-Past-Plur-2': [stem + 'evas'],    # vus capevas
            'Fin-Ind-Past-Plur-3': [stem + 'evan'],    # els/ellas capevan

            'Fin-Sub-Pres-Sing-1': [stem + 'eschi'],    # jeu capeschi
            'Fin-Sub-Pres-Sing-2': [stem + 'eschies'],  # ti capeschies
            'Fin-Sub-Pres-Sing-3': [stem + 'eschi'],    # el/ella capeschi
            'Fin-Sub-Pres-Plur-1': [stem + 'îen'],      # nus capîen
            'Fin-Sub-Pres-Plur-2': [stem + 'îes'],      # vus capîes
            'Fin-Sub-Pres-Plur-3': [stem + 'eschien'],  # els/ellas capeschien

            'Fin-Sub-Past-Sing-1': [stem + 'evi'],      # jeu capevi
            'Fin-Sub-Past-Sing-2': [stem + 'evies'],    # ti capevies
            'Fin-Sub-Past-Sing-3': [stem + 'evi'],      # el/ella capevi
            'Fin-Sub-Past-Plur-1': [stem + 'evien'],    # nus capevien
            'Fin-Sub-Past-Plur-2': [stem + 'evies'],    # vus capevies
            'Fin-Sub-Past-Plur-3': [stem + 'evien'],    # els/ellas capevien
 
            'Fin-Cnd-Pres-Sing-1': [stem + 'ess'],      # jeu capess
            'Fin-Cnd-Pres-Sing-2': [stem + 'esses'],    # ti capesses
            'Fin-Cnd-Pres-Sing-3': [stem + 'ess'],      # el/ella capess
            'Fin-Cnd-Pres-Plur-1': [stem + 'essen'],    # nus capessen
            'Fin-Cnd-Pres-Plur-2': [stem + 'esses'],    # vus capesses
            'Fin-Cnd-Pres-Plur-3': [stem + 'essen'],    # els/ellas capessen

            'Fin-Cnd-Past-Sing-1': [stem + 'essi'],     # jeu capessi
            'Fin-Cnd-Past-Sing-2': [stem + 'essies'],   # ti capessies
            'Fin-Cnd-Past-Sing-3': [stem + 'essi'],     # el/ella capessi
            'Fin-Cnd-Past-Plur-1': [stem + 'essien'],   # nus capessien
            'Fin-Cnd-Past-Plur-2': [stem + 'essies'],   # vus capessies
            'Fin-Cnd-Past-Plur-3': [stem + 'essien'],   # els/ellas capessien

            'Fin-Imp-Sing': [stem + 'escha'],           # capescha!
            'Fin-Imp-Plur': [stem + 'i'],               # capi!

            'Part-Pres': [stem + 'ent'],                # capent

            'Part-Past-Sing-Masc': [stem + 'ius'],      # capius
            'Part-Past-Sing-Fem': [stem + 'ida'],       # capida
            'Part-Past-Plur-Masc': [stem + 'i'],        # capi
            'Part-Past-Plur-Fem': [stem + 'idas'],      # capidas

            'Ger': [stem + 'end'],                      # capend
        }


# Used for ordering features. Purely cosmetic, so the output is easier to read.
SORT_ORDER = {
    'Inf': '0',
    'Fin': '1',
    'Part': '2',
    'Ger': '3',
    'Ind': '0',
    'Sub': '1',
    'Cnd': '2',
    'Imp': '3',
    'Pres': '0',
    'Past': '1',
    'Sing': '0',
    'Plur': '1',
    'Masc': '0',
    'Fem': '1',
    '1': '1',
    '2': '2',
    '3': '3',
}

# http://universaldependencies.org/u/feat/
FEATURE_KEY = {
    'Inf': 'VerbForm',
    'Fin': 'VerbForm',
    'Part': 'VerbForm',
    'Ger': 'VerbForm',
    'Ind': 'Mood',
    'Sub': 'Mood',
    'Cnd': 'Mood',
    'Imp': 'Mood',
    'Pres': 'Tense',
    'Past': 'Tense',
    'Sing': 'Number',
    'Plur': 'Number',
    'Masc': 'Gender',
    'Fem': 'Gender',
    '1': 'Person',
    '2': 'Person',
    '3': 'Person',
}


def get_form_sort_key(form):
    return '-'.join([SORT_ORDER[key] for key in form.split('-')])


if __name__ == '__main__':
    main()
