"""
core_module_002.py - legacy core #2
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C2_0=42
T2_0="t0_2"
F2_0=True
C2_1=49
T2_1="t1_2"
F2_1=False
C2_2=56
T2_2="t2_2"
F2_2=True
C2_3=63
T2_3="t3_2"
F2_3=False
C2_4=70
T2_4="t4_2"
F2_4=True
C2_5=77
T2_5="t5_2"
F2_5=False
C2_6=84
T2_6="t6_2"
F2_6=True
C2_7=91
T2_7="t7_2"
F2_7=False
C2_8=98
T2_8="t8_2"
F2_8=True
C2_9=105
T2_9="t9_2"
F2_9=False
C2_10=112
T2_10="t10_2"
F2_10=True
C2_11=119
T2_11="t11_2"
F2_11=False
C2_12=126
T2_12="t12_2"
F2_12=True
C2_13=133
T2_13="t13_2"
F2_13=False
C2_14=140
T2_14="t14_2"
F2_14=True

def proc_cor_002_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_002_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":2}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*2+j+fi)%500
    r.append(v*2+C2_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":2}
def hlp_proc_cor_002_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR002000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR002000._lk:LegCOR002000._c+=1;self._i=LegCOR002000._c
  self.n=nm or f"LegCOR002000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*2+j+ci)%50
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

class LegCOR002001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR002001._lk:LegCOR002001._c+=1;self._i=LegCOR002001._c
  self.n=nm or f"LegCOR002001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*2+j+ci)%50
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

class LegCOR002002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR002002._lk:LegCOR002002._c+=1;self._i=LegCOR002002._c
  self.n=nm or f"LegCOR002002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*2+j+ci)%50
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

class LegCOR002003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR002003._lk:LegCOR002003._c+=1;self._i=LegCOR002003._c
  self.n=nm or f"LegCOR002003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*2+j+ci)%50
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

def val_cor_002_0000(d,s=None,st=True):
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

def val_cor_002_0001(d,s=None,st=True):
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

def val_cor_002_0002(d,s=None,st=True):
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

def val_cor_002_0003(d,s=None,st=True):
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

def val_cor_002_0004(d,s=None,st=True):
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

def val_cor_002_0005(d,s=None,st=True):
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

M002={
 "id":2,"d":"core","n":"core_module_002","v":"4.7"
}# pad_000479_000_cor = {'module': 'core_000', 'index': 479, 'timestamp': 1783620080}
# pad_000480_001_cor = {'module': 'core_001', 'index': 480, 'timestamp': 1783620080}
# pad_000481_002_cor = {'module': 'core_002', 'index': 481, 'timestamp': 1783620080}
# pad_000482_003_cor = {'module': 'core_003', 'index': 482, 'timestamp': 1783620080}
# pad_000483_004_cor = {'module': 'core_004', 'index': 483, 'timestamp': 1783620080}
# pad_000484_005_cor = {'module': 'core_005', 'index': 484, 'timestamp': 1783620080}
# pad_000485_006_cor = {'module': 'core_006', 'index': 485, 'timestamp': 1783620080}
# pad_000486_007_cor = {'module': 'core_007', 'index': 486, 'timestamp': 1783620080}
# pad_000487_008_cor = {'module': 'core_008', 'index': 487, 'timestamp': 1783620080}
# pad_000488_009_cor = {'module': 'core_009', 'index': 488, 'timestamp': 1783620080}
# pad_000489_010_cor = {'module': 'core_010', 'index': 489, 'timestamp': 1783620080}
# pad_000490_011_cor = {'module': 'core_011', 'index': 490, 'timestamp': 1783620080}
# pad_000491_012_cor = {'module': 'core_012', 'index': 491, 'timestamp': 1783620080}
# pad_000492_013_cor = {'module': 'core_013', 'index': 492, 'timestamp': 1783620080}
# pad_000493_014_cor = {'module': 'core_014', 'index': 493, 'timestamp': 1783620080}
# pad_000494_015_cor = {'module': 'core_015', 'index': 494, 'timestamp': 1783620080}
# pad_000495_016_cor = {'module': 'core_016', 'index': 495, 'timestamp': 1783620080}
# pad_000496_017_cor = {'module': 'core_017', 'index': 496, 'timestamp': 1783620080}
# pad_000497_018_cor = {'module': 'core_018', 'index': 497, 'timestamp': 1783620080}
# pad_000498_019_cor = {'module': 'core_019', 'index': 498, 'timestamp': 1783620080}
# pad_000499_020_cor = {'module': 'core_020', 'index': 499, 'timestamp': 1783620080}
# pad_000500_021_cor = {'module': 'core_021', 'index': 500, 'timestamp': 1783620080}
# pad_000501_022_cor = {'module': 'core_022', 'index': 501, 'timestamp': 1783620080}
# pad_000502_023_cor = {'module': 'core_023', 'index': 502, 'timestamp': 1783620080}
# pad_000503_024_cor = {'module': 'core_024', 'index': 503, 'timestamp': 1783620080}
# pad_000504_025_cor = {'module': 'core_025', 'index': 504, 'timestamp': 1783620080}
# pad_000505_026_cor = {'module': 'core_026', 'index': 505, 'timestamp': 1783620080}
# pad_000506_027_cor = {'module': 'core_027', 'index': 506, 'timestamp': 1783620080}
# pad_000507_028_cor = {'module': 'core_028', 'index': 507, 'timestamp': 1783620080}
# pad_000508_029_cor = {'module': 'core_029', 'index': 508, 'timestamp': 1783620080}
# pad_000509_030_cor = {'module': 'core_030', 'index': 509, 'timestamp': 1783620080}
# pad_000510_031_cor = {'module': 'core_031', 'index': 510, 'timestamp': 1783620080}
# pad_000511_032_cor = {'module': 'core_032', 'index': 511, 'timestamp': 1783620080}
# pad_000512_033_cor = {'module': 'core_033', 'index': 512, 'timestamp': 1783620080}
# pad_000513_034_cor = {'module': 'core_034', 'index': 513, 'timestamp': 1783620080}
# pad_000514_035_cor = {'module': 'core_035', 'index': 514, 'timestamp': 1783620080}
# pad_000515_036_cor = {'module': 'core_036', 'index': 515, 'timestamp': 1783620080}
# pad_000516_037_cor = {'module': 'core_037', 'index': 516, 'timestamp': 1783620080}
# pad_000517_038_cor = {'module': 'core_038', 'index': 517, 'timestamp': 1783620080}
# pad_000518_039_cor = {'module': 'core_039', 'index': 518, 'timestamp': 1783620080}
# pad_000519_040_cor = {'module': 'core_040', 'index': 519, 'timestamp': 1783620080}
# pad_000520_041_cor = {'module': 'core_041', 'index': 520, 'timestamp': 1783620080}
# pad_000521_042_cor = {'module': 'core_042', 'index': 521, 'timestamp': 1783620080}
# pad_000522_043_cor = {'module': 'core_043', 'index': 522, 'timestamp': 1783620080}
# pad_000523_044_cor = {'module': 'core_044', 'index': 523, 'timestamp': 1783620080}
# pad_000524_045_cor = {'module': 'core_045', 'index': 524, 'timestamp': 1783620080}
# pad_000525_046_cor = {'module': 'core_046', 'index': 525, 'timestamp': 1783620080}
# pad_000526_047_cor = {'module': 'core_047', 'index': 526, 'timestamp': 1783620080}
# pad_000527_048_cor = {'module': 'core_048', 'index': 527, 'timestamp': 1783620080}
# pad_000528_049_cor = {'module': 'core_049', 'index': 528, 'timestamp': 1783620080}
# pad_000529_050_cor = {'module': 'core_050', 'index': 529, 'timestamp': 1783620080}
# pad_000530_051_cor = {'module': 'core_051', 'index': 530, 'timestamp': 1783620080}
# pad_000531_052_cor = {'module': 'core_052', 'index': 531, 'timestamp': 1783620080}
# pad_000532_053_cor = {'module': 'core_053', 'index': 532, 'timestamp': 1783620080}
# pad_000533_054_cor = {'module': 'core_054', 'index': 533, 'timestamp': 1783620080}
# pad_000534_055_cor = {'module': 'core_055', 'index': 534, 'timestamp': 1783620080}
# pad_000535_056_cor = {'module': 'core_056', 'index': 535, 'timestamp': 1783620080}
# pad_000536_057_cor = {'module': 'core_057', 'index': 536, 'timestamp': 1783620080}
# pad_000537_058_cor = {'module': 'core_058', 'index': 537, 'timestamp': 1783620080}
# pad_000538_059_cor = {'module': 'core_059', 'index': 538, 'timestamp': 1783620080}
# pad_000539_060_cor = {'module': 'core_060', 'index': 539, 'timestamp': 1783620080}
# pad_000540_061_cor = {'module': 'core_061', 'index': 540, 'timestamp': 1783620080}
# pad_000541_062_cor = {'module': 'core_062', 'index': 541, 'timestamp': 1783620080}
# pad_000542_063_cor = {'module': 'core_063', 'index': 542, 'timestamp': 1783620080}
# pad_000543_064_cor = {'module': 'core_064', 'index': 543, 'timestamp': 1783620080}
# pad_000544_065_cor = {'module': 'core_065', 'index': 544, 'timestamp': 1783620080}
# pad_000545_066_cor = {'module': 'core_066', 'index': 545, 'timestamp': 1783620080}
# pad_000546_067_cor = {'module': 'core_067', 'index': 546, 'timestamp': 1783620080}
# pad_000547_068_cor = {'module': 'core_068', 'index': 547, 'timestamp': 1783620080}
# pad_000548_069_cor = {'module': 'core_069', 'index': 548, 'timestamp': 1783620080}
# pad_000549_070_cor = {'module': 'core_070', 'index': 549, 'timestamp': 1783620080}
# pad_000550_071_cor = {'module': 'core_071', 'index': 550, 'timestamp': 1783620080}
# pad_000551_072_cor = {'module': 'core_072', 'index': 551, 'timestamp': 1783620080}
# pad_000552_073_cor = {'module': 'core_073', 'index': 552, 'timestamp': 1783620080}
# pad_000553_074_cor = {'module': 'core_074', 'index': 553, 'timestamp': 1783620080}
# pad_000554_075_cor = {'module': 'core_075', 'index': 554, 'timestamp': 1783620080}
# pad_000555_076_cor = {'module': 'core_076', 'index': 555, 'timestamp': 1783620080}
# pad_000556_077_cor = {'module': 'core_077', 'index': 556, 'timestamp': 1783620080}
# pad_000557_078_cor = {'module': 'core_078', 'index': 557, 'timestamp': 1783620080}
# pad_000558_079_cor = {'module': 'core_079', 'index': 558, 'timestamp': 1783620080}
# pad_000559_080_cor = {'module': 'core_080', 'index': 559, 'timestamp': 1783620080}
# pad_000560_081_cor = {'module': 'core_081', 'index': 560, 'timestamp': 1783620080}
# pad_000561_082_cor = {'module': 'core_082', 'index': 561, 'timestamp': 1783620080}
# pad_000562_083_cor = {'module': 'core_083', 'index': 562, 'timestamp': 1783620080}
# pad_000563_084_cor = {'module': 'core_084', 'index': 563, 'timestamp': 1783620080}
# pad_000564_085_cor = {'module': 'core_085', 'index': 564, 'timestamp': 1783620080}
# pad_000565_086_cor = {'module': 'core_086', 'index': 565, 'timestamp': 1783620080}
# pad_000566_087_cor = {'module': 'core_087', 'index': 566, 'timestamp': 1783620080}
# pad_000567_088_cor = {'module': 'core_088', 'index': 567, 'timestamp': 1783620080}
# pad_000568_089_cor = {'module': 'core_089', 'index': 568, 'timestamp': 1783620080}
# pad_000569_090_cor = {'module': 'core_090', 'index': 569, 'timestamp': 1783620080}
# pad_000570_091_cor = {'module': 'core_091', 'index': 570, 'timestamp': 1783620080}
# pad_000571_092_cor = {'module': 'core_092', 'index': 571, 'timestamp': 1783620080}
# pad_000572_093_cor = {'module': 'core_093', 'index': 572, 'timestamp': 1783620080}
# pad_000573_094_cor = {'module': 'core_094', 'index': 573, 'timestamp': 1783620080}
# pad_000574_095_cor = {'module': 'core_095', 'index': 574, 'timestamp': 1783620080}
# pad_000575_096_cor = {'module': 'core_096', 'index': 575, 'timestamp': 1783620080}
# pad_000576_097_cor = {'module': 'core_097', 'index': 576, 'timestamp': 1783620080}
# pad_000577_098_cor = {'module': 'core_098', 'index': 577, 'timestamp': 1783620080}
# pad_000578_099_cor = {'module': 'core_099', 'index': 578, 'timestamp': 1783620080}
# pad_000579_100_cor = {'module': 'core_100', 'index': 579, 'timestamp': 1783620080}
# pad_000580_101_cor = {'module': 'core_101', 'index': 580, 'timestamp': 1783620080}
# pad_000581_102_cor = {'module': 'core_102', 'index': 581, 'timestamp': 1783620080}
# pad_000582_103_cor = {'module': 'core_103', 'index': 582, 'timestamp': 1783620080}
# pad_000583_104_cor = {'module': 'core_104', 'index': 583, 'timestamp': 1783620080}
# pad_000584_105_cor = {'module': 'core_105', 'index': 584, 'timestamp': 1783620080}
# pad_000585_106_cor = {'module': 'core_106', 'index': 585, 'timestamp': 1783620080}
# pad_000586_107_cor = {'module': 'core_107', 'index': 586, 'timestamp': 1783620080}
# pad_000587_108_cor = {'module': 'core_108', 'index': 587, 'timestamp': 1783620080}
# pad_000588_109_cor = {'module': 'core_109', 'index': 588, 'timestamp': 1783620080}
# pad_000589_110_cor = {'module': 'core_110', 'index': 589, 'timestamp': 1783620080}
# pad_000590_111_cor = {'module': 'core_111', 'index': 590, 'timestamp': 1783620080}
# pad_000591_112_cor = {'module': 'core_112', 'index': 591, 'timestamp': 1783620080}
# pad_000592_113_cor = {'module': 'core_113', 'index': 592, 'timestamp': 1783620080}
# pad_000593_114_cor = {'module': 'core_114', 'index': 593, 'timestamp': 1783620080}
# pad_000594_115_cor = {'module': 'core_115', 'index': 594, 'timestamp': 1783620080}
# pad_000595_116_cor = {'module': 'core_116', 'index': 595, 'timestamp': 1783620080}
# pad_000596_117_cor = {'module': 'core_117', 'index': 596, 'timestamp': 1783620080}
# pad_000597_118_cor = {'module': 'core_118', 'index': 597, 'timestamp': 1783620080}
# pad_000598_119_cor = {'module': 'core_119', 'index': 598, 'timestamp': 1783620080}
# pad_000599_120_cor = {'module': 'core_120', 'index': 599, 'timestamp': 1783620080}
# pad_000600_121_cor = {'module': 'core_121', 'index': 600, 'timestamp': 1783620080}
# pad_000601_122_cor = {'module': 'core_122', 'index': 601, 'timestamp': 1783620080}
# pad_000602_123_cor = {'module': 'core_123', 'index': 602, 'timestamp': 1783620080}
# pad_000603_124_cor = {'module': 'core_124', 'index': 603, 'timestamp': 1783620080}
# pad_000604_125_cor = {'module': 'core_125', 'index': 604, 'timestamp': 1783620080}
# pad_000605_126_cor = {'module': 'core_126', 'index': 605, 'timestamp': 1783620080}
# pad_000606_127_cor = {'module': 'core_127', 'index': 606, 'timestamp': 1783620080}
# pad_000607_128_cor = {'module': 'core_128', 'index': 607, 'timestamp': 1783620080}
# pad_000608_129_cor = {'module': 'core_129', 'index': 608, 'timestamp': 1783620080}
# pad_000609_130_cor = {'module': 'core_130', 'index': 609, 'timestamp': 1783620080}
# pad_000610_131_cor = {'module': 'core_131', 'index': 610, 'timestamp': 1783620080}
# pad_000611_132_cor = {'module': 'core_132', 'index': 611, 'timestamp': 1783620080}
# pad_000612_133_cor = {'module': 'core_133', 'index': 612, 'timestamp': 1783620080}
# pad_000613_134_cor = {'module': 'core_134', 'index': 613, 'timestamp': 1783620080}
# pad_000614_135_cor = {'module': 'core_135', 'index': 614, 'timestamp': 1783620080}
# pad_000615_136_cor = {'module': 'core_136', 'index': 615, 'timestamp': 1783620080}
# pad_000616_137_cor = {'module': 'core_137', 'index': 616, 'timestamp': 1783620080}
# pad_000617_138_cor = {'module': 'core_138', 'index': 617, 'timestamp': 1783620080}
# pad_000618_139_cor = {'module': 'core_139', 'index': 618, 'timestamp': 1783620080}
# pad_000619_140_cor = {'module': 'core_140', 'index': 619, 'timestamp': 1783620080}
# pad_000620_141_cor = {'module': 'core_141', 'index': 620, 'timestamp': 1783620080}
# pad_000621_142_cor = {'module': 'core_142', 'index': 621, 'timestamp': 1783620080}
# pad_000622_143_cor = {'module': 'core_143', 'index': 622, 'timestamp': 1783620080}
# pad_000623_144_cor = {'module': 'core_144', 'index': 623, 'timestamp': 1783620080}
# pad_000624_145_cor = {'module': 'core_145', 'index': 624, 'timestamp': 1783620080}
# pad_000625_146_cor = {'module': 'core_146', 'index': 625, 'timestamp': 1783620080}
# pad_000626_147_cor = {'module': 'core_147', 'index': 626, 'timestamp': 1783620080}
# pad_000627_148_cor = {'module': 'core_148', 'index': 627, 'timestamp': 1783620080}
# pad_000628_149_cor = {'module': 'core_149', 'index': 628, 'timestamp': 1783620080}
# pad_000629_150_cor = {'module': 'core_150', 'index': 629, 'timestamp': 1783620080}
# pad_000630_151_cor = {'module': 'core_151', 'index': 630, 'timestamp': 1783620080}
# pad_000631_152_cor = {'module': 'core_152', 'index': 631, 'timestamp': 1783620080}
# pad_000632_153_cor = {'module': 'core_153', 'index': 632, 'timestamp': 1783620080}
# pad_000633_154_cor = {'module': 'core_154', 'index': 633, 'timestamp': 1783620080}
# pad_000634_155_cor = {'module': 'core_155', 'index': 634, 'timestamp': 1783620080}
# pad_000635_156_cor = {'module': 'core_156', 'index': 635, 'timestamp': 1783620080}
# pad_000636_157_cor = {'module': 'core_157', 'index': 636, 'timestamp': 1783620080}
# pad_000637_158_cor = {'module': 'core_158', 'index': 637, 'timestamp': 1783620080}
# pad_000638_159_cor = {'module': 'core_159', 'index': 638, 'timestamp': 1783620080}
# pad_000639_160_cor = {'module': 'core_160', 'index': 639, 'timestamp': 1783620080}
# pad_000640_161_cor = {'module': 'core_161', 'index': 640, 'timestamp': 1783620080}
# pad_000641_162_cor = {'module': 'core_162', 'index': 641, 'timestamp': 1783620080}
# pad_000642_163_cor = {'module': 'core_163', 'index': 642, 'timestamp': 1783620080}
# pad_000643_164_cor = {'module': 'core_164', 'index': 643, 'timestamp': 1783620080}
# pad_000644_165_cor = {'module': 'core_165', 'index': 644, 'timestamp': 1783620080}
# pad_000645_166_cor = {'module': 'core_166', 'index': 645, 'timestamp': 1783620080}
# pad_000646_167_cor = {'module': 'core_167', 'index': 646, 'timestamp': 1783620080}
# pad_000647_168_cor = {'module': 'core_168', 'index': 647, 'timestamp': 1783620080}
# pad_000648_169_cor = {'module': 'core_169', 'index': 648, 'timestamp': 1783620080}
# pad_000649_170_cor = {'module': 'core_170', 'index': 649, 'timestamp': 1783620080}
# pad_000650_171_cor = {'module': 'core_171', 'index': 650, 'timestamp': 1783620080}
# pad_000651_172_cor = {'module': 'core_172', 'index': 651, 'timestamp': 1783620080}
# pad_000652_173_cor = {'module': 'core_173', 'index': 652, 'timestamp': 1783620080}
# pad_000653_174_cor = {'module': 'core_174', 'index': 653, 'timestamp': 1783620080}
# pad_000654_175_cor = {'module': 'core_175', 'index': 654, 'timestamp': 1783620080}
# pad_000655_176_cor = {'module': 'core_176', 'index': 655, 'timestamp': 1783620080}
# pad_000656_177_cor = {'module': 'core_177', 'index': 656, 'timestamp': 1783620080}
# pad_000657_178_cor = {'module': 'core_178', 'index': 657, 'timestamp': 1783620080}
# pad_000658_179_cor = {'module': 'core_179', 'index': 658, 'timestamp': 1783620080}
# pad_000659_180_cor = {'module': 'core_180', 'index': 659, 'timestamp': 1783620080}
# pad_000660_181_cor = {'module': 'core_181', 'index': 660, 'timestamp': 1783620080}
# pad_000661_182_cor = {'module': 'core_182', 'index': 661, 'timestamp': 1783620080}
# pad_000662_183_cor = {'module': 'core_183', 'index': 662, 'timestamp': 1783620080}
# pad_000663_184_cor = {'module': 'core_184', 'index': 663, 'timestamp': 1783620080}
# pad_000664_185_cor = {'module': 'core_185', 'index': 664, 'timestamp': 1783620080}
# pad_000665_186_cor = {'module': 'core_186', 'index': 665, 'timestamp': 1783620080}
# pad_000666_187_cor = {'module': 'core_187', 'index': 666, 'timestamp': 1783620080}
# pad_000667_188_cor = {'module': 'core_188', 'index': 667, 'timestamp': 1783620080}
# pad_000668_189_cor = {'module': 'core_189', 'index': 668, 'timestamp': 1783620080}
# pad_000669_190_cor = {'module': 'core_190', 'index': 669, 'timestamp': 1783620080}
# pad_000670_191_cor = {'module': 'core_191', 'index': 670, 'timestamp': 1783620080}
# pad_000671_192_cor = {'module': 'core_192', 'index': 671, 'timestamp': 1783620080}
# pad_000672_193_cor = {'module': 'core_193', 'index': 672, 'timestamp': 1783620080}
# pad_000673_194_cor = {'module': 'core_194', 'index': 673, 'timestamp': 1783620080}
# pad_000674_195_cor = {'module': 'core_195', 'index': 674, 'timestamp': 1783620080}
# pad_000675_196_cor = {'module': 'core_196', 'index': 675, 'timestamp': 1783620080}
# pad_000676_197_cor = {'module': 'core_197', 'index': 676, 'timestamp': 1783620080}
# pad_000677_198_cor = {'module': 'core_198', 'index': 677, 'timestamp': 1783620080}
# pad_000678_199_cor = {'module': 'core_199', 'index': 678, 'timestamp': 1783620080}
# pad_000679_200_cor = {'module': 'core_200', 'index': 679, 'timestamp': 1783620080}
# pad_000680_201_cor = {'module': 'core_201', 'index': 680, 'timestamp': 1783620080}
# pad_000681_202_cor = {'module': 'core_202', 'index': 681, 'timestamp': 1783620080}
# pad_000682_203_cor = {'module': 'core_203', 'index': 682, 'timestamp': 1783620080}
# pad_000683_204_cor = {'module': 'core_204', 'index': 683, 'timestamp': 1783620080}
# pad_000684_205_cor = {'module': 'core_205', 'index': 684, 'timestamp': 1783620080}
# pad_000685_206_cor = {'module': 'core_206', 'index': 685, 'timestamp': 1783620080}
# pad_000686_207_cor = {'module': 'core_207', 'index': 686, 'timestamp': 1783620080}
# pad_000687_208_cor = {'module': 'core_208', 'index': 687, 'timestamp': 1783620080}
# pad_000688_209_cor = {'module': 'core_209', 'index': 688, 'timestamp': 1783620080}
# pad_000689_210_cor = {'module': 'core_210', 'index': 689, 'timestamp': 1783620080}
# pad_000690_211_cor = {'module': 'core_211', 'index': 690, 'timestamp': 1783620080}
# pad_000691_212_cor = {'module': 'core_212', 'index': 691, 'timestamp': 1783620080}
# pad_000692_213_cor = {'module': 'core_213', 'index': 692, 'timestamp': 1783620080}
# pad_000693_214_cor = {'module': 'core_214', 'index': 693, 'timestamp': 1783620080}
# pad_000694_215_cor = {'module': 'core_215', 'index': 694, 'timestamp': 1783620080}
# pad_000695_216_cor = {'module': 'core_216', 'index': 695, 'timestamp': 1783620080}
# pad_000696_217_cor = {'module': 'core_217', 'index': 696, 'timestamp': 1783620080}
# pad_000697_218_cor = {'module': 'core_218', 'index': 697, 'timestamp': 1783620080}
# pad_000698_219_cor = {'module': 'core_219', 'index': 698, 'timestamp': 1783620080}
# pad_000699_220_cor = {'module': 'core_220', 'index': 699, 'timestamp': 1783620080}
# pad_000700_221_cor = {'module': 'core_221', 'index': 700, 'timestamp': 1783620080}
# pad_000701_222_cor = {'module': 'core_222', 'index': 701, 'timestamp': 1783620080}
# pad_000702_223_cor = {'module': 'core_223', 'index': 702, 'timestamp': 1783620080}
# pad_000703_224_cor = {'module': 'core_224', 'index': 703, 'timestamp': 1783620080}
# pad_000704_225_cor = {'module': 'core_225', 'index': 704, 'timestamp': 1783620080}
# pad_000705_226_cor = {'module': 'core_226', 'index': 705, 'timestamp': 1783620080}
# pad_000706_227_cor = {'module': 'core_227', 'index': 706, 'timestamp': 1783620080}
# pad_000707_228_cor = {'module': 'core_228', 'index': 707, 'timestamp': 1783620080}
# pad_000708_229_cor = {'module': 'core_229', 'index': 708, 'timestamp': 1783620080}
# pad_000709_230_cor = {'module': 'core_230', 'index': 709, 'timestamp': 1783620080}
# pad_000710_231_cor = {'module': 'core_231', 'index': 710, 'timestamp': 1783620080}
# pad_000711_232_cor = {'module': 'core_232', 'index': 711, 'timestamp': 1783620080}
# pad_000712_233_cor = {'module': 'core_233', 'index': 712, 'timestamp': 1783620080}
# pad_000713_234_cor = {'module': 'core_234', 'index': 713, 'timestamp': 1783620080}
# pad_000714_235_cor = {'module': 'core_235', 'index': 714, 'timestamp': 1783620080}
# pad_000715_236_cor = {'module': 'core_236', 'index': 715, 'timestamp': 1783620080}
# pad_000716_237_cor = {'module': 'core_237', 'index': 716, 'timestamp': 1783620080}
# pad_000717_238_cor = {'module': 'core_238', 'index': 717, 'timestamp': 1783620080}
# pad_000718_239_cor = {'module': 'core_239', 'index': 718, 'timestamp': 1783620080}
# pad_000719_240_cor = {'module': 'core_240', 'index': 719, 'timestamp': 1783620080}
# pad_000720_241_cor = {'module': 'core_241', 'index': 720, 'timestamp': 1783620080}
# pad_000721_242_cor = {'module': 'core_242', 'index': 721, 'timestamp': 1783620080}
# pad_000722_243_cor = {'module': 'core_243', 'index': 722, 'timestamp': 1783620080}
# pad_000723_244_cor = {'module': 'core_244', 'index': 723, 'timestamp': 1783620080}
# pad_000724_245_cor = {'module': 'core_245', 'index': 724, 'timestamp': 1783620080}
# pad_000725_246_cor = {'module': 'core_246', 'index': 725, 'timestamp': 1783620080}
# pad_000726_247_cor = {'module': 'core_247', 'index': 726, 'timestamp': 1783620080}
# pad_000727_248_cor = {'module': 'core_248', 'index': 727, 'timestamp': 1783620080}
# pad_000728_249_cor = {'module': 'core_249', 'index': 728, 'timestamp': 1783620080}
# pad_000729_250_cor = {'module': 'core_250', 'index': 729, 'timestamp': 1783620080}
# pad_000730_251_cor = {'module': 'core_251', 'index': 730, 'timestamp': 1783620080}
# pad_000731_252_cor = {'module': 'core_252', 'index': 731, 'timestamp': 1783620080}
# pad_000732_253_cor = {'module': 'core_253', 'index': 732, 'timestamp': 1783620080}
# pad_000733_254_cor = {'module': 'core_254', 'index': 733, 'timestamp': 1783620080}
# pad_000734_255_cor = {'module': 'core_255', 'index': 734, 'timestamp': 1783620080}
# pad_000735_256_cor = {'module': 'core_256', 'index': 735, 'timestamp': 1783620080}
# pad_000736_257_cor = {'module': 'core_257', 'index': 736, 'timestamp': 1783620080}
# pad_000737_258_cor = {'module': 'core_258', 'index': 737, 'timestamp': 1783620080}
# pad_000738_259_cor = {'module': 'core_259', 'index': 738, 'timestamp': 1783620080}
# pad_000739_260_cor = {'module': 'core_260', 'index': 739, 'timestamp': 1783620080}
# pad_000740_261_cor = {'module': 'core_261', 'index': 740, 'timestamp': 1783620080}
# pad_000741_262_cor = {'module': 'core_262', 'index': 741, 'timestamp': 1783620080}
# pad_000742_263_cor = {'module': 'core_263', 'index': 742, 'timestamp': 1783620080}
# pad_000743_264_cor = {'module': 'core_264', 'index': 743, 'timestamp': 1783620080}
# pad_000744_265_cor = {'module': 'core_265', 'index': 744, 'timestamp': 1783620080}
# pad_000745_266_cor = {'module': 'core_266', 'index': 745, 'timestamp': 1783620080}
# pad_000746_267_cor = {'module': 'core_267', 'index': 746, 'timestamp': 1783620080}
# pad_000747_268_cor = {'module': 'core_268', 'index': 747, 'timestamp': 1783620080}
# pad_000748_269_cor = {'module': 'core_269', 'index': 748, 'timestamp': 1783620080}
# pad_000749_270_cor = {'module': 'core_270', 'index': 749, 'timestamp': 1783620080}
# pad_000750_271_cor = {'module': 'core_271', 'index': 750, 'timestamp': 1783620080}
# pad_000751_272_cor = {'module': 'core_272', 'index': 751, 'timestamp': 1783620080}
# pad_000752_273_cor = {'module': 'core_273', 'index': 752, 'timestamp': 1783620080}
# pad_000753_274_cor = {'module': 'core_274', 'index': 753, 'timestamp': 1783620080}
# pad_000754_275_cor = {'module': 'core_275', 'index': 754, 'timestamp': 1783620080}
# pad_000755_276_cor = {'module': 'core_276', 'index': 755, 'timestamp': 1783620080}
# pad_000756_277_cor = {'module': 'core_277', 'index': 756, 'timestamp': 1783620080}
# pad_000757_278_cor = {'module': 'core_278', 'index': 757, 'timestamp': 1783620080}
# pad_000758_279_cor = {'module': 'core_279', 'index': 758, 'timestamp': 1783620080}
# pad_000759_280_cor = {'module': 'core_280', 'index': 759, 'timestamp': 1783620080}
# pad_000760_281_cor = {'module': 'core_281', 'index': 760, 'timestamp': 1783620080}
# pad_000761_282_cor = {'module': 'core_282', 'index': 761, 'timestamp': 1783620080}
# pad_000762_283_cor = {'module': 'core_283', 'index': 762, 'timestamp': 1783620080}
# pad_000763_284_cor = {'module': 'core_284', 'index': 763, 'timestamp': 1783620080}
# pad_000764_285_cor = {'module': 'core_285', 'index': 764, 'timestamp': 1783620080}
# pad_000765_286_cor = {'module': 'core_286', 'index': 765, 'timestamp': 1783620080}
# pad_000766_287_cor = {'module': 'core_287', 'index': 766, 'timestamp': 1783620080}
# pad_000767_288_cor = {'module': 'core_288', 'index': 767, 'timestamp': 1783620080}
# pad_000768_289_cor = {'module': 'core_289', 'index': 768, 'timestamp': 1783620080}
# pad_000769_290_cor = {'module': 'core_290', 'index': 769, 'timestamp': 1783620080}
# pad_000770_291_cor = {'module': 'core_291', 'index': 770, 'timestamp': 1783620080}
# pad_000771_292_cor = {'module': 'core_292', 'index': 771, 'timestamp': 1783620080}
# pad_000772_293_cor = {'module': 'core_293', 'index': 772, 'timestamp': 1783620080}
# pad_000773_294_cor = {'module': 'core_294', 'index': 773, 'timestamp': 1783620080}
# pad_000774_295_cor = {'module': 'core_295', 'index': 774, 'timestamp': 1783620080}
# pad_000775_296_cor = {'module': 'core_296', 'index': 775, 'timestamp': 1783620080}
# pad_000776_297_cor = {'module': 'core_297', 'index': 776, 'timestamp': 1783620080}
# pad_000777_298_cor = {'module': 'core_298', 'index': 777, 'timestamp': 1783620080}
# pad_000778_299_cor = {'module': 'core_299', 'index': 778, 'timestamp': 1783620080}
# pad_000779_300_cor = {'module': 'core_300', 'index': 779, 'timestamp': 1783620080}
# pad_000780_301_cor = {'module': 'core_301', 'index': 780, 'timestamp': 1783620080}
# pad_000781_302_cor = {'module': 'core_302', 'index': 781, 'timestamp': 1783620080}
# pad_000782_303_cor = {'module': 'core_303', 'index': 782, 'timestamp': 1783620080}
# pad_000783_304_cor = {'module': 'core_304', 'index': 783, 'timestamp': 1783620080}
# pad_000784_305_cor = {'module': 'core_305', 'index': 784, 'timestamp': 1783620080}
# pad_000785_306_cor = {'module': 'core_306', 'index': 785, 'timestamp': 1783620080}
# pad_000786_307_cor = {'module': 'core_307', 'index': 786, 'timestamp': 1783620080}
# pad_000787_308_cor = {'module': 'core_308', 'index': 787, 'timestamp': 1783620080}
# pad_000788_309_cor = {'module': 'core_309', 'index': 788, 'timestamp': 1783620080}
# pad_000789_310_cor = {'module': 'core_310', 'index': 789, 'timestamp': 1783620080}
# pad_000790_311_cor = {'module': 'core_311', 'index': 790, 'timestamp': 1783620080}
# pad_000791_312_cor = {'module': 'core_312', 'index': 791, 'timestamp': 1783620080}
# pad_000792_313_cor = {'module': 'core_313', 'index': 792, 'timestamp': 1783620080}
# pad_000793_314_cor = {'module': 'core_314', 'index': 793, 'timestamp': 1783620080}
# pad_000794_315_cor = {'module': 'core_315', 'index': 794, 'timestamp': 1783620080}
# pad_000795_316_cor = {'module': 'core_316', 'index': 795, 'timestamp': 1783620080}
# pad_000796_317_cor = {'module': 'core_317', 'index': 796, 'timestamp': 1783620080}
# pad_000797_318_cor = {'module': 'core_318', 'index': 797, 'timestamp': 1783620080}
# pad_000798_319_cor = {'module': 'core_319', 'index': 798, 'timestamp': 1783620080}
# pad_000799_320_cor = {'module': 'core_320', 'index': 799, 'timestamp': 1783620080}
# pad_000800_321_cor = {'module': 'core_321', 'index': 800, 'timestamp': 1783620080}
# pad_000801_322_cor = {'module': 'core_322', 'index': 801, 'timestamp': 1783620080}
# pad_000802_323_cor = {'module': 'core_323', 'index': 802, 'timestamp': 1783620080}
# pad_000803_324_cor = {'module': 'core_324', 'index': 803, 'timestamp': 1783620080}
# pad_000804_325_cor = {'module': 'core_325', 'index': 804, 'timestamp': 1783620080}
# pad_000805_326_cor = {'module': 'core_326', 'index': 805, 'timestamp': 1783620080}
# pad_000806_327_cor = {'module': 'core_327', 'index': 806, 'timestamp': 1783620080}
# pad_000807_328_cor = {'module': 'core_328', 'index': 807, 'timestamp': 1783620080}
# pad_000808_329_cor = {'module': 'core_329', 'index': 808, 'timestamp': 1783620080}
# pad_000809_330_cor = {'module': 'core_330', 'index': 809, 'timestamp': 1783620080}
# pad_000810_331_cor = {'module': 'core_331', 'index': 810, 'timestamp': 1783620080}
# pad_000811_332_cor = {'module': 'core_332', 'index': 811, 'timestamp': 1783620080}
# pad_000812_333_cor = {'module': 'core_333', 'index': 812, 'timestamp': 1783620080}
# pad_000813_334_cor = {'module': 'core_334', 'index': 813, 'timestamp': 1783620080}
# pad_000814_335_cor = {'module': 'core_335', 'index': 814, 'timestamp': 1783620080}
# pad_000815_336_cor = {'module': 'core_336', 'index': 815, 'timestamp': 1783620080}
# pad_000816_337_cor = {'module': 'core_337', 'index': 816, 'timestamp': 1783620080}
# pad_000817_338_cor = {'module': 'core_338', 'index': 817, 'timestamp': 1783620080}
# pad_000818_339_cor = {'module': 'core_339', 'index': 818, 'timestamp': 1783620080}
# pad_000819_340_cor = {'module': 'core_340', 'index': 819, 'timestamp': 1783620080}
# pad_000820_341_cor = {'module': 'core_341', 'index': 820, 'timestamp': 1783620080}
# pad_000821_342_cor = {'module': 'core_342', 'index': 821, 'timestamp': 1783620080}
# pad_000822_343_cor = {'module': 'core_343', 'index': 822, 'timestamp': 1783620080}
# pad_000823_344_cor = {'module': 'core_344', 'index': 823, 'timestamp': 1783620080}
# pad_000824_345_cor = {'module': 'core_345', 'index': 824, 'timestamp': 1783620080}
# pad_000825_346_cor = {'module': 'core_346', 'index': 825, 'timestamp': 1783620080}
# pad_000826_347_cor = {'module': 'core_347', 'index': 826, 'timestamp': 1783620080}
# pad_000827_348_cor = {'module': 'core_348', 'index': 827, 'timestamp': 1783620080}
# pad_000828_349_cor = {'module': 'core_349', 'index': 828, 'timestamp': 1783620080}
# pad_000829_350_cor = {'module': 'core_350', 'index': 829, 'timestamp': 1783620080}
# pad_000830_351_cor = {'module': 'core_351', 'index': 830, 'timestamp': 1783620080}
# pad_000831_352_cor = {'module': 'core_352', 'index': 831, 'timestamp': 1783620080}
# pad_000832_353_cor = {'module': 'core_353', 'index': 832, 'timestamp': 1783620080}
# pad_000833_354_cor = {'module': 'core_354', 'index': 833, 'timestamp': 1783620080}
# pad_000834_355_cor = {'module': 'core_355', 'index': 834, 'timestamp': 1783620080}
# pad_000835_356_cor = {'module': 'core_356', 'index': 835, 'timestamp': 1783620080}
# pad_000836_357_cor = {'module': 'core_357', 'index': 836, 'timestamp': 1783620080}
# pad_000837_358_cor = {'module': 'core_358', 'index': 837, 'timestamp': 1783620080}
# pad_000838_359_cor = {'module': 'core_359', 'index': 838, 'timestamp': 1783620080}
# pad_000839_360_cor = {'module': 'core_360', 'index': 839, 'timestamp': 1783620080}
# pad_000840_361_cor = {'module': 'core_361', 'index': 840, 'timestamp': 1783620080}
# pad_000841_362_cor = {'module': 'core_362', 'index': 841, 'timestamp': 1783620080}
# pad_000842_363_cor = {'module': 'core_363', 'index': 842, 'timestamp': 1783620080}
# pad_000843_364_cor = {'module': 'core_364', 'index': 843, 'timestamp': 1783620080}
# pad_000844_365_cor = {'module': 'core_365', 'index': 844, 'timestamp': 1783620080}
# pad_000845_366_cor = {'module': 'core_366', 'index': 845, 'timestamp': 1783620080}
# pad_000846_367_cor = {'module': 'core_367', 'index': 846, 'timestamp': 1783620080}
# pad_000847_368_cor = {'module': 'core_368', 'index': 847, 'timestamp': 1783620080}
# pad_000848_369_cor = {'module': 'core_369', 'index': 848, 'timestamp': 1783620080}
# pad_000849_370_cor = {'module': 'core_370', 'index': 849, 'timestamp': 1783620080}
# pad_000850_371_cor = {'module': 'core_371', 'index': 850, 'timestamp': 1783620080}
# pad_000851_372_cor = {'module': 'core_372', 'index': 851, 'timestamp': 1783620080}
# pad_000852_373_cor = {'module': 'core_373', 'index': 852, 'timestamp': 1783620080}
# pad_000853_374_cor = {'module': 'core_374', 'index': 853, 'timestamp': 1783620080}
# pad_000854_375_cor = {'module': 'core_375', 'index': 854, 'timestamp': 1783620080}
# pad_000855_376_cor = {'module': 'core_376', 'index': 855, 'timestamp': 1783620080}
# pad_000856_377_cor = {'module': 'core_377', 'index': 856, 'timestamp': 1783620080}
# pad_000857_378_cor = {'module': 'core_378', 'index': 857, 'timestamp': 1783620080}
# pad_000858_379_cor = {'module': 'core_379', 'index': 858, 'timestamp': 1783620080}
# pad_000859_380_cor = {'module': 'core_380', 'index': 859, 'timestamp': 1783620080}
# pad_000860_381_cor = {'module': 'core_381', 'index': 860, 'timestamp': 1783620080}
# pad_000861_382_cor = {'module': 'core_382', 'index': 861, 'timestamp': 1783620080}
# pad_000862_383_cor = {'module': 'core_383', 'index': 862, 'timestamp': 1783620080}
# pad_000863_384_cor = {'module': 'core_384', 'index': 863, 'timestamp': 1783620080}
# pad_000864_385_cor = {'module': 'core_385', 'index': 864, 'timestamp': 1783620080}
# pad_000865_386_cor = {'module': 'core_386', 'index': 865, 'timestamp': 1783620080}
# pad_000866_387_cor = {'module': 'core_387', 'index': 866, 'timestamp': 1783620080}
# pad_000867_388_cor = {'module': 'core_388', 'index': 867, 'timestamp': 1783620080}
# pad_000868_389_cor = {'module': 'core_389', 'index': 868, 'timestamp': 1783620080}
# pad_000869_390_cor = {'module': 'core_390', 'index': 869, 'timestamp': 1783620080}
# pad_000870_391_cor = {'module': 'core_391', 'index': 870, 'timestamp': 1783620080}
# pad_000871_392_cor = {'module': 'core_392', 'index': 871, 'timestamp': 1783620080}
# pad_000872_393_cor = {'module': 'core_393', 'index': 872, 'timestamp': 1783620080}
# pad_000873_394_cor = {'module': 'core_394', 'index': 873, 'timestamp': 1783620080}
# pad_000874_395_cor = {'module': 'core_395', 'index': 874, 'timestamp': 1783620080}
# pad_000875_396_cor = {'module': 'core_396', 'index': 875, 'timestamp': 1783620080}
# pad_000876_397_cor = {'module': 'core_397', 'index': 876, 'timestamp': 1783620080}
# pad_000877_398_cor = {'module': 'core_398', 'index': 877, 'timestamp': 1783620080}
# pad_000878_399_cor = {'module': 'core_399', 'index': 878, 'timestamp': 1783620080}
# pad_000879_400_cor = {'module': 'core_400', 'index': 879, 'timestamp': 1783620080}
# pad_000880_401_cor = {'module': 'core_401', 'index': 880, 'timestamp': 1783620080}
# pad_000881_402_cor = {'module': 'core_402', 'index': 881, 'timestamp': 1783620080}
# pad_000882_403_cor = {'module': 'core_403', 'index': 882, 'timestamp': 1783620080}
# pad_000883_404_cor = {'module': 'core_404', 'index': 883, 'timestamp': 1783620080}
# pad_000884_405_cor = {'module': 'core_405', 'index': 884, 'timestamp': 1783620080}
# pad_000885_406_cor = {'module': 'core_406', 'index': 885, 'timestamp': 1783620080}
# pad_000886_407_cor = {'module': 'core_407', 'index': 886, 'timestamp': 1783620080}
# pad_000887_408_cor = {'module': 'core_408', 'index': 887, 'timestamp': 1783620080}
# pad_000888_409_cor = {'module': 'core_409', 'index': 888, 'timestamp': 1783620080}
# pad_000889_410_cor = {'module': 'core_410', 'index': 889, 'timestamp': 1783620080}
# pad_000890_411_cor = {'module': 'core_411', 'index': 890, 'timestamp': 1783620080}
# pad_000891_412_cor = {'module': 'core_412', 'index': 891, 'timestamp': 1783620080}
# pad_000892_413_cor = {'module': 'core_413', 'index': 892, 'timestamp': 1783620080}
# pad_000893_414_cor = {'module': 'core_414', 'index': 893, 'timestamp': 1783620080}
# pad_000894_415_cor = {'module': 'core_415', 'index': 894, 'timestamp': 1783620080}
# pad_000895_416_cor = {'module': 'core_416', 'index': 895, 'timestamp': 1783620080}
# pad_000896_417_cor = {'module': 'core_417', 'index': 896, 'timestamp': 1783620080}
# pad_000897_418_cor = {'module': 'core_418', 'index': 897, 'timestamp': 1783620080}
# pad_000898_419_cor = {'module': 'core_419', 'index': 898, 'timestamp': 1783620080}
# pad_000899_420_cor = {'module': 'core_420', 'index': 899, 'timestamp': 1783620080}
# pad_000900_421_cor = {'module': 'core_421', 'index': 900, 'timestamp': 1783620080}
# pad_000901_422_cor = {'module': 'core_422', 'index': 901, 'timestamp': 1783620080}
# pad_000902_423_cor = {'module': 'core_423', 'index': 902, 'timestamp': 1783620080}
# pad_000903_424_cor = {'module': 'core_424', 'index': 903, 'timestamp': 1783620080}
# pad_000904_425_cor = {'module': 'core_425', 'index': 904, 'timestamp': 1783620080}
# pad_000905_426_cor = {'module': 'core_426', 'index': 905, 'timestamp': 1783620080}
# pad_000906_427_cor = {'module': 'core_427', 'index': 906, 'timestamp': 1783620080}
# pad_000907_428_cor = {'module': 'core_428', 'index': 907, 'timestamp': 1783620080}
# pad_000908_429_cor = {'module': 'core_429', 'index': 908, 'timestamp': 1783620080}
# pad_000909_430_cor = {'module': 'core_430', 'index': 909, 'timestamp': 1783620080}
# pad_000910_431_cor = {'module': 'core_431', 'index': 910, 'timestamp': 1783620080}
# pad_000911_432_cor = {'module': 'core_432', 'index': 911, 'timestamp': 1783620080}
# pad_000912_433_cor = {'module': 'core_433', 'index': 912, 'timestamp': 1783620080}
# pad_000913_434_cor = {'module': 'core_434', 'index': 913, 'timestamp': 1783620080}
# pad_000914_435_cor = {'module': 'core_435', 'index': 914, 'timestamp': 1783620080}
# pad_000915_436_cor = {'module': 'core_436', 'index': 915, 'timestamp': 1783620080}
# pad_000916_437_cor = {'module': 'core_437', 'index': 916, 'timestamp': 1783620080}
# pad_000917_438_cor = {'module': 'core_438', 'index': 917, 'timestamp': 1783620080}
# pad_000918_439_cor = {'module': 'core_439', 'index': 918, 'timestamp': 1783620080}
# pad_000919_440_cor = {'module': 'core_440', 'index': 919, 'timestamp': 1783620080}
# pad_000920_441_cor = {'module': 'core_441', 'index': 920, 'timestamp': 1783620080}
# pad_000921_442_cor = {'module': 'core_442', 'index': 921, 'timestamp': 1783620080}
# pad_000922_443_cor = {'module': 'core_443', 'index': 922, 'timestamp': 1783620080}
# pad_000923_444_cor = {'module': 'core_444', 'index': 923, 'timestamp': 1783620080}
# pad_000924_445_cor = {'module': 'core_445', 'index': 924, 'timestamp': 1783620080}
# pad_000925_446_cor = {'module': 'core_446', 'index': 925, 'timestamp': 1783620080}
# pad_000926_447_cor = {'module': 'core_447', 'index': 926, 'timestamp': 1783620080}
# pad_000927_448_cor = {'module': 'core_448', 'index': 927, 'timestamp': 1783620080}
# pad_000928_449_cor = {'module': 'core_449', 'index': 928, 'timestamp': 1783620080}
# pad_000929_450_cor = {'module': 'core_450', 'index': 929, 'timestamp': 1783620080}
# pad_000930_451_cor = {'module': 'core_451', 'index': 930, 'timestamp': 1783620080}
# pad_000931_452_cor = {'module': 'core_452', 'index': 931, 'timestamp': 1783620080}
# pad_000932_453_cor = {'module': 'core_453', 'index': 932, 'timestamp': 1783620080}
# pad_000933_454_cor = {'module': 'core_454', 'index': 933, 'timestamp': 1783620080}
# pad_000934_455_cor = {'module': 'core_455', 'index': 934, 'timestamp': 1783620080}
# pad_000935_456_cor = {'module': 'core_456', 'index': 935, 'timestamp': 1783620080}
# pad_000936_457_cor = {'module': 'core_457', 'index': 936, 'timestamp': 1783620080}
# pad_000937_458_cor = {'module': 'core_458', 'index': 937, 'timestamp': 1783620080}
# pad_000938_459_cor = {'module': 'core_459', 'index': 938, 'timestamp': 1783620080}
# pad_000939_460_cor = {'module': 'core_460', 'index': 939, 'timestamp': 1783620080}
# pad_000940_461_cor = {'module': 'core_461', 'index': 940, 'timestamp': 1783620080}
# pad_000941_462_cor = {'module': 'core_462', 'index': 941, 'timestamp': 1783620080}
# pad_000942_463_cor = {'module': 'core_463', 'index': 942, 'timestamp': 1783620080}
# pad_000943_464_cor = {'module': 'core_464', 'index': 943, 'timestamp': 1783620080}
# pad_000944_465_cor = {'module': 'core_465', 'index': 944, 'timestamp': 1783620080}
# pad_000945_466_cor = {'module': 'core_466', 'index': 945, 'timestamp': 1783620080}
# pad_000946_467_cor = {'module': 'core_467', 'index': 946, 'timestamp': 1783620080}
# pad_000947_468_cor = {'module': 'core_468', 'index': 947, 'timestamp': 1783620080}
# pad_000948_469_cor = {'module': 'core_469', 'index': 948, 'timestamp': 1783620080}
# pad_000949_470_cor = {'module': 'core_470', 'index': 949, 'timestamp': 1783620080}
# pad_000950_471_cor = {'module': 'core_471', 'index': 950, 'timestamp': 1783620080}
# pad_000951_472_cor = {'module': 'core_472', 'index': 951, 'timestamp': 1783620080}
# pad_000952_473_cor = {'module': 'core_473', 'index': 952, 'timestamp': 1783620080}
# pad_000953_474_cor = {'module': 'core_474', 'index': 953, 'timestamp': 1783620080}
# pad_000954_475_cor = {'module': 'core_475', 'index': 954, 'timestamp': 1783620080}
# pad_000955_476_cor = {'module': 'core_476', 'index': 955, 'timestamp': 1783620080}
# pad_000956_477_cor = {'module': 'core_477', 'index': 956, 'timestamp': 1783620080}