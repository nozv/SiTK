def output(n, par1, par2, par3, par4):
    print('┌' + '─' * 31 + '┬' + ('─' * 7 + '┬') * (n - 1) + '─' * 7 + '┐')
    print('│{: <30}'.format('Кратность ошибки'), '│', *['{: >6}│'.format(i + 1) for i in range(0, n)])
    print('│{: <30}'.format('Корректирующая способность, %'), '│', *['{: >6}│'.format(i) for i in par1])
    print('│{: <30}'.format('Исправлено ошибок'), '│', *['{: >6}│'.format(i) for i in par2])
    print('│{: <30}'.format('Обнаружено ошибок'), '│', *['{: >6}│'.format(i) for i in par3])
    print('│{: <30}'.format('Всего ошибок'), '│', *['{: >6.0f}│'.format(i) for i in par4])
    print('└' + '─' * 31 + '┴' + ('─' * 7 + '┴') * (n - 1) + '─' * 7 + '┘')