height = 0
daily_climb = 7
nightly_slip = 2
days = 0

while height<=100:
    height+=daily_climb
    days+=1
    if height>=100:
        break
    else:
        height-=nightly_slip
print(days)