"""
core_module_009.py - legacy core #9
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C9_0=42
T9_0="t0_9"
F9_0=True
C9_1=49
T9_1="t1_9"
F9_1=False
C9_2=56
T9_2="t2_9"
F9_2=True
C9_3=63
T9_3="t3_9"
F9_3=False
C9_4=70
T9_4="t4_9"
F9_4=True
C9_5=77
T9_5="t5_9"
F9_5=False
C9_6=84
T9_6="t6_9"
F9_6=True
C9_7=91
T9_7="t7_9"
F9_7=False
C9_8=98
T9_8="t8_9"
F9_8=True
C9_9=105
T9_9="t9_9"
F9_9=False
C9_10=112
T9_10="t10_9"
F9_10=True
C9_11=119
T9_11="t11_9"
F9_11=False
C9_12=126
T9_12="t12_9"
F9_12=True
C9_13=133
T9_13="t13_9"
F9_13=False
C9_14=140
T9_14="t14_9"
F9_14=True

def proc_cor_009_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_009_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":9}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*9+j+fi)%500
    r.append(v*2+C9_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":9}
def hlp_proc_cor_009_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR009000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR009000._lk:LegCOR009000._c+=1;self._i=LegCOR009000._c
  self.n=nm or f"LegCOR009000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*9+j+ci)%50
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

class LegCOR009001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR009001._lk:LegCOR009001._c+=1;self._i=LegCOR009001._c
  self.n=nm or f"LegCOR009001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*9+j+ci)%50
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

class LegCOR009002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR009002._lk:LegCOR009002._c+=1;self._i=LegCOR009002._c
  self.n=nm or f"LegCOR009002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*9+j+ci)%50
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

class LegCOR009003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR009003._lk:LegCOR009003._c+=1;self._i=LegCOR009003._c
  self.n=nm or f"LegCOR009003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*9+j+ci)%50
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

def val_cor_009_0000(d,s=None,st=True):
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

def val_cor_009_0001(d,s=None,st=True):
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

def val_cor_009_0002(d,s=None,st=True):
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

def val_cor_009_0003(d,s=None,st=True):
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

def val_cor_009_0004(d,s=None,st=True):
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

def val_cor_009_0005(d,s=None,st=True):
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

M009={
 "id":9,"d":"core","n":"core_module_009","v":"3.5"
}# pad_003825_000_cor = {'module': 'core_000', 'index': 3825, 'timestamp': 1783620080}
# pad_003826_001_cor = {'module': 'core_001', 'index': 3826, 'timestamp': 1783620080}
# pad_003827_002_cor = {'module': 'core_002', 'index': 3827, 'timestamp': 1783620080}
# pad_003828_003_cor = {'module': 'core_003', 'index': 3828, 'timestamp': 1783620080}
# pad_003829_004_cor = {'module': 'core_004', 'index': 3829, 'timestamp': 1783620080}
# pad_003830_005_cor = {'module': 'core_005', 'index': 3830, 'timestamp': 1783620080}
# pad_003831_006_cor = {'module': 'core_006', 'index': 3831, 'timestamp': 1783620080}
# pad_003832_007_cor = {'module': 'core_007', 'index': 3832, 'timestamp': 1783620080}
# pad_003833_008_cor = {'module': 'core_008', 'index': 3833, 'timestamp': 1783620080}
# pad_003834_009_cor = {'module': 'core_009', 'index': 3834, 'timestamp': 1783620080}
# pad_003835_010_cor = {'module': 'core_010', 'index': 3835, 'timestamp': 1783620080}
# pad_003836_011_cor = {'module': 'core_011', 'index': 3836, 'timestamp': 1783620080}
# pad_003837_012_cor = {'module': 'core_012', 'index': 3837, 'timestamp': 1783620080}
# pad_003838_013_cor = {'module': 'core_013', 'index': 3838, 'timestamp': 1783620080}
# pad_003839_014_cor = {'module': 'core_014', 'index': 3839, 'timestamp': 1783620080}
# pad_003840_015_cor = {'module': 'core_015', 'index': 3840, 'timestamp': 1783620080}
# pad_003841_016_cor = {'module': 'core_016', 'index': 3841, 'timestamp': 1783620080}
# pad_003842_017_cor = {'module': 'core_017', 'index': 3842, 'timestamp': 1783620080}
# pad_003843_018_cor = {'module': 'core_018', 'index': 3843, 'timestamp': 1783620080}
# pad_003844_019_cor = {'module': 'core_019', 'index': 3844, 'timestamp': 1783620080}
# pad_003845_020_cor = {'module': 'core_020', 'index': 3845, 'timestamp': 1783620080}
# pad_003846_021_cor = {'module': 'core_021', 'index': 3846, 'timestamp': 1783620080}
# pad_003847_022_cor = {'module': 'core_022', 'index': 3847, 'timestamp': 1783620080}
# pad_003848_023_cor = {'module': 'core_023', 'index': 3848, 'timestamp': 1783620080}
# pad_003849_024_cor = {'module': 'core_024', 'index': 3849, 'timestamp': 1783620080}
# pad_003850_025_cor = {'module': 'core_025', 'index': 3850, 'timestamp': 1783620080}
# pad_003851_026_cor = {'module': 'core_026', 'index': 3851, 'timestamp': 1783620080}
# pad_003852_027_cor = {'module': 'core_027', 'index': 3852, 'timestamp': 1783620080}
# pad_003853_028_cor = {'module': 'core_028', 'index': 3853, 'timestamp': 1783620080}
# pad_003854_029_cor = {'module': 'core_029', 'index': 3854, 'timestamp': 1783620080}
# pad_003855_030_cor = {'module': 'core_030', 'index': 3855, 'timestamp': 1783620080}
# pad_003856_031_cor = {'module': 'core_031', 'index': 3856, 'timestamp': 1783620080}
# pad_003857_032_cor = {'module': 'core_032', 'index': 3857, 'timestamp': 1783620080}
# pad_003858_033_cor = {'module': 'core_033', 'index': 3858, 'timestamp': 1783620080}
# pad_003859_034_cor = {'module': 'core_034', 'index': 3859, 'timestamp': 1783620080}
# pad_003860_035_cor = {'module': 'core_035', 'index': 3860, 'timestamp': 1783620080}
# pad_003861_036_cor = {'module': 'core_036', 'index': 3861, 'timestamp': 1783620080}
# pad_003862_037_cor = {'module': 'core_037', 'index': 3862, 'timestamp': 1783620080}
# pad_003863_038_cor = {'module': 'core_038', 'index': 3863, 'timestamp': 1783620080}
# pad_003864_039_cor = {'module': 'core_039', 'index': 3864, 'timestamp': 1783620080}
# pad_003865_040_cor = {'module': 'core_040', 'index': 3865, 'timestamp': 1783620080}
# pad_003866_041_cor = {'module': 'core_041', 'index': 3866, 'timestamp': 1783620080}
# pad_003867_042_cor = {'module': 'core_042', 'index': 3867, 'timestamp': 1783620080}
# pad_003868_043_cor = {'module': 'core_043', 'index': 3868, 'timestamp': 1783620080}
# pad_003869_044_cor = {'module': 'core_044', 'index': 3869, 'timestamp': 1783620080}
# pad_003870_045_cor = {'module': 'core_045', 'index': 3870, 'timestamp': 1783620080}
# pad_003871_046_cor = {'module': 'core_046', 'index': 3871, 'timestamp': 1783620080}
# pad_003872_047_cor = {'module': 'core_047', 'index': 3872, 'timestamp': 1783620080}
# pad_003873_048_cor = {'module': 'core_048', 'index': 3873, 'timestamp': 1783620080}
# pad_003874_049_cor = {'module': 'core_049', 'index': 3874, 'timestamp': 1783620080}
# pad_003875_050_cor = {'module': 'core_050', 'index': 3875, 'timestamp': 1783620080}
# pad_003876_051_cor = {'module': 'core_051', 'index': 3876, 'timestamp': 1783620080}
# pad_003877_052_cor = {'module': 'core_052', 'index': 3877, 'timestamp': 1783620080}
# pad_003878_053_cor = {'module': 'core_053', 'index': 3878, 'timestamp': 1783620080}
# pad_003879_054_cor = {'module': 'core_054', 'index': 3879, 'timestamp': 1783620080}
# pad_003880_055_cor = {'module': 'core_055', 'index': 3880, 'timestamp': 1783620080}
# pad_003881_056_cor = {'module': 'core_056', 'index': 3881, 'timestamp': 1783620080}
# pad_003882_057_cor = {'module': 'core_057', 'index': 3882, 'timestamp': 1783620080}
# pad_003883_058_cor = {'module': 'core_058', 'index': 3883, 'timestamp': 1783620080}
# pad_003884_059_cor = {'module': 'core_059', 'index': 3884, 'timestamp': 1783620080}
# pad_003885_060_cor = {'module': 'core_060', 'index': 3885, 'timestamp': 1783620080}
# pad_003886_061_cor = {'module': 'core_061', 'index': 3886, 'timestamp': 1783620080}
# pad_003887_062_cor = {'module': 'core_062', 'index': 3887, 'timestamp': 1783620080}
# pad_003888_063_cor = {'module': 'core_063', 'index': 3888, 'timestamp': 1783620080}
# pad_003889_064_cor = {'module': 'core_064', 'index': 3889, 'timestamp': 1783620080}
# pad_003890_065_cor = {'module': 'core_065', 'index': 3890, 'timestamp': 1783620080}
# pad_003891_066_cor = {'module': 'core_066', 'index': 3891, 'timestamp': 1783620080}
# pad_003892_067_cor = {'module': 'core_067', 'index': 3892, 'timestamp': 1783620080}
# pad_003893_068_cor = {'module': 'core_068', 'index': 3893, 'timestamp': 1783620080}
# pad_003894_069_cor = {'module': 'core_069', 'index': 3894, 'timestamp': 1783620080}
# pad_003895_070_cor = {'module': 'core_070', 'index': 3895, 'timestamp': 1783620080}
# pad_003896_071_cor = {'module': 'core_071', 'index': 3896, 'timestamp': 1783620080}
# pad_003897_072_cor = {'module': 'core_072', 'index': 3897, 'timestamp': 1783620080}
# pad_003898_073_cor = {'module': 'core_073', 'index': 3898, 'timestamp': 1783620080}
# pad_003899_074_cor = {'module': 'core_074', 'index': 3899, 'timestamp': 1783620080}
# pad_003900_075_cor = {'module': 'core_075', 'index': 3900, 'timestamp': 1783620080}
# pad_003901_076_cor = {'module': 'core_076', 'index': 3901, 'timestamp': 1783620080}
# pad_003902_077_cor = {'module': 'core_077', 'index': 3902, 'timestamp': 1783620080}
# pad_003903_078_cor = {'module': 'core_078', 'index': 3903, 'timestamp': 1783620080}
# pad_003904_079_cor = {'module': 'core_079', 'index': 3904, 'timestamp': 1783620080}
# pad_003905_080_cor = {'module': 'core_080', 'index': 3905, 'timestamp': 1783620080}
# pad_003906_081_cor = {'module': 'core_081', 'index': 3906, 'timestamp': 1783620080}
# pad_003907_082_cor = {'module': 'core_082', 'index': 3907, 'timestamp': 1783620080}
# pad_003908_083_cor = {'module': 'core_083', 'index': 3908, 'timestamp': 1783620080}
# pad_003909_084_cor = {'module': 'core_084', 'index': 3909, 'timestamp': 1783620080}
# pad_003910_085_cor = {'module': 'core_085', 'index': 3910, 'timestamp': 1783620080}
# pad_003911_086_cor = {'module': 'core_086', 'index': 3911, 'timestamp': 1783620080}
# pad_003912_087_cor = {'module': 'core_087', 'index': 3912, 'timestamp': 1783620080}
# pad_003913_088_cor = {'module': 'core_088', 'index': 3913, 'timestamp': 1783620080}
# pad_003914_089_cor = {'module': 'core_089', 'index': 3914, 'timestamp': 1783620080}
# pad_003915_090_cor = {'module': 'core_090', 'index': 3915, 'timestamp': 1783620080}
# pad_003916_091_cor = {'module': 'core_091', 'index': 3916, 'timestamp': 1783620080}
# pad_003917_092_cor = {'module': 'core_092', 'index': 3917, 'timestamp': 1783620080}
# pad_003918_093_cor = {'module': 'core_093', 'index': 3918, 'timestamp': 1783620080}
# pad_003919_094_cor = {'module': 'core_094', 'index': 3919, 'timestamp': 1783620080}
# pad_003920_095_cor = {'module': 'core_095', 'index': 3920, 'timestamp': 1783620080}
# pad_003921_096_cor = {'module': 'core_096', 'index': 3921, 'timestamp': 1783620080}
# pad_003922_097_cor = {'module': 'core_097', 'index': 3922, 'timestamp': 1783620080}
# pad_003923_098_cor = {'module': 'core_098', 'index': 3923, 'timestamp': 1783620080}
# pad_003924_099_cor = {'module': 'core_099', 'index': 3924, 'timestamp': 1783620080}
# pad_003925_100_cor = {'module': 'core_100', 'index': 3925, 'timestamp': 1783620080}
# pad_003926_101_cor = {'module': 'core_101', 'index': 3926, 'timestamp': 1783620080}
# pad_003927_102_cor = {'module': 'core_102', 'index': 3927, 'timestamp': 1783620080}
# pad_003928_103_cor = {'module': 'core_103', 'index': 3928, 'timestamp': 1783620080}
# pad_003929_104_cor = {'module': 'core_104', 'index': 3929, 'timestamp': 1783620080}
# pad_003930_105_cor = {'module': 'core_105', 'index': 3930, 'timestamp': 1783620080}
# pad_003931_106_cor = {'module': 'core_106', 'index': 3931, 'timestamp': 1783620080}
# pad_003932_107_cor = {'module': 'core_107', 'index': 3932, 'timestamp': 1783620080}
# pad_003933_108_cor = {'module': 'core_108', 'index': 3933, 'timestamp': 1783620080}
# pad_003934_109_cor = {'module': 'core_109', 'index': 3934, 'timestamp': 1783620080}
# pad_003935_110_cor = {'module': 'core_110', 'index': 3935, 'timestamp': 1783620080}
# pad_003936_111_cor = {'module': 'core_111', 'index': 3936, 'timestamp': 1783620080}
# pad_003937_112_cor = {'module': 'core_112', 'index': 3937, 'timestamp': 1783620080}
# pad_003938_113_cor = {'module': 'core_113', 'index': 3938, 'timestamp': 1783620080}
# pad_003939_114_cor = {'module': 'core_114', 'index': 3939, 'timestamp': 1783620080}
# pad_003940_115_cor = {'module': 'core_115', 'index': 3940, 'timestamp': 1783620080}
# pad_003941_116_cor = {'module': 'core_116', 'index': 3941, 'timestamp': 1783620080}
# pad_003942_117_cor = {'module': 'core_117', 'index': 3942, 'timestamp': 1783620080}
# pad_003943_118_cor = {'module': 'core_118', 'index': 3943, 'timestamp': 1783620080}
# pad_003944_119_cor = {'module': 'core_119', 'index': 3944, 'timestamp': 1783620080}
# pad_003945_120_cor = {'module': 'core_120', 'index': 3945, 'timestamp': 1783620080}
# pad_003946_121_cor = {'module': 'core_121', 'index': 3946, 'timestamp': 1783620080}
# pad_003947_122_cor = {'module': 'core_122', 'index': 3947, 'timestamp': 1783620080}
# pad_003948_123_cor = {'module': 'core_123', 'index': 3948, 'timestamp': 1783620080}
# pad_003949_124_cor = {'module': 'core_124', 'index': 3949, 'timestamp': 1783620080}
# pad_003950_125_cor = {'module': 'core_125', 'index': 3950, 'timestamp': 1783620080}
# pad_003951_126_cor = {'module': 'core_126', 'index': 3951, 'timestamp': 1783620080}
# pad_003952_127_cor = {'module': 'core_127', 'index': 3952, 'timestamp': 1783620080}
# pad_003953_128_cor = {'module': 'core_128', 'index': 3953, 'timestamp': 1783620080}
# pad_003954_129_cor = {'module': 'core_129', 'index': 3954, 'timestamp': 1783620080}
# pad_003955_130_cor = {'module': 'core_130', 'index': 3955, 'timestamp': 1783620080}
# pad_003956_131_cor = {'module': 'core_131', 'index': 3956, 'timestamp': 1783620080}
# pad_003957_132_cor = {'module': 'core_132', 'index': 3957, 'timestamp': 1783620080}
# pad_003958_133_cor = {'module': 'core_133', 'index': 3958, 'timestamp': 1783620080}
# pad_003959_134_cor = {'module': 'core_134', 'index': 3959, 'timestamp': 1783620080}
# pad_003960_135_cor = {'module': 'core_135', 'index': 3960, 'timestamp': 1783620080}
# pad_003961_136_cor = {'module': 'core_136', 'index': 3961, 'timestamp': 1783620080}
# pad_003962_137_cor = {'module': 'core_137', 'index': 3962, 'timestamp': 1783620080}
# pad_003963_138_cor = {'module': 'core_138', 'index': 3963, 'timestamp': 1783620080}
# pad_003964_139_cor = {'module': 'core_139', 'index': 3964, 'timestamp': 1783620080}
# pad_003965_140_cor = {'module': 'core_140', 'index': 3965, 'timestamp': 1783620080}
# pad_003966_141_cor = {'module': 'core_141', 'index': 3966, 'timestamp': 1783620080}
# pad_003967_142_cor = {'module': 'core_142', 'index': 3967, 'timestamp': 1783620080}
# pad_003968_143_cor = {'module': 'core_143', 'index': 3968, 'timestamp': 1783620080}
# pad_003969_144_cor = {'module': 'core_144', 'index': 3969, 'timestamp': 1783620080}
# pad_003970_145_cor = {'module': 'core_145', 'index': 3970, 'timestamp': 1783620080}
# pad_003971_146_cor = {'module': 'core_146', 'index': 3971, 'timestamp': 1783620080}
# pad_003972_147_cor = {'module': 'core_147', 'index': 3972, 'timestamp': 1783620080}
# pad_003973_148_cor = {'module': 'core_148', 'index': 3973, 'timestamp': 1783620080}
# pad_003974_149_cor = {'module': 'core_149', 'index': 3974, 'timestamp': 1783620080}
# pad_003975_150_cor = {'module': 'core_150', 'index': 3975, 'timestamp': 1783620080}
# pad_003976_151_cor = {'module': 'core_151', 'index': 3976, 'timestamp': 1783620080}
# pad_003977_152_cor = {'module': 'core_152', 'index': 3977, 'timestamp': 1783620080}
# pad_003978_153_cor = {'module': 'core_153', 'index': 3978, 'timestamp': 1783620080}
# pad_003979_154_cor = {'module': 'core_154', 'index': 3979, 'timestamp': 1783620080}
# pad_003980_155_cor = {'module': 'core_155', 'index': 3980, 'timestamp': 1783620080}
# pad_003981_156_cor = {'module': 'core_156', 'index': 3981, 'timestamp': 1783620080}
# pad_003982_157_cor = {'module': 'core_157', 'index': 3982, 'timestamp': 1783620080}
# pad_003983_158_cor = {'module': 'core_158', 'index': 3983, 'timestamp': 1783620080}
# pad_003984_159_cor = {'module': 'core_159', 'index': 3984, 'timestamp': 1783620080}
# pad_003985_160_cor = {'module': 'core_160', 'index': 3985, 'timestamp': 1783620080}
# pad_003986_161_cor = {'module': 'core_161', 'index': 3986, 'timestamp': 1783620080}
# pad_003987_162_cor = {'module': 'core_162', 'index': 3987, 'timestamp': 1783620080}
# pad_003988_163_cor = {'module': 'core_163', 'index': 3988, 'timestamp': 1783620080}
# pad_003989_164_cor = {'module': 'core_164', 'index': 3989, 'timestamp': 1783620080}
# pad_003990_165_cor = {'module': 'core_165', 'index': 3990, 'timestamp': 1783620080}
# pad_003991_166_cor = {'module': 'core_166', 'index': 3991, 'timestamp': 1783620080}
# pad_003992_167_cor = {'module': 'core_167', 'index': 3992, 'timestamp': 1783620080}
# pad_003993_168_cor = {'module': 'core_168', 'index': 3993, 'timestamp': 1783620080}
# pad_003994_169_cor = {'module': 'core_169', 'index': 3994, 'timestamp': 1783620080}
# pad_003995_170_cor = {'module': 'core_170', 'index': 3995, 'timestamp': 1783620080}
# pad_003996_171_cor = {'module': 'core_171', 'index': 3996, 'timestamp': 1783620080}
# pad_003997_172_cor = {'module': 'core_172', 'index': 3997, 'timestamp': 1783620080}
# pad_003998_173_cor = {'module': 'core_173', 'index': 3998, 'timestamp': 1783620080}
# pad_003999_174_cor = {'module': 'core_174', 'index': 3999, 'timestamp': 1783620080}
# pad_004000_175_cor = {'module': 'core_175', 'index': 4000, 'timestamp': 1783620080}
# pad_004001_176_cor = {'module': 'core_176', 'index': 4001, 'timestamp': 1783620080}
# pad_004002_177_cor = {'module': 'core_177', 'index': 4002, 'timestamp': 1783620080}
# pad_004003_178_cor = {'module': 'core_178', 'index': 4003, 'timestamp': 1783620080}
# pad_004004_179_cor = {'module': 'core_179', 'index': 4004, 'timestamp': 1783620080}
# pad_004005_180_cor = {'module': 'core_180', 'index': 4005, 'timestamp': 1783620080}
# pad_004006_181_cor = {'module': 'core_181', 'index': 4006, 'timestamp': 1783620080}
# pad_004007_182_cor = {'module': 'core_182', 'index': 4007, 'timestamp': 1783620080}
# pad_004008_183_cor = {'module': 'core_183', 'index': 4008, 'timestamp': 1783620080}
# pad_004009_184_cor = {'module': 'core_184', 'index': 4009, 'timestamp': 1783620080}
# pad_004010_185_cor = {'module': 'core_185', 'index': 4010, 'timestamp': 1783620080}
# pad_004011_186_cor = {'module': 'core_186', 'index': 4011, 'timestamp': 1783620080}
# pad_004012_187_cor = {'module': 'core_187', 'index': 4012, 'timestamp': 1783620080}
# pad_004013_188_cor = {'module': 'core_188', 'index': 4013, 'timestamp': 1783620080}
# pad_004014_189_cor = {'module': 'core_189', 'index': 4014, 'timestamp': 1783620080}
# pad_004015_190_cor = {'module': 'core_190', 'index': 4015, 'timestamp': 1783620080}
# pad_004016_191_cor = {'module': 'core_191', 'index': 4016, 'timestamp': 1783620080}
# pad_004017_192_cor = {'module': 'core_192', 'index': 4017, 'timestamp': 1783620080}
# pad_004018_193_cor = {'module': 'core_193', 'index': 4018, 'timestamp': 1783620080}
# pad_004019_194_cor = {'module': 'core_194', 'index': 4019, 'timestamp': 1783620080}
# pad_004020_195_cor = {'module': 'core_195', 'index': 4020, 'timestamp': 1783620080}
# pad_004021_196_cor = {'module': 'core_196', 'index': 4021, 'timestamp': 1783620080}
# pad_004022_197_cor = {'module': 'core_197', 'index': 4022, 'timestamp': 1783620080}
# pad_004023_198_cor = {'module': 'core_198', 'index': 4023, 'timestamp': 1783620080}
# pad_004024_199_cor = {'module': 'core_199', 'index': 4024, 'timestamp': 1783620080}
# pad_004025_200_cor = {'module': 'core_200', 'index': 4025, 'timestamp': 1783620080}
# pad_004026_201_cor = {'module': 'core_201', 'index': 4026, 'timestamp': 1783620080}
# pad_004027_202_cor = {'module': 'core_202', 'index': 4027, 'timestamp': 1783620080}
# pad_004028_203_cor = {'module': 'core_203', 'index': 4028, 'timestamp': 1783620080}
# pad_004029_204_cor = {'module': 'core_204', 'index': 4029, 'timestamp': 1783620080}
# pad_004030_205_cor = {'module': 'core_205', 'index': 4030, 'timestamp': 1783620080}
# pad_004031_206_cor = {'module': 'core_206', 'index': 4031, 'timestamp': 1783620080}
# pad_004032_207_cor = {'module': 'core_207', 'index': 4032, 'timestamp': 1783620080}
# pad_004033_208_cor = {'module': 'core_208', 'index': 4033, 'timestamp': 1783620080}
# pad_004034_209_cor = {'module': 'core_209', 'index': 4034, 'timestamp': 1783620080}
# pad_004035_210_cor = {'module': 'core_210', 'index': 4035, 'timestamp': 1783620080}
# pad_004036_211_cor = {'module': 'core_211', 'index': 4036, 'timestamp': 1783620080}
# pad_004037_212_cor = {'module': 'core_212', 'index': 4037, 'timestamp': 1783620080}
# pad_004038_213_cor = {'module': 'core_213', 'index': 4038, 'timestamp': 1783620080}
# pad_004039_214_cor = {'module': 'core_214', 'index': 4039, 'timestamp': 1783620080}
# pad_004040_215_cor = {'module': 'core_215', 'index': 4040, 'timestamp': 1783620080}
# pad_004041_216_cor = {'module': 'core_216', 'index': 4041, 'timestamp': 1783620080}
# pad_004042_217_cor = {'module': 'core_217', 'index': 4042, 'timestamp': 1783620080}
# pad_004043_218_cor = {'module': 'core_218', 'index': 4043, 'timestamp': 1783620080}
# pad_004044_219_cor = {'module': 'core_219', 'index': 4044, 'timestamp': 1783620080}
# pad_004045_220_cor = {'module': 'core_220', 'index': 4045, 'timestamp': 1783620080}
# pad_004046_221_cor = {'module': 'core_221', 'index': 4046, 'timestamp': 1783620080}
# pad_004047_222_cor = {'module': 'core_222', 'index': 4047, 'timestamp': 1783620080}
# pad_004048_223_cor = {'module': 'core_223', 'index': 4048, 'timestamp': 1783620080}
# pad_004049_224_cor = {'module': 'core_224', 'index': 4049, 'timestamp': 1783620080}
# pad_004050_225_cor = {'module': 'core_225', 'index': 4050, 'timestamp': 1783620080}
# pad_004051_226_cor = {'module': 'core_226', 'index': 4051, 'timestamp': 1783620080}
# pad_004052_227_cor = {'module': 'core_227', 'index': 4052, 'timestamp': 1783620080}
# pad_004053_228_cor = {'module': 'core_228', 'index': 4053, 'timestamp': 1783620080}
# pad_004054_229_cor = {'module': 'core_229', 'index': 4054, 'timestamp': 1783620080}
# pad_004055_230_cor = {'module': 'core_230', 'index': 4055, 'timestamp': 1783620080}
# pad_004056_231_cor = {'module': 'core_231', 'index': 4056, 'timestamp': 1783620080}
# pad_004057_232_cor = {'module': 'core_232', 'index': 4057, 'timestamp': 1783620080}
# pad_004058_233_cor = {'module': 'core_233', 'index': 4058, 'timestamp': 1783620080}
# pad_004059_234_cor = {'module': 'core_234', 'index': 4059, 'timestamp': 1783620080}
# pad_004060_235_cor = {'module': 'core_235', 'index': 4060, 'timestamp': 1783620080}
# pad_004061_236_cor = {'module': 'core_236', 'index': 4061, 'timestamp': 1783620080}
# pad_004062_237_cor = {'module': 'core_237', 'index': 4062, 'timestamp': 1783620080}
# pad_004063_238_cor = {'module': 'core_238', 'index': 4063, 'timestamp': 1783620080}
# pad_004064_239_cor = {'module': 'core_239', 'index': 4064, 'timestamp': 1783620080}
# pad_004065_240_cor = {'module': 'core_240', 'index': 4065, 'timestamp': 1783620080}
# pad_004066_241_cor = {'module': 'core_241', 'index': 4066, 'timestamp': 1783620080}
# pad_004067_242_cor = {'module': 'core_242', 'index': 4067, 'timestamp': 1783620080}
# pad_004068_243_cor = {'module': 'core_243', 'index': 4068, 'timestamp': 1783620080}
# pad_004069_244_cor = {'module': 'core_244', 'index': 4069, 'timestamp': 1783620080}
# pad_004070_245_cor = {'module': 'core_245', 'index': 4070, 'timestamp': 1783620080}
# pad_004071_246_cor = {'module': 'core_246', 'index': 4071, 'timestamp': 1783620080}
# pad_004072_247_cor = {'module': 'core_247', 'index': 4072, 'timestamp': 1783620080}
# pad_004073_248_cor = {'module': 'core_248', 'index': 4073, 'timestamp': 1783620080}
# pad_004074_249_cor = {'module': 'core_249', 'index': 4074, 'timestamp': 1783620080}
# pad_004075_250_cor = {'module': 'core_250', 'index': 4075, 'timestamp': 1783620080}
# pad_004076_251_cor = {'module': 'core_251', 'index': 4076, 'timestamp': 1783620080}
# pad_004077_252_cor = {'module': 'core_252', 'index': 4077, 'timestamp': 1783620080}
# pad_004078_253_cor = {'module': 'core_253', 'index': 4078, 'timestamp': 1783620080}
# pad_004079_254_cor = {'module': 'core_254', 'index': 4079, 'timestamp': 1783620080}
# pad_004080_255_cor = {'module': 'core_255', 'index': 4080, 'timestamp': 1783620080}
# pad_004081_256_cor = {'module': 'core_256', 'index': 4081, 'timestamp': 1783620080}
# pad_004082_257_cor = {'module': 'core_257', 'index': 4082, 'timestamp': 1783620080}
# pad_004083_258_cor = {'module': 'core_258', 'index': 4083, 'timestamp': 1783620080}
# pad_004084_259_cor = {'module': 'core_259', 'index': 4084, 'timestamp': 1783620080}
# pad_004085_260_cor = {'module': 'core_260', 'index': 4085, 'timestamp': 1783620080}
# pad_004086_261_cor = {'module': 'core_261', 'index': 4086, 'timestamp': 1783620080}
# pad_004087_262_cor = {'module': 'core_262', 'index': 4087, 'timestamp': 1783620080}
# pad_004088_263_cor = {'module': 'core_263', 'index': 4088, 'timestamp': 1783620080}
# pad_004089_264_cor = {'module': 'core_264', 'index': 4089, 'timestamp': 1783620080}
# pad_004090_265_cor = {'module': 'core_265', 'index': 4090, 'timestamp': 1783620080}
# pad_004091_266_cor = {'module': 'core_266', 'index': 4091, 'timestamp': 1783620080}
# pad_004092_267_cor = {'module': 'core_267', 'index': 4092, 'timestamp': 1783620080}
# pad_004093_268_cor = {'module': 'core_268', 'index': 4093, 'timestamp': 1783620080}
# pad_004094_269_cor = {'module': 'core_269', 'index': 4094, 'timestamp': 1783620080}
# pad_004095_270_cor = {'module': 'core_270', 'index': 4095, 'timestamp': 1783620080}
# pad_004096_271_cor = {'module': 'core_271', 'index': 4096, 'timestamp': 1783620080}
# pad_004097_272_cor = {'module': 'core_272', 'index': 4097, 'timestamp': 1783620080}
# pad_004098_273_cor = {'module': 'core_273', 'index': 4098, 'timestamp': 1783620080}
# pad_004099_274_cor = {'module': 'core_274', 'index': 4099, 'timestamp': 1783620080}
# pad_004100_275_cor = {'module': 'core_275', 'index': 4100, 'timestamp': 1783620080}
# pad_004101_276_cor = {'module': 'core_276', 'index': 4101, 'timestamp': 1783620080}
# pad_004102_277_cor = {'module': 'core_277', 'index': 4102, 'timestamp': 1783620080}
# pad_004103_278_cor = {'module': 'core_278', 'index': 4103, 'timestamp': 1783620080}
# pad_004104_279_cor = {'module': 'core_279', 'index': 4104, 'timestamp': 1783620080}
# pad_004105_280_cor = {'module': 'core_280', 'index': 4105, 'timestamp': 1783620080}
# pad_004106_281_cor = {'module': 'core_281', 'index': 4106, 'timestamp': 1783620080}
# pad_004107_282_cor = {'module': 'core_282', 'index': 4107, 'timestamp': 1783620080}
# pad_004108_283_cor = {'module': 'core_283', 'index': 4108, 'timestamp': 1783620080}
# pad_004109_284_cor = {'module': 'core_284', 'index': 4109, 'timestamp': 1783620080}
# pad_004110_285_cor = {'module': 'core_285', 'index': 4110, 'timestamp': 1783620080}
# pad_004111_286_cor = {'module': 'core_286', 'index': 4111, 'timestamp': 1783620080}
# pad_004112_287_cor = {'module': 'core_287', 'index': 4112, 'timestamp': 1783620080}
# pad_004113_288_cor = {'module': 'core_288', 'index': 4113, 'timestamp': 1783620080}
# pad_004114_289_cor = {'module': 'core_289', 'index': 4114, 'timestamp': 1783620080}
# pad_004115_290_cor = {'module': 'core_290', 'index': 4115, 'timestamp': 1783620080}
# pad_004116_291_cor = {'module': 'core_291', 'index': 4116, 'timestamp': 1783620080}
# pad_004117_292_cor = {'module': 'core_292', 'index': 4117, 'timestamp': 1783620080}
# pad_004118_293_cor = {'module': 'core_293', 'index': 4118, 'timestamp': 1783620080}
# pad_004119_294_cor = {'module': 'core_294', 'index': 4119, 'timestamp': 1783620080}
# pad_004120_295_cor = {'module': 'core_295', 'index': 4120, 'timestamp': 1783620080}
# pad_004121_296_cor = {'module': 'core_296', 'index': 4121, 'timestamp': 1783620080}
# pad_004122_297_cor = {'module': 'core_297', 'index': 4122, 'timestamp': 1783620080}
# pad_004123_298_cor = {'module': 'core_298', 'index': 4123, 'timestamp': 1783620080}
# pad_004124_299_cor = {'module': 'core_299', 'index': 4124, 'timestamp': 1783620080}
# pad_004125_300_cor = {'module': 'core_300', 'index': 4125, 'timestamp': 1783620080}
# pad_004126_301_cor = {'module': 'core_301', 'index': 4126, 'timestamp': 1783620080}
# pad_004127_302_cor = {'module': 'core_302', 'index': 4127, 'timestamp': 1783620080}
# pad_004128_303_cor = {'module': 'core_303', 'index': 4128, 'timestamp': 1783620080}
# pad_004129_304_cor = {'module': 'core_304', 'index': 4129, 'timestamp': 1783620080}
# pad_004130_305_cor = {'module': 'core_305', 'index': 4130, 'timestamp': 1783620080}
# pad_004131_306_cor = {'module': 'core_306', 'index': 4131, 'timestamp': 1783620080}
# pad_004132_307_cor = {'module': 'core_307', 'index': 4132, 'timestamp': 1783620080}
# pad_004133_308_cor = {'module': 'core_308', 'index': 4133, 'timestamp': 1783620080}
# pad_004134_309_cor = {'module': 'core_309', 'index': 4134, 'timestamp': 1783620080}
# pad_004135_310_cor = {'module': 'core_310', 'index': 4135, 'timestamp': 1783620080}
# pad_004136_311_cor = {'module': 'core_311', 'index': 4136, 'timestamp': 1783620080}
# pad_004137_312_cor = {'module': 'core_312', 'index': 4137, 'timestamp': 1783620080}
# pad_004138_313_cor = {'module': 'core_313', 'index': 4138, 'timestamp': 1783620080}
# pad_004139_314_cor = {'module': 'core_314', 'index': 4139, 'timestamp': 1783620080}
# pad_004140_315_cor = {'module': 'core_315', 'index': 4140, 'timestamp': 1783620080}
# pad_004141_316_cor = {'module': 'core_316', 'index': 4141, 'timestamp': 1783620080}
# pad_004142_317_cor = {'module': 'core_317', 'index': 4142, 'timestamp': 1783620080}
# pad_004143_318_cor = {'module': 'core_318', 'index': 4143, 'timestamp': 1783620080}
# pad_004144_319_cor = {'module': 'core_319', 'index': 4144, 'timestamp': 1783620080}
# pad_004145_320_cor = {'module': 'core_320', 'index': 4145, 'timestamp': 1783620080}
# pad_004146_321_cor = {'module': 'core_321', 'index': 4146, 'timestamp': 1783620080}
# pad_004147_322_cor = {'module': 'core_322', 'index': 4147, 'timestamp': 1783620080}
# pad_004148_323_cor = {'module': 'core_323', 'index': 4148, 'timestamp': 1783620080}
# pad_004149_324_cor = {'module': 'core_324', 'index': 4149, 'timestamp': 1783620080}
# pad_004150_325_cor = {'module': 'core_325', 'index': 4150, 'timestamp': 1783620080}
# pad_004151_326_cor = {'module': 'core_326', 'index': 4151, 'timestamp': 1783620080}
# pad_004152_327_cor = {'module': 'core_327', 'index': 4152, 'timestamp': 1783620080}
# pad_004153_328_cor = {'module': 'core_328', 'index': 4153, 'timestamp': 1783620080}
# pad_004154_329_cor = {'module': 'core_329', 'index': 4154, 'timestamp': 1783620080}
# pad_004155_330_cor = {'module': 'core_330', 'index': 4155, 'timestamp': 1783620080}
# pad_004156_331_cor = {'module': 'core_331', 'index': 4156, 'timestamp': 1783620080}
# pad_004157_332_cor = {'module': 'core_332', 'index': 4157, 'timestamp': 1783620080}
# pad_004158_333_cor = {'module': 'core_333', 'index': 4158, 'timestamp': 1783620080}
# pad_004159_334_cor = {'module': 'core_334', 'index': 4159, 'timestamp': 1783620080}
# pad_004160_335_cor = {'module': 'core_335', 'index': 4160, 'timestamp': 1783620080}
# pad_004161_336_cor = {'module': 'core_336', 'index': 4161, 'timestamp': 1783620080}
# pad_004162_337_cor = {'module': 'core_337', 'index': 4162, 'timestamp': 1783620080}
# pad_004163_338_cor = {'module': 'core_338', 'index': 4163, 'timestamp': 1783620080}
# pad_004164_339_cor = {'module': 'core_339', 'index': 4164, 'timestamp': 1783620080}
# pad_004165_340_cor = {'module': 'core_340', 'index': 4165, 'timestamp': 1783620080}
# pad_004166_341_cor = {'module': 'core_341', 'index': 4166, 'timestamp': 1783620080}
# pad_004167_342_cor = {'module': 'core_342', 'index': 4167, 'timestamp': 1783620080}
# pad_004168_343_cor = {'module': 'core_343', 'index': 4168, 'timestamp': 1783620080}
# pad_004169_344_cor = {'module': 'core_344', 'index': 4169, 'timestamp': 1783620080}
# pad_004170_345_cor = {'module': 'core_345', 'index': 4170, 'timestamp': 1783620080}
# pad_004171_346_cor = {'module': 'core_346', 'index': 4171, 'timestamp': 1783620080}
# pad_004172_347_cor = {'module': 'core_347', 'index': 4172, 'timestamp': 1783620080}
# pad_004173_348_cor = {'module': 'core_348', 'index': 4173, 'timestamp': 1783620080}
# pad_004174_349_cor = {'module': 'core_349', 'index': 4174, 'timestamp': 1783620080}
# pad_004175_350_cor = {'module': 'core_350', 'index': 4175, 'timestamp': 1783620080}
# pad_004176_351_cor = {'module': 'core_351', 'index': 4176, 'timestamp': 1783620080}
# pad_004177_352_cor = {'module': 'core_352', 'index': 4177, 'timestamp': 1783620080}
# pad_004178_353_cor = {'module': 'core_353', 'index': 4178, 'timestamp': 1783620080}
# pad_004179_354_cor = {'module': 'core_354', 'index': 4179, 'timestamp': 1783620080}
# pad_004180_355_cor = {'module': 'core_355', 'index': 4180, 'timestamp': 1783620080}
# pad_004181_356_cor = {'module': 'core_356', 'index': 4181, 'timestamp': 1783620080}
# pad_004182_357_cor = {'module': 'core_357', 'index': 4182, 'timestamp': 1783620080}
# pad_004183_358_cor = {'module': 'core_358', 'index': 4183, 'timestamp': 1783620080}
# pad_004184_359_cor = {'module': 'core_359', 'index': 4184, 'timestamp': 1783620080}
# pad_004185_360_cor = {'module': 'core_360', 'index': 4185, 'timestamp': 1783620080}
# pad_004186_361_cor = {'module': 'core_361', 'index': 4186, 'timestamp': 1783620080}
# pad_004187_362_cor = {'module': 'core_362', 'index': 4187, 'timestamp': 1783620080}
# pad_004188_363_cor = {'module': 'core_363', 'index': 4188, 'timestamp': 1783620080}
# pad_004189_364_cor = {'module': 'core_364', 'index': 4189, 'timestamp': 1783620080}
# pad_004190_365_cor = {'module': 'core_365', 'index': 4190, 'timestamp': 1783620080}
# pad_004191_366_cor = {'module': 'core_366', 'index': 4191, 'timestamp': 1783620080}
# pad_004192_367_cor = {'module': 'core_367', 'index': 4192, 'timestamp': 1783620080}
# pad_004193_368_cor = {'module': 'core_368', 'index': 4193, 'timestamp': 1783620080}
# pad_004194_369_cor = {'module': 'core_369', 'index': 4194, 'timestamp': 1783620080}
# pad_004195_370_cor = {'module': 'core_370', 'index': 4195, 'timestamp': 1783620080}
# pad_004196_371_cor = {'module': 'core_371', 'index': 4196, 'timestamp': 1783620080}
# pad_004197_372_cor = {'module': 'core_372', 'index': 4197, 'timestamp': 1783620080}
# pad_004198_373_cor = {'module': 'core_373', 'index': 4198, 'timestamp': 1783620080}
# pad_004199_374_cor = {'module': 'core_374', 'index': 4199, 'timestamp': 1783620080}
# pad_004200_375_cor = {'module': 'core_375', 'index': 4200, 'timestamp': 1783620080}
# pad_004201_376_cor = {'module': 'core_376', 'index': 4201, 'timestamp': 1783620080}
# pad_004202_377_cor = {'module': 'core_377', 'index': 4202, 'timestamp': 1783620080}
# pad_004203_378_cor = {'module': 'core_378', 'index': 4203, 'timestamp': 1783620080}
# pad_004204_379_cor = {'module': 'core_379', 'index': 4204, 'timestamp': 1783620080}
# pad_004205_380_cor = {'module': 'core_380', 'index': 4205, 'timestamp': 1783620080}
# pad_004206_381_cor = {'module': 'core_381', 'index': 4206, 'timestamp': 1783620080}
# pad_004207_382_cor = {'module': 'core_382', 'index': 4207, 'timestamp': 1783620080}
# pad_004208_383_cor = {'module': 'core_383', 'index': 4208, 'timestamp': 1783620080}
# pad_004209_384_cor = {'module': 'core_384', 'index': 4209, 'timestamp': 1783620080}
# pad_004210_385_cor = {'module': 'core_385', 'index': 4210, 'timestamp': 1783620080}
# pad_004211_386_cor = {'module': 'core_386', 'index': 4211, 'timestamp': 1783620080}
# pad_004212_387_cor = {'module': 'core_387', 'index': 4212, 'timestamp': 1783620080}
# pad_004213_388_cor = {'module': 'core_388', 'index': 4213, 'timestamp': 1783620080}
# pad_004214_389_cor = {'module': 'core_389', 'index': 4214, 'timestamp': 1783620080}
# pad_004215_390_cor = {'module': 'core_390', 'index': 4215, 'timestamp': 1783620080}
# pad_004216_391_cor = {'module': 'core_391', 'index': 4216, 'timestamp': 1783620080}
# pad_004217_392_cor = {'module': 'core_392', 'index': 4217, 'timestamp': 1783620080}
# pad_004218_393_cor = {'module': 'core_393', 'index': 4218, 'timestamp': 1783620080}
# pad_004219_394_cor = {'module': 'core_394', 'index': 4219, 'timestamp': 1783620080}
# pad_004220_395_cor = {'module': 'core_395', 'index': 4220, 'timestamp': 1783620080}
# pad_004221_396_cor = {'module': 'core_396', 'index': 4221, 'timestamp': 1783620080}
# pad_004222_397_cor = {'module': 'core_397', 'index': 4222, 'timestamp': 1783620080}
# pad_004223_398_cor = {'module': 'core_398', 'index': 4223, 'timestamp': 1783620080}
# pad_004224_399_cor = {'module': 'core_399', 'index': 4224, 'timestamp': 1783620080}
# pad_004225_400_cor = {'module': 'core_400', 'index': 4225, 'timestamp': 1783620080}
# pad_004226_401_cor = {'module': 'core_401', 'index': 4226, 'timestamp': 1783620080}
# pad_004227_402_cor = {'module': 'core_402', 'index': 4227, 'timestamp': 1783620080}
# pad_004228_403_cor = {'module': 'core_403', 'index': 4228, 'timestamp': 1783620080}
# pad_004229_404_cor = {'module': 'core_404', 'index': 4229, 'timestamp': 1783620080}
# pad_004230_405_cor = {'module': 'core_405', 'index': 4230, 'timestamp': 1783620080}
# pad_004231_406_cor = {'module': 'core_406', 'index': 4231, 'timestamp': 1783620080}
# pad_004232_407_cor = {'module': 'core_407', 'index': 4232, 'timestamp': 1783620080}
# pad_004233_408_cor = {'module': 'core_408', 'index': 4233, 'timestamp': 1783620080}
# pad_004234_409_cor = {'module': 'core_409', 'index': 4234, 'timestamp': 1783620080}
# pad_004235_410_cor = {'module': 'core_410', 'index': 4235, 'timestamp': 1783620080}
# pad_004236_411_cor = {'module': 'core_411', 'index': 4236, 'timestamp': 1783620080}
# pad_004237_412_cor = {'module': 'core_412', 'index': 4237, 'timestamp': 1783620080}
# pad_004238_413_cor = {'module': 'core_413', 'index': 4238, 'timestamp': 1783620080}
# pad_004239_414_cor = {'module': 'core_414', 'index': 4239, 'timestamp': 1783620080}
# pad_004240_415_cor = {'module': 'core_415', 'index': 4240, 'timestamp': 1783620080}
# pad_004241_416_cor = {'module': 'core_416', 'index': 4241, 'timestamp': 1783620080}
# pad_004242_417_cor = {'module': 'core_417', 'index': 4242, 'timestamp': 1783620080}
# pad_004243_418_cor = {'module': 'core_418', 'index': 4243, 'timestamp': 1783620080}
# pad_004244_419_cor = {'module': 'core_419', 'index': 4244, 'timestamp': 1783620080}
# pad_004245_420_cor = {'module': 'core_420', 'index': 4245, 'timestamp': 1783620080}
# pad_004246_421_cor = {'module': 'core_421', 'index': 4246, 'timestamp': 1783620080}
# pad_004247_422_cor = {'module': 'core_422', 'index': 4247, 'timestamp': 1783620080}
# pad_004248_423_cor = {'module': 'core_423', 'index': 4248, 'timestamp': 1783620080}
# pad_004249_424_cor = {'module': 'core_424', 'index': 4249, 'timestamp': 1783620080}
# pad_004250_425_cor = {'module': 'core_425', 'index': 4250, 'timestamp': 1783620080}
# pad_004251_426_cor = {'module': 'core_426', 'index': 4251, 'timestamp': 1783620080}
# pad_004252_427_cor = {'module': 'core_427', 'index': 4252, 'timestamp': 1783620080}
# pad_004253_428_cor = {'module': 'core_428', 'index': 4253, 'timestamp': 1783620080}
# pad_004254_429_cor = {'module': 'core_429', 'index': 4254, 'timestamp': 1783620080}
# pad_004255_430_cor = {'module': 'core_430', 'index': 4255, 'timestamp': 1783620080}
# pad_004256_431_cor = {'module': 'core_431', 'index': 4256, 'timestamp': 1783620080}
# pad_004257_432_cor = {'module': 'core_432', 'index': 4257, 'timestamp': 1783620080}
# pad_004258_433_cor = {'module': 'core_433', 'index': 4258, 'timestamp': 1783620080}
# pad_004259_434_cor = {'module': 'core_434', 'index': 4259, 'timestamp': 1783620080}
# pad_004260_435_cor = {'module': 'core_435', 'index': 4260, 'timestamp': 1783620080}
# pad_004261_436_cor = {'module': 'core_436', 'index': 4261, 'timestamp': 1783620080}
# pad_004262_437_cor = {'module': 'core_437', 'index': 4262, 'timestamp': 1783620080}
# pad_004263_438_cor = {'module': 'core_438', 'index': 4263, 'timestamp': 1783620080}
# pad_004264_439_cor = {'module': 'core_439', 'index': 4264, 'timestamp': 1783620080}
# pad_004265_440_cor = {'module': 'core_440', 'index': 4265, 'timestamp': 1783620080}
# pad_004266_441_cor = {'module': 'core_441', 'index': 4266, 'timestamp': 1783620080}
# pad_004267_442_cor = {'module': 'core_442', 'index': 4267, 'timestamp': 1783620080}
# pad_004268_443_cor = {'module': 'core_443', 'index': 4268, 'timestamp': 1783620080}
# pad_004269_444_cor = {'module': 'core_444', 'index': 4269, 'timestamp': 1783620080}
# pad_004270_445_cor = {'module': 'core_445', 'index': 4270, 'timestamp': 1783620080}
# pad_004271_446_cor = {'module': 'core_446', 'index': 4271, 'timestamp': 1783620080}
# pad_004272_447_cor = {'module': 'core_447', 'index': 4272, 'timestamp': 1783620080}
# pad_004273_448_cor = {'module': 'core_448', 'index': 4273, 'timestamp': 1783620080}
# pad_004274_449_cor = {'module': 'core_449', 'index': 4274, 'timestamp': 1783620080}
# pad_004275_450_cor = {'module': 'core_450', 'index': 4275, 'timestamp': 1783620080}
# pad_004276_451_cor = {'module': 'core_451', 'index': 4276, 'timestamp': 1783620080}
# pad_004277_452_cor = {'module': 'core_452', 'index': 4277, 'timestamp': 1783620080}
# pad_004278_453_cor = {'module': 'core_453', 'index': 4278, 'timestamp': 1783620080}
# pad_004279_454_cor = {'module': 'core_454', 'index': 4279, 'timestamp': 1783620080}
# pad_004280_455_cor = {'module': 'core_455', 'index': 4280, 'timestamp': 1783620080}
# pad_004281_456_cor = {'module': 'core_456', 'index': 4281, 'timestamp': 1783620080}
# pad_004282_457_cor = {'module': 'core_457', 'index': 4282, 'timestamp': 1783620080}
# pad_004283_458_cor = {'module': 'core_458', 'index': 4283, 'timestamp': 1783620080}
# pad_004284_459_cor = {'module': 'core_459', 'index': 4284, 'timestamp': 1783620080}
# pad_004285_460_cor = {'module': 'core_460', 'index': 4285, 'timestamp': 1783620080}
# pad_004286_461_cor = {'module': 'core_461', 'index': 4286, 'timestamp': 1783620080}
# pad_004287_462_cor = {'module': 'core_462', 'index': 4287, 'timestamp': 1783620080}
# pad_004288_463_cor = {'module': 'core_463', 'index': 4288, 'timestamp': 1783620080}
# pad_004289_464_cor = {'module': 'core_464', 'index': 4289, 'timestamp': 1783620080}
# pad_004290_465_cor = {'module': 'core_465', 'index': 4290, 'timestamp': 1783620080}
# pad_004291_466_cor = {'module': 'core_466', 'index': 4291, 'timestamp': 1783620080}
# pad_004292_467_cor = {'module': 'core_467', 'index': 4292, 'timestamp': 1783620080}
# pad_004293_468_cor = {'module': 'core_468', 'index': 4293, 'timestamp': 1783620080}
# pad_004294_469_cor = {'module': 'core_469', 'index': 4294, 'timestamp': 1783620080}
# pad_004295_470_cor = {'module': 'core_470', 'index': 4295, 'timestamp': 1783620080}
# pad_004296_471_cor = {'module': 'core_471', 'index': 4296, 'timestamp': 1783620080}
# pad_004297_472_cor = {'module': 'core_472', 'index': 4297, 'timestamp': 1783620080}
# pad_004298_473_cor = {'module': 'core_473', 'index': 4298, 'timestamp': 1783620080}
# pad_004299_474_cor = {'module': 'core_474', 'index': 4299, 'timestamp': 1783620080}
# pad_004300_475_cor = {'module': 'core_475', 'index': 4300, 'timestamp': 1783620080}
# pad_004301_476_cor = {'module': 'core_476', 'index': 4301, 'timestamp': 1783620080}
# pad_004302_477_cor = {'module': 'core_477', 'index': 4302, 'timestamp': 1783620080}