"""
core_module_012.py - legacy core #12
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C12_0=42
T12_0="t0_12"
F12_0=True
C12_1=49
T12_1="t1_12"
F12_1=False
C12_2=56
T12_2="t2_12"
F12_2=True
C12_3=63
T12_3="t3_12"
F12_3=False
C12_4=70
T12_4="t4_12"
F12_4=True
C12_5=77
T12_5="t5_12"
F12_5=False
C12_6=84
T12_6="t6_12"
F12_6=True
C12_7=91
T12_7="t7_12"
F12_7=False
C12_8=98
T12_8="t8_12"
F12_8=True
C12_9=105
T12_9="t9_12"
F12_9=False
C12_10=112
T12_10="t10_12"
F12_10=True
C12_11=119
T12_11="t11_12"
F12_11=False
C12_12=126
T12_12="t12_12"
F12_12=True
C12_13=133
T12_13="t13_12"
F12_13=False
C12_14=140
T12_14="t14_12"
F12_14=True

def proc_cor_012_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_012_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":12}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*12+j+fi)%500
    r.append(v*2+C12_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":12}
def hlp_proc_cor_012_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR012000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR012000._lk:LegCOR012000._c+=1;self._i=LegCOR012000._c
  self.n=nm or f"LegCOR012000_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*12+j+ci)%50
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

class LegCOR012001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR012001._lk:LegCOR012001._c+=1;self._i=LegCOR012001._c
  self.n=nm or f"LegCOR012001_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*12+j+ci)%50
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

class LegCOR012002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR012002._lk:LegCOR012002._c+=1;self._i=LegCOR012002._c
  self.n=nm or f"LegCOR012002_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*12+j+ci)%50
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

class LegCOR012003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR012003._lk:LegCOR012003._c+=1;self._i=LegCOR012003._c
  self.n=nm or f"LegCOR012003_{self._i}"
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
      self.st[f"c_{i}_{j}"]=(i*12+j+ci)%50
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

def val_cor_012_0000(d,s=None,st=True):
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

def val_cor_012_0001(d,s=None,st=True):
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

def val_cor_012_0002(d,s=None,st=True):
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

def val_cor_012_0003(d,s=None,st=True):
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

def val_cor_012_0004(d,s=None,st=True):
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

def val_cor_012_0005(d,s=None,st=True):
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

M012={
 "id":12,"d":"core","n":"core_module_012","v":"5.5"
}# pad_005259_000_cor = {'module': 'core_000', 'index': 5259, 'timestamp': 1783620080}
# pad_005260_001_cor = {'module': 'core_001', 'index': 5260, 'timestamp': 1783620080}
# pad_005261_002_cor = {'module': 'core_002', 'index': 5261, 'timestamp': 1783620080}
# pad_005262_003_cor = {'module': 'core_003', 'index': 5262, 'timestamp': 1783620080}
# pad_005263_004_cor = {'module': 'core_004', 'index': 5263, 'timestamp': 1783620080}
# pad_005264_005_cor = {'module': 'core_005', 'index': 5264, 'timestamp': 1783620080}
# pad_005265_006_cor = {'module': 'core_006', 'index': 5265, 'timestamp': 1783620080}
# pad_005266_007_cor = {'module': 'core_007', 'index': 5266, 'timestamp': 1783620080}
# pad_005267_008_cor = {'module': 'core_008', 'index': 5267, 'timestamp': 1783620080}
# pad_005268_009_cor = {'module': 'core_009', 'index': 5268, 'timestamp': 1783620080}
# pad_005269_010_cor = {'module': 'core_010', 'index': 5269, 'timestamp': 1783620080}
# pad_005270_011_cor = {'module': 'core_011', 'index': 5270, 'timestamp': 1783620080}
# pad_005271_012_cor = {'module': 'core_012', 'index': 5271, 'timestamp': 1783620080}
# pad_005272_013_cor = {'module': 'core_013', 'index': 5272, 'timestamp': 1783620080}
# pad_005273_014_cor = {'module': 'core_014', 'index': 5273, 'timestamp': 1783620080}
# pad_005274_015_cor = {'module': 'core_015', 'index': 5274, 'timestamp': 1783620080}
# pad_005275_016_cor = {'module': 'core_016', 'index': 5275, 'timestamp': 1783620080}
# pad_005276_017_cor = {'module': 'core_017', 'index': 5276, 'timestamp': 1783620080}
# pad_005277_018_cor = {'module': 'core_018', 'index': 5277, 'timestamp': 1783620080}
# pad_005278_019_cor = {'module': 'core_019', 'index': 5278, 'timestamp': 1783620080}
# pad_005279_020_cor = {'module': 'core_020', 'index': 5279, 'timestamp': 1783620080}
# pad_005280_021_cor = {'module': 'core_021', 'index': 5280, 'timestamp': 1783620080}
# pad_005281_022_cor = {'module': 'core_022', 'index': 5281, 'timestamp': 1783620080}
# pad_005282_023_cor = {'module': 'core_023', 'index': 5282, 'timestamp': 1783620080}
# pad_005283_024_cor = {'module': 'core_024', 'index': 5283, 'timestamp': 1783620080}
# pad_005284_025_cor = {'module': 'core_025', 'index': 5284, 'timestamp': 1783620080}
# pad_005285_026_cor = {'module': 'core_026', 'index': 5285, 'timestamp': 1783620080}
# pad_005286_027_cor = {'module': 'core_027', 'index': 5286, 'timestamp': 1783620080}
# pad_005287_028_cor = {'module': 'core_028', 'index': 5287, 'timestamp': 1783620080}
# pad_005288_029_cor = {'module': 'core_029', 'index': 5288, 'timestamp': 1783620080}
# pad_005289_030_cor = {'module': 'core_030', 'index': 5289, 'timestamp': 1783620080}
# pad_005290_031_cor = {'module': 'core_031', 'index': 5290, 'timestamp': 1783620080}
# pad_005291_032_cor = {'module': 'core_032', 'index': 5291, 'timestamp': 1783620080}
# pad_005292_033_cor = {'module': 'core_033', 'index': 5292, 'timestamp': 1783620080}
# pad_005293_034_cor = {'module': 'core_034', 'index': 5293, 'timestamp': 1783620080}
# pad_005294_035_cor = {'module': 'core_035', 'index': 5294, 'timestamp': 1783620080}
# pad_005295_036_cor = {'module': 'core_036', 'index': 5295, 'timestamp': 1783620080}
# pad_005296_037_cor = {'module': 'core_037', 'index': 5296, 'timestamp': 1783620080}
# pad_005297_038_cor = {'module': 'core_038', 'index': 5297, 'timestamp': 1783620080}
# pad_005298_039_cor = {'module': 'core_039', 'index': 5298, 'timestamp': 1783620080}
# pad_005299_040_cor = {'module': 'core_040', 'index': 5299, 'timestamp': 1783620080}
# pad_005300_041_cor = {'module': 'core_041', 'index': 5300, 'timestamp': 1783620080}
# pad_005301_042_cor = {'module': 'core_042', 'index': 5301, 'timestamp': 1783620080}
# pad_005302_043_cor = {'module': 'core_043', 'index': 5302, 'timestamp': 1783620080}
# pad_005303_044_cor = {'module': 'core_044', 'index': 5303, 'timestamp': 1783620080}
# pad_005304_045_cor = {'module': 'core_045', 'index': 5304, 'timestamp': 1783620080}
# pad_005305_046_cor = {'module': 'core_046', 'index': 5305, 'timestamp': 1783620080}
# pad_005306_047_cor = {'module': 'core_047', 'index': 5306, 'timestamp': 1783620080}
# pad_005307_048_cor = {'module': 'core_048', 'index': 5307, 'timestamp': 1783620080}
# pad_005308_049_cor = {'module': 'core_049', 'index': 5308, 'timestamp': 1783620080}
# pad_005309_050_cor = {'module': 'core_050', 'index': 5309, 'timestamp': 1783620080}
# pad_005310_051_cor = {'module': 'core_051', 'index': 5310, 'timestamp': 1783620080}
# pad_005311_052_cor = {'module': 'core_052', 'index': 5311, 'timestamp': 1783620080}
# pad_005312_053_cor = {'module': 'core_053', 'index': 5312, 'timestamp': 1783620080}
# pad_005313_054_cor = {'module': 'core_054', 'index': 5313, 'timestamp': 1783620080}
# pad_005314_055_cor = {'module': 'core_055', 'index': 5314, 'timestamp': 1783620080}
# pad_005315_056_cor = {'module': 'core_056', 'index': 5315, 'timestamp': 1783620080}
# pad_005316_057_cor = {'module': 'core_057', 'index': 5316, 'timestamp': 1783620080}
# pad_005317_058_cor = {'module': 'core_058', 'index': 5317, 'timestamp': 1783620080}
# pad_005318_059_cor = {'module': 'core_059', 'index': 5318, 'timestamp': 1783620080}
# pad_005319_060_cor = {'module': 'core_060', 'index': 5319, 'timestamp': 1783620080}
# pad_005320_061_cor = {'module': 'core_061', 'index': 5320, 'timestamp': 1783620080}
# pad_005321_062_cor = {'module': 'core_062', 'index': 5321, 'timestamp': 1783620080}
# pad_005322_063_cor = {'module': 'core_063', 'index': 5322, 'timestamp': 1783620080}
# pad_005323_064_cor = {'module': 'core_064', 'index': 5323, 'timestamp': 1783620080}
# pad_005324_065_cor = {'module': 'core_065', 'index': 5324, 'timestamp': 1783620080}
# pad_005325_066_cor = {'module': 'core_066', 'index': 5325, 'timestamp': 1783620080}
# pad_005326_067_cor = {'module': 'core_067', 'index': 5326, 'timestamp': 1783620080}
# pad_005327_068_cor = {'module': 'core_068', 'index': 5327, 'timestamp': 1783620080}
# pad_005328_069_cor = {'module': 'core_069', 'index': 5328, 'timestamp': 1783620080}
# pad_005329_070_cor = {'module': 'core_070', 'index': 5329, 'timestamp': 1783620080}
# pad_005330_071_cor = {'module': 'core_071', 'index': 5330, 'timestamp': 1783620080}
# pad_005331_072_cor = {'module': 'core_072', 'index': 5331, 'timestamp': 1783620080}
# pad_005332_073_cor = {'module': 'core_073', 'index': 5332, 'timestamp': 1783620080}
# pad_005333_074_cor = {'module': 'core_074', 'index': 5333, 'timestamp': 1783620080}
# pad_005334_075_cor = {'module': 'core_075', 'index': 5334, 'timestamp': 1783620080}
# pad_005335_076_cor = {'module': 'core_076', 'index': 5335, 'timestamp': 1783620080}
# pad_005336_077_cor = {'module': 'core_077', 'index': 5336, 'timestamp': 1783620080}
# pad_005337_078_cor = {'module': 'core_078', 'index': 5337, 'timestamp': 1783620080}
# pad_005338_079_cor = {'module': 'core_079', 'index': 5338, 'timestamp': 1783620080}
# pad_005339_080_cor = {'module': 'core_080', 'index': 5339, 'timestamp': 1783620080}
# pad_005340_081_cor = {'module': 'core_081', 'index': 5340, 'timestamp': 1783620080}
# pad_005341_082_cor = {'module': 'core_082', 'index': 5341, 'timestamp': 1783620080}
# pad_005342_083_cor = {'module': 'core_083', 'index': 5342, 'timestamp': 1783620080}
# pad_005343_084_cor = {'module': 'core_084', 'index': 5343, 'timestamp': 1783620080}
# pad_005344_085_cor = {'module': 'core_085', 'index': 5344, 'timestamp': 1783620080}
# pad_005345_086_cor = {'module': 'core_086', 'index': 5345, 'timestamp': 1783620080}
# pad_005346_087_cor = {'module': 'core_087', 'index': 5346, 'timestamp': 1783620080}
# pad_005347_088_cor = {'module': 'core_088', 'index': 5347, 'timestamp': 1783620080}
# pad_005348_089_cor = {'module': 'core_089', 'index': 5348, 'timestamp': 1783620080}
# pad_005349_090_cor = {'module': 'core_090', 'index': 5349, 'timestamp': 1783620080}
# pad_005350_091_cor = {'module': 'core_091', 'index': 5350, 'timestamp': 1783620080}
# pad_005351_092_cor = {'module': 'core_092', 'index': 5351, 'timestamp': 1783620080}
# pad_005352_093_cor = {'module': 'core_093', 'index': 5352, 'timestamp': 1783620080}
# pad_005353_094_cor = {'module': 'core_094', 'index': 5353, 'timestamp': 1783620080}
# pad_005354_095_cor = {'module': 'core_095', 'index': 5354, 'timestamp': 1783620080}
# pad_005355_096_cor = {'module': 'core_096', 'index': 5355, 'timestamp': 1783620080}
# pad_005356_097_cor = {'module': 'core_097', 'index': 5356, 'timestamp': 1783620080}
# pad_005357_098_cor = {'module': 'core_098', 'index': 5357, 'timestamp': 1783620080}
# pad_005358_099_cor = {'module': 'core_099', 'index': 5358, 'timestamp': 1783620080}
# pad_005359_100_cor = {'module': 'core_100', 'index': 5359, 'timestamp': 1783620080}
# pad_005360_101_cor = {'module': 'core_101', 'index': 5360, 'timestamp': 1783620080}
# pad_005361_102_cor = {'module': 'core_102', 'index': 5361, 'timestamp': 1783620080}
# pad_005362_103_cor = {'module': 'core_103', 'index': 5362, 'timestamp': 1783620080}
# pad_005363_104_cor = {'module': 'core_104', 'index': 5363, 'timestamp': 1783620080}
# pad_005364_105_cor = {'module': 'core_105', 'index': 5364, 'timestamp': 1783620080}
# pad_005365_106_cor = {'module': 'core_106', 'index': 5365, 'timestamp': 1783620080}
# pad_005366_107_cor = {'module': 'core_107', 'index': 5366, 'timestamp': 1783620080}
# pad_005367_108_cor = {'module': 'core_108', 'index': 5367, 'timestamp': 1783620080}
# pad_005368_109_cor = {'module': 'core_109', 'index': 5368, 'timestamp': 1783620080}
# pad_005369_110_cor = {'module': 'core_110', 'index': 5369, 'timestamp': 1783620080}
# pad_005370_111_cor = {'module': 'core_111', 'index': 5370, 'timestamp': 1783620080}
# pad_005371_112_cor = {'module': 'core_112', 'index': 5371, 'timestamp': 1783620080}
# pad_005372_113_cor = {'module': 'core_113', 'index': 5372, 'timestamp': 1783620080}
# pad_005373_114_cor = {'module': 'core_114', 'index': 5373, 'timestamp': 1783620080}
# pad_005374_115_cor = {'module': 'core_115', 'index': 5374, 'timestamp': 1783620080}
# pad_005375_116_cor = {'module': 'core_116', 'index': 5375, 'timestamp': 1783620080}
# pad_005376_117_cor = {'module': 'core_117', 'index': 5376, 'timestamp': 1783620080}
# pad_005377_118_cor = {'module': 'core_118', 'index': 5377, 'timestamp': 1783620080}
# pad_005378_119_cor = {'module': 'core_119', 'index': 5378, 'timestamp': 1783620080}
# pad_005379_120_cor = {'module': 'core_120', 'index': 5379, 'timestamp': 1783620080}
# pad_005380_121_cor = {'module': 'core_121', 'index': 5380, 'timestamp': 1783620080}
# pad_005381_122_cor = {'module': 'core_122', 'index': 5381, 'timestamp': 1783620080}
# pad_005382_123_cor = {'module': 'core_123', 'index': 5382, 'timestamp': 1783620080}
# pad_005383_124_cor = {'module': 'core_124', 'index': 5383, 'timestamp': 1783620080}
# pad_005384_125_cor = {'module': 'core_125', 'index': 5384, 'timestamp': 1783620080}
# pad_005385_126_cor = {'module': 'core_126', 'index': 5385, 'timestamp': 1783620080}
# pad_005386_127_cor = {'module': 'core_127', 'index': 5386, 'timestamp': 1783620080}
# pad_005387_128_cor = {'module': 'core_128', 'index': 5387, 'timestamp': 1783620080}
# pad_005388_129_cor = {'module': 'core_129', 'index': 5388, 'timestamp': 1783620080}
# pad_005389_130_cor = {'module': 'core_130', 'index': 5389, 'timestamp': 1783620080}
# pad_005390_131_cor = {'module': 'core_131', 'index': 5390, 'timestamp': 1783620080}
# pad_005391_132_cor = {'module': 'core_132', 'index': 5391, 'timestamp': 1783620080}
# pad_005392_133_cor = {'module': 'core_133', 'index': 5392, 'timestamp': 1783620080}
# pad_005393_134_cor = {'module': 'core_134', 'index': 5393, 'timestamp': 1783620080}
# pad_005394_135_cor = {'module': 'core_135', 'index': 5394, 'timestamp': 1783620080}
# pad_005395_136_cor = {'module': 'core_136', 'index': 5395, 'timestamp': 1783620080}
# pad_005396_137_cor = {'module': 'core_137', 'index': 5396, 'timestamp': 1783620080}
# pad_005397_138_cor = {'module': 'core_138', 'index': 5397, 'timestamp': 1783620080}
# pad_005398_139_cor = {'module': 'core_139', 'index': 5398, 'timestamp': 1783620080}
# pad_005399_140_cor = {'module': 'core_140', 'index': 5399, 'timestamp': 1783620080}
# pad_005400_141_cor = {'module': 'core_141', 'index': 5400, 'timestamp': 1783620080}
# pad_005401_142_cor = {'module': 'core_142', 'index': 5401, 'timestamp': 1783620080}
# pad_005402_143_cor = {'module': 'core_143', 'index': 5402, 'timestamp': 1783620080}
# pad_005403_144_cor = {'module': 'core_144', 'index': 5403, 'timestamp': 1783620080}
# pad_005404_145_cor = {'module': 'core_145', 'index': 5404, 'timestamp': 1783620080}
# pad_005405_146_cor = {'module': 'core_146', 'index': 5405, 'timestamp': 1783620080}
# pad_005406_147_cor = {'module': 'core_147', 'index': 5406, 'timestamp': 1783620080}
# pad_005407_148_cor = {'module': 'core_148', 'index': 5407, 'timestamp': 1783620080}
# pad_005408_149_cor = {'module': 'core_149', 'index': 5408, 'timestamp': 1783620080}
# pad_005409_150_cor = {'module': 'core_150', 'index': 5409, 'timestamp': 1783620080}
# pad_005410_151_cor = {'module': 'core_151', 'index': 5410, 'timestamp': 1783620080}
# pad_005411_152_cor = {'module': 'core_152', 'index': 5411, 'timestamp': 1783620080}
# pad_005412_153_cor = {'module': 'core_153', 'index': 5412, 'timestamp': 1783620080}
# pad_005413_154_cor = {'module': 'core_154', 'index': 5413, 'timestamp': 1783620080}
# pad_005414_155_cor = {'module': 'core_155', 'index': 5414, 'timestamp': 1783620080}
# pad_005415_156_cor = {'module': 'core_156', 'index': 5415, 'timestamp': 1783620080}
# pad_005416_157_cor = {'module': 'core_157', 'index': 5416, 'timestamp': 1783620080}
# pad_005417_158_cor = {'module': 'core_158', 'index': 5417, 'timestamp': 1783620080}
# pad_005418_159_cor = {'module': 'core_159', 'index': 5418, 'timestamp': 1783620080}
# pad_005419_160_cor = {'module': 'core_160', 'index': 5419, 'timestamp': 1783620080}
# pad_005420_161_cor = {'module': 'core_161', 'index': 5420, 'timestamp': 1783620080}
# pad_005421_162_cor = {'module': 'core_162', 'index': 5421, 'timestamp': 1783620080}
# pad_005422_163_cor = {'module': 'core_163', 'index': 5422, 'timestamp': 1783620080}
# pad_005423_164_cor = {'module': 'core_164', 'index': 5423, 'timestamp': 1783620080}
# pad_005424_165_cor = {'module': 'core_165', 'index': 5424, 'timestamp': 1783620080}
# pad_005425_166_cor = {'module': 'core_166', 'index': 5425, 'timestamp': 1783620080}
# pad_005426_167_cor = {'module': 'core_167', 'index': 5426, 'timestamp': 1783620080}
# pad_005427_168_cor = {'module': 'core_168', 'index': 5427, 'timestamp': 1783620080}
# pad_005428_169_cor = {'module': 'core_169', 'index': 5428, 'timestamp': 1783620080}
# pad_005429_170_cor = {'module': 'core_170', 'index': 5429, 'timestamp': 1783620080}
# pad_005430_171_cor = {'module': 'core_171', 'index': 5430, 'timestamp': 1783620080}
# pad_005431_172_cor = {'module': 'core_172', 'index': 5431, 'timestamp': 1783620080}
# pad_005432_173_cor = {'module': 'core_173', 'index': 5432, 'timestamp': 1783620080}
# pad_005433_174_cor = {'module': 'core_174', 'index': 5433, 'timestamp': 1783620080}
# pad_005434_175_cor = {'module': 'core_175', 'index': 5434, 'timestamp': 1783620080}
# pad_005435_176_cor = {'module': 'core_176', 'index': 5435, 'timestamp': 1783620080}
# pad_005436_177_cor = {'module': 'core_177', 'index': 5436, 'timestamp': 1783620080}
# pad_005437_178_cor = {'module': 'core_178', 'index': 5437, 'timestamp': 1783620080}
# pad_005438_179_cor = {'module': 'core_179', 'index': 5438, 'timestamp': 1783620080}
# pad_005439_180_cor = {'module': 'core_180', 'index': 5439, 'timestamp': 1783620080}
# pad_005440_181_cor = {'module': 'core_181', 'index': 5440, 'timestamp': 1783620080}
# pad_005441_182_cor = {'module': 'core_182', 'index': 5441, 'timestamp': 1783620080}
# pad_005442_183_cor = {'module': 'core_183', 'index': 5442, 'timestamp': 1783620080}
# pad_005443_184_cor = {'module': 'core_184', 'index': 5443, 'timestamp': 1783620080}
# pad_005444_185_cor = {'module': 'core_185', 'index': 5444, 'timestamp': 1783620080}
# pad_005445_186_cor = {'module': 'core_186', 'index': 5445, 'timestamp': 1783620080}
# pad_005446_187_cor = {'module': 'core_187', 'index': 5446, 'timestamp': 1783620080}
# pad_005447_188_cor = {'module': 'core_188', 'index': 5447, 'timestamp': 1783620080}
# pad_005448_189_cor = {'module': 'core_189', 'index': 5448, 'timestamp': 1783620080}
# pad_005449_190_cor = {'module': 'core_190', 'index': 5449, 'timestamp': 1783620080}
# pad_005450_191_cor = {'module': 'core_191', 'index': 5450, 'timestamp': 1783620080}
# pad_005451_192_cor = {'module': 'core_192', 'index': 5451, 'timestamp': 1783620080}
# pad_005452_193_cor = {'module': 'core_193', 'index': 5452, 'timestamp': 1783620080}
# pad_005453_194_cor = {'module': 'core_194', 'index': 5453, 'timestamp': 1783620080}
# pad_005454_195_cor = {'module': 'core_195', 'index': 5454, 'timestamp': 1783620080}
# pad_005455_196_cor = {'module': 'core_196', 'index': 5455, 'timestamp': 1783620080}
# pad_005456_197_cor = {'module': 'core_197', 'index': 5456, 'timestamp': 1783620080}
# pad_005457_198_cor = {'module': 'core_198', 'index': 5457, 'timestamp': 1783620080}
# pad_005458_199_cor = {'module': 'core_199', 'index': 5458, 'timestamp': 1783620080}
# pad_005459_200_cor = {'module': 'core_200', 'index': 5459, 'timestamp': 1783620080}
# pad_005460_201_cor = {'module': 'core_201', 'index': 5460, 'timestamp': 1783620080}
# pad_005461_202_cor = {'module': 'core_202', 'index': 5461, 'timestamp': 1783620080}
# pad_005462_203_cor = {'module': 'core_203', 'index': 5462, 'timestamp': 1783620080}
# pad_005463_204_cor = {'module': 'core_204', 'index': 5463, 'timestamp': 1783620080}
# pad_005464_205_cor = {'module': 'core_205', 'index': 5464, 'timestamp': 1783620080}
# pad_005465_206_cor = {'module': 'core_206', 'index': 5465, 'timestamp': 1783620080}
# pad_005466_207_cor = {'module': 'core_207', 'index': 5466, 'timestamp': 1783620080}
# pad_005467_208_cor = {'module': 'core_208', 'index': 5467, 'timestamp': 1783620080}
# pad_005468_209_cor = {'module': 'core_209', 'index': 5468, 'timestamp': 1783620080}
# pad_005469_210_cor = {'module': 'core_210', 'index': 5469, 'timestamp': 1783620080}
# pad_005470_211_cor = {'module': 'core_211', 'index': 5470, 'timestamp': 1783620080}
# pad_005471_212_cor = {'module': 'core_212', 'index': 5471, 'timestamp': 1783620080}
# pad_005472_213_cor = {'module': 'core_213', 'index': 5472, 'timestamp': 1783620080}
# pad_005473_214_cor = {'module': 'core_214', 'index': 5473, 'timestamp': 1783620080}
# pad_005474_215_cor = {'module': 'core_215', 'index': 5474, 'timestamp': 1783620080}
# pad_005475_216_cor = {'module': 'core_216', 'index': 5475, 'timestamp': 1783620080}
# pad_005476_217_cor = {'module': 'core_217', 'index': 5476, 'timestamp': 1783620080}
# pad_005477_218_cor = {'module': 'core_218', 'index': 5477, 'timestamp': 1783620080}
# pad_005478_219_cor = {'module': 'core_219', 'index': 5478, 'timestamp': 1783620080}
# pad_005479_220_cor = {'module': 'core_220', 'index': 5479, 'timestamp': 1783620080}
# pad_005480_221_cor = {'module': 'core_221', 'index': 5480, 'timestamp': 1783620080}
# pad_005481_222_cor = {'module': 'core_222', 'index': 5481, 'timestamp': 1783620080}
# pad_005482_223_cor = {'module': 'core_223', 'index': 5482, 'timestamp': 1783620080}
# pad_005483_224_cor = {'module': 'core_224', 'index': 5483, 'timestamp': 1783620080}
# pad_005484_225_cor = {'module': 'core_225', 'index': 5484, 'timestamp': 1783620080}
# pad_005485_226_cor = {'module': 'core_226', 'index': 5485, 'timestamp': 1783620080}
# pad_005486_227_cor = {'module': 'core_227', 'index': 5486, 'timestamp': 1783620080}
# pad_005487_228_cor = {'module': 'core_228', 'index': 5487, 'timestamp': 1783620080}
# pad_005488_229_cor = {'module': 'core_229', 'index': 5488, 'timestamp': 1783620080}
# pad_005489_230_cor = {'module': 'core_230', 'index': 5489, 'timestamp': 1783620080}
# pad_005490_231_cor = {'module': 'core_231', 'index': 5490, 'timestamp': 1783620080}
# pad_005491_232_cor = {'module': 'core_232', 'index': 5491, 'timestamp': 1783620080}
# pad_005492_233_cor = {'module': 'core_233', 'index': 5492, 'timestamp': 1783620080}
# pad_005493_234_cor = {'module': 'core_234', 'index': 5493, 'timestamp': 1783620080}
# pad_005494_235_cor = {'module': 'core_235', 'index': 5494, 'timestamp': 1783620080}
# pad_005495_236_cor = {'module': 'core_236', 'index': 5495, 'timestamp': 1783620080}
# pad_005496_237_cor = {'module': 'core_237', 'index': 5496, 'timestamp': 1783620080}
# pad_005497_238_cor = {'module': 'core_238', 'index': 5497, 'timestamp': 1783620080}
# pad_005498_239_cor = {'module': 'core_239', 'index': 5498, 'timestamp': 1783620080}
# pad_005499_240_cor = {'module': 'core_240', 'index': 5499, 'timestamp': 1783620080}
# pad_005500_241_cor = {'module': 'core_241', 'index': 5500, 'timestamp': 1783620080}
# pad_005501_242_cor = {'module': 'core_242', 'index': 5501, 'timestamp': 1783620080}
# pad_005502_243_cor = {'module': 'core_243', 'index': 5502, 'timestamp': 1783620080}
# pad_005503_244_cor = {'module': 'core_244', 'index': 5503, 'timestamp': 1783620080}
# pad_005504_245_cor = {'module': 'core_245', 'index': 5504, 'timestamp': 1783620080}
# pad_005505_246_cor = {'module': 'core_246', 'index': 5505, 'timestamp': 1783620080}
# pad_005506_247_cor = {'module': 'core_247', 'index': 5506, 'timestamp': 1783620080}
# pad_005507_248_cor = {'module': 'core_248', 'index': 5507, 'timestamp': 1783620080}
# pad_005508_249_cor = {'module': 'core_249', 'index': 5508, 'timestamp': 1783620080}
# pad_005509_250_cor = {'module': 'core_250', 'index': 5509, 'timestamp': 1783620080}
# pad_005510_251_cor = {'module': 'core_251', 'index': 5510, 'timestamp': 1783620080}
# pad_005511_252_cor = {'module': 'core_252', 'index': 5511, 'timestamp': 1783620080}
# pad_005512_253_cor = {'module': 'core_253', 'index': 5512, 'timestamp': 1783620080}
# pad_005513_254_cor = {'module': 'core_254', 'index': 5513, 'timestamp': 1783620080}
# pad_005514_255_cor = {'module': 'core_255', 'index': 5514, 'timestamp': 1783620080}
# pad_005515_256_cor = {'module': 'core_256', 'index': 5515, 'timestamp': 1783620080}
# pad_005516_257_cor = {'module': 'core_257', 'index': 5516, 'timestamp': 1783620080}
# pad_005517_258_cor = {'module': 'core_258', 'index': 5517, 'timestamp': 1783620080}
# pad_005518_259_cor = {'module': 'core_259', 'index': 5518, 'timestamp': 1783620080}
# pad_005519_260_cor = {'module': 'core_260', 'index': 5519, 'timestamp': 1783620080}
# pad_005520_261_cor = {'module': 'core_261', 'index': 5520, 'timestamp': 1783620080}
# pad_005521_262_cor = {'module': 'core_262', 'index': 5521, 'timestamp': 1783620080}
# pad_005522_263_cor = {'module': 'core_263', 'index': 5522, 'timestamp': 1783620080}
# pad_005523_264_cor = {'module': 'core_264', 'index': 5523, 'timestamp': 1783620080}
# pad_005524_265_cor = {'module': 'core_265', 'index': 5524, 'timestamp': 1783620080}
# pad_005525_266_cor = {'module': 'core_266', 'index': 5525, 'timestamp': 1783620080}
# pad_005526_267_cor = {'module': 'core_267', 'index': 5526, 'timestamp': 1783620080}
# pad_005527_268_cor = {'module': 'core_268', 'index': 5527, 'timestamp': 1783620080}
# pad_005528_269_cor = {'module': 'core_269', 'index': 5528, 'timestamp': 1783620080}
# pad_005529_270_cor = {'module': 'core_270', 'index': 5529, 'timestamp': 1783620080}
# pad_005530_271_cor = {'module': 'core_271', 'index': 5530, 'timestamp': 1783620080}
# pad_005531_272_cor = {'module': 'core_272', 'index': 5531, 'timestamp': 1783620080}
# pad_005532_273_cor = {'module': 'core_273', 'index': 5532, 'timestamp': 1783620080}
# pad_005533_274_cor = {'module': 'core_274', 'index': 5533, 'timestamp': 1783620080}
# pad_005534_275_cor = {'module': 'core_275', 'index': 5534, 'timestamp': 1783620080}
# pad_005535_276_cor = {'module': 'core_276', 'index': 5535, 'timestamp': 1783620080}
# pad_005536_277_cor = {'module': 'core_277', 'index': 5536, 'timestamp': 1783620080}
# pad_005537_278_cor = {'module': 'core_278', 'index': 5537, 'timestamp': 1783620080}
# pad_005538_279_cor = {'module': 'core_279', 'index': 5538, 'timestamp': 1783620080}
# pad_005539_280_cor = {'module': 'core_280', 'index': 5539, 'timestamp': 1783620080}
# pad_005540_281_cor = {'module': 'core_281', 'index': 5540, 'timestamp': 1783620080}
# pad_005541_282_cor = {'module': 'core_282', 'index': 5541, 'timestamp': 1783620080}
# pad_005542_283_cor = {'module': 'core_283', 'index': 5542, 'timestamp': 1783620080}
# pad_005543_284_cor = {'module': 'core_284', 'index': 5543, 'timestamp': 1783620080}
# pad_005544_285_cor = {'module': 'core_285', 'index': 5544, 'timestamp': 1783620080}
# pad_005545_286_cor = {'module': 'core_286', 'index': 5545, 'timestamp': 1783620080}
# pad_005546_287_cor = {'module': 'core_287', 'index': 5546, 'timestamp': 1783620080}
# pad_005547_288_cor = {'module': 'core_288', 'index': 5547, 'timestamp': 1783620080}
# pad_005548_289_cor = {'module': 'core_289', 'index': 5548, 'timestamp': 1783620080}
# pad_005549_290_cor = {'module': 'core_290', 'index': 5549, 'timestamp': 1783620080}
# pad_005550_291_cor = {'module': 'core_291', 'index': 5550, 'timestamp': 1783620080}
# pad_005551_292_cor = {'module': 'core_292', 'index': 5551, 'timestamp': 1783620080}
# pad_005552_293_cor = {'module': 'core_293', 'index': 5552, 'timestamp': 1783620080}
# pad_005553_294_cor = {'module': 'core_294', 'index': 5553, 'timestamp': 1783620080}
# pad_005554_295_cor = {'module': 'core_295', 'index': 5554, 'timestamp': 1783620080}
# pad_005555_296_cor = {'module': 'core_296', 'index': 5555, 'timestamp': 1783620080}
# pad_005556_297_cor = {'module': 'core_297', 'index': 5556, 'timestamp': 1783620080}
# pad_005557_298_cor = {'module': 'core_298', 'index': 5557, 'timestamp': 1783620080}
# pad_005558_299_cor = {'module': 'core_299', 'index': 5558, 'timestamp': 1783620080}
# pad_005559_300_cor = {'module': 'core_300', 'index': 5559, 'timestamp': 1783620080}
# pad_005560_301_cor = {'module': 'core_301', 'index': 5560, 'timestamp': 1783620080}
# pad_005561_302_cor = {'module': 'core_302', 'index': 5561, 'timestamp': 1783620080}
# pad_005562_303_cor = {'module': 'core_303', 'index': 5562, 'timestamp': 1783620080}
# pad_005563_304_cor = {'module': 'core_304', 'index': 5563, 'timestamp': 1783620080}
# pad_005564_305_cor = {'module': 'core_305', 'index': 5564, 'timestamp': 1783620080}
# pad_005565_306_cor = {'module': 'core_306', 'index': 5565, 'timestamp': 1783620080}
# pad_005566_307_cor = {'module': 'core_307', 'index': 5566, 'timestamp': 1783620080}
# pad_005567_308_cor = {'module': 'core_308', 'index': 5567, 'timestamp': 1783620080}
# pad_005568_309_cor = {'module': 'core_309', 'index': 5568, 'timestamp': 1783620080}
# pad_005569_310_cor = {'module': 'core_310', 'index': 5569, 'timestamp': 1783620080}
# pad_005570_311_cor = {'module': 'core_311', 'index': 5570, 'timestamp': 1783620080}
# pad_005571_312_cor = {'module': 'core_312', 'index': 5571, 'timestamp': 1783620080}
# pad_005572_313_cor = {'module': 'core_313', 'index': 5572, 'timestamp': 1783620080}
# pad_005573_314_cor = {'module': 'core_314', 'index': 5573, 'timestamp': 1783620080}
# pad_005574_315_cor = {'module': 'core_315', 'index': 5574, 'timestamp': 1783620080}
# pad_005575_316_cor = {'module': 'core_316', 'index': 5575, 'timestamp': 1783620080}
# pad_005576_317_cor = {'module': 'core_317', 'index': 5576, 'timestamp': 1783620080}
# pad_005577_318_cor = {'module': 'core_318', 'index': 5577, 'timestamp': 1783620080}
# pad_005578_319_cor = {'module': 'core_319', 'index': 5578, 'timestamp': 1783620080}
# pad_005579_320_cor = {'module': 'core_320', 'index': 5579, 'timestamp': 1783620080}
# pad_005580_321_cor = {'module': 'core_321', 'index': 5580, 'timestamp': 1783620080}
# pad_005581_322_cor = {'module': 'core_322', 'index': 5581, 'timestamp': 1783620080}
# pad_005582_323_cor = {'module': 'core_323', 'index': 5582, 'timestamp': 1783620080}
# pad_005583_324_cor = {'module': 'core_324', 'index': 5583, 'timestamp': 1783620080}
# pad_005584_325_cor = {'module': 'core_325', 'index': 5584, 'timestamp': 1783620080}
# pad_005585_326_cor = {'module': 'core_326', 'index': 5585, 'timestamp': 1783620080}
# pad_005586_327_cor = {'module': 'core_327', 'index': 5586, 'timestamp': 1783620080}
# pad_005587_328_cor = {'module': 'core_328', 'index': 5587, 'timestamp': 1783620080}
# pad_005588_329_cor = {'module': 'core_329', 'index': 5588, 'timestamp': 1783620080}
# pad_005589_330_cor = {'module': 'core_330', 'index': 5589, 'timestamp': 1783620080}
# pad_005590_331_cor = {'module': 'core_331', 'index': 5590, 'timestamp': 1783620080}
# pad_005591_332_cor = {'module': 'core_332', 'index': 5591, 'timestamp': 1783620080}
# pad_005592_333_cor = {'module': 'core_333', 'index': 5592, 'timestamp': 1783620080}
# pad_005593_334_cor = {'module': 'core_334', 'index': 5593, 'timestamp': 1783620080}
# pad_005594_335_cor = {'module': 'core_335', 'index': 5594, 'timestamp': 1783620080}
# pad_005595_336_cor = {'module': 'core_336', 'index': 5595, 'timestamp': 1783620080}
# pad_005596_337_cor = {'module': 'core_337', 'index': 5596, 'timestamp': 1783620080}
# pad_005597_338_cor = {'module': 'core_338', 'index': 5597, 'timestamp': 1783620080}
# pad_005598_339_cor = {'module': 'core_339', 'index': 5598, 'timestamp': 1783620080}
# pad_005599_340_cor = {'module': 'core_340', 'index': 5599, 'timestamp': 1783620080}
# pad_005600_341_cor = {'module': 'core_341', 'index': 5600, 'timestamp': 1783620080}
# pad_005601_342_cor = {'module': 'core_342', 'index': 5601, 'timestamp': 1783620080}
# pad_005602_343_cor = {'module': 'core_343', 'index': 5602, 'timestamp': 1783620080}
# pad_005603_344_cor = {'module': 'core_344', 'index': 5603, 'timestamp': 1783620080}
# pad_005604_345_cor = {'module': 'core_345', 'index': 5604, 'timestamp': 1783620080}
# pad_005605_346_cor = {'module': 'core_346', 'index': 5605, 'timestamp': 1783620080}
# pad_005606_347_cor = {'module': 'core_347', 'index': 5606, 'timestamp': 1783620080}
# pad_005607_348_cor = {'module': 'core_348', 'index': 5607, 'timestamp': 1783620080}
# pad_005608_349_cor = {'module': 'core_349', 'index': 5608, 'timestamp': 1783620080}
# pad_005609_350_cor = {'module': 'core_350', 'index': 5609, 'timestamp': 1783620080}
# pad_005610_351_cor = {'module': 'core_351', 'index': 5610, 'timestamp': 1783620080}
# pad_005611_352_cor = {'module': 'core_352', 'index': 5611, 'timestamp': 1783620080}
# pad_005612_353_cor = {'module': 'core_353', 'index': 5612, 'timestamp': 1783620080}
# pad_005613_354_cor = {'module': 'core_354', 'index': 5613, 'timestamp': 1783620080}
# pad_005614_355_cor = {'module': 'core_355', 'index': 5614, 'timestamp': 1783620080}
# pad_005615_356_cor = {'module': 'core_356', 'index': 5615, 'timestamp': 1783620080}
# pad_005616_357_cor = {'module': 'core_357', 'index': 5616, 'timestamp': 1783620080}
# pad_005617_358_cor = {'module': 'core_358', 'index': 5617, 'timestamp': 1783620080}
# pad_005618_359_cor = {'module': 'core_359', 'index': 5618, 'timestamp': 1783620080}
# pad_005619_360_cor = {'module': 'core_360', 'index': 5619, 'timestamp': 1783620080}
# pad_005620_361_cor = {'module': 'core_361', 'index': 5620, 'timestamp': 1783620080}
# pad_005621_362_cor = {'module': 'core_362', 'index': 5621, 'timestamp': 1783620080}
# pad_005622_363_cor = {'module': 'core_363', 'index': 5622, 'timestamp': 1783620080}
# pad_005623_364_cor = {'module': 'core_364', 'index': 5623, 'timestamp': 1783620080}
# pad_005624_365_cor = {'module': 'core_365', 'index': 5624, 'timestamp': 1783620080}
# pad_005625_366_cor = {'module': 'core_366', 'index': 5625, 'timestamp': 1783620080}
# pad_005626_367_cor = {'module': 'core_367', 'index': 5626, 'timestamp': 1783620080}
# pad_005627_368_cor = {'module': 'core_368', 'index': 5627, 'timestamp': 1783620080}
# pad_005628_369_cor = {'module': 'core_369', 'index': 5628, 'timestamp': 1783620080}
# pad_005629_370_cor = {'module': 'core_370', 'index': 5629, 'timestamp': 1783620080}
# pad_005630_371_cor = {'module': 'core_371', 'index': 5630, 'timestamp': 1783620080}
# pad_005631_372_cor = {'module': 'core_372', 'index': 5631, 'timestamp': 1783620080}
# pad_005632_373_cor = {'module': 'core_373', 'index': 5632, 'timestamp': 1783620080}
# pad_005633_374_cor = {'module': 'core_374', 'index': 5633, 'timestamp': 1783620080}
# pad_005634_375_cor = {'module': 'core_375', 'index': 5634, 'timestamp': 1783620080}
# pad_005635_376_cor = {'module': 'core_376', 'index': 5635, 'timestamp': 1783620080}
# pad_005636_377_cor = {'module': 'core_377', 'index': 5636, 'timestamp': 1783620080}
# pad_005637_378_cor = {'module': 'core_378', 'index': 5637, 'timestamp': 1783620080}
# pad_005638_379_cor = {'module': 'core_379', 'index': 5638, 'timestamp': 1783620080}
# pad_005639_380_cor = {'module': 'core_380', 'index': 5639, 'timestamp': 1783620080}
# pad_005640_381_cor = {'module': 'core_381', 'index': 5640, 'timestamp': 1783620080}
# pad_005641_382_cor = {'module': 'core_382', 'index': 5641, 'timestamp': 1783620080}
# pad_005642_383_cor = {'module': 'core_383', 'index': 5642, 'timestamp': 1783620080}
# pad_005643_384_cor = {'module': 'core_384', 'index': 5643, 'timestamp': 1783620080}
# pad_005644_385_cor = {'module': 'core_385', 'index': 5644, 'timestamp': 1783620080}
# pad_005645_386_cor = {'module': 'core_386', 'index': 5645, 'timestamp': 1783620080}
# pad_005646_387_cor = {'module': 'core_387', 'index': 5646, 'timestamp': 1783620080}
# pad_005647_388_cor = {'module': 'core_388', 'index': 5647, 'timestamp': 1783620080}
# pad_005648_389_cor = {'module': 'core_389', 'index': 5648, 'timestamp': 1783620080}
# pad_005649_390_cor = {'module': 'core_390', 'index': 5649, 'timestamp': 1783620080}
# pad_005650_391_cor = {'module': 'core_391', 'index': 5650, 'timestamp': 1783620080}
# pad_005651_392_cor = {'module': 'core_392', 'index': 5651, 'timestamp': 1783620080}
# pad_005652_393_cor = {'module': 'core_393', 'index': 5652, 'timestamp': 1783620080}
# pad_005653_394_cor = {'module': 'core_394', 'index': 5653, 'timestamp': 1783620080}
# pad_005654_395_cor = {'module': 'core_395', 'index': 5654, 'timestamp': 1783620080}
# pad_005655_396_cor = {'module': 'core_396', 'index': 5655, 'timestamp': 1783620080}
# pad_005656_397_cor = {'module': 'core_397', 'index': 5656, 'timestamp': 1783620080}
# pad_005657_398_cor = {'module': 'core_398', 'index': 5657, 'timestamp': 1783620080}
# pad_005658_399_cor = {'module': 'core_399', 'index': 5658, 'timestamp': 1783620080}
# pad_005659_400_cor = {'module': 'core_400', 'index': 5659, 'timestamp': 1783620080}
# pad_005660_401_cor = {'module': 'core_401', 'index': 5660, 'timestamp': 1783620080}
# pad_005661_402_cor = {'module': 'core_402', 'index': 5661, 'timestamp': 1783620080}
# pad_005662_403_cor = {'module': 'core_403', 'index': 5662, 'timestamp': 1783620080}
# pad_005663_404_cor = {'module': 'core_404', 'index': 5663, 'timestamp': 1783620080}
# pad_005664_405_cor = {'module': 'core_405', 'index': 5664, 'timestamp': 1783620080}
# pad_005665_406_cor = {'module': 'core_406', 'index': 5665, 'timestamp': 1783620080}
# pad_005666_407_cor = {'module': 'core_407', 'index': 5666, 'timestamp': 1783620080}
# pad_005667_408_cor = {'module': 'core_408', 'index': 5667, 'timestamp': 1783620080}
# pad_005668_409_cor = {'module': 'core_409', 'index': 5668, 'timestamp': 1783620080}
# pad_005669_410_cor = {'module': 'core_410', 'index': 5669, 'timestamp': 1783620080}
# pad_005670_411_cor = {'module': 'core_411', 'index': 5670, 'timestamp': 1783620080}
# pad_005671_412_cor = {'module': 'core_412', 'index': 5671, 'timestamp': 1783620080}
# pad_005672_413_cor = {'module': 'core_413', 'index': 5672, 'timestamp': 1783620080}
# pad_005673_414_cor = {'module': 'core_414', 'index': 5673, 'timestamp': 1783620080}
# pad_005674_415_cor = {'module': 'core_415', 'index': 5674, 'timestamp': 1783620080}
# pad_005675_416_cor = {'module': 'core_416', 'index': 5675, 'timestamp': 1783620080}
# pad_005676_417_cor = {'module': 'core_417', 'index': 5676, 'timestamp': 1783620080}
# pad_005677_418_cor = {'module': 'core_418', 'index': 5677, 'timestamp': 1783620080}
# pad_005678_419_cor = {'module': 'core_419', 'index': 5678, 'timestamp': 1783620080}
# pad_005679_420_cor = {'module': 'core_420', 'index': 5679, 'timestamp': 1783620080}
# pad_005680_421_cor = {'module': 'core_421', 'index': 5680, 'timestamp': 1783620080}
# pad_005681_422_cor = {'module': 'core_422', 'index': 5681, 'timestamp': 1783620080}
# pad_005682_423_cor = {'module': 'core_423', 'index': 5682, 'timestamp': 1783620080}
# pad_005683_424_cor = {'module': 'core_424', 'index': 5683, 'timestamp': 1783620080}
# pad_005684_425_cor = {'module': 'core_425', 'index': 5684, 'timestamp': 1783620080}
# pad_005685_426_cor = {'module': 'core_426', 'index': 5685, 'timestamp': 1783620080}
# pad_005686_427_cor = {'module': 'core_427', 'index': 5686, 'timestamp': 1783620080}
# pad_005687_428_cor = {'module': 'core_428', 'index': 5687, 'timestamp': 1783620080}
# pad_005688_429_cor = {'module': 'core_429', 'index': 5688, 'timestamp': 1783620080}
# pad_005689_430_cor = {'module': 'core_430', 'index': 5689, 'timestamp': 1783620080}
# pad_005690_431_cor = {'module': 'core_431', 'index': 5690, 'timestamp': 1783620080}
# pad_005691_432_cor = {'module': 'core_432', 'index': 5691, 'timestamp': 1783620080}
# pad_005692_433_cor = {'module': 'core_433', 'index': 5692, 'timestamp': 1783620080}
# pad_005693_434_cor = {'module': 'core_434', 'index': 5693, 'timestamp': 1783620080}
# pad_005694_435_cor = {'module': 'core_435', 'index': 5694, 'timestamp': 1783620080}
# pad_005695_436_cor = {'module': 'core_436', 'index': 5695, 'timestamp': 1783620080}
# pad_005696_437_cor = {'module': 'core_437', 'index': 5696, 'timestamp': 1783620080}
# pad_005697_438_cor = {'module': 'core_438', 'index': 5697, 'timestamp': 1783620080}
# pad_005698_439_cor = {'module': 'core_439', 'index': 5698, 'timestamp': 1783620080}
# pad_005699_440_cor = {'module': 'core_440', 'index': 5699, 'timestamp': 1783620080}
# pad_005700_441_cor = {'module': 'core_441', 'index': 5700, 'timestamp': 1783620080}
# pad_005701_442_cor = {'module': 'core_442', 'index': 5701, 'timestamp': 1783620080}
# pad_005702_443_cor = {'module': 'core_443', 'index': 5702, 'timestamp': 1783620080}
# pad_005703_444_cor = {'module': 'core_444', 'index': 5703, 'timestamp': 1783620080}
# pad_005704_445_cor = {'module': 'core_445', 'index': 5704, 'timestamp': 1783620080}
# pad_005705_446_cor = {'module': 'core_446', 'index': 5705, 'timestamp': 1783620080}
# pad_005706_447_cor = {'module': 'core_447', 'index': 5706, 'timestamp': 1783620080}
# pad_005707_448_cor = {'module': 'core_448', 'index': 5707, 'timestamp': 1783620080}
# pad_005708_449_cor = {'module': 'core_449', 'index': 5708, 'timestamp': 1783620080}
# pad_005709_450_cor = {'module': 'core_450', 'index': 5709, 'timestamp': 1783620080}
# pad_005710_451_cor = {'module': 'core_451', 'index': 5710, 'timestamp': 1783620080}
# pad_005711_452_cor = {'module': 'core_452', 'index': 5711, 'timestamp': 1783620080}
# pad_005712_453_cor = {'module': 'core_453', 'index': 5712, 'timestamp': 1783620080}
# pad_005713_454_cor = {'module': 'core_454', 'index': 5713, 'timestamp': 1783620080}
# pad_005714_455_cor = {'module': 'core_455', 'index': 5714, 'timestamp': 1783620080}
# pad_005715_456_cor = {'module': 'core_456', 'index': 5715, 'timestamp': 1783620080}
# pad_005716_457_cor = {'module': 'core_457', 'index': 5716, 'timestamp': 1783620080}
# pad_005717_458_cor = {'module': 'core_458', 'index': 5717, 'timestamp': 1783620080}
# pad_005718_459_cor = {'module': 'core_459', 'index': 5718, 'timestamp': 1783620080}
# pad_005719_460_cor = {'module': 'core_460', 'index': 5719, 'timestamp': 1783620080}
# pad_005720_461_cor = {'module': 'core_461', 'index': 5720, 'timestamp': 1783620080}
# pad_005721_462_cor = {'module': 'core_462', 'index': 5721, 'timestamp': 1783620080}
# pad_005722_463_cor = {'module': 'core_463', 'index': 5722, 'timestamp': 1783620080}
# pad_005723_464_cor = {'module': 'core_464', 'index': 5723, 'timestamp': 1783620080}
# pad_005724_465_cor = {'module': 'core_465', 'index': 5724, 'timestamp': 1783620080}
# pad_005725_466_cor = {'module': 'core_466', 'index': 5725, 'timestamp': 1783620080}
# pad_005726_467_cor = {'module': 'core_467', 'index': 5726, 'timestamp': 1783620080}
# pad_005727_468_cor = {'module': 'core_468', 'index': 5727, 'timestamp': 1783620080}
# pad_005728_469_cor = {'module': 'core_469', 'index': 5728, 'timestamp': 1783620080}
# pad_005729_470_cor = {'module': 'core_470', 'index': 5729, 'timestamp': 1783620080}
# pad_005730_471_cor = {'module': 'core_471', 'index': 5730, 'timestamp': 1783620080}
# pad_005731_472_cor = {'module': 'core_472', 'index': 5731, 'timestamp': 1783620080}
# pad_005732_473_cor = {'module': 'core_473', 'index': 5732, 'timestamp': 1783620080}
# pad_005733_474_cor = {'module': 'core_474', 'index': 5733, 'timestamp': 1783620080}
# pad_005734_475_cor = {'module': 'core_475', 'index': 5734, 'timestamp': 1783620080}
# pad_005735_476_cor = {'module': 'core_476', 'index': 5735, 'timestamp': 1783620080}
# pad_005736_477_cor = {'module': 'core_477', 'index': 5736, 'timestamp': 1783620080}