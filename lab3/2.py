def  v_Celcius(Farengeit):
    celcuis = (5 / 9) * (farengeit -32)
    return celcuis
farengeit = float(input())
celcuis_gradus = v_Celcius(farengeit)
print(f"Из фаренгейт {farengeit} в цельсий {celcuis_gradus}")