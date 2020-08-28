#
# Title:goat_latin.py
# Description: similar to pig latin
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Author:G.S. Cole (guycole at gmail dot com)
#
class GoatLatin:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    def translate_word(self, candidate):
        if candidate[:1].lower() in self.vowels:
            # begins w/a vowel, then add 'ma'
            return f"{candidate}ma"
        else:
            # begins w/a consonant, remove first letter and append, then add 'ma'
            temp = candidate[:1]
            buffer = candidate[1:]
            return f"{buffer}{temp}ma"

    def translate_sentence(self, candidate):
        buffer = ''

        tokens = candidate.split(' ')
        for count, item in enumerate(tokens):
            temp = self.translate_word(item)
            trailer = (1+count) * 'a'
            buffer += f"{temp}{trailer} "

        return buffer

print('start')

if __name__ == '__main__':
    goat_latin = GoatLatin()
    result = goat_latin.translate_sentence('I speak Goat Latin')
    print(result)

# 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'

print('stop')

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
