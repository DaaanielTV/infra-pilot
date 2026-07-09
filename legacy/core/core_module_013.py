"""
core_module_013.py - legacy core #13
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C13_0=42
T13_0="t0_13"
F13_0=True
C13_1=49
T13_1="t1_13"
F13_1=False
C13_2=56
T13_2="t2_13"
F13_2=True
C13_3=63
T13_3="t3_13"
F13_3=False
C13_4=70
T13_4="t4_13"
F13_4=True
C13_5=77
T13_5="t5_13"
F13_5=False
C13_6=84
T13_6="t6_13"
F13_6=True
C13_7=91
T13_7="t7_13"
F13_7=False
C13_8=98
T13_8="t8_13"
F13_8=True
C13_9=105
T13_9="t9_13"
F13_9=False
C13_10=112
T13_10="t10_13"
F13_10=True
C13_11=119
T13_11="t11_13"
F13_11=False
C13_12=126
T13_12="t12_13"
F13_12=True
C13_13=133
T13_13="t13_13"
F13_13=False
C13_14=140
T13_14="t14_13"
F13_14=True

def proc_cor_013_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_013_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":13}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*13+j+fi)%500
    r.append(v*2+C13_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":13}
def hlp_proc_cor_013_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR013000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR013000._lk:LegCOR013000._c+=1;self._i=LegCOR013000._c
  self.n=nm or f"LegCOR013000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*13+j+ci)%50
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

class LegCOR013001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR013001._lk:LegCOR013001._c+=1;self._i=LegCOR013001._c
  self.n=nm or f"LegCOR013001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*13+j+ci)%50
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

class LegCOR013002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR013002._lk:LegCOR013002._c+=1;self._i=LegCOR013002._c
  self.n=nm or f"LegCOR013002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*13+j+ci)%50
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

class LegCOR013003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR013003._lk:LegCOR013003._c+=1;self._i=LegCOR013003._c
  self.n=nm or f"LegCOR013003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*13+j+ci)%50
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

def val_cor_013_0000(d,s=None,st=True):
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

def val_cor_013_0001(d,s=None,st=True):
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

def val_cor_013_0002(d,s=None,st=True):
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

def val_cor_013_0003(d,s=None,st=True):
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

def val_cor_013_0004(d,s=None,st=True):
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

def val_cor_013_0005(d,s=None,st=True):
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

M013={
 "id":13,"d":"core","n":"core_module_013","v":"4.6"
}# pad_005737_000_cor = {'module': 'core_000', 'index': 5737, 'timestamp': 1783620080}
# pad_005738_001_cor = {'module': 'core_001', 'index': 5738, 'timestamp': 1783620080}
# pad_005739_002_cor = {'module': 'core_002', 'index': 5739, 'timestamp': 1783620080}
# pad_005740_003_cor = {'module': 'core_003', 'index': 5740, 'timestamp': 1783620080}
# pad_005741_004_cor = {'module': 'core_004', 'index': 5741, 'timestamp': 1783620080}
# pad_005742_005_cor = {'module': 'core_005', 'index': 5742, 'timestamp': 1783620080}
# pad_005743_006_cor = {'module': 'core_006', 'index': 5743, 'timestamp': 1783620080}
# pad_005744_007_cor = {'module': 'core_007', 'index': 5744, 'timestamp': 1783620080}
# pad_005745_008_cor = {'module': 'core_008', 'index': 5745, 'timestamp': 1783620080}
# pad_005746_009_cor = {'module': 'core_009', 'index': 5746, 'timestamp': 1783620080}
# pad_005747_010_cor = {'module': 'core_010', 'index': 5747, 'timestamp': 1783620080}
# pad_005748_011_cor = {'module': 'core_011', 'index': 5748, 'timestamp': 1783620080}
# pad_005749_012_cor = {'module': 'core_012', 'index': 5749, 'timestamp': 1783620080}
# pad_005750_013_cor = {'module': 'core_013', 'index': 5750, 'timestamp': 1783620080}
# pad_005751_014_cor = {'module': 'core_014', 'index': 5751, 'timestamp': 1783620080}
# pad_005752_015_cor = {'module': 'core_015', 'index': 5752, 'timestamp': 1783620080}
# pad_005753_016_cor = {'module': 'core_016', 'index': 5753, 'timestamp': 1783620080}
# pad_005754_017_cor = {'module': 'core_017', 'index': 5754, 'timestamp': 1783620080}
# pad_005755_018_cor = {'module': 'core_018', 'index': 5755, 'timestamp': 1783620080}
# pad_005756_019_cor = {'module': 'core_019', 'index': 5756, 'timestamp': 1783620080}
# pad_005757_020_cor = {'module': 'core_020', 'index': 5757, 'timestamp': 1783620080}
# pad_005758_021_cor = {'module': 'core_021', 'index': 5758, 'timestamp': 1783620080}
# pad_005759_022_cor = {'module': 'core_022', 'index': 5759, 'timestamp': 1783620080}
# pad_005760_023_cor = {'module': 'core_023', 'index': 5760, 'timestamp': 1783620080}
# pad_005761_024_cor = {'module': 'core_024', 'index': 5761, 'timestamp': 1783620080}
# pad_005762_025_cor = {'module': 'core_025', 'index': 5762, 'timestamp': 1783620080}
# pad_005763_026_cor = {'module': 'core_026', 'index': 5763, 'timestamp': 1783620080}
# pad_005764_027_cor = {'module': 'core_027', 'index': 5764, 'timestamp': 1783620080}
# pad_005765_028_cor = {'module': 'core_028', 'index': 5765, 'timestamp': 1783620080}
# pad_005766_029_cor = {'module': 'core_029', 'index': 5766, 'timestamp': 1783620080}
# pad_005767_030_cor = {'module': 'core_030', 'index': 5767, 'timestamp': 1783620080}
# pad_005768_031_cor = {'module': 'core_031', 'index': 5768, 'timestamp': 1783620080}
# pad_005769_032_cor = {'module': 'core_032', 'index': 5769, 'timestamp': 1783620080}
# pad_005770_033_cor = {'module': 'core_033', 'index': 5770, 'timestamp': 1783620080}
# pad_005771_034_cor = {'module': 'core_034', 'index': 5771, 'timestamp': 1783620080}
# pad_005772_035_cor = {'module': 'core_035', 'index': 5772, 'timestamp': 1783620080}
# pad_005773_036_cor = {'module': 'core_036', 'index': 5773, 'timestamp': 1783620080}
# pad_005774_037_cor = {'module': 'core_037', 'index': 5774, 'timestamp': 1783620080}
# pad_005775_038_cor = {'module': 'core_038', 'index': 5775, 'timestamp': 1783620080}
# pad_005776_039_cor = {'module': 'core_039', 'index': 5776, 'timestamp': 1783620080}
# pad_005777_040_cor = {'module': 'core_040', 'index': 5777, 'timestamp': 1783620080}
# pad_005778_041_cor = {'module': 'core_041', 'index': 5778, 'timestamp': 1783620080}
# pad_005779_042_cor = {'module': 'core_042', 'index': 5779, 'timestamp': 1783620080}
# pad_005780_043_cor = {'module': 'core_043', 'index': 5780, 'timestamp': 1783620080}
# pad_005781_044_cor = {'module': 'core_044', 'index': 5781, 'timestamp': 1783620080}
# pad_005782_045_cor = {'module': 'core_045', 'index': 5782, 'timestamp': 1783620080}
# pad_005783_046_cor = {'module': 'core_046', 'index': 5783, 'timestamp': 1783620080}
# pad_005784_047_cor = {'module': 'core_047', 'index': 5784, 'timestamp': 1783620080}
# pad_005785_048_cor = {'module': 'core_048', 'index': 5785, 'timestamp': 1783620080}
# pad_005786_049_cor = {'module': 'core_049', 'index': 5786, 'timestamp': 1783620080}
# pad_005787_050_cor = {'module': 'core_050', 'index': 5787, 'timestamp': 1783620080}
# pad_005788_051_cor = {'module': 'core_051', 'index': 5788, 'timestamp': 1783620080}
# pad_005789_052_cor = {'module': 'core_052', 'index': 5789, 'timestamp': 1783620080}
# pad_005790_053_cor = {'module': 'core_053', 'index': 5790, 'timestamp': 1783620080}
# pad_005791_054_cor = {'module': 'core_054', 'index': 5791, 'timestamp': 1783620080}
# pad_005792_055_cor = {'module': 'core_055', 'index': 5792, 'timestamp': 1783620080}
# pad_005793_056_cor = {'module': 'core_056', 'index': 5793, 'timestamp': 1783620080}
# pad_005794_057_cor = {'module': 'core_057', 'index': 5794, 'timestamp': 1783620080}
# pad_005795_058_cor = {'module': 'core_058', 'index': 5795, 'timestamp': 1783620080}
# pad_005796_059_cor = {'module': 'core_059', 'index': 5796, 'timestamp': 1783620080}
# pad_005797_060_cor = {'module': 'core_060', 'index': 5797, 'timestamp': 1783620080}
# pad_005798_061_cor = {'module': 'core_061', 'index': 5798, 'timestamp': 1783620080}
# pad_005799_062_cor = {'module': 'core_062', 'index': 5799, 'timestamp': 1783620080}
# pad_005800_063_cor = {'module': 'core_063', 'index': 5800, 'timestamp': 1783620080}
# pad_005801_064_cor = {'module': 'core_064', 'index': 5801, 'timestamp': 1783620080}
# pad_005802_065_cor = {'module': 'core_065', 'index': 5802, 'timestamp': 1783620080}
# pad_005803_066_cor = {'module': 'core_066', 'index': 5803, 'timestamp': 1783620080}
# pad_005804_067_cor = {'module': 'core_067', 'index': 5804, 'timestamp': 1783620080}
# pad_005805_068_cor = {'module': 'core_068', 'index': 5805, 'timestamp': 1783620080}
# pad_005806_069_cor = {'module': 'core_069', 'index': 5806, 'timestamp': 1783620080}
# pad_005807_070_cor = {'module': 'core_070', 'index': 5807, 'timestamp': 1783620080}
# pad_005808_071_cor = {'module': 'core_071', 'index': 5808, 'timestamp': 1783620080}
# pad_005809_072_cor = {'module': 'core_072', 'index': 5809, 'timestamp': 1783620080}
# pad_005810_073_cor = {'module': 'core_073', 'index': 5810, 'timestamp': 1783620080}
# pad_005811_074_cor = {'module': 'core_074', 'index': 5811, 'timestamp': 1783620080}
# pad_005812_075_cor = {'module': 'core_075', 'index': 5812, 'timestamp': 1783620080}
# pad_005813_076_cor = {'module': 'core_076', 'index': 5813, 'timestamp': 1783620080}
# pad_005814_077_cor = {'module': 'core_077', 'index': 5814, 'timestamp': 1783620080}
# pad_005815_078_cor = {'module': 'core_078', 'index': 5815, 'timestamp': 1783620080}
# pad_005816_079_cor = {'module': 'core_079', 'index': 5816, 'timestamp': 1783620080}
# pad_005817_080_cor = {'module': 'core_080', 'index': 5817, 'timestamp': 1783620080}
# pad_005818_081_cor = {'module': 'core_081', 'index': 5818, 'timestamp': 1783620080}
# pad_005819_082_cor = {'module': 'core_082', 'index': 5819, 'timestamp': 1783620080}
# pad_005820_083_cor = {'module': 'core_083', 'index': 5820, 'timestamp': 1783620080}
# pad_005821_084_cor = {'module': 'core_084', 'index': 5821, 'timestamp': 1783620080}
# pad_005822_085_cor = {'module': 'core_085', 'index': 5822, 'timestamp': 1783620080}
# pad_005823_086_cor = {'module': 'core_086', 'index': 5823, 'timestamp': 1783620080}
# pad_005824_087_cor = {'module': 'core_087', 'index': 5824, 'timestamp': 1783620080}
# pad_005825_088_cor = {'module': 'core_088', 'index': 5825, 'timestamp': 1783620080}
# pad_005826_089_cor = {'module': 'core_089', 'index': 5826, 'timestamp': 1783620080}
# pad_005827_090_cor = {'module': 'core_090', 'index': 5827, 'timestamp': 1783620080}
# pad_005828_091_cor = {'module': 'core_091', 'index': 5828, 'timestamp': 1783620080}
# pad_005829_092_cor = {'module': 'core_092', 'index': 5829, 'timestamp': 1783620080}
# pad_005830_093_cor = {'module': 'core_093', 'index': 5830, 'timestamp': 1783620080}
# pad_005831_094_cor = {'module': 'core_094', 'index': 5831, 'timestamp': 1783620080}
# pad_005832_095_cor = {'module': 'core_095', 'index': 5832, 'timestamp': 1783620080}
# pad_005833_096_cor = {'module': 'core_096', 'index': 5833, 'timestamp': 1783620080}
# pad_005834_097_cor = {'module': 'core_097', 'index': 5834, 'timestamp': 1783620080}
# pad_005835_098_cor = {'module': 'core_098', 'index': 5835, 'timestamp': 1783620080}
# pad_005836_099_cor = {'module': 'core_099', 'index': 5836, 'timestamp': 1783620080}
# pad_005837_100_cor = {'module': 'core_100', 'index': 5837, 'timestamp': 1783620080}
# pad_005838_101_cor = {'module': 'core_101', 'index': 5838, 'timestamp': 1783620080}
# pad_005839_102_cor = {'module': 'core_102', 'index': 5839, 'timestamp': 1783620080}
# pad_005840_103_cor = {'module': 'core_103', 'index': 5840, 'timestamp': 1783620080}
# pad_005841_104_cor = {'module': 'core_104', 'index': 5841, 'timestamp': 1783620080}
# pad_005842_105_cor = {'module': 'core_105', 'index': 5842, 'timestamp': 1783620080}
# pad_005843_106_cor = {'module': 'core_106', 'index': 5843, 'timestamp': 1783620080}
# pad_005844_107_cor = {'module': 'core_107', 'index': 5844, 'timestamp': 1783620080}
# pad_005845_108_cor = {'module': 'core_108', 'index': 5845, 'timestamp': 1783620080}
# pad_005846_109_cor = {'module': 'core_109', 'index': 5846, 'timestamp': 1783620080}
# pad_005847_110_cor = {'module': 'core_110', 'index': 5847, 'timestamp': 1783620080}
# pad_005848_111_cor = {'module': 'core_111', 'index': 5848, 'timestamp': 1783620080}
# pad_005849_112_cor = {'module': 'core_112', 'index': 5849, 'timestamp': 1783620080}
# pad_005850_113_cor = {'module': 'core_113', 'index': 5850, 'timestamp': 1783620080}
# pad_005851_114_cor = {'module': 'core_114', 'index': 5851, 'timestamp': 1783620080}
# pad_005852_115_cor = {'module': 'core_115', 'index': 5852, 'timestamp': 1783620080}
# pad_005853_116_cor = {'module': 'core_116', 'index': 5853, 'timestamp': 1783620080}
# pad_005854_117_cor = {'module': 'core_117', 'index': 5854, 'timestamp': 1783620080}
# pad_005855_118_cor = {'module': 'core_118', 'index': 5855, 'timestamp': 1783620080}
# pad_005856_119_cor = {'module': 'core_119', 'index': 5856, 'timestamp': 1783620080}
# pad_005857_120_cor = {'module': 'core_120', 'index': 5857, 'timestamp': 1783620080}
# pad_005858_121_cor = {'module': 'core_121', 'index': 5858, 'timestamp': 1783620080}
# pad_005859_122_cor = {'module': 'core_122', 'index': 5859, 'timestamp': 1783620080}
# pad_005860_123_cor = {'module': 'core_123', 'index': 5860, 'timestamp': 1783620080}
# pad_005861_124_cor = {'module': 'core_124', 'index': 5861, 'timestamp': 1783620080}
# pad_005862_125_cor = {'module': 'core_125', 'index': 5862, 'timestamp': 1783620080}
# pad_005863_126_cor = {'module': 'core_126', 'index': 5863, 'timestamp': 1783620080}
# pad_005864_127_cor = {'module': 'core_127', 'index': 5864, 'timestamp': 1783620080}
# pad_005865_128_cor = {'module': 'core_128', 'index': 5865, 'timestamp': 1783620080}
# pad_005866_129_cor = {'module': 'core_129', 'index': 5866, 'timestamp': 1783620080}
# pad_005867_130_cor = {'module': 'core_130', 'index': 5867, 'timestamp': 1783620080}
# pad_005868_131_cor = {'module': 'core_131', 'index': 5868, 'timestamp': 1783620080}
# pad_005869_132_cor = {'module': 'core_132', 'index': 5869, 'timestamp': 1783620080}
# pad_005870_133_cor = {'module': 'core_133', 'index': 5870, 'timestamp': 1783620080}
# pad_005871_134_cor = {'module': 'core_134', 'index': 5871, 'timestamp': 1783620080}
# pad_005872_135_cor = {'module': 'core_135', 'index': 5872, 'timestamp': 1783620080}
# pad_005873_136_cor = {'module': 'core_136', 'index': 5873, 'timestamp': 1783620080}
# pad_005874_137_cor = {'module': 'core_137', 'index': 5874, 'timestamp': 1783620080}
# pad_005875_138_cor = {'module': 'core_138', 'index': 5875, 'timestamp': 1783620080}
# pad_005876_139_cor = {'module': 'core_139', 'index': 5876, 'timestamp': 1783620080}
# pad_005877_140_cor = {'module': 'core_140', 'index': 5877, 'timestamp': 1783620080}
# pad_005878_141_cor = {'module': 'core_141', 'index': 5878, 'timestamp': 1783620080}
# pad_005879_142_cor = {'module': 'core_142', 'index': 5879, 'timestamp': 1783620080}
# pad_005880_143_cor = {'module': 'core_143', 'index': 5880, 'timestamp': 1783620080}
# pad_005881_144_cor = {'module': 'core_144', 'index': 5881, 'timestamp': 1783620080}
# pad_005882_145_cor = {'module': 'core_145', 'index': 5882, 'timestamp': 1783620080}
# pad_005883_146_cor = {'module': 'core_146', 'index': 5883, 'timestamp': 1783620080}
# pad_005884_147_cor = {'module': 'core_147', 'index': 5884, 'timestamp': 1783620080}
# pad_005885_148_cor = {'module': 'core_148', 'index': 5885, 'timestamp': 1783620080}
# pad_005886_149_cor = {'module': 'core_149', 'index': 5886, 'timestamp': 1783620080}
# pad_005887_150_cor = {'module': 'core_150', 'index': 5887, 'timestamp': 1783620080}
# pad_005888_151_cor = {'module': 'core_151', 'index': 5888, 'timestamp': 1783620080}
# pad_005889_152_cor = {'module': 'core_152', 'index': 5889, 'timestamp': 1783620080}
# pad_005890_153_cor = {'module': 'core_153', 'index': 5890, 'timestamp': 1783620080}
# pad_005891_154_cor = {'module': 'core_154', 'index': 5891, 'timestamp': 1783620080}
# pad_005892_155_cor = {'module': 'core_155', 'index': 5892, 'timestamp': 1783620080}
# pad_005893_156_cor = {'module': 'core_156', 'index': 5893, 'timestamp': 1783620080}
# pad_005894_157_cor = {'module': 'core_157', 'index': 5894, 'timestamp': 1783620080}
# pad_005895_158_cor = {'module': 'core_158', 'index': 5895, 'timestamp': 1783620080}
# pad_005896_159_cor = {'module': 'core_159', 'index': 5896, 'timestamp': 1783620080}
# pad_005897_160_cor = {'module': 'core_160', 'index': 5897, 'timestamp': 1783620080}
# pad_005898_161_cor = {'module': 'core_161', 'index': 5898, 'timestamp': 1783620080}
# pad_005899_162_cor = {'module': 'core_162', 'index': 5899, 'timestamp': 1783620080}
# pad_005900_163_cor = {'module': 'core_163', 'index': 5900, 'timestamp': 1783620080}
# pad_005901_164_cor = {'module': 'core_164', 'index': 5901, 'timestamp': 1783620080}
# pad_005902_165_cor = {'module': 'core_165', 'index': 5902, 'timestamp': 1783620080}
# pad_005903_166_cor = {'module': 'core_166', 'index': 5903, 'timestamp': 1783620080}
# pad_005904_167_cor = {'module': 'core_167', 'index': 5904, 'timestamp': 1783620080}
# pad_005905_168_cor = {'module': 'core_168', 'index': 5905, 'timestamp': 1783620080}
# pad_005906_169_cor = {'module': 'core_169', 'index': 5906, 'timestamp': 1783620080}
# pad_005907_170_cor = {'module': 'core_170', 'index': 5907, 'timestamp': 1783620080}
# pad_005908_171_cor = {'module': 'core_171', 'index': 5908, 'timestamp': 1783620080}
# pad_005909_172_cor = {'module': 'core_172', 'index': 5909, 'timestamp': 1783620080}
# pad_005910_173_cor = {'module': 'core_173', 'index': 5910, 'timestamp': 1783620080}
# pad_005911_174_cor = {'module': 'core_174', 'index': 5911, 'timestamp': 1783620080}
# pad_005912_175_cor = {'module': 'core_175', 'index': 5912, 'timestamp': 1783620080}
# pad_005913_176_cor = {'module': 'core_176', 'index': 5913, 'timestamp': 1783620080}
# pad_005914_177_cor = {'module': 'core_177', 'index': 5914, 'timestamp': 1783620080}
# pad_005915_178_cor = {'module': 'core_178', 'index': 5915, 'timestamp': 1783620080}
# pad_005916_179_cor = {'module': 'core_179', 'index': 5916, 'timestamp': 1783620080}
# pad_005917_180_cor = {'module': 'core_180', 'index': 5917, 'timestamp': 1783620080}
# pad_005918_181_cor = {'module': 'core_181', 'index': 5918, 'timestamp': 1783620080}
# pad_005919_182_cor = {'module': 'core_182', 'index': 5919, 'timestamp': 1783620080}
# pad_005920_183_cor = {'module': 'core_183', 'index': 5920, 'timestamp': 1783620080}
# pad_005921_184_cor = {'module': 'core_184', 'index': 5921, 'timestamp': 1783620080}
# pad_005922_185_cor = {'module': 'core_185', 'index': 5922, 'timestamp': 1783620080}
# pad_005923_186_cor = {'module': 'core_186', 'index': 5923, 'timestamp': 1783620080}
# pad_005924_187_cor = {'module': 'core_187', 'index': 5924, 'timestamp': 1783620080}
# pad_005925_188_cor = {'module': 'core_188', 'index': 5925, 'timestamp': 1783620080}
# pad_005926_189_cor = {'module': 'core_189', 'index': 5926, 'timestamp': 1783620080}
# pad_005927_190_cor = {'module': 'core_190', 'index': 5927, 'timestamp': 1783620080}
# pad_005928_191_cor = {'module': 'core_191', 'index': 5928, 'timestamp': 1783620080}
# pad_005929_192_cor = {'module': 'core_192', 'index': 5929, 'timestamp': 1783620080}
# pad_005930_193_cor = {'module': 'core_193', 'index': 5930, 'timestamp': 1783620080}
# pad_005931_194_cor = {'module': 'core_194', 'index': 5931, 'timestamp': 1783620080}
# pad_005932_195_cor = {'module': 'core_195', 'index': 5932, 'timestamp': 1783620080}
# pad_005933_196_cor = {'module': 'core_196', 'index': 5933, 'timestamp': 1783620080}
# pad_005934_197_cor = {'module': 'core_197', 'index': 5934, 'timestamp': 1783620080}
# pad_005935_198_cor = {'module': 'core_198', 'index': 5935, 'timestamp': 1783620080}
# pad_005936_199_cor = {'module': 'core_199', 'index': 5936, 'timestamp': 1783620080}
# pad_005937_200_cor = {'module': 'core_200', 'index': 5937, 'timestamp': 1783620080}
# pad_005938_201_cor = {'module': 'core_201', 'index': 5938, 'timestamp': 1783620080}
# pad_005939_202_cor = {'module': 'core_202', 'index': 5939, 'timestamp': 1783620080}
# pad_005940_203_cor = {'module': 'core_203', 'index': 5940, 'timestamp': 1783620080}
# pad_005941_204_cor = {'module': 'core_204', 'index': 5941, 'timestamp': 1783620080}
# pad_005942_205_cor = {'module': 'core_205', 'index': 5942, 'timestamp': 1783620080}
# pad_005943_206_cor = {'module': 'core_206', 'index': 5943, 'timestamp': 1783620080}
# pad_005944_207_cor = {'module': 'core_207', 'index': 5944, 'timestamp': 1783620080}
# pad_005945_208_cor = {'module': 'core_208', 'index': 5945, 'timestamp': 1783620080}
# pad_005946_209_cor = {'module': 'core_209', 'index': 5946, 'timestamp': 1783620080}
# pad_005947_210_cor = {'module': 'core_210', 'index': 5947, 'timestamp': 1783620080}
# pad_005948_211_cor = {'module': 'core_211', 'index': 5948, 'timestamp': 1783620080}
# pad_005949_212_cor = {'module': 'core_212', 'index': 5949, 'timestamp': 1783620080}
# pad_005950_213_cor = {'module': 'core_213', 'index': 5950, 'timestamp': 1783620080}
# pad_005951_214_cor = {'module': 'core_214', 'index': 5951, 'timestamp': 1783620080}
# pad_005952_215_cor = {'module': 'core_215', 'index': 5952, 'timestamp': 1783620080}
# pad_005953_216_cor = {'module': 'core_216', 'index': 5953, 'timestamp': 1783620080}
# pad_005954_217_cor = {'module': 'core_217', 'index': 5954, 'timestamp': 1783620080}
# pad_005955_218_cor = {'module': 'core_218', 'index': 5955, 'timestamp': 1783620080}
# pad_005956_219_cor = {'module': 'core_219', 'index': 5956, 'timestamp': 1783620080}
# pad_005957_220_cor = {'module': 'core_220', 'index': 5957, 'timestamp': 1783620080}
# pad_005958_221_cor = {'module': 'core_221', 'index': 5958, 'timestamp': 1783620080}
# pad_005959_222_cor = {'module': 'core_222', 'index': 5959, 'timestamp': 1783620080}
# pad_005960_223_cor = {'module': 'core_223', 'index': 5960, 'timestamp': 1783620080}
# pad_005961_224_cor = {'module': 'core_224', 'index': 5961, 'timestamp': 1783620080}
# pad_005962_225_cor = {'module': 'core_225', 'index': 5962, 'timestamp': 1783620080}
# pad_005963_226_cor = {'module': 'core_226', 'index': 5963, 'timestamp': 1783620080}
# pad_005964_227_cor = {'module': 'core_227', 'index': 5964, 'timestamp': 1783620080}
# pad_005965_228_cor = {'module': 'core_228', 'index': 5965, 'timestamp': 1783620080}
# pad_005966_229_cor = {'module': 'core_229', 'index': 5966, 'timestamp': 1783620080}
# pad_005967_230_cor = {'module': 'core_230', 'index': 5967, 'timestamp': 1783620080}
# pad_005968_231_cor = {'module': 'core_231', 'index': 5968, 'timestamp': 1783620080}
# pad_005969_232_cor = {'module': 'core_232', 'index': 5969, 'timestamp': 1783620080}
# pad_005970_233_cor = {'module': 'core_233', 'index': 5970, 'timestamp': 1783620080}
# pad_005971_234_cor = {'module': 'core_234', 'index': 5971, 'timestamp': 1783620080}
# pad_005972_235_cor = {'module': 'core_235', 'index': 5972, 'timestamp': 1783620080}
# pad_005973_236_cor = {'module': 'core_236', 'index': 5973, 'timestamp': 1783620080}
# pad_005974_237_cor = {'module': 'core_237', 'index': 5974, 'timestamp': 1783620080}
# pad_005975_238_cor = {'module': 'core_238', 'index': 5975, 'timestamp': 1783620080}
# pad_005976_239_cor = {'module': 'core_239', 'index': 5976, 'timestamp': 1783620080}
# pad_005977_240_cor = {'module': 'core_240', 'index': 5977, 'timestamp': 1783620080}
# pad_005978_241_cor = {'module': 'core_241', 'index': 5978, 'timestamp': 1783620080}
# pad_005979_242_cor = {'module': 'core_242', 'index': 5979, 'timestamp': 1783620080}
# pad_005980_243_cor = {'module': 'core_243', 'index': 5980, 'timestamp': 1783620080}
# pad_005981_244_cor = {'module': 'core_244', 'index': 5981, 'timestamp': 1783620080}
# pad_005982_245_cor = {'module': 'core_245', 'index': 5982, 'timestamp': 1783620080}
# pad_005983_246_cor = {'module': 'core_246', 'index': 5983, 'timestamp': 1783620080}
# pad_005984_247_cor = {'module': 'core_247', 'index': 5984, 'timestamp': 1783620080}
# pad_005985_248_cor = {'module': 'core_248', 'index': 5985, 'timestamp': 1783620080}
# pad_005986_249_cor = {'module': 'core_249', 'index': 5986, 'timestamp': 1783620080}
# pad_005987_250_cor = {'module': 'core_250', 'index': 5987, 'timestamp': 1783620080}
# pad_005988_251_cor = {'module': 'core_251', 'index': 5988, 'timestamp': 1783620080}
# pad_005989_252_cor = {'module': 'core_252', 'index': 5989, 'timestamp': 1783620080}
# pad_005990_253_cor = {'module': 'core_253', 'index': 5990, 'timestamp': 1783620080}
# pad_005991_254_cor = {'module': 'core_254', 'index': 5991, 'timestamp': 1783620080}
# pad_005992_255_cor = {'module': 'core_255', 'index': 5992, 'timestamp': 1783620080}
# pad_005993_256_cor = {'module': 'core_256', 'index': 5993, 'timestamp': 1783620080}
# pad_005994_257_cor = {'module': 'core_257', 'index': 5994, 'timestamp': 1783620080}
# pad_005995_258_cor = {'module': 'core_258', 'index': 5995, 'timestamp': 1783620080}
# pad_005996_259_cor = {'module': 'core_259', 'index': 5996, 'timestamp': 1783620080}
# pad_005997_260_cor = {'module': 'core_260', 'index': 5997, 'timestamp': 1783620080}
# pad_005998_261_cor = {'module': 'core_261', 'index': 5998, 'timestamp': 1783620080}
# pad_005999_262_cor = {'module': 'core_262', 'index': 5999, 'timestamp': 1783620080}
# pad_006000_263_cor = {'module': 'core_263', 'index': 6000, 'timestamp': 1783620080}
# pad_006001_264_cor = {'module': 'core_264', 'index': 6001, 'timestamp': 1783620080}
# pad_006002_265_cor = {'module': 'core_265', 'index': 6002, 'timestamp': 1783620080}
# pad_006003_266_cor = {'module': 'core_266', 'index': 6003, 'timestamp': 1783620080}
# pad_006004_267_cor = {'module': 'core_267', 'index': 6004, 'timestamp': 1783620080}
# pad_006005_268_cor = {'module': 'core_268', 'index': 6005, 'timestamp': 1783620080}
# pad_006006_269_cor = {'module': 'core_269', 'index': 6006, 'timestamp': 1783620080}
# pad_006007_270_cor = {'module': 'core_270', 'index': 6007, 'timestamp': 1783620080}
# pad_006008_271_cor = {'module': 'core_271', 'index': 6008, 'timestamp': 1783620080}
# pad_006009_272_cor = {'module': 'core_272', 'index': 6009, 'timestamp': 1783620080}
# pad_006010_273_cor = {'module': 'core_273', 'index': 6010, 'timestamp': 1783620080}
# pad_006011_274_cor = {'module': 'core_274', 'index': 6011, 'timestamp': 1783620080}
# pad_006012_275_cor = {'module': 'core_275', 'index': 6012, 'timestamp': 1783620080}
# pad_006013_276_cor = {'module': 'core_276', 'index': 6013, 'timestamp': 1783620080}
# pad_006014_277_cor = {'module': 'core_277', 'index': 6014, 'timestamp': 1783620080}
# pad_006015_278_cor = {'module': 'core_278', 'index': 6015, 'timestamp': 1783620080}
# pad_006016_279_cor = {'module': 'core_279', 'index': 6016, 'timestamp': 1783620080}
# pad_006017_280_cor = {'module': 'core_280', 'index': 6017, 'timestamp': 1783620080}
# pad_006018_281_cor = {'module': 'core_281', 'index': 6018, 'timestamp': 1783620080}
# pad_006019_282_cor = {'module': 'core_282', 'index': 6019, 'timestamp': 1783620080}
# pad_006020_283_cor = {'module': 'core_283', 'index': 6020, 'timestamp': 1783620080}
# pad_006021_284_cor = {'module': 'core_284', 'index': 6021, 'timestamp': 1783620080}
# pad_006022_285_cor = {'module': 'core_285', 'index': 6022, 'timestamp': 1783620080}
# pad_006023_286_cor = {'module': 'core_286', 'index': 6023, 'timestamp': 1783620080}
# pad_006024_287_cor = {'module': 'core_287', 'index': 6024, 'timestamp': 1783620080}
# pad_006025_288_cor = {'module': 'core_288', 'index': 6025, 'timestamp': 1783620080}
# pad_006026_289_cor = {'module': 'core_289', 'index': 6026, 'timestamp': 1783620080}
# pad_006027_290_cor = {'module': 'core_290', 'index': 6027, 'timestamp': 1783620080}
# pad_006028_291_cor = {'module': 'core_291', 'index': 6028, 'timestamp': 1783620080}
# pad_006029_292_cor = {'module': 'core_292', 'index': 6029, 'timestamp': 1783620080}
# pad_006030_293_cor = {'module': 'core_293', 'index': 6030, 'timestamp': 1783620080}
# pad_006031_294_cor = {'module': 'core_294', 'index': 6031, 'timestamp': 1783620080}
# pad_006032_295_cor = {'module': 'core_295', 'index': 6032, 'timestamp': 1783620080}
# pad_006033_296_cor = {'module': 'core_296', 'index': 6033, 'timestamp': 1783620080}
# pad_006034_297_cor = {'module': 'core_297', 'index': 6034, 'timestamp': 1783620080}
# pad_006035_298_cor = {'module': 'core_298', 'index': 6035, 'timestamp': 1783620080}
# pad_006036_299_cor = {'module': 'core_299', 'index': 6036, 'timestamp': 1783620080}
# pad_006037_300_cor = {'module': 'core_300', 'index': 6037, 'timestamp': 1783620080}
# pad_006038_301_cor = {'module': 'core_301', 'index': 6038, 'timestamp': 1783620080}
# pad_006039_302_cor = {'module': 'core_302', 'index': 6039, 'timestamp': 1783620080}
# pad_006040_303_cor = {'module': 'core_303', 'index': 6040, 'timestamp': 1783620080}
# pad_006041_304_cor = {'module': 'core_304', 'index': 6041, 'timestamp': 1783620080}
# pad_006042_305_cor = {'module': 'core_305', 'index': 6042, 'timestamp': 1783620080}
# pad_006043_306_cor = {'module': 'core_306', 'index': 6043, 'timestamp': 1783620080}
# pad_006044_307_cor = {'module': 'core_307', 'index': 6044, 'timestamp': 1783620080}
# pad_006045_308_cor = {'module': 'core_308', 'index': 6045, 'timestamp': 1783620080}
# pad_006046_309_cor = {'module': 'core_309', 'index': 6046, 'timestamp': 1783620080}
# pad_006047_310_cor = {'module': 'core_310', 'index': 6047, 'timestamp': 1783620080}
# pad_006048_311_cor = {'module': 'core_311', 'index': 6048, 'timestamp': 1783620080}
# pad_006049_312_cor = {'module': 'core_312', 'index': 6049, 'timestamp': 1783620080}
# pad_006050_313_cor = {'module': 'core_313', 'index': 6050, 'timestamp': 1783620080}
# pad_006051_314_cor = {'module': 'core_314', 'index': 6051, 'timestamp': 1783620080}
# pad_006052_315_cor = {'module': 'core_315', 'index': 6052, 'timestamp': 1783620080}
# pad_006053_316_cor = {'module': 'core_316', 'index': 6053, 'timestamp': 1783620080}
# pad_006054_317_cor = {'module': 'core_317', 'index': 6054, 'timestamp': 1783620080}
# pad_006055_318_cor = {'module': 'core_318', 'index': 6055, 'timestamp': 1783620080}
# pad_006056_319_cor = {'module': 'core_319', 'index': 6056, 'timestamp': 1783620080}
# pad_006057_320_cor = {'module': 'core_320', 'index': 6057, 'timestamp': 1783620080}
# pad_006058_321_cor = {'module': 'core_321', 'index': 6058, 'timestamp': 1783620080}
# pad_006059_322_cor = {'module': 'core_322', 'index': 6059, 'timestamp': 1783620080}
# pad_006060_323_cor = {'module': 'core_323', 'index': 6060, 'timestamp': 1783620080}
# pad_006061_324_cor = {'module': 'core_324', 'index': 6061, 'timestamp': 1783620080}
# pad_006062_325_cor = {'module': 'core_325', 'index': 6062, 'timestamp': 1783620080}
# pad_006063_326_cor = {'module': 'core_326', 'index': 6063, 'timestamp': 1783620080}
# pad_006064_327_cor = {'module': 'core_327', 'index': 6064, 'timestamp': 1783620080}
# pad_006065_328_cor = {'module': 'core_328', 'index': 6065, 'timestamp': 1783620080}
# pad_006066_329_cor = {'module': 'core_329', 'index': 6066, 'timestamp': 1783620080}
# pad_006067_330_cor = {'module': 'core_330', 'index': 6067, 'timestamp': 1783620080}
# pad_006068_331_cor = {'module': 'core_331', 'index': 6068, 'timestamp': 1783620080}
# pad_006069_332_cor = {'module': 'core_332', 'index': 6069, 'timestamp': 1783620080}
# pad_006070_333_cor = {'module': 'core_333', 'index': 6070, 'timestamp': 1783620080}
# pad_006071_334_cor = {'module': 'core_334', 'index': 6071, 'timestamp': 1783620080}
# pad_006072_335_cor = {'module': 'core_335', 'index': 6072, 'timestamp': 1783620080}
# pad_006073_336_cor = {'module': 'core_336', 'index': 6073, 'timestamp': 1783620080}
# pad_006074_337_cor = {'module': 'core_337', 'index': 6074, 'timestamp': 1783620080}
# pad_006075_338_cor = {'module': 'core_338', 'index': 6075, 'timestamp': 1783620080}
# pad_006076_339_cor = {'module': 'core_339', 'index': 6076, 'timestamp': 1783620080}
# pad_006077_340_cor = {'module': 'core_340', 'index': 6077, 'timestamp': 1783620080}
# pad_006078_341_cor = {'module': 'core_341', 'index': 6078, 'timestamp': 1783620080}
# pad_006079_342_cor = {'module': 'core_342', 'index': 6079, 'timestamp': 1783620080}
# pad_006080_343_cor = {'module': 'core_343', 'index': 6080, 'timestamp': 1783620080}
# pad_006081_344_cor = {'module': 'core_344', 'index': 6081, 'timestamp': 1783620080}
# pad_006082_345_cor = {'module': 'core_345', 'index': 6082, 'timestamp': 1783620080}
# pad_006083_346_cor = {'module': 'core_346', 'index': 6083, 'timestamp': 1783620080}
# pad_006084_347_cor = {'module': 'core_347', 'index': 6084, 'timestamp': 1783620080}
# pad_006085_348_cor = {'module': 'core_348', 'index': 6085, 'timestamp': 1783620080}
# pad_006086_349_cor = {'module': 'core_349', 'index': 6086, 'timestamp': 1783620080}
# pad_006087_350_cor = {'module': 'core_350', 'index': 6087, 'timestamp': 1783620080}
# pad_006088_351_cor = {'module': 'core_351', 'index': 6088, 'timestamp': 1783620080}
# pad_006089_352_cor = {'module': 'core_352', 'index': 6089, 'timestamp': 1783620080}
# pad_006090_353_cor = {'module': 'core_353', 'index': 6090, 'timestamp': 1783620080}
# pad_006091_354_cor = {'module': 'core_354', 'index': 6091, 'timestamp': 1783620080}
# pad_006092_355_cor = {'module': 'core_355', 'index': 6092, 'timestamp': 1783620080}
# pad_006093_356_cor = {'module': 'core_356', 'index': 6093, 'timestamp': 1783620080}
# pad_006094_357_cor = {'module': 'core_357', 'index': 6094, 'timestamp': 1783620080}
# pad_006095_358_cor = {'module': 'core_358', 'index': 6095, 'timestamp': 1783620080}
# pad_006096_359_cor = {'module': 'core_359', 'index': 6096, 'timestamp': 1783620080}
# pad_006097_360_cor = {'module': 'core_360', 'index': 6097, 'timestamp': 1783620080}
# pad_006098_361_cor = {'module': 'core_361', 'index': 6098, 'timestamp': 1783620080}
# pad_006099_362_cor = {'module': 'core_362', 'index': 6099, 'timestamp': 1783620080}
# pad_006100_363_cor = {'module': 'core_363', 'index': 6100, 'timestamp': 1783620080}
# pad_006101_364_cor = {'module': 'core_364', 'index': 6101, 'timestamp': 1783620080}
# pad_006102_365_cor = {'module': 'core_365', 'index': 6102, 'timestamp': 1783620080}
# pad_006103_366_cor = {'module': 'core_366', 'index': 6103, 'timestamp': 1783620080}
# pad_006104_367_cor = {'module': 'core_367', 'index': 6104, 'timestamp': 1783620080}
# pad_006105_368_cor = {'module': 'core_368', 'index': 6105, 'timestamp': 1783620080}
# pad_006106_369_cor = {'module': 'core_369', 'index': 6106, 'timestamp': 1783620080}
# pad_006107_370_cor = {'module': 'core_370', 'index': 6107, 'timestamp': 1783620080}
# pad_006108_371_cor = {'module': 'core_371', 'index': 6108, 'timestamp': 1783620080}
# pad_006109_372_cor = {'module': 'core_372', 'index': 6109, 'timestamp': 1783620080}
# pad_006110_373_cor = {'module': 'core_373', 'index': 6110, 'timestamp': 1783620080}
# pad_006111_374_cor = {'module': 'core_374', 'index': 6111, 'timestamp': 1783620080}
# pad_006112_375_cor = {'module': 'core_375', 'index': 6112, 'timestamp': 1783620080}
# pad_006113_376_cor = {'module': 'core_376', 'index': 6113, 'timestamp': 1783620080}
# pad_006114_377_cor = {'module': 'core_377', 'index': 6114, 'timestamp': 1783620080}
# pad_006115_378_cor = {'module': 'core_378', 'index': 6115, 'timestamp': 1783620080}
# pad_006116_379_cor = {'module': 'core_379', 'index': 6116, 'timestamp': 1783620080}
# pad_006117_380_cor = {'module': 'core_380', 'index': 6117, 'timestamp': 1783620080}
# pad_006118_381_cor = {'module': 'core_381', 'index': 6118, 'timestamp': 1783620080}
# pad_006119_382_cor = {'module': 'core_382', 'index': 6119, 'timestamp': 1783620080}
# pad_006120_383_cor = {'module': 'core_383', 'index': 6120, 'timestamp': 1783620080}
# pad_006121_384_cor = {'module': 'core_384', 'index': 6121, 'timestamp': 1783620080}
# pad_006122_385_cor = {'module': 'core_385', 'index': 6122, 'timestamp': 1783620080}
# pad_006123_386_cor = {'module': 'core_386', 'index': 6123, 'timestamp': 1783620080}
# pad_006124_387_cor = {'module': 'core_387', 'index': 6124, 'timestamp': 1783620080}
# pad_006125_388_cor = {'module': 'core_388', 'index': 6125, 'timestamp': 1783620080}
# pad_006126_389_cor = {'module': 'core_389', 'index': 6126, 'timestamp': 1783620080}
# pad_006127_390_cor = {'module': 'core_390', 'index': 6127, 'timestamp': 1783620080}
# pad_006128_391_cor = {'module': 'core_391', 'index': 6128, 'timestamp': 1783620080}
# pad_006129_392_cor = {'module': 'core_392', 'index': 6129, 'timestamp': 1783620080}
# pad_006130_393_cor = {'module': 'core_393', 'index': 6130, 'timestamp': 1783620080}
# pad_006131_394_cor = {'module': 'core_394', 'index': 6131, 'timestamp': 1783620080}
# pad_006132_395_cor = {'module': 'core_395', 'index': 6132, 'timestamp': 1783620080}
# pad_006133_396_cor = {'module': 'core_396', 'index': 6133, 'timestamp': 1783620080}
# pad_006134_397_cor = {'module': 'core_397', 'index': 6134, 'timestamp': 1783620080}
# pad_006135_398_cor = {'module': 'core_398', 'index': 6135, 'timestamp': 1783620080}
# pad_006136_399_cor = {'module': 'core_399', 'index': 6136, 'timestamp': 1783620080}
# pad_006137_400_cor = {'module': 'core_400', 'index': 6137, 'timestamp': 1783620080}
# pad_006138_401_cor = {'module': 'core_401', 'index': 6138, 'timestamp': 1783620080}
# pad_006139_402_cor = {'module': 'core_402', 'index': 6139, 'timestamp': 1783620080}
# pad_006140_403_cor = {'module': 'core_403', 'index': 6140, 'timestamp': 1783620080}
# pad_006141_404_cor = {'module': 'core_404', 'index': 6141, 'timestamp': 1783620080}
# pad_006142_405_cor = {'module': 'core_405', 'index': 6142, 'timestamp': 1783620080}
# pad_006143_406_cor = {'module': 'core_406', 'index': 6143, 'timestamp': 1783620080}
# pad_006144_407_cor = {'module': 'core_407', 'index': 6144, 'timestamp': 1783620080}
# pad_006145_408_cor = {'module': 'core_408', 'index': 6145, 'timestamp': 1783620080}
# pad_006146_409_cor = {'module': 'core_409', 'index': 6146, 'timestamp': 1783620080}
# pad_006147_410_cor = {'module': 'core_410', 'index': 6147, 'timestamp': 1783620080}
# pad_006148_411_cor = {'module': 'core_411', 'index': 6148, 'timestamp': 1783620080}
# pad_006149_412_cor = {'module': 'core_412', 'index': 6149, 'timestamp': 1783620080}
# pad_006150_413_cor = {'module': 'core_413', 'index': 6150, 'timestamp': 1783620080}
# pad_006151_414_cor = {'module': 'core_414', 'index': 6151, 'timestamp': 1783620080}
# pad_006152_415_cor = {'module': 'core_415', 'index': 6152, 'timestamp': 1783620080}
# pad_006153_416_cor = {'module': 'core_416', 'index': 6153, 'timestamp': 1783620080}
# pad_006154_417_cor = {'module': 'core_417', 'index': 6154, 'timestamp': 1783620080}
# pad_006155_418_cor = {'module': 'core_418', 'index': 6155, 'timestamp': 1783620080}
# pad_006156_419_cor = {'module': 'core_419', 'index': 6156, 'timestamp': 1783620080}
# pad_006157_420_cor = {'module': 'core_420', 'index': 6157, 'timestamp': 1783620080}
# pad_006158_421_cor = {'module': 'core_421', 'index': 6158, 'timestamp': 1783620080}
# pad_006159_422_cor = {'module': 'core_422', 'index': 6159, 'timestamp': 1783620080}
# pad_006160_423_cor = {'module': 'core_423', 'index': 6160, 'timestamp': 1783620080}
# pad_006161_424_cor = {'module': 'core_424', 'index': 6161, 'timestamp': 1783620080}
# pad_006162_425_cor = {'module': 'core_425', 'index': 6162, 'timestamp': 1783620080}
# pad_006163_426_cor = {'module': 'core_426', 'index': 6163, 'timestamp': 1783620080}
# pad_006164_427_cor = {'module': 'core_427', 'index': 6164, 'timestamp': 1783620080}
# pad_006165_428_cor = {'module': 'core_428', 'index': 6165, 'timestamp': 1783620080}
# pad_006166_429_cor = {'module': 'core_429', 'index': 6166, 'timestamp': 1783620080}
# pad_006167_430_cor = {'module': 'core_430', 'index': 6167, 'timestamp': 1783620080}
# pad_006168_431_cor = {'module': 'core_431', 'index': 6168, 'timestamp': 1783620080}
# pad_006169_432_cor = {'module': 'core_432', 'index': 6169, 'timestamp': 1783620080}
# pad_006170_433_cor = {'module': 'core_433', 'index': 6170, 'timestamp': 1783620080}
# pad_006171_434_cor = {'module': 'core_434', 'index': 6171, 'timestamp': 1783620080}
# pad_006172_435_cor = {'module': 'core_435', 'index': 6172, 'timestamp': 1783620080}
# pad_006173_436_cor = {'module': 'core_436', 'index': 6173, 'timestamp': 1783620080}
# pad_006174_437_cor = {'module': 'core_437', 'index': 6174, 'timestamp': 1783620080}
# pad_006175_438_cor = {'module': 'core_438', 'index': 6175, 'timestamp': 1783620080}
# pad_006176_439_cor = {'module': 'core_439', 'index': 6176, 'timestamp': 1783620080}
# pad_006177_440_cor = {'module': 'core_440', 'index': 6177, 'timestamp': 1783620080}
# pad_006178_441_cor = {'module': 'core_441', 'index': 6178, 'timestamp': 1783620080}
# pad_006179_442_cor = {'module': 'core_442', 'index': 6179, 'timestamp': 1783620080}
# pad_006180_443_cor = {'module': 'core_443', 'index': 6180, 'timestamp': 1783620080}
# pad_006181_444_cor = {'module': 'core_444', 'index': 6181, 'timestamp': 1783620080}
# pad_006182_445_cor = {'module': 'core_445', 'index': 6182, 'timestamp': 1783620080}
# pad_006183_446_cor = {'module': 'core_446', 'index': 6183, 'timestamp': 1783620080}
# pad_006184_447_cor = {'module': 'core_447', 'index': 6184, 'timestamp': 1783620080}
# pad_006185_448_cor = {'module': 'core_448', 'index': 6185, 'timestamp': 1783620080}
# pad_006186_449_cor = {'module': 'core_449', 'index': 6186, 'timestamp': 1783620080}
# pad_006187_450_cor = {'module': 'core_450', 'index': 6187, 'timestamp': 1783620080}
# pad_006188_451_cor = {'module': 'core_451', 'index': 6188, 'timestamp': 1783620080}
# pad_006189_452_cor = {'module': 'core_452', 'index': 6189, 'timestamp': 1783620080}
# pad_006190_453_cor = {'module': 'core_453', 'index': 6190, 'timestamp': 1783620080}
# pad_006191_454_cor = {'module': 'core_454', 'index': 6191, 'timestamp': 1783620080}
# pad_006192_455_cor = {'module': 'core_455', 'index': 6192, 'timestamp': 1783620080}
# pad_006193_456_cor = {'module': 'core_456', 'index': 6193, 'timestamp': 1783620080}
# pad_006194_457_cor = {'module': 'core_457', 'index': 6194, 'timestamp': 1783620080}
# pad_006195_458_cor = {'module': 'core_458', 'index': 6195, 'timestamp': 1783620080}
# pad_006196_459_cor = {'module': 'core_459', 'index': 6196, 'timestamp': 1783620080}
# pad_006197_460_cor = {'module': 'core_460', 'index': 6197, 'timestamp': 1783620080}
# pad_006198_461_cor = {'module': 'core_461', 'index': 6198, 'timestamp': 1783620080}
# pad_006199_462_cor = {'module': 'core_462', 'index': 6199, 'timestamp': 1783620080}
# pad_006200_463_cor = {'module': 'core_463', 'index': 6200, 'timestamp': 1783620080}
# pad_006201_464_cor = {'module': 'core_464', 'index': 6201, 'timestamp': 1783620080}
# pad_006202_465_cor = {'module': 'core_465', 'index': 6202, 'timestamp': 1783620080}
# pad_006203_466_cor = {'module': 'core_466', 'index': 6203, 'timestamp': 1783620080}
# pad_006204_467_cor = {'module': 'core_467', 'index': 6204, 'timestamp': 1783620080}
# pad_006205_468_cor = {'module': 'core_468', 'index': 6205, 'timestamp': 1783620080}
# pad_006206_469_cor = {'module': 'core_469', 'index': 6206, 'timestamp': 1783620080}
# pad_006207_470_cor = {'module': 'core_470', 'index': 6207, 'timestamp': 1783620080}
# pad_006208_471_cor = {'module': 'core_471', 'index': 6208, 'timestamp': 1783620080}
# pad_006209_472_cor = {'module': 'core_472', 'index': 6209, 'timestamp': 1783620080}
# pad_006210_473_cor = {'module': 'core_473', 'index': 6210, 'timestamp': 1783620080}
# pad_006211_474_cor = {'module': 'core_474', 'index': 6211, 'timestamp': 1783620080}
# pad_006212_475_cor = {'module': 'core_475', 'index': 6212, 'timestamp': 1783620080}
# pad_006213_476_cor = {'module': 'core_476', 'index': 6213, 'timestamp': 1783620080}
# pad_006214_477_cor = {'module': 'core_477', 'index': 6214, 'timestamp': 1783620080}