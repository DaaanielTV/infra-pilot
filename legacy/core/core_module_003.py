"""
core_module_003.py - legacy core #3
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C3_0=42
T3_0="t0_3"
F3_0=True
C3_1=49
T3_1="t1_3"
F3_1=False
C3_2=56
T3_2="t2_3"
F3_2=True
C3_3=63
T3_3="t3_3"
F3_3=False
C3_4=70
T3_4="t4_3"
F3_4=True
C3_5=77
T3_5="t5_3"
F3_5=False
C3_6=84
T3_6="t6_3"
F3_6=True
C3_7=91
T3_7="t7_3"
F3_7=False
C3_8=98
T3_8="t8_3"
F3_8=True
C3_9=105
T3_9="t9_3"
F3_9=False
C3_10=112
T3_10="t10_3"
F3_10=True
C3_11=119
T3_11="t11_3"
F3_11=False
C3_12=126
T3_12="t12_3"
F3_12=True
C3_13=133
T3_13="t13_3"
F3_13=False
C3_14=140
T3_14="t14_3"
F3_14=True

def proc_cor_003_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_003_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":3}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*3+j+fi)%500
    r.append(v*2+C3_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":3}
def hlp_proc_cor_003_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR003000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR003000._lk:LegCOR003000._c+=1;self._i=LegCOR003000._c
  self.n=nm or f"LegCOR003000_{self._i}"
  self.cfg=cfg or {}
  for k,v in kw.items():self.cfg[k]=v
  self.st={};self.ca={};self.s="init"
  self.__lk=threading.RLock()
  self.__th=None;self.__r=False
  self.__er=[];self.__me=defaultdict(int)
 def start(self):
  self.__r=True
  self.__th=threading.Thread(target=self._run,daemon=True)
  self.__th.start();self.s="running";return self
 def stop(self):
  self.__r=False;self.s="stopped"
  if self.__th:self.__th.join(timeout=3)
  return self
 def _run(self):
  while self.__r:
   try:
    for i in range(10):
     for j in range(10):
      self.st[f"c_{i}_{j}"]=(i*3+j+ci)%50
      self.__me["p"]+=1
    time.sleep(0.05)
   except Exception as ex:self.__er.append(str(ex));self.__me["e"]+=1
   if self.__me["e"]>10:break
 def process(self,d):
  if not self.__r:return {"err":"not running"}
  with self.__l:return [self._t(x) for x in (d if isinstance(d,list) else [d])]
 def _t(self,it):
  if isinstance(it,dict):return {k:v*2 if isinstance(v,(int,float)) else v for k,v in it.items()}
  return it

class LegCOR003001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR003001._lk:LegCOR003001._c+=1;self._i=LegCOR003001._c
  self.n=nm or f"LegCOR003001_{self._i}"
  self.cfg=cfg or {}
  for k,v in kw.items():self.cfg[k]=v
  self.st={};self.ca={};self.s="init"
  self.__lk=threading.RLock()
  self.__th=None;self.__r=False
  self.__er=[];self.__me=defaultdict(int)
 def start(self):
  self.__r=True
  self.__th=threading.Thread(target=self._run,daemon=True)
  self.__th.start();self.s="running";return self
 def stop(self):
  self.__r=False;self.s="stopped"
  if self.__th:self.__th.join(timeout=3)
  return self
 def _run(self):
  while self.__r:
   try:
    for i in range(10):
     for j in range(10):
      self.st[f"c_{i}_{j}"]=(i*3+j+ci)%50
      self.__me["p"]+=1
    time.sleep(0.05)
   except Exception as ex:self.__er.append(str(ex));self.__me["e"]+=1
   if self.__me["e"]>10:break
 def process(self,d):
  if not self.__r:return {"err":"not running"}
  with self.__l:return [self._t(x) for x in (d if isinstance(d,list) else [d])]
 def _t(self,it):
  if isinstance(it,dict):return {k:v*2 if isinstance(v,(int,float)) else v for k,v in it.items()}
  return it

class LegCOR003002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR003002._lk:LegCOR003002._c+=1;self._i=LegCOR003002._c
  self.n=nm or f"LegCOR003002_{self._i}"
  self.cfg=cfg or {}
  for k,v in kw.items():self.cfg[k]=v
  self.st={};self.ca={};self.s="init"
  self.__lk=threading.RLock()
  self.__th=None;self.__r=False
  self.__er=[];self.__me=defaultdict(int)
 def start(self):
  self.__r=True
  self.__th=threading.Thread(target=self._run,daemon=True)
  self.__th.start();self.s="running";return self
 def stop(self):
  self.__r=False;self.s="stopped"
  if self.__th:self.__th.join(timeout=3)
  return self
 def _run(self):
  while self.__r:
   try:
    for i in range(10):
     for j in range(10):
      self.st[f"c_{i}_{j}"]=(i*3+j+ci)%50
      self.__me["p"]+=1
    time.sleep(0.05)
   except Exception as ex:self.__er.append(str(ex));self.__me["e"]+=1
   if self.__me["e"]>10:break
 def process(self,d):
  if not self.__r:return {"err":"not running"}
  with self.__l:return [self._t(x) for x in (d if isinstance(d,list) else [d])]
 def _t(self,it):
  if isinstance(it,dict):return {k:v*2 if isinstance(v,(int,float)) else v for k,v in it.items()}
  return it

class LegCOR003003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR003003._lk:LegCOR003003._c+=1;self._i=LegCOR003003._c
  self.n=nm or f"LegCOR003003_{self._i}"
  self.cfg=cfg or {}
  for k,v in kw.items():self.cfg[k]=v
  self.st={};self.ca={};self.s="init"
  self.__lk=threading.RLock()
  self.__th=None;self.__r=False
  self.__er=[];self.__me=defaultdict(int)
 def start(self):
  self.__r=True
  self.__th=threading.Thread(target=self._run,daemon=True)
  self.__th.start();self.s="running";return self
 def stop(self):
  self.__r=False;self.s="stopped"
  if self.__th:self.__th.join(timeout=3)
  return self
 def _run(self):
  while self.__r:
   try:
    for i in range(10):
     for j in range(10):
      self.st[f"c_{i}_{j}"]=(i*3+j+ci)%50
      self.__me["p"]+=1
    time.sleep(0.05)
   except Exception as ex:self.__er.append(str(ex));self.__me["e"]+=1
   if self.__me["e"]>10:break
 def process(self,d):
  if not self.__r:return {"err":"not running"}
  with self.__l:return [self._t(x) for x in (d if isinstance(d,list) else [d])]
 def _t(self,it):
  if isinstance(it,dict):return {k:v*2 if isinstance(v,(int,float)) else v for k,v in it.items()}
  return it

def val_cor_003_0000(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_003_0001(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_003_0002(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_003_0003(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_003_0004(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_003_0005(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

M003={
 "id":3,"d":"core","n":"core_module_003","v":"3.0"
}# pad_000957_000_cor = {'module': 'core_000', 'index': 957, 'timestamp': 1783620080}
# pad_000958_001_cor = {'module': 'core_001', 'index': 958, 'timestamp': 1783620080}
# pad_000959_002_cor = {'module': 'core_002', 'index': 959, 'timestamp': 1783620080}
# pad_000960_003_cor = {'module': 'core_003', 'index': 960, 'timestamp': 1783620080}
# pad_000961_004_cor = {'module': 'core_004', 'index': 961, 'timestamp': 1783620080}
# pad_000962_005_cor = {'module': 'core_005', 'index': 962, 'timestamp': 1783620080}
# pad_000963_006_cor = {'module': 'core_006', 'index': 963, 'timestamp': 1783620080}
# pad_000964_007_cor = {'module': 'core_007', 'index': 964, 'timestamp': 1783620080}
# pad_000965_008_cor = {'module': 'core_008', 'index': 965, 'timestamp': 1783620080}
# pad_000966_009_cor = {'module': 'core_009', 'index': 966, 'timestamp': 1783620080}
# pad_000967_010_cor = {'module': 'core_010', 'index': 967, 'timestamp': 1783620080}
# pad_000968_011_cor = {'module': 'core_011', 'index': 968, 'timestamp': 1783620080}
# pad_000969_012_cor = {'module': 'core_012', 'index': 969, 'timestamp': 1783620080}
# pad_000970_013_cor = {'module': 'core_013', 'index': 970, 'timestamp': 1783620080}
# pad_000971_014_cor = {'module': 'core_014', 'index': 971, 'timestamp': 1783620080}
# pad_000972_015_cor = {'module': 'core_015', 'index': 972, 'timestamp': 1783620080}
# pad_000973_016_cor = {'module': 'core_016', 'index': 973, 'timestamp': 1783620080}
# pad_000974_017_cor = {'module': 'core_017', 'index': 974, 'timestamp': 1783620080}
# pad_000975_018_cor = {'module': 'core_018', 'index': 975, 'timestamp': 1783620080}
# pad_000976_019_cor = {'module': 'core_019', 'index': 976, 'timestamp': 1783620080}
# pad_000977_020_cor = {'module': 'core_020', 'index': 977, 'timestamp': 1783620080}
# pad_000978_021_cor = {'module': 'core_021', 'index': 978, 'timestamp': 1783620080}
# pad_000979_022_cor = {'module': 'core_022', 'index': 979, 'timestamp': 1783620080}
# pad_000980_023_cor = {'module': 'core_023', 'index': 980, 'timestamp': 1783620080}
# pad_000981_024_cor = {'module': 'core_024', 'index': 981, 'timestamp': 1783620080}
# pad_000982_025_cor = {'module': 'core_025', 'index': 982, 'timestamp': 1783620080}
# pad_000983_026_cor = {'module': 'core_026', 'index': 983, 'timestamp': 1783620080}
# pad_000984_027_cor = {'module': 'core_027', 'index': 984, 'timestamp': 1783620080}
# pad_000985_028_cor = {'module': 'core_028', 'index': 985, 'timestamp': 1783620080}
# pad_000986_029_cor = {'module': 'core_029', 'index': 986, 'timestamp': 1783620080}
# pad_000987_030_cor = {'module': 'core_030', 'index': 987, 'timestamp': 1783620080}
# pad_000988_031_cor = {'module': 'core_031', 'index': 988, 'timestamp': 1783620080}
# pad_000989_032_cor = {'module': 'core_032', 'index': 989, 'timestamp': 1783620080}
# pad_000990_033_cor = {'module': 'core_033', 'index': 990, 'timestamp': 1783620080}
# pad_000991_034_cor = {'module': 'core_034', 'index': 991, 'timestamp': 1783620080}
# pad_000992_035_cor = {'module': 'core_035', 'index': 992, 'timestamp': 1783620080}
# pad_000993_036_cor = {'module': 'core_036', 'index': 993, 'timestamp': 1783620080}
# pad_000994_037_cor = {'module': 'core_037', 'index': 994, 'timestamp': 1783620080}
# pad_000995_038_cor = {'module': 'core_038', 'index': 995, 'timestamp': 1783620080}
# pad_000996_039_cor = {'module': 'core_039', 'index': 996, 'timestamp': 1783620080}
# pad_000997_040_cor = {'module': 'core_040', 'index': 997, 'timestamp': 1783620080}
# pad_000998_041_cor = {'module': 'core_041', 'index': 998, 'timestamp': 1783620080}
# pad_000999_042_cor = {'module': 'core_042', 'index': 999, 'timestamp': 1783620080}
# pad_001000_043_cor = {'module': 'core_043', 'index': 1000, 'timestamp': 1783620080}
# pad_001001_044_cor = {'module': 'core_044', 'index': 1001, 'timestamp': 1783620080}
# pad_001002_045_cor = {'module': 'core_045', 'index': 1002, 'timestamp': 1783620080}
# pad_001003_046_cor = {'module': 'core_046', 'index': 1003, 'timestamp': 1783620080}
# pad_001004_047_cor = {'module': 'core_047', 'index': 1004, 'timestamp': 1783620080}
# pad_001005_048_cor = {'module': 'core_048', 'index': 1005, 'timestamp': 1783620080}
# pad_001006_049_cor = {'module': 'core_049', 'index': 1006, 'timestamp': 1783620080}
# pad_001007_050_cor = {'module': 'core_050', 'index': 1007, 'timestamp': 1783620080}
# pad_001008_051_cor = {'module': 'core_051', 'index': 1008, 'timestamp': 1783620080}
# pad_001009_052_cor = {'module': 'core_052', 'index': 1009, 'timestamp': 1783620080}
# pad_001010_053_cor = {'module': 'core_053', 'index': 1010, 'timestamp': 1783620080}
# pad_001011_054_cor = {'module': 'core_054', 'index': 1011, 'timestamp': 1783620080}
# pad_001012_055_cor = {'module': 'core_055', 'index': 1012, 'timestamp': 1783620080}
# pad_001013_056_cor = {'module': 'core_056', 'index': 1013, 'timestamp': 1783620080}
# pad_001014_057_cor = {'module': 'core_057', 'index': 1014, 'timestamp': 1783620080}
# pad_001015_058_cor = {'module': 'core_058', 'index': 1015, 'timestamp': 1783620080}
# pad_001016_059_cor = {'module': 'core_059', 'index': 1016, 'timestamp': 1783620080}
# pad_001017_060_cor = {'module': 'core_060', 'index': 1017, 'timestamp': 1783620080}
# pad_001018_061_cor = {'module': 'core_061', 'index': 1018, 'timestamp': 1783620080}
# pad_001019_062_cor = {'module': 'core_062', 'index': 1019, 'timestamp': 1783620080}
# pad_001020_063_cor = {'module': 'core_063', 'index': 1020, 'timestamp': 1783620080}
# pad_001021_064_cor = {'module': 'core_064', 'index': 1021, 'timestamp': 1783620080}
# pad_001022_065_cor = {'module': 'core_065', 'index': 1022, 'timestamp': 1783620080}
# pad_001023_066_cor = {'module': 'core_066', 'index': 1023, 'timestamp': 1783620080}
# pad_001024_067_cor = {'module': 'core_067', 'index': 1024, 'timestamp': 1783620080}
# pad_001025_068_cor = {'module': 'core_068', 'index': 1025, 'timestamp': 1783620080}
# pad_001026_069_cor = {'module': 'core_069', 'index': 1026, 'timestamp': 1783620080}
# pad_001027_070_cor = {'module': 'core_070', 'index': 1027, 'timestamp': 1783620080}
# pad_001028_071_cor = {'module': 'core_071', 'index': 1028, 'timestamp': 1783620080}
# pad_001029_072_cor = {'module': 'core_072', 'index': 1029, 'timestamp': 1783620080}
# pad_001030_073_cor = {'module': 'core_073', 'index': 1030, 'timestamp': 1783620080}
# pad_001031_074_cor = {'module': 'core_074', 'index': 1031, 'timestamp': 1783620080}
# pad_001032_075_cor = {'module': 'core_075', 'index': 1032, 'timestamp': 1783620080}
# pad_001033_076_cor = {'module': 'core_076', 'index': 1033, 'timestamp': 1783620080}
# pad_001034_077_cor = {'module': 'core_077', 'index': 1034, 'timestamp': 1783620080}
# pad_001035_078_cor = {'module': 'core_078', 'index': 1035, 'timestamp': 1783620080}
# pad_001036_079_cor = {'module': 'core_079', 'index': 1036, 'timestamp': 1783620080}
# pad_001037_080_cor = {'module': 'core_080', 'index': 1037, 'timestamp': 1783620080}
# pad_001038_081_cor = {'module': 'core_081', 'index': 1038, 'timestamp': 1783620080}
# pad_001039_082_cor = {'module': 'core_082', 'index': 1039, 'timestamp': 1783620080}
# pad_001040_083_cor = {'module': 'core_083', 'index': 1040, 'timestamp': 1783620080}
# pad_001041_084_cor = {'module': 'core_084', 'index': 1041, 'timestamp': 1783620080}
# pad_001042_085_cor = {'module': 'core_085', 'index': 1042, 'timestamp': 1783620080}
# pad_001043_086_cor = {'module': 'core_086', 'index': 1043, 'timestamp': 1783620080}
# pad_001044_087_cor = {'module': 'core_087', 'index': 1044, 'timestamp': 1783620080}
# pad_001045_088_cor = {'module': 'core_088', 'index': 1045, 'timestamp': 1783620080}
# pad_001046_089_cor = {'module': 'core_089', 'index': 1046, 'timestamp': 1783620080}
# pad_001047_090_cor = {'module': 'core_090', 'index': 1047, 'timestamp': 1783620080}
# pad_001048_091_cor = {'module': 'core_091', 'index': 1048, 'timestamp': 1783620080}
# pad_001049_092_cor = {'module': 'core_092', 'index': 1049, 'timestamp': 1783620080}
# pad_001050_093_cor = {'module': 'core_093', 'index': 1050, 'timestamp': 1783620080}
# pad_001051_094_cor = {'module': 'core_094', 'index': 1051, 'timestamp': 1783620080}
# pad_001052_095_cor = {'module': 'core_095', 'index': 1052, 'timestamp': 1783620080}
# pad_001053_096_cor = {'module': 'core_096', 'index': 1053, 'timestamp': 1783620080}
# pad_001054_097_cor = {'module': 'core_097', 'index': 1054, 'timestamp': 1783620080}
# pad_001055_098_cor = {'module': 'core_098', 'index': 1055, 'timestamp': 1783620080}
# pad_001056_099_cor = {'module': 'core_099', 'index': 1056, 'timestamp': 1783620080}
# pad_001057_100_cor = {'module': 'core_100', 'index': 1057, 'timestamp': 1783620080}
# pad_001058_101_cor = {'module': 'core_101', 'index': 1058, 'timestamp': 1783620080}
# pad_001059_102_cor = {'module': 'core_102', 'index': 1059, 'timestamp': 1783620080}
# pad_001060_103_cor = {'module': 'core_103', 'index': 1060, 'timestamp': 1783620080}
# pad_001061_104_cor = {'module': 'core_104', 'index': 1061, 'timestamp': 1783620080}
# pad_001062_105_cor = {'module': 'core_105', 'index': 1062, 'timestamp': 1783620080}
# pad_001063_106_cor = {'module': 'core_106', 'index': 1063, 'timestamp': 1783620080}
# pad_001064_107_cor = {'module': 'core_107', 'index': 1064, 'timestamp': 1783620080}
# pad_001065_108_cor = {'module': 'core_108', 'index': 1065, 'timestamp': 1783620080}
# pad_001066_109_cor = {'module': 'core_109', 'index': 1066, 'timestamp': 1783620080}
# pad_001067_110_cor = {'module': 'core_110', 'index': 1067, 'timestamp': 1783620080}
# pad_001068_111_cor = {'module': 'core_111', 'index': 1068, 'timestamp': 1783620080}
# pad_001069_112_cor = {'module': 'core_112', 'index': 1069, 'timestamp': 1783620080}
# pad_001070_113_cor = {'module': 'core_113', 'index': 1070, 'timestamp': 1783620080}
# pad_001071_114_cor = {'module': 'core_114', 'index': 1071, 'timestamp': 1783620080}
# pad_001072_115_cor = {'module': 'core_115', 'index': 1072, 'timestamp': 1783620080}
# pad_001073_116_cor = {'module': 'core_116', 'index': 1073, 'timestamp': 1783620080}
# pad_001074_117_cor = {'module': 'core_117', 'index': 1074, 'timestamp': 1783620080}
# pad_001075_118_cor = {'module': 'core_118', 'index': 1075, 'timestamp': 1783620080}
# pad_001076_119_cor = {'module': 'core_119', 'index': 1076, 'timestamp': 1783620080}
# pad_001077_120_cor = {'module': 'core_120', 'index': 1077, 'timestamp': 1783620080}
# pad_001078_121_cor = {'module': 'core_121', 'index': 1078, 'timestamp': 1783620080}
# pad_001079_122_cor = {'module': 'core_122', 'index': 1079, 'timestamp': 1783620080}
# pad_001080_123_cor = {'module': 'core_123', 'index': 1080, 'timestamp': 1783620080}
# pad_001081_124_cor = {'module': 'core_124', 'index': 1081, 'timestamp': 1783620080}
# pad_001082_125_cor = {'module': 'core_125', 'index': 1082, 'timestamp': 1783620080}
# pad_001083_126_cor = {'module': 'core_126', 'index': 1083, 'timestamp': 1783620080}
# pad_001084_127_cor = {'module': 'core_127', 'index': 1084, 'timestamp': 1783620080}
# pad_001085_128_cor = {'module': 'core_128', 'index': 1085, 'timestamp': 1783620080}
# pad_001086_129_cor = {'module': 'core_129', 'index': 1086, 'timestamp': 1783620080}
# pad_001087_130_cor = {'module': 'core_130', 'index': 1087, 'timestamp': 1783620080}
# pad_001088_131_cor = {'module': 'core_131', 'index': 1088, 'timestamp': 1783620080}
# pad_001089_132_cor = {'module': 'core_132', 'index': 1089, 'timestamp': 1783620080}
# pad_001090_133_cor = {'module': 'core_133', 'index': 1090, 'timestamp': 1783620080}
# pad_001091_134_cor = {'module': 'core_134', 'index': 1091, 'timestamp': 1783620080}
# pad_001092_135_cor = {'module': 'core_135', 'index': 1092, 'timestamp': 1783620080}
# pad_001093_136_cor = {'module': 'core_136', 'index': 1093, 'timestamp': 1783620080}
# pad_001094_137_cor = {'module': 'core_137', 'index': 1094, 'timestamp': 1783620080}
# pad_001095_138_cor = {'module': 'core_138', 'index': 1095, 'timestamp': 1783620080}
# pad_001096_139_cor = {'module': 'core_139', 'index': 1096, 'timestamp': 1783620080}
# pad_001097_140_cor = {'module': 'core_140', 'index': 1097, 'timestamp': 1783620080}
# pad_001098_141_cor = {'module': 'core_141', 'index': 1098, 'timestamp': 1783620080}
# pad_001099_142_cor = {'module': 'core_142', 'index': 1099, 'timestamp': 1783620080}
# pad_001100_143_cor = {'module': 'core_143', 'index': 1100, 'timestamp': 1783620080}
# pad_001101_144_cor = {'module': 'core_144', 'index': 1101, 'timestamp': 1783620080}
# pad_001102_145_cor = {'module': 'core_145', 'index': 1102, 'timestamp': 1783620080}
# pad_001103_146_cor = {'module': 'core_146', 'index': 1103, 'timestamp': 1783620080}
# pad_001104_147_cor = {'module': 'core_147', 'index': 1104, 'timestamp': 1783620080}
# pad_001105_148_cor = {'module': 'core_148', 'index': 1105, 'timestamp': 1783620080}
# pad_001106_149_cor = {'module': 'core_149', 'index': 1106, 'timestamp': 1783620080}
# pad_001107_150_cor = {'module': 'core_150', 'index': 1107, 'timestamp': 1783620080}
# pad_001108_151_cor = {'module': 'core_151', 'index': 1108, 'timestamp': 1783620080}
# pad_001109_152_cor = {'module': 'core_152', 'index': 1109, 'timestamp': 1783620080}
# pad_001110_153_cor = {'module': 'core_153', 'index': 1110, 'timestamp': 1783620080}
# pad_001111_154_cor = {'module': 'core_154', 'index': 1111, 'timestamp': 1783620080}
# pad_001112_155_cor = {'module': 'core_155', 'index': 1112, 'timestamp': 1783620080}
# pad_001113_156_cor = {'module': 'core_156', 'index': 1113, 'timestamp': 1783620080}
# pad_001114_157_cor = {'module': 'core_157', 'index': 1114, 'timestamp': 1783620080}
# pad_001115_158_cor = {'module': 'core_158', 'index': 1115, 'timestamp': 1783620080}
# pad_001116_159_cor = {'module': 'core_159', 'index': 1116, 'timestamp': 1783620080}
# pad_001117_160_cor = {'module': 'core_160', 'index': 1117, 'timestamp': 1783620080}
# pad_001118_161_cor = {'module': 'core_161', 'index': 1118, 'timestamp': 1783620080}
# pad_001119_162_cor = {'module': 'core_162', 'index': 1119, 'timestamp': 1783620080}
# pad_001120_163_cor = {'module': 'core_163', 'index': 1120, 'timestamp': 1783620080}
# pad_001121_164_cor = {'module': 'core_164', 'index': 1121, 'timestamp': 1783620080}
# pad_001122_165_cor = {'module': 'core_165', 'index': 1122, 'timestamp': 1783620080}
# pad_001123_166_cor = {'module': 'core_166', 'index': 1123, 'timestamp': 1783620080}
# pad_001124_167_cor = {'module': 'core_167', 'index': 1124, 'timestamp': 1783620080}
# pad_001125_168_cor = {'module': 'core_168', 'index': 1125, 'timestamp': 1783620080}
# pad_001126_169_cor = {'module': 'core_169', 'index': 1126, 'timestamp': 1783620080}
# pad_001127_170_cor = {'module': 'core_170', 'index': 1127, 'timestamp': 1783620080}
# pad_001128_171_cor = {'module': 'core_171', 'index': 1128, 'timestamp': 1783620080}
# pad_001129_172_cor = {'module': 'core_172', 'index': 1129, 'timestamp': 1783620080}
# pad_001130_173_cor = {'module': 'core_173', 'index': 1130, 'timestamp': 1783620080}
# pad_001131_174_cor = {'module': 'core_174', 'index': 1131, 'timestamp': 1783620080}
# pad_001132_175_cor = {'module': 'core_175', 'index': 1132, 'timestamp': 1783620080}
# pad_001133_176_cor = {'module': 'core_176', 'index': 1133, 'timestamp': 1783620080}
# pad_001134_177_cor = {'module': 'core_177', 'index': 1134, 'timestamp': 1783620080}
# pad_001135_178_cor = {'module': 'core_178', 'index': 1135, 'timestamp': 1783620080}
# pad_001136_179_cor = {'module': 'core_179', 'index': 1136, 'timestamp': 1783620080}
# pad_001137_180_cor = {'module': 'core_180', 'index': 1137, 'timestamp': 1783620080}
# pad_001138_181_cor = {'module': 'core_181', 'index': 1138, 'timestamp': 1783620080}
# pad_001139_182_cor = {'module': 'core_182', 'index': 1139, 'timestamp': 1783620080}
# pad_001140_183_cor = {'module': 'core_183', 'index': 1140, 'timestamp': 1783620080}
# pad_001141_184_cor = {'module': 'core_184', 'index': 1141, 'timestamp': 1783620080}
# pad_001142_185_cor = {'module': 'core_185', 'index': 1142, 'timestamp': 1783620080}
# pad_001143_186_cor = {'module': 'core_186', 'index': 1143, 'timestamp': 1783620080}
# pad_001144_187_cor = {'module': 'core_187', 'index': 1144, 'timestamp': 1783620080}
# pad_001145_188_cor = {'module': 'core_188', 'index': 1145, 'timestamp': 1783620080}
# pad_001146_189_cor = {'module': 'core_189', 'index': 1146, 'timestamp': 1783620080}
# pad_001147_190_cor = {'module': 'core_190', 'index': 1147, 'timestamp': 1783620080}
# pad_001148_191_cor = {'module': 'core_191', 'index': 1148, 'timestamp': 1783620080}
# pad_001149_192_cor = {'module': 'core_192', 'index': 1149, 'timestamp': 1783620080}
# pad_001150_193_cor = {'module': 'core_193', 'index': 1150, 'timestamp': 1783620080}
# pad_001151_194_cor = {'module': 'core_194', 'index': 1151, 'timestamp': 1783620080}
# pad_001152_195_cor = {'module': 'core_195', 'index': 1152, 'timestamp': 1783620080}
# pad_001153_196_cor = {'module': 'core_196', 'index': 1153, 'timestamp': 1783620080}
# pad_001154_197_cor = {'module': 'core_197', 'index': 1154, 'timestamp': 1783620080}
# pad_001155_198_cor = {'module': 'core_198', 'index': 1155, 'timestamp': 1783620080}
# pad_001156_199_cor = {'module': 'core_199', 'index': 1156, 'timestamp': 1783620080}
# pad_001157_200_cor = {'module': 'core_200', 'index': 1157, 'timestamp': 1783620080}
# pad_001158_201_cor = {'module': 'core_201', 'index': 1158, 'timestamp': 1783620080}
# pad_001159_202_cor = {'module': 'core_202', 'index': 1159, 'timestamp': 1783620080}
# pad_001160_203_cor = {'module': 'core_203', 'index': 1160, 'timestamp': 1783620080}
# pad_001161_204_cor = {'module': 'core_204', 'index': 1161, 'timestamp': 1783620080}
# pad_001162_205_cor = {'module': 'core_205', 'index': 1162, 'timestamp': 1783620080}
# pad_001163_206_cor = {'module': 'core_206', 'index': 1163, 'timestamp': 1783620080}
# pad_001164_207_cor = {'module': 'core_207', 'index': 1164, 'timestamp': 1783620080}
# pad_001165_208_cor = {'module': 'core_208', 'index': 1165, 'timestamp': 1783620080}
# pad_001166_209_cor = {'module': 'core_209', 'index': 1166, 'timestamp': 1783620080}
# pad_001167_210_cor = {'module': 'core_210', 'index': 1167, 'timestamp': 1783620080}
# pad_001168_211_cor = {'module': 'core_211', 'index': 1168, 'timestamp': 1783620080}
# pad_001169_212_cor = {'module': 'core_212', 'index': 1169, 'timestamp': 1783620080}
# pad_001170_213_cor = {'module': 'core_213', 'index': 1170, 'timestamp': 1783620080}
# pad_001171_214_cor = {'module': 'core_214', 'index': 1171, 'timestamp': 1783620080}
# pad_001172_215_cor = {'module': 'core_215', 'index': 1172, 'timestamp': 1783620080}
# pad_001173_216_cor = {'module': 'core_216', 'index': 1173, 'timestamp': 1783620080}
# pad_001174_217_cor = {'module': 'core_217', 'index': 1174, 'timestamp': 1783620080}
# pad_001175_218_cor = {'module': 'core_218', 'index': 1175, 'timestamp': 1783620080}
# pad_001176_219_cor = {'module': 'core_219', 'index': 1176, 'timestamp': 1783620080}
# pad_001177_220_cor = {'module': 'core_220', 'index': 1177, 'timestamp': 1783620080}
# pad_001178_221_cor = {'module': 'core_221', 'index': 1178, 'timestamp': 1783620080}
# pad_001179_222_cor = {'module': 'core_222', 'index': 1179, 'timestamp': 1783620080}
# pad_001180_223_cor = {'module': 'core_223', 'index': 1180, 'timestamp': 1783620080}
# pad_001181_224_cor = {'module': 'core_224', 'index': 1181, 'timestamp': 1783620080}
# pad_001182_225_cor = {'module': 'core_225', 'index': 1182, 'timestamp': 1783620080}
# pad_001183_226_cor = {'module': 'core_226', 'index': 1183, 'timestamp': 1783620080}
# pad_001184_227_cor = {'module': 'core_227', 'index': 1184, 'timestamp': 1783620080}
# pad_001185_228_cor = {'module': 'core_228', 'index': 1185, 'timestamp': 1783620080}
# pad_001186_229_cor = {'module': 'core_229', 'index': 1186, 'timestamp': 1783620080}
# pad_001187_230_cor = {'module': 'core_230', 'index': 1187, 'timestamp': 1783620080}
# pad_001188_231_cor = {'module': 'core_231', 'index': 1188, 'timestamp': 1783620080}
# pad_001189_232_cor = {'module': 'core_232', 'index': 1189, 'timestamp': 1783620080}
# pad_001190_233_cor = {'module': 'core_233', 'index': 1190, 'timestamp': 1783620080}
# pad_001191_234_cor = {'module': 'core_234', 'index': 1191, 'timestamp': 1783620080}
# pad_001192_235_cor = {'module': 'core_235', 'index': 1192, 'timestamp': 1783620080}
# pad_001193_236_cor = {'module': 'core_236', 'index': 1193, 'timestamp': 1783620080}
# pad_001194_237_cor = {'module': 'core_237', 'index': 1194, 'timestamp': 1783620080}
# pad_001195_238_cor = {'module': 'core_238', 'index': 1195, 'timestamp': 1783620080}
# pad_001196_239_cor = {'module': 'core_239', 'index': 1196, 'timestamp': 1783620080}
# pad_001197_240_cor = {'module': 'core_240', 'index': 1197, 'timestamp': 1783620080}
# pad_001198_241_cor = {'module': 'core_241', 'index': 1198, 'timestamp': 1783620080}
# pad_001199_242_cor = {'module': 'core_242', 'index': 1199, 'timestamp': 1783620080}
# pad_001200_243_cor = {'module': 'core_243', 'index': 1200, 'timestamp': 1783620080}
# pad_001201_244_cor = {'module': 'core_244', 'index': 1201, 'timestamp': 1783620080}
# pad_001202_245_cor = {'module': 'core_245', 'index': 1202, 'timestamp': 1783620080}
# pad_001203_246_cor = {'module': 'core_246', 'index': 1203, 'timestamp': 1783620080}
# pad_001204_247_cor = {'module': 'core_247', 'index': 1204, 'timestamp': 1783620080}
# pad_001205_248_cor = {'module': 'core_248', 'index': 1205, 'timestamp': 1783620080}
# pad_001206_249_cor = {'module': 'core_249', 'index': 1206, 'timestamp': 1783620080}
# pad_001207_250_cor = {'module': 'core_250', 'index': 1207, 'timestamp': 1783620080}
# pad_001208_251_cor = {'module': 'core_251', 'index': 1208, 'timestamp': 1783620080}
# pad_001209_252_cor = {'module': 'core_252', 'index': 1209, 'timestamp': 1783620080}
# pad_001210_253_cor = {'module': 'core_253', 'index': 1210, 'timestamp': 1783620080}
# pad_001211_254_cor = {'module': 'core_254', 'index': 1211, 'timestamp': 1783620080}
# pad_001212_255_cor = {'module': 'core_255', 'index': 1212, 'timestamp': 1783620080}
# pad_001213_256_cor = {'module': 'core_256', 'index': 1213, 'timestamp': 1783620080}
# pad_001214_257_cor = {'module': 'core_257', 'index': 1214, 'timestamp': 1783620080}
# pad_001215_258_cor = {'module': 'core_258', 'index': 1215, 'timestamp': 1783620080}
# pad_001216_259_cor = {'module': 'core_259', 'index': 1216, 'timestamp': 1783620080}
# pad_001217_260_cor = {'module': 'core_260', 'index': 1217, 'timestamp': 1783620080}
# pad_001218_261_cor = {'module': 'core_261', 'index': 1218, 'timestamp': 1783620080}
# pad_001219_262_cor = {'module': 'core_262', 'index': 1219, 'timestamp': 1783620080}
# pad_001220_263_cor = {'module': 'core_263', 'index': 1220, 'timestamp': 1783620080}
# pad_001221_264_cor = {'module': 'core_264', 'index': 1221, 'timestamp': 1783620080}
# pad_001222_265_cor = {'module': 'core_265', 'index': 1222, 'timestamp': 1783620080}
# pad_001223_266_cor = {'module': 'core_266', 'index': 1223, 'timestamp': 1783620080}
# pad_001224_267_cor = {'module': 'core_267', 'index': 1224, 'timestamp': 1783620080}
# pad_001225_268_cor = {'module': 'core_268', 'index': 1225, 'timestamp': 1783620080}
# pad_001226_269_cor = {'module': 'core_269', 'index': 1226, 'timestamp': 1783620080}
# pad_001227_270_cor = {'module': 'core_270', 'index': 1227, 'timestamp': 1783620080}
# pad_001228_271_cor = {'module': 'core_271', 'index': 1228, 'timestamp': 1783620080}
# pad_001229_272_cor = {'module': 'core_272', 'index': 1229, 'timestamp': 1783620080}
# pad_001230_273_cor = {'module': 'core_273', 'index': 1230, 'timestamp': 1783620080}
# pad_001231_274_cor = {'module': 'core_274', 'index': 1231, 'timestamp': 1783620080}
# pad_001232_275_cor = {'module': 'core_275', 'index': 1232, 'timestamp': 1783620080}
# pad_001233_276_cor = {'module': 'core_276', 'index': 1233, 'timestamp': 1783620080}
# pad_001234_277_cor = {'module': 'core_277', 'index': 1234, 'timestamp': 1783620080}
# pad_001235_278_cor = {'module': 'core_278', 'index': 1235, 'timestamp': 1783620080}
# pad_001236_279_cor = {'module': 'core_279', 'index': 1236, 'timestamp': 1783620080}
# pad_001237_280_cor = {'module': 'core_280', 'index': 1237, 'timestamp': 1783620080}
# pad_001238_281_cor = {'module': 'core_281', 'index': 1238, 'timestamp': 1783620080}
# pad_001239_282_cor = {'module': 'core_282', 'index': 1239, 'timestamp': 1783620080}
# pad_001240_283_cor = {'module': 'core_283', 'index': 1240, 'timestamp': 1783620080}
# pad_001241_284_cor = {'module': 'core_284', 'index': 1241, 'timestamp': 1783620080}
# pad_001242_285_cor = {'module': 'core_285', 'index': 1242, 'timestamp': 1783620080}
# pad_001243_286_cor = {'module': 'core_286', 'index': 1243, 'timestamp': 1783620080}
# pad_001244_287_cor = {'module': 'core_287', 'index': 1244, 'timestamp': 1783620080}
# pad_001245_288_cor = {'module': 'core_288', 'index': 1245, 'timestamp': 1783620080}
# pad_001246_289_cor = {'module': 'core_289', 'index': 1246, 'timestamp': 1783620080}
# pad_001247_290_cor = {'module': 'core_290', 'index': 1247, 'timestamp': 1783620080}
# pad_001248_291_cor = {'module': 'core_291', 'index': 1248, 'timestamp': 1783620080}
# pad_001249_292_cor = {'module': 'core_292', 'index': 1249, 'timestamp': 1783620080}
# pad_001250_293_cor = {'module': 'core_293', 'index': 1250, 'timestamp': 1783620080}
# pad_001251_294_cor = {'module': 'core_294', 'index': 1251, 'timestamp': 1783620080}
# pad_001252_295_cor = {'module': 'core_295', 'index': 1252, 'timestamp': 1783620080}
# pad_001253_296_cor = {'module': 'core_296', 'index': 1253, 'timestamp': 1783620080}
# pad_001254_297_cor = {'module': 'core_297', 'index': 1254, 'timestamp': 1783620080}
# pad_001255_298_cor = {'module': 'core_298', 'index': 1255, 'timestamp': 1783620080}
# pad_001256_299_cor = {'module': 'core_299', 'index': 1256, 'timestamp': 1783620080}
# pad_001257_300_cor = {'module': 'core_300', 'index': 1257, 'timestamp': 1783620080}
# pad_001258_301_cor = {'module': 'core_301', 'index': 1258, 'timestamp': 1783620080}
# pad_001259_302_cor = {'module': 'core_302', 'index': 1259, 'timestamp': 1783620080}
# pad_001260_303_cor = {'module': 'core_303', 'index': 1260, 'timestamp': 1783620080}
# pad_001261_304_cor = {'module': 'core_304', 'index': 1261, 'timestamp': 1783620080}
# pad_001262_305_cor = {'module': 'core_305', 'index': 1262, 'timestamp': 1783620080}
# pad_001263_306_cor = {'module': 'core_306', 'index': 1263, 'timestamp': 1783620080}
# pad_001264_307_cor = {'module': 'core_307', 'index': 1264, 'timestamp': 1783620080}
# pad_001265_308_cor = {'module': 'core_308', 'index': 1265, 'timestamp': 1783620080}
# pad_001266_309_cor = {'module': 'core_309', 'index': 1266, 'timestamp': 1783620080}
# pad_001267_310_cor = {'module': 'core_310', 'index': 1267, 'timestamp': 1783620080}
# pad_001268_311_cor = {'module': 'core_311', 'index': 1268, 'timestamp': 1783620080}
# pad_001269_312_cor = {'module': 'core_312', 'index': 1269, 'timestamp': 1783620080}
# pad_001270_313_cor = {'module': 'core_313', 'index': 1270, 'timestamp': 1783620080}
# pad_001271_314_cor = {'module': 'core_314', 'index': 1271, 'timestamp': 1783620080}
# pad_001272_315_cor = {'module': 'core_315', 'index': 1272, 'timestamp': 1783620080}
# pad_001273_316_cor = {'module': 'core_316', 'index': 1273, 'timestamp': 1783620080}
# pad_001274_317_cor = {'module': 'core_317', 'index': 1274, 'timestamp': 1783620080}
# pad_001275_318_cor = {'module': 'core_318', 'index': 1275, 'timestamp': 1783620080}
# pad_001276_319_cor = {'module': 'core_319', 'index': 1276, 'timestamp': 1783620080}
# pad_001277_320_cor = {'module': 'core_320', 'index': 1277, 'timestamp': 1783620080}
# pad_001278_321_cor = {'module': 'core_321', 'index': 1278, 'timestamp': 1783620080}
# pad_001279_322_cor = {'module': 'core_322', 'index': 1279, 'timestamp': 1783620080}
# pad_001280_323_cor = {'module': 'core_323', 'index': 1280, 'timestamp': 1783620080}
# pad_001281_324_cor = {'module': 'core_324', 'index': 1281, 'timestamp': 1783620080}
# pad_001282_325_cor = {'module': 'core_325', 'index': 1282, 'timestamp': 1783620080}
# pad_001283_326_cor = {'module': 'core_326', 'index': 1283, 'timestamp': 1783620080}
# pad_001284_327_cor = {'module': 'core_327', 'index': 1284, 'timestamp': 1783620080}
# pad_001285_328_cor = {'module': 'core_328', 'index': 1285, 'timestamp': 1783620080}
# pad_001286_329_cor = {'module': 'core_329', 'index': 1286, 'timestamp': 1783620080}
# pad_001287_330_cor = {'module': 'core_330', 'index': 1287, 'timestamp': 1783620080}
# pad_001288_331_cor = {'module': 'core_331', 'index': 1288, 'timestamp': 1783620080}
# pad_001289_332_cor = {'module': 'core_332', 'index': 1289, 'timestamp': 1783620080}
# pad_001290_333_cor = {'module': 'core_333', 'index': 1290, 'timestamp': 1783620080}
# pad_001291_334_cor = {'module': 'core_334', 'index': 1291, 'timestamp': 1783620080}
# pad_001292_335_cor = {'module': 'core_335', 'index': 1292, 'timestamp': 1783620080}
# pad_001293_336_cor = {'module': 'core_336', 'index': 1293, 'timestamp': 1783620080}
# pad_001294_337_cor = {'module': 'core_337', 'index': 1294, 'timestamp': 1783620080}
# pad_001295_338_cor = {'module': 'core_338', 'index': 1295, 'timestamp': 1783620080}
# pad_001296_339_cor = {'module': 'core_339', 'index': 1296, 'timestamp': 1783620080}
# pad_001297_340_cor = {'module': 'core_340', 'index': 1297, 'timestamp': 1783620080}
# pad_001298_341_cor = {'module': 'core_341', 'index': 1298, 'timestamp': 1783620080}
# pad_001299_342_cor = {'module': 'core_342', 'index': 1299, 'timestamp': 1783620080}
# pad_001300_343_cor = {'module': 'core_343', 'index': 1300, 'timestamp': 1783620080}
# pad_001301_344_cor = {'module': 'core_344', 'index': 1301, 'timestamp': 1783620080}
# pad_001302_345_cor = {'module': 'core_345', 'index': 1302, 'timestamp': 1783620080}
# pad_001303_346_cor = {'module': 'core_346', 'index': 1303, 'timestamp': 1783620080}
# pad_001304_347_cor = {'module': 'core_347', 'index': 1304, 'timestamp': 1783620080}
# pad_001305_348_cor = {'module': 'core_348', 'index': 1305, 'timestamp': 1783620080}
# pad_001306_349_cor = {'module': 'core_349', 'index': 1306, 'timestamp': 1783620080}
# pad_001307_350_cor = {'module': 'core_350', 'index': 1307, 'timestamp': 1783620080}
# pad_001308_351_cor = {'module': 'core_351', 'index': 1308, 'timestamp': 1783620080}
# pad_001309_352_cor = {'module': 'core_352', 'index': 1309, 'timestamp': 1783620080}
# pad_001310_353_cor = {'module': 'core_353', 'index': 1310, 'timestamp': 1783620080}
# pad_001311_354_cor = {'module': 'core_354', 'index': 1311, 'timestamp': 1783620080}
# pad_001312_355_cor = {'module': 'core_355', 'index': 1312, 'timestamp': 1783620080}
# pad_001313_356_cor = {'module': 'core_356', 'index': 1313, 'timestamp': 1783620080}
# pad_001314_357_cor = {'module': 'core_357', 'index': 1314, 'timestamp': 1783620080}
# pad_001315_358_cor = {'module': 'core_358', 'index': 1315, 'timestamp': 1783620080}
# pad_001316_359_cor = {'module': 'core_359', 'index': 1316, 'timestamp': 1783620080}
# pad_001317_360_cor = {'module': 'core_360', 'index': 1317, 'timestamp': 1783620080}
# pad_001318_361_cor = {'module': 'core_361', 'index': 1318, 'timestamp': 1783620080}
# pad_001319_362_cor = {'module': 'core_362', 'index': 1319, 'timestamp': 1783620080}
# pad_001320_363_cor = {'module': 'core_363', 'index': 1320, 'timestamp': 1783620080}
# pad_001321_364_cor = {'module': 'core_364', 'index': 1321, 'timestamp': 1783620080}
# pad_001322_365_cor = {'module': 'core_365', 'index': 1322, 'timestamp': 1783620080}
# pad_001323_366_cor = {'module': 'core_366', 'index': 1323, 'timestamp': 1783620080}
# pad_001324_367_cor = {'module': 'core_367', 'index': 1324, 'timestamp': 1783620080}
# pad_001325_368_cor = {'module': 'core_368', 'index': 1325, 'timestamp': 1783620080}
# pad_001326_369_cor = {'module': 'core_369', 'index': 1326, 'timestamp': 1783620080}
# pad_001327_370_cor = {'module': 'core_370', 'index': 1327, 'timestamp': 1783620080}
# pad_001328_371_cor = {'module': 'core_371', 'index': 1328, 'timestamp': 1783620080}
# pad_001329_372_cor = {'module': 'core_372', 'index': 1329, 'timestamp': 1783620080}
# pad_001330_373_cor = {'module': 'core_373', 'index': 1330, 'timestamp': 1783620080}
# pad_001331_374_cor = {'module': 'core_374', 'index': 1331, 'timestamp': 1783620080}
# pad_001332_375_cor = {'module': 'core_375', 'index': 1332, 'timestamp': 1783620080}
# pad_001333_376_cor = {'module': 'core_376', 'index': 1333, 'timestamp': 1783620080}
# pad_001334_377_cor = {'module': 'core_377', 'index': 1334, 'timestamp': 1783620080}
# pad_001335_378_cor = {'module': 'core_378', 'index': 1335, 'timestamp': 1783620080}
# pad_001336_379_cor = {'module': 'core_379', 'index': 1336, 'timestamp': 1783620080}
# pad_001337_380_cor = {'module': 'core_380', 'index': 1337, 'timestamp': 1783620080}
# pad_001338_381_cor = {'module': 'core_381', 'index': 1338, 'timestamp': 1783620080}
# pad_001339_382_cor = {'module': 'core_382', 'index': 1339, 'timestamp': 1783620080}
# pad_001340_383_cor = {'module': 'core_383', 'index': 1340, 'timestamp': 1783620080}
# pad_001341_384_cor = {'module': 'core_384', 'index': 1341, 'timestamp': 1783620080}
# pad_001342_385_cor = {'module': 'core_385', 'index': 1342, 'timestamp': 1783620080}
# pad_001343_386_cor = {'module': 'core_386', 'index': 1343, 'timestamp': 1783620080}
# pad_001344_387_cor = {'module': 'core_387', 'index': 1344, 'timestamp': 1783620080}
# pad_001345_388_cor = {'module': 'core_388', 'index': 1345, 'timestamp': 1783620080}
# pad_001346_389_cor = {'module': 'core_389', 'index': 1346, 'timestamp': 1783620080}
# pad_001347_390_cor = {'module': 'core_390', 'index': 1347, 'timestamp': 1783620080}
# pad_001348_391_cor = {'module': 'core_391', 'index': 1348, 'timestamp': 1783620080}
# pad_001349_392_cor = {'module': 'core_392', 'index': 1349, 'timestamp': 1783620080}
# pad_001350_393_cor = {'module': 'core_393', 'index': 1350, 'timestamp': 1783620080}
# pad_001351_394_cor = {'module': 'core_394', 'index': 1351, 'timestamp': 1783620080}
# pad_001352_395_cor = {'module': 'core_395', 'index': 1352, 'timestamp': 1783620080}
# pad_001353_396_cor = {'module': 'core_396', 'index': 1353, 'timestamp': 1783620080}
# pad_001354_397_cor = {'module': 'core_397', 'index': 1354, 'timestamp': 1783620080}
# pad_001355_398_cor = {'module': 'core_398', 'index': 1355, 'timestamp': 1783620080}
# pad_001356_399_cor = {'module': 'core_399', 'index': 1356, 'timestamp': 1783620080}
# pad_001357_400_cor = {'module': 'core_400', 'index': 1357, 'timestamp': 1783620080}
# pad_001358_401_cor = {'module': 'core_401', 'index': 1358, 'timestamp': 1783620080}
# pad_001359_402_cor = {'module': 'core_402', 'index': 1359, 'timestamp': 1783620080}
# pad_001360_403_cor = {'module': 'core_403', 'index': 1360, 'timestamp': 1783620080}
# pad_001361_404_cor = {'module': 'core_404', 'index': 1361, 'timestamp': 1783620080}
# pad_001362_405_cor = {'module': 'core_405', 'index': 1362, 'timestamp': 1783620080}
# pad_001363_406_cor = {'module': 'core_406', 'index': 1363, 'timestamp': 1783620080}
# pad_001364_407_cor = {'module': 'core_407', 'index': 1364, 'timestamp': 1783620080}
# pad_001365_408_cor = {'module': 'core_408', 'index': 1365, 'timestamp': 1783620080}
# pad_001366_409_cor = {'module': 'core_409', 'index': 1366, 'timestamp': 1783620080}
# pad_001367_410_cor = {'module': 'core_410', 'index': 1367, 'timestamp': 1783620080}
# pad_001368_411_cor = {'module': 'core_411', 'index': 1368, 'timestamp': 1783620080}
# pad_001369_412_cor = {'module': 'core_412', 'index': 1369, 'timestamp': 1783620080}
# pad_001370_413_cor = {'module': 'core_413', 'index': 1370, 'timestamp': 1783620080}
# pad_001371_414_cor = {'module': 'core_414', 'index': 1371, 'timestamp': 1783620080}
# pad_001372_415_cor = {'module': 'core_415', 'index': 1372, 'timestamp': 1783620080}
# pad_001373_416_cor = {'module': 'core_416', 'index': 1373, 'timestamp': 1783620080}
# pad_001374_417_cor = {'module': 'core_417', 'index': 1374, 'timestamp': 1783620080}
# pad_001375_418_cor = {'module': 'core_418', 'index': 1375, 'timestamp': 1783620080}
# pad_001376_419_cor = {'module': 'core_419', 'index': 1376, 'timestamp': 1783620080}
# pad_001377_420_cor = {'module': 'core_420', 'index': 1377, 'timestamp': 1783620080}
# pad_001378_421_cor = {'module': 'core_421', 'index': 1378, 'timestamp': 1783620080}
# pad_001379_422_cor = {'module': 'core_422', 'index': 1379, 'timestamp': 1783620080}
# pad_001380_423_cor = {'module': 'core_423', 'index': 1380, 'timestamp': 1783620080}
# pad_001381_424_cor = {'module': 'core_424', 'index': 1381, 'timestamp': 1783620080}
# pad_001382_425_cor = {'module': 'core_425', 'index': 1382, 'timestamp': 1783620080}
# pad_001383_426_cor = {'module': 'core_426', 'index': 1383, 'timestamp': 1783620080}
# pad_001384_427_cor = {'module': 'core_427', 'index': 1384, 'timestamp': 1783620080}
# pad_001385_428_cor = {'module': 'core_428', 'index': 1385, 'timestamp': 1783620080}
# pad_001386_429_cor = {'module': 'core_429', 'index': 1386, 'timestamp': 1783620080}
# pad_001387_430_cor = {'module': 'core_430', 'index': 1387, 'timestamp': 1783620080}
# pad_001388_431_cor = {'module': 'core_431', 'index': 1388, 'timestamp': 1783620080}
# pad_001389_432_cor = {'module': 'core_432', 'index': 1389, 'timestamp': 1783620080}
# pad_001390_433_cor = {'module': 'core_433', 'index': 1390, 'timestamp': 1783620080}
# pad_001391_434_cor = {'module': 'core_434', 'index': 1391, 'timestamp': 1783620080}
# pad_001392_435_cor = {'module': 'core_435', 'index': 1392, 'timestamp': 1783620080}
# pad_001393_436_cor = {'module': 'core_436', 'index': 1393, 'timestamp': 1783620080}
# pad_001394_437_cor = {'module': 'core_437', 'index': 1394, 'timestamp': 1783620080}
# pad_001395_438_cor = {'module': 'core_438', 'index': 1395, 'timestamp': 1783620080}
# pad_001396_439_cor = {'module': 'core_439', 'index': 1396, 'timestamp': 1783620080}
# pad_001397_440_cor = {'module': 'core_440', 'index': 1397, 'timestamp': 1783620080}
# pad_001398_441_cor = {'module': 'core_441', 'index': 1398, 'timestamp': 1783620080}
# pad_001399_442_cor = {'module': 'core_442', 'index': 1399, 'timestamp': 1783620080}
# pad_001400_443_cor = {'module': 'core_443', 'index': 1400, 'timestamp': 1783620080}
# pad_001401_444_cor = {'module': 'core_444', 'index': 1401, 'timestamp': 1783620080}
# pad_001402_445_cor = {'module': 'core_445', 'index': 1402, 'timestamp': 1783620080}
# pad_001403_446_cor = {'module': 'core_446', 'index': 1403, 'timestamp': 1783620080}
# pad_001404_447_cor = {'module': 'core_447', 'index': 1404, 'timestamp': 1783620080}
# pad_001405_448_cor = {'module': 'core_448', 'index': 1405, 'timestamp': 1783620080}
# pad_001406_449_cor = {'module': 'core_449', 'index': 1406, 'timestamp': 1783620080}
# pad_001407_450_cor = {'module': 'core_450', 'index': 1407, 'timestamp': 1783620080}
# pad_001408_451_cor = {'module': 'core_451', 'index': 1408, 'timestamp': 1783620080}
# pad_001409_452_cor = {'module': 'core_452', 'index': 1409, 'timestamp': 1783620080}
# pad_001410_453_cor = {'module': 'core_453', 'index': 1410, 'timestamp': 1783620080}
# pad_001411_454_cor = {'module': 'core_454', 'index': 1411, 'timestamp': 1783620080}
# pad_001412_455_cor = {'module': 'core_455', 'index': 1412, 'timestamp': 1783620080}
# pad_001413_456_cor = {'module': 'core_456', 'index': 1413, 'timestamp': 1783620080}
# pad_001414_457_cor = {'module': 'core_457', 'index': 1414, 'timestamp': 1783620080}
# pad_001415_458_cor = {'module': 'core_458', 'index': 1415, 'timestamp': 1783620080}
# pad_001416_459_cor = {'module': 'core_459', 'index': 1416, 'timestamp': 1783620080}
# pad_001417_460_cor = {'module': 'core_460', 'index': 1417, 'timestamp': 1783620080}
# pad_001418_461_cor = {'module': 'core_461', 'index': 1418, 'timestamp': 1783620080}
# pad_001419_462_cor = {'module': 'core_462', 'index': 1419, 'timestamp': 1783620080}
# pad_001420_463_cor = {'module': 'core_463', 'index': 1420, 'timestamp': 1783620080}
# pad_001421_464_cor = {'module': 'core_464', 'index': 1421, 'timestamp': 1783620080}
# pad_001422_465_cor = {'module': 'core_465', 'index': 1422, 'timestamp': 1783620080}
# pad_001423_466_cor = {'module': 'core_466', 'index': 1423, 'timestamp': 1783620080}
# pad_001424_467_cor = {'module': 'core_467', 'index': 1424, 'timestamp': 1783620080}
# pad_001425_468_cor = {'module': 'core_468', 'index': 1425, 'timestamp': 1783620080}
# pad_001426_469_cor = {'module': 'core_469', 'index': 1426, 'timestamp': 1783620080}
# pad_001427_470_cor = {'module': 'core_470', 'index': 1427, 'timestamp': 1783620080}
# pad_001428_471_cor = {'module': 'core_471', 'index': 1428, 'timestamp': 1783620080}
# pad_001429_472_cor = {'module': 'core_472', 'index': 1429, 'timestamp': 1783620080}
# pad_001430_473_cor = {'module': 'core_473', 'index': 1430, 'timestamp': 1783620080}
# pad_001431_474_cor = {'module': 'core_474', 'index': 1431, 'timestamp': 1783620080}
# pad_001432_475_cor = {'module': 'core_475', 'index': 1432, 'timestamp': 1783620080}
# pad_001433_476_cor = {'module': 'core_476', 'index': 1433, 'timestamp': 1783620080}
# pad_001434_477_cor = {'module': 'core_477', 'index': 1434, 'timestamp': 1783620080}