#!/usr/bin/env python3
#
# Copyright (c) 2018 Sascha Brawer <sascha@brawer.ch>
# SPDX-License-Identifier: MIT-0

import codecs
from xml.sax.saxutils import escape

def main():
    with codecs.open('rm-sursilv.xml', 'w', 'utf-8') as out:
        out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        out.write('<LexicalResource dtdVersion="16">\n')
        out.write('\t<GlobalInformation>\n')
        out.write('\t\t<feat att="label" val="Sursilvan lexicon"/>\n')
        out.write('\t\t<feat att="languageCoding" val="IETF BCP-47"/>\n')
        out.write('\t\t<feat att="license" val="Creative Commons Zero v1.0 Universal"/>\n')
        out.write('\t\t<feat att="spdxLicenseIdentifier" val="CC0-1.0"/>\n')
        out.write('\t</GlobalInformation>\n')
        out.write('\t<Lexicon>\n')
        out.write('\t\t<feat att="language" val="rm-sursilv"/>\n')
        generate_verb_forms(out)
        out.write('\t</Lexicon>\n')
        out.write('</LexicalResource>\n')


def generate_verb_forms(out):
    for line in codecs.open('data/verbs.txt', 'r', encoding='utf-8'):
        if line.strip() and line[0] != '#':
            verb, verb_ipa, pattern, gloss = \
                [column.strip() for column in line.split('\t')]
            out.write('\t\t<LexicalEntry>\n')
            out.write('\t\t\t<feat att="partOfSpeech" val="uf:Verb"/>\n')
            out.write('\t\t\t<Lemma>\n')
            out.write('\t\t\t\t<feat att="writtenForm" val="%s"/>\n' %
                      escape(verb))
            out.write('\t\t\t</Lemma>\n')
            forms = inflect_verb(verb, verb_ipa, pattern)
            for key in sorted(forms.keys(), key=get_form_sort_key):
                for form, form_ipa in forms[key]:
                    out.write('\t\t\t<WordForm>\n')
                    out.write('\t\t\t\t<feat att="writtenForm" val="%s"/>\n' %
                              escape(form))
                    out.write('\t\t\t\t<feat att="phoneticForm" val="%s"/>\n' %
                              escape(form_ipa))
                    for value in key.split('-'):
                        out.write('\t\t\t\t<feat att="uf:%s" val="uf:%s"/>\n' %
                                  (FEATURE_KEY[value], value))
                    out.write('\t\t\t</WordForm>\n')
            out.write('\t\t\t<Sense>\n')
            out.write('\t\t\t\t<feat att="gloss" val="%s"/>\n' %
                      escape(gloss))
            out.write('\t\t\t</Sense>\n')
            out.write('\t\t</LexicalEntry>\n')


def inflect_verb(verb, verb_ipa, pattern):
    assert pattern in {'partir', 'capir'}, pattern
    if verb.endswith('ar') or verb.endswith('ir'):
        stem = verb[:-2]
    else:
        assert False, verb
    stem_ipa = verb_ipa[:-2]
    stem_ipa_unstressed = stem_ipa.replace('ˈ', '')
    if pattern == 'partir':
        forms = inflect_verb(verb, verb_ipa, pattern='capir')
        forms.update({
            'Fin-Ind-Pres-Sing-1': [
                (stem + 'el', stem_ipa + 'ɛl')],   # jeu partel
            'Fin-Ind-Pres-Sing-2': [
                (stem + 'as', stem_ipa + 'as')],   # ti partas
            'Fin-Ind-Pres-Sing-3': [
                (stem + 'a', stem_ipa + 'a')],     # el/ella parta
            'Fin-Ind-Pres-Plur-3': [
                (stem + 'an', stem_ipa + 'an')],   # els/ellas partan
            'Fin-Sub-Pres-Sing-1': [
                (stem + 'i', stem_ipa + 'i')],     # jeu parti
            'Fin-Sub-Pres-Sing-2': [
                (stem + 'ies', stem_ipa + 'ɪə̯s')], # ti parties
            'Fin-Sub-Pres-Sing-3': [
                (stem + 'i', stem_ipa + 'i')],     # el/ella parti
            'Fin-Sub-Pres-Plur-3': [
                (stem + 'ien', stem_ipa + 'ɪə̯n')], # els/ellas partien
            'Fin-Imp-Sing': [
                (stem + 'a', stem_ipa + 'a')],     # parta!
        })
        return forms
    elif pattern == 'capir':
        assert verb.endswith('ir'), verb
        assert verb_ipa.endswith('iː'), verb_ipa
        return {
            'Inf': [(verb, verb_ipa)],                   # capir, kaˈpiː

            'Fin-Ind-Pres-Sing-1': [
                (stem + 'eschel', stem_ipa + 'ɛʃel')],   # jeu capeschel
            'Fin-Ind-Pres-Sing-2': [
                (stem + 'eschas', stem_ipa + 'ɛʃas')],   # ti capeschas
            'Fin-Ind-Pres-Sing-3': [
                (stem + 'escha', stem_ipa + 'ɛʃa')],     # el/ella capescha
            'Fin-Ind-Pres-Plur-1': [
                (stem + 'in', stem_ipa + 'iːn')],        # nus capin
            'Fin-Ind-Pres-Plur-2': [
                (stem + 'is', stem_ipa + 'iːs')],        # vus capis
            'Fin-Ind-Pres-Plur-3': [
                (stem + 'eschan', stem_ipa + 'ɛʃan')],   # els/ellas capeschan

            'Fin-Ind-Past-Sing-1': [
                (stem + 'evel', stem_ipa + 'eːvel')],    # jeu capevel
            'Fin-Ind-Past-Sing-2': [
                (stem + 'evas', stem_ipa + 'eːvas')],     # ti capevas
            'Fin-Ind-Past-Sing-3': [
                (stem + 'eva', stem_ipa + 'eːva')],      # el/ella capeva
            'Fin-Ind-Past-Plur-1': [
                (stem + 'evan', stem_ipa + 'eːvan')],    # nus capevan
            'Fin-Ind-Past-Plur-2': [
                (stem + 'evas', stem_ipa + 'eːvas')],    # vus capevas
            'Fin-Ind-Past-Plur-3': [
                (stem + 'evan', stem_ipa + 'eːvan')],    # els/ellas capevan

            'Fin-Sub-Pres-Sing-1': [
                (stem + 'eschi', stem_ipa + 'ɛʃi')],     # jeu capeschi
            'Fin-Sub-Pres-Sing-2': [
                (stem + 'eschies',                       # ti capeschies
                 stem_ipa_unstressed + 'ɛˈʒɪə̯s')],
            'Fin-Sub-Pres-Sing-3': [
                (stem + 'eschi', stem_ipa + 'ɛʃi')],     # el/ella capeschi
            'Fin-Sub-Pres-Plur-1': [
                (stem + 'îen', stem_ipa + 'iːən')],      # nus capîen
            'Fin-Sub-Pres-Plur-2': [
                (stem + 'îes', stem_ipa + 'iːəs')],      # vus capîes
            'Fin-Sub-Pres-Plur-3': [
                (stem + 'eschien',                       # els/ellas capeschien
                 stem_ipa_unstressed + 'ɛˈʒɪə̯n')],
            'Fin-Sub-Past-Sing-1': [
                (stem + 'evi', stem_ipa + 'eːvi')],      # jeu capevi
            'Fin-Sub-Past-Sing-2': [
                (stem + 'evies',                         # ti capevies
                 stem_ipa_unstressed + 'ɛˈvɪə̯s')],
            'Fin-Sub-Past-Sing-3': [
                (stem + 'evi', stem_ipa + 'eːvi')],      # el/ella capevi
            'Fin-Sub-Past-Plur-1': [
                (stem + 'evien',                         # nus capevien
                 stem_ipa_unstressed + 'ɛˈvɪə̯n')],
            'Fin-Sub-Past-Plur-2': [
                (stem + 'evies',                         # vus capevies
                 stem_ipa_unstressed + 'ɛˈvɪə̯s')],
            'Fin-Sub-Past-Plur-3': [
                (stem + 'evien',                         # els/ellas capevien
                 stem_ipa_unstressed + 'ɛˈvɪə̯n')],
 
            'Fin-Cnd-Pres-Sing-1': [
                (stem + 'ess', stem_ipa + 'ɛs')],       # jeu capess
            'Fin-Cnd-Pres-Sing-2': [
                (stem + 'esses', stem_ipa + 'ɛsəs')],   # ti capesses
            'Fin-Cnd-Pres-Sing-3': [
                (stem + 'ess', stem_ipa + 'ɛs')],       # el/ella capess
            'Fin-Cnd-Pres-Plur-1': [
                (stem + 'essen', stem_ipa + 'ɛsən')],   # nus capessen
            'Fin-Cnd-Pres-Plur-2': [
                (stem + 'esses', stem_ipa + 'ɛsəs')],   # vus capesses
            'Fin-Cnd-Pres-Plur-3': [
                (stem + 'essen', stem_ipa + 'ɛsən')],   # els/ellas capessen

            'Fin-Cnd-Past-Sing-1': [
                (stem + 'essi', stem_ipa + 'ɛsi')],     # jeu capessi
            'Fin-Cnd-Past-Sing-2': [
                (stem + 'essies',                       # ti capessies
                 stem_ipa_unstressed + 'ɛˈsɪə̯s')],
            'Fin-Cnd-Past-Sing-3': [
                (stem + 'essi', stem_ipa + 'ɛsi')],     # el/ella capessi
            'Fin-Cnd-Past-Plur-1': [
                (stem + 'essien',                       # nus capessien
                 stem_ipa_unstressed + 'ɛˈsɪə̯n')],
            'Fin-Cnd-Past-Plur-2': [
                (stem + 'essies',                       # vus capessies
                 stem_ipa_unstressed + 'ɛˈsɪə̯s')],
            'Fin-Cnd-Past-Plur-3': [
                (stem + 'essien',                       # els/ellas capessien
                 stem_ipa_unstressed + 'ɛˈsɪə̯n')],

            'Fin-Imp-Sing': [
                (stem + 'escha', stem_ipa + 'ɛʃa')],    # capescha!
            'Fin-Imp-Plur': [
                (stem + 'i', stem_ipa + 'i')],          # capi!

            'Part-Pres': [
                (stem + 'ent', stem_ipa + 'ɛnt')],      # capent

            'Part-Past-Sing-Masc': [
                (stem + 'ius', stem_ipa + 'iːʊs')],     # capius
            'Part-Past-Sing-Fem': [
                (stem + 'ida', stem_ipa + 'iːda')],     # capida
            'Part-Past-Plur-Masc': [
                (stem + 'i', stem_ipa + 'iː')],         # capi
            'Part-Past-Plur-Fem': [
                (stem + 'idas', stem_ipa + 'iːdas')],   # capidas

            'Ger': [
                (stem + 'end', stem_ipa + 'ent')],      # capend
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
