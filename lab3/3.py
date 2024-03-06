def Chiken_Rabbit(numheads, numlegs):
    colvo_rab = (heads*2 - legs)/-2
    colvo_chic = heads - colvo_rab
    return colvo_chic, colvo_rab

heads = int(input())
legs = int(input())
colvo_chic, colvo_rab = Chiken_Rabbit(heads, legs)
print(f'курицы {colvo_chic} кролики{colvo_rab}')

"""
головы куриц = x
ноги = 2
всего ног 2x

головы кроликов 
35 - x 
ног 4
всего ног 4*(35-x)

"""
