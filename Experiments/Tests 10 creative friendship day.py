print('\n'.join([''.join([('Freindship'[(x - y) % 8] if ((x * 0.075) ** 2 + (y * 0.2) ** 2 - 1) ** 3 - (x * 0.075) ** 2 * (y * 0.2) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))