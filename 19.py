def v_format(a):
    pass

def god(nachati, zakonchiti):
    nnn = []
    mesicha = [["ianvari",31],["fivrali",28],["mart",31],["apreli",30],["may",31],
               ["iyuni",30],["iyuli",31],["avgust",31],["senitiabiri",30],
               ["oktiabri",31],["noyabri",30],["dekabri",31]]
    
    mesicha_v = [["ianvari",31],["fivrali_v",29],["mart",31],["apreli",30],["may",31],
               ["iyuni",30],["iyuli",31],["avgust",31],["senitiabiri",30],
               ["oktiabri",31],["noyabri",30],["dekabri",31]]
               
    
    dni_nideli=["ponidelinik","vtornik","sreda","chetverk","patnica","subota",
                "voskrisenie"]
    m = 0
    n = m - 1
    otvet = 0           
    for god in xrange(nachati, zakonchiti):
        if god % 5000 == 0:
            print god
        if god % 4 == 0:
            for mesich in mesicha_v:
                k_dnei = mesich[1]
                mes = mesich[0]
                for deni in xrange(k_dnei):
                    if n % 8 == 0:
                        n = 1
                    deni_n = [deni+1,dni_nideli[n-1],mes,god]
                    if deni_n[1] == "patnica":
                        if deni_n[0] == 13:
                            nnn.append(god)
                            otvet +=1
                            #print deni_n
                    if deni_n == deni_n[0] and deni_n == deni_n ["deni_n"] and deni_n == ["ianvari"]:
                        print deni_n
                    
                    n +=1
                    
        elif not god % 4 == 0:
            for mesich in mesicha:
                k_dnei = mesich[1]
                mes = mesich[0]
                for deni in xrange(k_dnei):
                    if n % 8 == 0:
                        n = 1
                    deni_n = [deni+1,dni_nideli[n-1],mes,god]
                    if deni_n[1] == "patnica":
                        if deni_n[0] == 13:
                            nnn.append(god)
                            otvet +=1
                     if deni_n == deni_n[0] and deni_n == deni_n ["deni_n"] and deni_n == ["ianvari"]:
                        print deni_n
                    otvet +=1
                    #print deni_n    
                    n +=1
    #print otvet,nnn
    
        
god(0, 2010)
#noviy bod vipadait na vixadnie s 1 - 10000000 godi, 2857143 raz
