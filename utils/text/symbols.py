# -*- coding: utf-8 -*-
'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from utils.text.ro_symbols import _pad, _eos, _bos, _characters, _punctuations, _phoneme_punctuations, _phonemes, _arpabet, phonemes, symbols

if __name__ == '__main__':
    print(" > TTS symbols ")
    print(symbols)
    print(" > TTS phonemes ")
    print(phonemes)
