count = 0
for n in range(len(s)):
    try:
        if s[n] == 'b':
            if s[n+1] == 'o':
                if s[n+2] == 'b':
                    count += 1
    except: IndexError
print(count)