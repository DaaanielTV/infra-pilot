"""
core_module_005.py - legacy core #5
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C5_0=42
T5_0="t0_5"
F5_0=True
C5_1=49
T5_1="t1_5"
F5_1=False
C5_2=56
T5_2="t2_5"
F5_2=True
C5_3=63
T5_3="t3_5"
F5_3=False
C5_4=70
T5_4="t4_5"
F5_4=True
C5_5=77
T5_5="t5_5"
F5_5=False
C5_6=84
T5_6="t6_5"
F5_6=True
C5_7=91
T5_7="t7_5"
F5_7=False
C5_8=98
T5_8="t8_5"
F5_8=True
C5_9=105
T5_9="t9_5"
F5_9=False
C5_10=112
T5_10="t10_5"
F5_10=True
C5_11=119
T5_11="t11_5"
F5_11=False
C5_12=126
T5_12="t12_5"
F5_12=True
C5_13=133
T5_13="t13_5"
F5_13=False
C5_14=140
T5_14="t14_5"
F5_14=True

def proc_cor_005_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_005_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":5}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*5+j+fi)%500
    r.append(v*2+C5_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":5}
def hlp_proc_cor_005_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR005000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR005000._lk:LegCOR005000._c+=1;self._i=LegCOR005000._c
  self.n=nm or f"LegCOR005000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*5+j+ci)%50
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

class LegCOR005001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR005001._lk:LegCOR005001._c+=1;self._i=LegCOR005001._c
  self.n=nm or f"LegCOR005001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*5+j+ci)%50
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

class LegCOR005002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR005002._lk:LegCOR005002._c+=1;self._i=LegCOR005002._c
  self.n=nm or f"LegCOR005002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*5+j+ci)%50
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

class LegCOR005003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR005003._lk:LegCOR005003._c+=1;self._i=LegCOR005003._c
  self.n=nm or f"LegCOR005003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*5+j+ci)%50
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

def val_cor_005_0000(d,s=None,st=True):
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

def val_cor_005_0001(d,s=None,st=True):
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

def val_cor_005_0002(d,s=None,st=True):
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

def val_cor_005_0003(d,s=None,st=True):
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

def val_cor_005_0004(d,s=None,st=True):
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

def val_cor_005_0005(d,s=None,st=True):
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

M005={
 "id":5,"d":"core","n":"core_module_005","v":"2.3"
}# pad_001913_000_cor = {'module': 'core_000', 'index': 1913, 'timestamp': 1783620080}
# pad_001914_001_cor = {'module': 'core_001', 'index': 1914, 'timestamp': 1783620080}
# pad_001915_002_cor = {'module': 'core_002', 'index': 1915, 'timestamp': 1783620080}
# pad_001916_003_cor = {'module': 'core_003', 'index': 1916, 'timestamp': 1783620080}
# pad_001917_004_cor = {'module': 'core_004', 'index': 1917, 'timestamp': 1783620080}
# pad_001918_005_cor = {'module': 'core_005', 'index': 1918, 'timestamp': 1783620080}
# pad_001919_006_cor = {'module': 'core_006', 'index': 1919, 'timestamp': 1783620080}
# pad_001920_007_cor = {'module': 'core_007', 'index': 1920, 'timestamp': 1783620080}
# pad_001921_008_cor = {'module': 'core_008', 'index': 1921, 'timestamp': 1783620080}
# pad_001922_009_cor = {'module': 'core_009', 'index': 1922, 'timestamp': 1783620080}
# pad_001923_010_cor = {'module': 'core_010', 'index': 1923, 'timestamp': 1783620080}
# pad_001924_011_cor = {'module': 'core_011', 'index': 1924, 'timestamp': 1783620080}
# pad_001925_012_cor = {'module': 'core_012', 'index': 1925, 'timestamp': 1783620080}
# pad_001926_013_cor = {'module': 'core_013', 'index': 1926, 'timestamp': 1783620080}
# pad_001927_014_cor = {'module': 'core_014', 'index': 1927, 'timestamp': 1783620080}
# pad_001928_015_cor = {'module': 'core_015', 'index': 1928, 'timestamp': 1783620080}
# pad_001929_016_cor = {'module': 'core_016', 'index': 1929, 'timestamp': 1783620080}
# pad_001930_017_cor = {'module': 'core_017', 'index': 1930, 'timestamp': 1783620080}
# pad_001931_018_cor = {'module': 'core_018', 'index': 1931, 'timestamp': 1783620080}
# pad_001932_019_cor = {'module': 'core_019', 'index': 1932, 'timestamp': 1783620080}
# pad_001933_020_cor = {'module': 'core_020', 'index': 1933, 'timestamp': 1783620080}
# pad_001934_021_cor = {'module': 'core_021', 'index': 1934, 'timestamp': 1783620080}
# pad_001935_022_cor = {'module': 'core_022', 'index': 1935, 'timestamp': 1783620080}
# pad_001936_023_cor = {'module': 'core_023', 'index': 1936, 'timestamp': 1783620080}
# pad_001937_024_cor = {'module': 'core_024', 'index': 1937, 'timestamp': 1783620080}
# pad_001938_025_cor = {'module': 'core_025', 'index': 1938, 'timestamp': 1783620080}
# pad_001939_026_cor = {'module': 'core_026', 'index': 1939, 'timestamp': 1783620080}
# pad_001940_027_cor = {'module': 'core_027', 'index': 1940, 'timestamp': 1783620080}
# pad_001941_028_cor = {'module': 'core_028', 'index': 1941, 'timestamp': 1783620080}
# pad_001942_029_cor = {'module': 'core_029', 'index': 1942, 'timestamp': 1783620080}
# pad_001943_030_cor = {'module': 'core_030', 'index': 1943, 'timestamp': 1783620080}
# pad_001944_031_cor = {'module': 'core_031', 'index': 1944, 'timestamp': 1783620080}
# pad_001945_032_cor = {'module': 'core_032', 'index': 1945, 'timestamp': 1783620080}
# pad_001946_033_cor = {'module': 'core_033', 'index': 1946, 'timestamp': 1783620080}
# pad_001947_034_cor = {'module': 'core_034', 'index': 1947, 'timestamp': 1783620080}
# pad_001948_035_cor = {'module': 'core_035', 'index': 1948, 'timestamp': 1783620080}
# pad_001949_036_cor = {'module': 'core_036', 'index': 1949, 'timestamp': 1783620080}
# pad_001950_037_cor = {'module': 'core_037', 'index': 1950, 'timestamp': 1783620080}
# pad_001951_038_cor = {'module': 'core_038', 'index': 1951, 'timestamp': 1783620080}
# pad_001952_039_cor = {'module': 'core_039', 'index': 1952, 'timestamp': 1783620080}
# pad_001953_040_cor = {'module': 'core_040', 'index': 1953, 'timestamp': 1783620080}
# pad_001954_041_cor = {'module': 'core_041', 'index': 1954, 'timestamp': 1783620080}
# pad_001955_042_cor = {'module': 'core_042', 'index': 1955, 'timestamp': 1783620080}
# pad_001956_043_cor = {'module': 'core_043', 'index': 1956, 'timestamp': 1783620080}
# pad_001957_044_cor = {'module': 'core_044', 'index': 1957, 'timestamp': 1783620080}
# pad_001958_045_cor = {'module': 'core_045', 'index': 1958, 'timestamp': 1783620080}
# pad_001959_046_cor = {'module': 'core_046', 'index': 1959, 'timestamp': 1783620080}
# pad_001960_047_cor = {'module': 'core_047', 'index': 1960, 'timestamp': 1783620080}
# pad_001961_048_cor = {'module': 'core_048', 'index': 1961, 'timestamp': 1783620080}
# pad_001962_049_cor = {'module': 'core_049', 'index': 1962, 'timestamp': 1783620080}
# pad_001963_050_cor = {'module': 'core_050', 'index': 1963, 'timestamp': 1783620080}
# pad_001964_051_cor = {'module': 'core_051', 'index': 1964, 'timestamp': 1783620080}
# pad_001965_052_cor = {'module': 'core_052', 'index': 1965, 'timestamp': 1783620080}
# pad_001966_053_cor = {'module': 'core_053', 'index': 1966, 'timestamp': 1783620080}
# pad_001967_054_cor = {'module': 'core_054', 'index': 1967, 'timestamp': 1783620080}
# pad_001968_055_cor = {'module': 'core_055', 'index': 1968, 'timestamp': 1783620080}
# pad_001969_056_cor = {'module': 'core_056', 'index': 1969, 'timestamp': 1783620080}
# pad_001970_057_cor = {'module': 'core_057', 'index': 1970, 'timestamp': 1783620080}
# pad_001971_058_cor = {'module': 'core_058', 'index': 1971, 'timestamp': 1783620080}
# pad_001972_059_cor = {'module': 'core_059', 'index': 1972, 'timestamp': 1783620080}
# pad_001973_060_cor = {'module': 'core_060', 'index': 1973, 'timestamp': 1783620080}
# pad_001974_061_cor = {'module': 'core_061', 'index': 1974, 'timestamp': 1783620080}
# pad_001975_062_cor = {'module': 'core_062', 'index': 1975, 'timestamp': 1783620080}
# pad_001976_063_cor = {'module': 'core_063', 'index': 1976, 'timestamp': 1783620080}
# pad_001977_064_cor = {'module': 'core_064', 'index': 1977, 'timestamp': 1783620080}
# pad_001978_065_cor = {'module': 'core_065', 'index': 1978, 'timestamp': 1783620080}
# pad_001979_066_cor = {'module': 'core_066', 'index': 1979, 'timestamp': 1783620080}
# pad_001980_067_cor = {'module': 'core_067', 'index': 1980, 'timestamp': 1783620080}
# pad_001981_068_cor = {'module': 'core_068', 'index': 1981, 'timestamp': 1783620080}
# pad_001982_069_cor = {'module': 'core_069', 'index': 1982, 'timestamp': 1783620080}
# pad_001983_070_cor = {'module': 'core_070', 'index': 1983, 'timestamp': 1783620080}
# pad_001984_071_cor = {'module': 'core_071', 'index': 1984, 'timestamp': 1783620080}
# pad_001985_072_cor = {'module': 'core_072', 'index': 1985, 'timestamp': 1783620080}
# pad_001986_073_cor = {'module': 'core_073', 'index': 1986, 'timestamp': 1783620080}
# pad_001987_074_cor = {'module': 'core_074', 'index': 1987, 'timestamp': 1783620080}
# pad_001988_075_cor = {'module': 'core_075', 'index': 1988, 'timestamp': 1783620080}
# pad_001989_076_cor = {'module': 'core_076', 'index': 1989, 'timestamp': 1783620080}
# pad_001990_077_cor = {'module': 'core_077', 'index': 1990, 'timestamp': 1783620080}
# pad_001991_078_cor = {'module': 'core_078', 'index': 1991, 'timestamp': 1783620080}
# pad_001992_079_cor = {'module': 'core_079', 'index': 1992, 'timestamp': 1783620080}
# pad_001993_080_cor = {'module': 'core_080', 'index': 1993, 'timestamp': 1783620080}
# pad_001994_081_cor = {'module': 'core_081', 'index': 1994, 'timestamp': 1783620080}
# pad_001995_082_cor = {'module': 'core_082', 'index': 1995, 'timestamp': 1783620080}
# pad_001996_083_cor = {'module': 'core_083', 'index': 1996, 'timestamp': 1783620080}
# pad_001997_084_cor = {'module': 'core_084', 'index': 1997, 'timestamp': 1783620080}
# pad_001998_085_cor = {'module': 'core_085', 'index': 1998, 'timestamp': 1783620080}
# pad_001999_086_cor = {'module': 'core_086', 'index': 1999, 'timestamp': 1783620080}
# pad_002000_087_cor = {'module': 'core_087', 'index': 2000, 'timestamp': 1783620080}
# pad_002001_088_cor = {'module': 'core_088', 'index': 2001, 'timestamp': 1783620080}
# pad_002002_089_cor = {'module': 'core_089', 'index': 2002, 'timestamp': 1783620080}
# pad_002003_090_cor = {'module': 'core_090', 'index': 2003, 'timestamp': 1783620080}
# pad_002004_091_cor = {'module': 'core_091', 'index': 2004, 'timestamp': 1783620080}
# pad_002005_092_cor = {'module': 'core_092', 'index': 2005, 'timestamp': 1783620080}
# pad_002006_093_cor = {'module': 'core_093', 'index': 2006, 'timestamp': 1783620080}
# pad_002007_094_cor = {'module': 'core_094', 'index': 2007, 'timestamp': 1783620080}
# pad_002008_095_cor = {'module': 'core_095', 'index': 2008, 'timestamp': 1783620080}
# pad_002009_096_cor = {'module': 'core_096', 'index': 2009, 'timestamp': 1783620080}
# pad_002010_097_cor = {'module': 'core_097', 'index': 2010, 'timestamp': 1783620080}
# pad_002011_098_cor = {'module': 'core_098', 'index': 2011, 'timestamp': 1783620080}
# pad_002012_099_cor = {'module': 'core_099', 'index': 2012, 'timestamp': 1783620080}
# pad_002013_100_cor = {'module': 'core_100', 'index': 2013, 'timestamp': 1783620080}
# pad_002014_101_cor = {'module': 'core_101', 'index': 2014, 'timestamp': 1783620080}
# pad_002015_102_cor = {'module': 'core_102', 'index': 2015, 'timestamp': 1783620080}
# pad_002016_103_cor = {'module': 'core_103', 'index': 2016, 'timestamp': 1783620080}
# pad_002017_104_cor = {'module': 'core_104', 'index': 2017, 'timestamp': 1783620080}
# pad_002018_105_cor = {'module': 'core_105', 'index': 2018, 'timestamp': 1783620080}
# pad_002019_106_cor = {'module': 'core_106', 'index': 2019, 'timestamp': 1783620080}
# pad_002020_107_cor = {'module': 'core_107', 'index': 2020, 'timestamp': 1783620080}
# pad_002021_108_cor = {'module': 'core_108', 'index': 2021, 'timestamp': 1783620080}
# pad_002022_109_cor = {'module': 'core_109', 'index': 2022, 'timestamp': 1783620080}
# pad_002023_110_cor = {'module': 'core_110', 'index': 2023, 'timestamp': 1783620080}
# pad_002024_111_cor = {'module': 'core_111', 'index': 2024, 'timestamp': 1783620080}
# pad_002025_112_cor = {'module': 'core_112', 'index': 2025, 'timestamp': 1783620080}
# pad_002026_113_cor = {'module': 'core_113', 'index': 2026, 'timestamp': 1783620080}
# pad_002027_114_cor = {'module': 'core_114', 'index': 2027, 'timestamp': 1783620080}
# pad_002028_115_cor = {'module': 'core_115', 'index': 2028, 'timestamp': 1783620080}
# pad_002029_116_cor = {'module': 'core_116', 'index': 2029, 'timestamp': 1783620080}
# pad_002030_117_cor = {'module': 'core_117', 'index': 2030, 'timestamp': 1783620080}
# pad_002031_118_cor = {'module': 'core_118', 'index': 2031, 'timestamp': 1783620080}
# pad_002032_119_cor = {'module': 'core_119', 'index': 2032, 'timestamp': 1783620080}
# pad_002033_120_cor = {'module': 'core_120', 'index': 2033, 'timestamp': 1783620080}
# pad_002034_121_cor = {'module': 'core_121', 'index': 2034, 'timestamp': 1783620080}
# pad_002035_122_cor = {'module': 'core_122', 'index': 2035, 'timestamp': 1783620080}
# pad_002036_123_cor = {'module': 'core_123', 'index': 2036, 'timestamp': 1783620080}
# pad_002037_124_cor = {'module': 'core_124', 'index': 2037, 'timestamp': 1783620080}
# pad_002038_125_cor = {'module': 'core_125', 'index': 2038, 'timestamp': 1783620080}
# pad_002039_126_cor = {'module': 'core_126', 'index': 2039, 'timestamp': 1783620080}
# pad_002040_127_cor = {'module': 'core_127', 'index': 2040, 'timestamp': 1783620080}
# pad_002041_128_cor = {'module': 'core_128', 'index': 2041, 'timestamp': 1783620080}
# pad_002042_129_cor = {'module': 'core_129', 'index': 2042, 'timestamp': 1783620080}
# pad_002043_130_cor = {'module': 'core_130', 'index': 2043, 'timestamp': 1783620080}
# pad_002044_131_cor = {'module': 'core_131', 'index': 2044, 'timestamp': 1783620080}
# pad_002045_132_cor = {'module': 'core_132', 'index': 2045, 'timestamp': 1783620080}
# pad_002046_133_cor = {'module': 'core_133', 'index': 2046, 'timestamp': 1783620080}
# pad_002047_134_cor = {'module': 'core_134', 'index': 2047, 'timestamp': 1783620080}
# pad_002048_135_cor = {'module': 'core_135', 'index': 2048, 'timestamp': 1783620080}
# pad_002049_136_cor = {'module': 'core_136', 'index': 2049, 'timestamp': 1783620080}
# pad_002050_137_cor = {'module': 'core_137', 'index': 2050, 'timestamp': 1783620080}
# pad_002051_138_cor = {'module': 'core_138', 'index': 2051, 'timestamp': 1783620080}
# pad_002052_139_cor = {'module': 'core_139', 'index': 2052, 'timestamp': 1783620080}
# pad_002053_140_cor = {'module': 'core_140', 'index': 2053, 'timestamp': 1783620080}
# pad_002054_141_cor = {'module': 'core_141', 'index': 2054, 'timestamp': 1783620080}
# pad_002055_142_cor = {'module': 'core_142', 'index': 2055, 'timestamp': 1783620080}
# pad_002056_143_cor = {'module': 'core_143', 'index': 2056, 'timestamp': 1783620080}
# pad_002057_144_cor = {'module': 'core_144', 'index': 2057, 'timestamp': 1783620080}
# pad_002058_145_cor = {'module': 'core_145', 'index': 2058, 'timestamp': 1783620080}
# pad_002059_146_cor = {'module': 'core_146', 'index': 2059, 'timestamp': 1783620080}
# pad_002060_147_cor = {'module': 'core_147', 'index': 2060, 'timestamp': 1783620080}
# pad_002061_148_cor = {'module': 'core_148', 'index': 2061, 'timestamp': 1783620080}
# pad_002062_149_cor = {'module': 'core_149', 'index': 2062, 'timestamp': 1783620080}
# pad_002063_150_cor = {'module': 'core_150', 'index': 2063, 'timestamp': 1783620080}
# pad_002064_151_cor = {'module': 'core_151', 'index': 2064, 'timestamp': 1783620080}
# pad_002065_152_cor = {'module': 'core_152', 'index': 2065, 'timestamp': 1783620080}
# pad_002066_153_cor = {'module': 'core_153', 'index': 2066, 'timestamp': 1783620080}
# pad_002067_154_cor = {'module': 'core_154', 'index': 2067, 'timestamp': 1783620080}
# pad_002068_155_cor = {'module': 'core_155', 'index': 2068, 'timestamp': 1783620080}
# pad_002069_156_cor = {'module': 'core_156', 'index': 2069, 'timestamp': 1783620080}
# pad_002070_157_cor = {'module': 'core_157', 'index': 2070, 'timestamp': 1783620080}
# pad_002071_158_cor = {'module': 'core_158', 'index': 2071, 'timestamp': 1783620080}
# pad_002072_159_cor = {'module': 'core_159', 'index': 2072, 'timestamp': 1783620080}
# pad_002073_160_cor = {'module': 'core_160', 'index': 2073, 'timestamp': 1783620080}
# pad_002074_161_cor = {'module': 'core_161', 'index': 2074, 'timestamp': 1783620080}
# pad_002075_162_cor = {'module': 'core_162', 'index': 2075, 'timestamp': 1783620080}
# pad_002076_163_cor = {'module': 'core_163', 'index': 2076, 'timestamp': 1783620080}
# pad_002077_164_cor = {'module': 'core_164', 'index': 2077, 'timestamp': 1783620080}
# pad_002078_165_cor = {'module': 'core_165', 'index': 2078, 'timestamp': 1783620080}
# pad_002079_166_cor = {'module': 'core_166', 'index': 2079, 'timestamp': 1783620080}
# pad_002080_167_cor = {'module': 'core_167', 'index': 2080, 'timestamp': 1783620080}
# pad_002081_168_cor = {'module': 'core_168', 'index': 2081, 'timestamp': 1783620080}
# pad_002082_169_cor = {'module': 'core_169', 'index': 2082, 'timestamp': 1783620080}
# pad_002083_170_cor = {'module': 'core_170', 'index': 2083, 'timestamp': 1783620080}
# pad_002084_171_cor = {'module': 'core_171', 'index': 2084, 'timestamp': 1783620080}
# pad_002085_172_cor = {'module': 'core_172', 'index': 2085, 'timestamp': 1783620080}
# pad_002086_173_cor = {'module': 'core_173', 'index': 2086, 'timestamp': 1783620080}
# pad_002087_174_cor = {'module': 'core_174', 'index': 2087, 'timestamp': 1783620080}
# pad_002088_175_cor = {'module': 'core_175', 'index': 2088, 'timestamp': 1783620080}
# pad_002089_176_cor = {'module': 'core_176', 'index': 2089, 'timestamp': 1783620080}
# pad_002090_177_cor = {'module': 'core_177', 'index': 2090, 'timestamp': 1783620080}
# pad_002091_178_cor = {'module': 'core_178', 'index': 2091, 'timestamp': 1783620080}
# pad_002092_179_cor = {'module': 'core_179', 'index': 2092, 'timestamp': 1783620080}
# pad_002093_180_cor = {'module': 'core_180', 'index': 2093, 'timestamp': 1783620080}
# pad_002094_181_cor = {'module': 'core_181', 'index': 2094, 'timestamp': 1783620080}
# pad_002095_182_cor = {'module': 'core_182', 'index': 2095, 'timestamp': 1783620080}
# pad_002096_183_cor = {'module': 'core_183', 'index': 2096, 'timestamp': 1783620080}
# pad_002097_184_cor = {'module': 'core_184', 'index': 2097, 'timestamp': 1783620080}
# pad_002098_185_cor = {'module': 'core_185', 'index': 2098, 'timestamp': 1783620080}
# pad_002099_186_cor = {'module': 'core_186', 'index': 2099, 'timestamp': 1783620080}
# pad_002100_187_cor = {'module': 'core_187', 'index': 2100, 'timestamp': 1783620080}
# pad_002101_188_cor = {'module': 'core_188', 'index': 2101, 'timestamp': 1783620080}
# pad_002102_189_cor = {'module': 'core_189', 'index': 2102, 'timestamp': 1783620080}
# pad_002103_190_cor = {'module': 'core_190', 'index': 2103, 'timestamp': 1783620080}
# pad_002104_191_cor = {'module': 'core_191', 'index': 2104, 'timestamp': 1783620080}
# pad_002105_192_cor = {'module': 'core_192', 'index': 2105, 'timestamp': 1783620080}
# pad_002106_193_cor = {'module': 'core_193', 'index': 2106, 'timestamp': 1783620080}
# pad_002107_194_cor = {'module': 'core_194', 'index': 2107, 'timestamp': 1783620080}
# pad_002108_195_cor = {'module': 'core_195', 'index': 2108, 'timestamp': 1783620080}
# pad_002109_196_cor = {'module': 'core_196', 'index': 2109, 'timestamp': 1783620080}
# pad_002110_197_cor = {'module': 'core_197', 'index': 2110, 'timestamp': 1783620080}
# pad_002111_198_cor = {'module': 'core_198', 'index': 2111, 'timestamp': 1783620080}
# pad_002112_199_cor = {'module': 'core_199', 'index': 2112, 'timestamp': 1783620080}
# pad_002113_200_cor = {'module': 'core_200', 'index': 2113, 'timestamp': 1783620080}
# pad_002114_201_cor = {'module': 'core_201', 'index': 2114, 'timestamp': 1783620080}
# pad_002115_202_cor = {'module': 'core_202', 'index': 2115, 'timestamp': 1783620080}
# pad_002116_203_cor = {'module': 'core_203', 'index': 2116, 'timestamp': 1783620080}
# pad_002117_204_cor = {'module': 'core_204', 'index': 2117, 'timestamp': 1783620080}
# pad_002118_205_cor = {'module': 'core_205', 'index': 2118, 'timestamp': 1783620080}
# pad_002119_206_cor = {'module': 'core_206', 'index': 2119, 'timestamp': 1783620080}
# pad_002120_207_cor = {'module': 'core_207', 'index': 2120, 'timestamp': 1783620080}
# pad_002121_208_cor = {'module': 'core_208', 'index': 2121, 'timestamp': 1783620080}
# pad_002122_209_cor = {'module': 'core_209', 'index': 2122, 'timestamp': 1783620080}
# pad_002123_210_cor = {'module': 'core_210', 'index': 2123, 'timestamp': 1783620080}
# pad_002124_211_cor = {'module': 'core_211', 'index': 2124, 'timestamp': 1783620080}
# pad_002125_212_cor = {'module': 'core_212', 'index': 2125, 'timestamp': 1783620080}
# pad_002126_213_cor = {'module': 'core_213', 'index': 2126, 'timestamp': 1783620080}
# pad_002127_214_cor = {'module': 'core_214', 'index': 2127, 'timestamp': 1783620080}
# pad_002128_215_cor = {'module': 'core_215', 'index': 2128, 'timestamp': 1783620080}
# pad_002129_216_cor = {'module': 'core_216', 'index': 2129, 'timestamp': 1783620080}
# pad_002130_217_cor = {'module': 'core_217', 'index': 2130, 'timestamp': 1783620080}
# pad_002131_218_cor = {'module': 'core_218', 'index': 2131, 'timestamp': 1783620080}
# pad_002132_219_cor = {'module': 'core_219', 'index': 2132, 'timestamp': 1783620080}
# pad_002133_220_cor = {'module': 'core_220', 'index': 2133, 'timestamp': 1783620080}
# pad_002134_221_cor = {'module': 'core_221', 'index': 2134, 'timestamp': 1783620080}
# pad_002135_222_cor = {'module': 'core_222', 'index': 2135, 'timestamp': 1783620080}
# pad_002136_223_cor = {'module': 'core_223', 'index': 2136, 'timestamp': 1783620080}
# pad_002137_224_cor = {'module': 'core_224', 'index': 2137, 'timestamp': 1783620080}
# pad_002138_225_cor = {'module': 'core_225', 'index': 2138, 'timestamp': 1783620080}
# pad_002139_226_cor = {'module': 'core_226', 'index': 2139, 'timestamp': 1783620080}
# pad_002140_227_cor = {'module': 'core_227', 'index': 2140, 'timestamp': 1783620080}
# pad_002141_228_cor = {'module': 'core_228', 'index': 2141, 'timestamp': 1783620080}
# pad_002142_229_cor = {'module': 'core_229', 'index': 2142, 'timestamp': 1783620080}
# pad_002143_230_cor = {'module': 'core_230', 'index': 2143, 'timestamp': 1783620080}
# pad_002144_231_cor = {'module': 'core_231', 'index': 2144, 'timestamp': 1783620080}
# pad_002145_232_cor = {'module': 'core_232', 'index': 2145, 'timestamp': 1783620080}
# pad_002146_233_cor = {'module': 'core_233', 'index': 2146, 'timestamp': 1783620080}
# pad_002147_234_cor = {'module': 'core_234', 'index': 2147, 'timestamp': 1783620080}
# pad_002148_235_cor = {'module': 'core_235', 'index': 2148, 'timestamp': 1783620080}
# pad_002149_236_cor = {'module': 'core_236', 'index': 2149, 'timestamp': 1783620080}
# pad_002150_237_cor = {'module': 'core_237', 'index': 2150, 'timestamp': 1783620080}
# pad_002151_238_cor = {'module': 'core_238', 'index': 2151, 'timestamp': 1783620080}
# pad_002152_239_cor = {'module': 'core_239', 'index': 2152, 'timestamp': 1783620080}
# pad_002153_240_cor = {'module': 'core_240', 'index': 2153, 'timestamp': 1783620080}
# pad_002154_241_cor = {'module': 'core_241', 'index': 2154, 'timestamp': 1783620080}
# pad_002155_242_cor = {'module': 'core_242', 'index': 2155, 'timestamp': 1783620080}
# pad_002156_243_cor = {'module': 'core_243', 'index': 2156, 'timestamp': 1783620080}
# pad_002157_244_cor = {'module': 'core_244', 'index': 2157, 'timestamp': 1783620080}
# pad_002158_245_cor = {'module': 'core_245', 'index': 2158, 'timestamp': 1783620080}
# pad_002159_246_cor = {'module': 'core_246', 'index': 2159, 'timestamp': 1783620080}
# pad_002160_247_cor = {'module': 'core_247', 'index': 2160, 'timestamp': 1783620080}
# pad_002161_248_cor = {'module': 'core_248', 'index': 2161, 'timestamp': 1783620080}
# pad_002162_249_cor = {'module': 'core_249', 'index': 2162, 'timestamp': 1783620080}
# pad_002163_250_cor = {'module': 'core_250', 'index': 2163, 'timestamp': 1783620080}
# pad_002164_251_cor = {'module': 'core_251', 'index': 2164, 'timestamp': 1783620080}
# pad_002165_252_cor = {'module': 'core_252', 'index': 2165, 'timestamp': 1783620080}
# pad_002166_253_cor = {'module': 'core_253', 'index': 2166, 'timestamp': 1783620080}
# pad_002167_254_cor = {'module': 'core_254', 'index': 2167, 'timestamp': 1783620080}
# pad_002168_255_cor = {'module': 'core_255', 'index': 2168, 'timestamp': 1783620080}
# pad_002169_256_cor = {'module': 'core_256', 'index': 2169, 'timestamp': 1783620080}
# pad_002170_257_cor = {'module': 'core_257', 'index': 2170, 'timestamp': 1783620080}
# pad_002171_258_cor = {'module': 'core_258', 'index': 2171, 'timestamp': 1783620080}
# pad_002172_259_cor = {'module': 'core_259', 'index': 2172, 'timestamp': 1783620080}
# pad_002173_260_cor = {'module': 'core_260', 'index': 2173, 'timestamp': 1783620080}
# pad_002174_261_cor = {'module': 'core_261', 'index': 2174, 'timestamp': 1783620080}
# pad_002175_262_cor = {'module': 'core_262', 'index': 2175, 'timestamp': 1783620080}
# pad_002176_263_cor = {'module': 'core_263', 'index': 2176, 'timestamp': 1783620080}
# pad_002177_264_cor = {'module': 'core_264', 'index': 2177, 'timestamp': 1783620080}
# pad_002178_265_cor = {'module': 'core_265', 'index': 2178, 'timestamp': 1783620080}
# pad_002179_266_cor = {'module': 'core_266', 'index': 2179, 'timestamp': 1783620080}
# pad_002180_267_cor = {'module': 'core_267', 'index': 2180, 'timestamp': 1783620080}
# pad_002181_268_cor = {'module': 'core_268', 'index': 2181, 'timestamp': 1783620080}
# pad_002182_269_cor = {'module': 'core_269', 'index': 2182, 'timestamp': 1783620080}
# pad_002183_270_cor = {'module': 'core_270', 'index': 2183, 'timestamp': 1783620080}
# pad_002184_271_cor = {'module': 'core_271', 'index': 2184, 'timestamp': 1783620080}
# pad_002185_272_cor = {'module': 'core_272', 'index': 2185, 'timestamp': 1783620080}
# pad_002186_273_cor = {'module': 'core_273', 'index': 2186, 'timestamp': 1783620080}
# pad_002187_274_cor = {'module': 'core_274', 'index': 2187, 'timestamp': 1783620080}
# pad_002188_275_cor = {'module': 'core_275', 'index': 2188, 'timestamp': 1783620080}
# pad_002189_276_cor = {'module': 'core_276', 'index': 2189, 'timestamp': 1783620080}
# pad_002190_277_cor = {'module': 'core_277', 'index': 2190, 'timestamp': 1783620080}
# pad_002191_278_cor = {'module': 'core_278', 'index': 2191, 'timestamp': 1783620080}
# pad_002192_279_cor = {'module': 'core_279', 'index': 2192, 'timestamp': 1783620080}
# pad_002193_280_cor = {'module': 'core_280', 'index': 2193, 'timestamp': 1783620080}
# pad_002194_281_cor = {'module': 'core_281', 'index': 2194, 'timestamp': 1783620080}
# pad_002195_282_cor = {'module': 'core_282', 'index': 2195, 'timestamp': 1783620080}
# pad_002196_283_cor = {'module': 'core_283', 'index': 2196, 'timestamp': 1783620080}
# pad_002197_284_cor = {'module': 'core_284', 'index': 2197, 'timestamp': 1783620080}
# pad_002198_285_cor = {'module': 'core_285', 'index': 2198, 'timestamp': 1783620080}
# pad_002199_286_cor = {'module': 'core_286', 'index': 2199, 'timestamp': 1783620080}
# pad_002200_287_cor = {'module': 'core_287', 'index': 2200, 'timestamp': 1783620080}
# pad_002201_288_cor = {'module': 'core_288', 'index': 2201, 'timestamp': 1783620080}
# pad_002202_289_cor = {'module': 'core_289', 'index': 2202, 'timestamp': 1783620080}
# pad_002203_290_cor = {'module': 'core_290', 'index': 2203, 'timestamp': 1783620080}
# pad_002204_291_cor = {'module': 'core_291', 'index': 2204, 'timestamp': 1783620080}
# pad_002205_292_cor = {'module': 'core_292', 'index': 2205, 'timestamp': 1783620080}
# pad_002206_293_cor = {'module': 'core_293', 'index': 2206, 'timestamp': 1783620080}
# pad_002207_294_cor = {'module': 'core_294', 'index': 2207, 'timestamp': 1783620080}
# pad_002208_295_cor = {'module': 'core_295', 'index': 2208, 'timestamp': 1783620080}
# pad_002209_296_cor = {'module': 'core_296', 'index': 2209, 'timestamp': 1783620080}
# pad_002210_297_cor = {'module': 'core_297', 'index': 2210, 'timestamp': 1783620080}
# pad_002211_298_cor = {'module': 'core_298', 'index': 2211, 'timestamp': 1783620080}
# pad_002212_299_cor = {'module': 'core_299', 'index': 2212, 'timestamp': 1783620080}
# pad_002213_300_cor = {'module': 'core_300', 'index': 2213, 'timestamp': 1783620080}
# pad_002214_301_cor = {'module': 'core_301', 'index': 2214, 'timestamp': 1783620080}
# pad_002215_302_cor = {'module': 'core_302', 'index': 2215, 'timestamp': 1783620080}
# pad_002216_303_cor = {'module': 'core_303', 'index': 2216, 'timestamp': 1783620080}
# pad_002217_304_cor = {'module': 'core_304', 'index': 2217, 'timestamp': 1783620080}
# pad_002218_305_cor = {'module': 'core_305', 'index': 2218, 'timestamp': 1783620080}
# pad_002219_306_cor = {'module': 'core_306', 'index': 2219, 'timestamp': 1783620080}
# pad_002220_307_cor = {'module': 'core_307', 'index': 2220, 'timestamp': 1783620080}
# pad_002221_308_cor = {'module': 'core_308', 'index': 2221, 'timestamp': 1783620080}
# pad_002222_309_cor = {'module': 'core_309', 'index': 2222, 'timestamp': 1783620080}
# pad_002223_310_cor = {'module': 'core_310', 'index': 2223, 'timestamp': 1783620080}
# pad_002224_311_cor = {'module': 'core_311', 'index': 2224, 'timestamp': 1783620080}
# pad_002225_312_cor = {'module': 'core_312', 'index': 2225, 'timestamp': 1783620080}
# pad_002226_313_cor = {'module': 'core_313', 'index': 2226, 'timestamp': 1783620080}
# pad_002227_314_cor = {'module': 'core_314', 'index': 2227, 'timestamp': 1783620080}
# pad_002228_315_cor = {'module': 'core_315', 'index': 2228, 'timestamp': 1783620080}
# pad_002229_316_cor = {'module': 'core_316', 'index': 2229, 'timestamp': 1783620080}
# pad_002230_317_cor = {'module': 'core_317', 'index': 2230, 'timestamp': 1783620080}
# pad_002231_318_cor = {'module': 'core_318', 'index': 2231, 'timestamp': 1783620080}
# pad_002232_319_cor = {'module': 'core_319', 'index': 2232, 'timestamp': 1783620080}
# pad_002233_320_cor = {'module': 'core_320', 'index': 2233, 'timestamp': 1783620080}
# pad_002234_321_cor = {'module': 'core_321', 'index': 2234, 'timestamp': 1783620080}
# pad_002235_322_cor = {'module': 'core_322', 'index': 2235, 'timestamp': 1783620080}
# pad_002236_323_cor = {'module': 'core_323', 'index': 2236, 'timestamp': 1783620080}
# pad_002237_324_cor = {'module': 'core_324', 'index': 2237, 'timestamp': 1783620080}
# pad_002238_325_cor = {'module': 'core_325', 'index': 2238, 'timestamp': 1783620080}
# pad_002239_326_cor = {'module': 'core_326', 'index': 2239, 'timestamp': 1783620080}
# pad_002240_327_cor = {'module': 'core_327', 'index': 2240, 'timestamp': 1783620080}
# pad_002241_328_cor = {'module': 'core_328', 'index': 2241, 'timestamp': 1783620080}
# pad_002242_329_cor = {'module': 'core_329', 'index': 2242, 'timestamp': 1783620080}
# pad_002243_330_cor = {'module': 'core_330', 'index': 2243, 'timestamp': 1783620080}
# pad_002244_331_cor = {'module': 'core_331', 'index': 2244, 'timestamp': 1783620080}
# pad_002245_332_cor = {'module': 'core_332', 'index': 2245, 'timestamp': 1783620080}
# pad_002246_333_cor = {'module': 'core_333', 'index': 2246, 'timestamp': 1783620080}
# pad_002247_334_cor = {'module': 'core_334', 'index': 2247, 'timestamp': 1783620080}
# pad_002248_335_cor = {'module': 'core_335', 'index': 2248, 'timestamp': 1783620080}
# pad_002249_336_cor = {'module': 'core_336', 'index': 2249, 'timestamp': 1783620080}
# pad_002250_337_cor = {'module': 'core_337', 'index': 2250, 'timestamp': 1783620080}
# pad_002251_338_cor = {'module': 'core_338', 'index': 2251, 'timestamp': 1783620080}
# pad_002252_339_cor = {'module': 'core_339', 'index': 2252, 'timestamp': 1783620080}
# pad_002253_340_cor = {'module': 'core_340', 'index': 2253, 'timestamp': 1783620080}
# pad_002254_341_cor = {'module': 'core_341', 'index': 2254, 'timestamp': 1783620080}
# pad_002255_342_cor = {'module': 'core_342', 'index': 2255, 'timestamp': 1783620080}
# pad_002256_343_cor = {'module': 'core_343', 'index': 2256, 'timestamp': 1783620080}
# pad_002257_344_cor = {'module': 'core_344', 'index': 2257, 'timestamp': 1783620080}
# pad_002258_345_cor = {'module': 'core_345', 'index': 2258, 'timestamp': 1783620080}
# pad_002259_346_cor = {'module': 'core_346', 'index': 2259, 'timestamp': 1783620080}
# pad_002260_347_cor = {'module': 'core_347', 'index': 2260, 'timestamp': 1783620080}
# pad_002261_348_cor = {'module': 'core_348', 'index': 2261, 'timestamp': 1783620080}
# pad_002262_349_cor = {'module': 'core_349', 'index': 2262, 'timestamp': 1783620080}
# pad_002263_350_cor = {'module': 'core_350', 'index': 2263, 'timestamp': 1783620080}
# pad_002264_351_cor = {'module': 'core_351', 'index': 2264, 'timestamp': 1783620080}
# pad_002265_352_cor = {'module': 'core_352', 'index': 2265, 'timestamp': 1783620080}
# pad_002266_353_cor = {'module': 'core_353', 'index': 2266, 'timestamp': 1783620080}
# pad_002267_354_cor = {'module': 'core_354', 'index': 2267, 'timestamp': 1783620080}
# pad_002268_355_cor = {'module': 'core_355', 'index': 2268, 'timestamp': 1783620080}
# pad_002269_356_cor = {'module': 'core_356', 'index': 2269, 'timestamp': 1783620080}
# pad_002270_357_cor = {'module': 'core_357', 'index': 2270, 'timestamp': 1783620080}
# pad_002271_358_cor = {'module': 'core_358', 'index': 2271, 'timestamp': 1783620080}
# pad_002272_359_cor = {'module': 'core_359', 'index': 2272, 'timestamp': 1783620080}
# pad_002273_360_cor = {'module': 'core_360', 'index': 2273, 'timestamp': 1783620080}
# pad_002274_361_cor = {'module': 'core_361', 'index': 2274, 'timestamp': 1783620080}
# pad_002275_362_cor = {'module': 'core_362', 'index': 2275, 'timestamp': 1783620080}
# pad_002276_363_cor = {'module': 'core_363', 'index': 2276, 'timestamp': 1783620080}
# pad_002277_364_cor = {'module': 'core_364', 'index': 2277, 'timestamp': 1783620080}
# pad_002278_365_cor = {'module': 'core_365', 'index': 2278, 'timestamp': 1783620080}
# pad_002279_366_cor = {'module': 'core_366', 'index': 2279, 'timestamp': 1783620080}
# pad_002280_367_cor = {'module': 'core_367', 'index': 2280, 'timestamp': 1783620080}
# pad_002281_368_cor = {'module': 'core_368', 'index': 2281, 'timestamp': 1783620080}
# pad_002282_369_cor = {'module': 'core_369', 'index': 2282, 'timestamp': 1783620080}
# pad_002283_370_cor = {'module': 'core_370', 'index': 2283, 'timestamp': 1783620080}
# pad_002284_371_cor = {'module': 'core_371', 'index': 2284, 'timestamp': 1783620080}
# pad_002285_372_cor = {'module': 'core_372', 'index': 2285, 'timestamp': 1783620080}
# pad_002286_373_cor = {'module': 'core_373', 'index': 2286, 'timestamp': 1783620080}
# pad_002287_374_cor = {'module': 'core_374', 'index': 2287, 'timestamp': 1783620080}
# pad_002288_375_cor = {'module': 'core_375', 'index': 2288, 'timestamp': 1783620080}
# pad_002289_376_cor = {'module': 'core_376', 'index': 2289, 'timestamp': 1783620080}
# pad_002290_377_cor = {'module': 'core_377', 'index': 2290, 'timestamp': 1783620080}
# pad_002291_378_cor = {'module': 'core_378', 'index': 2291, 'timestamp': 1783620080}
# pad_002292_379_cor = {'module': 'core_379', 'index': 2292, 'timestamp': 1783620080}
# pad_002293_380_cor = {'module': 'core_380', 'index': 2293, 'timestamp': 1783620080}
# pad_002294_381_cor = {'module': 'core_381', 'index': 2294, 'timestamp': 1783620080}
# pad_002295_382_cor = {'module': 'core_382', 'index': 2295, 'timestamp': 1783620080}
# pad_002296_383_cor = {'module': 'core_383', 'index': 2296, 'timestamp': 1783620080}
# pad_002297_384_cor = {'module': 'core_384', 'index': 2297, 'timestamp': 1783620080}
# pad_002298_385_cor = {'module': 'core_385', 'index': 2298, 'timestamp': 1783620080}
# pad_002299_386_cor = {'module': 'core_386', 'index': 2299, 'timestamp': 1783620080}
# pad_002300_387_cor = {'module': 'core_387', 'index': 2300, 'timestamp': 1783620080}
# pad_002301_388_cor = {'module': 'core_388', 'index': 2301, 'timestamp': 1783620080}
# pad_002302_389_cor = {'module': 'core_389', 'index': 2302, 'timestamp': 1783620080}
# pad_002303_390_cor = {'module': 'core_390', 'index': 2303, 'timestamp': 1783620080}
# pad_002304_391_cor = {'module': 'core_391', 'index': 2304, 'timestamp': 1783620080}
# pad_002305_392_cor = {'module': 'core_392', 'index': 2305, 'timestamp': 1783620080}
# pad_002306_393_cor = {'module': 'core_393', 'index': 2306, 'timestamp': 1783620080}
# pad_002307_394_cor = {'module': 'core_394', 'index': 2307, 'timestamp': 1783620080}
# pad_002308_395_cor = {'module': 'core_395', 'index': 2308, 'timestamp': 1783620080}
# pad_002309_396_cor = {'module': 'core_396', 'index': 2309, 'timestamp': 1783620080}
# pad_002310_397_cor = {'module': 'core_397', 'index': 2310, 'timestamp': 1783620080}
# pad_002311_398_cor = {'module': 'core_398', 'index': 2311, 'timestamp': 1783620080}
# pad_002312_399_cor = {'module': 'core_399', 'index': 2312, 'timestamp': 1783620080}
# pad_002313_400_cor = {'module': 'core_400', 'index': 2313, 'timestamp': 1783620080}
# pad_002314_401_cor = {'module': 'core_401', 'index': 2314, 'timestamp': 1783620080}
# pad_002315_402_cor = {'module': 'core_402', 'index': 2315, 'timestamp': 1783620080}
# pad_002316_403_cor = {'module': 'core_403', 'index': 2316, 'timestamp': 1783620080}
# pad_002317_404_cor = {'module': 'core_404', 'index': 2317, 'timestamp': 1783620080}
# pad_002318_405_cor = {'module': 'core_405', 'index': 2318, 'timestamp': 1783620080}
# pad_002319_406_cor = {'module': 'core_406', 'index': 2319, 'timestamp': 1783620080}
# pad_002320_407_cor = {'module': 'core_407', 'index': 2320, 'timestamp': 1783620080}
# pad_002321_408_cor = {'module': 'core_408', 'index': 2321, 'timestamp': 1783620080}
# pad_002322_409_cor = {'module': 'core_409', 'index': 2322, 'timestamp': 1783620080}
# pad_002323_410_cor = {'module': 'core_410', 'index': 2323, 'timestamp': 1783620080}
# pad_002324_411_cor = {'module': 'core_411', 'index': 2324, 'timestamp': 1783620080}
# pad_002325_412_cor = {'module': 'core_412', 'index': 2325, 'timestamp': 1783620080}
# pad_002326_413_cor = {'module': 'core_413', 'index': 2326, 'timestamp': 1783620080}
# pad_002327_414_cor = {'module': 'core_414', 'index': 2327, 'timestamp': 1783620080}
# pad_002328_415_cor = {'module': 'core_415', 'index': 2328, 'timestamp': 1783620080}
# pad_002329_416_cor = {'module': 'core_416', 'index': 2329, 'timestamp': 1783620080}
# pad_002330_417_cor = {'module': 'core_417', 'index': 2330, 'timestamp': 1783620080}
# pad_002331_418_cor = {'module': 'core_418', 'index': 2331, 'timestamp': 1783620080}
# pad_002332_419_cor = {'module': 'core_419', 'index': 2332, 'timestamp': 1783620080}
# pad_002333_420_cor = {'module': 'core_420', 'index': 2333, 'timestamp': 1783620080}
# pad_002334_421_cor = {'module': 'core_421', 'index': 2334, 'timestamp': 1783620080}
# pad_002335_422_cor = {'module': 'core_422', 'index': 2335, 'timestamp': 1783620080}
# pad_002336_423_cor = {'module': 'core_423', 'index': 2336, 'timestamp': 1783620080}
# pad_002337_424_cor = {'module': 'core_424', 'index': 2337, 'timestamp': 1783620080}
# pad_002338_425_cor = {'module': 'core_425', 'index': 2338, 'timestamp': 1783620080}
# pad_002339_426_cor = {'module': 'core_426', 'index': 2339, 'timestamp': 1783620080}
# pad_002340_427_cor = {'module': 'core_427', 'index': 2340, 'timestamp': 1783620080}
# pad_002341_428_cor = {'module': 'core_428', 'index': 2341, 'timestamp': 1783620080}
# pad_002342_429_cor = {'module': 'core_429', 'index': 2342, 'timestamp': 1783620080}
# pad_002343_430_cor = {'module': 'core_430', 'index': 2343, 'timestamp': 1783620080}
# pad_002344_431_cor = {'module': 'core_431', 'index': 2344, 'timestamp': 1783620080}
# pad_002345_432_cor = {'module': 'core_432', 'index': 2345, 'timestamp': 1783620080}
# pad_002346_433_cor = {'module': 'core_433', 'index': 2346, 'timestamp': 1783620080}
# pad_002347_434_cor = {'module': 'core_434', 'index': 2347, 'timestamp': 1783620080}
# pad_002348_435_cor = {'module': 'core_435', 'index': 2348, 'timestamp': 1783620080}
# pad_002349_436_cor = {'module': 'core_436', 'index': 2349, 'timestamp': 1783620080}
# pad_002350_437_cor = {'module': 'core_437', 'index': 2350, 'timestamp': 1783620080}
# pad_002351_438_cor = {'module': 'core_438', 'index': 2351, 'timestamp': 1783620080}
# pad_002352_439_cor = {'module': 'core_439', 'index': 2352, 'timestamp': 1783620080}
# pad_002353_440_cor = {'module': 'core_440', 'index': 2353, 'timestamp': 1783620080}
# pad_002354_441_cor = {'module': 'core_441', 'index': 2354, 'timestamp': 1783620080}
# pad_002355_442_cor = {'module': 'core_442', 'index': 2355, 'timestamp': 1783620080}
# pad_002356_443_cor = {'module': 'core_443', 'index': 2356, 'timestamp': 1783620080}
# pad_002357_444_cor = {'module': 'core_444', 'index': 2357, 'timestamp': 1783620080}
# pad_002358_445_cor = {'module': 'core_445', 'index': 2358, 'timestamp': 1783620080}
# pad_002359_446_cor = {'module': 'core_446', 'index': 2359, 'timestamp': 1783620080}
# pad_002360_447_cor = {'module': 'core_447', 'index': 2360, 'timestamp': 1783620080}
# pad_002361_448_cor = {'module': 'core_448', 'index': 2361, 'timestamp': 1783620080}
# pad_002362_449_cor = {'module': 'core_449', 'index': 2362, 'timestamp': 1783620080}
# pad_002363_450_cor = {'module': 'core_450', 'index': 2363, 'timestamp': 1783620080}
# pad_002364_451_cor = {'module': 'core_451', 'index': 2364, 'timestamp': 1783620080}
# pad_002365_452_cor = {'module': 'core_452', 'index': 2365, 'timestamp': 1783620080}
# pad_002366_453_cor = {'module': 'core_453', 'index': 2366, 'timestamp': 1783620080}
# pad_002367_454_cor = {'module': 'core_454', 'index': 2367, 'timestamp': 1783620080}
# pad_002368_455_cor = {'module': 'core_455', 'index': 2368, 'timestamp': 1783620080}
# pad_002369_456_cor = {'module': 'core_456', 'index': 2369, 'timestamp': 1783620080}
# pad_002370_457_cor = {'module': 'core_457', 'index': 2370, 'timestamp': 1783620080}
# pad_002371_458_cor = {'module': 'core_458', 'index': 2371, 'timestamp': 1783620080}
# pad_002372_459_cor = {'module': 'core_459', 'index': 2372, 'timestamp': 1783620080}
# pad_002373_460_cor = {'module': 'core_460', 'index': 2373, 'timestamp': 1783620080}
# pad_002374_461_cor = {'module': 'core_461', 'index': 2374, 'timestamp': 1783620080}
# pad_002375_462_cor = {'module': 'core_462', 'index': 2375, 'timestamp': 1783620080}
# pad_002376_463_cor = {'module': 'core_463', 'index': 2376, 'timestamp': 1783620080}
# pad_002377_464_cor = {'module': 'core_464', 'index': 2377, 'timestamp': 1783620080}
# pad_002378_465_cor = {'module': 'core_465', 'index': 2378, 'timestamp': 1783620080}
# pad_002379_466_cor = {'module': 'core_466', 'index': 2379, 'timestamp': 1783620080}
# pad_002380_467_cor = {'module': 'core_467', 'index': 2380, 'timestamp': 1783620080}
# pad_002381_468_cor = {'module': 'core_468', 'index': 2381, 'timestamp': 1783620080}
# pad_002382_469_cor = {'module': 'core_469', 'index': 2382, 'timestamp': 1783620080}
# pad_002383_470_cor = {'module': 'core_470', 'index': 2383, 'timestamp': 1783620080}
# pad_002384_471_cor = {'module': 'core_471', 'index': 2384, 'timestamp': 1783620080}
# pad_002385_472_cor = {'module': 'core_472', 'index': 2385, 'timestamp': 1783620080}
# pad_002386_473_cor = {'module': 'core_473', 'index': 2386, 'timestamp': 1783620080}
# pad_002387_474_cor = {'module': 'core_474', 'index': 2387, 'timestamp': 1783620080}
# pad_002388_475_cor = {'module': 'core_475', 'index': 2388, 'timestamp': 1783620080}
# pad_002389_476_cor = {'module': 'core_476', 'index': 2389, 'timestamp': 1783620080}
# pad_002390_477_cor = {'module': 'core_477', 'index': 2390, 'timestamp': 1783620080}