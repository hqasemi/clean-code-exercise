def pearson_correlation_coefficient(fp):
    t = []
    with open(fp, 'r') as f:
        for l in f:
            x = float(l.strip().split(',')[0])
            y = float(l.strip().split(',')[1])
            t.append((x, y))

    a_sum, b_sum = 0, 0
    for x, y in t:
        a_sum += x
        b_sum += y

    a_mean = a_sum / len(t)
    b_mean = b_sum / len(t)

    c_num = 0
    d_den_x = 0
    e_den_y = 0

    for x, y in t:
        c_num += (x - a_mean) * (y - b_mean)
        d_den_x += (x - a_mean) ** 2
        e_den_y += (y - b_mean) ** 2

    d = ((d_den_x * e_den_y) ** 0.5)
	
    if d == 0:
      return 0
    else: 
      return c_num / ((d_den_x * e_den_y) ** 0.5)
