"""
locale for internationalization (translation)
https://docs.python.org/3/library/locale.html
https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
"""

import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

print(locale.getlocale())
print(calendar.calendar(2022))
