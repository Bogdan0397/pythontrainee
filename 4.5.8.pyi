class Morph:
    def __init__(self, *args):
        self.morph_l = args

    def add_word(self, word):
        self.morph_l.append(word)

    def get_words(self):
        return tuple( self.morph_l)

    def __eq__(self, other):
        return other in self.morph_l



dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]

text = input()
counter = 0
for i in text:
    for j in dict_words:
        if i == j:
            counter+=1

print(counter)

