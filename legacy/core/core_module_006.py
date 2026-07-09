"""
core_module_006.py - legacy core #6
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C6_0=42
T6_0="t0_6"
F6_0=True
C6_1=49
T6_1="t1_6"
F6_1=False
C6_2=56
T6_2="t2_6"
F6_2=True
C6_3=63
T6_3="t3_6"
F6_3=False
C6_4=70
T6_4="t4_6"
F6_4=True
C6_5=77
T6_5="t5_6"
F6_5=False
C6_6=84
T6_6="t6_6"
F6_6=True
C6_7=91
T6_7="t7_6"
F6_7=False
C6_8=98
T6_8="t8_6"
F6_8=True
C6_9=105
T6_9="t9_6"
F6_9=False
C6_10=112
T6_10="t10_6"
F6_10=True
C6_11=119
T6_11="t11_6"
F6_11=False
C6_12=126
T6_12="t12_6"
F6_12=True
C6_13=133
T6_13="t13_6"
F6_13=False
C6_14=140
T6_14="t14_6"
F6_14=True

def proc_cor_006_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_006_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":6}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*6+j+fi)%500
    r.append(v*2+C6_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":6}
def hlp_proc_cor_006_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR006000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR006000._lk:LegCOR006000._c+=1;self._i=LegCOR006000._c
  self.n=nm or f"LegCOR006000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*6+j+ci)%50
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

class LegCOR006001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR006001._lk:LegCOR006001._c+=1;self._i=LegCOR006001._c
  self.n=nm or f"LegCOR006001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*6+j+ci)%50
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

class LegCOR006002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR006002._lk:LegCOR006002._c+=1;self._i=LegCOR006002._c
  self.n=nm or f"LegCOR006002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*6+j+ci)%50
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

class LegCOR006003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR006003._lk:LegCOR006003._c+=1;self._i=LegCOR006003._c
  self.n=nm or f"LegCOR006003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*6+j+ci)%50
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

def val_cor_006_0000(d,s=None,st=True):
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

def val_cor_006_0001(d,s=None,st=True):
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

def val_cor_006_0002(d,s=None,st=True):
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

def val_cor_006_0003(d,s=None,st=True):
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

def val_cor_006_0004(d,s=None,st=True):
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

def val_cor_006_0005(d,s=None,st=True):
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

M006={
 "id":6,"d":"core","n":"core_module_006","v":"3.1"
}# pad_002391_000_cor = {'module': 'core_000', 'index': 2391, 'timestamp': 1783620080}
# pad_002392_001_cor = {'module': 'core_001', 'index': 2392, 'timestamp': 1783620080}
# pad_002393_002_cor = {'module': 'core_002', 'index': 2393, 'timestamp': 1783620080}
# pad_002394_003_cor = {'module': 'core_003', 'index': 2394, 'timestamp': 1783620080}
# pad_002395_004_cor = {'module': 'core_004', 'index': 2395, 'timestamp': 1783620080}
# pad_002396_005_cor = {'module': 'core_005', 'index': 2396, 'timestamp': 1783620080}
# pad_002397_006_cor = {'module': 'core_006', 'index': 2397, 'timestamp': 1783620080}
# pad_002398_007_cor = {'module': 'core_007', 'index': 2398, 'timestamp': 1783620080}
# pad_002399_008_cor = {'module': 'core_008', 'index': 2399, 'timestamp': 1783620080}
# pad_002400_009_cor = {'module': 'core_009', 'index': 2400, 'timestamp': 1783620080}
# pad_002401_010_cor = {'module': 'core_010', 'index': 2401, 'timestamp': 1783620080}
# pad_002402_011_cor = {'module': 'core_011', 'index': 2402, 'timestamp': 1783620080}
# pad_002403_012_cor = {'module': 'core_012', 'index': 2403, 'timestamp': 1783620080}
# pad_002404_013_cor = {'module': 'core_013', 'index': 2404, 'timestamp': 1783620080}
# pad_002405_014_cor = {'module': 'core_014', 'index': 2405, 'timestamp': 1783620080}
# pad_002406_015_cor = {'module': 'core_015', 'index': 2406, 'timestamp': 1783620080}
# pad_002407_016_cor = {'module': 'core_016', 'index': 2407, 'timestamp': 1783620080}
# pad_002408_017_cor = {'module': 'core_017', 'index': 2408, 'timestamp': 1783620080}
# pad_002409_018_cor = {'module': 'core_018', 'index': 2409, 'timestamp': 1783620080}
# pad_002410_019_cor = {'module': 'core_019', 'index': 2410, 'timestamp': 1783620080}
# pad_002411_020_cor = {'module': 'core_020', 'index': 2411, 'timestamp': 1783620080}
# pad_002412_021_cor = {'module': 'core_021', 'index': 2412, 'timestamp': 1783620080}
# pad_002413_022_cor = {'module': 'core_022', 'index': 2413, 'timestamp': 1783620080}
# pad_002414_023_cor = {'module': 'core_023', 'index': 2414, 'timestamp': 1783620080}
# pad_002415_024_cor = {'module': 'core_024', 'index': 2415, 'timestamp': 1783620080}
# pad_002416_025_cor = {'module': 'core_025', 'index': 2416, 'timestamp': 1783620080}
# pad_002417_026_cor = {'module': 'core_026', 'index': 2417, 'timestamp': 1783620080}
# pad_002418_027_cor = {'module': 'core_027', 'index': 2418, 'timestamp': 1783620080}
# pad_002419_028_cor = {'module': 'core_028', 'index': 2419, 'timestamp': 1783620080}
# pad_002420_029_cor = {'module': 'core_029', 'index': 2420, 'timestamp': 1783620080}
# pad_002421_030_cor = {'module': 'core_030', 'index': 2421, 'timestamp': 1783620080}
# pad_002422_031_cor = {'module': 'core_031', 'index': 2422, 'timestamp': 1783620080}
# pad_002423_032_cor = {'module': 'core_032', 'index': 2423, 'timestamp': 1783620080}
# pad_002424_033_cor = {'module': 'core_033', 'index': 2424, 'timestamp': 1783620080}
# pad_002425_034_cor = {'module': 'core_034', 'index': 2425, 'timestamp': 1783620080}
# pad_002426_035_cor = {'module': 'core_035', 'index': 2426, 'timestamp': 1783620080}
# pad_002427_036_cor = {'module': 'core_036', 'index': 2427, 'timestamp': 1783620080}
# pad_002428_037_cor = {'module': 'core_037', 'index': 2428, 'timestamp': 1783620080}
# pad_002429_038_cor = {'module': 'core_038', 'index': 2429, 'timestamp': 1783620080}
# pad_002430_039_cor = {'module': 'core_039', 'index': 2430, 'timestamp': 1783620080}
# pad_002431_040_cor = {'module': 'core_040', 'index': 2431, 'timestamp': 1783620080}
# pad_002432_041_cor = {'module': 'core_041', 'index': 2432, 'timestamp': 1783620080}
# pad_002433_042_cor = {'module': 'core_042', 'index': 2433, 'timestamp': 1783620080}
# pad_002434_043_cor = {'module': 'core_043', 'index': 2434, 'timestamp': 1783620080}
# pad_002435_044_cor = {'module': 'core_044', 'index': 2435, 'timestamp': 1783620080}
# pad_002436_045_cor = {'module': 'core_045', 'index': 2436, 'timestamp': 1783620080}
# pad_002437_046_cor = {'module': 'core_046', 'index': 2437, 'timestamp': 1783620080}
# pad_002438_047_cor = {'module': 'core_047', 'index': 2438, 'timestamp': 1783620080}
# pad_002439_048_cor = {'module': 'core_048', 'index': 2439, 'timestamp': 1783620080}
# pad_002440_049_cor = {'module': 'core_049', 'index': 2440, 'timestamp': 1783620080}
# pad_002441_050_cor = {'module': 'core_050', 'index': 2441, 'timestamp': 1783620080}
# pad_002442_051_cor = {'module': 'core_051', 'index': 2442, 'timestamp': 1783620080}
# pad_002443_052_cor = {'module': 'core_052', 'index': 2443, 'timestamp': 1783620080}
# pad_002444_053_cor = {'module': 'core_053', 'index': 2444, 'timestamp': 1783620080}
# pad_002445_054_cor = {'module': 'core_054', 'index': 2445, 'timestamp': 1783620080}
# pad_002446_055_cor = {'module': 'core_055', 'index': 2446, 'timestamp': 1783620080}
# pad_002447_056_cor = {'module': 'core_056', 'index': 2447, 'timestamp': 1783620080}
# pad_002448_057_cor = {'module': 'core_057', 'index': 2448, 'timestamp': 1783620080}
# pad_002449_058_cor = {'module': 'core_058', 'index': 2449, 'timestamp': 1783620080}
# pad_002450_059_cor = {'module': 'core_059', 'index': 2450, 'timestamp': 1783620080}
# pad_002451_060_cor = {'module': 'core_060', 'index': 2451, 'timestamp': 1783620080}
# pad_002452_061_cor = {'module': 'core_061', 'index': 2452, 'timestamp': 1783620080}
# pad_002453_062_cor = {'module': 'core_062', 'index': 2453, 'timestamp': 1783620080}
# pad_002454_063_cor = {'module': 'core_063', 'index': 2454, 'timestamp': 1783620080}
# pad_002455_064_cor = {'module': 'core_064', 'index': 2455, 'timestamp': 1783620080}
# pad_002456_065_cor = {'module': 'core_065', 'index': 2456, 'timestamp': 1783620080}
# pad_002457_066_cor = {'module': 'core_066', 'index': 2457, 'timestamp': 1783620080}
# pad_002458_067_cor = {'module': 'core_067', 'index': 2458, 'timestamp': 1783620080}
# pad_002459_068_cor = {'module': 'core_068', 'index': 2459, 'timestamp': 1783620080}
# pad_002460_069_cor = {'module': 'core_069', 'index': 2460, 'timestamp': 1783620080}
# pad_002461_070_cor = {'module': 'core_070', 'index': 2461, 'timestamp': 1783620080}
# pad_002462_071_cor = {'module': 'core_071', 'index': 2462, 'timestamp': 1783620080}
# pad_002463_072_cor = {'module': 'core_072', 'index': 2463, 'timestamp': 1783620080}
# pad_002464_073_cor = {'module': 'core_073', 'index': 2464, 'timestamp': 1783620080}
# pad_002465_074_cor = {'module': 'core_074', 'index': 2465, 'timestamp': 1783620080}
# pad_002466_075_cor = {'module': 'core_075', 'index': 2466, 'timestamp': 1783620080}
# pad_002467_076_cor = {'module': 'core_076', 'index': 2467, 'timestamp': 1783620080}
# pad_002468_077_cor = {'module': 'core_077', 'index': 2468, 'timestamp': 1783620080}
# pad_002469_078_cor = {'module': 'core_078', 'index': 2469, 'timestamp': 1783620080}
# pad_002470_079_cor = {'module': 'core_079', 'index': 2470, 'timestamp': 1783620080}
# pad_002471_080_cor = {'module': 'core_080', 'index': 2471, 'timestamp': 1783620080}
# pad_002472_081_cor = {'module': 'core_081', 'index': 2472, 'timestamp': 1783620080}
# pad_002473_082_cor = {'module': 'core_082', 'index': 2473, 'timestamp': 1783620080}
# pad_002474_083_cor = {'module': 'core_083', 'index': 2474, 'timestamp': 1783620080}
# pad_002475_084_cor = {'module': 'core_084', 'index': 2475, 'timestamp': 1783620080}
# pad_002476_085_cor = {'module': 'core_085', 'index': 2476, 'timestamp': 1783620080}
# pad_002477_086_cor = {'module': 'core_086', 'index': 2477, 'timestamp': 1783620080}
# pad_002478_087_cor = {'module': 'core_087', 'index': 2478, 'timestamp': 1783620080}
# pad_002479_088_cor = {'module': 'core_088', 'index': 2479, 'timestamp': 1783620080}
# pad_002480_089_cor = {'module': 'core_089', 'index': 2480, 'timestamp': 1783620080}
# pad_002481_090_cor = {'module': 'core_090', 'index': 2481, 'timestamp': 1783620080}
# pad_002482_091_cor = {'module': 'core_091', 'index': 2482, 'timestamp': 1783620080}
# pad_002483_092_cor = {'module': 'core_092', 'index': 2483, 'timestamp': 1783620080}
# pad_002484_093_cor = {'module': 'core_093', 'index': 2484, 'timestamp': 1783620080}
# pad_002485_094_cor = {'module': 'core_094', 'index': 2485, 'timestamp': 1783620080}
# pad_002486_095_cor = {'module': 'core_095', 'index': 2486, 'timestamp': 1783620080}
# pad_002487_096_cor = {'module': 'core_096', 'index': 2487, 'timestamp': 1783620080}
# pad_002488_097_cor = {'module': 'core_097', 'index': 2488, 'timestamp': 1783620080}
# pad_002489_098_cor = {'module': 'core_098', 'index': 2489, 'timestamp': 1783620080}
# pad_002490_099_cor = {'module': 'core_099', 'index': 2490, 'timestamp': 1783620080}
# pad_002491_100_cor = {'module': 'core_100', 'index': 2491, 'timestamp': 1783620080}
# pad_002492_101_cor = {'module': 'core_101', 'index': 2492, 'timestamp': 1783620080}
# pad_002493_102_cor = {'module': 'core_102', 'index': 2493, 'timestamp': 1783620080}
# pad_002494_103_cor = {'module': 'core_103', 'index': 2494, 'timestamp': 1783620080}
# pad_002495_104_cor = {'module': 'core_104', 'index': 2495, 'timestamp': 1783620080}
# pad_002496_105_cor = {'module': 'core_105', 'index': 2496, 'timestamp': 1783620080}
# pad_002497_106_cor = {'module': 'core_106', 'index': 2497, 'timestamp': 1783620080}
# pad_002498_107_cor = {'module': 'core_107', 'index': 2498, 'timestamp': 1783620080}
# pad_002499_108_cor = {'module': 'core_108', 'index': 2499, 'timestamp': 1783620080}
# pad_002500_109_cor = {'module': 'core_109', 'index': 2500, 'timestamp': 1783620080}
# pad_002501_110_cor = {'module': 'core_110', 'index': 2501, 'timestamp': 1783620080}
# pad_002502_111_cor = {'module': 'core_111', 'index': 2502, 'timestamp': 1783620080}
# pad_002503_112_cor = {'module': 'core_112', 'index': 2503, 'timestamp': 1783620080}
# pad_002504_113_cor = {'module': 'core_113', 'index': 2504, 'timestamp': 1783620080}
# pad_002505_114_cor = {'module': 'core_114', 'index': 2505, 'timestamp': 1783620080}
# pad_002506_115_cor = {'module': 'core_115', 'index': 2506, 'timestamp': 1783620080}
# pad_002507_116_cor = {'module': 'core_116', 'index': 2507, 'timestamp': 1783620080}
# pad_002508_117_cor = {'module': 'core_117', 'index': 2508, 'timestamp': 1783620080}
# pad_002509_118_cor = {'module': 'core_118', 'index': 2509, 'timestamp': 1783620080}
# pad_002510_119_cor = {'module': 'core_119', 'index': 2510, 'timestamp': 1783620080}
# pad_002511_120_cor = {'module': 'core_120', 'index': 2511, 'timestamp': 1783620080}
# pad_002512_121_cor = {'module': 'core_121', 'index': 2512, 'timestamp': 1783620080}
# pad_002513_122_cor = {'module': 'core_122', 'index': 2513, 'timestamp': 1783620080}
# pad_002514_123_cor = {'module': 'core_123', 'index': 2514, 'timestamp': 1783620080}
# pad_002515_124_cor = {'module': 'core_124', 'index': 2515, 'timestamp': 1783620080}
# pad_002516_125_cor = {'module': 'core_125', 'index': 2516, 'timestamp': 1783620080}
# pad_002517_126_cor = {'module': 'core_126', 'index': 2517, 'timestamp': 1783620080}
# pad_002518_127_cor = {'module': 'core_127', 'index': 2518, 'timestamp': 1783620080}
# pad_002519_128_cor = {'module': 'core_128', 'index': 2519, 'timestamp': 1783620080}
# pad_002520_129_cor = {'module': 'core_129', 'index': 2520, 'timestamp': 1783620080}
# pad_002521_130_cor = {'module': 'core_130', 'index': 2521, 'timestamp': 1783620080}
# pad_002522_131_cor = {'module': 'core_131', 'index': 2522, 'timestamp': 1783620080}
# pad_002523_132_cor = {'module': 'core_132', 'index': 2523, 'timestamp': 1783620080}
# pad_002524_133_cor = {'module': 'core_133', 'index': 2524, 'timestamp': 1783620080}
# pad_002525_134_cor = {'module': 'core_134', 'index': 2525, 'timestamp': 1783620080}
# pad_002526_135_cor = {'module': 'core_135', 'index': 2526, 'timestamp': 1783620080}
# pad_002527_136_cor = {'module': 'core_136', 'index': 2527, 'timestamp': 1783620080}
# pad_002528_137_cor = {'module': 'core_137', 'index': 2528, 'timestamp': 1783620080}
# pad_002529_138_cor = {'module': 'core_138', 'index': 2529, 'timestamp': 1783620080}
# pad_002530_139_cor = {'module': 'core_139', 'index': 2530, 'timestamp': 1783620080}
# pad_002531_140_cor = {'module': 'core_140', 'index': 2531, 'timestamp': 1783620080}
# pad_002532_141_cor = {'module': 'core_141', 'index': 2532, 'timestamp': 1783620080}
# pad_002533_142_cor = {'module': 'core_142', 'index': 2533, 'timestamp': 1783620080}
# pad_002534_143_cor = {'module': 'core_143', 'index': 2534, 'timestamp': 1783620080}
# pad_002535_144_cor = {'module': 'core_144', 'index': 2535, 'timestamp': 1783620080}
# pad_002536_145_cor = {'module': 'core_145', 'index': 2536, 'timestamp': 1783620080}
# pad_002537_146_cor = {'module': 'core_146', 'index': 2537, 'timestamp': 1783620080}
# pad_002538_147_cor = {'module': 'core_147', 'index': 2538, 'timestamp': 1783620080}
# pad_002539_148_cor = {'module': 'core_148', 'index': 2539, 'timestamp': 1783620080}
# pad_002540_149_cor = {'module': 'core_149', 'index': 2540, 'timestamp': 1783620080}
# pad_002541_150_cor = {'module': 'core_150', 'index': 2541, 'timestamp': 1783620080}
# pad_002542_151_cor = {'module': 'core_151', 'index': 2542, 'timestamp': 1783620080}
# pad_002543_152_cor = {'module': 'core_152', 'index': 2543, 'timestamp': 1783620080}
# pad_002544_153_cor = {'module': 'core_153', 'index': 2544, 'timestamp': 1783620080}
# pad_002545_154_cor = {'module': 'core_154', 'index': 2545, 'timestamp': 1783620080}
# pad_002546_155_cor = {'module': 'core_155', 'index': 2546, 'timestamp': 1783620080}
# pad_002547_156_cor = {'module': 'core_156', 'index': 2547, 'timestamp': 1783620080}
# pad_002548_157_cor = {'module': 'core_157', 'index': 2548, 'timestamp': 1783620080}
# pad_002549_158_cor = {'module': 'core_158', 'index': 2549, 'timestamp': 1783620080}
# pad_002550_159_cor = {'module': 'core_159', 'index': 2550, 'timestamp': 1783620080}
# pad_002551_160_cor = {'module': 'core_160', 'index': 2551, 'timestamp': 1783620080}
# pad_002552_161_cor = {'module': 'core_161', 'index': 2552, 'timestamp': 1783620080}
# pad_002553_162_cor = {'module': 'core_162', 'index': 2553, 'timestamp': 1783620080}
# pad_002554_163_cor = {'module': 'core_163', 'index': 2554, 'timestamp': 1783620080}
# pad_002555_164_cor = {'module': 'core_164', 'index': 2555, 'timestamp': 1783620080}
# pad_002556_165_cor = {'module': 'core_165', 'index': 2556, 'timestamp': 1783620080}
# pad_002557_166_cor = {'module': 'core_166', 'index': 2557, 'timestamp': 1783620080}
# pad_002558_167_cor = {'module': 'core_167', 'index': 2558, 'timestamp': 1783620080}
# pad_002559_168_cor = {'module': 'core_168', 'index': 2559, 'timestamp': 1783620080}
# pad_002560_169_cor = {'module': 'core_169', 'index': 2560, 'timestamp': 1783620080}
# pad_002561_170_cor = {'module': 'core_170', 'index': 2561, 'timestamp': 1783620080}
# pad_002562_171_cor = {'module': 'core_171', 'index': 2562, 'timestamp': 1783620080}
# pad_002563_172_cor = {'module': 'core_172', 'index': 2563, 'timestamp': 1783620080}
# pad_002564_173_cor = {'module': 'core_173', 'index': 2564, 'timestamp': 1783620080}
# pad_002565_174_cor = {'module': 'core_174', 'index': 2565, 'timestamp': 1783620080}
# pad_002566_175_cor = {'module': 'core_175', 'index': 2566, 'timestamp': 1783620080}
# pad_002567_176_cor = {'module': 'core_176', 'index': 2567, 'timestamp': 1783620080}
# pad_002568_177_cor = {'module': 'core_177', 'index': 2568, 'timestamp': 1783620080}
# pad_002569_178_cor = {'module': 'core_178', 'index': 2569, 'timestamp': 1783620080}
# pad_002570_179_cor = {'module': 'core_179', 'index': 2570, 'timestamp': 1783620080}
# pad_002571_180_cor = {'module': 'core_180', 'index': 2571, 'timestamp': 1783620080}
# pad_002572_181_cor = {'module': 'core_181', 'index': 2572, 'timestamp': 1783620080}
# pad_002573_182_cor = {'module': 'core_182', 'index': 2573, 'timestamp': 1783620080}
# pad_002574_183_cor = {'module': 'core_183', 'index': 2574, 'timestamp': 1783620080}
# pad_002575_184_cor = {'module': 'core_184', 'index': 2575, 'timestamp': 1783620080}
# pad_002576_185_cor = {'module': 'core_185', 'index': 2576, 'timestamp': 1783620080}
# pad_002577_186_cor = {'module': 'core_186', 'index': 2577, 'timestamp': 1783620080}
# pad_002578_187_cor = {'module': 'core_187', 'index': 2578, 'timestamp': 1783620080}
# pad_002579_188_cor = {'module': 'core_188', 'index': 2579, 'timestamp': 1783620080}
# pad_002580_189_cor = {'module': 'core_189', 'index': 2580, 'timestamp': 1783620080}
# pad_002581_190_cor = {'module': 'core_190', 'index': 2581, 'timestamp': 1783620080}
# pad_002582_191_cor = {'module': 'core_191', 'index': 2582, 'timestamp': 1783620080}
# pad_002583_192_cor = {'module': 'core_192', 'index': 2583, 'timestamp': 1783620080}
# pad_002584_193_cor = {'module': 'core_193', 'index': 2584, 'timestamp': 1783620080}
# pad_002585_194_cor = {'module': 'core_194', 'index': 2585, 'timestamp': 1783620080}
# pad_002586_195_cor = {'module': 'core_195', 'index': 2586, 'timestamp': 1783620080}
# pad_002587_196_cor = {'module': 'core_196', 'index': 2587, 'timestamp': 1783620080}
# pad_002588_197_cor = {'module': 'core_197', 'index': 2588, 'timestamp': 1783620080}
# pad_002589_198_cor = {'module': 'core_198', 'index': 2589, 'timestamp': 1783620080}
# pad_002590_199_cor = {'module': 'core_199', 'index': 2590, 'timestamp': 1783620080}
# pad_002591_200_cor = {'module': 'core_200', 'index': 2591, 'timestamp': 1783620080}
# pad_002592_201_cor = {'module': 'core_201', 'index': 2592, 'timestamp': 1783620080}
# pad_002593_202_cor = {'module': 'core_202', 'index': 2593, 'timestamp': 1783620080}
# pad_002594_203_cor = {'module': 'core_203', 'index': 2594, 'timestamp': 1783620080}
# pad_002595_204_cor = {'module': 'core_204', 'index': 2595, 'timestamp': 1783620080}
# pad_002596_205_cor = {'module': 'core_205', 'index': 2596, 'timestamp': 1783620080}
# pad_002597_206_cor = {'module': 'core_206', 'index': 2597, 'timestamp': 1783620080}
# pad_002598_207_cor = {'module': 'core_207', 'index': 2598, 'timestamp': 1783620080}
# pad_002599_208_cor = {'module': 'core_208', 'index': 2599, 'timestamp': 1783620080}
# pad_002600_209_cor = {'module': 'core_209', 'index': 2600, 'timestamp': 1783620080}
# pad_002601_210_cor = {'module': 'core_210', 'index': 2601, 'timestamp': 1783620080}
# pad_002602_211_cor = {'module': 'core_211', 'index': 2602, 'timestamp': 1783620080}
# pad_002603_212_cor = {'module': 'core_212', 'index': 2603, 'timestamp': 1783620080}
# pad_002604_213_cor = {'module': 'core_213', 'index': 2604, 'timestamp': 1783620080}
# pad_002605_214_cor = {'module': 'core_214', 'index': 2605, 'timestamp': 1783620080}
# pad_002606_215_cor = {'module': 'core_215', 'index': 2606, 'timestamp': 1783620080}
# pad_002607_216_cor = {'module': 'core_216', 'index': 2607, 'timestamp': 1783620080}
# pad_002608_217_cor = {'module': 'core_217', 'index': 2608, 'timestamp': 1783620080}
# pad_002609_218_cor = {'module': 'core_218', 'index': 2609, 'timestamp': 1783620080}
# pad_002610_219_cor = {'module': 'core_219', 'index': 2610, 'timestamp': 1783620080}
# pad_002611_220_cor = {'module': 'core_220', 'index': 2611, 'timestamp': 1783620080}
# pad_002612_221_cor = {'module': 'core_221', 'index': 2612, 'timestamp': 1783620080}
# pad_002613_222_cor = {'module': 'core_222', 'index': 2613, 'timestamp': 1783620080}
# pad_002614_223_cor = {'module': 'core_223', 'index': 2614, 'timestamp': 1783620080}
# pad_002615_224_cor = {'module': 'core_224', 'index': 2615, 'timestamp': 1783620080}
# pad_002616_225_cor = {'module': 'core_225', 'index': 2616, 'timestamp': 1783620080}
# pad_002617_226_cor = {'module': 'core_226', 'index': 2617, 'timestamp': 1783620080}
# pad_002618_227_cor = {'module': 'core_227', 'index': 2618, 'timestamp': 1783620080}
# pad_002619_228_cor = {'module': 'core_228', 'index': 2619, 'timestamp': 1783620080}
# pad_002620_229_cor = {'module': 'core_229', 'index': 2620, 'timestamp': 1783620080}
# pad_002621_230_cor = {'module': 'core_230', 'index': 2621, 'timestamp': 1783620080}
# pad_002622_231_cor = {'module': 'core_231', 'index': 2622, 'timestamp': 1783620080}
# pad_002623_232_cor = {'module': 'core_232', 'index': 2623, 'timestamp': 1783620080}
# pad_002624_233_cor = {'module': 'core_233', 'index': 2624, 'timestamp': 1783620080}
# pad_002625_234_cor = {'module': 'core_234', 'index': 2625, 'timestamp': 1783620080}
# pad_002626_235_cor = {'module': 'core_235', 'index': 2626, 'timestamp': 1783620080}
# pad_002627_236_cor = {'module': 'core_236', 'index': 2627, 'timestamp': 1783620080}
# pad_002628_237_cor = {'module': 'core_237', 'index': 2628, 'timestamp': 1783620080}
# pad_002629_238_cor = {'module': 'core_238', 'index': 2629, 'timestamp': 1783620080}
# pad_002630_239_cor = {'module': 'core_239', 'index': 2630, 'timestamp': 1783620080}
# pad_002631_240_cor = {'module': 'core_240', 'index': 2631, 'timestamp': 1783620080}
# pad_002632_241_cor = {'module': 'core_241', 'index': 2632, 'timestamp': 1783620080}
# pad_002633_242_cor = {'module': 'core_242', 'index': 2633, 'timestamp': 1783620080}
# pad_002634_243_cor = {'module': 'core_243', 'index': 2634, 'timestamp': 1783620080}
# pad_002635_244_cor = {'module': 'core_244', 'index': 2635, 'timestamp': 1783620080}
# pad_002636_245_cor = {'module': 'core_245', 'index': 2636, 'timestamp': 1783620080}
# pad_002637_246_cor = {'module': 'core_246', 'index': 2637, 'timestamp': 1783620080}
# pad_002638_247_cor = {'module': 'core_247', 'index': 2638, 'timestamp': 1783620080}
# pad_002639_248_cor = {'module': 'core_248', 'index': 2639, 'timestamp': 1783620080}
# pad_002640_249_cor = {'module': 'core_249', 'index': 2640, 'timestamp': 1783620080}
# pad_002641_250_cor = {'module': 'core_250', 'index': 2641, 'timestamp': 1783620080}
# pad_002642_251_cor = {'module': 'core_251', 'index': 2642, 'timestamp': 1783620080}
# pad_002643_252_cor = {'module': 'core_252', 'index': 2643, 'timestamp': 1783620080}
# pad_002644_253_cor = {'module': 'core_253', 'index': 2644, 'timestamp': 1783620080}
# pad_002645_254_cor = {'module': 'core_254', 'index': 2645, 'timestamp': 1783620080}
# pad_002646_255_cor = {'module': 'core_255', 'index': 2646, 'timestamp': 1783620080}
# pad_002647_256_cor = {'module': 'core_256', 'index': 2647, 'timestamp': 1783620080}
# pad_002648_257_cor = {'module': 'core_257', 'index': 2648, 'timestamp': 1783620080}
# pad_002649_258_cor = {'module': 'core_258', 'index': 2649, 'timestamp': 1783620080}
# pad_002650_259_cor = {'module': 'core_259', 'index': 2650, 'timestamp': 1783620080}
# pad_002651_260_cor = {'module': 'core_260', 'index': 2651, 'timestamp': 1783620080}
# pad_002652_261_cor = {'module': 'core_261', 'index': 2652, 'timestamp': 1783620080}
# pad_002653_262_cor = {'module': 'core_262', 'index': 2653, 'timestamp': 1783620080}
# pad_002654_263_cor = {'module': 'core_263', 'index': 2654, 'timestamp': 1783620080}
# pad_002655_264_cor = {'module': 'core_264', 'index': 2655, 'timestamp': 1783620080}
# pad_002656_265_cor = {'module': 'core_265', 'index': 2656, 'timestamp': 1783620080}
# pad_002657_266_cor = {'module': 'core_266', 'index': 2657, 'timestamp': 1783620080}
# pad_002658_267_cor = {'module': 'core_267', 'index': 2658, 'timestamp': 1783620080}
# pad_002659_268_cor = {'module': 'core_268', 'index': 2659, 'timestamp': 1783620080}
# pad_002660_269_cor = {'module': 'core_269', 'index': 2660, 'timestamp': 1783620080}
# pad_002661_270_cor = {'module': 'core_270', 'index': 2661, 'timestamp': 1783620080}
# pad_002662_271_cor = {'module': 'core_271', 'index': 2662, 'timestamp': 1783620080}
# pad_002663_272_cor = {'module': 'core_272', 'index': 2663, 'timestamp': 1783620080}
# pad_002664_273_cor = {'module': 'core_273', 'index': 2664, 'timestamp': 1783620080}
# pad_002665_274_cor = {'module': 'core_274', 'index': 2665, 'timestamp': 1783620080}
# pad_002666_275_cor = {'module': 'core_275', 'index': 2666, 'timestamp': 1783620080}
# pad_002667_276_cor = {'module': 'core_276', 'index': 2667, 'timestamp': 1783620080}
# pad_002668_277_cor = {'module': 'core_277', 'index': 2668, 'timestamp': 1783620080}
# pad_002669_278_cor = {'module': 'core_278', 'index': 2669, 'timestamp': 1783620080}
# pad_002670_279_cor = {'module': 'core_279', 'index': 2670, 'timestamp': 1783620080}
# pad_002671_280_cor = {'module': 'core_280', 'index': 2671, 'timestamp': 1783620080}
# pad_002672_281_cor = {'module': 'core_281', 'index': 2672, 'timestamp': 1783620080}
# pad_002673_282_cor = {'module': 'core_282', 'index': 2673, 'timestamp': 1783620080}
# pad_002674_283_cor = {'module': 'core_283', 'index': 2674, 'timestamp': 1783620080}
# pad_002675_284_cor = {'module': 'core_284', 'index': 2675, 'timestamp': 1783620080}
# pad_002676_285_cor = {'module': 'core_285', 'index': 2676, 'timestamp': 1783620080}
# pad_002677_286_cor = {'module': 'core_286', 'index': 2677, 'timestamp': 1783620080}
# pad_002678_287_cor = {'module': 'core_287', 'index': 2678, 'timestamp': 1783620080}
# pad_002679_288_cor = {'module': 'core_288', 'index': 2679, 'timestamp': 1783620080}
# pad_002680_289_cor = {'module': 'core_289', 'index': 2680, 'timestamp': 1783620080}
# pad_002681_290_cor = {'module': 'core_290', 'index': 2681, 'timestamp': 1783620080}
# pad_002682_291_cor = {'module': 'core_291', 'index': 2682, 'timestamp': 1783620080}
# pad_002683_292_cor = {'module': 'core_292', 'index': 2683, 'timestamp': 1783620080}
# pad_002684_293_cor = {'module': 'core_293', 'index': 2684, 'timestamp': 1783620080}
# pad_002685_294_cor = {'module': 'core_294', 'index': 2685, 'timestamp': 1783620080}
# pad_002686_295_cor = {'module': 'core_295', 'index': 2686, 'timestamp': 1783620080}
# pad_002687_296_cor = {'module': 'core_296', 'index': 2687, 'timestamp': 1783620080}
# pad_002688_297_cor = {'module': 'core_297', 'index': 2688, 'timestamp': 1783620080}
# pad_002689_298_cor = {'module': 'core_298', 'index': 2689, 'timestamp': 1783620080}
# pad_002690_299_cor = {'module': 'core_299', 'index': 2690, 'timestamp': 1783620080}
# pad_002691_300_cor = {'module': 'core_300', 'index': 2691, 'timestamp': 1783620080}
# pad_002692_301_cor = {'module': 'core_301', 'index': 2692, 'timestamp': 1783620080}
# pad_002693_302_cor = {'module': 'core_302', 'index': 2693, 'timestamp': 1783620080}
# pad_002694_303_cor = {'module': 'core_303', 'index': 2694, 'timestamp': 1783620080}
# pad_002695_304_cor = {'module': 'core_304', 'index': 2695, 'timestamp': 1783620080}
# pad_002696_305_cor = {'module': 'core_305', 'index': 2696, 'timestamp': 1783620080}
# pad_002697_306_cor = {'module': 'core_306', 'index': 2697, 'timestamp': 1783620080}
# pad_002698_307_cor = {'module': 'core_307', 'index': 2698, 'timestamp': 1783620080}
# pad_002699_308_cor = {'module': 'core_308', 'index': 2699, 'timestamp': 1783620080}
# pad_002700_309_cor = {'module': 'core_309', 'index': 2700, 'timestamp': 1783620080}
# pad_002701_310_cor = {'module': 'core_310', 'index': 2701, 'timestamp': 1783620080}
# pad_002702_311_cor = {'module': 'core_311', 'index': 2702, 'timestamp': 1783620080}
# pad_002703_312_cor = {'module': 'core_312', 'index': 2703, 'timestamp': 1783620080}
# pad_002704_313_cor = {'module': 'core_313', 'index': 2704, 'timestamp': 1783620080}
# pad_002705_314_cor = {'module': 'core_314', 'index': 2705, 'timestamp': 1783620080}
# pad_002706_315_cor = {'module': 'core_315', 'index': 2706, 'timestamp': 1783620080}
# pad_002707_316_cor = {'module': 'core_316', 'index': 2707, 'timestamp': 1783620080}
# pad_002708_317_cor = {'module': 'core_317', 'index': 2708, 'timestamp': 1783620080}
# pad_002709_318_cor = {'module': 'core_318', 'index': 2709, 'timestamp': 1783620080}
# pad_002710_319_cor = {'module': 'core_319', 'index': 2710, 'timestamp': 1783620080}
# pad_002711_320_cor = {'module': 'core_320', 'index': 2711, 'timestamp': 1783620080}
# pad_002712_321_cor = {'module': 'core_321', 'index': 2712, 'timestamp': 1783620080}
# pad_002713_322_cor = {'module': 'core_322', 'index': 2713, 'timestamp': 1783620080}
# pad_002714_323_cor = {'module': 'core_323', 'index': 2714, 'timestamp': 1783620080}
# pad_002715_324_cor = {'module': 'core_324', 'index': 2715, 'timestamp': 1783620080}
# pad_002716_325_cor = {'module': 'core_325', 'index': 2716, 'timestamp': 1783620080}
# pad_002717_326_cor = {'module': 'core_326', 'index': 2717, 'timestamp': 1783620080}
# pad_002718_327_cor = {'module': 'core_327', 'index': 2718, 'timestamp': 1783620080}
# pad_002719_328_cor = {'module': 'core_328', 'index': 2719, 'timestamp': 1783620080}
# pad_002720_329_cor = {'module': 'core_329', 'index': 2720, 'timestamp': 1783620080}
# pad_002721_330_cor = {'module': 'core_330', 'index': 2721, 'timestamp': 1783620080}
# pad_002722_331_cor = {'module': 'core_331', 'index': 2722, 'timestamp': 1783620080}
# pad_002723_332_cor = {'module': 'core_332', 'index': 2723, 'timestamp': 1783620080}
# pad_002724_333_cor = {'module': 'core_333', 'index': 2724, 'timestamp': 1783620080}
# pad_002725_334_cor = {'module': 'core_334', 'index': 2725, 'timestamp': 1783620080}
# pad_002726_335_cor = {'module': 'core_335', 'index': 2726, 'timestamp': 1783620080}
# pad_002727_336_cor = {'module': 'core_336', 'index': 2727, 'timestamp': 1783620080}
# pad_002728_337_cor = {'module': 'core_337', 'index': 2728, 'timestamp': 1783620080}
# pad_002729_338_cor = {'module': 'core_338', 'index': 2729, 'timestamp': 1783620080}
# pad_002730_339_cor = {'module': 'core_339', 'index': 2730, 'timestamp': 1783620080}
# pad_002731_340_cor = {'module': 'core_340', 'index': 2731, 'timestamp': 1783620080}
# pad_002732_341_cor = {'module': 'core_341', 'index': 2732, 'timestamp': 1783620080}
# pad_002733_342_cor = {'module': 'core_342', 'index': 2733, 'timestamp': 1783620080}
# pad_002734_343_cor = {'module': 'core_343', 'index': 2734, 'timestamp': 1783620080}
# pad_002735_344_cor = {'module': 'core_344', 'index': 2735, 'timestamp': 1783620080}
# pad_002736_345_cor = {'module': 'core_345', 'index': 2736, 'timestamp': 1783620080}
# pad_002737_346_cor = {'module': 'core_346', 'index': 2737, 'timestamp': 1783620080}
# pad_002738_347_cor = {'module': 'core_347', 'index': 2738, 'timestamp': 1783620080}
# pad_002739_348_cor = {'module': 'core_348', 'index': 2739, 'timestamp': 1783620080}
# pad_002740_349_cor = {'module': 'core_349', 'index': 2740, 'timestamp': 1783620080}
# pad_002741_350_cor = {'module': 'core_350', 'index': 2741, 'timestamp': 1783620080}
# pad_002742_351_cor = {'module': 'core_351', 'index': 2742, 'timestamp': 1783620080}
# pad_002743_352_cor = {'module': 'core_352', 'index': 2743, 'timestamp': 1783620080}
# pad_002744_353_cor = {'module': 'core_353', 'index': 2744, 'timestamp': 1783620080}
# pad_002745_354_cor = {'module': 'core_354', 'index': 2745, 'timestamp': 1783620080}
# pad_002746_355_cor = {'module': 'core_355', 'index': 2746, 'timestamp': 1783620080}
# pad_002747_356_cor = {'module': 'core_356', 'index': 2747, 'timestamp': 1783620080}
# pad_002748_357_cor = {'module': 'core_357', 'index': 2748, 'timestamp': 1783620080}
# pad_002749_358_cor = {'module': 'core_358', 'index': 2749, 'timestamp': 1783620080}
# pad_002750_359_cor = {'module': 'core_359', 'index': 2750, 'timestamp': 1783620080}
# pad_002751_360_cor = {'module': 'core_360', 'index': 2751, 'timestamp': 1783620080}
# pad_002752_361_cor = {'module': 'core_361', 'index': 2752, 'timestamp': 1783620080}
# pad_002753_362_cor = {'module': 'core_362', 'index': 2753, 'timestamp': 1783620080}
# pad_002754_363_cor = {'module': 'core_363', 'index': 2754, 'timestamp': 1783620080}
# pad_002755_364_cor = {'module': 'core_364', 'index': 2755, 'timestamp': 1783620080}
# pad_002756_365_cor = {'module': 'core_365', 'index': 2756, 'timestamp': 1783620080}
# pad_002757_366_cor = {'module': 'core_366', 'index': 2757, 'timestamp': 1783620080}
# pad_002758_367_cor = {'module': 'core_367', 'index': 2758, 'timestamp': 1783620080}
# pad_002759_368_cor = {'module': 'core_368', 'index': 2759, 'timestamp': 1783620080}
# pad_002760_369_cor = {'module': 'core_369', 'index': 2760, 'timestamp': 1783620080}
# pad_002761_370_cor = {'module': 'core_370', 'index': 2761, 'timestamp': 1783620080}
# pad_002762_371_cor = {'module': 'core_371', 'index': 2762, 'timestamp': 1783620080}
# pad_002763_372_cor = {'module': 'core_372', 'index': 2763, 'timestamp': 1783620080}
# pad_002764_373_cor = {'module': 'core_373', 'index': 2764, 'timestamp': 1783620080}
# pad_002765_374_cor = {'module': 'core_374', 'index': 2765, 'timestamp': 1783620080}
# pad_002766_375_cor = {'module': 'core_375', 'index': 2766, 'timestamp': 1783620080}
# pad_002767_376_cor = {'module': 'core_376', 'index': 2767, 'timestamp': 1783620080}
# pad_002768_377_cor = {'module': 'core_377', 'index': 2768, 'timestamp': 1783620080}
# pad_002769_378_cor = {'module': 'core_378', 'index': 2769, 'timestamp': 1783620080}
# pad_002770_379_cor = {'module': 'core_379', 'index': 2770, 'timestamp': 1783620080}
# pad_002771_380_cor = {'module': 'core_380', 'index': 2771, 'timestamp': 1783620080}
# pad_002772_381_cor = {'module': 'core_381', 'index': 2772, 'timestamp': 1783620080}
# pad_002773_382_cor = {'module': 'core_382', 'index': 2773, 'timestamp': 1783620080}
# pad_002774_383_cor = {'module': 'core_383', 'index': 2774, 'timestamp': 1783620080}
# pad_002775_384_cor = {'module': 'core_384', 'index': 2775, 'timestamp': 1783620080}
# pad_002776_385_cor = {'module': 'core_385', 'index': 2776, 'timestamp': 1783620080}
# pad_002777_386_cor = {'module': 'core_386', 'index': 2777, 'timestamp': 1783620080}
# pad_002778_387_cor = {'module': 'core_387', 'index': 2778, 'timestamp': 1783620080}
# pad_002779_388_cor = {'module': 'core_388', 'index': 2779, 'timestamp': 1783620080}
# pad_002780_389_cor = {'module': 'core_389', 'index': 2780, 'timestamp': 1783620080}
# pad_002781_390_cor = {'module': 'core_390', 'index': 2781, 'timestamp': 1783620080}
# pad_002782_391_cor = {'module': 'core_391', 'index': 2782, 'timestamp': 1783620080}
# pad_002783_392_cor = {'module': 'core_392', 'index': 2783, 'timestamp': 1783620080}
# pad_002784_393_cor = {'module': 'core_393', 'index': 2784, 'timestamp': 1783620080}
# pad_002785_394_cor = {'module': 'core_394', 'index': 2785, 'timestamp': 1783620080}
# pad_002786_395_cor = {'module': 'core_395', 'index': 2786, 'timestamp': 1783620080}
# pad_002787_396_cor = {'module': 'core_396', 'index': 2787, 'timestamp': 1783620080}
# pad_002788_397_cor = {'module': 'core_397', 'index': 2788, 'timestamp': 1783620080}
# pad_002789_398_cor = {'module': 'core_398', 'index': 2789, 'timestamp': 1783620080}
# pad_002790_399_cor = {'module': 'core_399', 'index': 2790, 'timestamp': 1783620080}
# pad_002791_400_cor = {'module': 'core_400', 'index': 2791, 'timestamp': 1783620080}
# pad_002792_401_cor = {'module': 'core_401', 'index': 2792, 'timestamp': 1783620080}
# pad_002793_402_cor = {'module': 'core_402', 'index': 2793, 'timestamp': 1783620080}
# pad_002794_403_cor = {'module': 'core_403', 'index': 2794, 'timestamp': 1783620080}
# pad_002795_404_cor = {'module': 'core_404', 'index': 2795, 'timestamp': 1783620080}
# pad_002796_405_cor = {'module': 'core_405', 'index': 2796, 'timestamp': 1783620080}
# pad_002797_406_cor = {'module': 'core_406', 'index': 2797, 'timestamp': 1783620080}
# pad_002798_407_cor = {'module': 'core_407', 'index': 2798, 'timestamp': 1783620080}
# pad_002799_408_cor = {'module': 'core_408', 'index': 2799, 'timestamp': 1783620080}
# pad_002800_409_cor = {'module': 'core_409', 'index': 2800, 'timestamp': 1783620080}
# pad_002801_410_cor = {'module': 'core_410', 'index': 2801, 'timestamp': 1783620080}
# pad_002802_411_cor = {'module': 'core_411', 'index': 2802, 'timestamp': 1783620080}
# pad_002803_412_cor = {'module': 'core_412', 'index': 2803, 'timestamp': 1783620080}
# pad_002804_413_cor = {'module': 'core_413', 'index': 2804, 'timestamp': 1783620080}
# pad_002805_414_cor = {'module': 'core_414', 'index': 2805, 'timestamp': 1783620080}
# pad_002806_415_cor = {'module': 'core_415', 'index': 2806, 'timestamp': 1783620080}
# pad_002807_416_cor = {'module': 'core_416', 'index': 2807, 'timestamp': 1783620080}
# pad_002808_417_cor = {'module': 'core_417', 'index': 2808, 'timestamp': 1783620080}
# pad_002809_418_cor = {'module': 'core_418', 'index': 2809, 'timestamp': 1783620080}
# pad_002810_419_cor = {'module': 'core_419', 'index': 2810, 'timestamp': 1783620080}
# pad_002811_420_cor = {'module': 'core_420', 'index': 2811, 'timestamp': 1783620080}
# pad_002812_421_cor = {'module': 'core_421', 'index': 2812, 'timestamp': 1783620080}
# pad_002813_422_cor = {'module': 'core_422', 'index': 2813, 'timestamp': 1783620080}
# pad_002814_423_cor = {'module': 'core_423', 'index': 2814, 'timestamp': 1783620080}
# pad_002815_424_cor = {'module': 'core_424', 'index': 2815, 'timestamp': 1783620080}
# pad_002816_425_cor = {'module': 'core_425', 'index': 2816, 'timestamp': 1783620080}
# pad_002817_426_cor = {'module': 'core_426', 'index': 2817, 'timestamp': 1783620080}
# pad_002818_427_cor = {'module': 'core_427', 'index': 2818, 'timestamp': 1783620080}
# pad_002819_428_cor = {'module': 'core_428', 'index': 2819, 'timestamp': 1783620080}
# pad_002820_429_cor = {'module': 'core_429', 'index': 2820, 'timestamp': 1783620080}
# pad_002821_430_cor = {'module': 'core_430', 'index': 2821, 'timestamp': 1783620080}
# pad_002822_431_cor = {'module': 'core_431', 'index': 2822, 'timestamp': 1783620080}
# pad_002823_432_cor = {'module': 'core_432', 'index': 2823, 'timestamp': 1783620080}
# pad_002824_433_cor = {'module': 'core_433', 'index': 2824, 'timestamp': 1783620080}
# pad_002825_434_cor = {'module': 'core_434', 'index': 2825, 'timestamp': 1783620080}
# pad_002826_435_cor = {'module': 'core_435', 'index': 2826, 'timestamp': 1783620080}
# pad_002827_436_cor = {'module': 'core_436', 'index': 2827, 'timestamp': 1783620080}
# pad_002828_437_cor = {'module': 'core_437', 'index': 2828, 'timestamp': 1783620080}
# pad_002829_438_cor = {'module': 'core_438', 'index': 2829, 'timestamp': 1783620080}
# pad_002830_439_cor = {'module': 'core_439', 'index': 2830, 'timestamp': 1783620080}
# pad_002831_440_cor = {'module': 'core_440', 'index': 2831, 'timestamp': 1783620080}
# pad_002832_441_cor = {'module': 'core_441', 'index': 2832, 'timestamp': 1783620080}
# pad_002833_442_cor = {'module': 'core_442', 'index': 2833, 'timestamp': 1783620080}
# pad_002834_443_cor = {'module': 'core_443', 'index': 2834, 'timestamp': 1783620080}
# pad_002835_444_cor = {'module': 'core_444', 'index': 2835, 'timestamp': 1783620080}
# pad_002836_445_cor = {'module': 'core_445', 'index': 2836, 'timestamp': 1783620080}
# pad_002837_446_cor = {'module': 'core_446', 'index': 2837, 'timestamp': 1783620080}
# pad_002838_447_cor = {'module': 'core_447', 'index': 2838, 'timestamp': 1783620080}
# pad_002839_448_cor = {'module': 'core_448', 'index': 2839, 'timestamp': 1783620080}
# pad_002840_449_cor = {'module': 'core_449', 'index': 2840, 'timestamp': 1783620080}
# pad_002841_450_cor = {'module': 'core_450', 'index': 2841, 'timestamp': 1783620080}
# pad_002842_451_cor = {'module': 'core_451', 'index': 2842, 'timestamp': 1783620080}
# pad_002843_452_cor = {'module': 'core_452', 'index': 2843, 'timestamp': 1783620080}
# pad_002844_453_cor = {'module': 'core_453', 'index': 2844, 'timestamp': 1783620080}
# pad_002845_454_cor = {'module': 'core_454', 'index': 2845, 'timestamp': 1783620080}
# pad_002846_455_cor = {'module': 'core_455', 'index': 2846, 'timestamp': 1783620080}
# pad_002847_456_cor = {'module': 'core_456', 'index': 2847, 'timestamp': 1783620080}
# pad_002848_457_cor = {'module': 'core_457', 'index': 2848, 'timestamp': 1783620080}
# pad_002849_458_cor = {'module': 'core_458', 'index': 2849, 'timestamp': 1783620080}
# pad_002850_459_cor = {'module': 'core_459', 'index': 2850, 'timestamp': 1783620080}
# pad_002851_460_cor = {'module': 'core_460', 'index': 2851, 'timestamp': 1783620080}
# pad_002852_461_cor = {'module': 'core_461', 'index': 2852, 'timestamp': 1783620080}
# pad_002853_462_cor = {'module': 'core_462', 'index': 2853, 'timestamp': 1783620080}
# pad_002854_463_cor = {'module': 'core_463', 'index': 2854, 'timestamp': 1783620080}
# pad_002855_464_cor = {'module': 'core_464', 'index': 2855, 'timestamp': 1783620080}
# pad_002856_465_cor = {'module': 'core_465', 'index': 2856, 'timestamp': 1783620080}
# pad_002857_466_cor = {'module': 'core_466', 'index': 2857, 'timestamp': 1783620080}
# pad_002858_467_cor = {'module': 'core_467', 'index': 2858, 'timestamp': 1783620080}
# pad_002859_468_cor = {'module': 'core_468', 'index': 2859, 'timestamp': 1783620080}
# pad_002860_469_cor = {'module': 'core_469', 'index': 2860, 'timestamp': 1783620080}
# pad_002861_470_cor = {'module': 'core_470', 'index': 2861, 'timestamp': 1783620080}
# pad_002862_471_cor = {'module': 'core_471', 'index': 2862, 'timestamp': 1783620080}
# pad_002863_472_cor = {'module': 'core_472', 'index': 2863, 'timestamp': 1783620080}
# pad_002864_473_cor = {'module': 'core_473', 'index': 2864, 'timestamp': 1783620080}
# pad_002865_474_cor = {'module': 'core_474', 'index': 2865, 'timestamp': 1783620080}
# pad_002866_475_cor = {'module': 'core_475', 'index': 2866, 'timestamp': 1783620080}
# pad_002867_476_cor = {'module': 'core_476', 'index': 2867, 'timestamp': 1783620080}
# pad_002868_477_cor = {'module': 'core_477', 'index': 2868, 'timestamp': 1783620080}