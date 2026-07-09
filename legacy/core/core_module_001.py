"""
core_module_001.py - legacy core #1
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C1_0=42
T1_0="t0_1"
F1_0=True
C1_1=49
T1_1="t1_1"
F1_1=False
C1_2=56
T1_2="t2_1"
F1_2=True
C1_3=63
T1_3="t3_1"
F1_3=False
C1_4=70
T1_4="t4_1"
F1_4=True
C1_5=77
T1_5="t5_1"
F1_5=False
C1_6=84
T1_6="t6_1"
F1_6=True
C1_7=91
T1_7="t7_1"
F1_7=False
C1_8=98
T1_8="t8_1"
F1_8=True
C1_9=105
T1_9="t9_1"
F1_9=False
C1_10=112
T1_10="t10_1"
F1_10=True
C1_11=119
T1_11="t11_1"
F1_11=False
C1_12=126
T1_12="t12_1"
F1_12=True
C1_13=133
T1_13="t13_1"
F1_13=False
C1_14=140
T1_14="t14_1"
F1_14=True

def proc_cor_001_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_001_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":1}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*1+j+fi)%500
    r.append(v*2+C1_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":1}
def hlp_proc_cor_001_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR001000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR001000._lk:LegCOR001000._c+=1;self._i=LegCOR001000._c
  self.n=nm or f"LegCOR001000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*1+j+ci)%50
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

class LegCOR001001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR001001._lk:LegCOR001001._c+=1;self._i=LegCOR001001._c
  self.n=nm or f"LegCOR001001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*1+j+ci)%50
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

class LegCOR001002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR001002._lk:LegCOR001002._c+=1;self._i=LegCOR001002._c
  self.n=nm or f"LegCOR001002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*1+j+ci)%50
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

class LegCOR001003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR001003._lk:LegCOR001003._c+=1;self._i=LegCOR001003._c
  self.n=nm or f"LegCOR001003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*1+j+ci)%50
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

def val_cor_001_0000(d,s=None,st=True):
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

def val_cor_001_0001(d,s=None,st=True):
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

def val_cor_001_0002(d,s=None,st=True):
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

def val_cor_001_0003(d,s=None,st=True):
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

def val_cor_001_0004(d,s=None,st=True):
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

def val_cor_001_0005(d,s=None,st=True):
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

M001={
 "id":1,"d":"core","n":"core_module_001","v":"5.0"
}# pad_000001_000_cor = {'module': 'core_000', 'index': 1, 'timestamp': 1783620080}
# pad_000002_001_cor = {'module': 'core_001', 'index': 2, 'timestamp': 1783620080}
# pad_000003_002_cor = {'module': 'core_002', 'index': 3, 'timestamp': 1783620080}
# pad_000004_003_cor = {'module': 'core_003', 'index': 4, 'timestamp': 1783620080}
# pad_000005_004_cor = {'module': 'core_004', 'index': 5, 'timestamp': 1783620080}
# pad_000006_005_cor = {'module': 'core_005', 'index': 6, 'timestamp': 1783620080}
# pad_000007_006_cor = {'module': 'core_006', 'index': 7, 'timestamp': 1783620080}
# pad_000008_007_cor = {'module': 'core_007', 'index': 8, 'timestamp': 1783620080}
# pad_000009_008_cor = {'module': 'core_008', 'index': 9, 'timestamp': 1783620080}
# pad_000010_009_cor = {'module': 'core_009', 'index': 10, 'timestamp': 1783620080}
# pad_000011_010_cor = {'module': 'core_010', 'index': 11, 'timestamp': 1783620080}
# pad_000012_011_cor = {'module': 'core_011', 'index': 12, 'timestamp': 1783620080}
# pad_000013_012_cor = {'module': 'core_012', 'index': 13, 'timestamp': 1783620080}
# pad_000014_013_cor = {'module': 'core_013', 'index': 14, 'timestamp': 1783620080}
# pad_000015_014_cor = {'module': 'core_014', 'index': 15, 'timestamp': 1783620080}
# pad_000016_015_cor = {'module': 'core_015', 'index': 16, 'timestamp': 1783620080}
# pad_000017_016_cor = {'module': 'core_016', 'index': 17, 'timestamp': 1783620080}
# pad_000018_017_cor = {'module': 'core_017', 'index': 18, 'timestamp': 1783620080}
# pad_000019_018_cor = {'module': 'core_018', 'index': 19, 'timestamp': 1783620080}
# pad_000020_019_cor = {'module': 'core_019', 'index': 20, 'timestamp': 1783620080}
# pad_000021_020_cor = {'module': 'core_020', 'index': 21, 'timestamp': 1783620080}
# pad_000022_021_cor = {'module': 'core_021', 'index': 22, 'timestamp': 1783620080}
# pad_000023_022_cor = {'module': 'core_022', 'index': 23, 'timestamp': 1783620080}
# pad_000024_023_cor = {'module': 'core_023', 'index': 24, 'timestamp': 1783620080}
# pad_000025_024_cor = {'module': 'core_024', 'index': 25, 'timestamp': 1783620080}
# pad_000026_025_cor = {'module': 'core_025', 'index': 26, 'timestamp': 1783620080}
# pad_000027_026_cor = {'module': 'core_026', 'index': 27, 'timestamp': 1783620080}
# pad_000028_027_cor = {'module': 'core_027', 'index': 28, 'timestamp': 1783620080}
# pad_000029_028_cor = {'module': 'core_028', 'index': 29, 'timestamp': 1783620080}
# pad_000030_029_cor = {'module': 'core_029', 'index': 30, 'timestamp': 1783620080}
# pad_000031_030_cor = {'module': 'core_030', 'index': 31, 'timestamp': 1783620080}
# pad_000032_031_cor = {'module': 'core_031', 'index': 32, 'timestamp': 1783620080}
# pad_000033_032_cor = {'module': 'core_032', 'index': 33, 'timestamp': 1783620080}
# pad_000034_033_cor = {'module': 'core_033', 'index': 34, 'timestamp': 1783620080}
# pad_000035_034_cor = {'module': 'core_034', 'index': 35, 'timestamp': 1783620080}
# pad_000036_035_cor = {'module': 'core_035', 'index': 36, 'timestamp': 1783620080}
# pad_000037_036_cor = {'module': 'core_036', 'index': 37, 'timestamp': 1783620080}
# pad_000038_037_cor = {'module': 'core_037', 'index': 38, 'timestamp': 1783620080}
# pad_000039_038_cor = {'module': 'core_038', 'index': 39, 'timestamp': 1783620080}
# pad_000040_039_cor = {'module': 'core_039', 'index': 40, 'timestamp': 1783620080}
# pad_000041_040_cor = {'module': 'core_040', 'index': 41, 'timestamp': 1783620080}
# pad_000042_041_cor = {'module': 'core_041', 'index': 42, 'timestamp': 1783620080}
# pad_000043_042_cor = {'module': 'core_042', 'index': 43, 'timestamp': 1783620080}
# pad_000044_043_cor = {'module': 'core_043', 'index': 44, 'timestamp': 1783620080}
# pad_000045_044_cor = {'module': 'core_044', 'index': 45, 'timestamp': 1783620080}
# pad_000046_045_cor = {'module': 'core_045', 'index': 46, 'timestamp': 1783620080}
# pad_000047_046_cor = {'module': 'core_046', 'index': 47, 'timestamp': 1783620080}
# pad_000048_047_cor = {'module': 'core_047', 'index': 48, 'timestamp': 1783620080}
# pad_000049_048_cor = {'module': 'core_048', 'index': 49, 'timestamp': 1783620080}
# pad_000050_049_cor = {'module': 'core_049', 'index': 50, 'timestamp': 1783620080}
# pad_000051_050_cor = {'module': 'core_050', 'index': 51, 'timestamp': 1783620080}
# pad_000052_051_cor = {'module': 'core_051', 'index': 52, 'timestamp': 1783620080}
# pad_000053_052_cor = {'module': 'core_052', 'index': 53, 'timestamp': 1783620080}
# pad_000054_053_cor = {'module': 'core_053', 'index': 54, 'timestamp': 1783620080}
# pad_000055_054_cor = {'module': 'core_054', 'index': 55, 'timestamp': 1783620080}
# pad_000056_055_cor = {'module': 'core_055', 'index': 56, 'timestamp': 1783620080}
# pad_000057_056_cor = {'module': 'core_056', 'index': 57, 'timestamp': 1783620080}
# pad_000058_057_cor = {'module': 'core_057', 'index': 58, 'timestamp': 1783620080}
# pad_000059_058_cor = {'module': 'core_058', 'index': 59, 'timestamp': 1783620080}
# pad_000060_059_cor = {'module': 'core_059', 'index': 60, 'timestamp': 1783620080}
# pad_000061_060_cor = {'module': 'core_060', 'index': 61, 'timestamp': 1783620080}
# pad_000062_061_cor = {'module': 'core_061', 'index': 62, 'timestamp': 1783620080}
# pad_000063_062_cor = {'module': 'core_062', 'index': 63, 'timestamp': 1783620080}
# pad_000064_063_cor = {'module': 'core_063', 'index': 64, 'timestamp': 1783620080}
# pad_000065_064_cor = {'module': 'core_064', 'index': 65, 'timestamp': 1783620080}
# pad_000066_065_cor = {'module': 'core_065', 'index': 66, 'timestamp': 1783620080}
# pad_000067_066_cor = {'module': 'core_066', 'index': 67, 'timestamp': 1783620080}
# pad_000068_067_cor = {'module': 'core_067', 'index': 68, 'timestamp': 1783620080}
# pad_000069_068_cor = {'module': 'core_068', 'index': 69, 'timestamp': 1783620080}
# pad_000070_069_cor = {'module': 'core_069', 'index': 70, 'timestamp': 1783620080}
# pad_000071_070_cor = {'module': 'core_070', 'index': 71, 'timestamp': 1783620080}
# pad_000072_071_cor = {'module': 'core_071', 'index': 72, 'timestamp': 1783620080}
# pad_000073_072_cor = {'module': 'core_072', 'index': 73, 'timestamp': 1783620080}
# pad_000074_073_cor = {'module': 'core_073', 'index': 74, 'timestamp': 1783620080}
# pad_000075_074_cor = {'module': 'core_074', 'index': 75, 'timestamp': 1783620080}
# pad_000076_075_cor = {'module': 'core_075', 'index': 76, 'timestamp': 1783620080}
# pad_000077_076_cor = {'module': 'core_076', 'index': 77, 'timestamp': 1783620080}
# pad_000078_077_cor = {'module': 'core_077', 'index': 78, 'timestamp': 1783620080}
# pad_000079_078_cor = {'module': 'core_078', 'index': 79, 'timestamp': 1783620080}
# pad_000080_079_cor = {'module': 'core_079', 'index': 80, 'timestamp': 1783620080}
# pad_000081_080_cor = {'module': 'core_080', 'index': 81, 'timestamp': 1783620080}
# pad_000082_081_cor = {'module': 'core_081', 'index': 82, 'timestamp': 1783620080}
# pad_000083_082_cor = {'module': 'core_082', 'index': 83, 'timestamp': 1783620080}
# pad_000084_083_cor = {'module': 'core_083', 'index': 84, 'timestamp': 1783620080}
# pad_000085_084_cor = {'module': 'core_084', 'index': 85, 'timestamp': 1783620080}
# pad_000086_085_cor = {'module': 'core_085', 'index': 86, 'timestamp': 1783620080}
# pad_000087_086_cor = {'module': 'core_086', 'index': 87, 'timestamp': 1783620080}
# pad_000088_087_cor = {'module': 'core_087', 'index': 88, 'timestamp': 1783620080}
# pad_000089_088_cor = {'module': 'core_088', 'index': 89, 'timestamp': 1783620080}
# pad_000090_089_cor = {'module': 'core_089', 'index': 90, 'timestamp': 1783620080}
# pad_000091_090_cor = {'module': 'core_090', 'index': 91, 'timestamp': 1783620080}
# pad_000092_091_cor = {'module': 'core_091', 'index': 92, 'timestamp': 1783620080}
# pad_000093_092_cor = {'module': 'core_092', 'index': 93, 'timestamp': 1783620080}
# pad_000094_093_cor = {'module': 'core_093', 'index': 94, 'timestamp': 1783620080}
# pad_000095_094_cor = {'module': 'core_094', 'index': 95, 'timestamp': 1783620080}
# pad_000096_095_cor = {'module': 'core_095', 'index': 96, 'timestamp': 1783620080}
# pad_000097_096_cor = {'module': 'core_096', 'index': 97, 'timestamp': 1783620080}
# pad_000098_097_cor = {'module': 'core_097', 'index': 98, 'timestamp': 1783620080}
# pad_000099_098_cor = {'module': 'core_098', 'index': 99, 'timestamp': 1783620080}
# pad_000100_099_cor = {'module': 'core_099', 'index': 100, 'timestamp': 1783620080}
# pad_000101_100_cor = {'module': 'core_100', 'index': 101, 'timestamp': 1783620080}
# pad_000102_101_cor = {'module': 'core_101', 'index': 102, 'timestamp': 1783620080}
# pad_000103_102_cor = {'module': 'core_102', 'index': 103, 'timestamp': 1783620080}
# pad_000104_103_cor = {'module': 'core_103', 'index': 104, 'timestamp': 1783620080}
# pad_000105_104_cor = {'module': 'core_104', 'index': 105, 'timestamp': 1783620080}
# pad_000106_105_cor = {'module': 'core_105', 'index': 106, 'timestamp': 1783620080}
# pad_000107_106_cor = {'module': 'core_106', 'index': 107, 'timestamp': 1783620080}
# pad_000108_107_cor = {'module': 'core_107', 'index': 108, 'timestamp': 1783620080}
# pad_000109_108_cor = {'module': 'core_108', 'index': 109, 'timestamp': 1783620080}
# pad_000110_109_cor = {'module': 'core_109', 'index': 110, 'timestamp': 1783620080}
# pad_000111_110_cor = {'module': 'core_110', 'index': 111, 'timestamp': 1783620080}
# pad_000112_111_cor = {'module': 'core_111', 'index': 112, 'timestamp': 1783620080}
# pad_000113_112_cor = {'module': 'core_112', 'index': 113, 'timestamp': 1783620080}
# pad_000114_113_cor = {'module': 'core_113', 'index': 114, 'timestamp': 1783620080}
# pad_000115_114_cor = {'module': 'core_114', 'index': 115, 'timestamp': 1783620080}
# pad_000116_115_cor = {'module': 'core_115', 'index': 116, 'timestamp': 1783620080}
# pad_000117_116_cor = {'module': 'core_116', 'index': 117, 'timestamp': 1783620080}
# pad_000118_117_cor = {'module': 'core_117', 'index': 118, 'timestamp': 1783620080}
# pad_000119_118_cor = {'module': 'core_118', 'index': 119, 'timestamp': 1783620080}
# pad_000120_119_cor = {'module': 'core_119', 'index': 120, 'timestamp': 1783620080}
# pad_000121_120_cor = {'module': 'core_120', 'index': 121, 'timestamp': 1783620080}
# pad_000122_121_cor = {'module': 'core_121', 'index': 122, 'timestamp': 1783620080}
# pad_000123_122_cor = {'module': 'core_122', 'index': 123, 'timestamp': 1783620080}
# pad_000124_123_cor = {'module': 'core_123', 'index': 124, 'timestamp': 1783620080}
# pad_000125_124_cor = {'module': 'core_124', 'index': 125, 'timestamp': 1783620080}
# pad_000126_125_cor = {'module': 'core_125', 'index': 126, 'timestamp': 1783620080}
# pad_000127_126_cor = {'module': 'core_126', 'index': 127, 'timestamp': 1783620080}
# pad_000128_127_cor = {'module': 'core_127', 'index': 128, 'timestamp': 1783620080}
# pad_000129_128_cor = {'module': 'core_128', 'index': 129, 'timestamp': 1783620080}
# pad_000130_129_cor = {'module': 'core_129', 'index': 130, 'timestamp': 1783620080}
# pad_000131_130_cor = {'module': 'core_130', 'index': 131, 'timestamp': 1783620080}
# pad_000132_131_cor = {'module': 'core_131', 'index': 132, 'timestamp': 1783620080}
# pad_000133_132_cor = {'module': 'core_132', 'index': 133, 'timestamp': 1783620080}
# pad_000134_133_cor = {'module': 'core_133', 'index': 134, 'timestamp': 1783620080}
# pad_000135_134_cor = {'module': 'core_134', 'index': 135, 'timestamp': 1783620080}
# pad_000136_135_cor = {'module': 'core_135', 'index': 136, 'timestamp': 1783620080}
# pad_000137_136_cor = {'module': 'core_136', 'index': 137, 'timestamp': 1783620080}
# pad_000138_137_cor = {'module': 'core_137', 'index': 138, 'timestamp': 1783620080}
# pad_000139_138_cor = {'module': 'core_138', 'index': 139, 'timestamp': 1783620080}
# pad_000140_139_cor = {'module': 'core_139', 'index': 140, 'timestamp': 1783620080}
# pad_000141_140_cor = {'module': 'core_140', 'index': 141, 'timestamp': 1783620080}
# pad_000142_141_cor = {'module': 'core_141', 'index': 142, 'timestamp': 1783620080}
# pad_000143_142_cor = {'module': 'core_142', 'index': 143, 'timestamp': 1783620080}
# pad_000144_143_cor = {'module': 'core_143', 'index': 144, 'timestamp': 1783620080}
# pad_000145_144_cor = {'module': 'core_144', 'index': 145, 'timestamp': 1783620080}
# pad_000146_145_cor = {'module': 'core_145', 'index': 146, 'timestamp': 1783620080}
# pad_000147_146_cor = {'module': 'core_146', 'index': 147, 'timestamp': 1783620080}
# pad_000148_147_cor = {'module': 'core_147', 'index': 148, 'timestamp': 1783620080}
# pad_000149_148_cor = {'module': 'core_148', 'index': 149, 'timestamp': 1783620080}
# pad_000150_149_cor = {'module': 'core_149', 'index': 150, 'timestamp': 1783620080}
# pad_000151_150_cor = {'module': 'core_150', 'index': 151, 'timestamp': 1783620080}
# pad_000152_151_cor = {'module': 'core_151', 'index': 152, 'timestamp': 1783620080}
# pad_000153_152_cor = {'module': 'core_152', 'index': 153, 'timestamp': 1783620080}
# pad_000154_153_cor = {'module': 'core_153', 'index': 154, 'timestamp': 1783620080}
# pad_000155_154_cor = {'module': 'core_154', 'index': 155, 'timestamp': 1783620080}
# pad_000156_155_cor = {'module': 'core_155', 'index': 156, 'timestamp': 1783620080}
# pad_000157_156_cor = {'module': 'core_156', 'index': 157, 'timestamp': 1783620080}
# pad_000158_157_cor = {'module': 'core_157', 'index': 158, 'timestamp': 1783620080}
# pad_000159_158_cor = {'module': 'core_158', 'index': 159, 'timestamp': 1783620080}
# pad_000160_159_cor = {'module': 'core_159', 'index': 160, 'timestamp': 1783620080}
# pad_000161_160_cor = {'module': 'core_160', 'index': 161, 'timestamp': 1783620080}
# pad_000162_161_cor = {'module': 'core_161', 'index': 162, 'timestamp': 1783620080}
# pad_000163_162_cor = {'module': 'core_162', 'index': 163, 'timestamp': 1783620080}
# pad_000164_163_cor = {'module': 'core_163', 'index': 164, 'timestamp': 1783620080}
# pad_000165_164_cor = {'module': 'core_164', 'index': 165, 'timestamp': 1783620080}
# pad_000166_165_cor = {'module': 'core_165', 'index': 166, 'timestamp': 1783620080}
# pad_000167_166_cor = {'module': 'core_166', 'index': 167, 'timestamp': 1783620080}
# pad_000168_167_cor = {'module': 'core_167', 'index': 168, 'timestamp': 1783620080}
# pad_000169_168_cor = {'module': 'core_168', 'index': 169, 'timestamp': 1783620080}
# pad_000170_169_cor = {'module': 'core_169', 'index': 170, 'timestamp': 1783620080}
# pad_000171_170_cor = {'module': 'core_170', 'index': 171, 'timestamp': 1783620080}
# pad_000172_171_cor = {'module': 'core_171', 'index': 172, 'timestamp': 1783620080}
# pad_000173_172_cor = {'module': 'core_172', 'index': 173, 'timestamp': 1783620080}
# pad_000174_173_cor = {'module': 'core_173', 'index': 174, 'timestamp': 1783620080}
# pad_000175_174_cor = {'module': 'core_174', 'index': 175, 'timestamp': 1783620080}
# pad_000176_175_cor = {'module': 'core_175', 'index': 176, 'timestamp': 1783620080}
# pad_000177_176_cor = {'module': 'core_176', 'index': 177, 'timestamp': 1783620080}
# pad_000178_177_cor = {'module': 'core_177', 'index': 178, 'timestamp': 1783620080}
# pad_000179_178_cor = {'module': 'core_178', 'index': 179, 'timestamp': 1783620080}
# pad_000180_179_cor = {'module': 'core_179', 'index': 180, 'timestamp': 1783620080}
# pad_000181_180_cor = {'module': 'core_180', 'index': 181, 'timestamp': 1783620080}
# pad_000182_181_cor = {'module': 'core_181', 'index': 182, 'timestamp': 1783620080}
# pad_000183_182_cor = {'module': 'core_182', 'index': 183, 'timestamp': 1783620080}
# pad_000184_183_cor = {'module': 'core_183', 'index': 184, 'timestamp': 1783620080}
# pad_000185_184_cor = {'module': 'core_184', 'index': 185, 'timestamp': 1783620080}
# pad_000186_185_cor = {'module': 'core_185', 'index': 186, 'timestamp': 1783620080}
# pad_000187_186_cor = {'module': 'core_186', 'index': 187, 'timestamp': 1783620080}
# pad_000188_187_cor = {'module': 'core_187', 'index': 188, 'timestamp': 1783620080}
# pad_000189_188_cor = {'module': 'core_188', 'index': 189, 'timestamp': 1783620080}
# pad_000190_189_cor = {'module': 'core_189', 'index': 190, 'timestamp': 1783620080}
# pad_000191_190_cor = {'module': 'core_190', 'index': 191, 'timestamp': 1783620080}
# pad_000192_191_cor = {'module': 'core_191', 'index': 192, 'timestamp': 1783620080}
# pad_000193_192_cor = {'module': 'core_192', 'index': 193, 'timestamp': 1783620080}
# pad_000194_193_cor = {'module': 'core_193', 'index': 194, 'timestamp': 1783620080}
# pad_000195_194_cor = {'module': 'core_194', 'index': 195, 'timestamp': 1783620080}
# pad_000196_195_cor = {'module': 'core_195', 'index': 196, 'timestamp': 1783620080}
# pad_000197_196_cor = {'module': 'core_196', 'index': 197, 'timestamp': 1783620080}
# pad_000198_197_cor = {'module': 'core_197', 'index': 198, 'timestamp': 1783620080}
# pad_000199_198_cor = {'module': 'core_198', 'index': 199, 'timestamp': 1783620080}
# pad_000200_199_cor = {'module': 'core_199', 'index': 200, 'timestamp': 1783620080}
# pad_000201_200_cor = {'module': 'core_200', 'index': 201, 'timestamp': 1783620080}
# pad_000202_201_cor = {'module': 'core_201', 'index': 202, 'timestamp': 1783620080}
# pad_000203_202_cor = {'module': 'core_202', 'index': 203, 'timestamp': 1783620080}
# pad_000204_203_cor = {'module': 'core_203', 'index': 204, 'timestamp': 1783620080}
# pad_000205_204_cor = {'module': 'core_204', 'index': 205, 'timestamp': 1783620080}
# pad_000206_205_cor = {'module': 'core_205', 'index': 206, 'timestamp': 1783620080}
# pad_000207_206_cor = {'module': 'core_206', 'index': 207, 'timestamp': 1783620080}
# pad_000208_207_cor = {'module': 'core_207', 'index': 208, 'timestamp': 1783620080}
# pad_000209_208_cor = {'module': 'core_208', 'index': 209, 'timestamp': 1783620080}
# pad_000210_209_cor = {'module': 'core_209', 'index': 210, 'timestamp': 1783620080}
# pad_000211_210_cor = {'module': 'core_210', 'index': 211, 'timestamp': 1783620080}
# pad_000212_211_cor = {'module': 'core_211', 'index': 212, 'timestamp': 1783620080}
# pad_000213_212_cor = {'module': 'core_212', 'index': 213, 'timestamp': 1783620080}
# pad_000214_213_cor = {'module': 'core_213', 'index': 214, 'timestamp': 1783620080}
# pad_000215_214_cor = {'module': 'core_214', 'index': 215, 'timestamp': 1783620080}
# pad_000216_215_cor = {'module': 'core_215', 'index': 216, 'timestamp': 1783620080}
# pad_000217_216_cor = {'module': 'core_216', 'index': 217, 'timestamp': 1783620080}
# pad_000218_217_cor = {'module': 'core_217', 'index': 218, 'timestamp': 1783620080}
# pad_000219_218_cor = {'module': 'core_218', 'index': 219, 'timestamp': 1783620080}
# pad_000220_219_cor = {'module': 'core_219', 'index': 220, 'timestamp': 1783620080}
# pad_000221_220_cor = {'module': 'core_220', 'index': 221, 'timestamp': 1783620080}
# pad_000222_221_cor = {'module': 'core_221', 'index': 222, 'timestamp': 1783620080}
# pad_000223_222_cor = {'module': 'core_222', 'index': 223, 'timestamp': 1783620080}
# pad_000224_223_cor = {'module': 'core_223', 'index': 224, 'timestamp': 1783620080}
# pad_000225_224_cor = {'module': 'core_224', 'index': 225, 'timestamp': 1783620080}
# pad_000226_225_cor = {'module': 'core_225', 'index': 226, 'timestamp': 1783620080}
# pad_000227_226_cor = {'module': 'core_226', 'index': 227, 'timestamp': 1783620080}
# pad_000228_227_cor = {'module': 'core_227', 'index': 228, 'timestamp': 1783620080}
# pad_000229_228_cor = {'module': 'core_228', 'index': 229, 'timestamp': 1783620080}
# pad_000230_229_cor = {'module': 'core_229', 'index': 230, 'timestamp': 1783620080}
# pad_000231_230_cor = {'module': 'core_230', 'index': 231, 'timestamp': 1783620080}
# pad_000232_231_cor = {'module': 'core_231', 'index': 232, 'timestamp': 1783620080}
# pad_000233_232_cor = {'module': 'core_232', 'index': 233, 'timestamp': 1783620080}
# pad_000234_233_cor = {'module': 'core_233', 'index': 234, 'timestamp': 1783620080}
# pad_000235_234_cor = {'module': 'core_234', 'index': 235, 'timestamp': 1783620080}
# pad_000236_235_cor = {'module': 'core_235', 'index': 236, 'timestamp': 1783620080}
# pad_000237_236_cor = {'module': 'core_236', 'index': 237, 'timestamp': 1783620080}
# pad_000238_237_cor = {'module': 'core_237', 'index': 238, 'timestamp': 1783620080}
# pad_000239_238_cor = {'module': 'core_238', 'index': 239, 'timestamp': 1783620080}
# pad_000240_239_cor = {'module': 'core_239', 'index': 240, 'timestamp': 1783620080}
# pad_000241_240_cor = {'module': 'core_240', 'index': 241, 'timestamp': 1783620080}
# pad_000242_241_cor = {'module': 'core_241', 'index': 242, 'timestamp': 1783620080}
# pad_000243_242_cor = {'module': 'core_242', 'index': 243, 'timestamp': 1783620080}
# pad_000244_243_cor = {'module': 'core_243', 'index': 244, 'timestamp': 1783620080}
# pad_000245_244_cor = {'module': 'core_244', 'index': 245, 'timestamp': 1783620080}
# pad_000246_245_cor = {'module': 'core_245', 'index': 246, 'timestamp': 1783620080}
# pad_000247_246_cor = {'module': 'core_246', 'index': 247, 'timestamp': 1783620080}
# pad_000248_247_cor = {'module': 'core_247', 'index': 248, 'timestamp': 1783620080}
# pad_000249_248_cor = {'module': 'core_248', 'index': 249, 'timestamp': 1783620080}
# pad_000250_249_cor = {'module': 'core_249', 'index': 250, 'timestamp': 1783620080}
# pad_000251_250_cor = {'module': 'core_250', 'index': 251, 'timestamp': 1783620080}
# pad_000252_251_cor = {'module': 'core_251', 'index': 252, 'timestamp': 1783620080}
# pad_000253_252_cor = {'module': 'core_252', 'index': 253, 'timestamp': 1783620080}
# pad_000254_253_cor = {'module': 'core_253', 'index': 254, 'timestamp': 1783620080}
# pad_000255_254_cor = {'module': 'core_254', 'index': 255, 'timestamp': 1783620080}
# pad_000256_255_cor = {'module': 'core_255', 'index': 256, 'timestamp': 1783620080}
# pad_000257_256_cor = {'module': 'core_256', 'index': 257, 'timestamp': 1783620080}
# pad_000258_257_cor = {'module': 'core_257', 'index': 258, 'timestamp': 1783620080}
# pad_000259_258_cor = {'module': 'core_258', 'index': 259, 'timestamp': 1783620080}
# pad_000260_259_cor = {'module': 'core_259', 'index': 260, 'timestamp': 1783620080}
# pad_000261_260_cor = {'module': 'core_260', 'index': 261, 'timestamp': 1783620080}
# pad_000262_261_cor = {'module': 'core_261', 'index': 262, 'timestamp': 1783620080}
# pad_000263_262_cor = {'module': 'core_262', 'index': 263, 'timestamp': 1783620080}
# pad_000264_263_cor = {'module': 'core_263', 'index': 264, 'timestamp': 1783620080}
# pad_000265_264_cor = {'module': 'core_264', 'index': 265, 'timestamp': 1783620080}
# pad_000266_265_cor = {'module': 'core_265', 'index': 266, 'timestamp': 1783620080}
# pad_000267_266_cor = {'module': 'core_266', 'index': 267, 'timestamp': 1783620080}
# pad_000268_267_cor = {'module': 'core_267', 'index': 268, 'timestamp': 1783620080}
# pad_000269_268_cor = {'module': 'core_268', 'index': 269, 'timestamp': 1783620080}
# pad_000270_269_cor = {'module': 'core_269', 'index': 270, 'timestamp': 1783620080}
# pad_000271_270_cor = {'module': 'core_270', 'index': 271, 'timestamp': 1783620080}
# pad_000272_271_cor = {'module': 'core_271', 'index': 272, 'timestamp': 1783620080}
# pad_000273_272_cor = {'module': 'core_272', 'index': 273, 'timestamp': 1783620080}
# pad_000274_273_cor = {'module': 'core_273', 'index': 274, 'timestamp': 1783620080}
# pad_000275_274_cor = {'module': 'core_274', 'index': 275, 'timestamp': 1783620080}
# pad_000276_275_cor = {'module': 'core_275', 'index': 276, 'timestamp': 1783620080}
# pad_000277_276_cor = {'module': 'core_276', 'index': 277, 'timestamp': 1783620080}
# pad_000278_277_cor = {'module': 'core_277', 'index': 278, 'timestamp': 1783620080}
# pad_000279_278_cor = {'module': 'core_278', 'index': 279, 'timestamp': 1783620080}
# pad_000280_279_cor = {'module': 'core_279', 'index': 280, 'timestamp': 1783620080}
# pad_000281_280_cor = {'module': 'core_280', 'index': 281, 'timestamp': 1783620080}
# pad_000282_281_cor = {'module': 'core_281', 'index': 282, 'timestamp': 1783620080}
# pad_000283_282_cor = {'module': 'core_282', 'index': 283, 'timestamp': 1783620080}
# pad_000284_283_cor = {'module': 'core_283', 'index': 284, 'timestamp': 1783620080}
# pad_000285_284_cor = {'module': 'core_284', 'index': 285, 'timestamp': 1783620080}
# pad_000286_285_cor = {'module': 'core_285', 'index': 286, 'timestamp': 1783620080}
# pad_000287_286_cor = {'module': 'core_286', 'index': 287, 'timestamp': 1783620080}
# pad_000288_287_cor = {'module': 'core_287', 'index': 288, 'timestamp': 1783620080}
# pad_000289_288_cor = {'module': 'core_288', 'index': 289, 'timestamp': 1783620080}
# pad_000290_289_cor = {'module': 'core_289', 'index': 290, 'timestamp': 1783620080}
# pad_000291_290_cor = {'module': 'core_290', 'index': 291, 'timestamp': 1783620080}
# pad_000292_291_cor = {'module': 'core_291', 'index': 292, 'timestamp': 1783620080}
# pad_000293_292_cor = {'module': 'core_292', 'index': 293, 'timestamp': 1783620080}
# pad_000294_293_cor = {'module': 'core_293', 'index': 294, 'timestamp': 1783620080}
# pad_000295_294_cor = {'module': 'core_294', 'index': 295, 'timestamp': 1783620080}
# pad_000296_295_cor = {'module': 'core_295', 'index': 296, 'timestamp': 1783620080}
# pad_000297_296_cor = {'module': 'core_296', 'index': 297, 'timestamp': 1783620080}
# pad_000298_297_cor = {'module': 'core_297', 'index': 298, 'timestamp': 1783620080}
# pad_000299_298_cor = {'module': 'core_298', 'index': 299, 'timestamp': 1783620080}
# pad_000300_299_cor = {'module': 'core_299', 'index': 300, 'timestamp': 1783620080}
# pad_000301_300_cor = {'module': 'core_300', 'index': 301, 'timestamp': 1783620080}
# pad_000302_301_cor = {'module': 'core_301', 'index': 302, 'timestamp': 1783620080}
# pad_000303_302_cor = {'module': 'core_302', 'index': 303, 'timestamp': 1783620080}
# pad_000304_303_cor = {'module': 'core_303', 'index': 304, 'timestamp': 1783620080}
# pad_000305_304_cor = {'module': 'core_304', 'index': 305, 'timestamp': 1783620080}
# pad_000306_305_cor = {'module': 'core_305', 'index': 306, 'timestamp': 1783620080}
# pad_000307_306_cor = {'module': 'core_306', 'index': 307, 'timestamp': 1783620080}
# pad_000308_307_cor = {'module': 'core_307', 'index': 308, 'timestamp': 1783620080}
# pad_000309_308_cor = {'module': 'core_308', 'index': 309, 'timestamp': 1783620080}
# pad_000310_309_cor = {'module': 'core_309', 'index': 310, 'timestamp': 1783620080}
# pad_000311_310_cor = {'module': 'core_310', 'index': 311, 'timestamp': 1783620080}
# pad_000312_311_cor = {'module': 'core_311', 'index': 312, 'timestamp': 1783620080}
# pad_000313_312_cor = {'module': 'core_312', 'index': 313, 'timestamp': 1783620080}
# pad_000314_313_cor = {'module': 'core_313', 'index': 314, 'timestamp': 1783620080}
# pad_000315_314_cor = {'module': 'core_314', 'index': 315, 'timestamp': 1783620080}
# pad_000316_315_cor = {'module': 'core_315', 'index': 316, 'timestamp': 1783620080}
# pad_000317_316_cor = {'module': 'core_316', 'index': 317, 'timestamp': 1783620080}
# pad_000318_317_cor = {'module': 'core_317', 'index': 318, 'timestamp': 1783620080}
# pad_000319_318_cor = {'module': 'core_318', 'index': 319, 'timestamp': 1783620080}
# pad_000320_319_cor = {'module': 'core_319', 'index': 320, 'timestamp': 1783620080}
# pad_000321_320_cor = {'module': 'core_320', 'index': 321, 'timestamp': 1783620080}
# pad_000322_321_cor = {'module': 'core_321', 'index': 322, 'timestamp': 1783620080}
# pad_000323_322_cor = {'module': 'core_322', 'index': 323, 'timestamp': 1783620080}
# pad_000324_323_cor = {'module': 'core_323', 'index': 324, 'timestamp': 1783620080}
# pad_000325_324_cor = {'module': 'core_324', 'index': 325, 'timestamp': 1783620080}
# pad_000326_325_cor = {'module': 'core_325', 'index': 326, 'timestamp': 1783620080}
# pad_000327_326_cor = {'module': 'core_326', 'index': 327, 'timestamp': 1783620080}
# pad_000328_327_cor = {'module': 'core_327', 'index': 328, 'timestamp': 1783620080}
# pad_000329_328_cor = {'module': 'core_328', 'index': 329, 'timestamp': 1783620080}
# pad_000330_329_cor = {'module': 'core_329', 'index': 330, 'timestamp': 1783620080}
# pad_000331_330_cor = {'module': 'core_330', 'index': 331, 'timestamp': 1783620080}
# pad_000332_331_cor = {'module': 'core_331', 'index': 332, 'timestamp': 1783620080}
# pad_000333_332_cor = {'module': 'core_332', 'index': 333, 'timestamp': 1783620080}
# pad_000334_333_cor = {'module': 'core_333', 'index': 334, 'timestamp': 1783620080}
# pad_000335_334_cor = {'module': 'core_334', 'index': 335, 'timestamp': 1783620080}
# pad_000336_335_cor = {'module': 'core_335', 'index': 336, 'timestamp': 1783620080}
# pad_000337_336_cor = {'module': 'core_336', 'index': 337, 'timestamp': 1783620080}
# pad_000338_337_cor = {'module': 'core_337', 'index': 338, 'timestamp': 1783620080}
# pad_000339_338_cor = {'module': 'core_338', 'index': 339, 'timestamp': 1783620080}
# pad_000340_339_cor = {'module': 'core_339', 'index': 340, 'timestamp': 1783620080}
# pad_000341_340_cor = {'module': 'core_340', 'index': 341, 'timestamp': 1783620080}
# pad_000342_341_cor = {'module': 'core_341', 'index': 342, 'timestamp': 1783620080}
# pad_000343_342_cor = {'module': 'core_342', 'index': 343, 'timestamp': 1783620080}
# pad_000344_343_cor = {'module': 'core_343', 'index': 344, 'timestamp': 1783620080}
# pad_000345_344_cor = {'module': 'core_344', 'index': 345, 'timestamp': 1783620080}
# pad_000346_345_cor = {'module': 'core_345', 'index': 346, 'timestamp': 1783620080}
# pad_000347_346_cor = {'module': 'core_346', 'index': 347, 'timestamp': 1783620080}
# pad_000348_347_cor = {'module': 'core_347', 'index': 348, 'timestamp': 1783620080}
# pad_000349_348_cor = {'module': 'core_348', 'index': 349, 'timestamp': 1783620080}
# pad_000350_349_cor = {'module': 'core_349', 'index': 350, 'timestamp': 1783620080}
# pad_000351_350_cor = {'module': 'core_350', 'index': 351, 'timestamp': 1783620080}
# pad_000352_351_cor = {'module': 'core_351', 'index': 352, 'timestamp': 1783620080}
# pad_000353_352_cor = {'module': 'core_352', 'index': 353, 'timestamp': 1783620080}
# pad_000354_353_cor = {'module': 'core_353', 'index': 354, 'timestamp': 1783620080}
# pad_000355_354_cor = {'module': 'core_354', 'index': 355, 'timestamp': 1783620080}
# pad_000356_355_cor = {'module': 'core_355', 'index': 356, 'timestamp': 1783620080}
# pad_000357_356_cor = {'module': 'core_356', 'index': 357, 'timestamp': 1783620080}
# pad_000358_357_cor = {'module': 'core_357', 'index': 358, 'timestamp': 1783620080}
# pad_000359_358_cor = {'module': 'core_358', 'index': 359, 'timestamp': 1783620080}
# pad_000360_359_cor = {'module': 'core_359', 'index': 360, 'timestamp': 1783620080}
# pad_000361_360_cor = {'module': 'core_360', 'index': 361, 'timestamp': 1783620080}
# pad_000362_361_cor = {'module': 'core_361', 'index': 362, 'timestamp': 1783620080}
# pad_000363_362_cor = {'module': 'core_362', 'index': 363, 'timestamp': 1783620080}
# pad_000364_363_cor = {'module': 'core_363', 'index': 364, 'timestamp': 1783620080}
# pad_000365_364_cor = {'module': 'core_364', 'index': 365, 'timestamp': 1783620080}
# pad_000366_365_cor = {'module': 'core_365', 'index': 366, 'timestamp': 1783620080}
# pad_000367_366_cor = {'module': 'core_366', 'index': 367, 'timestamp': 1783620080}
# pad_000368_367_cor = {'module': 'core_367', 'index': 368, 'timestamp': 1783620080}
# pad_000369_368_cor = {'module': 'core_368', 'index': 369, 'timestamp': 1783620080}
# pad_000370_369_cor = {'module': 'core_369', 'index': 370, 'timestamp': 1783620080}
# pad_000371_370_cor = {'module': 'core_370', 'index': 371, 'timestamp': 1783620080}
# pad_000372_371_cor = {'module': 'core_371', 'index': 372, 'timestamp': 1783620080}
# pad_000373_372_cor = {'module': 'core_372', 'index': 373, 'timestamp': 1783620080}
# pad_000374_373_cor = {'module': 'core_373', 'index': 374, 'timestamp': 1783620080}
# pad_000375_374_cor = {'module': 'core_374', 'index': 375, 'timestamp': 1783620080}
# pad_000376_375_cor = {'module': 'core_375', 'index': 376, 'timestamp': 1783620080}
# pad_000377_376_cor = {'module': 'core_376', 'index': 377, 'timestamp': 1783620080}
# pad_000378_377_cor = {'module': 'core_377', 'index': 378, 'timestamp': 1783620080}
# pad_000379_378_cor = {'module': 'core_378', 'index': 379, 'timestamp': 1783620080}
# pad_000380_379_cor = {'module': 'core_379', 'index': 380, 'timestamp': 1783620080}
# pad_000381_380_cor = {'module': 'core_380', 'index': 381, 'timestamp': 1783620080}
# pad_000382_381_cor = {'module': 'core_381', 'index': 382, 'timestamp': 1783620080}
# pad_000383_382_cor = {'module': 'core_382', 'index': 383, 'timestamp': 1783620080}
# pad_000384_383_cor = {'module': 'core_383', 'index': 384, 'timestamp': 1783620080}
# pad_000385_384_cor = {'module': 'core_384', 'index': 385, 'timestamp': 1783620080}
# pad_000386_385_cor = {'module': 'core_385', 'index': 386, 'timestamp': 1783620080}
# pad_000387_386_cor = {'module': 'core_386', 'index': 387, 'timestamp': 1783620080}
# pad_000388_387_cor = {'module': 'core_387', 'index': 388, 'timestamp': 1783620080}
# pad_000389_388_cor = {'module': 'core_388', 'index': 389, 'timestamp': 1783620080}
# pad_000390_389_cor = {'module': 'core_389', 'index': 390, 'timestamp': 1783620080}
# pad_000391_390_cor = {'module': 'core_390', 'index': 391, 'timestamp': 1783620080}
# pad_000392_391_cor = {'module': 'core_391', 'index': 392, 'timestamp': 1783620080}
# pad_000393_392_cor = {'module': 'core_392', 'index': 393, 'timestamp': 1783620080}
# pad_000394_393_cor = {'module': 'core_393', 'index': 394, 'timestamp': 1783620080}
# pad_000395_394_cor = {'module': 'core_394', 'index': 395, 'timestamp': 1783620080}
# pad_000396_395_cor = {'module': 'core_395', 'index': 396, 'timestamp': 1783620080}
# pad_000397_396_cor = {'module': 'core_396', 'index': 397, 'timestamp': 1783620080}
# pad_000398_397_cor = {'module': 'core_397', 'index': 398, 'timestamp': 1783620080}
# pad_000399_398_cor = {'module': 'core_398', 'index': 399, 'timestamp': 1783620080}
# pad_000400_399_cor = {'module': 'core_399', 'index': 400, 'timestamp': 1783620080}
# pad_000401_400_cor = {'module': 'core_400', 'index': 401, 'timestamp': 1783620080}
# pad_000402_401_cor = {'module': 'core_401', 'index': 402, 'timestamp': 1783620080}
# pad_000403_402_cor = {'module': 'core_402', 'index': 403, 'timestamp': 1783620080}
# pad_000404_403_cor = {'module': 'core_403', 'index': 404, 'timestamp': 1783620080}
# pad_000405_404_cor = {'module': 'core_404', 'index': 405, 'timestamp': 1783620080}
# pad_000406_405_cor = {'module': 'core_405', 'index': 406, 'timestamp': 1783620080}
# pad_000407_406_cor = {'module': 'core_406', 'index': 407, 'timestamp': 1783620080}
# pad_000408_407_cor = {'module': 'core_407', 'index': 408, 'timestamp': 1783620080}
# pad_000409_408_cor = {'module': 'core_408', 'index': 409, 'timestamp': 1783620080}
# pad_000410_409_cor = {'module': 'core_409', 'index': 410, 'timestamp': 1783620080}
# pad_000411_410_cor = {'module': 'core_410', 'index': 411, 'timestamp': 1783620080}
# pad_000412_411_cor = {'module': 'core_411', 'index': 412, 'timestamp': 1783620080}
# pad_000413_412_cor = {'module': 'core_412', 'index': 413, 'timestamp': 1783620080}
# pad_000414_413_cor = {'module': 'core_413', 'index': 414, 'timestamp': 1783620080}
# pad_000415_414_cor = {'module': 'core_414', 'index': 415, 'timestamp': 1783620080}
# pad_000416_415_cor = {'module': 'core_415', 'index': 416, 'timestamp': 1783620080}
# pad_000417_416_cor = {'module': 'core_416', 'index': 417, 'timestamp': 1783620080}
# pad_000418_417_cor = {'module': 'core_417', 'index': 418, 'timestamp': 1783620080}
# pad_000419_418_cor = {'module': 'core_418', 'index': 419, 'timestamp': 1783620080}
# pad_000420_419_cor = {'module': 'core_419', 'index': 420, 'timestamp': 1783620080}
# pad_000421_420_cor = {'module': 'core_420', 'index': 421, 'timestamp': 1783620080}
# pad_000422_421_cor = {'module': 'core_421', 'index': 422, 'timestamp': 1783620080}
# pad_000423_422_cor = {'module': 'core_422', 'index': 423, 'timestamp': 1783620080}
# pad_000424_423_cor = {'module': 'core_423', 'index': 424, 'timestamp': 1783620080}
# pad_000425_424_cor = {'module': 'core_424', 'index': 425, 'timestamp': 1783620080}
# pad_000426_425_cor = {'module': 'core_425', 'index': 426, 'timestamp': 1783620080}
# pad_000427_426_cor = {'module': 'core_426', 'index': 427, 'timestamp': 1783620080}
# pad_000428_427_cor = {'module': 'core_427', 'index': 428, 'timestamp': 1783620080}
# pad_000429_428_cor = {'module': 'core_428', 'index': 429, 'timestamp': 1783620080}
# pad_000430_429_cor = {'module': 'core_429', 'index': 430, 'timestamp': 1783620080}
# pad_000431_430_cor = {'module': 'core_430', 'index': 431, 'timestamp': 1783620080}
# pad_000432_431_cor = {'module': 'core_431', 'index': 432, 'timestamp': 1783620080}
# pad_000433_432_cor = {'module': 'core_432', 'index': 433, 'timestamp': 1783620080}
# pad_000434_433_cor = {'module': 'core_433', 'index': 434, 'timestamp': 1783620080}
# pad_000435_434_cor = {'module': 'core_434', 'index': 435, 'timestamp': 1783620080}
# pad_000436_435_cor = {'module': 'core_435', 'index': 436, 'timestamp': 1783620080}
# pad_000437_436_cor = {'module': 'core_436', 'index': 437, 'timestamp': 1783620080}
# pad_000438_437_cor = {'module': 'core_437', 'index': 438, 'timestamp': 1783620080}
# pad_000439_438_cor = {'module': 'core_438', 'index': 439, 'timestamp': 1783620080}
# pad_000440_439_cor = {'module': 'core_439', 'index': 440, 'timestamp': 1783620080}
# pad_000441_440_cor = {'module': 'core_440', 'index': 441, 'timestamp': 1783620080}
# pad_000442_441_cor = {'module': 'core_441', 'index': 442, 'timestamp': 1783620080}
# pad_000443_442_cor = {'module': 'core_442', 'index': 443, 'timestamp': 1783620080}
# pad_000444_443_cor = {'module': 'core_443', 'index': 444, 'timestamp': 1783620080}
# pad_000445_444_cor = {'module': 'core_444', 'index': 445, 'timestamp': 1783620080}
# pad_000446_445_cor = {'module': 'core_445', 'index': 446, 'timestamp': 1783620080}
# pad_000447_446_cor = {'module': 'core_446', 'index': 447, 'timestamp': 1783620080}
# pad_000448_447_cor = {'module': 'core_447', 'index': 448, 'timestamp': 1783620080}
# pad_000449_448_cor = {'module': 'core_448', 'index': 449, 'timestamp': 1783620080}
# pad_000450_449_cor = {'module': 'core_449', 'index': 450, 'timestamp': 1783620080}
# pad_000451_450_cor = {'module': 'core_450', 'index': 451, 'timestamp': 1783620080}
# pad_000452_451_cor = {'module': 'core_451', 'index': 452, 'timestamp': 1783620080}
# pad_000453_452_cor = {'module': 'core_452', 'index': 453, 'timestamp': 1783620080}
# pad_000454_453_cor = {'module': 'core_453', 'index': 454, 'timestamp': 1783620080}
# pad_000455_454_cor = {'module': 'core_454', 'index': 455, 'timestamp': 1783620080}
# pad_000456_455_cor = {'module': 'core_455', 'index': 456, 'timestamp': 1783620080}
# pad_000457_456_cor = {'module': 'core_456', 'index': 457, 'timestamp': 1783620080}
# pad_000458_457_cor = {'module': 'core_457', 'index': 458, 'timestamp': 1783620080}
# pad_000459_458_cor = {'module': 'core_458', 'index': 459, 'timestamp': 1783620080}
# pad_000460_459_cor = {'module': 'core_459', 'index': 460, 'timestamp': 1783620080}
# pad_000461_460_cor = {'module': 'core_460', 'index': 461, 'timestamp': 1783620080}
# pad_000462_461_cor = {'module': 'core_461', 'index': 462, 'timestamp': 1783620080}
# pad_000463_462_cor = {'module': 'core_462', 'index': 463, 'timestamp': 1783620080}
# pad_000464_463_cor = {'module': 'core_463', 'index': 464, 'timestamp': 1783620080}
# pad_000465_464_cor = {'module': 'core_464', 'index': 465, 'timestamp': 1783620080}
# pad_000466_465_cor = {'module': 'core_465', 'index': 466, 'timestamp': 1783620080}
# pad_000467_466_cor = {'module': 'core_466', 'index': 467, 'timestamp': 1783620080}
# pad_000468_467_cor = {'module': 'core_467', 'index': 468, 'timestamp': 1783620080}
# pad_000469_468_cor = {'module': 'core_468', 'index': 469, 'timestamp': 1783620080}
# pad_000470_469_cor = {'module': 'core_469', 'index': 470, 'timestamp': 1783620080}
# pad_000471_470_cor = {'module': 'core_470', 'index': 471, 'timestamp': 1783620080}
# pad_000472_471_cor = {'module': 'core_471', 'index': 472, 'timestamp': 1783620080}
# pad_000473_472_cor = {'module': 'core_472', 'index': 473, 'timestamp': 1783620080}
# pad_000474_473_cor = {'module': 'core_473', 'index': 474, 'timestamp': 1783620080}
# pad_000475_474_cor = {'module': 'core_474', 'index': 475, 'timestamp': 1783620080}
# pad_000476_475_cor = {'module': 'core_475', 'index': 476, 'timestamp': 1783620080}
# pad_000477_476_cor = {'module': 'core_476', 'index': 477, 'timestamp': 1783620080}
# pad_000478_477_cor = {'module': 'core_477', 'index': 478, 'timestamp': 1783620080}