def validate_pin(pin):
    valid = "0123456789"
    list1 = list(valid)
    pin = list(pin)
    valid = True
    if (len(pin) != 4) and (len(pin) != 6):
        valid = False
    else:
        for i in pin:
            if i not in list1:
                valid = False
    return valid