# ページごとの一致率。使い方: perpage.py 書き起こし 鍵 codex...
import sys; sys.path.insert(0,__file__.rsplit('/',1)[0])
from xcompare import parse_codex, align, canon
from decode import tokens, load_key
k=load_key(sys.argv[2]); val=lambda t: k.get(t,'<'+str(t)+'>') if t else None
mine={lab:[canon(t) for t in ts] for lab,ts in tokens(sys.argv[1])}
for p in sys.argv[3:]:
    cx=parse_codex(p); res=[]
    for page in ('102r','102v'):
        N=s=v=0
        for lab,a in mine.items():
            if not lab.startswith(page): continue
            N+=len(a)
            for x,y in align(a,cx.get(lab,[])):
                if x is None: continue
                s+= x==y; v+= (y is not None and val(x)==val(y))
        res.append(f'{page} {N}記号 名前{100*s/N:.1f}% 値{100*v/N:.1f}%')
    print(p,' / '.join(res))
