import string
values = {'var':'foo'}
t=string.Template("$var is here but $missing is not provided")
try:
    print(f"substitue: {t.substitute(values)}")
except KeyError as err:
    print(f"ERROR: {err}")

print(f'safe_substitute(): {t.safe_substitute(values)}')