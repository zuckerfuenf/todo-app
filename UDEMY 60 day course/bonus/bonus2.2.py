def temp(temperature):
    if temperature > 25:
        state = "Hot"
    elif 15 <= temperature >= 25:
        state = "Warm"
    else:
        "Cold"