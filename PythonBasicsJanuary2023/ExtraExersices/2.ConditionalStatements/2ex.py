days_off = int(input())

WORK_DAYS_PLAYTIME = 63
OFF_DAYS_PLAYTIME = 127
TOM_PLAYTIME = 30000

work_days_total_playtime = (365 - days_off) * WORK_DAYS_PLAYTIME
off_days_playtime = days_off * OFF_DAYS_PLAYTIME
total_playtime = work_days_total_playtime + off_days_playtime

if TOM_PLAYTIME < total_playtime:
    print('Tom will run away')
    diff = total_playtime - TOM_PLAYTIME
    print(f'{diff//60} hours and {diff % 60} minutes more for play')
else:
    print('Tom sleeps well')
    diff = TOM_PLAYTIME - total_playtime
    print(f'{diff//60} hours and {diff % 60} minutes less for play')
