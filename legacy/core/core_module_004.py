"""
core_module_004.py - legacy core #4
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C4_0=42
T4_0="t0_4"
F4_0=True
C4_1=49
T4_1="t1_4"
F4_1=False
C4_2=56
T4_2="t2_4"
F4_2=True
C4_3=63
T4_3="t3_4"
F4_3=False
C4_4=70
T4_4="t4_4"
F4_4=True
C4_5=77
T4_5="t5_4"
F4_5=False
C4_6=84
T4_6="t6_4"
F4_6=True
C4_7=91
T4_7="t7_4"
F4_7=False
C4_8=98
T4_8="t8_4"
F4_8=True
C4_9=105
T4_9="t9_4"
F4_9=False
C4_10=112
T4_10="t10_4"
F4_10=True
C4_11=119
T4_11="t11_4"
F4_11=False
C4_12=126
T4_12="t12_4"
F4_12=True
C4_13=133
T4_13="t13_4"
F4_13=False
C4_14=140
T4_14="t14_4"
F4_14=True

def proc_cor_004_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_004_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":4}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*4+j+fi)%500
    r.append(v*2+C4_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":4}
def hlp_proc_cor_004_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR004000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR004000._lk:LegCOR004000._c+=1;self._i=LegCOR004000._c
  self.n=nm or f"LegCOR004000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*4+j+ci)%50
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

class LegCOR004001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR004001._lk:LegCOR004001._c+=1;self._i=LegCOR004001._c
  self.n=nm or f"LegCOR004001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*4+j+ci)%50
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

class LegCOR004002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR004002._lk:LegCOR004002._c+=1;self._i=LegCOR004002._c
  self.n=nm or f"LegCOR004002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*4+j+ci)%50
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

class LegCOR004003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR004003._lk:LegCOR004003._c+=1;self._i=LegCOR004003._c
  self.n=nm or f"LegCOR004003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*4+j+ci)%50
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

def val_cor_004_0000(d,s=None,st=True):
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

def val_cor_004_0001(d,s=None,st=True):
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

def val_cor_004_0002(d,s=None,st=True):
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

def val_cor_004_0003(d,s=None,st=True):
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

def val_cor_004_0004(d,s=None,st=True):
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

def val_cor_004_0005(d,s=None,st=True):
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

M004={
 "id":4,"d":"core","n":"core_module_004","v":"3.8"
}# pad_001435_000_cor = {'module': 'core_000', 'index': 1435, 'timestamp': 1783620080}
# pad_001436_001_cor = {'module': 'core_001', 'index': 1436, 'timestamp': 1783620080}
# pad_001437_002_cor = {'module': 'core_002', 'index': 1437, 'timestamp': 1783620080}
# pad_001438_003_cor = {'module': 'core_003', 'index': 1438, 'timestamp': 1783620080}
# pad_001439_004_cor = {'module': 'core_004', 'index': 1439, 'timestamp': 1783620080}
# pad_001440_005_cor = {'module': 'core_005', 'index': 1440, 'timestamp': 1783620080}
# pad_001441_006_cor = {'module': 'core_006', 'index': 1441, 'timestamp': 1783620080}
# pad_001442_007_cor = {'module': 'core_007', 'index': 1442, 'timestamp': 1783620080}
# pad_001443_008_cor = {'module': 'core_008', 'index': 1443, 'timestamp': 1783620080}
# pad_001444_009_cor = {'module': 'core_009', 'index': 1444, 'timestamp': 1783620080}
# pad_001445_010_cor = {'module': 'core_010', 'index': 1445, 'timestamp': 1783620080}
# pad_001446_011_cor = {'module': 'core_011', 'index': 1446, 'timestamp': 1783620080}
# pad_001447_012_cor = {'module': 'core_012', 'index': 1447, 'timestamp': 1783620080}
# pad_001448_013_cor = {'module': 'core_013', 'index': 1448, 'timestamp': 1783620080}
# pad_001449_014_cor = {'module': 'core_014', 'index': 1449, 'timestamp': 1783620080}
# pad_001450_015_cor = {'module': 'core_015', 'index': 1450, 'timestamp': 1783620080}
# pad_001451_016_cor = {'module': 'core_016', 'index': 1451, 'timestamp': 1783620080}
# pad_001452_017_cor = {'module': 'core_017', 'index': 1452, 'timestamp': 1783620080}
# pad_001453_018_cor = {'module': 'core_018', 'index': 1453, 'timestamp': 1783620080}
# pad_001454_019_cor = {'module': 'core_019', 'index': 1454, 'timestamp': 1783620080}
# pad_001455_020_cor = {'module': 'core_020', 'index': 1455, 'timestamp': 1783620080}
# pad_001456_021_cor = {'module': 'core_021', 'index': 1456, 'timestamp': 1783620080}
# pad_001457_022_cor = {'module': 'core_022', 'index': 1457, 'timestamp': 1783620080}
# pad_001458_023_cor = {'module': 'core_023', 'index': 1458, 'timestamp': 1783620080}
# pad_001459_024_cor = {'module': 'core_024', 'index': 1459, 'timestamp': 1783620080}
# pad_001460_025_cor = {'module': 'core_025', 'index': 1460, 'timestamp': 1783620080}
# pad_001461_026_cor = {'module': 'core_026', 'index': 1461, 'timestamp': 1783620080}
# pad_001462_027_cor = {'module': 'core_027', 'index': 1462, 'timestamp': 1783620080}
# pad_001463_028_cor = {'module': 'core_028', 'index': 1463, 'timestamp': 1783620080}
# pad_001464_029_cor = {'module': 'core_029', 'index': 1464, 'timestamp': 1783620080}
# pad_001465_030_cor = {'module': 'core_030', 'index': 1465, 'timestamp': 1783620080}
# pad_001466_031_cor = {'module': 'core_031', 'index': 1466, 'timestamp': 1783620080}
# pad_001467_032_cor = {'module': 'core_032', 'index': 1467, 'timestamp': 1783620080}
# pad_001468_033_cor = {'module': 'core_033', 'index': 1468, 'timestamp': 1783620080}
# pad_001469_034_cor = {'module': 'core_034', 'index': 1469, 'timestamp': 1783620080}
# pad_001470_035_cor = {'module': 'core_035', 'index': 1470, 'timestamp': 1783620080}
# pad_001471_036_cor = {'module': 'core_036', 'index': 1471, 'timestamp': 1783620080}
# pad_001472_037_cor = {'module': 'core_037', 'index': 1472, 'timestamp': 1783620080}
# pad_001473_038_cor = {'module': 'core_038', 'index': 1473, 'timestamp': 1783620080}
# pad_001474_039_cor = {'module': 'core_039', 'index': 1474, 'timestamp': 1783620080}
# pad_001475_040_cor = {'module': 'core_040', 'index': 1475, 'timestamp': 1783620080}
# pad_001476_041_cor = {'module': 'core_041', 'index': 1476, 'timestamp': 1783620080}
# pad_001477_042_cor = {'module': 'core_042', 'index': 1477, 'timestamp': 1783620080}
# pad_001478_043_cor = {'module': 'core_043', 'index': 1478, 'timestamp': 1783620080}
# pad_001479_044_cor = {'module': 'core_044', 'index': 1479, 'timestamp': 1783620080}
# pad_001480_045_cor = {'module': 'core_045', 'index': 1480, 'timestamp': 1783620080}
# pad_001481_046_cor = {'module': 'core_046', 'index': 1481, 'timestamp': 1783620080}
# pad_001482_047_cor = {'module': 'core_047', 'index': 1482, 'timestamp': 1783620080}
# pad_001483_048_cor = {'module': 'core_048', 'index': 1483, 'timestamp': 1783620080}
# pad_001484_049_cor = {'module': 'core_049', 'index': 1484, 'timestamp': 1783620080}
# pad_001485_050_cor = {'module': 'core_050', 'index': 1485, 'timestamp': 1783620080}
# pad_001486_051_cor = {'module': 'core_051', 'index': 1486, 'timestamp': 1783620080}
# pad_001487_052_cor = {'module': 'core_052', 'index': 1487, 'timestamp': 1783620080}
# pad_001488_053_cor = {'module': 'core_053', 'index': 1488, 'timestamp': 1783620080}
# pad_001489_054_cor = {'module': 'core_054', 'index': 1489, 'timestamp': 1783620080}
# pad_001490_055_cor = {'module': 'core_055', 'index': 1490, 'timestamp': 1783620080}
# pad_001491_056_cor = {'module': 'core_056', 'index': 1491, 'timestamp': 1783620080}
# pad_001492_057_cor = {'module': 'core_057', 'index': 1492, 'timestamp': 1783620080}
# pad_001493_058_cor = {'module': 'core_058', 'index': 1493, 'timestamp': 1783620080}
# pad_001494_059_cor = {'module': 'core_059', 'index': 1494, 'timestamp': 1783620080}
# pad_001495_060_cor = {'module': 'core_060', 'index': 1495, 'timestamp': 1783620080}
# pad_001496_061_cor = {'module': 'core_061', 'index': 1496, 'timestamp': 1783620080}
# pad_001497_062_cor = {'module': 'core_062', 'index': 1497, 'timestamp': 1783620080}
# pad_001498_063_cor = {'module': 'core_063', 'index': 1498, 'timestamp': 1783620080}
# pad_001499_064_cor = {'module': 'core_064', 'index': 1499, 'timestamp': 1783620080}
# pad_001500_065_cor = {'module': 'core_065', 'index': 1500, 'timestamp': 1783620080}
# pad_001501_066_cor = {'module': 'core_066', 'index': 1501, 'timestamp': 1783620080}
# pad_001502_067_cor = {'module': 'core_067', 'index': 1502, 'timestamp': 1783620080}
# pad_001503_068_cor = {'module': 'core_068', 'index': 1503, 'timestamp': 1783620080}
# pad_001504_069_cor = {'module': 'core_069', 'index': 1504, 'timestamp': 1783620080}
# pad_001505_070_cor = {'module': 'core_070', 'index': 1505, 'timestamp': 1783620080}
# pad_001506_071_cor = {'module': 'core_071', 'index': 1506, 'timestamp': 1783620080}
# pad_001507_072_cor = {'module': 'core_072', 'index': 1507, 'timestamp': 1783620080}
# pad_001508_073_cor = {'module': 'core_073', 'index': 1508, 'timestamp': 1783620080}
# pad_001509_074_cor = {'module': 'core_074', 'index': 1509, 'timestamp': 1783620080}
# pad_001510_075_cor = {'module': 'core_075', 'index': 1510, 'timestamp': 1783620080}
# pad_001511_076_cor = {'module': 'core_076', 'index': 1511, 'timestamp': 1783620080}
# pad_001512_077_cor = {'module': 'core_077', 'index': 1512, 'timestamp': 1783620080}
# pad_001513_078_cor = {'module': 'core_078', 'index': 1513, 'timestamp': 1783620080}
# pad_001514_079_cor = {'module': 'core_079', 'index': 1514, 'timestamp': 1783620080}
# pad_001515_080_cor = {'module': 'core_080', 'index': 1515, 'timestamp': 1783620080}
# pad_001516_081_cor = {'module': 'core_081', 'index': 1516, 'timestamp': 1783620080}
# pad_001517_082_cor = {'module': 'core_082', 'index': 1517, 'timestamp': 1783620080}
# pad_001518_083_cor = {'module': 'core_083', 'index': 1518, 'timestamp': 1783620080}
# pad_001519_084_cor = {'module': 'core_084', 'index': 1519, 'timestamp': 1783620080}
# pad_001520_085_cor = {'module': 'core_085', 'index': 1520, 'timestamp': 1783620080}
# pad_001521_086_cor = {'module': 'core_086', 'index': 1521, 'timestamp': 1783620080}
# pad_001522_087_cor = {'module': 'core_087', 'index': 1522, 'timestamp': 1783620080}
# pad_001523_088_cor = {'module': 'core_088', 'index': 1523, 'timestamp': 1783620080}
# pad_001524_089_cor = {'module': 'core_089', 'index': 1524, 'timestamp': 1783620080}
# pad_001525_090_cor = {'module': 'core_090', 'index': 1525, 'timestamp': 1783620080}
# pad_001526_091_cor = {'module': 'core_091', 'index': 1526, 'timestamp': 1783620080}
# pad_001527_092_cor = {'module': 'core_092', 'index': 1527, 'timestamp': 1783620080}
# pad_001528_093_cor = {'module': 'core_093', 'index': 1528, 'timestamp': 1783620080}
# pad_001529_094_cor = {'module': 'core_094', 'index': 1529, 'timestamp': 1783620080}
# pad_001530_095_cor = {'module': 'core_095', 'index': 1530, 'timestamp': 1783620080}
# pad_001531_096_cor = {'module': 'core_096', 'index': 1531, 'timestamp': 1783620080}
# pad_001532_097_cor = {'module': 'core_097', 'index': 1532, 'timestamp': 1783620080}
# pad_001533_098_cor = {'module': 'core_098', 'index': 1533, 'timestamp': 1783620080}
# pad_001534_099_cor = {'module': 'core_099', 'index': 1534, 'timestamp': 1783620080}
# pad_001535_100_cor = {'module': 'core_100', 'index': 1535, 'timestamp': 1783620080}
# pad_001536_101_cor = {'module': 'core_101', 'index': 1536, 'timestamp': 1783620080}
# pad_001537_102_cor = {'module': 'core_102', 'index': 1537, 'timestamp': 1783620080}
# pad_001538_103_cor = {'module': 'core_103', 'index': 1538, 'timestamp': 1783620080}
# pad_001539_104_cor = {'module': 'core_104', 'index': 1539, 'timestamp': 1783620080}
# pad_001540_105_cor = {'module': 'core_105', 'index': 1540, 'timestamp': 1783620080}
# pad_001541_106_cor = {'module': 'core_106', 'index': 1541, 'timestamp': 1783620080}
# pad_001542_107_cor = {'module': 'core_107', 'index': 1542, 'timestamp': 1783620080}
# pad_001543_108_cor = {'module': 'core_108', 'index': 1543, 'timestamp': 1783620080}
# pad_001544_109_cor = {'module': 'core_109', 'index': 1544, 'timestamp': 1783620080}
# pad_001545_110_cor = {'module': 'core_110', 'index': 1545, 'timestamp': 1783620080}
# pad_001546_111_cor = {'module': 'core_111', 'index': 1546, 'timestamp': 1783620080}
# pad_001547_112_cor = {'module': 'core_112', 'index': 1547, 'timestamp': 1783620080}
# pad_001548_113_cor = {'module': 'core_113', 'index': 1548, 'timestamp': 1783620080}
# pad_001549_114_cor = {'module': 'core_114', 'index': 1549, 'timestamp': 1783620080}
# pad_001550_115_cor = {'module': 'core_115', 'index': 1550, 'timestamp': 1783620080}
# pad_001551_116_cor = {'module': 'core_116', 'index': 1551, 'timestamp': 1783620080}
# pad_001552_117_cor = {'module': 'core_117', 'index': 1552, 'timestamp': 1783620080}
# pad_001553_118_cor = {'module': 'core_118', 'index': 1553, 'timestamp': 1783620080}
# pad_001554_119_cor = {'module': 'core_119', 'index': 1554, 'timestamp': 1783620080}
# pad_001555_120_cor = {'module': 'core_120', 'index': 1555, 'timestamp': 1783620080}
# pad_001556_121_cor = {'module': 'core_121', 'index': 1556, 'timestamp': 1783620080}
# pad_001557_122_cor = {'module': 'core_122', 'index': 1557, 'timestamp': 1783620080}
# pad_001558_123_cor = {'module': 'core_123', 'index': 1558, 'timestamp': 1783620080}
# pad_001559_124_cor = {'module': 'core_124', 'index': 1559, 'timestamp': 1783620080}
# pad_001560_125_cor = {'module': 'core_125', 'index': 1560, 'timestamp': 1783620080}
# pad_001561_126_cor = {'module': 'core_126', 'index': 1561, 'timestamp': 1783620080}
# pad_001562_127_cor = {'module': 'core_127', 'index': 1562, 'timestamp': 1783620080}
# pad_001563_128_cor = {'module': 'core_128', 'index': 1563, 'timestamp': 1783620080}
# pad_001564_129_cor = {'module': 'core_129', 'index': 1564, 'timestamp': 1783620080}
# pad_001565_130_cor = {'module': 'core_130', 'index': 1565, 'timestamp': 1783620080}
# pad_001566_131_cor = {'module': 'core_131', 'index': 1566, 'timestamp': 1783620080}
# pad_001567_132_cor = {'module': 'core_132', 'index': 1567, 'timestamp': 1783620080}
# pad_001568_133_cor = {'module': 'core_133', 'index': 1568, 'timestamp': 1783620080}
# pad_001569_134_cor = {'module': 'core_134', 'index': 1569, 'timestamp': 1783620080}
# pad_001570_135_cor = {'module': 'core_135', 'index': 1570, 'timestamp': 1783620080}
# pad_001571_136_cor = {'module': 'core_136', 'index': 1571, 'timestamp': 1783620080}
# pad_001572_137_cor = {'module': 'core_137', 'index': 1572, 'timestamp': 1783620080}
# pad_001573_138_cor = {'module': 'core_138', 'index': 1573, 'timestamp': 1783620080}
# pad_001574_139_cor = {'module': 'core_139', 'index': 1574, 'timestamp': 1783620080}
# pad_001575_140_cor = {'module': 'core_140', 'index': 1575, 'timestamp': 1783620080}
# pad_001576_141_cor = {'module': 'core_141', 'index': 1576, 'timestamp': 1783620080}
# pad_001577_142_cor = {'module': 'core_142', 'index': 1577, 'timestamp': 1783620080}
# pad_001578_143_cor = {'module': 'core_143', 'index': 1578, 'timestamp': 1783620080}
# pad_001579_144_cor = {'module': 'core_144', 'index': 1579, 'timestamp': 1783620080}
# pad_001580_145_cor = {'module': 'core_145', 'index': 1580, 'timestamp': 1783620080}
# pad_001581_146_cor = {'module': 'core_146', 'index': 1581, 'timestamp': 1783620080}
# pad_001582_147_cor = {'module': 'core_147', 'index': 1582, 'timestamp': 1783620080}
# pad_001583_148_cor = {'module': 'core_148', 'index': 1583, 'timestamp': 1783620080}
# pad_001584_149_cor = {'module': 'core_149', 'index': 1584, 'timestamp': 1783620080}
# pad_001585_150_cor = {'module': 'core_150', 'index': 1585, 'timestamp': 1783620080}
# pad_001586_151_cor = {'module': 'core_151', 'index': 1586, 'timestamp': 1783620080}
# pad_001587_152_cor = {'module': 'core_152', 'index': 1587, 'timestamp': 1783620080}
# pad_001588_153_cor = {'module': 'core_153', 'index': 1588, 'timestamp': 1783620080}
# pad_001589_154_cor = {'module': 'core_154', 'index': 1589, 'timestamp': 1783620080}
# pad_001590_155_cor = {'module': 'core_155', 'index': 1590, 'timestamp': 1783620080}
# pad_001591_156_cor = {'module': 'core_156', 'index': 1591, 'timestamp': 1783620080}
# pad_001592_157_cor = {'module': 'core_157', 'index': 1592, 'timestamp': 1783620080}
# pad_001593_158_cor = {'module': 'core_158', 'index': 1593, 'timestamp': 1783620080}
# pad_001594_159_cor = {'module': 'core_159', 'index': 1594, 'timestamp': 1783620080}
# pad_001595_160_cor = {'module': 'core_160', 'index': 1595, 'timestamp': 1783620080}
# pad_001596_161_cor = {'module': 'core_161', 'index': 1596, 'timestamp': 1783620080}
# pad_001597_162_cor = {'module': 'core_162', 'index': 1597, 'timestamp': 1783620080}
# pad_001598_163_cor = {'module': 'core_163', 'index': 1598, 'timestamp': 1783620080}
# pad_001599_164_cor = {'module': 'core_164', 'index': 1599, 'timestamp': 1783620080}
# pad_001600_165_cor = {'module': 'core_165', 'index': 1600, 'timestamp': 1783620080}
# pad_001601_166_cor = {'module': 'core_166', 'index': 1601, 'timestamp': 1783620080}
# pad_001602_167_cor = {'module': 'core_167', 'index': 1602, 'timestamp': 1783620080}
# pad_001603_168_cor = {'module': 'core_168', 'index': 1603, 'timestamp': 1783620080}
# pad_001604_169_cor = {'module': 'core_169', 'index': 1604, 'timestamp': 1783620080}
# pad_001605_170_cor = {'module': 'core_170', 'index': 1605, 'timestamp': 1783620080}
# pad_001606_171_cor = {'module': 'core_171', 'index': 1606, 'timestamp': 1783620080}
# pad_001607_172_cor = {'module': 'core_172', 'index': 1607, 'timestamp': 1783620080}
# pad_001608_173_cor = {'module': 'core_173', 'index': 1608, 'timestamp': 1783620080}
# pad_001609_174_cor = {'module': 'core_174', 'index': 1609, 'timestamp': 1783620080}
# pad_001610_175_cor = {'module': 'core_175', 'index': 1610, 'timestamp': 1783620080}
# pad_001611_176_cor = {'module': 'core_176', 'index': 1611, 'timestamp': 1783620080}
# pad_001612_177_cor = {'module': 'core_177', 'index': 1612, 'timestamp': 1783620080}
# pad_001613_178_cor = {'module': 'core_178', 'index': 1613, 'timestamp': 1783620080}
# pad_001614_179_cor = {'module': 'core_179', 'index': 1614, 'timestamp': 1783620080}
# pad_001615_180_cor = {'module': 'core_180', 'index': 1615, 'timestamp': 1783620080}
# pad_001616_181_cor = {'module': 'core_181', 'index': 1616, 'timestamp': 1783620080}
# pad_001617_182_cor = {'module': 'core_182', 'index': 1617, 'timestamp': 1783620080}
# pad_001618_183_cor = {'module': 'core_183', 'index': 1618, 'timestamp': 1783620080}
# pad_001619_184_cor = {'module': 'core_184', 'index': 1619, 'timestamp': 1783620080}
# pad_001620_185_cor = {'module': 'core_185', 'index': 1620, 'timestamp': 1783620080}
# pad_001621_186_cor = {'module': 'core_186', 'index': 1621, 'timestamp': 1783620080}
# pad_001622_187_cor = {'module': 'core_187', 'index': 1622, 'timestamp': 1783620080}
# pad_001623_188_cor = {'module': 'core_188', 'index': 1623, 'timestamp': 1783620080}
# pad_001624_189_cor = {'module': 'core_189', 'index': 1624, 'timestamp': 1783620080}
# pad_001625_190_cor = {'module': 'core_190', 'index': 1625, 'timestamp': 1783620080}
# pad_001626_191_cor = {'module': 'core_191', 'index': 1626, 'timestamp': 1783620080}
# pad_001627_192_cor = {'module': 'core_192', 'index': 1627, 'timestamp': 1783620080}
# pad_001628_193_cor = {'module': 'core_193', 'index': 1628, 'timestamp': 1783620080}
# pad_001629_194_cor = {'module': 'core_194', 'index': 1629, 'timestamp': 1783620080}
# pad_001630_195_cor = {'module': 'core_195', 'index': 1630, 'timestamp': 1783620080}
# pad_001631_196_cor = {'module': 'core_196', 'index': 1631, 'timestamp': 1783620080}
# pad_001632_197_cor = {'module': 'core_197', 'index': 1632, 'timestamp': 1783620080}
# pad_001633_198_cor = {'module': 'core_198', 'index': 1633, 'timestamp': 1783620080}
# pad_001634_199_cor = {'module': 'core_199', 'index': 1634, 'timestamp': 1783620080}
# pad_001635_200_cor = {'module': 'core_200', 'index': 1635, 'timestamp': 1783620080}
# pad_001636_201_cor = {'module': 'core_201', 'index': 1636, 'timestamp': 1783620080}
# pad_001637_202_cor = {'module': 'core_202', 'index': 1637, 'timestamp': 1783620080}
# pad_001638_203_cor = {'module': 'core_203', 'index': 1638, 'timestamp': 1783620080}
# pad_001639_204_cor = {'module': 'core_204', 'index': 1639, 'timestamp': 1783620080}
# pad_001640_205_cor = {'module': 'core_205', 'index': 1640, 'timestamp': 1783620080}
# pad_001641_206_cor = {'module': 'core_206', 'index': 1641, 'timestamp': 1783620080}
# pad_001642_207_cor = {'module': 'core_207', 'index': 1642, 'timestamp': 1783620080}
# pad_001643_208_cor = {'module': 'core_208', 'index': 1643, 'timestamp': 1783620080}
# pad_001644_209_cor = {'module': 'core_209', 'index': 1644, 'timestamp': 1783620080}
# pad_001645_210_cor = {'module': 'core_210', 'index': 1645, 'timestamp': 1783620080}
# pad_001646_211_cor = {'module': 'core_211', 'index': 1646, 'timestamp': 1783620080}
# pad_001647_212_cor = {'module': 'core_212', 'index': 1647, 'timestamp': 1783620080}
# pad_001648_213_cor = {'module': 'core_213', 'index': 1648, 'timestamp': 1783620080}
# pad_001649_214_cor = {'module': 'core_214', 'index': 1649, 'timestamp': 1783620080}
# pad_001650_215_cor = {'module': 'core_215', 'index': 1650, 'timestamp': 1783620080}
# pad_001651_216_cor = {'module': 'core_216', 'index': 1651, 'timestamp': 1783620080}
# pad_001652_217_cor = {'module': 'core_217', 'index': 1652, 'timestamp': 1783620080}
# pad_001653_218_cor = {'module': 'core_218', 'index': 1653, 'timestamp': 1783620080}
# pad_001654_219_cor = {'module': 'core_219', 'index': 1654, 'timestamp': 1783620080}
# pad_001655_220_cor = {'module': 'core_220', 'index': 1655, 'timestamp': 1783620080}
# pad_001656_221_cor = {'module': 'core_221', 'index': 1656, 'timestamp': 1783620080}
# pad_001657_222_cor = {'module': 'core_222', 'index': 1657, 'timestamp': 1783620080}
# pad_001658_223_cor = {'module': 'core_223', 'index': 1658, 'timestamp': 1783620080}
# pad_001659_224_cor = {'module': 'core_224', 'index': 1659, 'timestamp': 1783620080}
# pad_001660_225_cor = {'module': 'core_225', 'index': 1660, 'timestamp': 1783620080}
# pad_001661_226_cor = {'module': 'core_226', 'index': 1661, 'timestamp': 1783620080}
# pad_001662_227_cor = {'module': 'core_227', 'index': 1662, 'timestamp': 1783620080}
# pad_001663_228_cor = {'module': 'core_228', 'index': 1663, 'timestamp': 1783620080}
# pad_001664_229_cor = {'module': 'core_229', 'index': 1664, 'timestamp': 1783620080}
# pad_001665_230_cor = {'module': 'core_230', 'index': 1665, 'timestamp': 1783620080}
# pad_001666_231_cor = {'module': 'core_231', 'index': 1666, 'timestamp': 1783620080}
# pad_001667_232_cor = {'module': 'core_232', 'index': 1667, 'timestamp': 1783620080}
# pad_001668_233_cor = {'module': 'core_233', 'index': 1668, 'timestamp': 1783620080}
# pad_001669_234_cor = {'module': 'core_234', 'index': 1669, 'timestamp': 1783620080}
# pad_001670_235_cor = {'module': 'core_235', 'index': 1670, 'timestamp': 1783620080}
# pad_001671_236_cor = {'module': 'core_236', 'index': 1671, 'timestamp': 1783620080}
# pad_001672_237_cor = {'module': 'core_237', 'index': 1672, 'timestamp': 1783620080}
# pad_001673_238_cor = {'module': 'core_238', 'index': 1673, 'timestamp': 1783620080}
# pad_001674_239_cor = {'module': 'core_239', 'index': 1674, 'timestamp': 1783620080}
# pad_001675_240_cor = {'module': 'core_240', 'index': 1675, 'timestamp': 1783620080}
# pad_001676_241_cor = {'module': 'core_241', 'index': 1676, 'timestamp': 1783620080}
# pad_001677_242_cor = {'module': 'core_242', 'index': 1677, 'timestamp': 1783620080}
# pad_001678_243_cor = {'module': 'core_243', 'index': 1678, 'timestamp': 1783620080}
# pad_001679_244_cor = {'module': 'core_244', 'index': 1679, 'timestamp': 1783620080}
# pad_001680_245_cor = {'module': 'core_245', 'index': 1680, 'timestamp': 1783620080}
# pad_001681_246_cor = {'module': 'core_246', 'index': 1681, 'timestamp': 1783620080}
# pad_001682_247_cor = {'module': 'core_247', 'index': 1682, 'timestamp': 1783620080}
# pad_001683_248_cor = {'module': 'core_248', 'index': 1683, 'timestamp': 1783620080}
# pad_001684_249_cor = {'module': 'core_249', 'index': 1684, 'timestamp': 1783620080}
# pad_001685_250_cor = {'module': 'core_250', 'index': 1685, 'timestamp': 1783620080}
# pad_001686_251_cor = {'module': 'core_251', 'index': 1686, 'timestamp': 1783620080}
# pad_001687_252_cor = {'module': 'core_252', 'index': 1687, 'timestamp': 1783620080}
# pad_001688_253_cor = {'module': 'core_253', 'index': 1688, 'timestamp': 1783620080}
# pad_001689_254_cor = {'module': 'core_254', 'index': 1689, 'timestamp': 1783620080}
# pad_001690_255_cor = {'module': 'core_255', 'index': 1690, 'timestamp': 1783620080}
# pad_001691_256_cor = {'module': 'core_256', 'index': 1691, 'timestamp': 1783620080}
# pad_001692_257_cor = {'module': 'core_257', 'index': 1692, 'timestamp': 1783620080}
# pad_001693_258_cor = {'module': 'core_258', 'index': 1693, 'timestamp': 1783620080}
# pad_001694_259_cor = {'module': 'core_259', 'index': 1694, 'timestamp': 1783620080}
# pad_001695_260_cor = {'module': 'core_260', 'index': 1695, 'timestamp': 1783620080}
# pad_001696_261_cor = {'module': 'core_261', 'index': 1696, 'timestamp': 1783620080}
# pad_001697_262_cor = {'module': 'core_262', 'index': 1697, 'timestamp': 1783620080}
# pad_001698_263_cor = {'module': 'core_263', 'index': 1698, 'timestamp': 1783620080}
# pad_001699_264_cor = {'module': 'core_264', 'index': 1699, 'timestamp': 1783620080}
# pad_001700_265_cor = {'module': 'core_265', 'index': 1700, 'timestamp': 1783620080}
# pad_001701_266_cor = {'module': 'core_266', 'index': 1701, 'timestamp': 1783620080}
# pad_001702_267_cor = {'module': 'core_267', 'index': 1702, 'timestamp': 1783620080}
# pad_001703_268_cor = {'module': 'core_268', 'index': 1703, 'timestamp': 1783620080}
# pad_001704_269_cor = {'module': 'core_269', 'index': 1704, 'timestamp': 1783620080}
# pad_001705_270_cor = {'module': 'core_270', 'index': 1705, 'timestamp': 1783620080}
# pad_001706_271_cor = {'module': 'core_271', 'index': 1706, 'timestamp': 1783620080}
# pad_001707_272_cor = {'module': 'core_272', 'index': 1707, 'timestamp': 1783620080}
# pad_001708_273_cor = {'module': 'core_273', 'index': 1708, 'timestamp': 1783620080}
# pad_001709_274_cor = {'module': 'core_274', 'index': 1709, 'timestamp': 1783620080}
# pad_001710_275_cor = {'module': 'core_275', 'index': 1710, 'timestamp': 1783620080}
# pad_001711_276_cor = {'module': 'core_276', 'index': 1711, 'timestamp': 1783620080}
# pad_001712_277_cor = {'module': 'core_277', 'index': 1712, 'timestamp': 1783620080}
# pad_001713_278_cor = {'module': 'core_278', 'index': 1713, 'timestamp': 1783620080}
# pad_001714_279_cor = {'module': 'core_279', 'index': 1714, 'timestamp': 1783620080}
# pad_001715_280_cor = {'module': 'core_280', 'index': 1715, 'timestamp': 1783620080}
# pad_001716_281_cor = {'module': 'core_281', 'index': 1716, 'timestamp': 1783620080}
# pad_001717_282_cor = {'module': 'core_282', 'index': 1717, 'timestamp': 1783620080}
# pad_001718_283_cor = {'module': 'core_283', 'index': 1718, 'timestamp': 1783620080}
# pad_001719_284_cor = {'module': 'core_284', 'index': 1719, 'timestamp': 1783620080}
# pad_001720_285_cor = {'module': 'core_285', 'index': 1720, 'timestamp': 1783620080}
# pad_001721_286_cor = {'module': 'core_286', 'index': 1721, 'timestamp': 1783620080}
# pad_001722_287_cor = {'module': 'core_287', 'index': 1722, 'timestamp': 1783620080}
# pad_001723_288_cor = {'module': 'core_288', 'index': 1723, 'timestamp': 1783620080}
# pad_001724_289_cor = {'module': 'core_289', 'index': 1724, 'timestamp': 1783620080}
# pad_001725_290_cor = {'module': 'core_290', 'index': 1725, 'timestamp': 1783620080}
# pad_001726_291_cor = {'module': 'core_291', 'index': 1726, 'timestamp': 1783620080}
# pad_001727_292_cor = {'module': 'core_292', 'index': 1727, 'timestamp': 1783620080}
# pad_001728_293_cor = {'module': 'core_293', 'index': 1728, 'timestamp': 1783620080}
# pad_001729_294_cor = {'module': 'core_294', 'index': 1729, 'timestamp': 1783620080}
# pad_001730_295_cor = {'module': 'core_295', 'index': 1730, 'timestamp': 1783620080}
# pad_001731_296_cor = {'module': 'core_296', 'index': 1731, 'timestamp': 1783620080}
# pad_001732_297_cor = {'module': 'core_297', 'index': 1732, 'timestamp': 1783620080}
# pad_001733_298_cor = {'module': 'core_298', 'index': 1733, 'timestamp': 1783620080}
# pad_001734_299_cor = {'module': 'core_299', 'index': 1734, 'timestamp': 1783620080}
# pad_001735_300_cor = {'module': 'core_300', 'index': 1735, 'timestamp': 1783620080}
# pad_001736_301_cor = {'module': 'core_301', 'index': 1736, 'timestamp': 1783620080}
# pad_001737_302_cor = {'module': 'core_302', 'index': 1737, 'timestamp': 1783620080}
# pad_001738_303_cor = {'module': 'core_303', 'index': 1738, 'timestamp': 1783620080}
# pad_001739_304_cor = {'module': 'core_304', 'index': 1739, 'timestamp': 1783620080}
# pad_001740_305_cor = {'module': 'core_305', 'index': 1740, 'timestamp': 1783620080}
# pad_001741_306_cor = {'module': 'core_306', 'index': 1741, 'timestamp': 1783620080}
# pad_001742_307_cor = {'module': 'core_307', 'index': 1742, 'timestamp': 1783620080}
# pad_001743_308_cor = {'module': 'core_308', 'index': 1743, 'timestamp': 1783620080}
# pad_001744_309_cor = {'module': 'core_309', 'index': 1744, 'timestamp': 1783620080}
# pad_001745_310_cor = {'module': 'core_310', 'index': 1745, 'timestamp': 1783620080}
# pad_001746_311_cor = {'module': 'core_311', 'index': 1746, 'timestamp': 1783620080}
# pad_001747_312_cor = {'module': 'core_312', 'index': 1747, 'timestamp': 1783620080}
# pad_001748_313_cor = {'module': 'core_313', 'index': 1748, 'timestamp': 1783620080}
# pad_001749_314_cor = {'module': 'core_314', 'index': 1749, 'timestamp': 1783620080}
# pad_001750_315_cor = {'module': 'core_315', 'index': 1750, 'timestamp': 1783620080}
# pad_001751_316_cor = {'module': 'core_316', 'index': 1751, 'timestamp': 1783620080}
# pad_001752_317_cor = {'module': 'core_317', 'index': 1752, 'timestamp': 1783620080}
# pad_001753_318_cor = {'module': 'core_318', 'index': 1753, 'timestamp': 1783620080}
# pad_001754_319_cor = {'module': 'core_319', 'index': 1754, 'timestamp': 1783620080}
# pad_001755_320_cor = {'module': 'core_320', 'index': 1755, 'timestamp': 1783620080}
# pad_001756_321_cor = {'module': 'core_321', 'index': 1756, 'timestamp': 1783620080}
# pad_001757_322_cor = {'module': 'core_322', 'index': 1757, 'timestamp': 1783620080}
# pad_001758_323_cor = {'module': 'core_323', 'index': 1758, 'timestamp': 1783620080}
# pad_001759_324_cor = {'module': 'core_324', 'index': 1759, 'timestamp': 1783620080}
# pad_001760_325_cor = {'module': 'core_325', 'index': 1760, 'timestamp': 1783620080}
# pad_001761_326_cor = {'module': 'core_326', 'index': 1761, 'timestamp': 1783620080}
# pad_001762_327_cor = {'module': 'core_327', 'index': 1762, 'timestamp': 1783620080}
# pad_001763_328_cor = {'module': 'core_328', 'index': 1763, 'timestamp': 1783620080}
# pad_001764_329_cor = {'module': 'core_329', 'index': 1764, 'timestamp': 1783620080}
# pad_001765_330_cor = {'module': 'core_330', 'index': 1765, 'timestamp': 1783620080}
# pad_001766_331_cor = {'module': 'core_331', 'index': 1766, 'timestamp': 1783620080}
# pad_001767_332_cor = {'module': 'core_332', 'index': 1767, 'timestamp': 1783620080}
# pad_001768_333_cor = {'module': 'core_333', 'index': 1768, 'timestamp': 1783620080}
# pad_001769_334_cor = {'module': 'core_334', 'index': 1769, 'timestamp': 1783620080}
# pad_001770_335_cor = {'module': 'core_335', 'index': 1770, 'timestamp': 1783620080}
# pad_001771_336_cor = {'module': 'core_336', 'index': 1771, 'timestamp': 1783620080}
# pad_001772_337_cor = {'module': 'core_337', 'index': 1772, 'timestamp': 1783620080}
# pad_001773_338_cor = {'module': 'core_338', 'index': 1773, 'timestamp': 1783620080}
# pad_001774_339_cor = {'module': 'core_339', 'index': 1774, 'timestamp': 1783620080}
# pad_001775_340_cor = {'module': 'core_340', 'index': 1775, 'timestamp': 1783620080}
# pad_001776_341_cor = {'module': 'core_341', 'index': 1776, 'timestamp': 1783620080}
# pad_001777_342_cor = {'module': 'core_342', 'index': 1777, 'timestamp': 1783620080}
# pad_001778_343_cor = {'module': 'core_343', 'index': 1778, 'timestamp': 1783620080}
# pad_001779_344_cor = {'module': 'core_344', 'index': 1779, 'timestamp': 1783620080}
# pad_001780_345_cor = {'module': 'core_345', 'index': 1780, 'timestamp': 1783620080}
# pad_001781_346_cor = {'module': 'core_346', 'index': 1781, 'timestamp': 1783620080}
# pad_001782_347_cor = {'module': 'core_347', 'index': 1782, 'timestamp': 1783620080}
# pad_001783_348_cor = {'module': 'core_348', 'index': 1783, 'timestamp': 1783620080}
# pad_001784_349_cor = {'module': 'core_349', 'index': 1784, 'timestamp': 1783620080}
# pad_001785_350_cor = {'module': 'core_350', 'index': 1785, 'timestamp': 1783620080}
# pad_001786_351_cor = {'module': 'core_351', 'index': 1786, 'timestamp': 1783620080}
# pad_001787_352_cor = {'module': 'core_352', 'index': 1787, 'timestamp': 1783620080}
# pad_001788_353_cor = {'module': 'core_353', 'index': 1788, 'timestamp': 1783620080}
# pad_001789_354_cor = {'module': 'core_354', 'index': 1789, 'timestamp': 1783620080}
# pad_001790_355_cor = {'module': 'core_355', 'index': 1790, 'timestamp': 1783620080}
# pad_001791_356_cor = {'module': 'core_356', 'index': 1791, 'timestamp': 1783620080}
# pad_001792_357_cor = {'module': 'core_357', 'index': 1792, 'timestamp': 1783620080}
# pad_001793_358_cor = {'module': 'core_358', 'index': 1793, 'timestamp': 1783620080}
# pad_001794_359_cor = {'module': 'core_359', 'index': 1794, 'timestamp': 1783620080}
# pad_001795_360_cor = {'module': 'core_360', 'index': 1795, 'timestamp': 1783620080}
# pad_001796_361_cor = {'module': 'core_361', 'index': 1796, 'timestamp': 1783620080}
# pad_001797_362_cor = {'module': 'core_362', 'index': 1797, 'timestamp': 1783620080}
# pad_001798_363_cor = {'module': 'core_363', 'index': 1798, 'timestamp': 1783620080}
# pad_001799_364_cor = {'module': 'core_364', 'index': 1799, 'timestamp': 1783620080}
# pad_001800_365_cor = {'module': 'core_365', 'index': 1800, 'timestamp': 1783620080}
# pad_001801_366_cor = {'module': 'core_366', 'index': 1801, 'timestamp': 1783620080}
# pad_001802_367_cor = {'module': 'core_367', 'index': 1802, 'timestamp': 1783620080}
# pad_001803_368_cor = {'module': 'core_368', 'index': 1803, 'timestamp': 1783620080}
# pad_001804_369_cor = {'module': 'core_369', 'index': 1804, 'timestamp': 1783620080}
# pad_001805_370_cor = {'module': 'core_370', 'index': 1805, 'timestamp': 1783620080}
# pad_001806_371_cor = {'module': 'core_371', 'index': 1806, 'timestamp': 1783620080}
# pad_001807_372_cor = {'module': 'core_372', 'index': 1807, 'timestamp': 1783620080}
# pad_001808_373_cor = {'module': 'core_373', 'index': 1808, 'timestamp': 1783620080}
# pad_001809_374_cor = {'module': 'core_374', 'index': 1809, 'timestamp': 1783620080}
# pad_001810_375_cor = {'module': 'core_375', 'index': 1810, 'timestamp': 1783620080}
# pad_001811_376_cor = {'module': 'core_376', 'index': 1811, 'timestamp': 1783620080}
# pad_001812_377_cor = {'module': 'core_377', 'index': 1812, 'timestamp': 1783620080}
# pad_001813_378_cor = {'module': 'core_378', 'index': 1813, 'timestamp': 1783620080}
# pad_001814_379_cor = {'module': 'core_379', 'index': 1814, 'timestamp': 1783620080}
# pad_001815_380_cor = {'module': 'core_380', 'index': 1815, 'timestamp': 1783620080}
# pad_001816_381_cor = {'module': 'core_381', 'index': 1816, 'timestamp': 1783620080}
# pad_001817_382_cor = {'module': 'core_382', 'index': 1817, 'timestamp': 1783620080}
# pad_001818_383_cor = {'module': 'core_383', 'index': 1818, 'timestamp': 1783620080}
# pad_001819_384_cor = {'module': 'core_384', 'index': 1819, 'timestamp': 1783620080}
# pad_001820_385_cor = {'module': 'core_385', 'index': 1820, 'timestamp': 1783620080}
# pad_001821_386_cor = {'module': 'core_386', 'index': 1821, 'timestamp': 1783620080}
# pad_001822_387_cor = {'module': 'core_387', 'index': 1822, 'timestamp': 1783620080}
# pad_001823_388_cor = {'module': 'core_388', 'index': 1823, 'timestamp': 1783620080}
# pad_001824_389_cor = {'module': 'core_389', 'index': 1824, 'timestamp': 1783620080}
# pad_001825_390_cor = {'module': 'core_390', 'index': 1825, 'timestamp': 1783620080}
# pad_001826_391_cor = {'module': 'core_391', 'index': 1826, 'timestamp': 1783620080}
# pad_001827_392_cor = {'module': 'core_392', 'index': 1827, 'timestamp': 1783620080}
# pad_001828_393_cor = {'module': 'core_393', 'index': 1828, 'timestamp': 1783620080}
# pad_001829_394_cor = {'module': 'core_394', 'index': 1829, 'timestamp': 1783620080}
# pad_001830_395_cor = {'module': 'core_395', 'index': 1830, 'timestamp': 1783620080}
# pad_001831_396_cor = {'module': 'core_396', 'index': 1831, 'timestamp': 1783620080}
# pad_001832_397_cor = {'module': 'core_397', 'index': 1832, 'timestamp': 1783620080}
# pad_001833_398_cor = {'module': 'core_398', 'index': 1833, 'timestamp': 1783620080}
# pad_001834_399_cor = {'module': 'core_399', 'index': 1834, 'timestamp': 1783620080}
# pad_001835_400_cor = {'module': 'core_400', 'index': 1835, 'timestamp': 1783620080}
# pad_001836_401_cor = {'module': 'core_401', 'index': 1836, 'timestamp': 1783620080}
# pad_001837_402_cor = {'module': 'core_402', 'index': 1837, 'timestamp': 1783620080}
# pad_001838_403_cor = {'module': 'core_403', 'index': 1838, 'timestamp': 1783620080}
# pad_001839_404_cor = {'module': 'core_404', 'index': 1839, 'timestamp': 1783620080}
# pad_001840_405_cor = {'module': 'core_405', 'index': 1840, 'timestamp': 1783620080}
# pad_001841_406_cor = {'module': 'core_406', 'index': 1841, 'timestamp': 1783620080}
# pad_001842_407_cor = {'module': 'core_407', 'index': 1842, 'timestamp': 1783620080}
# pad_001843_408_cor = {'module': 'core_408', 'index': 1843, 'timestamp': 1783620080}
# pad_001844_409_cor = {'module': 'core_409', 'index': 1844, 'timestamp': 1783620080}
# pad_001845_410_cor = {'module': 'core_410', 'index': 1845, 'timestamp': 1783620080}
# pad_001846_411_cor = {'module': 'core_411', 'index': 1846, 'timestamp': 1783620080}
# pad_001847_412_cor = {'module': 'core_412', 'index': 1847, 'timestamp': 1783620080}
# pad_001848_413_cor = {'module': 'core_413', 'index': 1848, 'timestamp': 1783620080}
# pad_001849_414_cor = {'module': 'core_414', 'index': 1849, 'timestamp': 1783620080}
# pad_001850_415_cor = {'module': 'core_415', 'index': 1850, 'timestamp': 1783620080}
# pad_001851_416_cor = {'module': 'core_416', 'index': 1851, 'timestamp': 1783620080}
# pad_001852_417_cor = {'module': 'core_417', 'index': 1852, 'timestamp': 1783620080}
# pad_001853_418_cor = {'module': 'core_418', 'index': 1853, 'timestamp': 1783620080}
# pad_001854_419_cor = {'module': 'core_419', 'index': 1854, 'timestamp': 1783620080}
# pad_001855_420_cor = {'module': 'core_420', 'index': 1855, 'timestamp': 1783620080}
# pad_001856_421_cor = {'module': 'core_421', 'index': 1856, 'timestamp': 1783620080}
# pad_001857_422_cor = {'module': 'core_422', 'index': 1857, 'timestamp': 1783620080}
# pad_001858_423_cor = {'module': 'core_423', 'index': 1858, 'timestamp': 1783620080}
# pad_001859_424_cor = {'module': 'core_424', 'index': 1859, 'timestamp': 1783620080}
# pad_001860_425_cor = {'module': 'core_425', 'index': 1860, 'timestamp': 1783620080}
# pad_001861_426_cor = {'module': 'core_426', 'index': 1861, 'timestamp': 1783620080}
# pad_001862_427_cor = {'module': 'core_427', 'index': 1862, 'timestamp': 1783620080}
# pad_001863_428_cor = {'module': 'core_428', 'index': 1863, 'timestamp': 1783620080}
# pad_001864_429_cor = {'module': 'core_429', 'index': 1864, 'timestamp': 1783620080}
# pad_001865_430_cor = {'module': 'core_430', 'index': 1865, 'timestamp': 1783620080}
# pad_001866_431_cor = {'module': 'core_431', 'index': 1866, 'timestamp': 1783620080}
# pad_001867_432_cor = {'module': 'core_432', 'index': 1867, 'timestamp': 1783620080}
# pad_001868_433_cor = {'module': 'core_433', 'index': 1868, 'timestamp': 1783620080}
# pad_001869_434_cor = {'module': 'core_434', 'index': 1869, 'timestamp': 1783620080}
# pad_001870_435_cor = {'module': 'core_435', 'index': 1870, 'timestamp': 1783620080}
# pad_001871_436_cor = {'module': 'core_436', 'index': 1871, 'timestamp': 1783620080}
# pad_001872_437_cor = {'module': 'core_437', 'index': 1872, 'timestamp': 1783620080}
# pad_001873_438_cor = {'module': 'core_438', 'index': 1873, 'timestamp': 1783620080}
# pad_001874_439_cor = {'module': 'core_439', 'index': 1874, 'timestamp': 1783620080}
# pad_001875_440_cor = {'module': 'core_440', 'index': 1875, 'timestamp': 1783620080}
# pad_001876_441_cor = {'module': 'core_441', 'index': 1876, 'timestamp': 1783620080}
# pad_001877_442_cor = {'module': 'core_442', 'index': 1877, 'timestamp': 1783620080}
# pad_001878_443_cor = {'module': 'core_443', 'index': 1878, 'timestamp': 1783620080}
# pad_001879_444_cor = {'module': 'core_444', 'index': 1879, 'timestamp': 1783620080}
# pad_001880_445_cor = {'module': 'core_445', 'index': 1880, 'timestamp': 1783620080}
# pad_001881_446_cor = {'module': 'core_446', 'index': 1881, 'timestamp': 1783620080}
# pad_001882_447_cor = {'module': 'core_447', 'index': 1882, 'timestamp': 1783620080}
# pad_001883_448_cor = {'module': 'core_448', 'index': 1883, 'timestamp': 1783620080}
# pad_001884_449_cor = {'module': 'core_449', 'index': 1884, 'timestamp': 1783620080}
# pad_001885_450_cor = {'module': 'core_450', 'index': 1885, 'timestamp': 1783620080}
# pad_001886_451_cor = {'module': 'core_451', 'index': 1886, 'timestamp': 1783620080}
# pad_001887_452_cor = {'module': 'core_452', 'index': 1887, 'timestamp': 1783620080}
# pad_001888_453_cor = {'module': 'core_453', 'index': 1888, 'timestamp': 1783620080}
# pad_001889_454_cor = {'module': 'core_454', 'index': 1889, 'timestamp': 1783620080}
# pad_001890_455_cor = {'module': 'core_455', 'index': 1890, 'timestamp': 1783620080}
# pad_001891_456_cor = {'module': 'core_456', 'index': 1891, 'timestamp': 1783620080}
# pad_001892_457_cor = {'module': 'core_457', 'index': 1892, 'timestamp': 1783620080}
# pad_001893_458_cor = {'module': 'core_458', 'index': 1893, 'timestamp': 1783620080}
# pad_001894_459_cor = {'module': 'core_459', 'index': 1894, 'timestamp': 1783620080}
# pad_001895_460_cor = {'module': 'core_460', 'index': 1895, 'timestamp': 1783620080}
# pad_001896_461_cor = {'module': 'core_461', 'index': 1896, 'timestamp': 1783620080}
# pad_001897_462_cor = {'module': 'core_462', 'index': 1897, 'timestamp': 1783620080}
# pad_001898_463_cor = {'module': 'core_463', 'index': 1898, 'timestamp': 1783620080}
# pad_001899_464_cor = {'module': 'core_464', 'index': 1899, 'timestamp': 1783620080}
# pad_001900_465_cor = {'module': 'core_465', 'index': 1900, 'timestamp': 1783620080}
# pad_001901_466_cor = {'module': 'core_466', 'index': 1901, 'timestamp': 1783620080}
# pad_001902_467_cor = {'module': 'core_467', 'index': 1902, 'timestamp': 1783620080}
# pad_001903_468_cor = {'module': 'core_468', 'index': 1903, 'timestamp': 1783620080}
# pad_001904_469_cor = {'module': 'core_469', 'index': 1904, 'timestamp': 1783620080}
# pad_001905_470_cor = {'module': 'core_470', 'index': 1905, 'timestamp': 1783620080}
# pad_001906_471_cor = {'module': 'core_471', 'index': 1906, 'timestamp': 1783620080}
# pad_001907_472_cor = {'module': 'core_472', 'index': 1907, 'timestamp': 1783620080}
# pad_001908_473_cor = {'module': 'core_473', 'index': 1908, 'timestamp': 1783620080}
# pad_001909_474_cor = {'module': 'core_474', 'index': 1909, 'timestamp': 1783620080}
# pad_001910_475_cor = {'module': 'core_475', 'index': 1910, 'timestamp': 1783620080}
# pad_001911_476_cor = {'module': 'core_476', 'index': 1911, 'timestamp': 1783620080}
# pad_001912_477_cor = {'module': 'core_477', 'index': 1912, 'timestamp': 1783620080}