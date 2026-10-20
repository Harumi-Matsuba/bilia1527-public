# 1回目の書き起こしと Codex の書き起こしを、行ごとに編集距離で対応させて比べる。
# 一致率＝（名前が一致した記号）/（1回目の記号の数）。値での一致（鍵で同じ値になる別名を同じとみる）も出す。
# 使い方: xcompare.py 1回目 鍵 codex1.txt [codex2.txt ...]  → 標準出力に要約、compare.tsv に行ごとの食い違い
import sys,re
sys.path.insert(0,__file__.rsplit('/',1)[0])
from decode import tokens, norm, load_key
def canon(t):
    t=t.strip().rstrip('?')
    t=t.replace('⁄','/')
    if '/' in t and not t.startswith('('): t=t.split('/')[0]
    t=re.sub(r'^([GBoHR])\.0?(\d+)$',r'\1.\2',t)
    return t
def parse_codex(p):
    d={}
    for line in open(p):
        line=line.strip().strip('`')
        m=re.match(r'^([rv])_L(\d+)\s*(.*)$',line)
        if not m: continue
        lab=('102r.' if m.group(1)=='r' else '102v.')+m.group(2).zfill(2)
        toks=re.findall(r'\(\s*\d+\s*\)|\[[^\]]*\]|\S+',m.group(3))
        d[lab]=[canon(t.replace(' ','')) for t in toks if not t.startswith('[')]
    return d
def align(a,b):
    n,m=len(a),len(b); D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0]=i
    for j in range(m+1): D[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            D[i][j]=min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+(a[i-1]!=b[j-1]))
    i,j=n,m; pairs=[]
    while i>0 or j>0:
        if i>0 and j>0 and D[i][j]==D[i-1][j-1]+(a[i-1]!=b[j-1]): pairs.append((a[i-1],b[j-1])); i-=1; j-=1
        elif i>0 and D[i][j]==D[i-1][j]+1: pairs.append((a[i-1],None)); i-=1
        else: pairs.append((None,b[j-1])); j-=1
    return pairs[::-1]
if __name__=='__main__':
    mine={lab:[canon(t) for t in ts] for lab,ts in tokens(sys.argv[1])}
    key=load_key(sys.argv[2])
    val=lambda t: key.get(t,'<'+str(t)+'>') if t is not None else None
    out=open(sys.argv[3].rsplit('/',1)[0]+'/compare.tsv','w') if len(sys.argv)>3 else None
    N=sum(len(v) for v in mine.values())
    for p in sys.argv[3:]:
        cx=parse_codex(p); same=sameval=0; miss=[lab for lab in mine if lab not in cx]
        for lab,a in mine.items():
            b=cx.get(lab,[])
            for x,y in align(a,b):
                if x is None: continue
                if x==y: same+=1
                if y is not None and val(x)==val(y): sameval+=1
                elif out and x!=y: out.write(f'{p.rsplit("/",1)[1]}\t{lab}\t{x}\t{y}\n')
        print(f'{p}: 1回目の記号 {N}、名前の一致 {same} ({100*same/N:.1f}%)、値の一致 {sameval} ({100*sameval/N:.1f}%)、Codex にない行 {miss}')
