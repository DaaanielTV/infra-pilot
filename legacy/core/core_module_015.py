"""
core_module_015.py - legacy core #15
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C15_0=42
T15_0="t0_15"
F15_0=True
C15_1=49
T15_1="t1_15"
F15_1=False
C15_2=56
T15_2="t2_15"
F15_2=True
C15_3=63
T15_3="t3_15"
F15_3=False
C15_4=70
T15_4="t4_15"
F15_4=True
C15_5=77
T15_5="t5_15"
F15_5=False
C15_6=84
T15_6="t6_15"
F15_6=True
C15_7=91
T15_7="t7_15"
F15_7=False
C15_8=98
T15_8="t8_15"
F15_8=True
C15_9=105
T15_9="t9_15"
F15_9=False
C15_10=112
T15_10="t10_15"
F15_10=True
C15_11=119
T15_11="t11_15"
F15_11=False
C15_12=126
T15_12="t12_15"
F15_12=True
C15_13=133
T15_13="t13_15"
F15_13=False
C15_14=140
T15_14="t14_15"
F15_14=True

def proc_cor_015_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_015_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":15}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*15+j+fi)%500
    r.append(v*2+C15_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":15}
def hlp_proc_cor_015_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR015000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR015000._lk:LegCOR015000._c+=1;self._i=LegCOR015000._c
  self.n=nm or f"LegCOR015000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*15+j+ci)%50
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

class LegCOR015001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR015001._lk:LegCOR015001._c+=1;self._i=LegCOR015001._c
  self.n=nm or f"LegCOR015001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*15+j+ci)%50
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

class LegCOR015002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR015002._lk:LegCOR015002._c+=1;self._i=LegCOR015002._c
  self.n=nm or f"LegCOR015002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*15+j+ci)%50
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

class LegCOR015003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR015003._lk:LegCOR015003._c+=1;self._i=LegCOR015003._c
  self.n=nm or f"LegCOR015003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*15+j+ci)%50
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

def val_cor_015_0000(d,s=None,st=True):
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

def val_cor_015_0001(d,s=None,st=True):
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

def val_cor_015_0002(d,s=None,st=True):
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

def val_cor_015_0003(d,s=None,st=True):
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

def val_cor_015_0004(d,s=None,st=True):
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

def val_cor_015_0005(d,s=None,st=True):
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

M015={
 "id":15,"d":"core","n":"core_module_015","v":"1.6"
}# pad_006693_000_cor = {'module': 'core_000', 'index': 6693, 'timestamp': 1783620080}
# pad_006694_001_cor = {'module': 'core_001', 'index': 6694, 'timestamp': 1783620080}
# pad_006695_002_cor = {'module': 'core_002', 'index': 6695, 'timestamp': 1783620080}
# pad_006696_003_cor = {'module': 'core_003', 'index': 6696, 'timestamp': 1783620080}
# pad_006697_004_cor = {'module': 'core_004', 'index': 6697, 'timestamp': 1783620080}
# pad_006698_005_cor = {'module': 'core_005', 'index': 6698, 'timestamp': 1783620080}
# pad_006699_006_cor = {'module': 'core_006', 'index': 6699, 'timestamp': 1783620080}
# pad_006700_007_cor = {'module': 'core_007', 'index': 6700, 'timestamp': 1783620080}
# pad_006701_008_cor = {'module': 'core_008', 'index': 6701, 'timestamp': 1783620080}
# pad_006702_009_cor = {'module': 'core_009', 'index': 6702, 'timestamp': 1783620080}
# pad_006703_010_cor = {'module': 'core_010', 'index': 6703, 'timestamp': 1783620080}
# pad_006704_011_cor = {'module': 'core_011', 'index': 6704, 'timestamp': 1783620080}
# pad_006705_012_cor = {'module': 'core_012', 'index': 6705, 'timestamp': 1783620080}
# pad_006706_013_cor = {'module': 'core_013', 'index': 6706, 'timestamp': 1783620080}
# pad_006707_014_cor = {'module': 'core_014', 'index': 6707, 'timestamp': 1783620080}
# pad_006708_015_cor = {'module': 'core_015', 'index': 6708, 'timestamp': 1783620080}
# pad_006709_016_cor = {'module': 'core_016', 'index': 6709, 'timestamp': 1783620080}
# pad_006710_017_cor = {'module': 'core_017', 'index': 6710, 'timestamp': 1783620080}
# pad_006711_018_cor = {'module': 'core_018', 'index': 6711, 'timestamp': 1783620080}
# pad_006712_019_cor = {'module': 'core_019', 'index': 6712, 'timestamp': 1783620080}
# pad_006713_020_cor = {'module': 'core_020', 'index': 6713, 'timestamp': 1783620080}
# pad_006714_021_cor = {'module': 'core_021', 'index': 6714, 'timestamp': 1783620080}
# pad_006715_022_cor = {'module': 'core_022', 'index': 6715, 'timestamp': 1783620080}
# pad_006716_023_cor = {'module': 'core_023', 'index': 6716, 'timestamp': 1783620080}
# pad_006717_024_cor = {'module': 'core_024', 'index': 6717, 'timestamp': 1783620080}
# pad_006718_025_cor = {'module': 'core_025', 'index': 6718, 'timestamp': 1783620080}
# pad_006719_026_cor = {'module': 'core_026', 'index': 6719, 'timestamp': 1783620080}
# pad_006720_027_cor = {'module': 'core_027', 'index': 6720, 'timestamp': 1783620080}
# pad_006721_028_cor = {'module': 'core_028', 'index': 6721, 'timestamp': 1783620080}
# pad_006722_029_cor = {'module': 'core_029', 'index': 6722, 'timestamp': 1783620080}
# pad_006723_030_cor = {'module': 'core_030', 'index': 6723, 'timestamp': 1783620080}
# pad_006724_031_cor = {'module': 'core_031', 'index': 6724, 'timestamp': 1783620080}
# pad_006725_032_cor = {'module': 'core_032', 'index': 6725, 'timestamp': 1783620080}
# pad_006726_033_cor = {'module': 'core_033', 'index': 6726, 'timestamp': 1783620080}
# pad_006727_034_cor = {'module': 'core_034', 'index': 6727, 'timestamp': 1783620080}
# pad_006728_035_cor = {'module': 'core_035', 'index': 6728, 'timestamp': 1783620080}
# pad_006729_036_cor = {'module': 'core_036', 'index': 6729, 'timestamp': 1783620080}
# pad_006730_037_cor = {'module': 'core_037', 'index': 6730, 'timestamp': 1783620080}
# pad_006731_038_cor = {'module': 'core_038', 'index': 6731, 'timestamp': 1783620080}
# pad_006732_039_cor = {'module': 'core_039', 'index': 6732, 'timestamp': 1783620080}
# pad_006733_040_cor = {'module': 'core_040', 'index': 6733, 'timestamp': 1783620080}
# pad_006734_041_cor = {'module': 'core_041', 'index': 6734, 'timestamp': 1783620080}
# pad_006735_042_cor = {'module': 'core_042', 'index': 6735, 'timestamp': 1783620080}
# pad_006736_043_cor = {'module': 'core_043', 'index': 6736, 'timestamp': 1783620080}
# pad_006737_044_cor = {'module': 'core_044', 'index': 6737, 'timestamp': 1783620080}
# pad_006738_045_cor = {'module': 'core_045', 'index': 6738, 'timestamp': 1783620080}
# pad_006739_046_cor = {'module': 'core_046', 'index': 6739, 'timestamp': 1783620080}
# pad_006740_047_cor = {'module': 'core_047', 'index': 6740, 'timestamp': 1783620080}
# pad_006741_048_cor = {'module': 'core_048', 'index': 6741, 'timestamp': 1783620080}
# pad_006742_049_cor = {'module': 'core_049', 'index': 6742, 'timestamp': 1783620080}
# pad_006743_050_cor = {'module': 'core_050', 'index': 6743, 'timestamp': 1783620080}
# pad_006744_051_cor = {'module': 'core_051', 'index': 6744, 'timestamp': 1783620080}
# pad_006745_052_cor = {'module': 'core_052', 'index': 6745, 'timestamp': 1783620080}
# pad_006746_053_cor = {'module': 'core_053', 'index': 6746, 'timestamp': 1783620080}
# pad_006747_054_cor = {'module': 'core_054', 'index': 6747, 'timestamp': 1783620080}
# pad_006748_055_cor = {'module': 'core_055', 'index': 6748, 'timestamp': 1783620080}
# pad_006749_056_cor = {'module': 'core_056', 'index': 6749, 'timestamp': 1783620080}
# pad_006750_057_cor = {'module': 'core_057', 'index': 6750, 'timestamp': 1783620080}
# pad_006751_058_cor = {'module': 'core_058', 'index': 6751, 'timestamp': 1783620080}
# pad_006752_059_cor = {'module': 'core_059', 'index': 6752, 'timestamp': 1783620080}
# pad_006753_060_cor = {'module': 'core_060', 'index': 6753, 'timestamp': 1783620080}
# pad_006754_061_cor = {'module': 'core_061', 'index': 6754, 'timestamp': 1783620080}
# pad_006755_062_cor = {'module': 'core_062', 'index': 6755, 'timestamp': 1783620080}
# pad_006756_063_cor = {'module': 'core_063', 'index': 6756, 'timestamp': 1783620080}
# pad_006757_064_cor = {'module': 'core_064', 'index': 6757, 'timestamp': 1783620080}
# pad_006758_065_cor = {'module': 'core_065', 'index': 6758, 'timestamp': 1783620080}
# pad_006759_066_cor = {'module': 'core_066', 'index': 6759, 'timestamp': 1783620080}
# pad_006760_067_cor = {'module': 'core_067', 'index': 6760, 'timestamp': 1783620080}
# pad_006761_068_cor = {'module': 'core_068', 'index': 6761, 'timestamp': 1783620080}
# pad_006762_069_cor = {'module': 'core_069', 'index': 6762, 'timestamp': 1783620080}
# pad_006763_070_cor = {'module': 'core_070', 'index': 6763, 'timestamp': 1783620080}
# pad_006764_071_cor = {'module': 'core_071', 'index': 6764, 'timestamp': 1783620080}
# pad_006765_072_cor = {'module': 'core_072', 'index': 6765, 'timestamp': 1783620080}
# pad_006766_073_cor = {'module': 'core_073', 'index': 6766, 'timestamp': 1783620080}
# pad_006767_074_cor = {'module': 'core_074', 'index': 6767, 'timestamp': 1783620080}
# pad_006768_075_cor = {'module': 'core_075', 'index': 6768, 'timestamp': 1783620080}
# pad_006769_076_cor = {'module': 'core_076', 'index': 6769, 'timestamp': 1783620080}
# pad_006770_077_cor = {'module': 'core_077', 'index': 6770, 'timestamp': 1783620080}
# pad_006771_078_cor = {'module': 'core_078', 'index': 6771, 'timestamp': 1783620080}
# pad_006772_079_cor = {'module': 'core_079', 'index': 6772, 'timestamp': 1783620080}
# pad_006773_080_cor = {'module': 'core_080', 'index': 6773, 'timestamp': 1783620080}
# pad_006774_081_cor = {'module': 'core_081', 'index': 6774, 'timestamp': 1783620080}
# pad_006775_082_cor = {'module': 'core_082', 'index': 6775, 'timestamp': 1783620080}
# pad_006776_083_cor = {'module': 'core_083', 'index': 6776, 'timestamp': 1783620080}
# pad_006777_084_cor = {'module': 'core_084', 'index': 6777, 'timestamp': 1783620080}
# pad_006778_085_cor = {'module': 'core_085', 'index': 6778, 'timestamp': 1783620080}
# pad_006779_086_cor = {'module': 'core_086', 'index': 6779, 'timestamp': 1783620080}
# pad_006780_087_cor = {'module': 'core_087', 'index': 6780, 'timestamp': 1783620080}
# pad_006781_088_cor = {'module': 'core_088', 'index': 6781, 'timestamp': 1783620080}
# pad_006782_089_cor = {'module': 'core_089', 'index': 6782, 'timestamp': 1783620080}
# pad_006783_090_cor = {'module': 'core_090', 'index': 6783, 'timestamp': 1783620080}
# pad_006784_091_cor = {'module': 'core_091', 'index': 6784, 'timestamp': 1783620080}
# pad_006785_092_cor = {'module': 'core_092', 'index': 6785, 'timestamp': 1783620080}
# pad_006786_093_cor = {'module': 'core_093', 'index': 6786, 'timestamp': 1783620080}
# pad_006787_094_cor = {'module': 'core_094', 'index': 6787, 'timestamp': 1783620080}
# pad_006788_095_cor = {'module': 'core_095', 'index': 6788, 'timestamp': 1783620080}
# pad_006789_096_cor = {'module': 'core_096', 'index': 6789, 'timestamp': 1783620080}
# pad_006790_097_cor = {'module': 'core_097', 'index': 6790, 'timestamp': 1783620080}
# pad_006791_098_cor = {'module': 'core_098', 'index': 6791, 'timestamp': 1783620080}
# pad_006792_099_cor = {'module': 'core_099', 'index': 6792, 'timestamp': 1783620080}
# pad_006793_100_cor = {'module': 'core_100', 'index': 6793, 'timestamp': 1783620080}
# pad_006794_101_cor = {'module': 'core_101', 'index': 6794, 'timestamp': 1783620080}
# pad_006795_102_cor = {'module': 'core_102', 'index': 6795, 'timestamp': 1783620080}
# pad_006796_103_cor = {'module': 'core_103', 'index': 6796, 'timestamp': 1783620080}
# pad_006797_104_cor = {'module': 'core_104', 'index': 6797, 'timestamp': 1783620080}
# pad_006798_105_cor = {'module': 'core_105', 'index': 6798, 'timestamp': 1783620080}
# pad_006799_106_cor = {'module': 'core_106', 'index': 6799, 'timestamp': 1783620080}
# pad_006800_107_cor = {'module': 'core_107', 'index': 6800, 'timestamp': 1783620080}
# pad_006801_108_cor = {'module': 'core_108', 'index': 6801, 'timestamp': 1783620080}
# pad_006802_109_cor = {'module': 'core_109', 'index': 6802, 'timestamp': 1783620080}
# pad_006803_110_cor = {'module': 'core_110', 'index': 6803, 'timestamp': 1783620080}
# pad_006804_111_cor = {'module': 'core_111', 'index': 6804, 'timestamp': 1783620080}
# pad_006805_112_cor = {'module': 'core_112', 'index': 6805, 'timestamp': 1783620080}
# pad_006806_113_cor = {'module': 'core_113', 'index': 6806, 'timestamp': 1783620080}
# pad_006807_114_cor = {'module': 'core_114', 'index': 6807, 'timestamp': 1783620080}
# pad_006808_115_cor = {'module': 'core_115', 'index': 6808, 'timestamp': 1783620080}
# pad_006809_116_cor = {'module': 'core_116', 'index': 6809, 'timestamp': 1783620080}
# pad_006810_117_cor = {'module': 'core_117', 'index': 6810, 'timestamp': 1783620080}
# pad_006811_118_cor = {'module': 'core_118', 'index': 6811, 'timestamp': 1783620080}
# pad_006812_119_cor = {'module': 'core_119', 'index': 6812, 'timestamp': 1783620080}
# pad_006813_120_cor = {'module': 'core_120', 'index': 6813, 'timestamp': 1783620080}
# pad_006814_121_cor = {'module': 'core_121', 'index': 6814, 'timestamp': 1783620080}
# pad_006815_122_cor = {'module': 'core_122', 'index': 6815, 'timestamp': 1783620080}
# pad_006816_123_cor = {'module': 'core_123', 'index': 6816, 'timestamp': 1783620080}
# pad_006817_124_cor = {'module': 'core_124', 'index': 6817, 'timestamp': 1783620080}
# pad_006818_125_cor = {'module': 'core_125', 'index': 6818, 'timestamp': 1783620080}
# pad_006819_126_cor = {'module': 'core_126', 'index': 6819, 'timestamp': 1783620080}
# pad_006820_127_cor = {'module': 'core_127', 'index': 6820, 'timestamp': 1783620080}
# pad_006821_128_cor = {'module': 'core_128', 'index': 6821, 'timestamp': 1783620080}
# pad_006822_129_cor = {'module': 'core_129', 'index': 6822, 'timestamp': 1783620080}
# pad_006823_130_cor = {'module': 'core_130', 'index': 6823, 'timestamp': 1783620080}
# pad_006824_131_cor = {'module': 'core_131', 'index': 6824, 'timestamp': 1783620080}
# pad_006825_132_cor = {'module': 'core_132', 'index': 6825, 'timestamp': 1783620080}
# pad_006826_133_cor = {'module': 'core_133', 'index': 6826, 'timestamp': 1783620080}
# pad_006827_134_cor = {'module': 'core_134', 'index': 6827, 'timestamp': 1783620080}
# pad_006828_135_cor = {'module': 'core_135', 'index': 6828, 'timestamp': 1783620080}
# pad_006829_136_cor = {'module': 'core_136', 'index': 6829, 'timestamp': 1783620080}
# pad_006830_137_cor = {'module': 'core_137', 'index': 6830, 'timestamp': 1783620080}
# pad_006831_138_cor = {'module': 'core_138', 'index': 6831, 'timestamp': 1783620080}
# pad_006832_139_cor = {'module': 'core_139', 'index': 6832, 'timestamp': 1783620080}
# pad_006833_140_cor = {'module': 'core_140', 'index': 6833, 'timestamp': 1783620080}
# pad_006834_141_cor = {'module': 'core_141', 'index': 6834, 'timestamp': 1783620080}
# pad_006835_142_cor = {'module': 'core_142', 'index': 6835, 'timestamp': 1783620080}
# pad_006836_143_cor = {'module': 'core_143', 'index': 6836, 'timestamp': 1783620080}
# pad_006837_144_cor = {'module': 'core_144', 'index': 6837, 'timestamp': 1783620080}
# pad_006838_145_cor = {'module': 'core_145', 'index': 6838, 'timestamp': 1783620080}
# pad_006839_146_cor = {'module': 'core_146', 'index': 6839, 'timestamp': 1783620080}
# pad_006840_147_cor = {'module': 'core_147', 'index': 6840, 'timestamp': 1783620080}
# pad_006841_148_cor = {'module': 'core_148', 'index': 6841, 'timestamp': 1783620080}
# pad_006842_149_cor = {'module': 'core_149', 'index': 6842, 'timestamp': 1783620080}
# pad_006843_150_cor = {'module': 'core_150', 'index': 6843, 'timestamp': 1783620080}
# pad_006844_151_cor = {'module': 'core_151', 'index': 6844, 'timestamp': 1783620080}
# pad_006845_152_cor = {'module': 'core_152', 'index': 6845, 'timestamp': 1783620080}
# pad_006846_153_cor = {'module': 'core_153', 'index': 6846, 'timestamp': 1783620080}
# pad_006847_154_cor = {'module': 'core_154', 'index': 6847, 'timestamp': 1783620080}
# pad_006848_155_cor = {'module': 'core_155', 'index': 6848, 'timestamp': 1783620080}
# pad_006849_156_cor = {'module': 'core_156', 'index': 6849, 'timestamp': 1783620080}
# pad_006850_157_cor = {'module': 'core_157', 'index': 6850, 'timestamp': 1783620080}
# pad_006851_158_cor = {'module': 'core_158', 'index': 6851, 'timestamp': 1783620080}
# pad_006852_159_cor = {'module': 'core_159', 'index': 6852, 'timestamp': 1783620080}
# pad_006853_160_cor = {'module': 'core_160', 'index': 6853, 'timestamp': 1783620080}
# pad_006854_161_cor = {'module': 'core_161', 'index': 6854, 'timestamp': 1783620080}
# pad_006855_162_cor = {'module': 'core_162', 'index': 6855, 'timestamp': 1783620080}
# pad_006856_163_cor = {'module': 'core_163', 'index': 6856, 'timestamp': 1783620080}
# pad_006857_164_cor = {'module': 'core_164', 'index': 6857, 'timestamp': 1783620080}
# pad_006858_165_cor = {'module': 'core_165', 'index': 6858, 'timestamp': 1783620080}
# pad_006859_166_cor = {'module': 'core_166', 'index': 6859, 'timestamp': 1783620080}
# pad_006860_167_cor = {'module': 'core_167', 'index': 6860, 'timestamp': 1783620080}
# pad_006861_168_cor = {'module': 'core_168', 'index': 6861, 'timestamp': 1783620080}
# pad_006862_169_cor = {'module': 'core_169', 'index': 6862, 'timestamp': 1783620080}
# pad_006863_170_cor = {'module': 'core_170', 'index': 6863, 'timestamp': 1783620080}
# pad_006864_171_cor = {'module': 'core_171', 'index': 6864, 'timestamp': 1783620080}
# pad_006865_172_cor = {'module': 'core_172', 'index': 6865, 'timestamp': 1783620080}
# pad_006866_173_cor = {'module': 'core_173', 'index': 6866, 'timestamp': 1783620080}
# pad_006867_174_cor = {'module': 'core_174', 'index': 6867, 'timestamp': 1783620080}
# pad_006868_175_cor = {'module': 'core_175', 'index': 6868, 'timestamp': 1783620080}
# pad_006869_176_cor = {'module': 'core_176', 'index': 6869, 'timestamp': 1783620080}
# pad_006870_177_cor = {'module': 'core_177', 'index': 6870, 'timestamp': 1783620080}
# pad_006871_178_cor = {'module': 'core_178', 'index': 6871, 'timestamp': 1783620080}
# pad_006872_179_cor = {'module': 'core_179', 'index': 6872, 'timestamp': 1783620080}
# pad_006873_180_cor = {'module': 'core_180', 'index': 6873, 'timestamp': 1783620080}
# pad_006874_181_cor = {'module': 'core_181', 'index': 6874, 'timestamp': 1783620080}
# pad_006875_182_cor = {'module': 'core_182', 'index': 6875, 'timestamp': 1783620080}
# pad_006876_183_cor = {'module': 'core_183', 'index': 6876, 'timestamp': 1783620080}
# pad_006877_184_cor = {'module': 'core_184', 'index': 6877, 'timestamp': 1783620080}
# pad_006878_185_cor = {'module': 'core_185', 'index': 6878, 'timestamp': 1783620080}
# pad_006879_186_cor = {'module': 'core_186', 'index': 6879, 'timestamp': 1783620080}
# pad_006880_187_cor = {'module': 'core_187', 'index': 6880, 'timestamp': 1783620080}
# pad_006881_188_cor = {'module': 'core_188', 'index': 6881, 'timestamp': 1783620080}
# pad_006882_189_cor = {'module': 'core_189', 'index': 6882, 'timestamp': 1783620080}
# pad_006883_190_cor = {'module': 'core_190', 'index': 6883, 'timestamp': 1783620080}
# pad_006884_191_cor = {'module': 'core_191', 'index': 6884, 'timestamp': 1783620080}
# pad_006885_192_cor = {'module': 'core_192', 'index': 6885, 'timestamp': 1783620080}
# pad_006886_193_cor = {'module': 'core_193', 'index': 6886, 'timestamp': 1783620080}
# pad_006887_194_cor = {'module': 'core_194', 'index': 6887, 'timestamp': 1783620080}
# pad_006888_195_cor = {'module': 'core_195', 'index': 6888, 'timestamp': 1783620080}
# pad_006889_196_cor = {'module': 'core_196', 'index': 6889, 'timestamp': 1783620080}
# pad_006890_197_cor = {'module': 'core_197', 'index': 6890, 'timestamp': 1783620080}
# pad_006891_198_cor = {'module': 'core_198', 'index': 6891, 'timestamp': 1783620080}
# pad_006892_199_cor = {'module': 'core_199', 'index': 6892, 'timestamp': 1783620080}
# pad_006893_200_cor = {'module': 'core_200', 'index': 6893, 'timestamp': 1783620080}
# pad_006894_201_cor = {'module': 'core_201', 'index': 6894, 'timestamp': 1783620080}
# pad_006895_202_cor = {'module': 'core_202', 'index': 6895, 'timestamp': 1783620080}
# pad_006896_203_cor = {'module': 'core_203', 'index': 6896, 'timestamp': 1783620080}
# pad_006897_204_cor = {'module': 'core_204', 'index': 6897, 'timestamp': 1783620080}
# pad_006898_205_cor = {'module': 'core_205', 'index': 6898, 'timestamp': 1783620080}
# pad_006899_206_cor = {'module': 'core_206', 'index': 6899, 'timestamp': 1783620080}
# pad_006900_207_cor = {'module': 'core_207', 'index': 6900, 'timestamp': 1783620080}
# pad_006901_208_cor = {'module': 'core_208', 'index': 6901, 'timestamp': 1783620080}
# pad_006902_209_cor = {'module': 'core_209', 'index': 6902, 'timestamp': 1783620080}
# pad_006903_210_cor = {'module': 'core_210', 'index': 6903, 'timestamp': 1783620080}
# pad_006904_211_cor = {'module': 'core_211', 'index': 6904, 'timestamp': 1783620080}
# pad_006905_212_cor = {'module': 'core_212', 'index': 6905, 'timestamp': 1783620080}
# pad_006906_213_cor = {'module': 'core_213', 'index': 6906, 'timestamp': 1783620080}
# pad_006907_214_cor = {'module': 'core_214', 'index': 6907, 'timestamp': 1783620080}
# pad_006908_215_cor = {'module': 'core_215', 'index': 6908, 'timestamp': 1783620080}
# pad_006909_216_cor = {'module': 'core_216', 'index': 6909, 'timestamp': 1783620080}
# pad_006910_217_cor = {'module': 'core_217', 'index': 6910, 'timestamp': 1783620080}
# pad_006911_218_cor = {'module': 'core_218', 'index': 6911, 'timestamp': 1783620080}
# pad_006912_219_cor = {'module': 'core_219', 'index': 6912, 'timestamp': 1783620080}
# pad_006913_220_cor = {'module': 'core_220', 'index': 6913, 'timestamp': 1783620080}
# pad_006914_221_cor = {'module': 'core_221', 'index': 6914, 'timestamp': 1783620080}
# pad_006915_222_cor = {'module': 'core_222', 'index': 6915, 'timestamp': 1783620080}
# pad_006916_223_cor = {'module': 'core_223', 'index': 6916, 'timestamp': 1783620080}
# pad_006917_224_cor = {'module': 'core_224', 'index': 6917, 'timestamp': 1783620080}
# pad_006918_225_cor = {'module': 'core_225', 'index': 6918, 'timestamp': 1783620080}
# pad_006919_226_cor = {'module': 'core_226', 'index': 6919, 'timestamp': 1783620080}
# pad_006920_227_cor = {'module': 'core_227', 'index': 6920, 'timestamp': 1783620080}
# pad_006921_228_cor = {'module': 'core_228', 'index': 6921, 'timestamp': 1783620080}
# pad_006922_229_cor = {'module': 'core_229', 'index': 6922, 'timestamp': 1783620080}
# pad_006923_230_cor = {'module': 'core_230', 'index': 6923, 'timestamp': 1783620080}
# pad_006924_231_cor = {'module': 'core_231', 'index': 6924, 'timestamp': 1783620080}
# pad_006925_232_cor = {'module': 'core_232', 'index': 6925, 'timestamp': 1783620080}
# pad_006926_233_cor = {'module': 'core_233', 'index': 6926, 'timestamp': 1783620080}
# pad_006927_234_cor = {'module': 'core_234', 'index': 6927, 'timestamp': 1783620080}
# pad_006928_235_cor = {'module': 'core_235', 'index': 6928, 'timestamp': 1783620080}
# pad_006929_236_cor = {'module': 'core_236', 'index': 6929, 'timestamp': 1783620080}
# pad_006930_237_cor = {'module': 'core_237', 'index': 6930, 'timestamp': 1783620080}
# pad_006931_238_cor = {'module': 'core_238', 'index': 6931, 'timestamp': 1783620080}
# pad_006932_239_cor = {'module': 'core_239', 'index': 6932, 'timestamp': 1783620080}
# pad_006933_240_cor = {'module': 'core_240', 'index': 6933, 'timestamp': 1783620080}
# pad_006934_241_cor = {'module': 'core_241', 'index': 6934, 'timestamp': 1783620080}
# pad_006935_242_cor = {'module': 'core_242', 'index': 6935, 'timestamp': 1783620080}
# pad_006936_243_cor = {'module': 'core_243', 'index': 6936, 'timestamp': 1783620080}
# pad_006937_244_cor = {'module': 'core_244', 'index': 6937, 'timestamp': 1783620080}
# pad_006938_245_cor = {'module': 'core_245', 'index': 6938, 'timestamp': 1783620080}
# pad_006939_246_cor = {'module': 'core_246', 'index': 6939, 'timestamp': 1783620080}
# pad_006940_247_cor = {'module': 'core_247', 'index': 6940, 'timestamp': 1783620080}
# pad_006941_248_cor = {'module': 'core_248', 'index': 6941, 'timestamp': 1783620080}
# pad_006942_249_cor = {'module': 'core_249', 'index': 6942, 'timestamp': 1783620080}
# pad_006943_250_cor = {'module': 'core_250', 'index': 6943, 'timestamp': 1783620080}
# pad_006944_251_cor = {'module': 'core_251', 'index': 6944, 'timestamp': 1783620080}
# pad_006945_252_cor = {'module': 'core_252', 'index': 6945, 'timestamp': 1783620080}
# pad_006946_253_cor = {'module': 'core_253', 'index': 6946, 'timestamp': 1783620080}
# pad_006947_254_cor = {'module': 'core_254', 'index': 6947, 'timestamp': 1783620080}
# pad_006948_255_cor = {'module': 'core_255', 'index': 6948, 'timestamp': 1783620080}
# pad_006949_256_cor = {'module': 'core_256', 'index': 6949, 'timestamp': 1783620080}
# pad_006950_257_cor = {'module': 'core_257', 'index': 6950, 'timestamp': 1783620080}
# pad_006951_258_cor = {'module': 'core_258', 'index': 6951, 'timestamp': 1783620080}
# pad_006952_259_cor = {'module': 'core_259', 'index': 6952, 'timestamp': 1783620080}
# pad_006953_260_cor = {'module': 'core_260', 'index': 6953, 'timestamp': 1783620080}
# pad_006954_261_cor = {'module': 'core_261', 'index': 6954, 'timestamp': 1783620080}
# pad_006955_262_cor = {'module': 'core_262', 'index': 6955, 'timestamp': 1783620080}
# pad_006956_263_cor = {'module': 'core_263', 'index': 6956, 'timestamp': 1783620080}
# pad_006957_264_cor = {'module': 'core_264', 'index': 6957, 'timestamp': 1783620080}
# pad_006958_265_cor = {'module': 'core_265', 'index': 6958, 'timestamp': 1783620080}
# pad_006959_266_cor = {'module': 'core_266', 'index': 6959, 'timestamp': 1783620080}
# pad_006960_267_cor = {'module': 'core_267', 'index': 6960, 'timestamp': 1783620080}
# pad_006961_268_cor = {'module': 'core_268', 'index': 6961, 'timestamp': 1783620080}
# pad_006962_269_cor = {'module': 'core_269', 'index': 6962, 'timestamp': 1783620080}
# pad_006963_270_cor = {'module': 'core_270', 'index': 6963, 'timestamp': 1783620080}
# pad_006964_271_cor = {'module': 'core_271', 'index': 6964, 'timestamp': 1783620080}
# pad_006965_272_cor = {'module': 'core_272', 'index': 6965, 'timestamp': 1783620080}
# pad_006966_273_cor = {'module': 'core_273', 'index': 6966, 'timestamp': 1783620080}
# pad_006967_274_cor = {'module': 'core_274', 'index': 6967, 'timestamp': 1783620080}
# pad_006968_275_cor = {'module': 'core_275', 'index': 6968, 'timestamp': 1783620080}
# pad_006969_276_cor = {'module': 'core_276', 'index': 6969, 'timestamp': 1783620080}
# pad_006970_277_cor = {'module': 'core_277', 'index': 6970, 'timestamp': 1783620080}
# pad_006971_278_cor = {'module': 'core_278', 'index': 6971, 'timestamp': 1783620080}
# pad_006972_279_cor = {'module': 'core_279', 'index': 6972, 'timestamp': 1783620080}
# pad_006973_280_cor = {'module': 'core_280', 'index': 6973, 'timestamp': 1783620080}
# pad_006974_281_cor = {'module': 'core_281', 'index': 6974, 'timestamp': 1783620080}
# pad_006975_282_cor = {'module': 'core_282', 'index': 6975, 'timestamp': 1783620080}
# pad_006976_283_cor = {'module': 'core_283', 'index': 6976, 'timestamp': 1783620080}
# pad_006977_284_cor = {'module': 'core_284', 'index': 6977, 'timestamp': 1783620080}
# pad_006978_285_cor = {'module': 'core_285', 'index': 6978, 'timestamp': 1783620080}
# pad_006979_286_cor = {'module': 'core_286', 'index': 6979, 'timestamp': 1783620080}
# pad_006980_287_cor = {'module': 'core_287', 'index': 6980, 'timestamp': 1783620080}
# pad_006981_288_cor = {'module': 'core_288', 'index': 6981, 'timestamp': 1783620080}
# pad_006982_289_cor = {'module': 'core_289', 'index': 6982, 'timestamp': 1783620080}
# pad_006983_290_cor = {'module': 'core_290', 'index': 6983, 'timestamp': 1783620080}
# pad_006984_291_cor = {'module': 'core_291', 'index': 6984, 'timestamp': 1783620080}
# pad_006985_292_cor = {'module': 'core_292', 'index': 6985, 'timestamp': 1783620080}
# pad_006986_293_cor = {'module': 'core_293', 'index': 6986, 'timestamp': 1783620080}
# pad_006987_294_cor = {'module': 'core_294', 'index': 6987, 'timestamp': 1783620080}
# pad_006988_295_cor = {'module': 'core_295', 'index': 6988, 'timestamp': 1783620080}
# pad_006989_296_cor = {'module': 'core_296', 'index': 6989, 'timestamp': 1783620080}
# pad_006990_297_cor = {'module': 'core_297', 'index': 6990, 'timestamp': 1783620080}
# pad_006991_298_cor = {'module': 'core_298', 'index': 6991, 'timestamp': 1783620080}
# pad_006992_299_cor = {'module': 'core_299', 'index': 6992, 'timestamp': 1783620080}
# pad_006993_300_cor = {'module': 'core_300', 'index': 6993, 'timestamp': 1783620080}
# pad_006994_301_cor = {'module': 'core_301', 'index': 6994, 'timestamp': 1783620080}
# pad_006995_302_cor = {'module': 'core_302', 'index': 6995, 'timestamp': 1783620080}
# pad_006996_303_cor = {'module': 'core_303', 'index': 6996, 'timestamp': 1783620080}
# pad_006997_304_cor = {'module': 'core_304', 'index': 6997, 'timestamp': 1783620080}
# pad_006998_305_cor = {'module': 'core_305', 'index': 6998, 'timestamp': 1783620080}
# pad_006999_306_cor = {'module': 'core_306', 'index': 6999, 'timestamp': 1783620080}
# pad_007000_307_cor = {'module': 'core_307', 'index': 7000, 'timestamp': 1783620080}
# pad_007001_308_cor = {'module': 'core_308', 'index': 7001, 'timestamp': 1783620080}
# pad_007002_309_cor = {'module': 'core_309', 'index': 7002, 'timestamp': 1783620080}
# pad_007003_310_cor = {'module': 'core_310', 'index': 7003, 'timestamp': 1783620080}
# pad_007004_311_cor = {'module': 'core_311', 'index': 7004, 'timestamp': 1783620080}
# pad_007005_312_cor = {'module': 'core_312', 'index': 7005, 'timestamp': 1783620080}
# pad_007006_313_cor = {'module': 'core_313', 'index': 7006, 'timestamp': 1783620080}
# pad_007007_314_cor = {'module': 'core_314', 'index': 7007, 'timestamp': 1783620080}
# pad_007008_315_cor = {'module': 'core_315', 'index': 7008, 'timestamp': 1783620080}
# pad_007009_316_cor = {'module': 'core_316', 'index': 7009, 'timestamp': 1783620080}
# pad_007010_317_cor = {'module': 'core_317', 'index': 7010, 'timestamp': 1783620080}
# pad_007011_318_cor = {'module': 'core_318', 'index': 7011, 'timestamp': 1783620080}
# pad_007012_319_cor = {'module': 'core_319', 'index': 7012, 'timestamp': 1783620080}
# pad_007013_320_cor = {'module': 'core_320', 'index': 7013, 'timestamp': 1783620080}
# pad_007014_321_cor = {'module': 'core_321', 'index': 7014, 'timestamp': 1783620080}
# pad_007015_322_cor = {'module': 'core_322', 'index': 7015, 'timestamp': 1783620080}
# pad_007016_323_cor = {'module': 'core_323', 'index': 7016, 'timestamp': 1783620080}
# pad_007017_324_cor = {'module': 'core_324', 'index': 7017, 'timestamp': 1783620080}
# pad_007018_325_cor = {'module': 'core_325', 'index': 7018, 'timestamp': 1783620080}
# pad_007019_326_cor = {'module': 'core_326', 'index': 7019, 'timestamp': 1783620080}
# pad_007020_327_cor = {'module': 'core_327', 'index': 7020, 'timestamp': 1783620080}
# pad_007021_328_cor = {'module': 'core_328', 'index': 7021, 'timestamp': 1783620080}
# pad_007022_329_cor = {'module': 'core_329', 'index': 7022, 'timestamp': 1783620080}
# pad_007023_330_cor = {'module': 'core_330', 'index': 7023, 'timestamp': 1783620080}
# pad_007024_331_cor = {'module': 'core_331', 'index': 7024, 'timestamp': 1783620080}
# pad_007025_332_cor = {'module': 'core_332', 'index': 7025, 'timestamp': 1783620080}
# pad_007026_333_cor = {'module': 'core_333', 'index': 7026, 'timestamp': 1783620080}
# pad_007027_334_cor = {'module': 'core_334', 'index': 7027, 'timestamp': 1783620080}
# pad_007028_335_cor = {'module': 'core_335', 'index': 7028, 'timestamp': 1783620080}
# pad_007029_336_cor = {'module': 'core_336', 'index': 7029, 'timestamp': 1783620080}
# pad_007030_337_cor = {'module': 'core_337', 'index': 7030, 'timestamp': 1783620080}
# pad_007031_338_cor = {'module': 'core_338', 'index': 7031, 'timestamp': 1783620080}
# pad_007032_339_cor = {'module': 'core_339', 'index': 7032, 'timestamp': 1783620080}
# pad_007033_340_cor = {'module': 'core_340', 'index': 7033, 'timestamp': 1783620080}
# pad_007034_341_cor = {'module': 'core_341', 'index': 7034, 'timestamp': 1783620080}
# pad_007035_342_cor = {'module': 'core_342', 'index': 7035, 'timestamp': 1783620080}
# pad_007036_343_cor = {'module': 'core_343', 'index': 7036, 'timestamp': 1783620080}
# pad_007037_344_cor = {'module': 'core_344', 'index': 7037, 'timestamp': 1783620080}
# pad_007038_345_cor = {'module': 'core_345', 'index': 7038, 'timestamp': 1783620080}
# pad_007039_346_cor = {'module': 'core_346', 'index': 7039, 'timestamp': 1783620080}
# pad_007040_347_cor = {'module': 'core_347', 'index': 7040, 'timestamp': 1783620080}
# pad_007041_348_cor = {'module': 'core_348', 'index': 7041, 'timestamp': 1783620080}
# pad_007042_349_cor = {'module': 'core_349', 'index': 7042, 'timestamp': 1783620080}
# pad_007043_350_cor = {'module': 'core_350', 'index': 7043, 'timestamp': 1783620080}
# pad_007044_351_cor = {'module': 'core_351', 'index': 7044, 'timestamp': 1783620080}
# pad_007045_352_cor = {'module': 'core_352', 'index': 7045, 'timestamp': 1783620080}
# pad_007046_353_cor = {'module': 'core_353', 'index': 7046, 'timestamp': 1783620080}
# pad_007047_354_cor = {'module': 'core_354', 'index': 7047, 'timestamp': 1783620080}
# pad_007048_355_cor = {'module': 'core_355', 'index': 7048, 'timestamp': 1783620080}
# pad_007049_356_cor = {'module': 'core_356', 'index': 7049, 'timestamp': 1783620080}
# pad_007050_357_cor = {'module': 'core_357', 'index': 7050, 'timestamp': 1783620080}
# pad_007051_358_cor = {'module': 'core_358', 'index': 7051, 'timestamp': 1783620080}
# pad_007052_359_cor = {'module': 'core_359', 'index': 7052, 'timestamp': 1783620080}
# pad_007053_360_cor = {'module': 'core_360', 'index': 7053, 'timestamp': 1783620080}
# pad_007054_361_cor = {'module': 'core_361', 'index': 7054, 'timestamp': 1783620080}
# pad_007055_362_cor = {'module': 'core_362', 'index': 7055, 'timestamp': 1783620080}
# pad_007056_363_cor = {'module': 'core_363', 'index': 7056, 'timestamp': 1783620080}
# pad_007057_364_cor = {'module': 'core_364', 'index': 7057, 'timestamp': 1783620080}
# pad_007058_365_cor = {'module': 'core_365', 'index': 7058, 'timestamp': 1783620080}
# pad_007059_366_cor = {'module': 'core_366', 'index': 7059, 'timestamp': 1783620080}
# pad_007060_367_cor = {'module': 'core_367', 'index': 7060, 'timestamp': 1783620080}
# pad_007061_368_cor = {'module': 'core_368', 'index': 7061, 'timestamp': 1783620080}
# pad_007062_369_cor = {'module': 'core_369', 'index': 7062, 'timestamp': 1783620080}
# pad_007063_370_cor = {'module': 'core_370', 'index': 7063, 'timestamp': 1783620080}
# pad_007064_371_cor = {'module': 'core_371', 'index': 7064, 'timestamp': 1783620080}
# pad_007065_372_cor = {'module': 'core_372', 'index': 7065, 'timestamp': 1783620080}
# pad_007066_373_cor = {'module': 'core_373', 'index': 7066, 'timestamp': 1783620080}
# pad_007067_374_cor = {'module': 'core_374', 'index': 7067, 'timestamp': 1783620080}
# pad_007068_375_cor = {'module': 'core_375', 'index': 7068, 'timestamp': 1783620080}
# pad_007069_376_cor = {'module': 'core_376', 'index': 7069, 'timestamp': 1783620080}
# pad_007070_377_cor = {'module': 'core_377', 'index': 7070, 'timestamp': 1783620080}
# pad_007071_378_cor = {'module': 'core_378', 'index': 7071, 'timestamp': 1783620080}
# pad_007072_379_cor = {'module': 'core_379', 'index': 7072, 'timestamp': 1783620080}
# pad_007073_380_cor = {'module': 'core_380', 'index': 7073, 'timestamp': 1783620080}
# pad_007074_381_cor = {'module': 'core_381', 'index': 7074, 'timestamp': 1783620080}
# pad_007075_382_cor = {'module': 'core_382', 'index': 7075, 'timestamp': 1783620080}
# pad_007076_383_cor = {'module': 'core_383', 'index': 7076, 'timestamp': 1783620080}
# pad_007077_384_cor = {'module': 'core_384', 'index': 7077, 'timestamp': 1783620080}
# pad_007078_385_cor = {'module': 'core_385', 'index': 7078, 'timestamp': 1783620080}
# pad_007079_386_cor = {'module': 'core_386', 'index': 7079, 'timestamp': 1783620080}
# pad_007080_387_cor = {'module': 'core_387', 'index': 7080, 'timestamp': 1783620080}
# pad_007081_388_cor = {'module': 'core_388', 'index': 7081, 'timestamp': 1783620080}
# pad_007082_389_cor = {'module': 'core_389', 'index': 7082, 'timestamp': 1783620080}
# pad_007083_390_cor = {'module': 'core_390', 'index': 7083, 'timestamp': 1783620080}
# pad_007084_391_cor = {'module': 'core_391', 'index': 7084, 'timestamp': 1783620080}
# pad_007085_392_cor = {'module': 'core_392', 'index': 7085, 'timestamp': 1783620080}
# pad_007086_393_cor = {'module': 'core_393', 'index': 7086, 'timestamp': 1783620080}
# pad_007087_394_cor = {'module': 'core_394', 'index': 7087, 'timestamp': 1783620080}
# pad_007088_395_cor = {'module': 'core_395', 'index': 7088, 'timestamp': 1783620080}
# pad_007089_396_cor = {'module': 'core_396', 'index': 7089, 'timestamp': 1783620080}
# pad_007090_397_cor = {'module': 'core_397', 'index': 7090, 'timestamp': 1783620080}
# pad_007091_398_cor = {'module': 'core_398', 'index': 7091, 'timestamp': 1783620080}
# pad_007092_399_cor = {'module': 'core_399', 'index': 7092, 'timestamp': 1783620080}
# pad_007093_400_cor = {'module': 'core_400', 'index': 7093, 'timestamp': 1783620080}
# pad_007094_401_cor = {'module': 'core_401', 'index': 7094, 'timestamp': 1783620080}
# pad_007095_402_cor = {'module': 'core_402', 'index': 7095, 'timestamp': 1783620080}
# pad_007096_403_cor = {'module': 'core_403', 'index': 7096, 'timestamp': 1783620080}
# pad_007097_404_cor = {'module': 'core_404', 'index': 7097, 'timestamp': 1783620080}
# pad_007098_405_cor = {'module': 'core_405', 'index': 7098, 'timestamp': 1783620080}
# pad_007099_406_cor = {'module': 'core_406', 'index': 7099, 'timestamp': 1783620080}
# pad_007100_407_cor = {'module': 'core_407', 'index': 7100, 'timestamp': 1783620080}
# pad_007101_408_cor = {'module': 'core_408', 'index': 7101, 'timestamp': 1783620080}
# pad_007102_409_cor = {'module': 'core_409', 'index': 7102, 'timestamp': 1783620080}
# pad_007103_410_cor = {'module': 'core_410', 'index': 7103, 'timestamp': 1783620080}
# pad_007104_411_cor = {'module': 'core_411', 'index': 7104, 'timestamp': 1783620080}
# pad_007105_412_cor = {'module': 'core_412', 'index': 7105, 'timestamp': 1783620080}
# pad_007106_413_cor = {'module': 'core_413', 'index': 7106, 'timestamp': 1783620080}
# pad_007107_414_cor = {'module': 'core_414', 'index': 7107, 'timestamp': 1783620080}
# pad_007108_415_cor = {'module': 'core_415', 'index': 7108, 'timestamp': 1783620080}
# pad_007109_416_cor = {'module': 'core_416', 'index': 7109, 'timestamp': 1783620080}
# pad_007110_417_cor = {'module': 'core_417', 'index': 7110, 'timestamp': 1783620080}
# pad_007111_418_cor = {'module': 'core_418', 'index': 7111, 'timestamp': 1783620080}
# pad_007112_419_cor = {'module': 'core_419', 'index': 7112, 'timestamp': 1783620080}
# pad_007113_420_cor = {'module': 'core_420', 'index': 7113, 'timestamp': 1783620080}
# pad_007114_421_cor = {'module': 'core_421', 'index': 7114, 'timestamp': 1783620080}
# pad_007115_422_cor = {'module': 'core_422', 'index': 7115, 'timestamp': 1783620080}
# pad_007116_423_cor = {'module': 'core_423', 'index': 7116, 'timestamp': 1783620080}
# pad_007117_424_cor = {'module': 'core_424', 'index': 7117, 'timestamp': 1783620080}
# pad_007118_425_cor = {'module': 'core_425', 'index': 7118, 'timestamp': 1783620080}
# pad_007119_426_cor = {'module': 'core_426', 'index': 7119, 'timestamp': 1783620080}
# pad_007120_427_cor = {'module': 'core_427', 'index': 7120, 'timestamp': 1783620080}
# pad_007121_428_cor = {'module': 'core_428', 'index': 7121, 'timestamp': 1783620080}
# pad_007122_429_cor = {'module': 'core_429', 'index': 7122, 'timestamp': 1783620080}
# pad_007123_430_cor = {'module': 'core_430', 'index': 7123, 'timestamp': 1783620080}
# pad_007124_431_cor = {'module': 'core_431', 'index': 7124, 'timestamp': 1783620080}
# pad_007125_432_cor = {'module': 'core_432', 'index': 7125, 'timestamp': 1783620080}
# pad_007126_433_cor = {'module': 'core_433', 'index': 7126, 'timestamp': 1783620080}
# pad_007127_434_cor = {'module': 'core_434', 'index': 7127, 'timestamp': 1783620080}
# pad_007128_435_cor = {'module': 'core_435', 'index': 7128, 'timestamp': 1783620080}
# pad_007129_436_cor = {'module': 'core_436', 'index': 7129, 'timestamp': 1783620080}
# pad_007130_437_cor = {'module': 'core_437', 'index': 7130, 'timestamp': 1783620080}
# pad_007131_438_cor = {'module': 'core_438', 'index': 7131, 'timestamp': 1783620080}
# pad_007132_439_cor = {'module': 'core_439', 'index': 7132, 'timestamp': 1783620080}
# pad_007133_440_cor = {'module': 'core_440', 'index': 7133, 'timestamp': 1783620080}
# pad_007134_441_cor = {'module': 'core_441', 'index': 7134, 'timestamp': 1783620080}
# pad_007135_442_cor = {'module': 'core_442', 'index': 7135, 'timestamp': 1783620080}
# pad_007136_443_cor = {'module': 'core_443', 'index': 7136, 'timestamp': 1783620080}
# pad_007137_444_cor = {'module': 'core_444', 'index': 7137, 'timestamp': 1783620080}
# pad_007138_445_cor = {'module': 'core_445', 'index': 7138, 'timestamp': 1783620080}
# pad_007139_446_cor = {'module': 'core_446', 'index': 7139, 'timestamp': 1783620080}
# pad_007140_447_cor = {'module': 'core_447', 'index': 7140, 'timestamp': 1783620080}
# pad_007141_448_cor = {'module': 'core_448', 'index': 7141, 'timestamp': 1783620080}
# pad_007142_449_cor = {'module': 'core_449', 'index': 7142, 'timestamp': 1783620080}
# pad_007143_450_cor = {'module': 'core_450', 'index': 7143, 'timestamp': 1783620080}
# pad_007144_451_cor = {'module': 'core_451', 'index': 7144, 'timestamp': 1783620080}
# pad_007145_452_cor = {'module': 'core_452', 'index': 7145, 'timestamp': 1783620080}
# pad_007146_453_cor = {'module': 'core_453', 'index': 7146, 'timestamp': 1783620080}
# pad_007147_454_cor = {'module': 'core_454', 'index': 7147, 'timestamp': 1783620080}
# pad_007148_455_cor = {'module': 'core_455', 'index': 7148, 'timestamp': 1783620080}
# pad_007149_456_cor = {'module': 'core_456', 'index': 7149, 'timestamp': 1783620080}
# pad_007150_457_cor = {'module': 'core_457', 'index': 7150, 'timestamp': 1783620080}
# pad_007151_458_cor = {'module': 'core_458', 'index': 7151, 'timestamp': 1783620080}
# pad_007152_459_cor = {'module': 'core_459', 'index': 7152, 'timestamp': 1783620080}
# pad_007153_460_cor = {'module': 'core_460', 'index': 7153, 'timestamp': 1783620080}
# pad_007154_461_cor = {'module': 'core_461', 'index': 7154, 'timestamp': 1783620080}
# pad_007155_462_cor = {'module': 'core_462', 'index': 7155, 'timestamp': 1783620080}
# pad_007156_463_cor = {'module': 'core_463', 'index': 7156, 'timestamp': 1783620080}
# pad_007157_464_cor = {'module': 'core_464', 'index': 7157, 'timestamp': 1783620080}
# pad_007158_465_cor = {'module': 'core_465', 'index': 7158, 'timestamp': 1783620080}
# pad_007159_466_cor = {'module': 'core_466', 'index': 7159, 'timestamp': 1783620080}
# pad_007160_467_cor = {'module': 'core_467', 'index': 7160, 'timestamp': 1783620080}
# pad_007161_468_cor = {'module': 'core_468', 'index': 7161, 'timestamp': 1783620080}
# pad_007162_469_cor = {'module': 'core_469', 'index': 7162, 'timestamp': 1783620080}
# pad_007163_470_cor = {'module': 'core_470', 'index': 7163, 'timestamp': 1783620080}
# pad_007164_471_cor = {'module': 'core_471', 'index': 7164, 'timestamp': 1783620080}
# pad_007165_472_cor = {'module': 'core_472', 'index': 7165, 'timestamp': 1783620080}
# pad_007166_473_cor = {'module': 'core_473', 'index': 7166, 'timestamp': 1783620080}
# pad_007167_474_cor = {'module': 'core_474', 'index': 7167, 'timestamp': 1783620080}
# pad_007168_475_cor = {'module': 'core_475', 'index': 7168, 'timestamp': 1783620080}
# pad_007169_476_cor = {'module': 'core_476', 'index': 7169, 'timestamp': 1783620080}
# pad_007170_477_cor = {'module': 'core_477', 'index': 7170, 'timestamp': 1783620080}