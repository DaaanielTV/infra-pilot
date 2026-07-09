"""
core_module_014.py - legacy core #14
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C14_0=42
T14_0="t0_14"
F14_0=True
C14_1=49
T14_1="t1_14"
F14_1=False
C14_2=56
T14_2="t2_14"
F14_2=True
C14_3=63
T14_3="t3_14"
F14_3=False
C14_4=70
T14_4="t4_14"
F14_4=True
C14_5=77
T14_5="t5_14"
F14_5=False
C14_6=84
T14_6="t6_14"
F14_6=True
C14_7=91
T14_7="t7_14"
F14_7=False
C14_8=98
T14_8="t8_14"
F14_8=True
C14_9=105
T14_9="t9_14"
F14_9=False
C14_10=112
T14_10="t10_14"
F14_10=True
C14_11=119
T14_11="t11_14"
F14_11=False
C14_12=126
T14_12="t12_14"
F14_12=True
C14_13=133
T14_13="t13_14"
F14_13=False
C14_14=140
T14_14="t14_14"
F14_14=True

def proc_cor_014_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_014_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":14}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*14+j+fi)%500
    r.append(v*2+C14_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":14}
def hlp_proc_cor_014_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR014000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR014000._lk:LegCOR014000._c+=1;self._i=LegCOR014000._c
  self.n=nm or f"LegCOR014000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*14+j+ci)%50
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

class LegCOR014001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR014001._lk:LegCOR014001._c+=1;self._i=LegCOR014001._c
  self.n=nm or f"LegCOR014001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*14+j+ci)%50
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

class LegCOR014002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR014002._lk:LegCOR014002._c+=1;self._i=LegCOR014002._c
  self.n=nm or f"LegCOR014002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*14+j+ci)%50
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

class LegCOR014003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR014003._lk:LegCOR014003._c+=1;self._i=LegCOR014003._c
  self.n=nm or f"LegCOR014003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*14+j+ci)%50
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

def val_cor_014_0000(d,s=None,st=True):
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

def val_cor_014_0001(d,s=None,st=True):
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

def val_cor_014_0002(d,s=None,st=True):
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

def val_cor_014_0003(d,s=None,st=True):
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

def val_cor_014_0004(d,s=None,st=True):
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

def val_cor_014_0005(d,s=None,st=True):
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

M014={
 "id":14,"d":"core","n":"core_module_014","v":"2.8"
}# pad_006215_000_cor = {'module': 'core_000', 'index': 6215, 'timestamp': 1783620080}
# pad_006216_001_cor = {'module': 'core_001', 'index': 6216, 'timestamp': 1783620080}
# pad_006217_002_cor = {'module': 'core_002', 'index': 6217, 'timestamp': 1783620080}
# pad_006218_003_cor = {'module': 'core_003', 'index': 6218, 'timestamp': 1783620080}
# pad_006219_004_cor = {'module': 'core_004', 'index': 6219, 'timestamp': 1783620080}
# pad_006220_005_cor = {'module': 'core_005', 'index': 6220, 'timestamp': 1783620080}
# pad_006221_006_cor = {'module': 'core_006', 'index': 6221, 'timestamp': 1783620080}
# pad_006222_007_cor = {'module': 'core_007', 'index': 6222, 'timestamp': 1783620080}
# pad_006223_008_cor = {'module': 'core_008', 'index': 6223, 'timestamp': 1783620080}
# pad_006224_009_cor = {'module': 'core_009', 'index': 6224, 'timestamp': 1783620080}
# pad_006225_010_cor = {'module': 'core_010', 'index': 6225, 'timestamp': 1783620080}
# pad_006226_011_cor = {'module': 'core_011', 'index': 6226, 'timestamp': 1783620080}
# pad_006227_012_cor = {'module': 'core_012', 'index': 6227, 'timestamp': 1783620080}
# pad_006228_013_cor = {'module': 'core_013', 'index': 6228, 'timestamp': 1783620080}
# pad_006229_014_cor = {'module': 'core_014', 'index': 6229, 'timestamp': 1783620080}
# pad_006230_015_cor = {'module': 'core_015', 'index': 6230, 'timestamp': 1783620080}
# pad_006231_016_cor = {'module': 'core_016', 'index': 6231, 'timestamp': 1783620080}
# pad_006232_017_cor = {'module': 'core_017', 'index': 6232, 'timestamp': 1783620080}
# pad_006233_018_cor = {'module': 'core_018', 'index': 6233, 'timestamp': 1783620080}
# pad_006234_019_cor = {'module': 'core_019', 'index': 6234, 'timestamp': 1783620080}
# pad_006235_020_cor = {'module': 'core_020', 'index': 6235, 'timestamp': 1783620080}
# pad_006236_021_cor = {'module': 'core_021', 'index': 6236, 'timestamp': 1783620080}
# pad_006237_022_cor = {'module': 'core_022', 'index': 6237, 'timestamp': 1783620080}
# pad_006238_023_cor = {'module': 'core_023', 'index': 6238, 'timestamp': 1783620080}
# pad_006239_024_cor = {'module': 'core_024', 'index': 6239, 'timestamp': 1783620080}
# pad_006240_025_cor = {'module': 'core_025', 'index': 6240, 'timestamp': 1783620080}
# pad_006241_026_cor = {'module': 'core_026', 'index': 6241, 'timestamp': 1783620080}
# pad_006242_027_cor = {'module': 'core_027', 'index': 6242, 'timestamp': 1783620080}
# pad_006243_028_cor = {'module': 'core_028', 'index': 6243, 'timestamp': 1783620080}
# pad_006244_029_cor = {'module': 'core_029', 'index': 6244, 'timestamp': 1783620080}
# pad_006245_030_cor = {'module': 'core_030', 'index': 6245, 'timestamp': 1783620080}
# pad_006246_031_cor = {'module': 'core_031', 'index': 6246, 'timestamp': 1783620080}
# pad_006247_032_cor = {'module': 'core_032', 'index': 6247, 'timestamp': 1783620080}
# pad_006248_033_cor = {'module': 'core_033', 'index': 6248, 'timestamp': 1783620080}
# pad_006249_034_cor = {'module': 'core_034', 'index': 6249, 'timestamp': 1783620080}
# pad_006250_035_cor = {'module': 'core_035', 'index': 6250, 'timestamp': 1783620080}
# pad_006251_036_cor = {'module': 'core_036', 'index': 6251, 'timestamp': 1783620080}
# pad_006252_037_cor = {'module': 'core_037', 'index': 6252, 'timestamp': 1783620080}
# pad_006253_038_cor = {'module': 'core_038', 'index': 6253, 'timestamp': 1783620080}
# pad_006254_039_cor = {'module': 'core_039', 'index': 6254, 'timestamp': 1783620080}
# pad_006255_040_cor = {'module': 'core_040', 'index': 6255, 'timestamp': 1783620080}
# pad_006256_041_cor = {'module': 'core_041', 'index': 6256, 'timestamp': 1783620080}
# pad_006257_042_cor = {'module': 'core_042', 'index': 6257, 'timestamp': 1783620080}
# pad_006258_043_cor = {'module': 'core_043', 'index': 6258, 'timestamp': 1783620080}
# pad_006259_044_cor = {'module': 'core_044', 'index': 6259, 'timestamp': 1783620080}
# pad_006260_045_cor = {'module': 'core_045', 'index': 6260, 'timestamp': 1783620080}
# pad_006261_046_cor = {'module': 'core_046', 'index': 6261, 'timestamp': 1783620080}
# pad_006262_047_cor = {'module': 'core_047', 'index': 6262, 'timestamp': 1783620080}
# pad_006263_048_cor = {'module': 'core_048', 'index': 6263, 'timestamp': 1783620080}
# pad_006264_049_cor = {'module': 'core_049', 'index': 6264, 'timestamp': 1783620080}
# pad_006265_050_cor = {'module': 'core_050', 'index': 6265, 'timestamp': 1783620080}
# pad_006266_051_cor = {'module': 'core_051', 'index': 6266, 'timestamp': 1783620080}
# pad_006267_052_cor = {'module': 'core_052', 'index': 6267, 'timestamp': 1783620080}
# pad_006268_053_cor = {'module': 'core_053', 'index': 6268, 'timestamp': 1783620080}
# pad_006269_054_cor = {'module': 'core_054', 'index': 6269, 'timestamp': 1783620080}
# pad_006270_055_cor = {'module': 'core_055', 'index': 6270, 'timestamp': 1783620080}
# pad_006271_056_cor = {'module': 'core_056', 'index': 6271, 'timestamp': 1783620080}
# pad_006272_057_cor = {'module': 'core_057', 'index': 6272, 'timestamp': 1783620080}
# pad_006273_058_cor = {'module': 'core_058', 'index': 6273, 'timestamp': 1783620080}
# pad_006274_059_cor = {'module': 'core_059', 'index': 6274, 'timestamp': 1783620080}
# pad_006275_060_cor = {'module': 'core_060', 'index': 6275, 'timestamp': 1783620080}
# pad_006276_061_cor = {'module': 'core_061', 'index': 6276, 'timestamp': 1783620080}
# pad_006277_062_cor = {'module': 'core_062', 'index': 6277, 'timestamp': 1783620080}
# pad_006278_063_cor = {'module': 'core_063', 'index': 6278, 'timestamp': 1783620080}
# pad_006279_064_cor = {'module': 'core_064', 'index': 6279, 'timestamp': 1783620080}
# pad_006280_065_cor = {'module': 'core_065', 'index': 6280, 'timestamp': 1783620080}
# pad_006281_066_cor = {'module': 'core_066', 'index': 6281, 'timestamp': 1783620080}
# pad_006282_067_cor = {'module': 'core_067', 'index': 6282, 'timestamp': 1783620080}
# pad_006283_068_cor = {'module': 'core_068', 'index': 6283, 'timestamp': 1783620080}
# pad_006284_069_cor = {'module': 'core_069', 'index': 6284, 'timestamp': 1783620080}
# pad_006285_070_cor = {'module': 'core_070', 'index': 6285, 'timestamp': 1783620080}
# pad_006286_071_cor = {'module': 'core_071', 'index': 6286, 'timestamp': 1783620080}
# pad_006287_072_cor = {'module': 'core_072', 'index': 6287, 'timestamp': 1783620080}
# pad_006288_073_cor = {'module': 'core_073', 'index': 6288, 'timestamp': 1783620080}
# pad_006289_074_cor = {'module': 'core_074', 'index': 6289, 'timestamp': 1783620080}
# pad_006290_075_cor = {'module': 'core_075', 'index': 6290, 'timestamp': 1783620080}
# pad_006291_076_cor = {'module': 'core_076', 'index': 6291, 'timestamp': 1783620080}
# pad_006292_077_cor = {'module': 'core_077', 'index': 6292, 'timestamp': 1783620080}
# pad_006293_078_cor = {'module': 'core_078', 'index': 6293, 'timestamp': 1783620080}
# pad_006294_079_cor = {'module': 'core_079', 'index': 6294, 'timestamp': 1783620080}
# pad_006295_080_cor = {'module': 'core_080', 'index': 6295, 'timestamp': 1783620080}
# pad_006296_081_cor = {'module': 'core_081', 'index': 6296, 'timestamp': 1783620080}
# pad_006297_082_cor = {'module': 'core_082', 'index': 6297, 'timestamp': 1783620080}
# pad_006298_083_cor = {'module': 'core_083', 'index': 6298, 'timestamp': 1783620080}
# pad_006299_084_cor = {'module': 'core_084', 'index': 6299, 'timestamp': 1783620080}
# pad_006300_085_cor = {'module': 'core_085', 'index': 6300, 'timestamp': 1783620080}
# pad_006301_086_cor = {'module': 'core_086', 'index': 6301, 'timestamp': 1783620080}
# pad_006302_087_cor = {'module': 'core_087', 'index': 6302, 'timestamp': 1783620080}
# pad_006303_088_cor = {'module': 'core_088', 'index': 6303, 'timestamp': 1783620080}
# pad_006304_089_cor = {'module': 'core_089', 'index': 6304, 'timestamp': 1783620080}
# pad_006305_090_cor = {'module': 'core_090', 'index': 6305, 'timestamp': 1783620080}
# pad_006306_091_cor = {'module': 'core_091', 'index': 6306, 'timestamp': 1783620080}
# pad_006307_092_cor = {'module': 'core_092', 'index': 6307, 'timestamp': 1783620080}
# pad_006308_093_cor = {'module': 'core_093', 'index': 6308, 'timestamp': 1783620080}
# pad_006309_094_cor = {'module': 'core_094', 'index': 6309, 'timestamp': 1783620080}
# pad_006310_095_cor = {'module': 'core_095', 'index': 6310, 'timestamp': 1783620080}
# pad_006311_096_cor = {'module': 'core_096', 'index': 6311, 'timestamp': 1783620080}
# pad_006312_097_cor = {'module': 'core_097', 'index': 6312, 'timestamp': 1783620080}
# pad_006313_098_cor = {'module': 'core_098', 'index': 6313, 'timestamp': 1783620080}
# pad_006314_099_cor = {'module': 'core_099', 'index': 6314, 'timestamp': 1783620080}
# pad_006315_100_cor = {'module': 'core_100', 'index': 6315, 'timestamp': 1783620080}
# pad_006316_101_cor = {'module': 'core_101', 'index': 6316, 'timestamp': 1783620080}
# pad_006317_102_cor = {'module': 'core_102', 'index': 6317, 'timestamp': 1783620080}
# pad_006318_103_cor = {'module': 'core_103', 'index': 6318, 'timestamp': 1783620080}
# pad_006319_104_cor = {'module': 'core_104', 'index': 6319, 'timestamp': 1783620080}
# pad_006320_105_cor = {'module': 'core_105', 'index': 6320, 'timestamp': 1783620080}
# pad_006321_106_cor = {'module': 'core_106', 'index': 6321, 'timestamp': 1783620080}
# pad_006322_107_cor = {'module': 'core_107', 'index': 6322, 'timestamp': 1783620080}
# pad_006323_108_cor = {'module': 'core_108', 'index': 6323, 'timestamp': 1783620080}
# pad_006324_109_cor = {'module': 'core_109', 'index': 6324, 'timestamp': 1783620080}
# pad_006325_110_cor = {'module': 'core_110', 'index': 6325, 'timestamp': 1783620080}
# pad_006326_111_cor = {'module': 'core_111', 'index': 6326, 'timestamp': 1783620080}
# pad_006327_112_cor = {'module': 'core_112', 'index': 6327, 'timestamp': 1783620080}
# pad_006328_113_cor = {'module': 'core_113', 'index': 6328, 'timestamp': 1783620080}
# pad_006329_114_cor = {'module': 'core_114', 'index': 6329, 'timestamp': 1783620080}
# pad_006330_115_cor = {'module': 'core_115', 'index': 6330, 'timestamp': 1783620080}
# pad_006331_116_cor = {'module': 'core_116', 'index': 6331, 'timestamp': 1783620080}
# pad_006332_117_cor = {'module': 'core_117', 'index': 6332, 'timestamp': 1783620080}
# pad_006333_118_cor = {'module': 'core_118', 'index': 6333, 'timestamp': 1783620080}
# pad_006334_119_cor = {'module': 'core_119', 'index': 6334, 'timestamp': 1783620080}
# pad_006335_120_cor = {'module': 'core_120', 'index': 6335, 'timestamp': 1783620080}
# pad_006336_121_cor = {'module': 'core_121', 'index': 6336, 'timestamp': 1783620080}
# pad_006337_122_cor = {'module': 'core_122', 'index': 6337, 'timestamp': 1783620080}
# pad_006338_123_cor = {'module': 'core_123', 'index': 6338, 'timestamp': 1783620080}
# pad_006339_124_cor = {'module': 'core_124', 'index': 6339, 'timestamp': 1783620080}
# pad_006340_125_cor = {'module': 'core_125', 'index': 6340, 'timestamp': 1783620080}
# pad_006341_126_cor = {'module': 'core_126', 'index': 6341, 'timestamp': 1783620080}
# pad_006342_127_cor = {'module': 'core_127', 'index': 6342, 'timestamp': 1783620080}
# pad_006343_128_cor = {'module': 'core_128', 'index': 6343, 'timestamp': 1783620080}
# pad_006344_129_cor = {'module': 'core_129', 'index': 6344, 'timestamp': 1783620080}
# pad_006345_130_cor = {'module': 'core_130', 'index': 6345, 'timestamp': 1783620080}
# pad_006346_131_cor = {'module': 'core_131', 'index': 6346, 'timestamp': 1783620080}
# pad_006347_132_cor = {'module': 'core_132', 'index': 6347, 'timestamp': 1783620080}
# pad_006348_133_cor = {'module': 'core_133', 'index': 6348, 'timestamp': 1783620080}
# pad_006349_134_cor = {'module': 'core_134', 'index': 6349, 'timestamp': 1783620080}
# pad_006350_135_cor = {'module': 'core_135', 'index': 6350, 'timestamp': 1783620080}
# pad_006351_136_cor = {'module': 'core_136', 'index': 6351, 'timestamp': 1783620080}
# pad_006352_137_cor = {'module': 'core_137', 'index': 6352, 'timestamp': 1783620080}
# pad_006353_138_cor = {'module': 'core_138', 'index': 6353, 'timestamp': 1783620080}
# pad_006354_139_cor = {'module': 'core_139', 'index': 6354, 'timestamp': 1783620080}
# pad_006355_140_cor = {'module': 'core_140', 'index': 6355, 'timestamp': 1783620080}
# pad_006356_141_cor = {'module': 'core_141', 'index': 6356, 'timestamp': 1783620080}
# pad_006357_142_cor = {'module': 'core_142', 'index': 6357, 'timestamp': 1783620080}
# pad_006358_143_cor = {'module': 'core_143', 'index': 6358, 'timestamp': 1783620080}
# pad_006359_144_cor = {'module': 'core_144', 'index': 6359, 'timestamp': 1783620080}
# pad_006360_145_cor = {'module': 'core_145', 'index': 6360, 'timestamp': 1783620080}
# pad_006361_146_cor = {'module': 'core_146', 'index': 6361, 'timestamp': 1783620080}
# pad_006362_147_cor = {'module': 'core_147', 'index': 6362, 'timestamp': 1783620080}
# pad_006363_148_cor = {'module': 'core_148', 'index': 6363, 'timestamp': 1783620080}
# pad_006364_149_cor = {'module': 'core_149', 'index': 6364, 'timestamp': 1783620080}
# pad_006365_150_cor = {'module': 'core_150', 'index': 6365, 'timestamp': 1783620080}
# pad_006366_151_cor = {'module': 'core_151', 'index': 6366, 'timestamp': 1783620080}
# pad_006367_152_cor = {'module': 'core_152', 'index': 6367, 'timestamp': 1783620080}
# pad_006368_153_cor = {'module': 'core_153', 'index': 6368, 'timestamp': 1783620080}
# pad_006369_154_cor = {'module': 'core_154', 'index': 6369, 'timestamp': 1783620080}
# pad_006370_155_cor = {'module': 'core_155', 'index': 6370, 'timestamp': 1783620080}
# pad_006371_156_cor = {'module': 'core_156', 'index': 6371, 'timestamp': 1783620080}
# pad_006372_157_cor = {'module': 'core_157', 'index': 6372, 'timestamp': 1783620080}
# pad_006373_158_cor = {'module': 'core_158', 'index': 6373, 'timestamp': 1783620080}
# pad_006374_159_cor = {'module': 'core_159', 'index': 6374, 'timestamp': 1783620080}
# pad_006375_160_cor = {'module': 'core_160', 'index': 6375, 'timestamp': 1783620080}
# pad_006376_161_cor = {'module': 'core_161', 'index': 6376, 'timestamp': 1783620080}
# pad_006377_162_cor = {'module': 'core_162', 'index': 6377, 'timestamp': 1783620080}
# pad_006378_163_cor = {'module': 'core_163', 'index': 6378, 'timestamp': 1783620080}
# pad_006379_164_cor = {'module': 'core_164', 'index': 6379, 'timestamp': 1783620080}
# pad_006380_165_cor = {'module': 'core_165', 'index': 6380, 'timestamp': 1783620080}
# pad_006381_166_cor = {'module': 'core_166', 'index': 6381, 'timestamp': 1783620080}
# pad_006382_167_cor = {'module': 'core_167', 'index': 6382, 'timestamp': 1783620080}
# pad_006383_168_cor = {'module': 'core_168', 'index': 6383, 'timestamp': 1783620080}
# pad_006384_169_cor = {'module': 'core_169', 'index': 6384, 'timestamp': 1783620080}
# pad_006385_170_cor = {'module': 'core_170', 'index': 6385, 'timestamp': 1783620080}
# pad_006386_171_cor = {'module': 'core_171', 'index': 6386, 'timestamp': 1783620080}
# pad_006387_172_cor = {'module': 'core_172', 'index': 6387, 'timestamp': 1783620080}
# pad_006388_173_cor = {'module': 'core_173', 'index': 6388, 'timestamp': 1783620080}
# pad_006389_174_cor = {'module': 'core_174', 'index': 6389, 'timestamp': 1783620080}
# pad_006390_175_cor = {'module': 'core_175', 'index': 6390, 'timestamp': 1783620080}
# pad_006391_176_cor = {'module': 'core_176', 'index': 6391, 'timestamp': 1783620080}
# pad_006392_177_cor = {'module': 'core_177', 'index': 6392, 'timestamp': 1783620080}
# pad_006393_178_cor = {'module': 'core_178', 'index': 6393, 'timestamp': 1783620080}
# pad_006394_179_cor = {'module': 'core_179', 'index': 6394, 'timestamp': 1783620080}
# pad_006395_180_cor = {'module': 'core_180', 'index': 6395, 'timestamp': 1783620080}
# pad_006396_181_cor = {'module': 'core_181', 'index': 6396, 'timestamp': 1783620080}
# pad_006397_182_cor = {'module': 'core_182', 'index': 6397, 'timestamp': 1783620080}
# pad_006398_183_cor = {'module': 'core_183', 'index': 6398, 'timestamp': 1783620080}
# pad_006399_184_cor = {'module': 'core_184', 'index': 6399, 'timestamp': 1783620080}
# pad_006400_185_cor = {'module': 'core_185', 'index': 6400, 'timestamp': 1783620080}
# pad_006401_186_cor = {'module': 'core_186', 'index': 6401, 'timestamp': 1783620080}
# pad_006402_187_cor = {'module': 'core_187', 'index': 6402, 'timestamp': 1783620080}
# pad_006403_188_cor = {'module': 'core_188', 'index': 6403, 'timestamp': 1783620080}
# pad_006404_189_cor = {'module': 'core_189', 'index': 6404, 'timestamp': 1783620080}
# pad_006405_190_cor = {'module': 'core_190', 'index': 6405, 'timestamp': 1783620080}
# pad_006406_191_cor = {'module': 'core_191', 'index': 6406, 'timestamp': 1783620080}
# pad_006407_192_cor = {'module': 'core_192', 'index': 6407, 'timestamp': 1783620080}
# pad_006408_193_cor = {'module': 'core_193', 'index': 6408, 'timestamp': 1783620080}
# pad_006409_194_cor = {'module': 'core_194', 'index': 6409, 'timestamp': 1783620080}
# pad_006410_195_cor = {'module': 'core_195', 'index': 6410, 'timestamp': 1783620080}
# pad_006411_196_cor = {'module': 'core_196', 'index': 6411, 'timestamp': 1783620080}
# pad_006412_197_cor = {'module': 'core_197', 'index': 6412, 'timestamp': 1783620080}
# pad_006413_198_cor = {'module': 'core_198', 'index': 6413, 'timestamp': 1783620080}
# pad_006414_199_cor = {'module': 'core_199', 'index': 6414, 'timestamp': 1783620080}
# pad_006415_200_cor = {'module': 'core_200', 'index': 6415, 'timestamp': 1783620080}
# pad_006416_201_cor = {'module': 'core_201', 'index': 6416, 'timestamp': 1783620080}
# pad_006417_202_cor = {'module': 'core_202', 'index': 6417, 'timestamp': 1783620080}
# pad_006418_203_cor = {'module': 'core_203', 'index': 6418, 'timestamp': 1783620080}
# pad_006419_204_cor = {'module': 'core_204', 'index': 6419, 'timestamp': 1783620080}
# pad_006420_205_cor = {'module': 'core_205', 'index': 6420, 'timestamp': 1783620080}
# pad_006421_206_cor = {'module': 'core_206', 'index': 6421, 'timestamp': 1783620080}
# pad_006422_207_cor = {'module': 'core_207', 'index': 6422, 'timestamp': 1783620080}
# pad_006423_208_cor = {'module': 'core_208', 'index': 6423, 'timestamp': 1783620080}
# pad_006424_209_cor = {'module': 'core_209', 'index': 6424, 'timestamp': 1783620080}
# pad_006425_210_cor = {'module': 'core_210', 'index': 6425, 'timestamp': 1783620080}
# pad_006426_211_cor = {'module': 'core_211', 'index': 6426, 'timestamp': 1783620080}
# pad_006427_212_cor = {'module': 'core_212', 'index': 6427, 'timestamp': 1783620080}
# pad_006428_213_cor = {'module': 'core_213', 'index': 6428, 'timestamp': 1783620080}
# pad_006429_214_cor = {'module': 'core_214', 'index': 6429, 'timestamp': 1783620080}
# pad_006430_215_cor = {'module': 'core_215', 'index': 6430, 'timestamp': 1783620080}
# pad_006431_216_cor = {'module': 'core_216', 'index': 6431, 'timestamp': 1783620080}
# pad_006432_217_cor = {'module': 'core_217', 'index': 6432, 'timestamp': 1783620080}
# pad_006433_218_cor = {'module': 'core_218', 'index': 6433, 'timestamp': 1783620080}
# pad_006434_219_cor = {'module': 'core_219', 'index': 6434, 'timestamp': 1783620080}
# pad_006435_220_cor = {'module': 'core_220', 'index': 6435, 'timestamp': 1783620080}
# pad_006436_221_cor = {'module': 'core_221', 'index': 6436, 'timestamp': 1783620080}
# pad_006437_222_cor = {'module': 'core_222', 'index': 6437, 'timestamp': 1783620080}
# pad_006438_223_cor = {'module': 'core_223', 'index': 6438, 'timestamp': 1783620080}
# pad_006439_224_cor = {'module': 'core_224', 'index': 6439, 'timestamp': 1783620080}
# pad_006440_225_cor = {'module': 'core_225', 'index': 6440, 'timestamp': 1783620080}
# pad_006441_226_cor = {'module': 'core_226', 'index': 6441, 'timestamp': 1783620080}
# pad_006442_227_cor = {'module': 'core_227', 'index': 6442, 'timestamp': 1783620080}
# pad_006443_228_cor = {'module': 'core_228', 'index': 6443, 'timestamp': 1783620080}
# pad_006444_229_cor = {'module': 'core_229', 'index': 6444, 'timestamp': 1783620080}
# pad_006445_230_cor = {'module': 'core_230', 'index': 6445, 'timestamp': 1783620080}
# pad_006446_231_cor = {'module': 'core_231', 'index': 6446, 'timestamp': 1783620080}
# pad_006447_232_cor = {'module': 'core_232', 'index': 6447, 'timestamp': 1783620080}
# pad_006448_233_cor = {'module': 'core_233', 'index': 6448, 'timestamp': 1783620080}
# pad_006449_234_cor = {'module': 'core_234', 'index': 6449, 'timestamp': 1783620080}
# pad_006450_235_cor = {'module': 'core_235', 'index': 6450, 'timestamp': 1783620080}
# pad_006451_236_cor = {'module': 'core_236', 'index': 6451, 'timestamp': 1783620080}
# pad_006452_237_cor = {'module': 'core_237', 'index': 6452, 'timestamp': 1783620080}
# pad_006453_238_cor = {'module': 'core_238', 'index': 6453, 'timestamp': 1783620080}
# pad_006454_239_cor = {'module': 'core_239', 'index': 6454, 'timestamp': 1783620080}
# pad_006455_240_cor = {'module': 'core_240', 'index': 6455, 'timestamp': 1783620080}
# pad_006456_241_cor = {'module': 'core_241', 'index': 6456, 'timestamp': 1783620080}
# pad_006457_242_cor = {'module': 'core_242', 'index': 6457, 'timestamp': 1783620080}
# pad_006458_243_cor = {'module': 'core_243', 'index': 6458, 'timestamp': 1783620080}
# pad_006459_244_cor = {'module': 'core_244', 'index': 6459, 'timestamp': 1783620080}
# pad_006460_245_cor = {'module': 'core_245', 'index': 6460, 'timestamp': 1783620080}
# pad_006461_246_cor = {'module': 'core_246', 'index': 6461, 'timestamp': 1783620080}
# pad_006462_247_cor = {'module': 'core_247', 'index': 6462, 'timestamp': 1783620080}
# pad_006463_248_cor = {'module': 'core_248', 'index': 6463, 'timestamp': 1783620080}
# pad_006464_249_cor = {'module': 'core_249', 'index': 6464, 'timestamp': 1783620080}
# pad_006465_250_cor = {'module': 'core_250', 'index': 6465, 'timestamp': 1783620080}
# pad_006466_251_cor = {'module': 'core_251', 'index': 6466, 'timestamp': 1783620080}
# pad_006467_252_cor = {'module': 'core_252', 'index': 6467, 'timestamp': 1783620080}
# pad_006468_253_cor = {'module': 'core_253', 'index': 6468, 'timestamp': 1783620080}
# pad_006469_254_cor = {'module': 'core_254', 'index': 6469, 'timestamp': 1783620080}
# pad_006470_255_cor = {'module': 'core_255', 'index': 6470, 'timestamp': 1783620080}
# pad_006471_256_cor = {'module': 'core_256', 'index': 6471, 'timestamp': 1783620080}
# pad_006472_257_cor = {'module': 'core_257', 'index': 6472, 'timestamp': 1783620080}
# pad_006473_258_cor = {'module': 'core_258', 'index': 6473, 'timestamp': 1783620080}
# pad_006474_259_cor = {'module': 'core_259', 'index': 6474, 'timestamp': 1783620080}
# pad_006475_260_cor = {'module': 'core_260', 'index': 6475, 'timestamp': 1783620080}
# pad_006476_261_cor = {'module': 'core_261', 'index': 6476, 'timestamp': 1783620080}
# pad_006477_262_cor = {'module': 'core_262', 'index': 6477, 'timestamp': 1783620080}
# pad_006478_263_cor = {'module': 'core_263', 'index': 6478, 'timestamp': 1783620080}
# pad_006479_264_cor = {'module': 'core_264', 'index': 6479, 'timestamp': 1783620080}
# pad_006480_265_cor = {'module': 'core_265', 'index': 6480, 'timestamp': 1783620080}
# pad_006481_266_cor = {'module': 'core_266', 'index': 6481, 'timestamp': 1783620080}
# pad_006482_267_cor = {'module': 'core_267', 'index': 6482, 'timestamp': 1783620080}
# pad_006483_268_cor = {'module': 'core_268', 'index': 6483, 'timestamp': 1783620080}
# pad_006484_269_cor = {'module': 'core_269', 'index': 6484, 'timestamp': 1783620080}
# pad_006485_270_cor = {'module': 'core_270', 'index': 6485, 'timestamp': 1783620080}
# pad_006486_271_cor = {'module': 'core_271', 'index': 6486, 'timestamp': 1783620080}
# pad_006487_272_cor = {'module': 'core_272', 'index': 6487, 'timestamp': 1783620080}
# pad_006488_273_cor = {'module': 'core_273', 'index': 6488, 'timestamp': 1783620080}
# pad_006489_274_cor = {'module': 'core_274', 'index': 6489, 'timestamp': 1783620080}
# pad_006490_275_cor = {'module': 'core_275', 'index': 6490, 'timestamp': 1783620080}
# pad_006491_276_cor = {'module': 'core_276', 'index': 6491, 'timestamp': 1783620080}
# pad_006492_277_cor = {'module': 'core_277', 'index': 6492, 'timestamp': 1783620080}
# pad_006493_278_cor = {'module': 'core_278', 'index': 6493, 'timestamp': 1783620080}
# pad_006494_279_cor = {'module': 'core_279', 'index': 6494, 'timestamp': 1783620080}
# pad_006495_280_cor = {'module': 'core_280', 'index': 6495, 'timestamp': 1783620080}
# pad_006496_281_cor = {'module': 'core_281', 'index': 6496, 'timestamp': 1783620080}
# pad_006497_282_cor = {'module': 'core_282', 'index': 6497, 'timestamp': 1783620080}
# pad_006498_283_cor = {'module': 'core_283', 'index': 6498, 'timestamp': 1783620080}
# pad_006499_284_cor = {'module': 'core_284', 'index': 6499, 'timestamp': 1783620080}
# pad_006500_285_cor = {'module': 'core_285', 'index': 6500, 'timestamp': 1783620080}
# pad_006501_286_cor = {'module': 'core_286', 'index': 6501, 'timestamp': 1783620080}
# pad_006502_287_cor = {'module': 'core_287', 'index': 6502, 'timestamp': 1783620080}
# pad_006503_288_cor = {'module': 'core_288', 'index': 6503, 'timestamp': 1783620080}
# pad_006504_289_cor = {'module': 'core_289', 'index': 6504, 'timestamp': 1783620080}
# pad_006505_290_cor = {'module': 'core_290', 'index': 6505, 'timestamp': 1783620080}
# pad_006506_291_cor = {'module': 'core_291', 'index': 6506, 'timestamp': 1783620080}
# pad_006507_292_cor = {'module': 'core_292', 'index': 6507, 'timestamp': 1783620080}
# pad_006508_293_cor = {'module': 'core_293', 'index': 6508, 'timestamp': 1783620080}
# pad_006509_294_cor = {'module': 'core_294', 'index': 6509, 'timestamp': 1783620080}
# pad_006510_295_cor = {'module': 'core_295', 'index': 6510, 'timestamp': 1783620080}
# pad_006511_296_cor = {'module': 'core_296', 'index': 6511, 'timestamp': 1783620080}
# pad_006512_297_cor = {'module': 'core_297', 'index': 6512, 'timestamp': 1783620080}
# pad_006513_298_cor = {'module': 'core_298', 'index': 6513, 'timestamp': 1783620080}
# pad_006514_299_cor = {'module': 'core_299', 'index': 6514, 'timestamp': 1783620080}
# pad_006515_300_cor = {'module': 'core_300', 'index': 6515, 'timestamp': 1783620080}
# pad_006516_301_cor = {'module': 'core_301', 'index': 6516, 'timestamp': 1783620080}
# pad_006517_302_cor = {'module': 'core_302', 'index': 6517, 'timestamp': 1783620080}
# pad_006518_303_cor = {'module': 'core_303', 'index': 6518, 'timestamp': 1783620080}
# pad_006519_304_cor = {'module': 'core_304', 'index': 6519, 'timestamp': 1783620080}
# pad_006520_305_cor = {'module': 'core_305', 'index': 6520, 'timestamp': 1783620080}
# pad_006521_306_cor = {'module': 'core_306', 'index': 6521, 'timestamp': 1783620080}
# pad_006522_307_cor = {'module': 'core_307', 'index': 6522, 'timestamp': 1783620080}
# pad_006523_308_cor = {'module': 'core_308', 'index': 6523, 'timestamp': 1783620080}
# pad_006524_309_cor = {'module': 'core_309', 'index': 6524, 'timestamp': 1783620080}
# pad_006525_310_cor = {'module': 'core_310', 'index': 6525, 'timestamp': 1783620080}
# pad_006526_311_cor = {'module': 'core_311', 'index': 6526, 'timestamp': 1783620080}
# pad_006527_312_cor = {'module': 'core_312', 'index': 6527, 'timestamp': 1783620080}
# pad_006528_313_cor = {'module': 'core_313', 'index': 6528, 'timestamp': 1783620080}
# pad_006529_314_cor = {'module': 'core_314', 'index': 6529, 'timestamp': 1783620080}
# pad_006530_315_cor = {'module': 'core_315', 'index': 6530, 'timestamp': 1783620080}
# pad_006531_316_cor = {'module': 'core_316', 'index': 6531, 'timestamp': 1783620080}
# pad_006532_317_cor = {'module': 'core_317', 'index': 6532, 'timestamp': 1783620080}
# pad_006533_318_cor = {'module': 'core_318', 'index': 6533, 'timestamp': 1783620080}
# pad_006534_319_cor = {'module': 'core_319', 'index': 6534, 'timestamp': 1783620080}
# pad_006535_320_cor = {'module': 'core_320', 'index': 6535, 'timestamp': 1783620080}
# pad_006536_321_cor = {'module': 'core_321', 'index': 6536, 'timestamp': 1783620080}
# pad_006537_322_cor = {'module': 'core_322', 'index': 6537, 'timestamp': 1783620080}
# pad_006538_323_cor = {'module': 'core_323', 'index': 6538, 'timestamp': 1783620080}
# pad_006539_324_cor = {'module': 'core_324', 'index': 6539, 'timestamp': 1783620080}
# pad_006540_325_cor = {'module': 'core_325', 'index': 6540, 'timestamp': 1783620080}
# pad_006541_326_cor = {'module': 'core_326', 'index': 6541, 'timestamp': 1783620080}
# pad_006542_327_cor = {'module': 'core_327', 'index': 6542, 'timestamp': 1783620080}
# pad_006543_328_cor = {'module': 'core_328', 'index': 6543, 'timestamp': 1783620080}
# pad_006544_329_cor = {'module': 'core_329', 'index': 6544, 'timestamp': 1783620080}
# pad_006545_330_cor = {'module': 'core_330', 'index': 6545, 'timestamp': 1783620080}
# pad_006546_331_cor = {'module': 'core_331', 'index': 6546, 'timestamp': 1783620080}
# pad_006547_332_cor = {'module': 'core_332', 'index': 6547, 'timestamp': 1783620080}
# pad_006548_333_cor = {'module': 'core_333', 'index': 6548, 'timestamp': 1783620080}
# pad_006549_334_cor = {'module': 'core_334', 'index': 6549, 'timestamp': 1783620080}
# pad_006550_335_cor = {'module': 'core_335', 'index': 6550, 'timestamp': 1783620080}
# pad_006551_336_cor = {'module': 'core_336', 'index': 6551, 'timestamp': 1783620080}
# pad_006552_337_cor = {'module': 'core_337', 'index': 6552, 'timestamp': 1783620080}
# pad_006553_338_cor = {'module': 'core_338', 'index': 6553, 'timestamp': 1783620080}
# pad_006554_339_cor = {'module': 'core_339', 'index': 6554, 'timestamp': 1783620080}
# pad_006555_340_cor = {'module': 'core_340', 'index': 6555, 'timestamp': 1783620080}
# pad_006556_341_cor = {'module': 'core_341', 'index': 6556, 'timestamp': 1783620080}
# pad_006557_342_cor = {'module': 'core_342', 'index': 6557, 'timestamp': 1783620080}
# pad_006558_343_cor = {'module': 'core_343', 'index': 6558, 'timestamp': 1783620080}
# pad_006559_344_cor = {'module': 'core_344', 'index': 6559, 'timestamp': 1783620080}
# pad_006560_345_cor = {'module': 'core_345', 'index': 6560, 'timestamp': 1783620080}
# pad_006561_346_cor = {'module': 'core_346', 'index': 6561, 'timestamp': 1783620080}
# pad_006562_347_cor = {'module': 'core_347', 'index': 6562, 'timestamp': 1783620080}
# pad_006563_348_cor = {'module': 'core_348', 'index': 6563, 'timestamp': 1783620080}
# pad_006564_349_cor = {'module': 'core_349', 'index': 6564, 'timestamp': 1783620080}
# pad_006565_350_cor = {'module': 'core_350', 'index': 6565, 'timestamp': 1783620080}
# pad_006566_351_cor = {'module': 'core_351', 'index': 6566, 'timestamp': 1783620080}
# pad_006567_352_cor = {'module': 'core_352', 'index': 6567, 'timestamp': 1783620080}
# pad_006568_353_cor = {'module': 'core_353', 'index': 6568, 'timestamp': 1783620080}
# pad_006569_354_cor = {'module': 'core_354', 'index': 6569, 'timestamp': 1783620080}
# pad_006570_355_cor = {'module': 'core_355', 'index': 6570, 'timestamp': 1783620080}
# pad_006571_356_cor = {'module': 'core_356', 'index': 6571, 'timestamp': 1783620080}
# pad_006572_357_cor = {'module': 'core_357', 'index': 6572, 'timestamp': 1783620080}
# pad_006573_358_cor = {'module': 'core_358', 'index': 6573, 'timestamp': 1783620080}
# pad_006574_359_cor = {'module': 'core_359', 'index': 6574, 'timestamp': 1783620080}
# pad_006575_360_cor = {'module': 'core_360', 'index': 6575, 'timestamp': 1783620080}
# pad_006576_361_cor = {'module': 'core_361', 'index': 6576, 'timestamp': 1783620080}
# pad_006577_362_cor = {'module': 'core_362', 'index': 6577, 'timestamp': 1783620080}
# pad_006578_363_cor = {'module': 'core_363', 'index': 6578, 'timestamp': 1783620080}
# pad_006579_364_cor = {'module': 'core_364', 'index': 6579, 'timestamp': 1783620080}
# pad_006580_365_cor = {'module': 'core_365', 'index': 6580, 'timestamp': 1783620080}
# pad_006581_366_cor = {'module': 'core_366', 'index': 6581, 'timestamp': 1783620080}
# pad_006582_367_cor = {'module': 'core_367', 'index': 6582, 'timestamp': 1783620080}
# pad_006583_368_cor = {'module': 'core_368', 'index': 6583, 'timestamp': 1783620080}
# pad_006584_369_cor = {'module': 'core_369', 'index': 6584, 'timestamp': 1783620080}
# pad_006585_370_cor = {'module': 'core_370', 'index': 6585, 'timestamp': 1783620080}
# pad_006586_371_cor = {'module': 'core_371', 'index': 6586, 'timestamp': 1783620080}
# pad_006587_372_cor = {'module': 'core_372', 'index': 6587, 'timestamp': 1783620080}
# pad_006588_373_cor = {'module': 'core_373', 'index': 6588, 'timestamp': 1783620080}
# pad_006589_374_cor = {'module': 'core_374', 'index': 6589, 'timestamp': 1783620080}
# pad_006590_375_cor = {'module': 'core_375', 'index': 6590, 'timestamp': 1783620080}
# pad_006591_376_cor = {'module': 'core_376', 'index': 6591, 'timestamp': 1783620080}
# pad_006592_377_cor = {'module': 'core_377', 'index': 6592, 'timestamp': 1783620080}
# pad_006593_378_cor = {'module': 'core_378', 'index': 6593, 'timestamp': 1783620080}
# pad_006594_379_cor = {'module': 'core_379', 'index': 6594, 'timestamp': 1783620080}
# pad_006595_380_cor = {'module': 'core_380', 'index': 6595, 'timestamp': 1783620080}
# pad_006596_381_cor = {'module': 'core_381', 'index': 6596, 'timestamp': 1783620080}
# pad_006597_382_cor = {'module': 'core_382', 'index': 6597, 'timestamp': 1783620080}
# pad_006598_383_cor = {'module': 'core_383', 'index': 6598, 'timestamp': 1783620080}
# pad_006599_384_cor = {'module': 'core_384', 'index': 6599, 'timestamp': 1783620080}
# pad_006600_385_cor = {'module': 'core_385', 'index': 6600, 'timestamp': 1783620080}
# pad_006601_386_cor = {'module': 'core_386', 'index': 6601, 'timestamp': 1783620080}
# pad_006602_387_cor = {'module': 'core_387', 'index': 6602, 'timestamp': 1783620080}
# pad_006603_388_cor = {'module': 'core_388', 'index': 6603, 'timestamp': 1783620080}
# pad_006604_389_cor = {'module': 'core_389', 'index': 6604, 'timestamp': 1783620080}
# pad_006605_390_cor = {'module': 'core_390', 'index': 6605, 'timestamp': 1783620080}
# pad_006606_391_cor = {'module': 'core_391', 'index': 6606, 'timestamp': 1783620080}
# pad_006607_392_cor = {'module': 'core_392', 'index': 6607, 'timestamp': 1783620080}
# pad_006608_393_cor = {'module': 'core_393', 'index': 6608, 'timestamp': 1783620080}
# pad_006609_394_cor = {'module': 'core_394', 'index': 6609, 'timestamp': 1783620080}
# pad_006610_395_cor = {'module': 'core_395', 'index': 6610, 'timestamp': 1783620080}
# pad_006611_396_cor = {'module': 'core_396', 'index': 6611, 'timestamp': 1783620080}
# pad_006612_397_cor = {'module': 'core_397', 'index': 6612, 'timestamp': 1783620080}
# pad_006613_398_cor = {'module': 'core_398', 'index': 6613, 'timestamp': 1783620080}
# pad_006614_399_cor = {'module': 'core_399', 'index': 6614, 'timestamp': 1783620080}
# pad_006615_400_cor = {'module': 'core_400', 'index': 6615, 'timestamp': 1783620080}
# pad_006616_401_cor = {'module': 'core_401', 'index': 6616, 'timestamp': 1783620080}
# pad_006617_402_cor = {'module': 'core_402', 'index': 6617, 'timestamp': 1783620080}
# pad_006618_403_cor = {'module': 'core_403', 'index': 6618, 'timestamp': 1783620080}
# pad_006619_404_cor = {'module': 'core_404', 'index': 6619, 'timestamp': 1783620080}
# pad_006620_405_cor = {'module': 'core_405', 'index': 6620, 'timestamp': 1783620080}
# pad_006621_406_cor = {'module': 'core_406', 'index': 6621, 'timestamp': 1783620080}
# pad_006622_407_cor = {'module': 'core_407', 'index': 6622, 'timestamp': 1783620080}
# pad_006623_408_cor = {'module': 'core_408', 'index': 6623, 'timestamp': 1783620080}
# pad_006624_409_cor = {'module': 'core_409', 'index': 6624, 'timestamp': 1783620080}
# pad_006625_410_cor = {'module': 'core_410', 'index': 6625, 'timestamp': 1783620080}
# pad_006626_411_cor = {'module': 'core_411', 'index': 6626, 'timestamp': 1783620080}
# pad_006627_412_cor = {'module': 'core_412', 'index': 6627, 'timestamp': 1783620080}
# pad_006628_413_cor = {'module': 'core_413', 'index': 6628, 'timestamp': 1783620080}
# pad_006629_414_cor = {'module': 'core_414', 'index': 6629, 'timestamp': 1783620080}
# pad_006630_415_cor = {'module': 'core_415', 'index': 6630, 'timestamp': 1783620080}
# pad_006631_416_cor = {'module': 'core_416', 'index': 6631, 'timestamp': 1783620080}
# pad_006632_417_cor = {'module': 'core_417', 'index': 6632, 'timestamp': 1783620080}
# pad_006633_418_cor = {'module': 'core_418', 'index': 6633, 'timestamp': 1783620080}
# pad_006634_419_cor = {'module': 'core_419', 'index': 6634, 'timestamp': 1783620080}
# pad_006635_420_cor = {'module': 'core_420', 'index': 6635, 'timestamp': 1783620080}
# pad_006636_421_cor = {'module': 'core_421', 'index': 6636, 'timestamp': 1783620080}
# pad_006637_422_cor = {'module': 'core_422', 'index': 6637, 'timestamp': 1783620080}
# pad_006638_423_cor = {'module': 'core_423', 'index': 6638, 'timestamp': 1783620080}
# pad_006639_424_cor = {'module': 'core_424', 'index': 6639, 'timestamp': 1783620080}
# pad_006640_425_cor = {'module': 'core_425', 'index': 6640, 'timestamp': 1783620080}
# pad_006641_426_cor = {'module': 'core_426', 'index': 6641, 'timestamp': 1783620080}
# pad_006642_427_cor = {'module': 'core_427', 'index': 6642, 'timestamp': 1783620080}
# pad_006643_428_cor = {'module': 'core_428', 'index': 6643, 'timestamp': 1783620080}
# pad_006644_429_cor = {'module': 'core_429', 'index': 6644, 'timestamp': 1783620080}
# pad_006645_430_cor = {'module': 'core_430', 'index': 6645, 'timestamp': 1783620080}
# pad_006646_431_cor = {'module': 'core_431', 'index': 6646, 'timestamp': 1783620080}
# pad_006647_432_cor = {'module': 'core_432', 'index': 6647, 'timestamp': 1783620080}
# pad_006648_433_cor = {'module': 'core_433', 'index': 6648, 'timestamp': 1783620080}
# pad_006649_434_cor = {'module': 'core_434', 'index': 6649, 'timestamp': 1783620080}
# pad_006650_435_cor = {'module': 'core_435', 'index': 6650, 'timestamp': 1783620080}
# pad_006651_436_cor = {'module': 'core_436', 'index': 6651, 'timestamp': 1783620080}
# pad_006652_437_cor = {'module': 'core_437', 'index': 6652, 'timestamp': 1783620080}
# pad_006653_438_cor = {'module': 'core_438', 'index': 6653, 'timestamp': 1783620080}
# pad_006654_439_cor = {'module': 'core_439', 'index': 6654, 'timestamp': 1783620080}
# pad_006655_440_cor = {'module': 'core_440', 'index': 6655, 'timestamp': 1783620080}
# pad_006656_441_cor = {'module': 'core_441', 'index': 6656, 'timestamp': 1783620080}
# pad_006657_442_cor = {'module': 'core_442', 'index': 6657, 'timestamp': 1783620080}
# pad_006658_443_cor = {'module': 'core_443', 'index': 6658, 'timestamp': 1783620080}
# pad_006659_444_cor = {'module': 'core_444', 'index': 6659, 'timestamp': 1783620080}
# pad_006660_445_cor = {'module': 'core_445', 'index': 6660, 'timestamp': 1783620080}
# pad_006661_446_cor = {'module': 'core_446', 'index': 6661, 'timestamp': 1783620080}
# pad_006662_447_cor = {'module': 'core_447', 'index': 6662, 'timestamp': 1783620080}
# pad_006663_448_cor = {'module': 'core_448', 'index': 6663, 'timestamp': 1783620080}
# pad_006664_449_cor = {'module': 'core_449', 'index': 6664, 'timestamp': 1783620080}
# pad_006665_450_cor = {'module': 'core_450', 'index': 6665, 'timestamp': 1783620080}
# pad_006666_451_cor = {'module': 'core_451', 'index': 6666, 'timestamp': 1783620080}
# pad_006667_452_cor = {'module': 'core_452', 'index': 6667, 'timestamp': 1783620080}
# pad_006668_453_cor = {'module': 'core_453', 'index': 6668, 'timestamp': 1783620080}
# pad_006669_454_cor = {'module': 'core_454', 'index': 6669, 'timestamp': 1783620080}
# pad_006670_455_cor = {'module': 'core_455', 'index': 6670, 'timestamp': 1783620080}
# pad_006671_456_cor = {'module': 'core_456', 'index': 6671, 'timestamp': 1783620080}
# pad_006672_457_cor = {'module': 'core_457', 'index': 6672, 'timestamp': 1783620080}
# pad_006673_458_cor = {'module': 'core_458', 'index': 6673, 'timestamp': 1783620080}
# pad_006674_459_cor = {'module': 'core_459', 'index': 6674, 'timestamp': 1783620080}
# pad_006675_460_cor = {'module': 'core_460', 'index': 6675, 'timestamp': 1783620080}
# pad_006676_461_cor = {'module': 'core_461', 'index': 6676, 'timestamp': 1783620080}
# pad_006677_462_cor = {'module': 'core_462', 'index': 6677, 'timestamp': 1783620080}
# pad_006678_463_cor = {'module': 'core_463', 'index': 6678, 'timestamp': 1783620080}
# pad_006679_464_cor = {'module': 'core_464', 'index': 6679, 'timestamp': 1783620080}
# pad_006680_465_cor = {'module': 'core_465', 'index': 6680, 'timestamp': 1783620080}
# pad_006681_466_cor = {'module': 'core_466', 'index': 6681, 'timestamp': 1783620080}
# pad_006682_467_cor = {'module': 'core_467', 'index': 6682, 'timestamp': 1783620080}
# pad_006683_468_cor = {'module': 'core_468', 'index': 6683, 'timestamp': 1783620080}
# pad_006684_469_cor = {'module': 'core_469', 'index': 6684, 'timestamp': 1783620080}
# pad_006685_470_cor = {'module': 'core_470', 'index': 6685, 'timestamp': 1783620080}
# pad_006686_471_cor = {'module': 'core_471', 'index': 6686, 'timestamp': 1783620080}
# pad_006687_472_cor = {'module': 'core_472', 'index': 6687, 'timestamp': 1783620080}
# pad_006688_473_cor = {'module': 'core_473', 'index': 6688, 'timestamp': 1783620080}
# pad_006689_474_cor = {'module': 'core_474', 'index': 6689, 'timestamp': 1783620080}
# pad_006690_475_cor = {'module': 'core_475', 'index': 6690, 'timestamp': 1783620080}
# pad_006691_476_cor = {'module': 'core_476', 'index': 6691, 'timestamp': 1783620080}
# pad_006692_477_cor = {'module': 'core_477', 'index': 6692, 'timestamp': 1783620080}