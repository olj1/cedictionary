import eng_to_ipa as ipa
import pronouncing
import itertools
from cedict_utils_mod.cedict_utils.cedict import CedictParser, CedictEntry
from dragonmapper import transcriptions
import re

# english_string = "who" 
test_strings = [
    "rural, fix accumulate, fix yard",
    "birthday",
    "bomb",
    "bomber",
    "ghost",
    "punk",
    "punker",
    "earth",
    "earthy",
]


ipa_to_pin_vwls_consts = {
    "ɑ":"a", 
    "bu":"bu",
    "wei":"wei",
    "dei":"dei",
    "mei":"mei",
    "bei":"bei",
    "kei":"kei",
    "lei":"lei",
    "pei":"pei",
    "zei":"zei",
    "nei":"nei",
    "tei":"tei",
    "tai":"tai",
    "wai":"wai",
    "pai":"pai",
    "sai":"sai",
    "dai":"dai",
    "gai":"gai",
    "hai":"hai",
    "kai":"kai",
    "lai":"lai",
    "mai":"mai",
    "nai":"nai",
    "bai":"bai",
    "cai":"cai",
    "zai":"zai",
    "en":"en",
    "ou":"ou",
    "er":"er",
    "a":"a",
    "eng":"eng",
    "æ":"ei",
    "ʊ":"wu",
    "ɛ":"ye",
    "e":"ei", 
    "ə":"e",
    "ɚ":"er",
    "i":"yi",
    "ɪ":"yi",
    "ɔ":"wo",
    "aʊ":"au",
    "u":"wu",
    "ai":"ai",
    "aɪ":"ai",
    "oʊ":"ou",
    "f":"fe",
    "g":"ge",
    "j":"ji",
    "k":"ge",
    "l":"le",
    "m":"mo",
    "n":"ne",
    "oŋ":"ang",
    "p":"po",
    "b":"bo",
    "r":"ri",
    "s":"si",
    "ʃ":"shi",
    "d":"de",
    "t":"te",
    "z":"zi",
    "c":"ci",
    "ʤ":"ji",
    "ʧ":"qi",
    "ɕ":"xi",
    "ʈʂ":"zhi",
    "w":"wu",
    "y":"yi",
}

ipa_to_pin_vwls_consts_keys = list(ipa_to_pin_vwls_consts.keys())
ipa_to_pin_vwls_consts_vals = list(ipa_to_pin_vwls_consts.values())

# @ETI


                    # 1
def convert_english_to_ipa(english_string):
    if ' ' in english_string:
        eng_to_ipa_string = ipa.convert(english_string)
        english_to_ipa_split = eng_to_ipa_string.split()
        return english_to_ipa_split.split(' ')
    else:
        english_string = ipa.convert(english_string)
        return english_string

# print(f"ENGLISH TO IPA: {convert_english_to_ipa(english_string)}")

# # @RNCI


def flatten_lists(l):
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list
    
                    # 2
def replace_non_compatible_ipa(eng_to_ipa_split_string):
    is_list = type(eng_to_ipa_split_string) == list
    stringify = ""
    if not is_list:
        compatible_words = [
            word.replace(word, 'x') if word == "h" else word for word in eng_to_ipa_split_string
        ]
        return stringify.join(compatible_words)
        compatible_words = [
            word.replace(word[0], 'x') if word[0] == "h" else word for word in eng_to_ipa_split_string
        ]
        return stringify.join(compatible_words)


ipa_to_ipa_w_x = replace_non_compatible_ipa(convert_english_to_ipa(english_string))
# print(f"IPA REPLACE H: {ipa_to_ipa_w_x}")


def split_any_word(word):
    return [char for char in word]

# def split_list_of_ipa(list_of_ipa):
#     split_ipa_list = [split_any_word(word) for word in ipa_to_ipa_w_x]
#     return split_ipa_list


def replace_pinyin_list_word(list_word):
    new_list = []
    for char in list_word:
        if char in list_word and char in ipa_to_pin_vwls_consts_keys:
            new_list.append(ipa_to_pin_vwls_consts[char])
    return new_list

# def replace_all_word_sets(list):
#     pre_query_list = []
#     for list_word in list:
#         pre_query_list.append(replace_pinyin_list_word(list_word))
#     return pre_query_list

# last_list = replace_all_word_sets(split_list_of_ipa(ipa_to_ipa_w_x))

def even_or_odd(int):
    if int % 2:
        return "even"
    else:
        return "odd"
    
def convert_ipa_string_to_pinyin(ipa_string):
    eng_vowels = [
        "a",
        "e",
        "i",
        "o",
        "u",
    ]
    eng_consonants = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    eng_digraphs = [
        "ch",
        "sh",
        "zh",
        "th",
    ]
    excluded_pinyin_digraphs = [
        "bo",
        "po",
    ]
    excluded_pinyin_consonants = [
        "r",
        "s",
        "q",
        "y",
        "j",
        "x",
        "c",
        "v",
    ]
    other_excluded_pinyin_consonants = [
        "y",
        "q",
        "r",
        "v",
        "j",
        "f",

    ]
    try:
        first_pinyin = transcriptions.ipa_to_pinyin(ipa_string)
        if transcriptions.is_pinyin(first_pinyin):
            return first_pinyin
        else:
            print("HI")
            excepted_ipa_string_to_list = split_any_word(ipa_string)
            pinyinized_syllables_list = replace_pinyin_list_word(excepted_ipa_string_to_list)
            print(pinyinized_syllables_list)
            for word in pinyinized_syllables_list:
                if word[:-1] in eng_digraphs and word[-1] in eng_vowels:
                    first_first = word[:-1]
                    first_last = word[len(word[0])]
                    last_first = word[1]
                    last_last = word[len(word[1])]
                    if first_first not in eng_vowels and first_last in eng_vowels and last_first in eng_vowels:
                        return first_first + pinyinized_syllables_list[1]
            return pinyinized_syllables_list   
    except:
        # print("BYE")
        excepted_ipa_string_to_list = split_any_word(ipa_string)
        print(excepted_ipa_string_to_list)
        for index, ipa in enumerate(excepted_ipa_string_to_list):
            print(f"IPA = {ipa}, INDEX = {index}")
            if ipa == "o" and index != len(excepted_ipa_string_to_list) - 1 and excepted_ipa_string_to_list[index+1] == 'ʊ':
                excepted_ipa_string_to_list.remove("o")
                excepted_ipa_string_to_list.remove("ʊ")
                excepted_ipa_string_to_list.insert(index, "ou")
            elif ipa == 'ɛ' and index != len(excepted_ipa_string_to_list) - 1 and excepted_ipa_string_to_list[index+1] == 'n':
                excepted_ipa_string_to_list.remove("ɛ")
                excepted_ipa_string_to_list.remove("n")
                excepted_ipa_string_to_list.insert(index, "en")
            elif ipa == 'ə' and index != len(excepted_ipa_string_to_list) - 1 and excepted_ipa_string_to_list[index+1] == 'ŋ':
                excepted_ipa_string_to_list.remove ('ə')
                excepted_ipa_string_to_list.remove('ŋ')
                excepted_ipa_string_to_list.insert(index, "eng")
            elif ipa in eng_consonants and ipa not in excluded_pinyin_consonants and index != len(excepted_ipa_string_to_list) - 1 and excepted_ipa_string_to_list[index+1] == 'ɛ':
                excepted_ipa_string_to_list.remove(ipa)
                excepted_ipa_string_to_list.remove('ɛ')
                excepted_ipa_string_to_list.insert(index, ipa + "ei")
            elif ipa == "e" and index != len(excepted_ipa_string_to_list) - 1 and excepted_ipa_string_to_list[index+1] == 'r':
                excepted_ipa_string_to_list.remove(ipa)
                excepted_ipa_string_to_list.remove('r')
                excepted_ipa_string_to_list.insert(index, "er")
            elif ipa in eng_consonants and ipa not in other_excluded_pinyin_consonants and index != len(excepted_ipa_string_to_list) - 1 and excepted_ipa_string_to_list[index+1] == 'i':
                excepted_ipa_string_to_list.remove(ipa)
                excepted_ipa_string_to_list.remove('i')
                excepted_ipa_string_to_list.insert(index, ipa + "ai")
            elif ipa in eng_consonants and ipa not in other_excluded_pinyin_consonants and index != len(excepted_ipa_string_to_list) - 1 and (len(excepted_ipa_string_to_list) - 1) - index >= 2 and excepted_ipa_string_to_list[index+1] == 'a' and excepted_ipa_string_to_list[index+2] == 'ɪ':
                excepted_ipa_string_to_list.remove(ipa)
                excepted_ipa_string_to_list.remove('a')
                excepted_ipa_string_to_list.remove('ɪ')
                excepted_ipa_string_to_list.insert(index, ipa[0] + "ai")
        # print(excepted_ipa_string_to_list)
        pinyinized_syllables_list = replace_pinyin_list_word(excepted_ipa_string_to_list)
        # print(f"P2: {pinyinized_syllables_list}")
        odds_to_sub = []
        for index, word in enumerate(pinyinized_syllables_list): 
            first_word_first_char = word[0]
            first_word_last_char = word[-1]
            first_word_first_two = word[0:2]
            last_index = len(pinyinized_syllables_list)-1
            if even_or_odd(index) == "odd":
                print(f"ODD: {word}")   
            if even_or_odd(index) == "even":
                print(f"EVEN: {word}")
            if even_or_odd(index) == "odd" and first_word_first_char in eng_consonants and first_word_last_char in eng_vowels and index != last_index and pinyinized_syllables_list[index+1] == "e" and pinyinized_syllables_list[index+2] == "ri":
                odds_to_sub.append(word)
            elif first_word_first_char in eng_consonants and first_word_first_char != "j" and first_word_last_char in eng_vowels and index != last_index and pinyinized_syllables_list[index+1][0] in eng_vowels and first_word_first_two not in eng_digraphs:
                odds_to_sub.append(word[0] + pinyinized_syllables_list[index+1])
            elif first_word_first_char in eng_consonants and index != last_index and pinyinized_syllables_list[index+1][0] in eng_consonants and pinyinized_syllables_list[index-1] != "e":
                odds_to_sub.append(word)
            elif first_word_first_char in eng_consonants and index != last_index and pinyinized_syllables_list[index+1][0] in eng_consonants and pinyinized_syllables_list[index-1] != "e" and word != "ri":
                print("ri")
                odds_to_sub.append(word)
            elif first_word_first_char in eng_consonants and index == last_index and pinyinized_syllables_list[index-1] != "e":
                odds_to_sub.append(word)
            elif first_word_first_char in eng_consonants and index == last_index and pinyinized_syllables_list[index-1] == "e" and word != "ri":
                odds_to_sub.append(word)
            elif word == "e" and index != last_index and pinyinized_syllables_list[index+1] == "ri":
                odds_to_sub.append("er")
            elif word[0] in eng_consonants and word[-1] in eng_vowels and index != last_index and pinyinized_syllables_list[index+1][0] in eng_vowels  and first_word_first_two not in eng_digraphs:
                odds_to_sub.append(word[0] + pinyinized_syllables_list[index+1])
            elif word[0] in eng_consonants and word[-1] in eng_vowels and index != last_index and pinyinized_syllables_list[index+1][0] in eng_vowels  and first_word_first_two  in eng_digraphs:
                odds_to_sub.append(first_word_first_two + pinyinized_syllables_list[index+1])
            elif word[0] in eng_vowels and word[-1] in eng_vowels and index != last_index and pinyinized_syllables_list[index-1][0] not in eng_consonants and pinyinized_syllables_list[index-1][-1] not in eng_vowels:
                odds_to_sub.append(word)
            elif word[0] in eng_vowels and word[-1] in eng_vowels and index != last_index and pinyinized_syllables_list[index+1][0] in eng_consonants and index == 0:
                odds_to_sub.append(word)

        return odds_to_sub



convert_ipa_string_to_pinyin(replace_non_compatible_ipa(convert_english_to_ipa(english_string)))

