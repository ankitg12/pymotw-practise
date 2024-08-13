import string
values = {'var': 'foo'}

t=string.Template("""
Variable: $var
Escape: $$
Variabe in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s="""
Variable: %(var)s
Escape: %%
Variabe in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s= """
Variable: {var}
Escape: {{}}
Variabe in text: {var}iable
"""
print('FORMAT:', s.format(**values))