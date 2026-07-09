"""
core_module_008.py - legacy core #8
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C8_0=42
T8_0="t0_8"
F8_0=True
C8_1=49
T8_1="t1_8"
F8_1=False
C8_2=56
T8_2="t2_8"
F8_2=True
C8_3=63
T8_3="t3_8"
F8_3=False
C8_4=70
T8_4="t4_8"
F8_4=True
C8_5=77
T8_5="t5_8"
F8_5=False
C8_6=84
T8_6="t6_8"
F8_6=True
C8_7=91
T8_7="t7_8"
F8_7=False
C8_8=98
T8_8="t8_8"
F8_8=True
C8_9=105
T8_9="t9_8"
F8_9=False
C8_10=112
T8_10="t10_8"
F8_10=True
C8_11=119
T8_11="t11_8"
F8_11=False
C8_12=126
T8_12="t12_8"
F8_12=True
C8_13=133
T8_13="t13_8"
F8_13=False
C8_14=140
T8_14="t14_8"
F8_14=True

def proc_cor_008_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_008_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":8}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*8+j+fi)%500
    r.append(v*2+C8_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":8}
def hlp_proc_cor_008_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR008000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR008000._lk:LegCOR008000._c+=1;self._i=LegCOR008000._c
  self.n=nm or f"LegCOR008000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*8+j+ci)%50
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

class LegCOR008001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR008001._lk:LegCOR008001._c+=1;self._i=LegCOR008001._c
  self.n=nm or f"LegCOR008001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*8+j+ci)%50
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

class LegCOR008002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR008002._lk:LegCOR008002._c+=1;self._i=LegCOR008002._c
  self.n=nm or f"LegCOR008002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*8+j+ci)%50
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

class LegCOR008003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR008003._lk:LegCOR008003._c+=1;self._i=LegCOR008003._c
  self.n=nm or f"LegCOR008003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*8+j+ci)%50
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

def val_cor_008_0000(d,s=None,st=True):
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

def val_cor_008_0001(d,s=None,st=True):
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

def val_cor_008_0002(d,s=None,st=True):
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

def val_cor_008_0003(d,s=None,st=True):
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

def val_cor_008_0004(d,s=None,st=True):
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

def val_cor_008_0005(d,s=None,st=True):
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

M008={
 "id":8,"d":"core","n":"core_module_008","v":"1.9"
}# pad_003347_000_cor = {'module': 'core_000', 'index': 3347, 'timestamp': 1783620080}
# pad_003348_001_cor = {'module': 'core_001', 'index': 3348, 'timestamp': 1783620080}
# pad_003349_002_cor = {'module': 'core_002', 'index': 3349, 'timestamp': 1783620080}
# pad_003350_003_cor = {'module': 'core_003', 'index': 3350, 'timestamp': 1783620080}
# pad_003351_004_cor = {'module': 'core_004', 'index': 3351, 'timestamp': 1783620080}
# pad_003352_005_cor = {'module': 'core_005', 'index': 3352, 'timestamp': 1783620080}
# pad_003353_006_cor = {'module': 'core_006', 'index': 3353, 'timestamp': 1783620080}
# pad_003354_007_cor = {'module': 'core_007', 'index': 3354, 'timestamp': 1783620080}
# pad_003355_008_cor = {'module': 'core_008', 'index': 3355, 'timestamp': 1783620080}
# pad_003356_009_cor = {'module': 'core_009', 'index': 3356, 'timestamp': 1783620080}
# pad_003357_010_cor = {'module': 'core_010', 'index': 3357, 'timestamp': 1783620080}
# pad_003358_011_cor = {'module': 'core_011', 'index': 3358, 'timestamp': 1783620080}
# pad_003359_012_cor = {'module': 'core_012', 'index': 3359, 'timestamp': 1783620080}
# pad_003360_013_cor = {'module': 'core_013', 'index': 3360, 'timestamp': 1783620080}
# pad_003361_014_cor = {'module': 'core_014', 'index': 3361, 'timestamp': 1783620080}
# pad_003362_015_cor = {'module': 'core_015', 'index': 3362, 'timestamp': 1783620080}
# pad_003363_016_cor = {'module': 'core_016', 'index': 3363, 'timestamp': 1783620080}
# pad_003364_017_cor = {'module': 'core_017', 'index': 3364, 'timestamp': 1783620080}
# pad_003365_018_cor = {'module': 'core_018', 'index': 3365, 'timestamp': 1783620080}
# pad_003366_019_cor = {'module': 'core_019', 'index': 3366, 'timestamp': 1783620080}
# pad_003367_020_cor = {'module': 'core_020', 'index': 3367, 'timestamp': 1783620080}
# pad_003368_021_cor = {'module': 'core_021', 'index': 3368, 'timestamp': 1783620080}
# pad_003369_022_cor = {'module': 'core_022', 'index': 3369, 'timestamp': 1783620080}
# pad_003370_023_cor = {'module': 'core_023', 'index': 3370, 'timestamp': 1783620080}
# pad_003371_024_cor = {'module': 'core_024', 'index': 3371, 'timestamp': 1783620080}
# pad_003372_025_cor = {'module': 'core_025', 'index': 3372, 'timestamp': 1783620080}
# pad_003373_026_cor = {'module': 'core_026', 'index': 3373, 'timestamp': 1783620080}
# pad_003374_027_cor = {'module': 'core_027', 'index': 3374, 'timestamp': 1783620080}
# pad_003375_028_cor = {'module': 'core_028', 'index': 3375, 'timestamp': 1783620080}
# pad_003376_029_cor = {'module': 'core_029', 'index': 3376, 'timestamp': 1783620080}
# pad_003377_030_cor = {'module': 'core_030', 'index': 3377, 'timestamp': 1783620080}
# pad_003378_031_cor = {'module': 'core_031', 'index': 3378, 'timestamp': 1783620080}
# pad_003379_032_cor = {'module': 'core_032', 'index': 3379, 'timestamp': 1783620080}
# pad_003380_033_cor = {'module': 'core_033', 'index': 3380, 'timestamp': 1783620080}
# pad_003381_034_cor = {'module': 'core_034', 'index': 3381, 'timestamp': 1783620080}
# pad_003382_035_cor = {'module': 'core_035', 'index': 3382, 'timestamp': 1783620080}
# pad_003383_036_cor = {'module': 'core_036', 'index': 3383, 'timestamp': 1783620080}
# pad_003384_037_cor = {'module': 'core_037', 'index': 3384, 'timestamp': 1783620080}
# pad_003385_038_cor = {'module': 'core_038', 'index': 3385, 'timestamp': 1783620080}
# pad_003386_039_cor = {'module': 'core_039', 'index': 3386, 'timestamp': 1783620080}
# pad_003387_040_cor = {'module': 'core_040', 'index': 3387, 'timestamp': 1783620080}
# pad_003388_041_cor = {'module': 'core_041', 'index': 3388, 'timestamp': 1783620080}
# pad_003389_042_cor = {'module': 'core_042', 'index': 3389, 'timestamp': 1783620080}
# pad_003390_043_cor = {'module': 'core_043', 'index': 3390, 'timestamp': 1783620080}
# pad_003391_044_cor = {'module': 'core_044', 'index': 3391, 'timestamp': 1783620080}
# pad_003392_045_cor = {'module': 'core_045', 'index': 3392, 'timestamp': 1783620080}
# pad_003393_046_cor = {'module': 'core_046', 'index': 3393, 'timestamp': 1783620080}
# pad_003394_047_cor = {'module': 'core_047', 'index': 3394, 'timestamp': 1783620080}
# pad_003395_048_cor = {'module': 'core_048', 'index': 3395, 'timestamp': 1783620080}
# pad_003396_049_cor = {'module': 'core_049', 'index': 3396, 'timestamp': 1783620080}
# pad_003397_050_cor = {'module': 'core_050', 'index': 3397, 'timestamp': 1783620080}
# pad_003398_051_cor = {'module': 'core_051', 'index': 3398, 'timestamp': 1783620080}
# pad_003399_052_cor = {'module': 'core_052', 'index': 3399, 'timestamp': 1783620080}
# pad_003400_053_cor = {'module': 'core_053', 'index': 3400, 'timestamp': 1783620080}
# pad_003401_054_cor = {'module': 'core_054', 'index': 3401, 'timestamp': 1783620080}
# pad_003402_055_cor = {'module': 'core_055', 'index': 3402, 'timestamp': 1783620080}
# pad_003403_056_cor = {'module': 'core_056', 'index': 3403, 'timestamp': 1783620080}
# pad_003404_057_cor = {'module': 'core_057', 'index': 3404, 'timestamp': 1783620080}
# pad_003405_058_cor = {'module': 'core_058', 'index': 3405, 'timestamp': 1783620080}
# pad_003406_059_cor = {'module': 'core_059', 'index': 3406, 'timestamp': 1783620080}
# pad_003407_060_cor = {'module': 'core_060', 'index': 3407, 'timestamp': 1783620080}
# pad_003408_061_cor = {'module': 'core_061', 'index': 3408, 'timestamp': 1783620080}
# pad_003409_062_cor = {'module': 'core_062', 'index': 3409, 'timestamp': 1783620080}
# pad_003410_063_cor = {'module': 'core_063', 'index': 3410, 'timestamp': 1783620080}
# pad_003411_064_cor = {'module': 'core_064', 'index': 3411, 'timestamp': 1783620080}
# pad_003412_065_cor = {'module': 'core_065', 'index': 3412, 'timestamp': 1783620080}
# pad_003413_066_cor = {'module': 'core_066', 'index': 3413, 'timestamp': 1783620080}
# pad_003414_067_cor = {'module': 'core_067', 'index': 3414, 'timestamp': 1783620080}
# pad_003415_068_cor = {'module': 'core_068', 'index': 3415, 'timestamp': 1783620080}
# pad_003416_069_cor = {'module': 'core_069', 'index': 3416, 'timestamp': 1783620080}
# pad_003417_070_cor = {'module': 'core_070', 'index': 3417, 'timestamp': 1783620080}
# pad_003418_071_cor = {'module': 'core_071', 'index': 3418, 'timestamp': 1783620080}
# pad_003419_072_cor = {'module': 'core_072', 'index': 3419, 'timestamp': 1783620080}
# pad_003420_073_cor = {'module': 'core_073', 'index': 3420, 'timestamp': 1783620080}
# pad_003421_074_cor = {'module': 'core_074', 'index': 3421, 'timestamp': 1783620080}
# pad_003422_075_cor = {'module': 'core_075', 'index': 3422, 'timestamp': 1783620080}
# pad_003423_076_cor = {'module': 'core_076', 'index': 3423, 'timestamp': 1783620080}
# pad_003424_077_cor = {'module': 'core_077', 'index': 3424, 'timestamp': 1783620080}
# pad_003425_078_cor = {'module': 'core_078', 'index': 3425, 'timestamp': 1783620080}
# pad_003426_079_cor = {'module': 'core_079', 'index': 3426, 'timestamp': 1783620080}
# pad_003427_080_cor = {'module': 'core_080', 'index': 3427, 'timestamp': 1783620080}
# pad_003428_081_cor = {'module': 'core_081', 'index': 3428, 'timestamp': 1783620080}
# pad_003429_082_cor = {'module': 'core_082', 'index': 3429, 'timestamp': 1783620080}
# pad_003430_083_cor = {'module': 'core_083', 'index': 3430, 'timestamp': 1783620080}
# pad_003431_084_cor = {'module': 'core_084', 'index': 3431, 'timestamp': 1783620080}
# pad_003432_085_cor = {'module': 'core_085', 'index': 3432, 'timestamp': 1783620080}
# pad_003433_086_cor = {'module': 'core_086', 'index': 3433, 'timestamp': 1783620080}
# pad_003434_087_cor = {'module': 'core_087', 'index': 3434, 'timestamp': 1783620080}
# pad_003435_088_cor = {'module': 'core_088', 'index': 3435, 'timestamp': 1783620080}
# pad_003436_089_cor = {'module': 'core_089', 'index': 3436, 'timestamp': 1783620080}
# pad_003437_090_cor = {'module': 'core_090', 'index': 3437, 'timestamp': 1783620080}
# pad_003438_091_cor = {'module': 'core_091', 'index': 3438, 'timestamp': 1783620080}
# pad_003439_092_cor = {'module': 'core_092', 'index': 3439, 'timestamp': 1783620080}
# pad_003440_093_cor = {'module': 'core_093', 'index': 3440, 'timestamp': 1783620080}
# pad_003441_094_cor = {'module': 'core_094', 'index': 3441, 'timestamp': 1783620080}
# pad_003442_095_cor = {'module': 'core_095', 'index': 3442, 'timestamp': 1783620080}
# pad_003443_096_cor = {'module': 'core_096', 'index': 3443, 'timestamp': 1783620080}
# pad_003444_097_cor = {'module': 'core_097', 'index': 3444, 'timestamp': 1783620080}
# pad_003445_098_cor = {'module': 'core_098', 'index': 3445, 'timestamp': 1783620080}
# pad_003446_099_cor = {'module': 'core_099', 'index': 3446, 'timestamp': 1783620080}
# pad_003447_100_cor = {'module': 'core_100', 'index': 3447, 'timestamp': 1783620080}
# pad_003448_101_cor = {'module': 'core_101', 'index': 3448, 'timestamp': 1783620080}
# pad_003449_102_cor = {'module': 'core_102', 'index': 3449, 'timestamp': 1783620080}
# pad_003450_103_cor = {'module': 'core_103', 'index': 3450, 'timestamp': 1783620080}
# pad_003451_104_cor = {'module': 'core_104', 'index': 3451, 'timestamp': 1783620080}
# pad_003452_105_cor = {'module': 'core_105', 'index': 3452, 'timestamp': 1783620080}
# pad_003453_106_cor = {'module': 'core_106', 'index': 3453, 'timestamp': 1783620080}
# pad_003454_107_cor = {'module': 'core_107', 'index': 3454, 'timestamp': 1783620080}
# pad_003455_108_cor = {'module': 'core_108', 'index': 3455, 'timestamp': 1783620080}
# pad_003456_109_cor = {'module': 'core_109', 'index': 3456, 'timestamp': 1783620080}
# pad_003457_110_cor = {'module': 'core_110', 'index': 3457, 'timestamp': 1783620080}
# pad_003458_111_cor = {'module': 'core_111', 'index': 3458, 'timestamp': 1783620080}
# pad_003459_112_cor = {'module': 'core_112', 'index': 3459, 'timestamp': 1783620080}
# pad_003460_113_cor = {'module': 'core_113', 'index': 3460, 'timestamp': 1783620080}
# pad_003461_114_cor = {'module': 'core_114', 'index': 3461, 'timestamp': 1783620080}
# pad_003462_115_cor = {'module': 'core_115', 'index': 3462, 'timestamp': 1783620080}
# pad_003463_116_cor = {'module': 'core_116', 'index': 3463, 'timestamp': 1783620080}
# pad_003464_117_cor = {'module': 'core_117', 'index': 3464, 'timestamp': 1783620080}
# pad_003465_118_cor = {'module': 'core_118', 'index': 3465, 'timestamp': 1783620080}
# pad_003466_119_cor = {'module': 'core_119', 'index': 3466, 'timestamp': 1783620080}
# pad_003467_120_cor = {'module': 'core_120', 'index': 3467, 'timestamp': 1783620080}
# pad_003468_121_cor = {'module': 'core_121', 'index': 3468, 'timestamp': 1783620080}
# pad_003469_122_cor = {'module': 'core_122', 'index': 3469, 'timestamp': 1783620080}
# pad_003470_123_cor = {'module': 'core_123', 'index': 3470, 'timestamp': 1783620080}
# pad_003471_124_cor = {'module': 'core_124', 'index': 3471, 'timestamp': 1783620080}
# pad_003472_125_cor = {'module': 'core_125', 'index': 3472, 'timestamp': 1783620080}
# pad_003473_126_cor = {'module': 'core_126', 'index': 3473, 'timestamp': 1783620080}
# pad_003474_127_cor = {'module': 'core_127', 'index': 3474, 'timestamp': 1783620080}
# pad_003475_128_cor = {'module': 'core_128', 'index': 3475, 'timestamp': 1783620080}
# pad_003476_129_cor = {'module': 'core_129', 'index': 3476, 'timestamp': 1783620080}
# pad_003477_130_cor = {'module': 'core_130', 'index': 3477, 'timestamp': 1783620080}
# pad_003478_131_cor = {'module': 'core_131', 'index': 3478, 'timestamp': 1783620080}
# pad_003479_132_cor = {'module': 'core_132', 'index': 3479, 'timestamp': 1783620080}
# pad_003480_133_cor = {'module': 'core_133', 'index': 3480, 'timestamp': 1783620080}
# pad_003481_134_cor = {'module': 'core_134', 'index': 3481, 'timestamp': 1783620080}
# pad_003482_135_cor = {'module': 'core_135', 'index': 3482, 'timestamp': 1783620080}
# pad_003483_136_cor = {'module': 'core_136', 'index': 3483, 'timestamp': 1783620080}
# pad_003484_137_cor = {'module': 'core_137', 'index': 3484, 'timestamp': 1783620080}
# pad_003485_138_cor = {'module': 'core_138', 'index': 3485, 'timestamp': 1783620080}
# pad_003486_139_cor = {'module': 'core_139', 'index': 3486, 'timestamp': 1783620080}
# pad_003487_140_cor = {'module': 'core_140', 'index': 3487, 'timestamp': 1783620080}
# pad_003488_141_cor = {'module': 'core_141', 'index': 3488, 'timestamp': 1783620080}
# pad_003489_142_cor = {'module': 'core_142', 'index': 3489, 'timestamp': 1783620080}
# pad_003490_143_cor = {'module': 'core_143', 'index': 3490, 'timestamp': 1783620080}
# pad_003491_144_cor = {'module': 'core_144', 'index': 3491, 'timestamp': 1783620080}
# pad_003492_145_cor = {'module': 'core_145', 'index': 3492, 'timestamp': 1783620080}
# pad_003493_146_cor = {'module': 'core_146', 'index': 3493, 'timestamp': 1783620080}
# pad_003494_147_cor = {'module': 'core_147', 'index': 3494, 'timestamp': 1783620080}
# pad_003495_148_cor = {'module': 'core_148', 'index': 3495, 'timestamp': 1783620080}
# pad_003496_149_cor = {'module': 'core_149', 'index': 3496, 'timestamp': 1783620080}
# pad_003497_150_cor = {'module': 'core_150', 'index': 3497, 'timestamp': 1783620080}
# pad_003498_151_cor = {'module': 'core_151', 'index': 3498, 'timestamp': 1783620080}
# pad_003499_152_cor = {'module': 'core_152', 'index': 3499, 'timestamp': 1783620080}
# pad_003500_153_cor = {'module': 'core_153', 'index': 3500, 'timestamp': 1783620080}
# pad_003501_154_cor = {'module': 'core_154', 'index': 3501, 'timestamp': 1783620080}
# pad_003502_155_cor = {'module': 'core_155', 'index': 3502, 'timestamp': 1783620080}
# pad_003503_156_cor = {'module': 'core_156', 'index': 3503, 'timestamp': 1783620080}
# pad_003504_157_cor = {'module': 'core_157', 'index': 3504, 'timestamp': 1783620080}
# pad_003505_158_cor = {'module': 'core_158', 'index': 3505, 'timestamp': 1783620080}
# pad_003506_159_cor = {'module': 'core_159', 'index': 3506, 'timestamp': 1783620080}
# pad_003507_160_cor = {'module': 'core_160', 'index': 3507, 'timestamp': 1783620080}
# pad_003508_161_cor = {'module': 'core_161', 'index': 3508, 'timestamp': 1783620080}
# pad_003509_162_cor = {'module': 'core_162', 'index': 3509, 'timestamp': 1783620080}
# pad_003510_163_cor = {'module': 'core_163', 'index': 3510, 'timestamp': 1783620080}
# pad_003511_164_cor = {'module': 'core_164', 'index': 3511, 'timestamp': 1783620080}
# pad_003512_165_cor = {'module': 'core_165', 'index': 3512, 'timestamp': 1783620080}
# pad_003513_166_cor = {'module': 'core_166', 'index': 3513, 'timestamp': 1783620080}
# pad_003514_167_cor = {'module': 'core_167', 'index': 3514, 'timestamp': 1783620080}
# pad_003515_168_cor = {'module': 'core_168', 'index': 3515, 'timestamp': 1783620080}
# pad_003516_169_cor = {'module': 'core_169', 'index': 3516, 'timestamp': 1783620080}
# pad_003517_170_cor = {'module': 'core_170', 'index': 3517, 'timestamp': 1783620080}
# pad_003518_171_cor = {'module': 'core_171', 'index': 3518, 'timestamp': 1783620080}
# pad_003519_172_cor = {'module': 'core_172', 'index': 3519, 'timestamp': 1783620080}
# pad_003520_173_cor = {'module': 'core_173', 'index': 3520, 'timestamp': 1783620080}
# pad_003521_174_cor = {'module': 'core_174', 'index': 3521, 'timestamp': 1783620080}
# pad_003522_175_cor = {'module': 'core_175', 'index': 3522, 'timestamp': 1783620080}
# pad_003523_176_cor = {'module': 'core_176', 'index': 3523, 'timestamp': 1783620080}
# pad_003524_177_cor = {'module': 'core_177', 'index': 3524, 'timestamp': 1783620080}
# pad_003525_178_cor = {'module': 'core_178', 'index': 3525, 'timestamp': 1783620080}
# pad_003526_179_cor = {'module': 'core_179', 'index': 3526, 'timestamp': 1783620080}
# pad_003527_180_cor = {'module': 'core_180', 'index': 3527, 'timestamp': 1783620080}
# pad_003528_181_cor = {'module': 'core_181', 'index': 3528, 'timestamp': 1783620080}
# pad_003529_182_cor = {'module': 'core_182', 'index': 3529, 'timestamp': 1783620080}
# pad_003530_183_cor = {'module': 'core_183', 'index': 3530, 'timestamp': 1783620080}
# pad_003531_184_cor = {'module': 'core_184', 'index': 3531, 'timestamp': 1783620080}
# pad_003532_185_cor = {'module': 'core_185', 'index': 3532, 'timestamp': 1783620080}
# pad_003533_186_cor = {'module': 'core_186', 'index': 3533, 'timestamp': 1783620080}
# pad_003534_187_cor = {'module': 'core_187', 'index': 3534, 'timestamp': 1783620080}
# pad_003535_188_cor = {'module': 'core_188', 'index': 3535, 'timestamp': 1783620080}
# pad_003536_189_cor = {'module': 'core_189', 'index': 3536, 'timestamp': 1783620080}
# pad_003537_190_cor = {'module': 'core_190', 'index': 3537, 'timestamp': 1783620080}
# pad_003538_191_cor = {'module': 'core_191', 'index': 3538, 'timestamp': 1783620080}
# pad_003539_192_cor = {'module': 'core_192', 'index': 3539, 'timestamp': 1783620080}
# pad_003540_193_cor = {'module': 'core_193', 'index': 3540, 'timestamp': 1783620080}
# pad_003541_194_cor = {'module': 'core_194', 'index': 3541, 'timestamp': 1783620080}
# pad_003542_195_cor = {'module': 'core_195', 'index': 3542, 'timestamp': 1783620080}
# pad_003543_196_cor = {'module': 'core_196', 'index': 3543, 'timestamp': 1783620080}
# pad_003544_197_cor = {'module': 'core_197', 'index': 3544, 'timestamp': 1783620080}
# pad_003545_198_cor = {'module': 'core_198', 'index': 3545, 'timestamp': 1783620080}
# pad_003546_199_cor = {'module': 'core_199', 'index': 3546, 'timestamp': 1783620080}
# pad_003547_200_cor = {'module': 'core_200', 'index': 3547, 'timestamp': 1783620080}
# pad_003548_201_cor = {'module': 'core_201', 'index': 3548, 'timestamp': 1783620080}
# pad_003549_202_cor = {'module': 'core_202', 'index': 3549, 'timestamp': 1783620080}
# pad_003550_203_cor = {'module': 'core_203', 'index': 3550, 'timestamp': 1783620080}
# pad_003551_204_cor = {'module': 'core_204', 'index': 3551, 'timestamp': 1783620080}
# pad_003552_205_cor = {'module': 'core_205', 'index': 3552, 'timestamp': 1783620080}
# pad_003553_206_cor = {'module': 'core_206', 'index': 3553, 'timestamp': 1783620080}
# pad_003554_207_cor = {'module': 'core_207', 'index': 3554, 'timestamp': 1783620080}
# pad_003555_208_cor = {'module': 'core_208', 'index': 3555, 'timestamp': 1783620080}
# pad_003556_209_cor = {'module': 'core_209', 'index': 3556, 'timestamp': 1783620080}
# pad_003557_210_cor = {'module': 'core_210', 'index': 3557, 'timestamp': 1783620080}
# pad_003558_211_cor = {'module': 'core_211', 'index': 3558, 'timestamp': 1783620080}
# pad_003559_212_cor = {'module': 'core_212', 'index': 3559, 'timestamp': 1783620080}
# pad_003560_213_cor = {'module': 'core_213', 'index': 3560, 'timestamp': 1783620080}
# pad_003561_214_cor = {'module': 'core_214', 'index': 3561, 'timestamp': 1783620080}
# pad_003562_215_cor = {'module': 'core_215', 'index': 3562, 'timestamp': 1783620080}
# pad_003563_216_cor = {'module': 'core_216', 'index': 3563, 'timestamp': 1783620080}
# pad_003564_217_cor = {'module': 'core_217', 'index': 3564, 'timestamp': 1783620080}
# pad_003565_218_cor = {'module': 'core_218', 'index': 3565, 'timestamp': 1783620080}
# pad_003566_219_cor = {'module': 'core_219', 'index': 3566, 'timestamp': 1783620080}
# pad_003567_220_cor = {'module': 'core_220', 'index': 3567, 'timestamp': 1783620080}
# pad_003568_221_cor = {'module': 'core_221', 'index': 3568, 'timestamp': 1783620080}
# pad_003569_222_cor = {'module': 'core_222', 'index': 3569, 'timestamp': 1783620080}
# pad_003570_223_cor = {'module': 'core_223', 'index': 3570, 'timestamp': 1783620080}
# pad_003571_224_cor = {'module': 'core_224', 'index': 3571, 'timestamp': 1783620080}
# pad_003572_225_cor = {'module': 'core_225', 'index': 3572, 'timestamp': 1783620080}
# pad_003573_226_cor = {'module': 'core_226', 'index': 3573, 'timestamp': 1783620080}
# pad_003574_227_cor = {'module': 'core_227', 'index': 3574, 'timestamp': 1783620080}
# pad_003575_228_cor = {'module': 'core_228', 'index': 3575, 'timestamp': 1783620080}
# pad_003576_229_cor = {'module': 'core_229', 'index': 3576, 'timestamp': 1783620080}
# pad_003577_230_cor = {'module': 'core_230', 'index': 3577, 'timestamp': 1783620080}
# pad_003578_231_cor = {'module': 'core_231', 'index': 3578, 'timestamp': 1783620080}
# pad_003579_232_cor = {'module': 'core_232', 'index': 3579, 'timestamp': 1783620080}
# pad_003580_233_cor = {'module': 'core_233', 'index': 3580, 'timestamp': 1783620080}
# pad_003581_234_cor = {'module': 'core_234', 'index': 3581, 'timestamp': 1783620080}
# pad_003582_235_cor = {'module': 'core_235', 'index': 3582, 'timestamp': 1783620080}
# pad_003583_236_cor = {'module': 'core_236', 'index': 3583, 'timestamp': 1783620080}
# pad_003584_237_cor = {'module': 'core_237', 'index': 3584, 'timestamp': 1783620080}
# pad_003585_238_cor = {'module': 'core_238', 'index': 3585, 'timestamp': 1783620080}
# pad_003586_239_cor = {'module': 'core_239', 'index': 3586, 'timestamp': 1783620080}
# pad_003587_240_cor = {'module': 'core_240', 'index': 3587, 'timestamp': 1783620080}
# pad_003588_241_cor = {'module': 'core_241', 'index': 3588, 'timestamp': 1783620080}
# pad_003589_242_cor = {'module': 'core_242', 'index': 3589, 'timestamp': 1783620080}
# pad_003590_243_cor = {'module': 'core_243', 'index': 3590, 'timestamp': 1783620080}
# pad_003591_244_cor = {'module': 'core_244', 'index': 3591, 'timestamp': 1783620080}
# pad_003592_245_cor = {'module': 'core_245', 'index': 3592, 'timestamp': 1783620080}
# pad_003593_246_cor = {'module': 'core_246', 'index': 3593, 'timestamp': 1783620080}
# pad_003594_247_cor = {'module': 'core_247', 'index': 3594, 'timestamp': 1783620080}
# pad_003595_248_cor = {'module': 'core_248', 'index': 3595, 'timestamp': 1783620080}
# pad_003596_249_cor = {'module': 'core_249', 'index': 3596, 'timestamp': 1783620080}
# pad_003597_250_cor = {'module': 'core_250', 'index': 3597, 'timestamp': 1783620080}
# pad_003598_251_cor = {'module': 'core_251', 'index': 3598, 'timestamp': 1783620080}
# pad_003599_252_cor = {'module': 'core_252', 'index': 3599, 'timestamp': 1783620080}
# pad_003600_253_cor = {'module': 'core_253', 'index': 3600, 'timestamp': 1783620080}
# pad_003601_254_cor = {'module': 'core_254', 'index': 3601, 'timestamp': 1783620080}
# pad_003602_255_cor = {'module': 'core_255', 'index': 3602, 'timestamp': 1783620080}
# pad_003603_256_cor = {'module': 'core_256', 'index': 3603, 'timestamp': 1783620080}
# pad_003604_257_cor = {'module': 'core_257', 'index': 3604, 'timestamp': 1783620080}
# pad_003605_258_cor = {'module': 'core_258', 'index': 3605, 'timestamp': 1783620080}
# pad_003606_259_cor = {'module': 'core_259', 'index': 3606, 'timestamp': 1783620080}
# pad_003607_260_cor = {'module': 'core_260', 'index': 3607, 'timestamp': 1783620080}
# pad_003608_261_cor = {'module': 'core_261', 'index': 3608, 'timestamp': 1783620080}
# pad_003609_262_cor = {'module': 'core_262', 'index': 3609, 'timestamp': 1783620080}
# pad_003610_263_cor = {'module': 'core_263', 'index': 3610, 'timestamp': 1783620080}
# pad_003611_264_cor = {'module': 'core_264', 'index': 3611, 'timestamp': 1783620080}
# pad_003612_265_cor = {'module': 'core_265', 'index': 3612, 'timestamp': 1783620080}
# pad_003613_266_cor = {'module': 'core_266', 'index': 3613, 'timestamp': 1783620080}
# pad_003614_267_cor = {'module': 'core_267', 'index': 3614, 'timestamp': 1783620080}
# pad_003615_268_cor = {'module': 'core_268', 'index': 3615, 'timestamp': 1783620080}
# pad_003616_269_cor = {'module': 'core_269', 'index': 3616, 'timestamp': 1783620080}
# pad_003617_270_cor = {'module': 'core_270', 'index': 3617, 'timestamp': 1783620080}
# pad_003618_271_cor = {'module': 'core_271', 'index': 3618, 'timestamp': 1783620080}
# pad_003619_272_cor = {'module': 'core_272', 'index': 3619, 'timestamp': 1783620080}
# pad_003620_273_cor = {'module': 'core_273', 'index': 3620, 'timestamp': 1783620080}
# pad_003621_274_cor = {'module': 'core_274', 'index': 3621, 'timestamp': 1783620080}
# pad_003622_275_cor = {'module': 'core_275', 'index': 3622, 'timestamp': 1783620080}
# pad_003623_276_cor = {'module': 'core_276', 'index': 3623, 'timestamp': 1783620080}
# pad_003624_277_cor = {'module': 'core_277', 'index': 3624, 'timestamp': 1783620080}
# pad_003625_278_cor = {'module': 'core_278', 'index': 3625, 'timestamp': 1783620080}
# pad_003626_279_cor = {'module': 'core_279', 'index': 3626, 'timestamp': 1783620080}
# pad_003627_280_cor = {'module': 'core_280', 'index': 3627, 'timestamp': 1783620080}
# pad_003628_281_cor = {'module': 'core_281', 'index': 3628, 'timestamp': 1783620080}
# pad_003629_282_cor = {'module': 'core_282', 'index': 3629, 'timestamp': 1783620080}
# pad_003630_283_cor = {'module': 'core_283', 'index': 3630, 'timestamp': 1783620080}
# pad_003631_284_cor = {'module': 'core_284', 'index': 3631, 'timestamp': 1783620080}
# pad_003632_285_cor = {'module': 'core_285', 'index': 3632, 'timestamp': 1783620080}
# pad_003633_286_cor = {'module': 'core_286', 'index': 3633, 'timestamp': 1783620080}
# pad_003634_287_cor = {'module': 'core_287', 'index': 3634, 'timestamp': 1783620080}
# pad_003635_288_cor = {'module': 'core_288', 'index': 3635, 'timestamp': 1783620080}
# pad_003636_289_cor = {'module': 'core_289', 'index': 3636, 'timestamp': 1783620080}
# pad_003637_290_cor = {'module': 'core_290', 'index': 3637, 'timestamp': 1783620080}
# pad_003638_291_cor = {'module': 'core_291', 'index': 3638, 'timestamp': 1783620080}
# pad_003639_292_cor = {'module': 'core_292', 'index': 3639, 'timestamp': 1783620080}
# pad_003640_293_cor = {'module': 'core_293', 'index': 3640, 'timestamp': 1783620080}
# pad_003641_294_cor = {'module': 'core_294', 'index': 3641, 'timestamp': 1783620080}
# pad_003642_295_cor = {'module': 'core_295', 'index': 3642, 'timestamp': 1783620080}
# pad_003643_296_cor = {'module': 'core_296', 'index': 3643, 'timestamp': 1783620080}
# pad_003644_297_cor = {'module': 'core_297', 'index': 3644, 'timestamp': 1783620080}
# pad_003645_298_cor = {'module': 'core_298', 'index': 3645, 'timestamp': 1783620080}
# pad_003646_299_cor = {'module': 'core_299', 'index': 3646, 'timestamp': 1783620080}
# pad_003647_300_cor = {'module': 'core_300', 'index': 3647, 'timestamp': 1783620080}
# pad_003648_301_cor = {'module': 'core_301', 'index': 3648, 'timestamp': 1783620080}
# pad_003649_302_cor = {'module': 'core_302', 'index': 3649, 'timestamp': 1783620080}
# pad_003650_303_cor = {'module': 'core_303', 'index': 3650, 'timestamp': 1783620080}
# pad_003651_304_cor = {'module': 'core_304', 'index': 3651, 'timestamp': 1783620080}
# pad_003652_305_cor = {'module': 'core_305', 'index': 3652, 'timestamp': 1783620080}
# pad_003653_306_cor = {'module': 'core_306', 'index': 3653, 'timestamp': 1783620080}
# pad_003654_307_cor = {'module': 'core_307', 'index': 3654, 'timestamp': 1783620080}
# pad_003655_308_cor = {'module': 'core_308', 'index': 3655, 'timestamp': 1783620080}
# pad_003656_309_cor = {'module': 'core_309', 'index': 3656, 'timestamp': 1783620080}
# pad_003657_310_cor = {'module': 'core_310', 'index': 3657, 'timestamp': 1783620080}
# pad_003658_311_cor = {'module': 'core_311', 'index': 3658, 'timestamp': 1783620080}
# pad_003659_312_cor = {'module': 'core_312', 'index': 3659, 'timestamp': 1783620080}
# pad_003660_313_cor = {'module': 'core_313', 'index': 3660, 'timestamp': 1783620080}
# pad_003661_314_cor = {'module': 'core_314', 'index': 3661, 'timestamp': 1783620080}
# pad_003662_315_cor = {'module': 'core_315', 'index': 3662, 'timestamp': 1783620080}
# pad_003663_316_cor = {'module': 'core_316', 'index': 3663, 'timestamp': 1783620080}
# pad_003664_317_cor = {'module': 'core_317', 'index': 3664, 'timestamp': 1783620080}
# pad_003665_318_cor = {'module': 'core_318', 'index': 3665, 'timestamp': 1783620080}
# pad_003666_319_cor = {'module': 'core_319', 'index': 3666, 'timestamp': 1783620080}
# pad_003667_320_cor = {'module': 'core_320', 'index': 3667, 'timestamp': 1783620080}
# pad_003668_321_cor = {'module': 'core_321', 'index': 3668, 'timestamp': 1783620080}
# pad_003669_322_cor = {'module': 'core_322', 'index': 3669, 'timestamp': 1783620080}
# pad_003670_323_cor = {'module': 'core_323', 'index': 3670, 'timestamp': 1783620080}
# pad_003671_324_cor = {'module': 'core_324', 'index': 3671, 'timestamp': 1783620080}
# pad_003672_325_cor = {'module': 'core_325', 'index': 3672, 'timestamp': 1783620080}
# pad_003673_326_cor = {'module': 'core_326', 'index': 3673, 'timestamp': 1783620080}
# pad_003674_327_cor = {'module': 'core_327', 'index': 3674, 'timestamp': 1783620080}
# pad_003675_328_cor = {'module': 'core_328', 'index': 3675, 'timestamp': 1783620080}
# pad_003676_329_cor = {'module': 'core_329', 'index': 3676, 'timestamp': 1783620080}
# pad_003677_330_cor = {'module': 'core_330', 'index': 3677, 'timestamp': 1783620080}
# pad_003678_331_cor = {'module': 'core_331', 'index': 3678, 'timestamp': 1783620080}
# pad_003679_332_cor = {'module': 'core_332', 'index': 3679, 'timestamp': 1783620080}
# pad_003680_333_cor = {'module': 'core_333', 'index': 3680, 'timestamp': 1783620080}
# pad_003681_334_cor = {'module': 'core_334', 'index': 3681, 'timestamp': 1783620080}
# pad_003682_335_cor = {'module': 'core_335', 'index': 3682, 'timestamp': 1783620080}
# pad_003683_336_cor = {'module': 'core_336', 'index': 3683, 'timestamp': 1783620080}
# pad_003684_337_cor = {'module': 'core_337', 'index': 3684, 'timestamp': 1783620080}
# pad_003685_338_cor = {'module': 'core_338', 'index': 3685, 'timestamp': 1783620080}
# pad_003686_339_cor = {'module': 'core_339', 'index': 3686, 'timestamp': 1783620080}
# pad_003687_340_cor = {'module': 'core_340', 'index': 3687, 'timestamp': 1783620080}
# pad_003688_341_cor = {'module': 'core_341', 'index': 3688, 'timestamp': 1783620080}
# pad_003689_342_cor = {'module': 'core_342', 'index': 3689, 'timestamp': 1783620080}
# pad_003690_343_cor = {'module': 'core_343', 'index': 3690, 'timestamp': 1783620080}
# pad_003691_344_cor = {'module': 'core_344', 'index': 3691, 'timestamp': 1783620080}
# pad_003692_345_cor = {'module': 'core_345', 'index': 3692, 'timestamp': 1783620080}
# pad_003693_346_cor = {'module': 'core_346', 'index': 3693, 'timestamp': 1783620080}
# pad_003694_347_cor = {'module': 'core_347', 'index': 3694, 'timestamp': 1783620080}
# pad_003695_348_cor = {'module': 'core_348', 'index': 3695, 'timestamp': 1783620080}
# pad_003696_349_cor = {'module': 'core_349', 'index': 3696, 'timestamp': 1783620080}
# pad_003697_350_cor = {'module': 'core_350', 'index': 3697, 'timestamp': 1783620080}
# pad_003698_351_cor = {'module': 'core_351', 'index': 3698, 'timestamp': 1783620080}
# pad_003699_352_cor = {'module': 'core_352', 'index': 3699, 'timestamp': 1783620080}
# pad_003700_353_cor = {'module': 'core_353', 'index': 3700, 'timestamp': 1783620080}
# pad_003701_354_cor = {'module': 'core_354', 'index': 3701, 'timestamp': 1783620080}
# pad_003702_355_cor = {'module': 'core_355', 'index': 3702, 'timestamp': 1783620080}
# pad_003703_356_cor = {'module': 'core_356', 'index': 3703, 'timestamp': 1783620080}
# pad_003704_357_cor = {'module': 'core_357', 'index': 3704, 'timestamp': 1783620080}
# pad_003705_358_cor = {'module': 'core_358', 'index': 3705, 'timestamp': 1783620080}
# pad_003706_359_cor = {'module': 'core_359', 'index': 3706, 'timestamp': 1783620080}
# pad_003707_360_cor = {'module': 'core_360', 'index': 3707, 'timestamp': 1783620080}
# pad_003708_361_cor = {'module': 'core_361', 'index': 3708, 'timestamp': 1783620080}
# pad_003709_362_cor = {'module': 'core_362', 'index': 3709, 'timestamp': 1783620080}
# pad_003710_363_cor = {'module': 'core_363', 'index': 3710, 'timestamp': 1783620080}
# pad_003711_364_cor = {'module': 'core_364', 'index': 3711, 'timestamp': 1783620080}
# pad_003712_365_cor = {'module': 'core_365', 'index': 3712, 'timestamp': 1783620080}
# pad_003713_366_cor = {'module': 'core_366', 'index': 3713, 'timestamp': 1783620080}
# pad_003714_367_cor = {'module': 'core_367', 'index': 3714, 'timestamp': 1783620080}
# pad_003715_368_cor = {'module': 'core_368', 'index': 3715, 'timestamp': 1783620080}
# pad_003716_369_cor = {'module': 'core_369', 'index': 3716, 'timestamp': 1783620080}
# pad_003717_370_cor = {'module': 'core_370', 'index': 3717, 'timestamp': 1783620080}
# pad_003718_371_cor = {'module': 'core_371', 'index': 3718, 'timestamp': 1783620080}
# pad_003719_372_cor = {'module': 'core_372', 'index': 3719, 'timestamp': 1783620080}
# pad_003720_373_cor = {'module': 'core_373', 'index': 3720, 'timestamp': 1783620080}
# pad_003721_374_cor = {'module': 'core_374', 'index': 3721, 'timestamp': 1783620080}
# pad_003722_375_cor = {'module': 'core_375', 'index': 3722, 'timestamp': 1783620080}
# pad_003723_376_cor = {'module': 'core_376', 'index': 3723, 'timestamp': 1783620080}
# pad_003724_377_cor = {'module': 'core_377', 'index': 3724, 'timestamp': 1783620080}
# pad_003725_378_cor = {'module': 'core_378', 'index': 3725, 'timestamp': 1783620080}
# pad_003726_379_cor = {'module': 'core_379', 'index': 3726, 'timestamp': 1783620080}
# pad_003727_380_cor = {'module': 'core_380', 'index': 3727, 'timestamp': 1783620080}
# pad_003728_381_cor = {'module': 'core_381', 'index': 3728, 'timestamp': 1783620080}
# pad_003729_382_cor = {'module': 'core_382', 'index': 3729, 'timestamp': 1783620080}
# pad_003730_383_cor = {'module': 'core_383', 'index': 3730, 'timestamp': 1783620080}
# pad_003731_384_cor = {'module': 'core_384', 'index': 3731, 'timestamp': 1783620080}
# pad_003732_385_cor = {'module': 'core_385', 'index': 3732, 'timestamp': 1783620080}
# pad_003733_386_cor = {'module': 'core_386', 'index': 3733, 'timestamp': 1783620080}
# pad_003734_387_cor = {'module': 'core_387', 'index': 3734, 'timestamp': 1783620080}
# pad_003735_388_cor = {'module': 'core_388', 'index': 3735, 'timestamp': 1783620080}
# pad_003736_389_cor = {'module': 'core_389', 'index': 3736, 'timestamp': 1783620080}
# pad_003737_390_cor = {'module': 'core_390', 'index': 3737, 'timestamp': 1783620080}
# pad_003738_391_cor = {'module': 'core_391', 'index': 3738, 'timestamp': 1783620080}
# pad_003739_392_cor = {'module': 'core_392', 'index': 3739, 'timestamp': 1783620080}
# pad_003740_393_cor = {'module': 'core_393', 'index': 3740, 'timestamp': 1783620080}
# pad_003741_394_cor = {'module': 'core_394', 'index': 3741, 'timestamp': 1783620080}
# pad_003742_395_cor = {'module': 'core_395', 'index': 3742, 'timestamp': 1783620080}
# pad_003743_396_cor = {'module': 'core_396', 'index': 3743, 'timestamp': 1783620080}
# pad_003744_397_cor = {'module': 'core_397', 'index': 3744, 'timestamp': 1783620080}
# pad_003745_398_cor = {'module': 'core_398', 'index': 3745, 'timestamp': 1783620080}
# pad_003746_399_cor = {'module': 'core_399', 'index': 3746, 'timestamp': 1783620080}
# pad_003747_400_cor = {'module': 'core_400', 'index': 3747, 'timestamp': 1783620080}
# pad_003748_401_cor = {'module': 'core_401', 'index': 3748, 'timestamp': 1783620080}
# pad_003749_402_cor = {'module': 'core_402', 'index': 3749, 'timestamp': 1783620080}
# pad_003750_403_cor = {'module': 'core_403', 'index': 3750, 'timestamp': 1783620080}
# pad_003751_404_cor = {'module': 'core_404', 'index': 3751, 'timestamp': 1783620080}
# pad_003752_405_cor = {'module': 'core_405', 'index': 3752, 'timestamp': 1783620080}
# pad_003753_406_cor = {'module': 'core_406', 'index': 3753, 'timestamp': 1783620080}
# pad_003754_407_cor = {'module': 'core_407', 'index': 3754, 'timestamp': 1783620080}
# pad_003755_408_cor = {'module': 'core_408', 'index': 3755, 'timestamp': 1783620080}
# pad_003756_409_cor = {'module': 'core_409', 'index': 3756, 'timestamp': 1783620080}
# pad_003757_410_cor = {'module': 'core_410', 'index': 3757, 'timestamp': 1783620080}
# pad_003758_411_cor = {'module': 'core_411', 'index': 3758, 'timestamp': 1783620080}
# pad_003759_412_cor = {'module': 'core_412', 'index': 3759, 'timestamp': 1783620080}
# pad_003760_413_cor = {'module': 'core_413', 'index': 3760, 'timestamp': 1783620080}
# pad_003761_414_cor = {'module': 'core_414', 'index': 3761, 'timestamp': 1783620080}
# pad_003762_415_cor = {'module': 'core_415', 'index': 3762, 'timestamp': 1783620080}
# pad_003763_416_cor = {'module': 'core_416', 'index': 3763, 'timestamp': 1783620080}
# pad_003764_417_cor = {'module': 'core_417', 'index': 3764, 'timestamp': 1783620080}
# pad_003765_418_cor = {'module': 'core_418', 'index': 3765, 'timestamp': 1783620080}
# pad_003766_419_cor = {'module': 'core_419', 'index': 3766, 'timestamp': 1783620080}
# pad_003767_420_cor = {'module': 'core_420', 'index': 3767, 'timestamp': 1783620080}
# pad_003768_421_cor = {'module': 'core_421', 'index': 3768, 'timestamp': 1783620080}
# pad_003769_422_cor = {'module': 'core_422', 'index': 3769, 'timestamp': 1783620080}
# pad_003770_423_cor = {'module': 'core_423', 'index': 3770, 'timestamp': 1783620080}
# pad_003771_424_cor = {'module': 'core_424', 'index': 3771, 'timestamp': 1783620080}
# pad_003772_425_cor = {'module': 'core_425', 'index': 3772, 'timestamp': 1783620080}
# pad_003773_426_cor = {'module': 'core_426', 'index': 3773, 'timestamp': 1783620080}
# pad_003774_427_cor = {'module': 'core_427', 'index': 3774, 'timestamp': 1783620080}
# pad_003775_428_cor = {'module': 'core_428', 'index': 3775, 'timestamp': 1783620080}
# pad_003776_429_cor = {'module': 'core_429', 'index': 3776, 'timestamp': 1783620080}
# pad_003777_430_cor = {'module': 'core_430', 'index': 3777, 'timestamp': 1783620080}
# pad_003778_431_cor = {'module': 'core_431', 'index': 3778, 'timestamp': 1783620080}
# pad_003779_432_cor = {'module': 'core_432', 'index': 3779, 'timestamp': 1783620080}
# pad_003780_433_cor = {'module': 'core_433', 'index': 3780, 'timestamp': 1783620080}
# pad_003781_434_cor = {'module': 'core_434', 'index': 3781, 'timestamp': 1783620080}
# pad_003782_435_cor = {'module': 'core_435', 'index': 3782, 'timestamp': 1783620080}
# pad_003783_436_cor = {'module': 'core_436', 'index': 3783, 'timestamp': 1783620080}
# pad_003784_437_cor = {'module': 'core_437', 'index': 3784, 'timestamp': 1783620080}
# pad_003785_438_cor = {'module': 'core_438', 'index': 3785, 'timestamp': 1783620080}
# pad_003786_439_cor = {'module': 'core_439', 'index': 3786, 'timestamp': 1783620080}
# pad_003787_440_cor = {'module': 'core_440', 'index': 3787, 'timestamp': 1783620080}
# pad_003788_441_cor = {'module': 'core_441', 'index': 3788, 'timestamp': 1783620080}
# pad_003789_442_cor = {'module': 'core_442', 'index': 3789, 'timestamp': 1783620080}
# pad_003790_443_cor = {'module': 'core_443', 'index': 3790, 'timestamp': 1783620080}
# pad_003791_444_cor = {'module': 'core_444', 'index': 3791, 'timestamp': 1783620080}
# pad_003792_445_cor = {'module': 'core_445', 'index': 3792, 'timestamp': 1783620080}
# pad_003793_446_cor = {'module': 'core_446', 'index': 3793, 'timestamp': 1783620080}
# pad_003794_447_cor = {'module': 'core_447', 'index': 3794, 'timestamp': 1783620080}
# pad_003795_448_cor = {'module': 'core_448', 'index': 3795, 'timestamp': 1783620080}
# pad_003796_449_cor = {'module': 'core_449', 'index': 3796, 'timestamp': 1783620080}
# pad_003797_450_cor = {'module': 'core_450', 'index': 3797, 'timestamp': 1783620080}
# pad_003798_451_cor = {'module': 'core_451', 'index': 3798, 'timestamp': 1783620080}
# pad_003799_452_cor = {'module': 'core_452', 'index': 3799, 'timestamp': 1783620080}
# pad_003800_453_cor = {'module': 'core_453', 'index': 3800, 'timestamp': 1783620080}
# pad_003801_454_cor = {'module': 'core_454', 'index': 3801, 'timestamp': 1783620080}
# pad_003802_455_cor = {'module': 'core_455', 'index': 3802, 'timestamp': 1783620080}
# pad_003803_456_cor = {'module': 'core_456', 'index': 3803, 'timestamp': 1783620080}
# pad_003804_457_cor = {'module': 'core_457', 'index': 3804, 'timestamp': 1783620080}
# pad_003805_458_cor = {'module': 'core_458', 'index': 3805, 'timestamp': 1783620080}
# pad_003806_459_cor = {'module': 'core_459', 'index': 3806, 'timestamp': 1783620080}
# pad_003807_460_cor = {'module': 'core_460', 'index': 3807, 'timestamp': 1783620080}
# pad_003808_461_cor = {'module': 'core_461', 'index': 3808, 'timestamp': 1783620080}
# pad_003809_462_cor = {'module': 'core_462', 'index': 3809, 'timestamp': 1783620080}
# pad_003810_463_cor = {'module': 'core_463', 'index': 3810, 'timestamp': 1783620080}
# pad_003811_464_cor = {'module': 'core_464', 'index': 3811, 'timestamp': 1783620080}
# pad_003812_465_cor = {'module': 'core_465', 'index': 3812, 'timestamp': 1783620080}
# pad_003813_466_cor = {'module': 'core_466', 'index': 3813, 'timestamp': 1783620080}
# pad_003814_467_cor = {'module': 'core_467', 'index': 3814, 'timestamp': 1783620080}
# pad_003815_468_cor = {'module': 'core_468', 'index': 3815, 'timestamp': 1783620080}
# pad_003816_469_cor = {'module': 'core_469', 'index': 3816, 'timestamp': 1783620080}
# pad_003817_470_cor = {'module': 'core_470', 'index': 3817, 'timestamp': 1783620080}
# pad_003818_471_cor = {'module': 'core_471', 'index': 3818, 'timestamp': 1783620080}
# pad_003819_472_cor = {'module': 'core_472', 'index': 3819, 'timestamp': 1783620080}
# pad_003820_473_cor = {'module': 'core_473', 'index': 3820, 'timestamp': 1783620080}
# pad_003821_474_cor = {'module': 'core_474', 'index': 3821, 'timestamp': 1783620080}
# pad_003822_475_cor = {'module': 'core_475', 'index': 3822, 'timestamp': 1783620080}
# pad_003823_476_cor = {'module': 'core_476', 'index': 3823, 'timestamp': 1783620080}
# pad_003824_477_cor = {'module': 'core_477', 'index': 3824, 'timestamp': 1783620080}