user_input = "ala"

try:
    x = [2, 3][int(user_input) // 1]
except ValueError:  # jeśli user input nie da się zmienić na int
    raise IndexError('error')
except ZeroDivisionError:  # ponieważ wpisaliśmy dzielenie przez zero
    x = 'lol'
except TypeError:
    x = "float"
except IndexError:
    x = "idx"

print(x)