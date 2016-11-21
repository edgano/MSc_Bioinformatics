def rabinacci(old, young, reproduction_rate, months):
    result = None
    if months == 1:
        result = young
    else:
        result = rabinacci(young, old * reproduction_rate + young, reproduction_rate, months - 1)

    return result

months = 31
reproduction_rate =4

print rabinacci(0, 1, reproduction_rate, months)