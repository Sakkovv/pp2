def gramy_ounce(grams):
    ounce = 28.3495231 * grams
    return ounce

grams_a = float(input())
ounce_a = gramy_ounce(grams_a)
print(f"{grams_a} грамы в унциях {ounce_a}")