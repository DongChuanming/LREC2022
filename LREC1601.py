#!/usr/bin/env python
# coding: utf-8

# In[84]:


with open("/media/cdong/Elements/these/publication/LREC/data/list_basias_id.txt", "r", encoding="utf-8") as w:
    with open("/media/cdong/Elements/these/publication/LREC/data/list_basol_id.txt", "r", encoding="utf-8") as r:
        lr=r.readlines()
        c=0
        sb=set()
        for l in lr:
            if len(l.strip()) >3:
                sb.add(l.strip())
                c+=1


# In[85]:


c


# In[1]:


len(sb)


# In[2]:


len(sb)


# In[1]:


couples=list()

with open("inst.tsv", "r", encoding="utf-8") as r:
    with open("inst.txt", "w", encoding="utf-8") as w:
        ll=r.readlines()
        for l in ll:
            cp=("","")
            units=l.split("\t")
            if len(units)==4:
                io=units[1].strip()
                ib=units[2].strip()
                ia=units[3].strip()
                try:
                    exec("so="+io)
                    if type(so)==set:
                    #print(type(sb))
                        for e in so:
                            w.write(e+"\n")
                            
                    exec("sb="+ib)
                    if type(sb)==set:
                    #print(type(sb))
                        for e in sb:
                            w.write(e+"\n")
                #except:
                #    pass
                #try:
                    exec("sa="+ia)
                    #print(type(sa))
                    if type(sa)==set:
                        for e in sa:
                            w.write(e+"\n")
                    couples.append((so,sb,sa))
                except:
                    pass
                #print(type(sb))


# In[ ]:





# In[2]:


couples


# In[378]:


def tokens(w,l1,l2):
    for i in range(len(l1)):
        w=w.replace(l1[i],l2[i])
    lw=w.split(" ")
    while "" in lw:
        lw.remove("")
    return lw


# In[620]:


l1=["'","(",")",",","-",'"',"&"]
l2=["' "," ( "," ) "," ,"," - ",' " '," & "]


#lseg=["&","'",]
dstop={"&":[" "," et "],"-":[" "],"'":[' '],".":[""," "]}
dseg={"(",")","/",":",";",",",'"'}


# In[ ]:





# In[621]:


with open("tokens_nom_modified.txt","r", encoding="utf-8") as t:
    lt=t.readlines()
    noise=[]
    for w in lt:
        noise.append(w.strip())
print(noise)


# In[622]:


noise=['de', 'et', 'ets', 'ex', 'ex.','sté', 'sa', 'anc','anc.', 'des',
       "d'",'a', 'm','cie', 'sarl', 's.a.r.l.', "s.a.", 'la', 'du', "l'",'dli',
       'fils', 'earl', 'e.a.r.l.', 'le', 'ste', 'sas', 's.a.s.', 'les',
      'mr', 'mme', 'à','en','sur', 'sci','mm','bp','pour', 'groupe', 'aux',
      "au",'sca',"s.c.a.", 'group','(',')',",","'","-"]


# In[623]:


#liste des tokens marquant une société, 
societe_type=["sté","sté.","ste","ets","éts","cie", "sa", "s.a.","s.a","sarl",
             "s.a.r.l.","s.a.r.l","dli","earl","société","societe", "sas", 'mme', 'union',
             "s.a.s.","s.a.s", "gaec", "g.a.e.c.", "g.a.e.c","compagnie", "etablissement",
             "établissement","etablissements","établissements","scea",'atelier','ateliers',
             "s.c.e.a.","s.c.e.a","sci", "s.c.i.","s.c.i","bp","groupe","groupes","site",
              "entreprises","entreprise","sca","s.c.a.","s.c.a","association","group",
              "groups",'cooperative',]
              
societe_filiation= ["fils","fille","filles", "service","services",'agence','agences',
              "frère","frere","frères","freres",'direction',"division","divisions","filiales"]

societe_nom_ancient= ["ex","ex.","anc","anc.","ancienne",
                      "ancien", "anciennement"]


# In[624]:


grammatical=["le", "la", "les", "l'", "de","du",
             "des","d'","à", "a", "au", "aux","en","par",
             "sur","pour", "et","ses","&",'avant','(',")",",",":"]


# In[625]:


noise=["sté","sté.","ste","ets","éts","cie", "sa", "s.a.","s.a","sarl",
             "s.a.r.l.","s.a.r.l","dli","earl","société","societe", "sas", 'mme', 'union',
             "s.a.s.","s.a.s", "gaec", "g.a.e.c.", "g.a.e.c","compagnie", "etablissement",
             "établissement","etablissements","établissements","scea",'atelier','ateliers',
             "s.c.e.a.","s.c.e.a","sci", "s.c.i.","s.c.i","bp","groupe","groupes","site",
              "entreprises","entreprise","sca","s.c.a.","s.c.a","association","group",
              "groups",'cooperative',"fils","fille","filles", "service","services",'agence','agences',
              "frère","frere","frères","freres",'direction',"division","divisions","le", "la", "les", "l'", "de","du",
             "des","d'","à", "a", "au", "aux","en","par",
             "sur","pour", "et","ses","&",'avant',"ex","ex.","anc","anc.","ancienne",
                      "ancien", "anciennement"]


# In[ ]:





# In[626]:


def common(a,b):
    if a.lower() in b.lower():
        return a
    elif b.lower() in a.lower():
        return b
    else:
        return ""
    


# In[627]:


def common_list(a,b,c):
    lindex=list()
    assert len(a)<=len(b)
    la=list()
    lb=list()
    for m1 in a:
        la.append(m1.lower())
    for m2 in b:
        lb.append(m2.lower())
    for i in range(len(la)):
        m=la[i]
        if m not in c:
            if m in lb:
                lindex.append(i)
                
    if len(lindex) >0:
        return a[min(lindex):max(lindex)+1]
    else:
        return lindex


# In[628]:


import copy
l=[1,2,3]
tl=l.copy()
l.pop(0)
l.pop(0)
l.pop(0)
tl


# In[629]:


#On cherche dans une liste des token si il y a 
#des mots consécutifs qui commence par les lettre dans la list l 

def initial_matching(l, m, c):
    anonymes=list()
    rec=list()
    assert len(l)>0
    tl=l.copy()
    for i in range(len(m)):
        mm=m[i]
        im=mm[0].upper()
        #c est une dictionnaire d'exclusion, 
        #ça peut être une liste des mots grammaticaux
        #[] si on n'exclut pas de mot
        if mm.lower() not in c:
            if len(l)>0:
                #print(l)
                if im==l[0]:
                    #m=m[i:]
                    rec.append(mm)
                    l.pop(0)
                    if len(l)==0:
                        if i==len(m)-1:
                            result=rec.copy()
                            anonymes.append(result)
                else:
                    l=tl.copy()
                    rec=[]
            else:
                result=rec.copy()
                anonymes.append(result)
                #print(anonymes)
                l=tl.copy()
                #if len(l)>0:
                if im==l[0]:
                    #m=m[i:]
                    rec.append(mm)
                    l.pop(0)
                else:
                    l=tl.copy()
        else:
            rec.append(mm)
    return anonymes
            
        
        


# In[630]:


tokens("ETG (ex CHAUSSON) Emboutissage Tôlerie Gennevilliers",l1,l2)


# In[631]:


mots=initial_matching(["E", "T", "G"],['ETG', '(', 'ex', 'CHAUSSON', ')', 'Emboutissage', 'Tôlerie', 'Gennevilliers'],[])


# In[632]:


mots


# In[633]:


l=[1,2,3]
l.remove(2)


# In[634]:


l


# In[635]:


def Anonym(a,b,c):
    lindex=list()
    #assert len(a)<=len(b)
    #la=list()
    #lb=list()
    annonymes=list()
    ca=' '.join(a)
    cb=' '.join(b)
    #if not ca.isupper():
    for m1 in a:
        if m1.isupper():
            if m1.lower() not in c:
                lm1=list(m1)
                #if len(lm1) >1:
                #print(m1)
                while "." in lm1:
                    lm1.remove(".")
                if len(lm1) >1:
                    llm1=lm1.copy()
                    lanon1=initial_matching(lm1, a, [])
                    lm1=llm1.copy()
                    lanon2=initial_matching(lm1, a, c)
                    lm1=llm1.copy()
                    lanon3=initial_matching(lm1, b, [])
                    lm1=llm1.copy()
                    lanon4=initial_matching(lm1, b, c)
                    annonymes.append({m1:[lanon1, lanon2, lanon3, lanon4]})
    return annonymes
                
    #else:
    #    return []
    


# In[ ]:





# In[636]:


def find_common_in_shorter_string(ma,mb,l1,l2,lall):
#for so,sa,sb in couples:
    #for ma in sa:
    la=tokens(ma, l1, l2)
        #for mb in sb:
    lb=tokens(mb, l1, l2)
    if len(la)<len(lb):
        cm=common_list(la,lb,lall)
    if len(lb)<len(la):
        cm=common_list(lb,la,lall)
    if len(la)==len(lb):
        cm=common_list(la,lb,lall)
    return reverse_token(cm, l1,l2)
            #print(la)
            #print(lb)
            #print(cm)
            #print("\n")
            
        
        


# In[637]:


def reverse_token(l, l1,l2):
    sl=' '.join(l)
    assert len(l1)==len(l2)
    for i in range(len(l1)):
        sl=sl.replace(l2[i],l1[i])
    return sl
    


# In[638]:


l=["je", "l'", "ai", "fait"]
nl=reverse_token(l,l1,l2)
nl


# In[639]:


def clean_result(l, l1,l2):
    res=False
    rec=dict()
    for d in l:
        for k in d:
            v=d[k]
            for ll in v:
                if len(ll)>0:
                    res=True
                    #print(ll)
                    for e in ll:
                        ne=reverse_token(e, l1,l2)
                        rec[k]=rec.get(k,set())|{ne}
    if res:
        return rec
    else:
        return {}
                    
                


# In[640]:


#for sa,sb in couples:
def finding_anonyme(ma,mb,c,l1,l2):
    #for ma in sa:
    la=tokens(ma, l1, l2)
        #for mb in sb:
    lb=tokens(mb, l1, l2)
    ab=Anonym(la,lb,c)
    ba=Anonym(lb,la,c)
            
            #print(la)
            #print(lb)
            #print(aa)
    dab=clean_result(ab, l1, l2)
    dba=clean_result(ba, l1, l2)
    cr=dict()
    for k,v in dab.items():
        cr[k]=cr.get(k,set())|v
    for k,v in dba.items():
        cr[k]=cr.get(k,set())|v
    #return cr
    return dab, dba

            #print(cm)
            #print("\n")
            
        
        


# In[641]:


for so, sa, sb in couples:
    for ma in sa:
        for mb in sb:
            print(ma)
            print(mb)
            print(finding_anonyme(ma,mb,grammatical,l1,l2))
            print("\n")


# In[642]:


couples


# In[ ]:





# In[643]:


def decomposition(e):
    import re
    d=dict()
    e=e.strip().replace(" ex ",", ex ").replace(" anc ",", anc ").replace(" EX ",", EX ").replace(" ANC ",", ANC ")
    pat=r"(\W+(ex|anc|EX|Ex|ANC|Anc|ancien|Ancien|ANCIEN|anciens|Anciens|ANCIENS|ancienne|Ancienne|ANCIENNE|anciennes|Anciennes|ANCIENNES|anciennement|Anciennement|ANCIENNEMENT)[\.\s\:\-]+\w+[^,\)\(]*\)*)"
    prefix=r"(\W+(ex|anc|EX|Ex|ANC|Anc|ancien|Ancien|ANCIEN|anciens|Anciens|ANCIENS|ancienne|Ancienne|ANCIENNE|anciennes|Anciennes|ANCIENNES|anciennement|Anciennement|ANCIENNEMENT)[\.\s\:\-]+\s*)"
    l=re.findall(pat, " "+e)
    #print(l)
    nc=re.sub(pat, "", " "+e).strip()
    nl=[]
    nnl=[]
    for t in l:
        if len(t)>0:
            tt=" "+t[0].strip().lstrip("(").rstrip(")")
            if "(" not in tt:
                nl.append(re.sub(prefix,"",tt).strip())
            else:
                lcompt=tt.split("(")
                ltt=lcompt[0]
                nl.append({"main" : re.sub(prefix,"",ltt).strip(),"complement":lcompt[1:]})
                #nl.append({"complement":lcompt[1:]})
    if len(re.sub(pasmot,"",nc.strip()))<1:
        #print(e)
        #print(l)
        try:
            nc=nl[0]
        except:
            nc=e
        
    '''for n in nl:
        if ')' in n:
            if '(' not in n:
                nn=n.replace(")","")
                nnl.append(nn)
            else:
                nnl.append(nn)
        else:
            nnl.append(nn)'''
    #d[nc]={"ancient":nl}


    #for k in d:
    #dk=d[k]
    complec=r"\([^)]*\)*"
    l=re.findall(complec, nc)
    lcomp=[]
    for compl_e in l:
        nce=compl_e.strip().lstrip("(").rstrip(")").strip()
        
        lcomp.append(nce)
    
    nc=re.sub(complec, "", nc)
    
    #finding extension " - "
    
    #exts=re.compile(r"(\s*[-,.:]+\s+|\s+[-,.:]+\s*)")
    #exts=re.compile(r"\s*(\s-|-\s|\s,|,\s|\s\.|\.\s|\s\:|\:\s)\s*")
    exts=re.compile(r"\s*\+\s*|\s+-\s*|\s*-\s+|\s*,\s+|\s+,\s*|\s+\.\s+|\s+\.\s*|\s*\:\s+|\s+\:\s*")
    #le=nc.split(" - ")
    le=re.split(exts,nc)
    nc=le[0]
    if len(le)>0:
        le=le[1:]
    else:
        le=[]
        
        
    #finding alternative " / "
    sepex=re.compile(r"\s*\/\s*")
    #la=nc.split(" / ")
    la=re.split(sepex,nc)
    nc=la[0]
    if len(la)>0:
        la=la[1:]
    else:
        la=[]

    #print(nc)
    #d=dict()
    d[nc.strip()]={"ancient":nl, "complement":lcomp, "alternative":la, "extension":le}
    #print(d)
    #print("\n")
    return d


# In[644]:


l=[1,2,3]
l.pop(-1)


# In[645]:


l


# In[646]:


def remove_noise(m,l1,l2,l):
    if len(m)>0:
        if m[0].lower() in l:
            m.pop(0)
    if len(m)>0:
        if m[-1].lower() in l:
            m.pop(-1)
        
    
    '''for t in m:
        if t.lower() in l:
            #print(t)
            tb=t+" "
            te=" "+t
            tl=len(tb)
            if len(c)>tl:
                if c[:tl]==tb:
                    c=c[tl:].strip()
                if len(c)> tl:
                    #cl=len(c)
                    if c[-tl:] == te:
                        c=c[:-tl].strip()'''
    return reverse_token(m,l1,l2)


# In[647]:


def cleansing(ch,l1,l2,lr,threshold):
    m=tokens(ch, l1, l2)
    c=0
    while c<threshold:
        c+=1
        for r in lr: 
            ch=remove_noise(m,l1,l2,r)
            m=tokens(ch, l1, l2)
            #print(m)
    return ch.strip()
        


# In[648]:


#tokens("Cie d'ECLAIRAGE et de CHAUFFAGE par le GAZ de la BANLIEUE PARISIENNE",l1,l2)


# In[649]:


def enlever_anonyme(ch,anno,l1,l2,lr):
    ltk=tokens(ch,l1,l2)
    for ka in anno:
        while ka.upper() in ltk:
            ltk.remove(ka)
            
    nk=reverse_token(ltk,l1,l2)
    for punct in l1:
        c=0
        while punct in nk:
            nk=nk.strip().strip(punct).strip()
            c+=1
            if c>9:
                break


    clk=cleansing(nk,l1,l2,lr,10)
    if len(clk.strip()) == 0 :
        clk=cleansing(ch,l1,l2,lr,10)
    
    return clk

''' ltk1=tokens(k1,l1,l2)
                for ka in anno1:
                    while ka.upper() in ltk1:
                        ltk1.remove(ka)
                nk1=reverse_token(ltk1,l1,l2)
                for punct in l1:
                    c=0
                    while punct in nk1:
                        nk1=nk1.strip().strip(punct).strip()
                        c+=1
                        if c>9:
                            break

                    
                clk1=cleansing(nk1,l1,l2,lr,10)
                if len(clk1.strip()) == 0 :
                    clk1=cleansing(k1,l1,l2,lr,10)'''


# In[650]:


lall=[societe_type, grammatical,societe_filiation]


# In[651]:


lr=[societe_type, grammatical]


# In[652]:


lf=[societe_filiation,grammatical]


# In[653]:


lanc=[societe_nom_ancient, grammatical]


# In[654]:


tokens("S.A(S.A.R.L. DU FIBROCIMENT ET DES REVETEMENTS(STE",l1,l2,)


# In[655]:


cleansing("S.A(S.A.R.L. DU FIBROCIMENT ET DES REVETEMENTS(STE",l1,l2,lr,10)


# In[656]:


couples


# In[657]:


def uniformed(ch):
    import unidecode
    unaccented_string = unidecode.unidecode(ch.lower())
    return unaccented_string.replace(".","").strip()


# In[658]:


uniformed("Établissement")


# In[659]:


def symbol_split(ch,s):
    rec=""
    lr=list()
    for l in ch:
        if l in s:
            rec=rec.strip()
            if len(rec)>0:
                lr.append(rec)
                rec=""
        else:
            rec+=l
    rec=rec.strip()
    if len(rec)>0:
        lr.append(rec)
    return lr


# In[660]:


symbol_split('''abc (c'est "une eureur",/unique:  ''',dseg)


# In[661]:


def sub_generation(rec,d,k):
    nr=rec.copy()
    for e in rec:
        #ch=nc
        for v in d[k]:
            nc=e.replace(k,v)
            lnc=nc.strip().split(" ")
            while "" in lnc:
                lnc.remove("")
            nr.add(" ".join(lnc))
    return nr


# In[662]:


def iter_sub(ch,d):
    rec={ch}
    #lc=[ch]
    nc=ch
    for k in d:
        rec=sub_generation(rec,d,k)
        '''for e in rec:
            #ch=nc
            for v in d[k]:
                nc=e.replace(k,v)
                lnc=nc.strip().split(" ")
                while "" in lnc:
                    lnc.remove("")
                rec.add(" ".join(lnc))'''
    return list(rec)
            
        


# In[663]:


iter_sub("A.D.C.",dstop)


# In[664]:


#l1=["'","(",")",",","-",'"',"&"]
#l2=["' "," ( "," ) "," ,"," - ",' " '," & "]

#dstop={"&":[" ","et"],"-":[" "],"'":[' '],".":[""," "]}
#dseg={"(",")","/",":",";",",",'"',"[",']',"|"}

def seg_tensor(lm,dstop):
    nlm=list()
    for l in lm:
        nl=[]
        for m in l:
            nl+=iter_sub(m,dstop)
        nlm.append(nl)
    return nlm
            


# In[665]:


seg_tensor([['TRAPIL'], ['Dexel', 'G. Genet Ordures Services', 'Docks Pétroliers de Paris', "Pétrolière d'Importation"], ['Transports Pétroliers par Pipeline'], [], []],dstop)


# In[ ]:





# In[ ]:





# In[666]:


def list_dict(d):
    rec=list()
    if len(d)>0:
        for k in d:
            rec.append(k)
            for v in d[k]:
                rec.append(v)
    return rec


# In[ ]:





# In[667]:


def find_occur_inlist(lm1,lm2,l1,l2,o):
    count=0
    #print(l1)
    for m2 in lm2:
        for i1 in l1:
            for e in i1:
                if len(e)>0:
                    if m2 in e or e in m2:
                        #print((m2,e))
                        count=1
                        #return 1
    #print(l2)
    for m1 in lm1:
        for i2 in l2:
            for e in i2:
                if len(e)>0:
                    if m1 in e or e in m1:
                        #print((m1,e))
                        count=1
                    #return 1
        #print("\n\n")
    return count


# In[668]:


def find_occur_uniformed(lm1,lm2,l1,l2,o):
    count=0
    #print(l1)
    for m2 in lm2:
        for i1 in l1:
            for e in i1:
                if len(e)>0:
                    if uniformed(m2) in uniformed(e) or uniformed(e) in uniformed(m2) :
                        #print((m2,e))
                        count=1
                        #return 1
    #print(l2)
    for m1 in lm1:
        for i2 in l2:
            for e in i2:
                if len(e)>0:
                    if uniformed(m1) in uniformed(e) or uniformed(e) in uniformed(m1) :
                        #print((m1,e))
                        count=1
                    #return 1
        #print("\n\n")
    return count


# In[669]:


def find_occur_tensor(llm1,llm2,l1,l2,o):
    count=0
    #print(l1)
    for lm2 in llm2:
        for m2 in lm2:
            for i1 in l1:
                for e in i1:
                    if len(e)>0:
                        if m2 in e or e in m2 :
                            #print((m2,e))
                            count=1
                            #return 1
                        else:
                            for eo in o:
                                if m2 in eo or eo in m2:
                                    count=1
    #print(l2)
    for lm1 in llm1:
        for m1 in lm1:
            for i2 in l2:
                for e in i2:
                    if len(e)>0:
                        if m1 in e or e in m1 :
                            #print((m1,e))
                            count=1
                        else:
                            for eo in o:
                                if e in eo or eo in e:
                                    count=1
                    #return 1
        #print("\n\n")
    return count


# In[670]:


def find_occur_tensor_uniformed(llm1,llm2,l1,l2,o):
    count=0
    #print(l1)
    for lm2 in llm2:
        for m2 in lm2:
            for i1 in l1:
                for e in i1:
                    if len(e)>0:
                        if uniformed(m2) in uniformed(e) or uniformed(e) in uniformed(m2):
                            #if uniformed(m2) != uniformed(e):
                            #    print((m2,e))
                            count=1
                            #return 1
                        else:
                            for eo in o:
                                if uniformed(m2) in uniformed(eo) or uniformed(eo) in uniformed(m2):
                                    count=1
    #print(l2)
    for lm1 in llm1:
        for m1 in lm1:
            for i2 in l2:
                for e in i2:
                    if len(e)>0:
                        if uniformed(m1) in uniformed(e) or uniformed(e) in uniformed(m1) :
                            #print((m1,e))
                            #if uniformed(m1) != uniformed(e):
                            #    print((m1,e))
                            count=1
                        else:
                            for eo in o:
                                if uniformed(e) in uniformed(eo) or uniformed(eo) in uniformed(e):
                                    count=1
                    #return 1
    print("\n\n")
    return count


# In[671]:


def cleansing_tensor(lm,l1,l2,lr,threshold):
    nlm=list()
    for l in lm:
        nl=list()
        for m in l:
            nm=cleansing(m,l1,l2,lr,threshold)
            nl.append(nm)
            
        nlm.append(nl)
    return nlm
            
        


# In[ ]:





# In[684]:


all_count=0
cr_segment=0
f_segment=0
foundby_segment=0
lv=list()
import re
pasmot=r'\W+'
for o,b,a in couples:
    #rule 1, ancient sites
    for i1 in b:
        d1=decomposition(i1)
        for i2 in a:
            all_count+=1
            #print(e1)
            #print(e2)
            #print(e1)
            cmab=find_common_in_shorter_string(i1,i2,l1,l2,noise)
            
            
            #d1=decomposition(i1)
            d2=decomposition(i2)
            
            anno1, anno2=finding_anonyme(i1,i2,grammatical,l1,l2)
            
            
            #print("\n\n")
            #print(d1)
            for k1,v1 in d1.items() :
                a1=v1["ancient"]
                at1=[]
                if len(a1)>0:
                    for ea in a1:
                        if type(ea)==dict:
                            at1.append(ea["main"])
                            #at1+=ea["complement"]
                        else:
                            at1.append(ea)
                            
                #if type(a1)==dict:
                #    a1=[]
                c1=v1["complement"]
                t1=v1["alternative"]
                e1=v1["extension"]
                #clk1=enlever_anonyme(k1,anno1,l1,l2,lall)
                clk1=enlever_anonyme(k1,anno1,l1,l2,[])
                #clk1=cleansing(k1,l1,l2,lr,10)
                lm1=[[k1],at1,c1,t1,e1,list_dict(anno1),[clk1]]
                #nlm1=cleansing_tensor(lm1,l1,l2,lf,10)
                slm1=seg_tensor(lm1,dstop)
                nlm1=cleansing_tensor(slm1,l1,l2,lall,10)
                
            for k2,v2 in d2.items():
                #if k2=='PROPETROL SA':
                #    print(d2)

                a2=v2["ancient"]
                at2=list()
                if len(a2)>0:
                    for ea in a2:
                        if type(ea)==dict:
                            at2.append(ea["main"])
                            #at2+=ea["complement"]
                            #at2.append(list(ea.values()))
                        else:
                            at2.append(ea)
                c2=v2["complement"]
                t2=v2["alternative"]
                e2=v2["extension"]

                #clk2=cleansing(k2,l1,l2,lr,10)
                clk2=enlever_anonyme(k2,anno2,l1,l2,[])
                #clk2=enlever_anonyme(k2,anno2,l1,l2,lall)
                lm2=[[k2],at2,c2,t2,e2, list_dict(anno2), [clk2]]
                #nlm2=cleansing_tensor(lm2,l1,l2,lf,10)
                slm2=seg_tensor(lm2,dstop)
                nlm2=cleansing_tensor(slm2,l1,l2,lall,10)
                #print(i1)
                #print(lm1[:5])
                #o51=lm1[:5]
                #n51=slm1[:5]
                #print(slm1[:5])
                #o52=lm2[:5]
                #n52=slm2[:5]
                #print(i2)
                #print(lm2[:5])
                #print(slm2[:5])
                #print(i1)
                #print(i2)
                #print(lm1)
                #print(lm2)
                #print("\n\n")
                if uniformed(i1)!=i1 or uniformed(i2)!=i2:
                    cr_segment+=1
                    if find_occur_tensor_uniformed([[i1]],[[i2]],[[i1]],[[i2]],o)==0:
                        f_segment+=1
                        foundby_segment+=find_occur_tensor_uniformed(nlm1,nlm2,nlm1,nlm2,o)
                    
                #if uniformed(i1)!=i1 or uniformed(i2)!=i2:
                #    cr_segment+=1
                #    if find_occur_tensor(o51,o52,o51,o52,o)==0:
                #        f_segment+=1
                #    foundby_segment+=find_occur_tensor_uniformed(o51,o52,o51,o52,o)
                #if o51!=n51 or o52!=n52:
                #    cr_segment+=1
                #    if find_occur_tensor_uniformed([[i1]],[[i2]],[[i1]],[[i2]],o)==0:
                    #if find_occur_tensor_uniformed(o51,o52,o51,o52,o)==0:
                #        f_segment+=1
                 #   foundby_segment+=find_occur_tensor_uniformed(n51,n52,n51,n52,o)
                #if len(anno1)+len(anno2) > 0 :
                #if uniformed(i1)!=uniformed(i2):
                    #if find_occur_tensor_uniformed(lm1,lm2,lm1,lm2,o) == 0:
                    
                    #if clk2!=k2 or clk1!=k1 :
                #    cr_segment+=1
                #if len(at1)+len(at2)+len(c1)+len(c2)+len(t1)+len(t2)+len(e1)+len(e2) >0:
                #if len(at1)+len(at2) > 0 :
                #if k1 not in k2 and k2 not in k1:
                    #if find_occur_uniformed(lan1,lan2,[[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,])
                    #if find_occur_uniformed([i1],[i2],[[i1]],[[i2]],o)==0:
                    #if find_occur_tensor_uniformed([[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,],[[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,],o)==0:
                    #    if len(cmab)>0:
                    #        print(cmab)
                    #        print(i1)
                    #        print(i2)
                    #        print(lm1)
                    #        print(lm2)
                    #        print("\n\n")
                    
                    #cr_segment+=1
                    #if find_occur_tensor_uniformed([[i1]],[[i2]],[[i1]],[[i2]],o)==0:
                    #if find_occur_tensor_uniformed([[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,],[[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,],o)==0:
                     #   f_segment+=1
                    #foundby_segment+=find_occur_tensor_uniformed(lm1,lm2,lm1,lm2,o)
                        #foundby_segment+=find_occur_tensor_uniformed([[k1],at1,c1,t1,e1,list_dict(anno1)],[[k2],at2,c2,t2,e2,list_dict(anno2)],[[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,],o)
                #if k1==k2 or k1 in at2 or k2 in at1:
                #    foundby_segment+=1
                    #lan1=list(anno1.keys())
                    #lan2=list(anno2.keys())
                    #foundby_segment+=find_occur_tensor_uniformed([list_dict(anno1)+[clk1]],[list_dict(anno2)+[clk2]],[[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,],o)
                    #foundby_segment+=find_occur_uniformed([clk1],[clk2],[[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,],o)
                #lan1=list(anno1.keys())
                #lan2=list(anno2.keys())
                #if find_occur_tensor_uniformed([[clk1],at1,c1,t1,e1,lan1],[[clk2],at2,c2,t2,e2,lan2],[[clk1],at1,c1,t1,e1,lan1],[[clk2],at2,c2,t2,e2,lan2],o) == 1:

                #foundby_segment+=find_occur_tensor_uniformed([[clk1],at1,c1,t1,e1,lan1],[[clk2],at2,c2,t2,e2,lan2],[[clk1],at1,c1,t1,e1,lan1],[[clk2],at2,c2,t2,e2,lan2])
                #if find_occur_uniformed(lan1,lan2,[[k1],at1,c1,t1,e1],[[k2],at2,c2,t2,e2,]) == 0:
                        
                    #print(i1)
                    #    print(i2)
                    #    print(lm1)
                    #    print(lm2)
                    #    print("\n\n")


                    
            
            #print(i1)
            #print(i2)
            #print(lm1)
            #print(lm2)
            #print("\n\n")
        ''' print(k1)
            print(cleansing(k1,l1,l2,lr,10))
            print(k2)
            print(cleansing(k2,l1,l2,lr,10))'''
        
        #essayer de calculer l'augmentation de corpus par la segmentation
        #chercher les segments dans les variantions extraites
        #choisir les bon résultats et 
        #afficher les règles qui sont appliqués pour les obtenir
        
                    


# In[685]:


#valide les commentaires

# change - into espace, change & to et or espace
# SPLIT par SARL, Cie etc.
# change word order (for two tokens) yes 
# 


# In[686]:


cr_segment


# In[687]:


f_segment


# In[688]:


all_count


# In[689]:


foundby_segment


# In[33]:


def find_occur_inlist(lm1,lm2,l1,l2):
    count=0
    #print(l1)
    for m2 in lm2:
        for i1 in l1:
            for e in i1:
                if len(e)>0:
                    if m2 in e or e in m2:
                        #print((m2,e))
                        count=1
                        #return 1
    #print(l2)
    for m1 in lm1:
        for i2 in l2:
            for e in i2:
                if len(e)>0:
                    if m1 in e or e in m1:
                        #print((m1,e))
                        count=1
                    #return 1
        #print("\n\n")
    return count


# In[34]:


def find_occur_uniformed(lm1,lm2,l1,l2):
    count=0
    #print(l1)
    for m2 in lm2:
        for i1 in l1:
            for e in i1:
                if len(e)>0:
                    if uniformed(m2) in uniformed(e) or uniformed(e) in uniformed(m2) :
                        #print((m2,e))
                        count=1
                        #return 1
    #print(l2)
    for m1 in lm1:
        for i2 in l2:
            for e in i2:
                if len(e)>0:
                    if uniformed(m1) in uniformed(e) or uniformed(e) in uniformed(m1) :
                        #print((m1,e))
                        count=1
                    #return 1
        #print("\n\n")
    return count


# In[35]:


def find_occur_tensor(llm1,llm2,l1,l2):
    count=0
    #print(l1)
    for lm2 in llm2:
        for m2 in lm2:
            for i1 in l1:
                for e in i1:
                    if len(e)>0:
                        if m2 in e or e in m2 :
                            #print((m2,e))
                            count=1
                            #return 1
    #print(l2)
    for lm1 in llm1:
        for m1 in lm1:
            for i2 in l2:
                for e in i2:
                    if len(e)>0:
                        if m1 in e or e in m1 :
                            #print((m1,e))
                            count=1
                    #return 1
        #print("\n\n")
    return count


# In[36]:


def find_occur_tensor_uniformed(llm1,llm2,l1,l2):
    count=0
    #print(l1)
    for lm2 in llm2:
        for m2 in lm2:
            for i1 in l1:
                for e in i1:
                    if len(e)>0:
                        if uniformed(m2) in uniformed(e) or uniformed(e) in uniformed(m2) :
                            #print((m2,e))
                            count=1
                            #return 1
    #print(l2)
    for lm1 in llm1:
        for m1 in lm1:
            for i2 in l2:
                for e in i2:
                    if len(e)>0:
                        if uniformed(m1) in uniformed(e) or uniformed(e) in uniformed(m1) :
                            #print((m1,e))
                            count=1
                    #return 1
        #print("\n\n")
    return count


# In[ ]:





# In[167]:


find_occur_inlist(["a"],["b"],[["b"],["bcd"]],[["b"],["bcd"]])


# In[181]:


tokens("BIEBER  Ets S.A.R.L.", l1, l2)


# In[175]:


remove_noise(['BIEBER', 'Ets', 'S.A.R.L.'],"BIEBER  Ets S.A.R.L.",societe_type)


# In[146]:


lv=list()
import re
pasmot=r'\W+'
for b,a in couples:
    #rule 1, ancient sites
    for e in a:
        d=dict()
        pat=r"(\W+(ex|anc|EX|Ex|ANC|Anc|ancien|Ancien|ANCIEN|anciens|Anciens|ANCIENS|ancienne|Ancienne|ANCIENNE|anciennes|Anciennes|ANCIENNES|anciennement|Anciennement|ANCIENNEMENT)[\.\s\:\-]+\w+[^,\)]*\)*)"
        prefix=r"(\W+(ex|anc|EX|Ex|ANC|Anc|ancien|Ancien|ANCIEN|anciens|Anciens|ANCIENS|ancienne|Ancienne|ANCIENNE|anciennes|Anciennes|ANCIENNES|anciennement|Anciennement|ANCIENNEMENT)[\.\s\:\-]+\s*)"
        l=re.findall(pat, e)
        nc=re.sub(pat, "", e)
        nl=[]
        nnl=[]
        for t in l:
            if len(t)>0:
                nl.append(re.sub(prefix,"",t[0]).rstrip(")"))
        #print(l)
        
        print(e)
        #print(nc)
        if len(re.sub(pasmot,"",nc.strip()))<1:
            nc=e
        #nnl=[]
        '''for n in nl:
            if ')' in n:
                if '(' not in n:
                    nn=n.replace(")","")
                    nnl.append(nn)
                else:
                    nnl.append(nn)
            else:
                nnl.append(nn)'''
        d[nc]={"ancient":nl}
        
        
        for k in d:
            dk=d[k]
            pat=r"\([^)]*\)"
            l=re.findall(pat, k)
            nc=re.sub(pat, "", k)
            #finding alternative " / "
            la=nc.split(" / ")
            nc=la[0]
            if len(la)>0:
                la=la[1:]
            else:
                la=[]
            #finding extension " - "
            le=nc.split(" - ")
            nc=le[0]
            if len(le)>0:
                le=le[1:]
            else:
                le=[]
            
            print(nc)
            d=dict()
            d[nc]={"ancient":dk, "complement":l, "alternative":la, "extension":le}
            print(d)
            print("\n")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[73]:





# In[ ]:





# In[352]:


import re
for o,b,a in couples:
    #rule 1, ancient sites
    for e in a:
        if '+' in e:
            print(e+"\n")


# In[70]:


n="123)"
nn=n.replace(")","")


# In[71]:


nn


# In[ ]:




