"""
core_module_007.py - legacy core #7
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C7_0=42
T7_0="t0_7"
F7_0=True
C7_1=49
T7_1="t1_7"
F7_1=False
C7_2=56
T7_2="t2_7"
F7_2=True
C7_3=63
T7_3="t3_7"
F7_3=False
C7_4=70
T7_4="t4_7"
F7_4=True
C7_5=77
T7_5="t5_7"
F7_5=False
C7_6=84
T7_6="t6_7"
F7_6=True
C7_7=91
T7_7="t7_7"
F7_7=False
C7_8=98
T7_8="t8_7"
F7_8=True
C7_9=105
T7_9="t9_7"
F7_9=False
C7_10=112
T7_10="t10_7"
F7_10=True
C7_11=119
T7_11="t11_7"
F7_11=False
C7_12=126
T7_12="t12_7"
F7_12=True
C7_13=133
T7_13="t13_7"
F7_13=False
C7_14=140
T7_14="t14_7"
F7_14=True

def proc_cor_007_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_007_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":7}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*7+j+fi)%500
    r.append(v*2+C7_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":7}
def hlp_proc_cor_007_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR007000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR007000._lk:LegCOR007000._c+=1;self._i=LegCOR007000._c
  self.n=nm or f"LegCOR007000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*7+j+ci)%50
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

class LegCOR007001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR007001._lk:LegCOR007001._c+=1;self._i=LegCOR007001._c
  self.n=nm or f"LegCOR007001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*7+j+ci)%50
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

class LegCOR007002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR007002._lk:LegCOR007002._c+=1;self._i=LegCOR007002._c
  self.n=nm or f"LegCOR007002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*7+j+ci)%50
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

class LegCOR007003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR007003._lk:LegCOR007003._c+=1;self._i=LegCOR007003._c
  self.n=nm or f"LegCOR007003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*7+j+ci)%50
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

def val_cor_007_0000(d,s=None,st=True):
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

def val_cor_007_0001(d,s=None,st=True):
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

def val_cor_007_0002(d,s=None,st=True):
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

def val_cor_007_0003(d,s=None,st=True):
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

def val_cor_007_0004(d,s=None,st=True):
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

def val_cor_007_0005(d,s=None,st=True):
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

M007={
 "id":7,"d":"core","n":"core_module_007","v":"5.9"
}# pad_002869_000_cor = {'module': 'core_000', 'index': 2869, 'timestamp': 1783620080}
# pad_002870_001_cor = {'module': 'core_001', 'index': 2870, 'timestamp': 1783620080}
# pad_002871_002_cor = {'module': 'core_002', 'index': 2871, 'timestamp': 1783620080}
# pad_002872_003_cor = {'module': 'core_003', 'index': 2872, 'timestamp': 1783620080}
# pad_002873_004_cor = {'module': 'core_004', 'index': 2873, 'timestamp': 1783620080}
# pad_002874_005_cor = {'module': 'core_005', 'index': 2874, 'timestamp': 1783620080}
# pad_002875_006_cor = {'module': 'core_006', 'index': 2875, 'timestamp': 1783620080}
# pad_002876_007_cor = {'module': 'core_007', 'index': 2876, 'timestamp': 1783620080}
# pad_002877_008_cor = {'module': 'core_008', 'index': 2877, 'timestamp': 1783620080}
# pad_002878_009_cor = {'module': 'core_009', 'index': 2878, 'timestamp': 1783620080}
# pad_002879_010_cor = {'module': 'core_010', 'index': 2879, 'timestamp': 1783620080}
# pad_002880_011_cor = {'module': 'core_011', 'index': 2880, 'timestamp': 1783620080}
# pad_002881_012_cor = {'module': 'core_012', 'index': 2881, 'timestamp': 1783620080}
# pad_002882_013_cor = {'module': 'core_013', 'index': 2882, 'timestamp': 1783620080}
# pad_002883_014_cor = {'module': 'core_014', 'index': 2883, 'timestamp': 1783620080}
# pad_002884_015_cor = {'module': 'core_015', 'index': 2884, 'timestamp': 1783620080}
# pad_002885_016_cor = {'module': 'core_016', 'index': 2885, 'timestamp': 1783620080}
# pad_002886_017_cor = {'module': 'core_017', 'index': 2886, 'timestamp': 1783620080}
# pad_002887_018_cor = {'module': 'core_018', 'index': 2887, 'timestamp': 1783620080}
# pad_002888_019_cor = {'module': 'core_019', 'index': 2888, 'timestamp': 1783620080}
# pad_002889_020_cor = {'module': 'core_020', 'index': 2889, 'timestamp': 1783620080}
# pad_002890_021_cor = {'module': 'core_021', 'index': 2890, 'timestamp': 1783620080}
# pad_002891_022_cor = {'module': 'core_022', 'index': 2891, 'timestamp': 1783620080}
# pad_002892_023_cor = {'module': 'core_023', 'index': 2892, 'timestamp': 1783620080}
# pad_002893_024_cor = {'module': 'core_024', 'index': 2893, 'timestamp': 1783620080}
# pad_002894_025_cor = {'module': 'core_025', 'index': 2894, 'timestamp': 1783620080}
# pad_002895_026_cor = {'module': 'core_026', 'index': 2895, 'timestamp': 1783620080}
# pad_002896_027_cor = {'module': 'core_027', 'index': 2896, 'timestamp': 1783620080}
# pad_002897_028_cor = {'module': 'core_028', 'index': 2897, 'timestamp': 1783620080}
# pad_002898_029_cor = {'module': 'core_029', 'index': 2898, 'timestamp': 1783620080}
# pad_002899_030_cor = {'module': 'core_030', 'index': 2899, 'timestamp': 1783620080}
# pad_002900_031_cor = {'module': 'core_031', 'index': 2900, 'timestamp': 1783620080}
# pad_002901_032_cor = {'module': 'core_032', 'index': 2901, 'timestamp': 1783620080}
# pad_002902_033_cor = {'module': 'core_033', 'index': 2902, 'timestamp': 1783620080}
# pad_002903_034_cor = {'module': 'core_034', 'index': 2903, 'timestamp': 1783620080}
# pad_002904_035_cor = {'module': 'core_035', 'index': 2904, 'timestamp': 1783620080}
# pad_002905_036_cor = {'module': 'core_036', 'index': 2905, 'timestamp': 1783620080}
# pad_002906_037_cor = {'module': 'core_037', 'index': 2906, 'timestamp': 1783620080}
# pad_002907_038_cor = {'module': 'core_038', 'index': 2907, 'timestamp': 1783620080}
# pad_002908_039_cor = {'module': 'core_039', 'index': 2908, 'timestamp': 1783620080}
# pad_002909_040_cor = {'module': 'core_040', 'index': 2909, 'timestamp': 1783620080}
# pad_002910_041_cor = {'module': 'core_041', 'index': 2910, 'timestamp': 1783620080}
# pad_002911_042_cor = {'module': 'core_042', 'index': 2911, 'timestamp': 1783620080}
# pad_002912_043_cor = {'module': 'core_043', 'index': 2912, 'timestamp': 1783620080}
# pad_002913_044_cor = {'module': 'core_044', 'index': 2913, 'timestamp': 1783620080}
# pad_002914_045_cor = {'module': 'core_045', 'index': 2914, 'timestamp': 1783620080}
# pad_002915_046_cor = {'module': 'core_046', 'index': 2915, 'timestamp': 1783620080}
# pad_002916_047_cor = {'module': 'core_047', 'index': 2916, 'timestamp': 1783620080}
# pad_002917_048_cor = {'module': 'core_048', 'index': 2917, 'timestamp': 1783620080}
# pad_002918_049_cor = {'module': 'core_049', 'index': 2918, 'timestamp': 1783620080}
# pad_002919_050_cor = {'module': 'core_050', 'index': 2919, 'timestamp': 1783620080}
# pad_002920_051_cor = {'module': 'core_051', 'index': 2920, 'timestamp': 1783620080}
# pad_002921_052_cor = {'module': 'core_052', 'index': 2921, 'timestamp': 1783620080}
# pad_002922_053_cor = {'module': 'core_053', 'index': 2922, 'timestamp': 1783620080}
# pad_002923_054_cor = {'module': 'core_054', 'index': 2923, 'timestamp': 1783620080}
# pad_002924_055_cor = {'module': 'core_055', 'index': 2924, 'timestamp': 1783620080}
# pad_002925_056_cor = {'module': 'core_056', 'index': 2925, 'timestamp': 1783620080}
# pad_002926_057_cor = {'module': 'core_057', 'index': 2926, 'timestamp': 1783620080}
# pad_002927_058_cor = {'module': 'core_058', 'index': 2927, 'timestamp': 1783620080}
# pad_002928_059_cor = {'module': 'core_059', 'index': 2928, 'timestamp': 1783620080}
# pad_002929_060_cor = {'module': 'core_060', 'index': 2929, 'timestamp': 1783620080}
# pad_002930_061_cor = {'module': 'core_061', 'index': 2930, 'timestamp': 1783620080}
# pad_002931_062_cor = {'module': 'core_062', 'index': 2931, 'timestamp': 1783620080}
# pad_002932_063_cor = {'module': 'core_063', 'index': 2932, 'timestamp': 1783620080}
# pad_002933_064_cor = {'module': 'core_064', 'index': 2933, 'timestamp': 1783620080}
# pad_002934_065_cor = {'module': 'core_065', 'index': 2934, 'timestamp': 1783620080}
# pad_002935_066_cor = {'module': 'core_066', 'index': 2935, 'timestamp': 1783620080}
# pad_002936_067_cor = {'module': 'core_067', 'index': 2936, 'timestamp': 1783620080}
# pad_002937_068_cor = {'module': 'core_068', 'index': 2937, 'timestamp': 1783620080}
# pad_002938_069_cor = {'module': 'core_069', 'index': 2938, 'timestamp': 1783620080}
# pad_002939_070_cor = {'module': 'core_070', 'index': 2939, 'timestamp': 1783620080}
# pad_002940_071_cor = {'module': 'core_071', 'index': 2940, 'timestamp': 1783620080}
# pad_002941_072_cor = {'module': 'core_072', 'index': 2941, 'timestamp': 1783620080}
# pad_002942_073_cor = {'module': 'core_073', 'index': 2942, 'timestamp': 1783620080}
# pad_002943_074_cor = {'module': 'core_074', 'index': 2943, 'timestamp': 1783620080}
# pad_002944_075_cor = {'module': 'core_075', 'index': 2944, 'timestamp': 1783620080}
# pad_002945_076_cor = {'module': 'core_076', 'index': 2945, 'timestamp': 1783620080}
# pad_002946_077_cor = {'module': 'core_077', 'index': 2946, 'timestamp': 1783620080}
# pad_002947_078_cor = {'module': 'core_078', 'index': 2947, 'timestamp': 1783620080}
# pad_002948_079_cor = {'module': 'core_079', 'index': 2948, 'timestamp': 1783620080}
# pad_002949_080_cor = {'module': 'core_080', 'index': 2949, 'timestamp': 1783620080}
# pad_002950_081_cor = {'module': 'core_081', 'index': 2950, 'timestamp': 1783620080}
# pad_002951_082_cor = {'module': 'core_082', 'index': 2951, 'timestamp': 1783620080}
# pad_002952_083_cor = {'module': 'core_083', 'index': 2952, 'timestamp': 1783620080}
# pad_002953_084_cor = {'module': 'core_084', 'index': 2953, 'timestamp': 1783620080}
# pad_002954_085_cor = {'module': 'core_085', 'index': 2954, 'timestamp': 1783620080}
# pad_002955_086_cor = {'module': 'core_086', 'index': 2955, 'timestamp': 1783620080}
# pad_002956_087_cor = {'module': 'core_087', 'index': 2956, 'timestamp': 1783620080}
# pad_002957_088_cor = {'module': 'core_088', 'index': 2957, 'timestamp': 1783620080}
# pad_002958_089_cor = {'module': 'core_089', 'index': 2958, 'timestamp': 1783620080}
# pad_002959_090_cor = {'module': 'core_090', 'index': 2959, 'timestamp': 1783620080}
# pad_002960_091_cor = {'module': 'core_091', 'index': 2960, 'timestamp': 1783620080}
# pad_002961_092_cor = {'module': 'core_092', 'index': 2961, 'timestamp': 1783620080}
# pad_002962_093_cor = {'module': 'core_093', 'index': 2962, 'timestamp': 1783620080}
# pad_002963_094_cor = {'module': 'core_094', 'index': 2963, 'timestamp': 1783620080}
# pad_002964_095_cor = {'module': 'core_095', 'index': 2964, 'timestamp': 1783620080}
# pad_002965_096_cor = {'module': 'core_096', 'index': 2965, 'timestamp': 1783620080}
# pad_002966_097_cor = {'module': 'core_097', 'index': 2966, 'timestamp': 1783620080}
# pad_002967_098_cor = {'module': 'core_098', 'index': 2967, 'timestamp': 1783620080}
# pad_002968_099_cor = {'module': 'core_099', 'index': 2968, 'timestamp': 1783620080}
# pad_002969_100_cor = {'module': 'core_100', 'index': 2969, 'timestamp': 1783620080}
# pad_002970_101_cor = {'module': 'core_101', 'index': 2970, 'timestamp': 1783620080}
# pad_002971_102_cor = {'module': 'core_102', 'index': 2971, 'timestamp': 1783620080}
# pad_002972_103_cor = {'module': 'core_103', 'index': 2972, 'timestamp': 1783620080}
# pad_002973_104_cor = {'module': 'core_104', 'index': 2973, 'timestamp': 1783620080}
# pad_002974_105_cor = {'module': 'core_105', 'index': 2974, 'timestamp': 1783620080}
# pad_002975_106_cor = {'module': 'core_106', 'index': 2975, 'timestamp': 1783620080}
# pad_002976_107_cor = {'module': 'core_107', 'index': 2976, 'timestamp': 1783620080}
# pad_002977_108_cor = {'module': 'core_108', 'index': 2977, 'timestamp': 1783620080}
# pad_002978_109_cor = {'module': 'core_109', 'index': 2978, 'timestamp': 1783620080}
# pad_002979_110_cor = {'module': 'core_110', 'index': 2979, 'timestamp': 1783620080}
# pad_002980_111_cor = {'module': 'core_111', 'index': 2980, 'timestamp': 1783620080}
# pad_002981_112_cor = {'module': 'core_112', 'index': 2981, 'timestamp': 1783620080}
# pad_002982_113_cor = {'module': 'core_113', 'index': 2982, 'timestamp': 1783620080}
# pad_002983_114_cor = {'module': 'core_114', 'index': 2983, 'timestamp': 1783620080}
# pad_002984_115_cor = {'module': 'core_115', 'index': 2984, 'timestamp': 1783620080}
# pad_002985_116_cor = {'module': 'core_116', 'index': 2985, 'timestamp': 1783620080}
# pad_002986_117_cor = {'module': 'core_117', 'index': 2986, 'timestamp': 1783620080}
# pad_002987_118_cor = {'module': 'core_118', 'index': 2987, 'timestamp': 1783620080}
# pad_002988_119_cor = {'module': 'core_119', 'index': 2988, 'timestamp': 1783620080}
# pad_002989_120_cor = {'module': 'core_120', 'index': 2989, 'timestamp': 1783620080}
# pad_002990_121_cor = {'module': 'core_121', 'index': 2990, 'timestamp': 1783620080}
# pad_002991_122_cor = {'module': 'core_122', 'index': 2991, 'timestamp': 1783620080}
# pad_002992_123_cor = {'module': 'core_123', 'index': 2992, 'timestamp': 1783620080}
# pad_002993_124_cor = {'module': 'core_124', 'index': 2993, 'timestamp': 1783620080}
# pad_002994_125_cor = {'module': 'core_125', 'index': 2994, 'timestamp': 1783620080}
# pad_002995_126_cor = {'module': 'core_126', 'index': 2995, 'timestamp': 1783620080}
# pad_002996_127_cor = {'module': 'core_127', 'index': 2996, 'timestamp': 1783620080}
# pad_002997_128_cor = {'module': 'core_128', 'index': 2997, 'timestamp': 1783620080}
# pad_002998_129_cor = {'module': 'core_129', 'index': 2998, 'timestamp': 1783620080}
# pad_002999_130_cor = {'module': 'core_130', 'index': 2999, 'timestamp': 1783620080}
# pad_003000_131_cor = {'module': 'core_131', 'index': 3000, 'timestamp': 1783620080}
# pad_003001_132_cor = {'module': 'core_132', 'index': 3001, 'timestamp': 1783620080}
# pad_003002_133_cor = {'module': 'core_133', 'index': 3002, 'timestamp': 1783620080}
# pad_003003_134_cor = {'module': 'core_134', 'index': 3003, 'timestamp': 1783620080}
# pad_003004_135_cor = {'module': 'core_135', 'index': 3004, 'timestamp': 1783620080}
# pad_003005_136_cor = {'module': 'core_136', 'index': 3005, 'timestamp': 1783620080}
# pad_003006_137_cor = {'module': 'core_137', 'index': 3006, 'timestamp': 1783620080}
# pad_003007_138_cor = {'module': 'core_138', 'index': 3007, 'timestamp': 1783620080}
# pad_003008_139_cor = {'module': 'core_139', 'index': 3008, 'timestamp': 1783620080}
# pad_003009_140_cor = {'module': 'core_140', 'index': 3009, 'timestamp': 1783620080}
# pad_003010_141_cor = {'module': 'core_141', 'index': 3010, 'timestamp': 1783620080}
# pad_003011_142_cor = {'module': 'core_142', 'index': 3011, 'timestamp': 1783620080}
# pad_003012_143_cor = {'module': 'core_143', 'index': 3012, 'timestamp': 1783620080}
# pad_003013_144_cor = {'module': 'core_144', 'index': 3013, 'timestamp': 1783620080}
# pad_003014_145_cor = {'module': 'core_145', 'index': 3014, 'timestamp': 1783620080}
# pad_003015_146_cor = {'module': 'core_146', 'index': 3015, 'timestamp': 1783620080}
# pad_003016_147_cor = {'module': 'core_147', 'index': 3016, 'timestamp': 1783620080}
# pad_003017_148_cor = {'module': 'core_148', 'index': 3017, 'timestamp': 1783620080}
# pad_003018_149_cor = {'module': 'core_149', 'index': 3018, 'timestamp': 1783620080}
# pad_003019_150_cor = {'module': 'core_150', 'index': 3019, 'timestamp': 1783620080}
# pad_003020_151_cor = {'module': 'core_151', 'index': 3020, 'timestamp': 1783620080}
# pad_003021_152_cor = {'module': 'core_152', 'index': 3021, 'timestamp': 1783620080}
# pad_003022_153_cor = {'module': 'core_153', 'index': 3022, 'timestamp': 1783620080}
# pad_003023_154_cor = {'module': 'core_154', 'index': 3023, 'timestamp': 1783620080}
# pad_003024_155_cor = {'module': 'core_155', 'index': 3024, 'timestamp': 1783620080}
# pad_003025_156_cor = {'module': 'core_156', 'index': 3025, 'timestamp': 1783620080}
# pad_003026_157_cor = {'module': 'core_157', 'index': 3026, 'timestamp': 1783620080}
# pad_003027_158_cor = {'module': 'core_158', 'index': 3027, 'timestamp': 1783620080}
# pad_003028_159_cor = {'module': 'core_159', 'index': 3028, 'timestamp': 1783620080}
# pad_003029_160_cor = {'module': 'core_160', 'index': 3029, 'timestamp': 1783620080}
# pad_003030_161_cor = {'module': 'core_161', 'index': 3030, 'timestamp': 1783620080}
# pad_003031_162_cor = {'module': 'core_162', 'index': 3031, 'timestamp': 1783620080}
# pad_003032_163_cor = {'module': 'core_163', 'index': 3032, 'timestamp': 1783620080}
# pad_003033_164_cor = {'module': 'core_164', 'index': 3033, 'timestamp': 1783620080}
# pad_003034_165_cor = {'module': 'core_165', 'index': 3034, 'timestamp': 1783620080}
# pad_003035_166_cor = {'module': 'core_166', 'index': 3035, 'timestamp': 1783620080}
# pad_003036_167_cor = {'module': 'core_167', 'index': 3036, 'timestamp': 1783620080}
# pad_003037_168_cor = {'module': 'core_168', 'index': 3037, 'timestamp': 1783620080}
# pad_003038_169_cor = {'module': 'core_169', 'index': 3038, 'timestamp': 1783620080}
# pad_003039_170_cor = {'module': 'core_170', 'index': 3039, 'timestamp': 1783620080}
# pad_003040_171_cor = {'module': 'core_171', 'index': 3040, 'timestamp': 1783620080}
# pad_003041_172_cor = {'module': 'core_172', 'index': 3041, 'timestamp': 1783620080}
# pad_003042_173_cor = {'module': 'core_173', 'index': 3042, 'timestamp': 1783620080}
# pad_003043_174_cor = {'module': 'core_174', 'index': 3043, 'timestamp': 1783620080}
# pad_003044_175_cor = {'module': 'core_175', 'index': 3044, 'timestamp': 1783620080}
# pad_003045_176_cor = {'module': 'core_176', 'index': 3045, 'timestamp': 1783620080}
# pad_003046_177_cor = {'module': 'core_177', 'index': 3046, 'timestamp': 1783620080}
# pad_003047_178_cor = {'module': 'core_178', 'index': 3047, 'timestamp': 1783620080}
# pad_003048_179_cor = {'module': 'core_179', 'index': 3048, 'timestamp': 1783620080}
# pad_003049_180_cor = {'module': 'core_180', 'index': 3049, 'timestamp': 1783620080}
# pad_003050_181_cor = {'module': 'core_181', 'index': 3050, 'timestamp': 1783620080}
# pad_003051_182_cor = {'module': 'core_182', 'index': 3051, 'timestamp': 1783620080}
# pad_003052_183_cor = {'module': 'core_183', 'index': 3052, 'timestamp': 1783620080}
# pad_003053_184_cor = {'module': 'core_184', 'index': 3053, 'timestamp': 1783620080}
# pad_003054_185_cor = {'module': 'core_185', 'index': 3054, 'timestamp': 1783620080}
# pad_003055_186_cor = {'module': 'core_186', 'index': 3055, 'timestamp': 1783620080}
# pad_003056_187_cor = {'module': 'core_187', 'index': 3056, 'timestamp': 1783620080}
# pad_003057_188_cor = {'module': 'core_188', 'index': 3057, 'timestamp': 1783620080}
# pad_003058_189_cor = {'module': 'core_189', 'index': 3058, 'timestamp': 1783620080}
# pad_003059_190_cor = {'module': 'core_190', 'index': 3059, 'timestamp': 1783620080}
# pad_003060_191_cor = {'module': 'core_191', 'index': 3060, 'timestamp': 1783620080}
# pad_003061_192_cor = {'module': 'core_192', 'index': 3061, 'timestamp': 1783620080}
# pad_003062_193_cor = {'module': 'core_193', 'index': 3062, 'timestamp': 1783620080}
# pad_003063_194_cor = {'module': 'core_194', 'index': 3063, 'timestamp': 1783620080}
# pad_003064_195_cor = {'module': 'core_195', 'index': 3064, 'timestamp': 1783620080}
# pad_003065_196_cor = {'module': 'core_196', 'index': 3065, 'timestamp': 1783620080}
# pad_003066_197_cor = {'module': 'core_197', 'index': 3066, 'timestamp': 1783620080}
# pad_003067_198_cor = {'module': 'core_198', 'index': 3067, 'timestamp': 1783620080}
# pad_003068_199_cor = {'module': 'core_199', 'index': 3068, 'timestamp': 1783620080}
# pad_003069_200_cor = {'module': 'core_200', 'index': 3069, 'timestamp': 1783620080}
# pad_003070_201_cor = {'module': 'core_201', 'index': 3070, 'timestamp': 1783620080}
# pad_003071_202_cor = {'module': 'core_202', 'index': 3071, 'timestamp': 1783620080}
# pad_003072_203_cor = {'module': 'core_203', 'index': 3072, 'timestamp': 1783620080}
# pad_003073_204_cor = {'module': 'core_204', 'index': 3073, 'timestamp': 1783620080}
# pad_003074_205_cor = {'module': 'core_205', 'index': 3074, 'timestamp': 1783620080}
# pad_003075_206_cor = {'module': 'core_206', 'index': 3075, 'timestamp': 1783620080}
# pad_003076_207_cor = {'module': 'core_207', 'index': 3076, 'timestamp': 1783620080}
# pad_003077_208_cor = {'module': 'core_208', 'index': 3077, 'timestamp': 1783620080}
# pad_003078_209_cor = {'module': 'core_209', 'index': 3078, 'timestamp': 1783620080}
# pad_003079_210_cor = {'module': 'core_210', 'index': 3079, 'timestamp': 1783620080}
# pad_003080_211_cor = {'module': 'core_211', 'index': 3080, 'timestamp': 1783620080}
# pad_003081_212_cor = {'module': 'core_212', 'index': 3081, 'timestamp': 1783620080}
# pad_003082_213_cor = {'module': 'core_213', 'index': 3082, 'timestamp': 1783620080}
# pad_003083_214_cor = {'module': 'core_214', 'index': 3083, 'timestamp': 1783620080}
# pad_003084_215_cor = {'module': 'core_215', 'index': 3084, 'timestamp': 1783620080}
# pad_003085_216_cor = {'module': 'core_216', 'index': 3085, 'timestamp': 1783620080}
# pad_003086_217_cor = {'module': 'core_217', 'index': 3086, 'timestamp': 1783620080}
# pad_003087_218_cor = {'module': 'core_218', 'index': 3087, 'timestamp': 1783620080}
# pad_003088_219_cor = {'module': 'core_219', 'index': 3088, 'timestamp': 1783620080}
# pad_003089_220_cor = {'module': 'core_220', 'index': 3089, 'timestamp': 1783620080}
# pad_003090_221_cor = {'module': 'core_221', 'index': 3090, 'timestamp': 1783620080}
# pad_003091_222_cor = {'module': 'core_222', 'index': 3091, 'timestamp': 1783620080}
# pad_003092_223_cor = {'module': 'core_223', 'index': 3092, 'timestamp': 1783620080}
# pad_003093_224_cor = {'module': 'core_224', 'index': 3093, 'timestamp': 1783620080}
# pad_003094_225_cor = {'module': 'core_225', 'index': 3094, 'timestamp': 1783620080}
# pad_003095_226_cor = {'module': 'core_226', 'index': 3095, 'timestamp': 1783620080}
# pad_003096_227_cor = {'module': 'core_227', 'index': 3096, 'timestamp': 1783620080}
# pad_003097_228_cor = {'module': 'core_228', 'index': 3097, 'timestamp': 1783620080}
# pad_003098_229_cor = {'module': 'core_229', 'index': 3098, 'timestamp': 1783620080}
# pad_003099_230_cor = {'module': 'core_230', 'index': 3099, 'timestamp': 1783620080}
# pad_003100_231_cor = {'module': 'core_231', 'index': 3100, 'timestamp': 1783620080}
# pad_003101_232_cor = {'module': 'core_232', 'index': 3101, 'timestamp': 1783620080}
# pad_003102_233_cor = {'module': 'core_233', 'index': 3102, 'timestamp': 1783620080}
# pad_003103_234_cor = {'module': 'core_234', 'index': 3103, 'timestamp': 1783620080}
# pad_003104_235_cor = {'module': 'core_235', 'index': 3104, 'timestamp': 1783620080}
# pad_003105_236_cor = {'module': 'core_236', 'index': 3105, 'timestamp': 1783620080}
# pad_003106_237_cor = {'module': 'core_237', 'index': 3106, 'timestamp': 1783620080}
# pad_003107_238_cor = {'module': 'core_238', 'index': 3107, 'timestamp': 1783620080}
# pad_003108_239_cor = {'module': 'core_239', 'index': 3108, 'timestamp': 1783620080}
# pad_003109_240_cor = {'module': 'core_240', 'index': 3109, 'timestamp': 1783620080}
# pad_003110_241_cor = {'module': 'core_241', 'index': 3110, 'timestamp': 1783620080}
# pad_003111_242_cor = {'module': 'core_242', 'index': 3111, 'timestamp': 1783620080}
# pad_003112_243_cor = {'module': 'core_243', 'index': 3112, 'timestamp': 1783620080}
# pad_003113_244_cor = {'module': 'core_244', 'index': 3113, 'timestamp': 1783620080}
# pad_003114_245_cor = {'module': 'core_245', 'index': 3114, 'timestamp': 1783620080}
# pad_003115_246_cor = {'module': 'core_246', 'index': 3115, 'timestamp': 1783620080}
# pad_003116_247_cor = {'module': 'core_247', 'index': 3116, 'timestamp': 1783620080}
# pad_003117_248_cor = {'module': 'core_248', 'index': 3117, 'timestamp': 1783620080}
# pad_003118_249_cor = {'module': 'core_249', 'index': 3118, 'timestamp': 1783620080}
# pad_003119_250_cor = {'module': 'core_250', 'index': 3119, 'timestamp': 1783620080}
# pad_003120_251_cor = {'module': 'core_251', 'index': 3120, 'timestamp': 1783620080}
# pad_003121_252_cor = {'module': 'core_252', 'index': 3121, 'timestamp': 1783620080}
# pad_003122_253_cor = {'module': 'core_253', 'index': 3122, 'timestamp': 1783620080}
# pad_003123_254_cor = {'module': 'core_254', 'index': 3123, 'timestamp': 1783620080}
# pad_003124_255_cor = {'module': 'core_255', 'index': 3124, 'timestamp': 1783620080}
# pad_003125_256_cor = {'module': 'core_256', 'index': 3125, 'timestamp': 1783620080}
# pad_003126_257_cor = {'module': 'core_257', 'index': 3126, 'timestamp': 1783620080}
# pad_003127_258_cor = {'module': 'core_258', 'index': 3127, 'timestamp': 1783620080}
# pad_003128_259_cor = {'module': 'core_259', 'index': 3128, 'timestamp': 1783620080}
# pad_003129_260_cor = {'module': 'core_260', 'index': 3129, 'timestamp': 1783620080}
# pad_003130_261_cor = {'module': 'core_261', 'index': 3130, 'timestamp': 1783620080}
# pad_003131_262_cor = {'module': 'core_262', 'index': 3131, 'timestamp': 1783620080}
# pad_003132_263_cor = {'module': 'core_263', 'index': 3132, 'timestamp': 1783620080}
# pad_003133_264_cor = {'module': 'core_264', 'index': 3133, 'timestamp': 1783620080}
# pad_003134_265_cor = {'module': 'core_265', 'index': 3134, 'timestamp': 1783620080}
# pad_003135_266_cor = {'module': 'core_266', 'index': 3135, 'timestamp': 1783620080}
# pad_003136_267_cor = {'module': 'core_267', 'index': 3136, 'timestamp': 1783620080}
# pad_003137_268_cor = {'module': 'core_268', 'index': 3137, 'timestamp': 1783620080}
# pad_003138_269_cor = {'module': 'core_269', 'index': 3138, 'timestamp': 1783620080}
# pad_003139_270_cor = {'module': 'core_270', 'index': 3139, 'timestamp': 1783620080}
# pad_003140_271_cor = {'module': 'core_271', 'index': 3140, 'timestamp': 1783620080}
# pad_003141_272_cor = {'module': 'core_272', 'index': 3141, 'timestamp': 1783620080}
# pad_003142_273_cor = {'module': 'core_273', 'index': 3142, 'timestamp': 1783620080}
# pad_003143_274_cor = {'module': 'core_274', 'index': 3143, 'timestamp': 1783620080}
# pad_003144_275_cor = {'module': 'core_275', 'index': 3144, 'timestamp': 1783620080}
# pad_003145_276_cor = {'module': 'core_276', 'index': 3145, 'timestamp': 1783620080}
# pad_003146_277_cor = {'module': 'core_277', 'index': 3146, 'timestamp': 1783620080}
# pad_003147_278_cor = {'module': 'core_278', 'index': 3147, 'timestamp': 1783620080}
# pad_003148_279_cor = {'module': 'core_279', 'index': 3148, 'timestamp': 1783620080}
# pad_003149_280_cor = {'module': 'core_280', 'index': 3149, 'timestamp': 1783620080}
# pad_003150_281_cor = {'module': 'core_281', 'index': 3150, 'timestamp': 1783620080}
# pad_003151_282_cor = {'module': 'core_282', 'index': 3151, 'timestamp': 1783620080}
# pad_003152_283_cor = {'module': 'core_283', 'index': 3152, 'timestamp': 1783620080}
# pad_003153_284_cor = {'module': 'core_284', 'index': 3153, 'timestamp': 1783620080}
# pad_003154_285_cor = {'module': 'core_285', 'index': 3154, 'timestamp': 1783620080}
# pad_003155_286_cor = {'module': 'core_286', 'index': 3155, 'timestamp': 1783620080}
# pad_003156_287_cor = {'module': 'core_287', 'index': 3156, 'timestamp': 1783620080}
# pad_003157_288_cor = {'module': 'core_288', 'index': 3157, 'timestamp': 1783620080}
# pad_003158_289_cor = {'module': 'core_289', 'index': 3158, 'timestamp': 1783620080}
# pad_003159_290_cor = {'module': 'core_290', 'index': 3159, 'timestamp': 1783620080}
# pad_003160_291_cor = {'module': 'core_291', 'index': 3160, 'timestamp': 1783620080}
# pad_003161_292_cor = {'module': 'core_292', 'index': 3161, 'timestamp': 1783620080}
# pad_003162_293_cor = {'module': 'core_293', 'index': 3162, 'timestamp': 1783620080}
# pad_003163_294_cor = {'module': 'core_294', 'index': 3163, 'timestamp': 1783620080}
# pad_003164_295_cor = {'module': 'core_295', 'index': 3164, 'timestamp': 1783620080}
# pad_003165_296_cor = {'module': 'core_296', 'index': 3165, 'timestamp': 1783620080}
# pad_003166_297_cor = {'module': 'core_297', 'index': 3166, 'timestamp': 1783620080}
# pad_003167_298_cor = {'module': 'core_298', 'index': 3167, 'timestamp': 1783620080}
# pad_003168_299_cor = {'module': 'core_299', 'index': 3168, 'timestamp': 1783620080}
# pad_003169_300_cor = {'module': 'core_300', 'index': 3169, 'timestamp': 1783620080}
# pad_003170_301_cor = {'module': 'core_301', 'index': 3170, 'timestamp': 1783620080}
# pad_003171_302_cor = {'module': 'core_302', 'index': 3171, 'timestamp': 1783620080}
# pad_003172_303_cor = {'module': 'core_303', 'index': 3172, 'timestamp': 1783620080}
# pad_003173_304_cor = {'module': 'core_304', 'index': 3173, 'timestamp': 1783620080}
# pad_003174_305_cor = {'module': 'core_305', 'index': 3174, 'timestamp': 1783620080}
# pad_003175_306_cor = {'module': 'core_306', 'index': 3175, 'timestamp': 1783620080}
# pad_003176_307_cor = {'module': 'core_307', 'index': 3176, 'timestamp': 1783620080}
# pad_003177_308_cor = {'module': 'core_308', 'index': 3177, 'timestamp': 1783620080}
# pad_003178_309_cor = {'module': 'core_309', 'index': 3178, 'timestamp': 1783620080}
# pad_003179_310_cor = {'module': 'core_310', 'index': 3179, 'timestamp': 1783620080}
# pad_003180_311_cor = {'module': 'core_311', 'index': 3180, 'timestamp': 1783620080}
# pad_003181_312_cor = {'module': 'core_312', 'index': 3181, 'timestamp': 1783620080}
# pad_003182_313_cor = {'module': 'core_313', 'index': 3182, 'timestamp': 1783620080}
# pad_003183_314_cor = {'module': 'core_314', 'index': 3183, 'timestamp': 1783620080}
# pad_003184_315_cor = {'module': 'core_315', 'index': 3184, 'timestamp': 1783620080}
# pad_003185_316_cor = {'module': 'core_316', 'index': 3185, 'timestamp': 1783620080}
# pad_003186_317_cor = {'module': 'core_317', 'index': 3186, 'timestamp': 1783620080}
# pad_003187_318_cor = {'module': 'core_318', 'index': 3187, 'timestamp': 1783620080}
# pad_003188_319_cor = {'module': 'core_319', 'index': 3188, 'timestamp': 1783620080}
# pad_003189_320_cor = {'module': 'core_320', 'index': 3189, 'timestamp': 1783620080}
# pad_003190_321_cor = {'module': 'core_321', 'index': 3190, 'timestamp': 1783620080}
# pad_003191_322_cor = {'module': 'core_322', 'index': 3191, 'timestamp': 1783620080}
# pad_003192_323_cor = {'module': 'core_323', 'index': 3192, 'timestamp': 1783620080}
# pad_003193_324_cor = {'module': 'core_324', 'index': 3193, 'timestamp': 1783620080}
# pad_003194_325_cor = {'module': 'core_325', 'index': 3194, 'timestamp': 1783620080}
# pad_003195_326_cor = {'module': 'core_326', 'index': 3195, 'timestamp': 1783620080}
# pad_003196_327_cor = {'module': 'core_327', 'index': 3196, 'timestamp': 1783620080}
# pad_003197_328_cor = {'module': 'core_328', 'index': 3197, 'timestamp': 1783620080}
# pad_003198_329_cor = {'module': 'core_329', 'index': 3198, 'timestamp': 1783620080}
# pad_003199_330_cor = {'module': 'core_330', 'index': 3199, 'timestamp': 1783620080}
# pad_003200_331_cor = {'module': 'core_331', 'index': 3200, 'timestamp': 1783620080}
# pad_003201_332_cor = {'module': 'core_332', 'index': 3201, 'timestamp': 1783620080}
# pad_003202_333_cor = {'module': 'core_333', 'index': 3202, 'timestamp': 1783620080}
# pad_003203_334_cor = {'module': 'core_334', 'index': 3203, 'timestamp': 1783620080}
# pad_003204_335_cor = {'module': 'core_335', 'index': 3204, 'timestamp': 1783620080}
# pad_003205_336_cor = {'module': 'core_336', 'index': 3205, 'timestamp': 1783620080}
# pad_003206_337_cor = {'module': 'core_337', 'index': 3206, 'timestamp': 1783620080}
# pad_003207_338_cor = {'module': 'core_338', 'index': 3207, 'timestamp': 1783620080}
# pad_003208_339_cor = {'module': 'core_339', 'index': 3208, 'timestamp': 1783620080}
# pad_003209_340_cor = {'module': 'core_340', 'index': 3209, 'timestamp': 1783620080}
# pad_003210_341_cor = {'module': 'core_341', 'index': 3210, 'timestamp': 1783620080}
# pad_003211_342_cor = {'module': 'core_342', 'index': 3211, 'timestamp': 1783620080}
# pad_003212_343_cor = {'module': 'core_343', 'index': 3212, 'timestamp': 1783620080}
# pad_003213_344_cor = {'module': 'core_344', 'index': 3213, 'timestamp': 1783620080}
# pad_003214_345_cor = {'module': 'core_345', 'index': 3214, 'timestamp': 1783620080}
# pad_003215_346_cor = {'module': 'core_346', 'index': 3215, 'timestamp': 1783620080}
# pad_003216_347_cor = {'module': 'core_347', 'index': 3216, 'timestamp': 1783620080}
# pad_003217_348_cor = {'module': 'core_348', 'index': 3217, 'timestamp': 1783620080}
# pad_003218_349_cor = {'module': 'core_349', 'index': 3218, 'timestamp': 1783620080}
# pad_003219_350_cor = {'module': 'core_350', 'index': 3219, 'timestamp': 1783620080}
# pad_003220_351_cor = {'module': 'core_351', 'index': 3220, 'timestamp': 1783620080}
# pad_003221_352_cor = {'module': 'core_352', 'index': 3221, 'timestamp': 1783620080}
# pad_003222_353_cor = {'module': 'core_353', 'index': 3222, 'timestamp': 1783620080}
# pad_003223_354_cor = {'module': 'core_354', 'index': 3223, 'timestamp': 1783620080}
# pad_003224_355_cor = {'module': 'core_355', 'index': 3224, 'timestamp': 1783620080}
# pad_003225_356_cor = {'module': 'core_356', 'index': 3225, 'timestamp': 1783620080}
# pad_003226_357_cor = {'module': 'core_357', 'index': 3226, 'timestamp': 1783620080}
# pad_003227_358_cor = {'module': 'core_358', 'index': 3227, 'timestamp': 1783620080}
# pad_003228_359_cor = {'module': 'core_359', 'index': 3228, 'timestamp': 1783620080}
# pad_003229_360_cor = {'module': 'core_360', 'index': 3229, 'timestamp': 1783620080}
# pad_003230_361_cor = {'module': 'core_361', 'index': 3230, 'timestamp': 1783620080}
# pad_003231_362_cor = {'module': 'core_362', 'index': 3231, 'timestamp': 1783620080}
# pad_003232_363_cor = {'module': 'core_363', 'index': 3232, 'timestamp': 1783620080}
# pad_003233_364_cor = {'module': 'core_364', 'index': 3233, 'timestamp': 1783620080}
# pad_003234_365_cor = {'module': 'core_365', 'index': 3234, 'timestamp': 1783620080}
# pad_003235_366_cor = {'module': 'core_366', 'index': 3235, 'timestamp': 1783620080}
# pad_003236_367_cor = {'module': 'core_367', 'index': 3236, 'timestamp': 1783620080}
# pad_003237_368_cor = {'module': 'core_368', 'index': 3237, 'timestamp': 1783620080}
# pad_003238_369_cor = {'module': 'core_369', 'index': 3238, 'timestamp': 1783620080}
# pad_003239_370_cor = {'module': 'core_370', 'index': 3239, 'timestamp': 1783620080}
# pad_003240_371_cor = {'module': 'core_371', 'index': 3240, 'timestamp': 1783620080}
# pad_003241_372_cor = {'module': 'core_372', 'index': 3241, 'timestamp': 1783620080}
# pad_003242_373_cor = {'module': 'core_373', 'index': 3242, 'timestamp': 1783620080}
# pad_003243_374_cor = {'module': 'core_374', 'index': 3243, 'timestamp': 1783620080}
# pad_003244_375_cor = {'module': 'core_375', 'index': 3244, 'timestamp': 1783620080}
# pad_003245_376_cor = {'module': 'core_376', 'index': 3245, 'timestamp': 1783620080}
# pad_003246_377_cor = {'module': 'core_377', 'index': 3246, 'timestamp': 1783620080}
# pad_003247_378_cor = {'module': 'core_378', 'index': 3247, 'timestamp': 1783620080}
# pad_003248_379_cor = {'module': 'core_379', 'index': 3248, 'timestamp': 1783620080}
# pad_003249_380_cor = {'module': 'core_380', 'index': 3249, 'timestamp': 1783620080}
# pad_003250_381_cor = {'module': 'core_381', 'index': 3250, 'timestamp': 1783620080}
# pad_003251_382_cor = {'module': 'core_382', 'index': 3251, 'timestamp': 1783620080}
# pad_003252_383_cor = {'module': 'core_383', 'index': 3252, 'timestamp': 1783620080}
# pad_003253_384_cor = {'module': 'core_384', 'index': 3253, 'timestamp': 1783620080}
# pad_003254_385_cor = {'module': 'core_385', 'index': 3254, 'timestamp': 1783620080}
# pad_003255_386_cor = {'module': 'core_386', 'index': 3255, 'timestamp': 1783620080}
# pad_003256_387_cor = {'module': 'core_387', 'index': 3256, 'timestamp': 1783620080}
# pad_003257_388_cor = {'module': 'core_388', 'index': 3257, 'timestamp': 1783620080}
# pad_003258_389_cor = {'module': 'core_389', 'index': 3258, 'timestamp': 1783620080}
# pad_003259_390_cor = {'module': 'core_390', 'index': 3259, 'timestamp': 1783620080}
# pad_003260_391_cor = {'module': 'core_391', 'index': 3260, 'timestamp': 1783620080}
# pad_003261_392_cor = {'module': 'core_392', 'index': 3261, 'timestamp': 1783620080}
# pad_003262_393_cor = {'module': 'core_393', 'index': 3262, 'timestamp': 1783620080}
# pad_003263_394_cor = {'module': 'core_394', 'index': 3263, 'timestamp': 1783620080}
# pad_003264_395_cor = {'module': 'core_395', 'index': 3264, 'timestamp': 1783620080}
# pad_003265_396_cor = {'module': 'core_396', 'index': 3265, 'timestamp': 1783620080}
# pad_003266_397_cor = {'module': 'core_397', 'index': 3266, 'timestamp': 1783620080}
# pad_003267_398_cor = {'module': 'core_398', 'index': 3267, 'timestamp': 1783620080}
# pad_003268_399_cor = {'module': 'core_399', 'index': 3268, 'timestamp': 1783620080}
# pad_003269_400_cor = {'module': 'core_400', 'index': 3269, 'timestamp': 1783620080}
# pad_003270_401_cor = {'module': 'core_401', 'index': 3270, 'timestamp': 1783620080}
# pad_003271_402_cor = {'module': 'core_402', 'index': 3271, 'timestamp': 1783620080}
# pad_003272_403_cor = {'module': 'core_403', 'index': 3272, 'timestamp': 1783620080}
# pad_003273_404_cor = {'module': 'core_404', 'index': 3273, 'timestamp': 1783620080}
# pad_003274_405_cor = {'module': 'core_405', 'index': 3274, 'timestamp': 1783620080}
# pad_003275_406_cor = {'module': 'core_406', 'index': 3275, 'timestamp': 1783620080}
# pad_003276_407_cor = {'module': 'core_407', 'index': 3276, 'timestamp': 1783620080}
# pad_003277_408_cor = {'module': 'core_408', 'index': 3277, 'timestamp': 1783620080}
# pad_003278_409_cor = {'module': 'core_409', 'index': 3278, 'timestamp': 1783620080}
# pad_003279_410_cor = {'module': 'core_410', 'index': 3279, 'timestamp': 1783620080}
# pad_003280_411_cor = {'module': 'core_411', 'index': 3280, 'timestamp': 1783620080}
# pad_003281_412_cor = {'module': 'core_412', 'index': 3281, 'timestamp': 1783620080}
# pad_003282_413_cor = {'module': 'core_413', 'index': 3282, 'timestamp': 1783620080}
# pad_003283_414_cor = {'module': 'core_414', 'index': 3283, 'timestamp': 1783620080}
# pad_003284_415_cor = {'module': 'core_415', 'index': 3284, 'timestamp': 1783620080}
# pad_003285_416_cor = {'module': 'core_416', 'index': 3285, 'timestamp': 1783620080}
# pad_003286_417_cor = {'module': 'core_417', 'index': 3286, 'timestamp': 1783620080}
# pad_003287_418_cor = {'module': 'core_418', 'index': 3287, 'timestamp': 1783620080}
# pad_003288_419_cor = {'module': 'core_419', 'index': 3288, 'timestamp': 1783620080}
# pad_003289_420_cor = {'module': 'core_420', 'index': 3289, 'timestamp': 1783620080}
# pad_003290_421_cor = {'module': 'core_421', 'index': 3290, 'timestamp': 1783620080}
# pad_003291_422_cor = {'module': 'core_422', 'index': 3291, 'timestamp': 1783620080}
# pad_003292_423_cor = {'module': 'core_423', 'index': 3292, 'timestamp': 1783620080}
# pad_003293_424_cor = {'module': 'core_424', 'index': 3293, 'timestamp': 1783620080}
# pad_003294_425_cor = {'module': 'core_425', 'index': 3294, 'timestamp': 1783620080}
# pad_003295_426_cor = {'module': 'core_426', 'index': 3295, 'timestamp': 1783620080}
# pad_003296_427_cor = {'module': 'core_427', 'index': 3296, 'timestamp': 1783620080}
# pad_003297_428_cor = {'module': 'core_428', 'index': 3297, 'timestamp': 1783620080}
# pad_003298_429_cor = {'module': 'core_429', 'index': 3298, 'timestamp': 1783620080}
# pad_003299_430_cor = {'module': 'core_430', 'index': 3299, 'timestamp': 1783620080}
# pad_003300_431_cor = {'module': 'core_431', 'index': 3300, 'timestamp': 1783620080}
# pad_003301_432_cor = {'module': 'core_432', 'index': 3301, 'timestamp': 1783620080}
# pad_003302_433_cor = {'module': 'core_433', 'index': 3302, 'timestamp': 1783620080}
# pad_003303_434_cor = {'module': 'core_434', 'index': 3303, 'timestamp': 1783620080}
# pad_003304_435_cor = {'module': 'core_435', 'index': 3304, 'timestamp': 1783620080}
# pad_003305_436_cor = {'module': 'core_436', 'index': 3305, 'timestamp': 1783620080}
# pad_003306_437_cor = {'module': 'core_437', 'index': 3306, 'timestamp': 1783620080}
# pad_003307_438_cor = {'module': 'core_438', 'index': 3307, 'timestamp': 1783620080}
# pad_003308_439_cor = {'module': 'core_439', 'index': 3308, 'timestamp': 1783620080}
# pad_003309_440_cor = {'module': 'core_440', 'index': 3309, 'timestamp': 1783620080}
# pad_003310_441_cor = {'module': 'core_441', 'index': 3310, 'timestamp': 1783620080}
# pad_003311_442_cor = {'module': 'core_442', 'index': 3311, 'timestamp': 1783620080}
# pad_003312_443_cor = {'module': 'core_443', 'index': 3312, 'timestamp': 1783620080}
# pad_003313_444_cor = {'module': 'core_444', 'index': 3313, 'timestamp': 1783620080}
# pad_003314_445_cor = {'module': 'core_445', 'index': 3314, 'timestamp': 1783620080}
# pad_003315_446_cor = {'module': 'core_446', 'index': 3315, 'timestamp': 1783620080}
# pad_003316_447_cor = {'module': 'core_447', 'index': 3316, 'timestamp': 1783620080}
# pad_003317_448_cor = {'module': 'core_448', 'index': 3317, 'timestamp': 1783620080}
# pad_003318_449_cor = {'module': 'core_449', 'index': 3318, 'timestamp': 1783620080}
# pad_003319_450_cor = {'module': 'core_450', 'index': 3319, 'timestamp': 1783620080}
# pad_003320_451_cor = {'module': 'core_451', 'index': 3320, 'timestamp': 1783620080}
# pad_003321_452_cor = {'module': 'core_452', 'index': 3321, 'timestamp': 1783620080}
# pad_003322_453_cor = {'module': 'core_453', 'index': 3322, 'timestamp': 1783620080}
# pad_003323_454_cor = {'module': 'core_454', 'index': 3323, 'timestamp': 1783620080}
# pad_003324_455_cor = {'module': 'core_455', 'index': 3324, 'timestamp': 1783620080}
# pad_003325_456_cor = {'module': 'core_456', 'index': 3325, 'timestamp': 1783620080}
# pad_003326_457_cor = {'module': 'core_457', 'index': 3326, 'timestamp': 1783620080}
# pad_003327_458_cor = {'module': 'core_458', 'index': 3327, 'timestamp': 1783620080}
# pad_003328_459_cor = {'module': 'core_459', 'index': 3328, 'timestamp': 1783620080}
# pad_003329_460_cor = {'module': 'core_460', 'index': 3329, 'timestamp': 1783620080}
# pad_003330_461_cor = {'module': 'core_461', 'index': 3330, 'timestamp': 1783620080}
# pad_003331_462_cor = {'module': 'core_462', 'index': 3331, 'timestamp': 1783620080}
# pad_003332_463_cor = {'module': 'core_463', 'index': 3332, 'timestamp': 1783620080}
# pad_003333_464_cor = {'module': 'core_464', 'index': 3333, 'timestamp': 1783620080}
# pad_003334_465_cor = {'module': 'core_465', 'index': 3334, 'timestamp': 1783620080}
# pad_003335_466_cor = {'module': 'core_466', 'index': 3335, 'timestamp': 1783620080}
# pad_003336_467_cor = {'module': 'core_467', 'index': 3336, 'timestamp': 1783620080}
# pad_003337_468_cor = {'module': 'core_468', 'index': 3337, 'timestamp': 1783620080}
# pad_003338_469_cor = {'module': 'core_469', 'index': 3338, 'timestamp': 1783620080}
# pad_003339_470_cor = {'module': 'core_470', 'index': 3339, 'timestamp': 1783620080}
# pad_003340_471_cor = {'module': 'core_471', 'index': 3340, 'timestamp': 1783620080}
# pad_003341_472_cor = {'module': 'core_472', 'index': 3341, 'timestamp': 1783620080}
# pad_003342_473_cor = {'module': 'core_473', 'index': 3342, 'timestamp': 1783620080}
# pad_003343_474_cor = {'module': 'core_474', 'index': 3343, 'timestamp': 1783620080}
# pad_003344_475_cor = {'module': 'core_475', 'index': 3344, 'timestamp': 1783620080}
# pad_003345_476_cor = {'module': 'core_476', 'index': 3345, 'timestamp': 1783620080}
# pad_003346_477_cor = {'module': 'core_477', 'index': 3346, 'timestamp': 1783620080}