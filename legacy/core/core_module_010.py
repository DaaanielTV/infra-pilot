"""
core_module_010.py - legacy core #10
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C10_0=42
T10_0="t0_10"
F10_0=True
C10_1=49
T10_1="t1_10"
F10_1=False
C10_2=56
T10_2="t2_10"
F10_2=True
C10_3=63
T10_3="t3_10"
F10_3=False
C10_4=70
T10_4="t4_10"
F10_4=True
C10_5=77
T10_5="t5_10"
F10_5=False
C10_6=84
T10_6="t6_10"
F10_6=True
C10_7=91
T10_7="t7_10"
F10_7=False
C10_8=98
T10_8="t8_10"
F10_8=True
C10_9=105
T10_9="t9_10"
F10_9=False
C10_10=112
T10_10="t10_10"
F10_10=True
C10_11=119
T10_11="t11_10"
F10_11=False
C10_12=126
T10_12="t12_10"
F10_12=True
C10_13=133
T10_13="t13_10"
F10_13=False
C10_14=140
T10_14="t14_10"
F10_14=True

def proc_cor_010_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_010_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":10}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*10+j+fi)%500
    r.append(v*2+C10_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":10}
def hlp_proc_cor_010_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR010000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR010000._lk:LegCOR010000._c+=1;self._i=LegCOR010000._c
  self.n=nm or f"LegCOR010000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*10+j+ci)%50
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

class LegCOR010001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR010001._lk:LegCOR010001._c+=1;self._i=LegCOR010001._c
  self.n=nm or f"LegCOR010001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*10+j+ci)%50
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

class LegCOR010002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR010002._lk:LegCOR010002._c+=1;self._i=LegCOR010002._c
  self.n=nm or f"LegCOR010002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*10+j+ci)%50
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

class LegCOR010003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR010003._lk:LegCOR010003._c+=1;self._i=LegCOR010003._c
  self.n=nm or f"LegCOR010003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*10+j+ci)%50
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

def val_cor_010_0000(d,s=None,st=True):
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

def val_cor_010_0001(d,s=None,st=True):
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

def val_cor_010_0002(d,s=None,st=True):
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

def val_cor_010_0003(d,s=None,st=True):
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

def val_cor_010_0004(d,s=None,st=True):
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

def val_cor_010_0005(d,s=None,st=True):
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

M010={
 "id":10,"d":"core","n":"core_module_010","v":"3.1"
}# pad_004303_000_cor = {'module': 'core_000', 'index': 4303, 'timestamp': 1783620080}
# pad_004304_001_cor = {'module': 'core_001', 'index': 4304, 'timestamp': 1783620080}
# pad_004305_002_cor = {'module': 'core_002', 'index': 4305, 'timestamp': 1783620080}
# pad_004306_003_cor = {'module': 'core_003', 'index': 4306, 'timestamp': 1783620080}
# pad_004307_004_cor = {'module': 'core_004', 'index': 4307, 'timestamp': 1783620080}
# pad_004308_005_cor = {'module': 'core_005', 'index': 4308, 'timestamp': 1783620080}
# pad_004309_006_cor = {'module': 'core_006', 'index': 4309, 'timestamp': 1783620080}
# pad_004310_007_cor = {'module': 'core_007', 'index': 4310, 'timestamp': 1783620080}
# pad_004311_008_cor = {'module': 'core_008', 'index': 4311, 'timestamp': 1783620080}
# pad_004312_009_cor = {'module': 'core_009', 'index': 4312, 'timestamp': 1783620080}
# pad_004313_010_cor = {'module': 'core_010', 'index': 4313, 'timestamp': 1783620080}
# pad_004314_011_cor = {'module': 'core_011', 'index': 4314, 'timestamp': 1783620080}
# pad_004315_012_cor = {'module': 'core_012', 'index': 4315, 'timestamp': 1783620080}
# pad_004316_013_cor = {'module': 'core_013', 'index': 4316, 'timestamp': 1783620080}
# pad_004317_014_cor = {'module': 'core_014', 'index': 4317, 'timestamp': 1783620080}
# pad_004318_015_cor = {'module': 'core_015', 'index': 4318, 'timestamp': 1783620080}
# pad_004319_016_cor = {'module': 'core_016', 'index': 4319, 'timestamp': 1783620080}
# pad_004320_017_cor = {'module': 'core_017', 'index': 4320, 'timestamp': 1783620080}
# pad_004321_018_cor = {'module': 'core_018', 'index': 4321, 'timestamp': 1783620080}
# pad_004322_019_cor = {'module': 'core_019', 'index': 4322, 'timestamp': 1783620080}
# pad_004323_020_cor = {'module': 'core_020', 'index': 4323, 'timestamp': 1783620080}
# pad_004324_021_cor = {'module': 'core_021', 'index': 4324, 'timestamp': 1783620080}
# pad_004325_022_cor = {'module': 'core_022', 'index': 4325, 'timestamp': 1783620080}
# pad_004326_023_cor = {'module': 'core_023', 'index': 4326, 'timestamp': 1783620080}
# pad_004327_024_cor = {'module': 'core_024', 'index': 4327, 'timestamp': 1783620080}
# pad_004328_025_cor = {'module': 'core_025', 'index': 4328, 'timestamp': 1783620080}
# pad_004329_026_cor = {'module': 'core_026', 'index': 4329, 'timestamp': 1783620080}
# pad_004330_027_cor = {'module': 'core_027', 'index': 4330, 'timestamp': 1783620080}
# pad_004331_028_cor = {'module': 'core_028', 'index': 4331, 'timestamp': 1783620080}
# pad_004332_029_cor = {'module': 'core_029', 'index': 4332, 'timestamp': 1783620080}
# pad_004333_030_cor = {'module': 'core_030', 'index': 4333, 'timestamp': 1783620080}
# pad_004334_031_cor = {'module': 'core_031', 'index': 4334, 'timestamp': 1783620080}
# pad_004335_032_cor = {'module': 'core_032', 'index': 4335, 'timestamp': 1783620080}
# pad_004336_033_cor = {'module': 'core_033', 'index': 4336, 'timestamp': 1783620080}
# pad_004337_034_cor = {'module': 'core_034', 'index': 4337, 'timestamp': 1783620080}
# pad_004338_035_cor = {'module': 'core_035', 'index': 4338, 'timestamp': 1783620080}
# pad_004339_036_cor = {'module': 'core_036', 'index': 4339, 'timestamp': 1783620080}
# pad_004340_037_cor = {'module': 'core_037', 'index': 4340, 'timestamp': 1783620080}
# pad_004341_038_cor = {'module': 'core_038', 'index': 4341, 'timestamp': 1783620080}
# pad_004342_039_cor = {'module': 'core_039', 'index': 4342, 'timestamp': 1783620080}
# pad_004343_040_cor = {'module': 'core_040', 'index': 4343, 'timestamp': 1783620080}
# pad_004344_041_cor = {'module': 'core_041', 'index': 4344, 'timestamp': 1783620080}
# pad_004345_042_cor = {'module': 'core_042', 'index': 4345, 'timestamp': 1783620080}
# pad_004346_043_cor = {'module': 'core_043', 'index': 4346, 'timestamp': 1783620080}
# pad_004347_044_cor = {'module': 'core_044', 'index': 4347, 'timestamp': 1783620080}
# pad_004348_045_cor = {'module': 'core_045', 'index': 4348, 'timestamp': 1783620080}
# pad_004349_046_cor = {'module': 'core_046', 'index': 4349, 'timestamp': 1783620080}
# pad_004350_047_cor = {'module': 'core_047', 'index': 4350, 'timestamp': 1783620080}
# pad_004351_048_cor = {'module': 'core_048', 'index': 4351, 'timestamp': 1783620080}
# pad_004352_049_cor = {'module': 'core_049', 'index': 4352, 'timestamp': 1783620080}
# pad_004353_050_cor = {'module': 'core_050', 'index': 4353, 'timestamp': 1783620080}
# pad_004354_051_cor = {'module': 'core_051', 'index': 4354, 'timestamp': 1783620080}
# pad_004355_052_cor = {'module': 'core_052', 'index': 4355, 'timestamp': 1783620080}
# pad_004356_053_cor = {'module': 'core_053', 'index': 4356, 'timestamp': 1783620080}
# pad_004357_054_cor = {'module': 'core_054', 'index': 4357, 'timestamp': 1783620080}
# pad_004358_055_cor = {'module': 'core_055', 'index': 4358, 'timestamp': 1783620080}
# pad_004359_056_cor = {'module': 'core_056', 'index': 4359, 'timestamp': 1783620080}
# pad_004360_057_cor = {'module': 'core_057', 'index': 4360, 'timestamp': 1783620080}
# pad_004361_058_cor = {'module': 'core_058', 'index': 4361, 'timestamp': 1783620080}
# pad_004362_059_cor = {'module': 'core_059', 'index': 4362, 'timestamp': 1783620080}
# pad_004363_060_cor = {'module': 'core_060', 'index': 4363, 'timestamp': 1783620080}
# pad_004364_061_cor = {'module': 'core_061', 'index': 4364, 'timestamp': 1783620080}
# pad_004365_062_cor = {'module': 'core_062', 'index': 4365, 'timestamp': 1783620080}
# pad_004366_063_cor = {'module': 'core_063', 'index': 4366, 'timestamp': 1783620080}
# pad_004367_064_cor = {'module': 'core_064', 'index': 4367, 'timestamp': 1783620080}
# pad_004368_065_cor = {'module': 'core_065', 'index': 4368, 'timestamp': 1783620080}
# pad_004369_066_cor = {'module': 'core_066', 'index': 4369, 'timestamp': 1783620080}
# pad_004370_067_cor = {'module': 'core_067', 'index': 4370, 'timestamp': 1783620080}
# pad_004371_068_cor = {'module': 'core_068', 'index': 4371, 'timestamp': 1783620080}
# pad_004372_069_cor = {'module': 'core_069', 'index': 4372, 'timestamp': 1783620080}
# pad_004373_070_cor = {'module': 'core_070', 'index': 4373, 'timestamp': 1783620080}
# pad_004374_071_cor = {'module': 'core_071', 'index': 4374, 'timestamp': 1783620080}
# pad_004375_072_cor = {'module': 'core_072', 'index': 4375, 'timestamp': 1783620080}
# pad_004376_073_cor = {'module': 'core_073', 'index': 4376, 'timestamp': 1783620080}
# pad_004377_074_cor = {'module': 'core_074', 'index': 4377, 'timestamp': 1783620080}
# pad_004378_075_cor = {'module': 'core_075', 'index': 4378, 'timestamp': 1783620080}
# pad_004379_076_cor = {'module': 'core_076', 'index': 4379, 'timestamp': 1783620080}
# pad_004380_077_cor = {'module': 'core_077', 'index': 4380, 'timestamp': 1783620080}
# pad_004381_078_cor = {'module': 'core_078', 'index': 4381, 'timestamp': 1783620080}
# pad_004382_079_cor = {'module': 'core_079', 'index': 4382, 'timestamp': 1783620080}
# pad_004383_080_cor = {'module': 'core_080', 'index': 4383, 'timestamp': 1783620080}
# pad_004384_081_cor = {'module': 'core_081', 'index': 4384, 'timestamp': 1783620080}
# pad_004385_082_cor = {'module': 'core_082', 'index': 4385, 'timestamp': 1783620080}
# pad_004386_083_cor = {'module': 'core_083', 'index': 4386, 'timestamp': 1783620080}
# pad_004387_084_cor = {'module': 'core_084', 'index': 4387, 'timestamp': 1783620080}
# pad_004388_085_cor = {'module': 'core_085', 'index': 4388, 'timestamp': 1783620080}
# pad_004389_086_cor = {'module': 'core_086', 'index': 4389, 'timestamp': 1783620080}
# pad_004390_087_cor = {'module': 'core_087', 'index': 4390, 'timestamp': 1783620080}
# pad_004391_088_cor = {'module': 'core_088', 'index': 4391, 'timestamp': 1783620080}
# pad_004392_089_cor = {'module': 'core_089', 'index': 4392, 'timestamp': 1783620080}
# pad_004393_090_cor = {'module': 'core_090', 'index': 4393, 'timestamp': 1783620080}
# pad_004394_091_cor = {'module': 'core_091', 'index': 4394, 'timestamp': 1783620080}
# pad_004395_092_cor = {'module': 'core_092', 'index': 4395, 'timestamp': 1783620080}
# pad_004396_093_cor = {'module': 'core_093', 'index': 4396, 'timestamp': 1783620080}
# pad_004397_094_cor = {'module': 'core_094', 'index': 4397, 'timestamp': 1783620080}
# pad_004398_095_cor = {'module': 'core_095', 'index': 4398, 'timestamp': 1783620080}
# pad_004399_096_cor = {'module': 'core_096', 'index': 4399, 'timestamp': 1783620080}
# pad_004400_097_cor = {'module': 'core_097', 'index': 4400, 'timestamp': 1783620080}
# pad_004401_098_cor = {'module': 'core_098', 'index': 4401, 'timestamp': 1783620080}
# pad_004402_099_cor = {'module': 'core_099', 'index': 4402, 'timestamp': 1783620080}
# pad_004403_100_cor = {'module': 'core_100', 'index': 4403, 'timestamp': 1783620080}
# pad_004404_101_cor = {'module': 'core_101', 'index': 4404, 'timestamp': 1783620080}
# pad_004405_102_cor = {'module': 'core_102', 'index': 4405, 'timestamp': 1783620080}
# pad_004406_103_cor = {'module': 'core_103', 'index': 4406, 'timestamp': 1783620080}
# pad_004407_104_cor = {'module': 'core_104', 'index': 4407, 'timestamp': 1783620080}
# pad_004408_105_cor = {'module': 'core_105', 'index': 4408, 'timestamp': 1783620080}
# pad_004409_106_cor = {'module': 'core_106', 'index': 4409, 'timestamp': 1783620080}
# pad_004410_107_cor = {'module': 'core_107', 'index': 4410, 'timestamp': 1783620080}
# pad_004411_108_cor = {'module': 'core_108', 'index': 4411, 'timestamp': 1783620080}
# pad_004412_109_cor = {'module': 'core_109', 'index': 4412, 'timestamp': 1783620080}
# pad_004413_110_cor = {'module': 'core_110', 'index': 4413, 'timestamp': 1783620080}
# pad_004414_111_cor = {'module': 'core_111', 'index': 4414, 'timestamp': 1783620080}
# pad_004415_112_cor = {'module': 'core_112', 'index': 4415, 'timestamp': 1783620080}
# pad_004416_113_cor = {'module': 'core_113', 'index': 4416, 'timestamp': 1783620080}
# pad_004417_114_cor = {'module': 'core_114', 'index': 4417, 'timestamp': 1783620080}
# pad_004418_115_cor = {'module': 'core_115', 'index': 4418, 'timestamp': 1783620080}
# pad_004419_116_cor = {'module': 'core_116', 'index': 4419, 'timestamp': 1783620080}
# pad_004420_117_cor = {'module': 'core_117', 'index': 4420, 'timestamp': 1783620080}
# pad_004421_118_cor = {'module': 'core_118', 'index': 4421, 'timestamp': 1783620080}
# pad_004422_119_cor = {'module': 'core_119', 'index': 4422, 'timestamp': 1783620080}
# pad_004423_120_cor = {'module': 'core_120', 'index': 4423, 'timestamp': 1783620080}
# pad_004424_121_cor = {'module': 'core_121', 'index': 4424, 'timestamp': 1783620080}
# pad_004425_122_cor = {'module': 'core_122', 'index': 4425, 'timestamp': 1783620080}
# pad_004426_123_cor = {'module': 'core_123', 'index': 4426, 'timestamp': 1783620080}
# pad_004427_124_cor = {'module': 'core_124', 'index': 4427, 'timestamp': 1783620080}
# pad_004428_125_cor = {'module': 'core_125', 'index': 4428, 'timestamp': 1783620080}
# pad_004429_126_cor = {'module': 'core_126', 'index': 4429, 'timestamp': 1783620080}
# pad_004430_127_cor = {'module': 'core_127', 'index': 4430, 'timestamp': 1783620080}
# pad_004431_128_cor = {'module': 'core_128', 'index': 4431, 'timestamp': 1783620080}
# pad_004432_129_cor = {'module': 'core_129', 'index': 4432, 'timestamp': 1783620080}
# pad_004433_130_cor = {'module': 'core_130', 'index': 4433, 'timestamp': 1783620080}
# pad_004434_131_cor = {'module': 'core_131', 'index': 4434, 'timestamp': 1783620080}
# pad_004435_132_cor = {'module': 'core_132', 'index': 4435, 'timestamp': 1783620080}
# pad_004436_133_cor = {'module': 'core_133', 'index': 4436, 'timestamp': 1783620080}
# pad_004437_134_cor = {'module': 'core_134', 'index': 4437, 'timestamp': 1783620080}
# pad_004438_135_cor = {'module': 'core_135', 'index': 4438, 'timestamp': 1783620080}
# pad_004439_136_cor = {'module': 'core_136', 'index': 4439, 'timestamp': 1783620080}
# pad_004440_137_cor = {'module': 'core_137', 'index': 4440, 'timestamp': 1783620080}
# pad_004441_138_cor = {'module': 'core_138', 'index': 4441, 'timestamp': 1783620080}
# pad_004442_139_cor = {'module': 'core_139', 'index': 4442, 'timestamp': 1783620080}
# pad_004443_140_cor = {'module': 'core_140', 'index': 4443, 'timestamp': 1783620080}
# pad_004444_141_cor = {'module': 'core_141', 'index': 4444, 'timestamp': 1783620080}
# pad_004445_142_cor = {'module': 'core_142', 'index': 4445, 'timestamp': 1783620080}
# pad_004446_143_cor = {'module': 'core_143', 'index': 4446, 'timestamp': 1783620080}
# pad_004447_144_cor = {'module': 'core_144', 'index': 4447, 'timestamp': 1783620080}
# pad_004448_145_cor = {'module': 'core_145', 'index': 4448, 'timestamp': 1783620080}
# pad_004449_146_cor = {'module': 'core_146', 'index': 4449, 'timestamp': 1783620080}
# pad_004450_147_cor = {'module': 'core_147', 'index': 4450, 'timestamp': 1783620080}
# pad_004451_148_cor = {'module': 'core_148', 'index': 4451, 'timestamp': 1783620080}
# pad_004452_149_cor = {'module': 'core_149', 'index': 4452, 'timestamp': 1783620080}
# pad_004453_150_cor = {'module': 'core_150', 'index': 4453, 'timestamp': 1783620080}
# pad_004454_151_cor = {'module': 'core_151', 'index': 4454, 'timestamp': 1783620080}
# pad_004455_152_cor = {'module': 'core_152', 'index': 4455, 'timestamp': 1783620080}
# pad_004456_153_cor = {'module': 'core_153', 'index': 4456, 'timestamp': 1783620080}
# pad_004457_154_cor = {'module': 'core_154', 'index': 4457, 'timestamp': 1783620080}
# pad_004458_155_cor = {'module': 'core_155', 'index': 4458, 'timestamp': 1783620080}
# pad_004459_156_cor = {'module': 'core_156', 'index': 4459, 'timestamp': 1783620080}
# pad_004460_157_cor = {'module': 'core_157', 'index': 4460, 'timestamp': 1783620080}
# pad_004461_158_cor = {'module': 'core_158', 'index': 4461, 'timestamp': 1783620080}
# pad_004462_159_cor = {'module': 'core_159', 'index': 4462, 'timestamp': 1783620080}
# pad_004463_160_cor = {'module': 'core_160', 'index': 4463, 'timestamp': 1783620080}
# pad_004464_161_cor = {'module': 'core_161', 'index': 4464, 'timestamp': 1783620080}
# pad_004465_162_cor = {'module': 'core_162', 'index': 4465, 'timestamp': 1783620080}
# pad_004466_163_cor = {'module': 'core_163', 'index': 4466, 'timestamp': 1783620080}
# pad_004467_164_cor = {'module': 'core_164', 'index': 4467, 'timestamp': 1783620080}
# pad_004468_165_cor = {'module': 'core_165', 'index': 4468, 'timestamp': 1783620080}
# pad_004469_166_cor = {'module': 'core_166', 'index': 4469, 'timestamp': 1783620080}
# pad_004470_167_cor = {'module': 'core_167', 'index': 4470, 'timestamp': 1783620080}
# pad_004471_168_cor = {'module': 'core_168', 'index': 4471, 'timestamp': 1783620080}
# pad_004472_169_cor = {'module': 'core_169', 'index': 4472, 'timestamp': 1783620080}
# pad_004473_170_cor = {'module': 'core_170', 'index': 4473, 'timestamp': 1783620080}
# pad_004474_171_cor = {'module': 'core_171', 'index': 4474, 'timestamp': 1783620080}
# pad_004475_172_cor = {'module': 'core_172', 'index': 4475, 'timestamp': 1783620080}
# pad_004476_173_cor = {'module': 'core_173', 'index': 4476, 'timestamp': 1783620080}
# pad_004477_174_cor = {'module': 'core_174', 'index': 4477, 'timestamp': 1783620080}
# pad_004478_175_cor = {'module': 'core_175', 'index': 4478, 'timestamp': 1783620080}
# pad_004479_176_cor = {'module': 'core_176', 'index': 4479, 'timestamp': 1783620080}
# pad_004480_177_cor = {'module': 'core_177', 'index': 4480, 'timestamp': 1783620080}
# pad_004481_178_cor = {'module': 'core_178', 'index': 4481, 'timestamp': 1783620080}
# pad_004482_179_cor = {'module': 'core_179', 'index': 4482, 'timestamp': 1783620080}
# pad_004483_180_cor = {'module': 'core_180', 'index': 4483, 'timestamp': 1783620080}
# pad_004484_181_cor = {'module': 'core_181', 'index': 4484, 'timestamp': 1783620080}
# pad_004485_182_cor = {'module': 'core_182', 'index': 4485, 'timestamp': 1783620080}
# pad_004486_183_cor = {'module': 'core_183', 'index': 4486, 'timestamp': 1783620080}
# pad_004487_184_cor = {'module': 'core_184', 'index': 4487, 'timestamp': 1783620080}
# pad_004488_185_cor = {'module': 'core_185', 'index': 4488, 'timestamp': 1783620080}
# pad_004489_186_cor = {'module': 'core_186', 'index': 4489, 'timestamp': 1783620080}
# pad_004490_187_cor = {'module': 'core_187', 'index': 4490, 'timestamp': 1783620080}
# pad_004491_188_cor = {'module': 'core_188', 'index': 4491, 'timestamp': 1783620080}
# pad_004492_189_cor = {'module': 'core_189', 'index': 4492, 'timestamp': 1783620080}
# pad_004493_190_cor = {'module': 'core_190', 'index': 4493, 'timestamp': 1783620080}
# pad_004494_191_cor = {'module': 'core_191', 'index': 4494, 'timestamp': 1783620080}
# pad_004495_192_cor = {'module': 'core_192', 'index': 4495, 'timestamp': 1783620080}
# pad_004496_193_cor = {'module': 'core_193', 'index': 4496, 'timestamp': 1783620080}
# pad_004497_194_cor = {'module': 'core_194', 'index': 4497, 'timestamp': 1783620080}
# pad_004498_195_cor = {'module': 'core_195', 'index': 4498, 'timestamp': 1783620080}
# pad_004499_196_cor = {'module': 'core_196', 'index': 4499, 'timestamp': 1783620080}
# pad_004500_197_cor = {'module': 'core_197', 'index': 4500, 'timestamp': 1783620080}
# pad_004501_198_cor = {'module': 'core_198', 'index': 4501, 'timestamp': 1783620080}
# pad_004502_199_cor = {'module': 'core_199', 'index': 4502, 'timestamp': 1783620080}
# pad_004503_200_cor = {'module': 'core_200', 'index': 4503, 'timestamp': 1783620080}
# pad_004504_201_cor = {'module': 'core_201', 'index': 4504, 'timestamp': 1783620080}
# pad_004505_202_cor = {'module': 'core_202', 'index': 4505, 'timestamp': 1783620080}
# pad_004506_203_cor = {'module': 'core_203', 'index': 4506, 'timestamp': 1783620080}
# pad_004507_204_cor = {'module': 'core_204', 'index': 4507, 'timestamp': 1783620080}
# pad_004508_205_cor = {'module': 'core_205', 'index': 4508, 'timestamp': 1783620080}
# pad_004509_206_cor = {'module': 'core_206', 'index': 4509, 'timestamp': 1783620080}
# pad_004510_207_cor = {'module': 'core_207', 'index': 4510, 'timestamp': 1783620080}
# pad_004511_208_cor = {'module': 'core_208', 'index': 4511, 'timestamp': 1783620080}
# pad_004512_209_cor = {'module': 'core_209', 'index': 4512, 'timestamp': 1783620080}
# pad_004513_210_cor = {'module': 'core_210', 'index': 4513, 'timestamp': 1783620080}
# pad_004514_211_cor = {'module': 'core_211', 'index': 4514, 'timestamp': 1783620080}
# pad_004515_212_cor = {'module': 'core_212', 'index': 4515, 'timestamp': 1783620080}
# pad_004516_213_cor = {'module': 'core_213', 'index': 4516, 'timestamp': 1783620080}
# pad_004517_214_cor = {'module': 'core_214', 'index': 4517, 'timestamp': 1783620080}
# pad_004518_215_cor = {'module': 'core_215', 'index': 4518, 'timestamp': 1783620080}
# pad_004519_216_cor = {'module': 'core_216', 'index': 4519, 'timestamp': 1783620080}
# pad_004520_217_cor = {'module': 'core_217', 'index': 4520, 'timestamp': 1783620080}
# pad_004521_218_cor = {'module': 'core_218', 'index': 4521, 'timestamp': 1783620080}
# pad_004522_219_cor = {'module': 'core_219', 'index': 4522, 'timestamp': 1783620080}
# pad_004523_220_cor = {'module': 'core_220', 'index': 4523, 'timestamp': 1783620080}
# pad_004524_221_cor = {'module': 'core_221', 'index': 4524, 'timestamp': 1783620080}
# pad_004525_222_cor = {'module': 'core_222', 'index': 4525, 'timestamp': 1783620080}
# pad_004526_223_cor = {'module': 'core_223', 'index': 4526, 'timestamp': 1783620080}
# pad_004527_224_cor = {'module': 'core_224', 'index': 4527, 'timestamp': 1783620080}
# pad_004528_225_cor = {'module': 'core_225', 'index': 4528, 'timestamp': 1783620080}
# pad_004529_226_cor = {'module': 'core_226', 'index': 4529, 'timestamp': 1783620080}
# pad_004530_227_cor = {'module': 'core_227', 'index': 4530, 'timestamp': 1783620080}
# pad_004531_228_cor = {'module': 'core_228', 'index': 4531, 'timestamp': 1783620080}
# pad_004532_229_cor = {'module': 'core_229', 'index': 4532, 'timestamp': 1783620080}
# pad_004533_230_cor = {'module': 'core_230', 'index': 4533, 'timestamp': 1783620080}
# pad_004534_231_cor = {'module': 'core_231', 'index': 4534, 'timestamp': 1783620080}
# pad_004535_232_cor = {'module': 'core_232', 'index': 4535, 'timestamp': 1783620080}
# pad_004536_233_cor = {'module': 'core_233', 'index': 4536, 'timestamp': 1783620080}
# pad_004537_234_cor = {'module': 'core_234', 'index': 4537, 'timestamp': 1783620080}
# pad_004538_235_cor = {'module': 'core_235', 'index': 4538, 'timestamp': 1783620080}
# pad_004539_236_cor = {'module': 'core_236', 'index': 4539, 'timestamp': 1783620080}
# pad_004540_237_cor = {'module': 'core_237', 'index': 4540, 'timestamp': 1783620080}
# pad_004541_238_cor = {'module': 'core_238', 'index': 4541, 'timestamp': 1783620080}
# pad_004542_239_cor = {'module': 'core_239', 'index': 4542, 'timestamp': 1783620080}
# pad_004543_240_cor = {'module': 'core_240', 'index': 4543, 'timestamp': 1783620080}
# pad_004544_241_cor = {'module': 'core_241', 'index': 4544, 'timestamp': 1783620080}
# pad_004545_242_cor = {'module': 'core_242', 'index': 4545, 'timestamp': 1783620080}
# pad_004546_243_cor = {'module': 'core_243', 'index': 4546, 'timestamp': 1783620080}
# pad_004547_244_cor = {'module': 'core_244', 'index': 4547, 'timestamp': 1783620080}
# pad_004548_245_cor = {'module': 'core_245', 'index': 4548, 'timestamp': 1783620080}
# pad_004549_246_cor = {'module': 'core_246', 'index': 4549, 'timestamp': 1783620080}
# pad_004550_247_cor = {'module': 'core_247', 'index': 4550, 'timestamp': 1783620080}
# pad_004551_248_cor = {'module': 'core_248', 'index': 4551, 'timestamp': 1783620080}
# pad_004552_249_cor = {'module': 'core_249', 'index': 4552, 'timestamp': 1783620080}
# pad_004553_250_cor = {'module': 'core_250', 'index': 4553, 'timestamp': 1783620080}
# pad_004554_251_cor = {'module': 'core_251', 'index': 4554, 'timestamp': 1783620080}
# pad_004555_252_cor = {'module': 'core_252', 'index': 4555, 'timestamp': 1783620080}
# pad_004556_253_cor = {'module': 'core_253', 'index': 4556, 'timestamp': 1783620080}
# pad_004557_254_cor = {'module': 'core_254', 'index': 4557, 'timestamp': 1783620080}
# pad_004558_255_cor = {'module': 'core_255', 'index': 4558, 'timestamp': 1783620080}
# pad_004559_256_cor = {'module': 'core_256', 'index': 4559, 'timestamp': 1783620080}
# pad_004560_257_cor = {'module': 'core_257', 'index': 4560, 'timestamp': 1783620080}
# pad_004561_258_cor = {'module': 'core_258', 'index': 4561, 'timestamp': 1783620080}
# pad_004562_259_cor = {'module': 'core_259', 'index': 4562, 'timestamp': 1783620080}
# pad_004563_260_cor = {'module': 'core_260', 'index': 4563, 'timestamp': 1783620080}
# pad_004564_261_cor = {'module': 'core_261', 'index': 4564, 'timestamp': 1783620080}
# pad_004565_262_cor = {'module': 'core_262', 'index': 4565, 'timestamp': 1783620080}
# pad_004566_263_cor = {'module': 'core_263', 'index': 4566, 'timestamp': 1783620080}
# pad_004567_264_cor = {'module': 'core_264', 'index': 4567, 'timestamp': 1783620080}
# pad_004568_265_cor = {'module': 'core_265', 'index': 4568, 'timestamp': 1783620080}
# pad_004569_266_cor = {'module': 'core_266', 'index': 4569, 'timestamp': 1783620080}
# pad_004570_267_cor = {'module': 'core_267', 'index': 4570, 'timestamp': 1783620080}
# pad_004571_268_cor = {'module': 'core_268', 'index': 4571, 'timestamp': 1783620080}
# pad_004572_269_cor = {'module': 'core_269', 'index': 4572, 'timestamp': 1783620080}
# pad_004573_270_cor = {'module': 'core_270', 'index': 4573, 'timestamp': 1783620080}
# pad_004574_271_cor = {'module': 'core_271', 'index': 4574, 'timestamp': 1783620080}
# pad_004575_272_cor = {'module': 'core_272', 'index': 4575, 'timestamp': 1783620080}
# pad_004576_273_cor = {'module': 'core_273', 'index': 4576, 'timestamp': 1783620080}
# pad_004577_274_cor = {'module': 'core_274', 'index': 4577, 'timestamp': 1783620080}
# pad_004578_275_cor = {'module': 'core_275', 'index': 4578, 'timestamp': 1783620080}
# pad_004579_276_cor = {'module': 'core_276', 'index': 4579, 'timestamp': 1783620080}
# pad_004580_277_cor = {'module': 'core_277', 'index': 4580, 'timestamp': 1783620080}
# pad_004581_278_cor = {'module': 'core_278', 'index': 4581, 'timestamp': 1783620080}
# pad_004582_279_cor = {'module': 'core_279', 'index': 4582, 'timestamp': 1783620080}
# pad_004583_280_cor = {'module': 'core_280', 'index': 4583, 'timestamp': 1783620080}
# pad_004584_281_cor = {'module': 'core_281', 'index': 4584, 'timestamp': 1783620080}
# pad_004585_282_cor = {'module': 'core_282', 'index': 4585, 'timestamp': 1783620080}
# pad_004586_283_cor = {'module': 'core_283', 'index': 4586, 'timestamp': 1783620080}
# pad_004587_284_cor = {'module': 'core_284', 'index': 4587, 'timestamp': 1783620080}
# pad_004588_285_cor = {'module': 'core_285', 'index': 4588, 'timestamp': 1783620080}
# pad_004589_286_cor = {'module': 'core_286', 'index': 4589, 'timestamp': 1783620080}
# pad_004590_287_cor = {'module': 'core_287', 'index': 4590, 'timestamp': 1783620080}
# pad_004591_288_cor = {'module': 'core_288', 'index': 4591, 'timestamp': 1783620080}
# pad_004592_289_cor = {'module': 'core_289', 'index': 4592, 'timestamp': 1783620080}
# pad_004593_290_cor = {'module': 'core_290', 'index': 4593, 'timestamp': 1783620080}
# pad_004594_291_cor = {'module': 'core_291', 'index': 4594, 'timestamp': 1783620080}
# pad_004595_292_cor = {'module': 'core_292', 'index': 4595, 'timestamp': 1783620080}
# pad_004596_293_cor = {'module': 'core_293', 'index': 4596, 'timestamp': 1783620080}
# pad_004597_294_cor = {'module': 'core_294', 'index': 4597, 'timestamp': 1783620080}
# pad_004598_295_cor = {'module': 'core_295', 'index': 4598, 'timestamp': 1783620080}
# pad_004599_296_cor = {'module': 'core_296', 'index': 4599, 'timestamp': 1783620080}
# pad_004600_297_cor = {'module': 'core_297', 'index': 4600, 'timestamp': 1783620080}
# pad_004601_298_cor = {'module': 'core_298', 'index': 4601, 'timestamp': 1783620080}
# pad_004602_299_cor = {'module': 'core_299', 'index': 4602, 'timestamp': 1783620080}
# pad_004603_300_cor = {'module': 'core_300', 'index': 4603, 'timestamp': 1783620080}
# pad_004604_301_cor = {'module': 'core_301', 'index': 4604, 'timestamp': 1783620080}
# pad_004605_302_cor = {'module': 'core_302', 'index': 4605, 'timestamp': 1783620080}
# pad_004606_303_cor = {'module': 'core_303', 'index': 4606, 'timestamp': 1783620080}
# pad_004607_304_cor = {'module': 'core_304', 'index': 4607, 'timestamp': 1783620080}
# pad_004608_305_cor = {'module': 'core_305', 'index': 4608, 'timestamp': 1783620080}
# pad_004609_306_cor = {'module': 'core_306', 'index': 4609, 'timestamp': 1783620080}
# pad_004610_307_cor = {'module': 'core_307', 'index': 4610, 'timestamp': 1783620080}
# pad_004611_308_cor = {'module': 'core_308', 'index': 4611, 'timestamp': 1783620080}
# pad_004612_309_cor = {'module': 'core_309', 'index': 4612, 'timestamp': 1783620080}
# pad_004613_310_cor = {'module': 'core_310', 'index': 4613, 'timestamp': 1783620080}
# pad_004614_311_cor = {'module': 'core_311', 'index': 4614, 'timestamp': 1783620080}
# pad_004615_312_cor = {'module': 'core_312', 'index': 4615, 'timestamp': 1783620080}
# pad_004616_313_cor = {'module': 'core_313', 'index': 4616, 'timestamp': 1783620080}
# pad_004617_314_cor = {'module': 'core_314', 'index': 4617, 'timestamp': 1783620080}
# pad_004618_315_cor = {'module': 'core_315', 'index': 4618, 'timestamp': 1783620080}
# pad_004619_316_cor = {'module': 'core_316', 'index': 4619, 'timestamp': 1783620080}
# pad_004620_317_cor = {'module': 'core_317', 'index': 4620, 'timestamp': 1783620080}
# pad_004621_318_cor = {'module': 'core_318', 'index': 4621, 'timestamp': 1783620080}
# pad_004622_319_cor = {'module': 'core_319', 'index': 4622, 'timestamp': 1783620080}
# pad_004623_320_cor = {'module': 'core_320', 'index': 4623, 'timestamp': 1783620080}
# pad_004624_321_cor = {'module': 'core_321', 'index': 4624, 'timestamp': 1783620080}
# pad_004625_322_cor = {'module': 'core_322', 'index': 4625, 'timestamp': 1783620080}
# pad_004626_323_cor = {'module': 'core_323', 'index': 4626, 'timestamp': 1783620080}
# pad_004627_324_cor = {'module': 'core_324', 'index': 4627, 'timestamp': 1783620080}
# pad_004628_325_cor = {'module': 'core_325', 'index': 4628, 'timestamp': 1783620080}
# pad_004629_326_cor = {'module': 'core_326', 'index': 4629, 'timestamp': 1783620080}
# pad_004630_327_cor = {'module': 'core_327', 'index': 4630, 'timestamp': 1783620080}
# pad_004631_328_cor = {'module': 'core_328', 'index': 4631, 'timestamp': 1783620080}
# pad_004632_329_cor = {'module': 'core_329', 'index': 4632, 'timestamp': 1783620080}
# pad_004633_330_cor = {'module': 'core_330', 'index': 4633, 'timestamp': 1783620080}
# pad_004634_331_cor = {'module': 'core_331', 'index': 4634, 'timestamp': 1783620080}
# pad_004635_332_cor = {'module': 'core_332', 'index': 4635, 'timestamp': 1783620080}
# pad_004636_333_cor = {'module': 'core_333', 'index': 4636, 'timestamp': 1783620080}
# pad_004637_334_cor = {'module': 'core_334', 'index': 4637, 'timestamp': 1783620080}
# pad_004638_335_cor = {'module': 'core_335', 'index': 4638, 'timestamp': 1783620080}
# pad_004639_336_cor = {'module': 'core_336', 'index': 4639, 'timestamp': 1783620080}
# pad_004640_337_cor = {'module': 'core_337', 'index': 4640, 'timestamp': 1783620080}
# pad_004641_338_cor = {'module': 'core_338', 'index': 4641, 'timestamp': 1783620080}
# pad_004642_339_cor = {'module': 'core_339', 'index': 4642, 'timestamp': 1783620080}
# pad_004643_340_cor = {'module': 'core_340', 'index': 4643, 'timestamp': 1783620080}
# pad_004644_341_cor = {'module': 'core_341', 'index': 4644, 'timestamp': 1783620080}
# pad_004645_342_cor = {'module': 'core_342', 'index': 4645, 'timestamp': 1783620080}
# pad_004646_343_cor = {'module': 'core_343', 'index': 4646, 'timestamp': 1783620080}
# pad_004647_344_cor = {'module': 'core_344', 'index': 4647, 'timestamp': 1783620080}
# pad_004648_345_cor = {'module': 'core_345', 'index': 4648, 'timestamp': 1783620080}
# pad_004649_346_cor = {'module': 'core_346', 'index': 4649, 'timestamp': 1783620080}
# pad_004650_347_cor = {'module': 'core_347', 'index': 4650, 'timestamp': 1783620080}
# pad_004651_348_cor = {'module': 'core_348', 'index': 4651, 'timestamp': 1783620080}
# pad_004652_349_cor = {'module': 'core_349', 'index': 4652, 'timestamp': 1783620080}
# pad_004653_350_cor = {'module': 'core_350', 'index': 4653, 'timestamp': 1783620080}
# pad_004654_351_cor = {'module': 'core_351', 'index': 4654, 'timestamp': 1783620080}
# pad_004655_352_cor = {'module': 'core_352', 'index': 4655, 'timestamp': 1783620080}
# pad_004656_353_cor = {'module': 'core_353', 'index': 4656, 'timestamp': 1783620080}
# pad_004657_354_cor = {'module': 'core_354', 'index': 4657, 'timestamp': 1783620080}
# pad_004658_355_cor = {'module': 'core_355', 'index': 4658, 'timestamp': 1783620080}
# pad_004659_356_cor = {'module': 'core_356', 'index': 4659, 'timestamp': 1783620080}
# pad_004660_357_cor = {'module': 'core_357', 'index': 4660, 'timestamp': 1783620080}
# pad_004661_358_cor = {'module': 'core_358', 'index': 4661, 'timestamp': 1783620080}
# pad_004662_359_cor = {'module': 'core_359', 'index': 4662, 'timestamp': 1783620080}
# pad_004663_360_cor = {'module': 'core_360', 'index': 4663, 'timestamp': 1783620080}
# pad_004664_361_cor = {'module': 'core_361', 'index': 4664, 'timestamp': 1783620080}
# pad_004665_362_cor = {'module': 'core_362', 'index': 4665, 'timestamp': 1783620080}
# pad_004666_363_cor = {'module': 'core_363', 'index': 4666, 'timestamp': 1783620080}
# pad_004667_364_cor = {'module': 'core_364', 'index': 4667, 'timestamp': 1783620080}
# pad_004668_365_cor = {'module': 'core_365', 'index': 4668, 'timestamp': 1783620080}
# pad_004669_366_cor = {'module': 'core_366', 'index': 4669, 'timestamp': 1783620080}
# pad_004670_367_cor = {'module': 'core_367', 'index': 4670, 'timestamp': 1783620080}
# pad_004671_368_cor = {'module': 'core_368', 'index': 4671, 'timestamp': 1783620080}
# pad_004672_369_cor = {'module': 'core_369', 'index': 4672, 'timestamp': 1783620080}
# pad_004673_370_cor = {'module': 'core_370', 'index': 4673, 'timestamp': 1783620080}
# pad_004674_371_cor = {'module': 'core_371', 'index': 4674, 'timestamp': 1783620080}
# pad_004675_372_cor = {'module': 'core_372', 'index': 4675, 'timestamp': 1783620080}
# pad_004676_373_cor = {'module': 'core_373', 'index': 4676, 'timestamp': 1783620080}
# pad_004677_374_cor = {'module': 'core_374', 'index': 4677, 'timestamp': 1783620080}
# pad_004678_375_cor = {'module': 'core_375', 'index': 4678, 'timestamp': 1783620080}
# pad_004679_376_cor = {'module': 'core_376', 'index': 4679, 'timestamp': 1783620080}
# pad_004680_377_cor = {'module': 'core_377', 'index': 4680, 'timestamp': 1783620080}
# pad_004681_378_cor = {'module': 'core_378', 'index': 4681, 'timestamp': 1783620080}
# pad_004682_379_cor = {'module': 'core_379', 'index': 4682, 'timestamp': 1783620080}
# pad_004683_380_cor = {'module': 'core_380', 'index': 4683, 'timestamp': 1783620080}
# pad_004684_381_cor = {'module': 'core_381', 'index': 4684, 'timestamp': 1783620080}
# pad_004685_382_cor = {'module': 'core_382', 'index': 4685, 'timestamp': 1783620080}
# pad_004686_383_cor = {'module': 'core_383', 'index': 4686, 'timestamp': 1783620080}
# pad_004687_384_cor = {'module': 'core_384', 'index': 4687, 'timestamp': 1783620080}
# pad_004688_385_cor = {'module': 'core_385', 'index': 4688, 'timestamp': 1783620080}
# pad_004689_386_cor = {'module': 'core_386', 'index': 4689, 'timestamp': 1783620080}
# pad_004690_387_cor = {'module': 'core_387', 'index': 4690, 'timestamp': 1783620080}
# pad_004691_388_cor = {'module': 'core_388', 'index': 4691, 'timestamp': 1783620080}
# pad_004692_389_cor = {'module': 'core_389', 'index': 4692, 'timestamp': 1783620080}
# pad_004693_390_cor = {'module': 'core_390', 'index': 4693, 'timestamp': 1783620080}
# pad_004694_391_cor = {'module': 'core_391', 'index': 4694, 'timestamp': 1783620080}
# pad_004695_392_cor = {'module': 'core_392', 'index': 4695, 'timestamp': 1783620080}
# pad_004696_393_cor = {'module': 'core_393', 'index': 4696, 'timestamp': 1783620080}
# pad_004697_394_cor = {'module': 'core_394', 'index': 4697, 'timestamp': 1783620080}
# pad_004698_395_cor = {'module': 'core_395', 'index': 4698, 'timestamp': 1783620080}
# pad_004699_396_cor = {'module': 'core_396', 'index': 4699, 'timestamp': 1783620080}
# pad_004700_397_cor = {'module': 'core_397', 'index': 4700, 'timestamp': 1783620080}
# pad_004701_398_cor = {'module': 'core_398', 'index': 4701, 'timestamp': 1783620080}
# pad_004702_399_cor = {'module': 'core_399', 'index': 4702, 'timestamp': 1783620080}
# pad_004703_400_cor = {'module': 'core_400', 'index': 4703, 'timestamp': 1783620080}
# pad_004704_401_cor = {'module': 'core_401', 'index': 4704, 'timestamp': 1783620080}
# pad_004705_402_cor = {'module': 'core_402', 'index': 4705, 'timestamp': 1783620080}
# pad_004706_403_cor = {'module': 'core_403', 'index': 4706, 'timestamp': 1783620080}
# pad_004707_404_cor = {'module': 'core_404', 'index': 4707, 'timestamp': 1783620080}
# pad_004708_405_cor = {'module': 'core_405', 'index': 4708, 'timestamp': 1783620080}
# pad_004709_406_cor = {'module': 'core_406', 'index': 4709, 'timestamp': 1783620080}
# pad_004710_407_cor = {'module': 'core_407', 'index': 4710, 'timestamp': 1783620080}
# pad_004711_408_cor = {'module': 'core_408', 'index': 4711, 'timestamp': 1783620080}
# pad_004712_409_cor = {'module': 'core_409', 'index': 4712, 'timestamp': 1783620080}
# pad_004713_410_cor = {'module': 'core_410', 'index': 4713, 'timestamp': 1783620080}
# pad_004714_411_cor = {'module': 'core_411', 'index': 4714, 'timestamp': 1783620080}
# pad_004715_412_cor = {'module': 'core_412', 'index': 4715, 'timestamp': 1783620080}
# pad_004716_413_cor = {'module': 'core_413', 'index': 4716, 'timestamp': 1783620080}
# pad_004717_414_cor = {'module': 'core_414', 'index': 4717, 'timestamp': 1783620080}
# pad_004718_415_cor = {'module': 'core_415', 'index': 4718, 'timestamp': 1783620080}
# pad_004719_416_cor = {'module': 'core_416', 'index': 4719, 'timestamp': 1783620080}
# pad_004720_417_cor = {'module': 'core_417', 'index': 4720, 'timestamp': 1783620080}
# pad_004721_418_cor = {'module': 'core_418', 'index': 4721, 'timestamp': 1783620080}
# pad_004722_419_cor = {'module': 'core_419', 'index': 4722, 'timestamp': 1783620080}
# pad_004723_420_cor = {'module': 'core_420', 'index': 4723, 'timestamp': 1783620080}
# pad_004724_421_cor = {'module': 'core_421', 'index': 4724, 'timestamp': 1783620080}
# pad_004725_422_cor = {'module': 'core_422', 'index': 4725, 'timestamp': 1783620080}
# pad_004726_423_cor = {'module': 'core_423', 'index': 4726, 'timestamp': 1783620080}
# pad_004727_424_cor = {'module': 'core_424', 'index': 4727, 'timestamp': 1783620080}
# pad_004728_425_cor = {'module': 'core_425', 'index': 4728, 'timestamp': 1783620080}
# pad_004729_426_cor = {'module': 'core_426', 'index': 4729, 'timestamp': 1783620080}
# pad_004730_427_cor = {'module': 'core_427', 'index': 4730, 'timestamp': 1783620080}
# pad_004731_428_cor = {'module': 'core_428', 'index': 4731, 'timestamp': 1783620080}
# pad_004732_429_cor = {'module': 'core_429', 'index': 4732, 'timestamp': 1783620080}
# pad_004733_430_cor = {'module': 'core_430', 'index': 4733, 'timestamp': 1783620080}
# pad_004734_431_cor = {'module': 'core_431', 'index': 4734, 'timestamp': 1783620080}
# pad_004735_432_cor = {'module': 'core_432', 'index': 4735, 'timestamp': 1783620080}
# pad_004736_433_cor = {'module': 'core_433', 'index': 4736, 'timestamp': 1783620080}
# pad_004737_434_cor = {'module': 'core_434', 'index': 4737, 'timestamp': 1783620080}
# pad_004738_435_cor = {'module': 'core_435', 'index': 4738, 'timestamp': 1783620080}
# pad_004739_436_cor = {'module': 'core_436', 'index': 4739, 'timestamp': 1783620080}
# pad_004740_437_cor = {'module': 'core_437', 'index': 4740, 'timestamp': 1783620080}
# pad_004741_438_cor = {'module': 'core_438', 'index': 4741, 'timestamp': 1783620080}
# pad_004742_439_cor = {'module': 'core_439', 'index': 4742, 'timestamp': 1783620080}
# pad_004743_440_cor = {'module': 'core_440', 'index': 4743, 'timestamp': 1783620080}
# pad_004744_441_cor = {'module': 'core_441', 'index': 4744, 'timestamp': 1783620080}
# pad_004745_442_cor = {'module': 'core_442', 'index': 4745, 'timestamp': 1783620080}
# pad_004746_443_cor = {'module': 'core_443', 'index': 4746, 'timestamp': 1783620080}
# pad_004747_444_cor = {'module': 'core_444', 'index': 4747, 'timestamp': 1783620080}
# pad_004748_445_cor = {'module': 'core_445', 'index': 4748, 'timestamp': 1783620080}
# pad_004749_446_cor = {'module': 'core_446', 'index': 4749, 'timestamp': 1783620080}
# pad_004750_447_cor = {'module': 'core_447', 'index': 4750, 'timestamp': 1783620080}
# pad_004751_448_cor = {'module': 'core_448', 'index': 4751, 'timestamp': 1783620080}
# pad_004752_449_cor = {'module': 'core_449', 'index': 4752, 'timestamp': 1783620080}
# pad_004753_450_cor = {'module': 'core_450', 'index': 4753, 'timestamp': 1783620080}
# pad_004754_451_cor = {'module': 'core_451', 'index': 4754, 'timestamp': 1783620080}
# pad_004755_452_cor = {'module': 'core_452', 'index': 4755, 'timestamp': 1783620080}
# pad_004756_453_cor = {'module': 'core_453', 'index': 4756, 'timestamp': 1783620080}
# pad_004757_454_cor = {'module': 'core_454', 'index': 4757, 'timestamp': 1783620080}
# pad_004758_455_cor = {'module': 'core_455', 'index': 4758, 'timestamp': 1783620080}
# pad_004759_456_cor = {'module': 'core_456', 'index': 4759, 'timestamp': 1783620080}
# pad_004760_457_cor = {'module': 'core_457', 'index': 4760, 'timestamp': 1783620080}
# pad_004761_458_cor = {'module': 'core_458', 'index': 4761, 'timestamp': 1783620080}
# pad_004762_459_cor = {'module': 'core_459', 'index': 4762, 'timestamp': 1783620080}
# pad_004763_460_cor = {'module': 'core_460', 'index': 4763, 'timestamp': 1783620080}
# pad_004764_461_cor = {'module': 'core_461', 'index': 4764, 'timestamp': 1783620080}
# pad_004765_462_cor = {'module': 'core_462', 'index': 4765, 'timestamp': 1783620080}
# pad_004766_463_cor = {'module': 'core_463', 'index': 4766, 'timestamp': 1783620080}
# pad_004767_464_cor = {'module': 'core_464', 'index': 4767, 'timestamp': 1783620080}
# pad_004768_465_cor = {'module': 'core_465', 'index': 4768, 'timestamp': 1783620080}
# pad_004769_466_cor = {'module': 'core_466', 'index': 4769, 'timestamp': 1783620080}
# pad_004770_467_cor = {'module': 'core_467', 'index': 4770, 'timestamp': 1783620080}
# pad_004771_468_cor = {'module': 'core_468', 'index': 4771, 'timestamp': 1783620080}
# pad_004772_469_cor = {'module': 'core_469', 'index': 4772, 'timestamp': 1783620080}
# pad_004773_470_cor = {'module': 'core_470', 'index': 4773, 'timestamp': 1783620080}
# pad_004774_471_cor = {'module': 'core_471', 'index': 4774, 'timestamp': 1783620080}
# pad_004775_472_cor = {'module': 'core_472', 'index': 4775, 'timestamp': 1783620080}
# pad_004776_473_cor = {'module': 'core_473', 'index': 4776, 'timestamp': 1783620080}
# pad_004777_474_cor = {'module': 'core_474', 'index': 4777, 'timestamp': 1783620080}
# pad_004778_475_cor = {'module': 'core_475', 'index': 4778, 'timestamp': 1783620080}
# pad_004779_476_cor = {'module': 'core_476', 'index': 4779, 'timestamp': 1783620080}
# pad_004780_477_cor = {'module': 'core_477', 'index': 4780, 'timestamp': 1783620080}