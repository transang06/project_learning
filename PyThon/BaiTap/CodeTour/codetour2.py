lines = []
i = 0
while i < 3:
    s = input()
    if s:
        lines.append(s)
    else:
        break
    i += 1
value = []
for i in lines:
    value.append(i.split())

if 1 <= int(value[0][0]) <= 10 ** 5 and 1 <= int(value[0][1]) <= int(value[0][0]):

    nam = []
    a = 1
    for i in value[1]:
        nam.append({'id': a, 'diem': i})
        a += 1

    nu = []
    a = 1
    for i in value[2]:
        nu.append({'id': a, 'diem': i})
        a += 1

    diem_nam_moi = []
    for i in value[1]:
        diem_nam_moi.append(float(i))
    diem_nam_moi.sort()
    nam_moi = []
    a = 1
    for i in diem_nam_moi:
        nam_moi.append({'id': a, 'diem': i})
        a += 1

    diem_nu_moi = []
    for i in value[2]:
        diem_nu_moi.append(float(i))
    diem_nu_moi.sort(reverse=True)
    nu_moi = []
    a = 1
    for i in diem_nu_moi:
        nu_moi.append({'id': a, 'diem': i})
        a += 1
    idNam = 0
    for x in nam_moi:
        if x['diem'] == float(nam[int(value[0][1]) - 1]['diem']):
            idNam = x['id']
    diemNu = nu_moi[idNam - 1]['diem']

    idNu = 0
    for x in nu:
        if float(x['diem']) == diemNu:
            idNu = x['id']
    print(idNu, diemNu)
else:
    print('nhap lai')
