#-*- coding:utf-8 -*-

# myLib.py : Personal Library on Jupyter Notebook Environment for python beginners
# - Python 초보자의 학습곡선 단축을 위한 '초보자가 직접 작성&사용'하는 Function이나 정보 모음. 
# - 본인이 만들어서 직접 사용하는 것으로, 오류 가능성 항상 있음에 유의.
# - 향후 『import ./myLib』으로 사용할 수 있도록 변경해야 하는 과제가 있음.

# ▣ 자주 사용하는 jupyter notebook cell 명령어
#   %run -i ./myLib.py

# ▣ 자주 사용하는 conda 명령어
# conda env list                    # conda 가상환경 확인
# conda activate r-reticulate
# conda list | find /N /I "scikit"  # 설치된 Module 확인
# 윈도우> start /b jupyter notebook
# conda update conda   
# conda create -n TF2Keras tensorflow numpy scipy sympy matplotlib seaborn pandas pandas-profiling scikit-learn jupyterlab tensorflow-gpu gensim bokeh jedi jpype1 kiwisolver nltk spacy statsmodels tqdm pydot
# python> from tensorflow.python.client import device_lib
# python> device_lib.list_local_devices()

import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sns
# scipy, sympy, bokeh, seaborn, sklearn, tensorflow, keras, plotnine
# import statsmodels.api as sm
# import statsmodels.formula.api as smf

np.set_printoptions(precision=5, suppress=True)  # line매직을 사용한 유사 기능 : %precision 5

# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl # 이 이하의 몇 줄은 마크 페너의 mlwpy.py에서 사용하는 python 모듈임
import itertools as it, collections as co, functools as ft
import sklearn, warnings, glob, patsy, textwrap

## ---------- matplotlib 한글 폰트 검색 및 반영 ---------- ##
# (1) 설치된 Font 중 사용 가능한 한글 폰트 찾기
# from matplotlib import font_manager
# fm = font_manager.FontManager()

# fm.ttflist
# (2) matplotlib에 한글 폰트 반영
# plt.rcParams['font.family'] = 'Malgun Gothic'  # 음수(-)가 잘 못 표시되는 관계로 주석 처리함. 2020.03.25

# (3) 위와 같이 했을 때 안되면, 다음 2개 중 하나로 처리한다.
# plt.rc('font', family='Gulim')
# plt.rcParams['font.family'] = 'Gulim'
## ---------- matplotlib 한글 폰트 검색 및 반영 ---------- ##

import os, re, sys, io, importlib, sqlite3, sympy, matplotlib, time, inspect, math, pydot
# https://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it
from datetime import datetime
from IPython.display import Markdown, display, Image, IFrame # https://stackoverflow.com/questions/19470099/view-pdf-image-in-an-ipython-notebook
from mpl_toolkits.mplot3d import Axes3D

## ------------------------------------------------------------------------------------------- ##
def getSubClasses(aObj):
    aClass = aObj if type(aObj) == type(object) else aObj.__class__
    tmplist = aClass.__subclasses__()
    if len(tmplist) == 0:
        result = list(aClass)
    elif len(tmplist) > 0:
        cnt = 0
        returnlist = []
        for item in tmplist:
            if len(item.__subclasses__()) > 0:
                returnlist.append(getSubClasses(item))
            else:
                returnlist.append(item)
        result = {aClass : returnlist}
    return result

def printSubClasses(anySequence, cnt=0, indent_str = ' ㆍ'):  
    # [Foo.__name__, Foo.__subclasses__()] ★★★ https://www.python-course.eu/index.php ★★★
    # print( 'length : ', len(anySequence) if hasattr(anySequence,'__len__') else 0, "\treceive : ", anySequence)
    if (len(anySequence) if hasattr(anySequence,'__len__') else 0) > 0:
        for dKey, dVal in anySequence.items():
            # print("PROCESSING : ", dVal, " in ", dKey.__name__)
            print(cnt, indent_str * cnt, dKey.__name__)
            cnt = cnt + 1
            if hasattr(dVal[0], 'items'):
                for item in dVal:
                    printSubClasses(item, cnt)
            else:
                print(cnt, indent_str * cnt, dVal[0].__name__)
            cnt = cnt - 1
    else:
        print(cnt, indent_str * cnt, anySequence.__name__)

# getSubClasses 및 printSubClasses 검증
# class Foo(object): pass
# class Bar(Foo): pass
# class Bing(Bar): pass
# class Baz(Foo): pass
# class MPrnt(object): pass
# class MultiIn(Foo, MPrnt): pass
# aDict = {Foo:[{Bar:[Bing]}, Baz, MultiIn], MPrnt:[MultiIn]}

# printSubClasses(getSubClasses(Foo))
# printSubClasses(getSubClasses(MPrnt))

## ------------------------------------------------------------------------------------------- ##
def hasattrCatchError(obj, name, dispError=False):
    """
    pandas DataFrame의 속성 '_constructor_expanddim'에 대해 descobj() 실행 시 
    NotImplementedError가 발생하여 이를 실행 중에 인지하고 처리하기 위해 작성함.
    결국, 각종 이유로 인해 오류도 없고, 해당 속성이 있을 경우에만 True를 Return하도록 함.

    참조 URL : https://stackoverflow.com/questions/4990718/about-catching-any-exception 
    """
    try:
        hasattr(obj, name)
    except Exception as e:  # 오류 발생 시
        if dispError:
            print(name, '\n☞', e, '\n☞ Document :', e.__doc__)
        return False
    else:                   # 성공적으로 실행 시
        return hasattr(obj, name)

## ------------------------------------------------------------------------------------------- ##
def hasproperty(strObj, rtnPropertyTF=False):  # 참고, 유사 ≒ hasattr('object')
    """
    hasattr(object, '속성명')의 기능을 참고하여 작성한 것으로서
    hasattr이 특정 속성(Property)에 대해 True/False만 return해 주는 것에서 더 나아가 
    string으로 『object.속성명』 방식으로 전달하면 
    『속성 -> class -> mro()』 정보가 표시되도록 했습니다.
    """
    try:
        p = eval(strObj)  # p = object's property
        if hasattr(type(p),'mro'):
            if rtnPropertyTF: # Class Property = Attribute + Method 
                return True, type(p).mro()[0].__name__
            else:
                return type(p).mro()[0].__name__  # mro() vs __mro__
        else:
            return None

    except AttributeError:
        if rtnPropertyTF:  # Return "해당 Property 존재 여부" 
            return False, strObj + " doesn't exist!"
        else:
            return strObj + " doesn't exist!"

    except TypeError:
        try:
            if rtnPropertyTF: # Class Property = Attribute + Method 
                return True, type(p).__mro__[0].__name__
            else:
                return type(p).__mro__[0].__name__  # mro() vs __mro__
        except TypeError:
            if rtnPropertyTF:
                return False, strObj + ' : N/A'
            else:
                return strObj + ' : N/A' # 'The argument 1 must be a string!'

## ------------------------------------------------------------------------------------------- ##
def descobj(strObj, show_property=True, pWidth=90):
    """
    기본적으로 클래스 또는 Object의 (다중 포함) 상속관계를 파악하기 위한 것이며
    Property들에 대해서는 (callable인지 아닌 지를 알기 위해) function 또는 method인지를
    파악하기 위해 작성했습니다.

    또, hasattr은 class나 object의 속성명을 알아야 실행할 수 있는데, 
    하위의 속성명을 몰라도 object나 class에서 파악할 수 있는 기능을 추가했습니다.

    결국, 『① 내장 dir()과 hasattr()의 기능을 포괄하며 ②상속 관계 파악을 위한 정보』를 제공합니다.
    향후 regular expression을 사용하여 원하는 속성만 나타나도록 조절하는 기능을 추가할 것입니다.

    참고로, print function에 대한 file.stdout 출력은 다음과 같이 cell magic을 써서 저장할 수 있습니다.
    Cell①> %%capture capture_output --no-stderr
            descobj('A') # https://www.scrygroup.com/tutorial/2019-03-09/capturing_jupyter_cell_output
    Cell②> strVar = capture_output.stdout
            for item in strVar.split('\n'):  # '\n'을 기준으로 분리, list에 저장
                print(item)                  # 별도 저장된 문자열 정보 사용
    """
    boldFR = '\033[1m'; boldTO = '\033[0m'  # myLib에서는 descobj 밖으로...
    def print_class(aClass, lv=1):
        for item in aClass.__bases__:
            print('ㆍ'*lv, item.__name__)
            lv = lv+1
            print_class(item, lv)
    try:   
        obj = eval(strObj)
        if type(obj) == type(object):  # class
            print('* Parent classes of Class', boldFR, strObj, boldTO, '\t(ID :', id(obj), ')' )
            tmpClassName = obj.__name__
            print('-' * pWidth)
            print_class(obj)          
        else:                          # object
            print('* Parent classes of Object', boldFR, strObj, boldTO,
                  '\t(Class :', obj.__class__.__name__, '\tID :', id(obj), ')' ) 
            tmpClassName = obj.__class__.__name__
            print('-' * pWidth)
            print_class(obj.__class__)

        if show_property == True:
            print('\n* Properties of', boldFR, strObj, boldTO) 
            print('-' * pWidth)
            strItems = sorted(dir(eval(strObj)))
            for i in range(len(strItems)):
                if hasattrCatchError(obj, strItems[i]):  # hasattr() 결과 True인 경우 (Exception 발생 없고, attr이 있는 경우)
                    print("{:5} {:45} {:45}".format(i+1, strItems[i], hasproperty(strObj + '.' + strItems[i])))
                else:
                # if tmpClassName == 'DataFrame' and strItems[i] == '_constructor_expanddim':
                #     # pandas.core.frame.DataFrame._constructor_expanddim : NotImplementedError 
                #     print("{:5} {:45} {:45}".format(i+1, strItems[i], 'NotImplementedError !!!'))
                    print("{:5} {:45} {:45}".format(i+1, strItems[i], '***** N/A *****'))

    except TypeError: 
        print('TypeError:', strObj, 'must be a string, bytes or code object!')
    except NameError:
        print('NameError:', strObj, 'is not defined or inherited from \'object\'')

## ------------------------------------------------------------------------------------------- ##
def compobj(strObj1, strObj2, pWidth=45):  # Comparison of 2 Objects
    """
    주로 class와 그 class를 상속한 object의 property들을 비교하기 위한 것이며
    전혀 다른 class vs. class 또는 object vs. object에 대해 실행하는 것도 가능합니다.
    단, 이 경우 좌, 우에 표시되는 property들이 같은 것이라도 다른 줄(row)에 표시될 수 있습니다.
    """
    try:
        dirResult = []
        dirResult.insert(0, list(dir(eval(strObj1))))  
        dirResult.insert(1, list(dir(eval(strObj2))))

        x = len(dirResult[0])
        y = len(dirResult[1])
        len_max = x if x >= y else y
        len_min = x if x <  y else y
        len_diff = abs(x - y)

        print("SerNo","{:45} {:45}".format('obj1: ' + strObj1 + ', type: ' + type(eval(strObj1)).__name__, 
                                         'obj2: ' + strObj2 + ', type: ' + type(eval(strObj2)).__name__))
        print("-----",'-' * pWidth, '-' * pWidth)

        for i in range(len_max):
            print_flag = 'careful'
            if len_diff == 0 and len_max > 0:
                print_flag = 'OK'
            elif len_diff != 0 and i <= len_min - 1:
                print_flag = 'OK'
            else:
                print_flag = 'x' if x > y else 'y'

            if print_flag == 'OK':
                print("{:5} {:45} {:45}".format(i+1, dirResult[0][i], dirResult[1][i]))
            elif print_flag == 'x':
                print("{:5} {:45} {:45}".format(i+1, dirResult[0][i], ' '))
            elif print_flag == 'y':
                print("{:5} {:45} {:45}".format(i+1, ' ',             dirResult[1][i]))
            else:
                continue

    except TypeError: 
        print('TypeError: Every parameter must be a string, bytes or code object!')
    except NameError:
        print('NameError: One or Both of parameters are not defined!')

##  123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789  ##

## =========================================================================================== ##
##                                      Start of class my                                      ##
## =========================================================================================== ##
class my:  # import myLibClass; my = myLibClass.myLib()
  ## 참고 : https://item4.blog/2015-07-18/Some-Ambiguousness-in-Python-Tutorial-Call-by-What/
  #  Python은 함수를 실행할때 Call by reference같은 느낌으로 reference를 넘겨줍니다. 
  #  하지만 이때 넘겨주는 것은 변수(Variable)의 reference가 아니라 변수가 담고 있는 자료(Data)의 reference입니다. 
  #  자료가 mutable하다면 변경해도 reference가 보존되므로 결과적으로 Call by reference처럼 보일 것이고, 자료가 immutable하다면 결과적으로 Call by value처럼 보일 것입니다.
  #  이 문제를 해소하는 가장 쉬운 방법은 Tutorial 본문에서 문제의 저 문단을 아예 빼고 Python만의 방법을 소개하는 것이라고 생각합니다. 
  #  물론 이 글처럼 id라던가 is 연산자 같은걸 이야기하면 어렵게 되므로 아예 따로 독립된 문서가 필요할거같습니다.
  
  ## ------ pipe 연산자(>>)를 사용하지 않아도, pandas 기능으로 다음과 같이 구현할 수 있다 ------ ##
  # 관행적으로 instance object는 self로 parameter를 나타내고 class object는 cls로 parameter를 나타낸다. ☞ self 이해하기 : https://wikidocs.net/1742
  @classmethod
  def pdHeadTail(cls, df=None, n1=2, n2=2): # R's psych::headTail
      if type(df) == type(pd.DataFrame()):
          pass
      else:
          df = pd.DataFrame(df)

      return pd.concat([pd.concat([df.head(n1), 
                                   pd.DataFrame(list('─' * df.shape[1]), 
                                                columns=['─'],
                                                index=df.columns).T], 
                                   axis=0), 
                        df.tail(n2)], axis=0)

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def pdCalcRowCol(cls, df, func=None):  # func = function of "df or series"
    temp_df = pd.concat([df, pd.DataFrame(df.apply(func,axis=0)).T], axis=0)
    return pd.concat([temp_df, pd.DataFrame(temp_df.apply(func, axis=1))], axis=1)

  ## ------------------------------------------------------------------------------------------- ##
  # from datetime import datetime                   # https://brownbears.tistory.com/432
  @classmethod
  def sPrintLog(cls, dt=None):  # Simple(간이) Print Log # https://docs.python.org/ko/3.8/library/datetime.html?highlight=datetime#module-datetime
      # print(datetime.now().strftime("%Y-%m-%d %A %H:%M:%S [%V Week,"), "{Dx} Day]".format(Dx=int(datetime.now().strftime("%j")) + 1))
      if dt:
          pass
      else:
          dt = datetime.now()

      return dt.strftime('%Y-%m-%d %A %H:%M:%S [%V week, %j day]')

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def npArrInfo(cls, ndarrayObj, itemRelDesc=False):  # np.info, np.source, np.lookfor
      """
      np.info()를 기본으로 하여 일부 정보가 추가 표시되도록 기능을 보강했습니다.
      참고 : np.source(x), np.lookfor(x), np.linalg.matrix_rank(x), x.data, x.flags
             np.nanpercentile(x, [0,25,50,75,100]) or np.nanquantile(x, [0,.25,.5,.75,1.]), 
             np.nanmean(x), np.nanmedian(x), np.nanstd(x), np.nanvar(x)
      """
      strItemRelDesc = """
  shape's item 곱셈 →    size     (=item 갯수. 즉, "개별" 원소 갯수) 
  └→ '['갯수         x) itemsize (=bytes/dtype) ☞ dtype의 memory 수치
                          --------
                          nbytes                  ☞ 전체 memory 수치 """
      try:
          blankStr = " "
          descPhrase = "= items in 'n-1' dimension (one dim. = one '[')"
          orgObjClass = type(ndarrayObj)
          if type(ndarrayObj) in [type(pd.DataFrame()), type(pd.Series(dtype='int')), type(pd.DataFrame().index)]:
              #print("original class: ", type(ndarrayObj).__name__, end=",\t\t")
              ndarrayObj = ndarrayObj.values
          elif type(ndarrayObj) in [type(list()), type(tuple())]:
              #print("original class: ", type(ndarrayObj).__name__, end=",\t\t")
              ndarrayObj = np.array(ndarrayObj)
          elif type(ndarrayObj) == type(map([],[])):
              #print("original class: ", type(ndarrayObj).__name__, end=",\t\t")
              ndarrayObj = np.array(list(ndarrayObj))
          if orgObjClass != type(np.array([])):
              print("original class: ", orgObjClass.__name__, end=",\t\t")
          if type(ndarrayObj) == type(np.array([])):
              # fake_stdout = io.BytesIO() # https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-in-python-into-some-sort-of-string-buffer
              # np.info(ndarrayObj, output=fake_stdout)
              # print(fake_stdout.getvalue())
              print(" class   \t",  type(ndarrayObj),            '\n',  # "np.info(ndarrayObj)"를 대신함
                    "shape    \t",  ndarrayObj.shape,            '\n',
                    "strides  \t",  ndarrayObj.strides,          '\n',
                    "itemsize \t",  ndarrayObj.itemsize,         '\n',
                    "aligned  \t",  ndarrayObj.flags.aligned,    "\t\t\tcontiguous\t", ndarrayObj.flags.contiguous, '\n',
                    "fortran\t",    ndarrayObj.flags.fortran,    "\t\t\tdata type\t",  ndarrayObj.dtype,            '\n')
              try:
                  rank_res = np.linalg.matrix_rank(ndarrayObj)
              except TypeError:
                  rank_res = "N/A"
              print('axis:\033[1m', ndarrayObj.ndim, '\033[0m\t', 'len():', len(ndarrayObj),
                    eval("descPhrase" if itemRelDesc else "blankStr"),
                    '\nrank', rank_res, '\tsize:', ndarrayObj.size, '\t', 'no of bytes(nbytes):', ndarrayObj.nbytes)
              if itemRelDesc:
                  print(strItemRelDesc)
          else:
              print("Only numpy.ndarray is allowed!")
      except NameError:
          print("NameError : name not defined!")
      else:
          if orgObjClass in [type(pd.DataFrame()), type(pd.Series(dtype='int'))]:
              print('\n', orgObjClass.index, "\n ♣ If (or After converted to) pd.DataFrame, run \033[1m.info()\033[0m or \033[1m.describe()\033[0m for detail info.!")

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def npConcat(a1, a2, func='c', axisNum=0, outCmd=None):
      possibleFunc = {'c': 'concatenate', 'h': 'hstack', 'v':'vstack'}
      func = possibleFunc[func[0]] if func[0] in ['c', 'h', 'v'] else func
      try:
          if func == 'concatenate':
              res = eval('np.' + func)((a1, a2), axis=axisNum, out=outCmd)
          elif func == 'hstack' or func == 'vstack':
              res = eval('np.' + func)((a1, a2))
          else:
              raise Exception("Function '{1}{0}{2}' isn't defined. One of '{1}c{2}oncatenate, {1}h{2}stack and {1}v{2}stack' is allowed.".format(func, '\033[1m', '\033[0m'))
          return res
      except Exception as e:
          print("\033[1mError!\033[0m", e)
  ## ------------------------------------------------------------------------------------------- ##
  # def typeLenShape(obj=None, printFlag=True):
  #     rtnValue = (type(obj), len(obj), obj.shape) if hasattr(obj, 'shape') else (type(obj), len(obj))
  #     if printFlag:
  #         print(rtnValue)
  #     else:
  #         return rtnValue

  ## ------------------------------------------------------------------------------------------- ##
  # from IPython.display import Markdown, display, Image
  @classmethod
  def printbmd(cls, string):  # print black & white text markdown print
      display(Markdown(string))

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def printcmd(cls, string, color=None):  # print color text markdown print
      colorstr = "<span style='color:{}'>{}</span>".format(color, string)
      display(Markdown(colorstr))

  ## ------------------------------------------------------------------------------------------- ##
  lib_exist = importlib.util.find_spec("pydot")
  if lib_exist:
      lib_exist = None
      import pydot  # https://pythonprogramming.altervista.org/mind-map-with-python/
  else: 
      pass  # print("passed: 'import pydot'")
  # https://stackoverflow.com/questions/4596962/display-graph-without-saving-using-pydot
  # from IPython.display import display, Image
  @classmethod
  def makeTreeGraph(cls, argTreeContent=None, argRD="TB", argGT="graph"):
      colors = {0:'black',  1:'purple', 2:'navy', 3:'blue', 4:'brown', 5:'green',  
                6:'gray',   7:'orange', 8:'gold', 9:'red'}
      graph = pydot.Dot(graph_type=argGT, rankdir=argRD)
      #https://www.programcreek.com/python/example/5731/pydot.Edge  cf) 6060/pydot.Node
      graph.set_node_defaults(fontsize='12') # color='red',style='filled',shape='oval',fontname='Courier'
      for i in argTreeContent.index:
          if argTreeContent.iloc[i].SrcNode == 'root': 
              continue
          edge = pydot.Edge(src=argTreeContent.iloc[i].SrcNode, dst=argTreeContent.iloc[i].DstNode,
                            color = colors[int(argTreeContent.iloc[i].TreeWBS[0]) % 10],
                            style = 'dashed' if int(argTreeContent.iloc[i].TreeWBS[0]) % 2 else 'line') 
          graph.add_edge(edge)
      # display(Image(graph.create_png())) # graph.write_png("Hello.png"); os.startfile("Hello.png")
      return graph

  @classmethod
  def viewPyDotGraph(cls, argGraph = None):
      display(Image(argGraph.create_png()))

  @classmethod
  def viewTreeGraph(cls, argTreeContent=None, argRD="TB", argGT="graph"): # makeTreeGraph + viewPyDotGraph
      cls.viewPyDotGraph(makeTreeGraph(argTreeContent, argRD=argRD, argGT=argGT))

  # ▣ 예시 : The Machine Learning Workflow
  treeContent = pd.DataFrame( # black, red, orange, yellow, green, blue, navy, purple, gray, white
      columns= [ 'TreeWBS', 'SrcNode', 'DstNode'], # 열: TreeWBS(선택) / Source Node(필수) / Destination Node(필수)
      data = [ [ '0root',   'root',    'The Machine Learning\nWorkflow'], # root는 없어도 무방
               [ '0',       'The Machine Learning\nWorkflow',     '0. Data Input & Gathering'],
               [ '1',       'The Machine Learning\nWorkflow',     '1. Data Preprocessing'],
               [ '1.1',     '1. Data Preprocessing',              '1.1 Database Merge [ Feedback starts ]'],
               [ '1.2',     '1. Data Preprocessing',              '1.2 Encoding Categorical Variables'],
               [ '1.3',     '1. Data Preprocessing',              '1.3 Data Scaling & Normalization'],
               [ '1.4',     '1. Data Preprocessing',              '1.4 Imputing Missing Values'],
               [ '1.5',     '1. Data Preprocessing',              '1.5 Exploratory Data Analysis'],
               [ '1.6',     '1. Data Preprocessing',              '1.6 Train (& Val.) / Test Split\n& Augmentation'],
             # [ '2',       'The Machine Learning\nWorkflow',     '2. Exploratory\n\tData Analysis'], 
             # [ '2.1',     '3. Exploratory\n\tData Analysis',    'Data Visulization'],
               [ '2',       'The Machine Learning\nWorkflow',     '2. Model Building\n(Recursive)'],
               [ '2.1',     '2. Model Building\n(Recursive)',     '2.1 Model(s) Selection (preliminary)'],
               [ '2.2',     '2. Model Building\n(Recursive)',     '2.2 Model Fitting / Training'],
               [ '2.3',     '2. Model Building\n(Recursive)',     '2.3 Model Evaluation (w/ val. set)'],
               [ '2.4',     '2. Model Building\n(Recursive)',     '2.4 Hyperparameters Tuning'],
               [ '2.5',     '2. Model Building\n(Recursive)',     '2.5 Model Selection (Final, w/ test set)\n[ Feedback ends ]'],
               [ '3',       'The Machine Learning\nWorkflow',     '3. Model Output'],
               [ '3.1',     '3. Model Output',                    'Predictions (Model + Real Data)']
              ] )

  # ▣ 예시 : 함수 활용 ①
  # pydotGraph = my.makeTreeGraph(my.treeContent, "LR") # LR: Left to Right, RL: Right to Left
  # my.viewPyDotGraph(pydotGraph)                    # TB: Top to Bottom ( = UD: Up Down), BT: Bottom to Top 

  Books4AIStudy = pd.DataFrame(  # https://tensorflow.blog/book-roadmap/ 참조하였으며, 이를 기반으로 관심 서적을 보강함. 데이터 과학 일반 및 자연어 처리 보강 필요
    columns = [ 'TreeWBS', 'SrcNode', 'DstNode'],
    data = [['0',   'The Books for AI Study',               'Health & Medical Statistics, Dr. Bae'], # 배정민, 보건의학통계
            ['0',   'Health & Medical Statistics, Dr. Bae', 'jamovi Statistics, Seong Tae Je'],
            ['0',   'jamovi Statistics, Seong Tae Je',      'Statistics, Andy Field'],
            ['0',   'Statistics, Andy Field',               'An Intro to SL, Gareth James'],         # SL: Statistical Learning
            ['0',   'The Books for AI Study',               'Python Coding Dojang*'],
            ['0',   'Python Coding Dojang*',                'Practices of the Python Pro, Dane Hillard'],
            ['0',   'Python Coding Dojang*',                'Pandas Cookbook 2e, Matt Harrison'],
            ['0',   'Pandas Cookbook 2e, Matt Harrison',    'Self Study ML DL, rickiepark'],
          # ['0',   'Self Study ML DL, rickiepark',         'Data Science from Scratch 2e, Joel Grus'],
            ['0',   'Self Study ML DL, rickiepark',         'ML for Everyone, Mark Fenner'],
            ['0',   'Self Study ML DL, rickiepark',         'Intro to ML, Andreas Müller'],
            ['0',   'ML for Everyone, Mark Fenner',         'Intro to ML, Andreas Müller'],
            ['0',   'Intro to ML, Andreas Müller',          'ML Cookbook, Chris Albon'],
            ['0',   'ML Cookbook, Chris Albon',             'An Intro to SL, Gareth James'],         # SL: Statistical Learning
            ['0',   'An Intro to SL, Gareth James',         'The Elements of SL 2e, Trevor Hastie'], # SL: Statistical Learning
            ['0',   'ML Cookbook, Chris Albon',             'Hands-on ML 2e, Aurélien Géron'],
            ['0',   'Intro to ML, Andreas Müller',          'Hands-on ML 2e, Aurélien Géron'],
            ['0',   'ML for Everyone, Mark Fenner',         'Hands-on ML 2e, Aurélien Géron'],
            ['0',   'ML for Everyone, Mark Fenner',         'pycaret Tutorial, Moez Ali'],  # https://dacon.io/codeshare/1701 https://today-1.tistory.com/17
            ['0',   'pycaret Tutorial, Moez Ali',           'Kakao Arena & Dacon Competition'],
            ['0',   'Self Study ML DL, rickiepark',         'DL Illustrated, Jon Krohn' ],
            ['0',   'DL Illustrated, Jon Krohn',            'Hands-on ML 2e, Aurélien Géron'],
            ['0',   'Self Study ML DL, rickiepark',         'Do it DL, rickiepark'],
            ['0',   'Do it DL, rickiepark',                 'DL, François Chollet'],
            ['0',   'Do it DL, rickiepark',                 'Grokking DL, Andrew Trask'],
            ['0',   'Grokking DL, Andrew Trask',            'DL from Scratch I~III, Saito Goki'],
            ['0',   'DL, François Chollet',                 'Hands-on ML 2e, Aurélien Géron'],
            ['0',   'The Elements of SL 2e, Trevor Hastie', 'Hands-on ML 2e, Aurélien Géron'], # SL: Statistical Learning
            ['0',   'Hands-on ML 2e, Aurélien Géron',       'Hands-On Computer Vision\nwith TF2, Benjamin Planche'], # 딥러닝 컴퓨터 비전, 김정인 옮김
            ['0',   'Hands-on ML 2e, Aurélien Géron',       'GAN, David Foster'],
            ['0',   'Hands-on ML 2e, Aurélien Géron',       'GAN in Action, Jakub Langr'],
            ['0',   'Hands-on ML 2e, Aurélien Géron',       'Deep Reinforcement Learning\nin Action, Alex Zai'] # 심층 강화학습 인 액션, 류광 옮김
           ] )

  # ▣ 예시 : 함수 활용 ②
  # Books4AIStudyGraph = my.makeTreeGraph(my.Books4AIStudy, "TB") # LR: Left to Right, RL: Right to Left
  # my.viewPyDotGraph(Books4AIStudyGraph)                         # TB: Top to Bottom ( = UD: Up Down), BT: Bottom to Top  

  ## ------------------------------------------------------------------------------------------- ##
  #  Wes McKinney, Python for Data Analysis, ver 2, Chap. 2, page 66, duck typing
  @classmethod
  def isiterable(cls, obj):
      try:
          iter(obj)
          return True
      except TypeError: # not iterable
          return False

  ## ------------------------------------------------------------------------------------------- ## 일부 오류 있음. 
  @classmethod
  def ismutable(cls, aObj):   # https://docs.python.org/ko/3/library/stdtypes.html#immutable-sequence-types
      # tTypes = [True, [bytearray(b''), [], {1,}, {}]]  # https://docs.python.org/ko/3/library/stdtypes.html#typesmapping
      # fTypes = [False,[0, 1., 1j, False, "", b'', (1,), range(1), frozenset()] ]
      result = False
      try:
          result = aObj.__hash__() if hasattr(aObj, '__hash__') else False # 불변에는 있고(True), 가변에는 없다(False)
          result = not ( type(result) == type(1) )    # 그러므로 hash() 결과가 정수면 불변이며 immuatable여부는 False임
      except TypeError: # mutable
          result = True
      # else:
      #     # success
      # finally:
      #     # 1번은 실행
      if result:
          pass
      else:
          result = issubclass(type(aObj), collections.abc.MutableSequence)
      return result

# 검증 예시 ① ☞ 관련 항목 : dictionary의 키로는 immutable한 값은 사용할 수 있지만, mutable한 객체는 사용할 수 없습니다.
# tTypes = [True, [bytearray(b''), [], {1,}, {}]]
# fTypes =  [False,[0, 1., 1j, False, "", b'', (1,), range(1), frozenset()] ]
# for obj in fTypes[1]:
#     print("All items must be " + str(fTypes[0]) + "! ... and validation result is ", 
#           "success (○)" if not my.ismutable(obj) else "fail (ㅜ.ㅜ) ", str( my.ismutable(obj)), '\t불변', '\t', type(obj))
# for obj in tTypes[1]:
#     print("All items must be " + str(tTypes[0]) + "!  ... and validation result is ", 
#           "success (○)" if my.ismutable(obj) else "fail (ㅜ.ㅜ) ", str( my.ismutable(obj)), '\t가변', '\t', type(obj))

# 예시 Script ②
# tTypes = [bytearray(b''), [], {1,}, {}]  # https://docs.python.org/ko/3/library/stdtypes.html#typesmapping
# fTypes = [0, 1., 1j, False, "", b'', (1,), range(1), frozenset()] 
#
# for itemType in [tTypes, fTypes]:
#     print('mutable types ...' if itemType == tTypes else 'immutable types ...')
#     for item in itemType:
#         print('\t', type(item))

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def typelen(cls, obj):  # Object's Short Information : type + len
      res = (type(obj), )
      res_desc = ('type', )
      if hasattr(obj, 'dtype'):
          res += (obj.dtype, )
          res_desc += ('dtype', )
      if hasattr(obj, 'shape'):
          res += (obj.shape, )
          res_desc += ('shape', )
      if hasattr(obj, 'ndim'):
          res += (obj.ndim, )
          res_desc += ('ndim(axis)', )
      if hasattr(obj, '__len__'):
          res += (len(obj), )
          res_desc += ('len', )
      return (res, res_desc)

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def viewitems(cls, obj, frPtr=0, toPtr=-1, dict_key=True):
      if hasattr(obj, '__iter__'):
          i = 0
          if frPtr > toPtr:
              if toPtr == -1:
                  toPtr = len(obj)
              else:
                  toPtr = frPtr
                  print("Ptr 오류 : '시작 > 끝'이므로 실행할 수 없습니다. '시작=시작'으로 실행합니다.") 
          else:
              pass

          if frPtr >=0:
              pass
          else:
              frPtr += len(obj)

          if toPtr >= 0:
              if toPtr > len(obj):
                  toPtr = len(obj)
              else:
                  pass
          else:
              toPtr += len(obj)

          if type(obj) == type(dict()):
              for key in obj:
                  if frPtr <= i <= toPtr:
                      if dict_key:
                          print(i + 1, '\t', key, '\t', obj[key])
                      else:
                          print(obj[key])
                      if frPtr == toPtr:  # 한 번만 실행하고 Loop 탈출
                          break
                  i = i + 1
          elif type(obj) == type(set()) or type(obj) == type(frozenset()):
              for item in obj:
                  if frPtr <= i <= toPtr:
                      print(i + 1, '\t', item)
                      if frPtr == toPtr:  # 한 번만 실행하고 Loop 탈출
                          break
                  i = i + 1
          elif type(obj) == type(list())  or type(obj) == type(tuple()) or type(obj) == type(str()):
              print(obj[frPtr]) if frPtr == toPtr else print(obj[frPtr:toPtr + 1])
          elif type(obj) == type(np.array(list())) or type(obj) == pd.DataFrame(list()):
              print(obj[frPtr]) if frPtr == toPtr else print(obj[frPtr:toPtr + 1])
      else:
          print(obj)

  ## ------------------------------------------------------------------------------------------- ##
  # import sqlite3  

      # pandas 기능 활용 SQLite 연결 ---------------------------------------------------------------- #
      # - 방법을 몰라서 runsql을 만들었으나, 다음과 같이 pandas의 기본 기능을 활용하면 쉽다.
      # - (아래에 정의된) 기존에 작성한 Function은 transaction commit 기능도 있으므로 계속 사용해도 무방할 것으로 생각된다.
      # - cf : ㅇ https://beomi.github.io/2017/10/21/SQLAlchemy-Query-to-Pandas-DataFrame/ 
      #        ㅇ https://pandas.pydata.org/pandas-docs/version/0.22.0/generated/pandas.read_sql_query.html#pandas.read_sql_query
      # import sqlite3
      # import pandas as pd
      #
      # conn = sqlite3.connect("./sqlite_filename.db") ### DB 연결 ### # isolation_level, conn은 with 사용 가능
      #
      # def runsql(sqlstr=None, db_connect=conn):      # 매번 conn을 지정하는 번거로움을 없애기 위함 
      #     return pd.read_sql_query(sql=sqlstr, con=db_connect)
      #
      # sqlstr = "select * from tips limit 3"
      # df = runsql(sqlstr, conn)
      #
      # conn.close()                                   ### 연결 닫기 ###
      # ---------------------------------------------------------------------------------------- #
  @classmethod
  def runSQL(cls, sqlstr=None, cursor=None, params=None, 
          conn_str=None, conn_commit=False, conn_close=False):
      """
      sqlite3의 execute 함수를 편하게 활용하도록 하기 위한 함수로서, 다음 2가지를 전제로 한다.
      (1) import sqlite3     
      (2) cursor 오브젝트는 'cursor'로 명명한다.
          이 경우 runSQL 함수 호출 시 별도로 cursor를 지정할 필요가 없다.
      """
      result = 'Nothing executed!!!'
      trxn = 'TRXN'
      if cursor:
          conn = cursor.connection
          pass
      else:
          conn = sqlite3.connect(conn_str if conn_str else '')
          cursor = conn.cursor()

      try:
          if params:
              cursor.execute(sqlstr, params)
          else:
              cursor.execute(sqlstr)
      except Exception as inst:
          result = (type(inst), inst)
      else: # try 절이 예외를 일으키지 않을 때 실행되어야만 하는 코드에 유용
          # result = 'Executed successfully!'

          # if sqlstr.lower().index('drop ', 0, 10) >= 0:
          if sqlstr[:5].upper().strip() == 'DROP':
              trxn = 'DROP'
              result = "Executed successfully!"
              conn_commit = True
          else:
              trxn = sqlstr[:7].upper().strip()  # Select, Insert, Update, Delete
              if trxn == 'SELECT':
                  result = cursor.fetchall()  
                  if len(result) > 0:
                      pass
                  else:  # Insert, Update, REPLACE, DELETE
                      result = "No row fetched!"
              else:
                  result = "Executed successfully!"
                  conn_commit = True

          if conn_commit:
              conn.commit()

          if conn_close:
              conn.close()

      if len(result) > 0:
          if trxn == 'SELECT':
              return pd.DataFrame(data=result, columns=list(np.array(cursor.description).T[0]))
          else:
              return (trxn, result, cursor.rowcount if cursor.rowcount >=0 else 0, 'COMMIT True' if conn_commit else 'COMMIT False')
      else:
          return (trxn, result, cursor.rowcount if cursor.rowcount >=0 else 0, 'COMMIT True' if conn_commit else 'COMMIT False')

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def plot2d(cls,
             Fx=None,
             x_from=-5, x_to=5, x_step=1000,
             y_from=None, y_to=None,
             # slope2nd = False,
             figsize_row=12, figsize_col=8,
             plot_color="blue",
             # plot_color2="cornflowerblue",
             plot_title="2D Plot"):
      """▣ 사용 예시
      ㅇ 환경
      import numpy as np  # 『필요한 Library』 Import 필수 ☞ np.수학함수
      # NumPy Functions
      #  - Financial    : https://docs.scipy.org/doc/numpy/reference/routines.financial.html
      #  - Logic        : https://docs.scipy.org/doc/numpy/reference/routines.logic.html
      #  - Mathematical : https://docs.scipy.org/doc/numpy/reference/routines.math.html
      #  - Universal    : https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs
      #  - Window       : https://docs.scipy.org/doc/numpy/reference/routines.window.html
      import matplotlib.pyplot as plt
      ㅇ 일반 함수
         - 1차 함수 : x + 2
         - 2차 함수 : 2*x**2 + 3*x + 4
         - 3차 함수 : 3*x**3 + 4*x**2 + 5*x + 10
         - n차 함수 : 3*np.power(x, n) 방식으로 지정
      ㅇ 2차 곡선(원: https://mathcoding.tistory.com/21?category=756794)
         - 원      : np.sqrt(반지름² - np.power(x,2))    
         - *포물선 : 위 "일반 > 2차 함수" 참고
         - 타원    : np.sqrt(상수 - 계수 * np.power(x,2))
         - 쌍곡선  : 좌우로 퍼진 쌍곡선, y계수 * np.sqrt(np.power(x,2)*x계수**2 - 상수**2)
                     상하로 퍼진 쌍곡선, y계수 * np.sqrt(np.power(x,2)*x계수**2 - 상수**2)
      ㅇ 지수 함수 
         - 2**x 또는 2 * np.exp(x)
         - Sigmoid Function : 1 / (1 + np.exp(-x))
      ㅇ 로그 함수
         - 자연 로그 : np.log(x)
         - 상용 로그 : np.log10(x)  ☞ log2(x)
      ㅇ 삼각 함수
         - sin : plot2d("np.sin(x)", -np.pi, np.pi)
         - tan : 무한대를 고려하여 offset 적용 필요
                 offset = 0.1; plot2d("np.tan(x)", -np.pi/2 + offset, np.pi/2 - offset)
      ㅇ hyperbolic 
         - sinh : plot2d("np.sinh(x)", -np.pi, np.pi)
      """
      # 독립변수 x 정의
      x = np.linspace(x_from, x_to, x_step)

      # 함수를 종속변수 y에 지정
      y = (lambda x: eval(Fx))(x)

      # 그래프 : 중심 내용
      plt.figure(figsize=(figsize_row, figsize_col))
      plt.plot(x, y, color=plot_color)
      # if slope2nd:
      #     y2 = (lambda x: eval(Fx))(-x)
      #     plt.plot(x, y, color=plot_color2)

      # 그래프 : 꾸미기
      if plot_title == "2D Plot":
          plot_title = plot_title + " : " + Fx
      else:
          pass
      plt.title=(plot_title)

      if y_from == None and y_to == None:
          pass  # Default 설정 수용 
      else:
          if y_from == None:
              y_from = y(np.min(x))
          if y_to == None:
              y_to = y(np.max(x))
          plt.ylim(y_from, y_to) 

      plt.xlabel('X') # X 라벨
      plt.ylabel('Y') # y 라벨
      plt.grid(True) # 그리드
      plt.axvline(x=0, color='green', linewidth=1, linestyle='--')
      plt.axhline(y=0, color='green', linewidth=1, linestyle='--')

      # 그리기 실행
      plt.show( )

  ## ------------------------------------------------------------------------------------------- ##
  # from mpl_toolkits.mplot3d import Axes3D
  @classmethod
  def plot3d(cls,
             Fxy,
             x_from=-5, x_to=5, x_step=50,
             y_from=-5, y_to=5, y_step=50,
             figsize_row=12, figsize_col=8,
             plot_rstride=1, plot_cstride=1, plot_stride=None,
             plot_alpha=0.3,
             plot_color="cornflowerblue",  #"lightgreen", "yellowgreen"
             plot_edge_color="black",
             plot_title="3D Plot"):
      """▣ 사용 예시
      ㅇ 환경
      import numpy as np  # 『필요한 Library』 Import 필수 ☞ np.수학함수
      # NumPy Functions
      #  - Financial    : https://docs.scipy.org/doc/numpy/reference/routines.financial.html
      #  - Logic        : https://docs.scipy.org/doc/numpy/reference/routines.logic.html
      #  - Mathematical : https://docs.scipy.org/doc/numpy/reference/routines.math.html
      #  - Universal    : https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs
      #  - Window       : https://docs.scipy.org/doc/numpy/reference/routines.window.html
      import matplotlib.pyplot as plt
      from mpl_toolkits.mplot3d import Axes3D
      ㅇ 함수 : 소문자 x, y를 사용하여 함수식 정의 필수
         ㆍfunstr = "x**2 + y**2"; plot3d(funstr)
         ㆍfunstr = "(2 * x**2 + y**2) * np.exp(-(2 * x**2 + y**2))"; plot3d(funstr)
         ㆍplot3d("np.sin(x) + np.cos(y)")
         ㆍ독립변수가 2개인 Softmax Function : plot3d("np.exp(x) / (np.exp(x) + np.exp(-y))", plot_stride=5)
         ㆍ가장 간단한 2차원 가우스 함수 : plot3d("np.exp(-(x**2 + y**2))", x_from=-3, x_to=3, y_from=-3, y_to=3, plot_stride=1)
      """
      # 독립변수 x, y 정의
      x = np.linspace(x_from, x_to, x_step)
      y = np.linspace(y_from, y_to, y_step)

      # 함수를 종속변수 z에 지정
      # z = (lambda x,y: eval(Fxy))(x,y)

      z = np.zeros((len(x), len(y))) 
      for xi in range(x_step):
          for yi in range(y_step):
              z[yi, xi] = (lambda x,y: eval(Fxy))(x[xi], y[yi]) 

      xz, yz = np.meshgrid(x, y)

      if plot_stride == None:
          pass
      else:
          plot_rstride = plot_stride
          plot_cstride = plot_stride

      # 그래프 : 중심 내용
      plt.figure(figsize=(figsize_row, figsize_col))
      ax = plt.subplot(1, 1, 1, projection='3d')
      ax.plot_surface(xz, yz, z, 
                      rstride=plot_rstride, # 가로 보폭(정수)
                      cstride=plot_cstride, # 세로 보폭(정수)
                      alpha=plot_alpha,     # (투명)0 ~ 1(불투명) 범위의 투명도
                      color=plot_color, 
                      edgecolor=plot_edge_color) 

      if plot_title == "3D Plot":
          plot_title = plot_title + " : " + Fxy
      else:
          pass
      ax.set_title(plot_title + '\n') 

      ax.set_xlabel('X')
      ax.set_ylabel('Y')

      # 그리기 실행
      plt.show()

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def plot_fit_history(cls, history=None, plt_figsize=(14,6), offsetDenominator=20, pltGrid=True): # plt_ylim=3):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch

    plt.figure(figsize=plt_figsize)

    def compareTwoNumber(x, y, howto='min'):
      rtnValue = 0
      if x > y:
        rtnValue = (y if howto == 'min' else x)
      else:
        rtnValue = (x if howto == 'min' else y)
      return rtnValue  

    idx = 0
    if 'mae' in hist.columns  and 'val_mae' in hist.columns:
      idx = idx + 1
    if 'mse' in hist.columns  and 'val_mse' in hist.columns:
      idx = idx + 1
    if 'loss' in hist.columns and 'val_loss' in hist.columns:
      idx = idx + 1
    if 'acc' in hist.columns  and 'val_acc' in hist.columns:
      idx = idx + 1
    if 'accuracy' in hist.columns  and 'val_accuracy' in hist.columns:
      idx = idx + 1

    if idx <= 2:
      sp_row = 1
      sp_col = 2
    elif idx <= 4:
      sp_row = 2
      sp_col = 2

    idx = 0

    if 'mae' in hist.columns and 'val_mae' in hist.columns:
      idx = idx + 1
      plt.subplot(sp_row, sp_col, idx)  # row, column, index
      plt.xlabel('Epoch')
      plt.ylabel('Mean Absolute Error') # [MPG]
      plt.plot(hist['epoch'], hist['mae'],     label='Trn Error')
      plt.plot(hist['epoch'], hist['val_mae'], label='Val Error')
      # plt.ylim([0, plt_ylim * hist['mae'].quantile(0.75)])    #plt.ylim([0,5])
      tMin1 = hist['mae'].quantile(0);     tMax1 = hist['mae'].quantile(1)
      tMin2 = hist['val_mae'].quantile(0); tMax2 = hist['val_mae'].quantile(1)
      tMin = compareTwoNumber(tMin1, tMin2,'min');     tMax = compareTwoNumber(tMax1, tMax2, 'max')
      tMin = tMin - (tMin + tMax) / offsetDenominator; tMax = tMax + (tMin + tMax) / offsetDenominator
      plt.ylim([tMin, tMax]) 
      plt.legend()
      plt.title('Training and Validation MAE')
      if pltGrid: plt.grid()

    if 'mse' in hist.columns and 'val_mse' in hist.columns:
      idx = idx + 1
      plt.subplot(sp_row, sp_col, idx)
      plt.xlabel('Epoch')
      plt.ylabel('Mean Square Error') # [$MPG^2$]
      plt.plot(hist['epoch'], hist['mse'],     label='Trn Error')
      plt.plot(hist['epoch'], hist['val_mse'], label='Val Error')
      # plt.ylim([0, plt_ylim * hist['mse'].quantile(0.75)])  #plt.ylim([0,20])
      tMin1 = hist['mse'].quantile(0);     tMax1 = hist['mse'].quantile(1)
      tMin2 = hist['val_mse'].quantile(0); tMax2 = hist['val_mse'].quantile(1)
      tMin = compareTwoNumber(tMin1, tMin2,'min');     tMax = compareTwoNumber(tMax1, tMax2, 'max')
      tMin = tMin - (tMin + tMax) / offsetDenominator; tMax = tMax + (tMin + tMax) / offsetDenominator
      plt.ylim([tMin, tMax])     
      plt.legend()
      plt.title('Training and Validation MSE')
      if pltGrid: plt.grid()

    if 'loss' in hist.columns and 'val_loss' in hist.columns:
      idx = idx + 1
      plt.subplot(sp_row, sp_col, idx)
      plt.xlabel('Epoch')
      plt.ylabel('Loss')
      plt.plot(hist['epoch'], hist['loss'],     label='Trn Loss')
      plt.plot(hist['epoch'], hist['val_loss'], label='Val Loss')
      # plt.ylim([0, plt_ylim * hist['loss'].quantile(0.75)])  # plt.ylim([0,20])
      tMin1 = hist['loss'].quantile(0);     tMax1 = hist['loss'].quantile(1)
      tMin2 = hist['val_loss'].quantile(0); tMax2 = hist['val_loss'].quantile(1)
      tMin = compareTwoNumber(tMin1, tMin2,'min');     tMax = compareTwoNumber(tMax1, tMax2, 'max')
      tMin = tMin - (tMin + tMax) / offsetDenominator; tMax = tMax + (tMin + tMax) / offsetDenominator
      plt.ylim([tMin, tMax])        
      plt.legend()
      plt.title('Training and Validation Loss')
      if pltGrid: plt.grid()

    if ('acc' in hist.columns and 'val_acc' in hist.columns) or \
      ('accuracy' in hist.columns and 'val_accuracy' in hist.columns):
      idx = idx + 1
      plt.subplot(sp_row, sp_col, idx)
      plt.xlabel('Epoch')
      plt.ylabel('Accuracy')
      if 'acc' in hist.columns:
        plt.plot(hist['epoch'], hist['acc'],     label='Trn Accuracy', )
        plt.plot(hist['epoch'], hist['val_acc'], label='Val Accuracy')
        # plt.ylim([0, plt_ylim * hist['acc'].quantile(0.75)])  # plt.ylim([0,20])
        tMin1 = hist['acc'].quantile(0);     tMax1 = hist['acc'].quantile(1)
        tMin2 = hist['val_acc'].quantile(0); tMax2 = hist['val_acc'].quantile(1)
      else:
        plt.plot(hist['epoch'], hist['accuracy'],     label='Trn Accuracy')
        plt.plot(hist['epoch'], hist['val_accuracy'], label='Val Accuracy')
        # plt.ylim([0, plt_ylim * hist['accuracy'].quantile(0.75)])  # plt.ylim([0,20])
        tMin1 = hist['accuracy'].quantile(0);          tMax1 = hist['accuracy'].quantile(1)
        tMin2 = hist['val_accuracy'].quantile(0);      tMax2 = hist['val_accuracy'].quantile(1)
      tMin = compareTwoNumber(tMin1, tMin2,'min');     tMax = compareTwoNumber(tMax1, tMax2, 'max')
      tMin = tMin - (tMin + tMax) / offsetDenominator; tMax = tMax + (tMin + tMax) / offsetDenominator
      plt.ylim([tMin, tMax])
      plt.legend()
      plt.title('Training and Validation Accuracy')
      if pltGrid: plt.grid()

    plt.show()

  ## ------------------------------------------------------------------------------------------- ##
  # from sklearn.model_selection import train_test_split
  @classmethod
  def train_val_test_split(cls, X, y, frac=(0.7, 0.2, 0.1), random_state=None, shuffle=True, stratify=None):
      ''' https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
      param X, y : Data to be split
      param frac : Ratio of train set to whole dataset

      Eg: passing frac=(0.7, 0.2, 0.1)
          X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(X, y, np.array([73.5, 15, 11.5]) / 100)
      '''

      # assert train_frac >= 0 and train_frac <= 1, "Invalid training set fraction"
      assert round(frac[0] + frac[1] + frac[2],5) == 1.0, "Invalid training set fraction. The total is not 1."
      assert frac[0] * frac[1] * frac[2] > 0,    "Invalid training set fraction. All fractions must be greater than zero."
      assert len(X) == len(y), "the Length of X & y are not same!"

      X_train, Xtmp, y_train, Ytmp = sklearn.model_selection.train_test_split(
          X, y, train_size=frac[0], random_state=random_state, shuffle=shuffle, stratify=stratify)

      X_val, X_test, y_val, y_test = sklearn.model_selection.train_test_split(
          Xtmp, Ytmp, train_size=frac[1]/(frac[1] + frac[2]), random_state=random_state, shuffle=shuffle, stratify=stratify)

      return X_train, X_val, X_test, y_train, y_val, y_test

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def ChooseRightSklearnEstimator(cls,
                                  data_cnt=0,
                                  prediction_for_what=None,
                                  label_exist=None,
                                  data_scarce=None,
                                  print_sklearn_url=False):

      """인자 사용 호출 예시 : print(ChooseRightEstimator(1000, 'C', True)[1])
                               print(ChooseRightEstimator(1001, 'E', False, False, True)[1])
                               print(ChooseRightEstimator(...))
      ㆍdata_cnt = 1000
      ㆍprediction_for_what = 'C' category, 'N' number, 'E' etc
      ㆍlabel_exist = True     (when prediction_for_what == 'C')
      ㆍdata_scarcity = False  (when prediction_for_what == 'N')"""

      url = "url for choosing the right estimator", "https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html"
      if type(data_cnt) == type(...):
          answer = url
      else:
          if print_sklearn_url:
              print(url[0], ":", url[1],"\n")

          if data_cnt > 0:
              pass
          else:
              data_cnt = int(input("data 건수를 양의 정수로 입력하세요:"))

          if data_cnt > 0:
              if data_cnt >= 50:
                  if prediction_for_what==None:
                      prediction_for_category = input("예측 대상 Data유형? - 범주(C)/수치(N)/기타(E):")[0].upper() 

                  if prediction_for_what=='C':
                      if label_exist == None:
                          label_exist = True if input("예측 대상인 범주형 Data에 대해 정답(Label)이 있습니까? (Y/N):")[0].upper() == 'Y' else False
                      if label_exist:
                          if data_cnt >= 100000:
                              answer = True, "SGDClassifier/GBDT(XGBoost) ☞ 잘 안되면, kernel approximation"
                          else:
                              answer = True, "Linear SVC\t☞ 잘 안되면,\t(Text면) NaiveBayes,\n\t\t\t\t(아니면) KNeighborsClassifier ☞ 잘 안되면, SVC 또는 EnsembleClassifiers"
                      else:
                          answer = True, "군집화(Clustering)"
                  elif prediction_for_what=='N':
                      if data_cnt >= 100000:
                          answer = True, "SGDRegressor"
                      else:
                          if data_scarce==None:
                              data_scarce = True if input("Data가 희소한가? (Y/N):")[0].upper() == 'Y' else False
                          if data_scarce:
                              answer = True, "라쏘 회귀/일래스틱넷"
                          else:
                              answer = True, "릿지 회귀 또는 SVR(선형 커널) ☞ 잘 안되면, SVR(RBF 커널) 또는 EnsembleRegressors"
                  elif prediction_for_what=='E':
                      # "차원 축소 시각화"
                      if data_cnt >= 100000:
                          answer = True, "dimensionality reduction: RandomizedPCA\t☞ 잘 안되면, kernel approximation"
                      else:
                          answer = True, "dimensionality reduction: RandomizedPCA\n\t☞ 잘 안되면, Isomap 또는 SpectralEmbedding\t☞ 잘 안되면, LLE" 
                  else:
                      answer = False, "예측 대상은 범주형(C) 또는 수치형(N)만 지정 가능합니다."
              else:
                  answer = False, "Data 추가 수집(∵ 50↓)"
          else:
              answer = False, "『data건수 > 0』이 아니므로 판단 불가!!!"
      return answer

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def sql2pd(cls, inputSQL="SELECT ...", printPandasScript=True, printDebugInfo=False): 
      """o Function Naming : sql script string to pandas dataframe ☜ Helper function for pandas dataframe basic usage in SQL way
      o 개발 동기 : 자주 사용하는 처리는 SQL 방식으로 처리하여 학습곡선의 문턱을 낮춘다. 고급기능은 DB Function을 활용하거나 한다.
        - 주1. 사용하는 기능만을 사용하는데, 다양한 기능을 제공하는 pandas의 많은 기능을 익히기는 힘들다.
        - 주2. pandas는 2차원 표형식의 Data를 다루는 module인데, Database에서 제공하는 기능보다는 번잡스럽고 부족하다.
        - 주3. 기존에 가지고 있는 SQL의 기능을 활용하여, SQL Script를 pandas 기능으로 전환하도록 하면 학습곡선이 완만할 수 있다.
        - 부1. 『 ① 키워드 중심 SQL → pandas 전환과 ② script 출력 』으로 pandas 사용에 익숙해진다. 
      o 사용 상의 주의 사항 : 복잡한 SQL Query는 실제 database를 연결하여 수행한다.
        - 1개의 SELECT문으로 이루어진 순방향 정렬만 되는 간단한 SQL만을 대상으로 한다. 
          SELECT가 여러 번 사용된 복잡한 SQL은 대상이 아니다. WINDOW Function은 향후 보강하여 추가하도록 한다.
          ☞ 복잡한 SQL(또는 pandas) 사용은 Script가 출력되도록 하여 단순한 방법으로 실행한 후 조합하여 활용한다.
             SQL ORDER BY의 ascending/descending 지정은 안되며, pandas로 전환된 script에서는 무조건 Ascending으로만 되어 있다.
             SQL에서 DISTINCT는 다양한 곳에서 사용 가능하나 pandas에서는 Series의 기능이므로 column 하나에 대해서만 사용 가능하다
        - 아래 함수 본문에서 IF로 비교하는 SQL Keyword는 대부분 한 줄에 하나씩만 사용하는 것이 좋다.
          ☞ 예: 일반적인 SQL에서는 한 줄에 입력해도 되지만, 이 함수를 사용할 때는 AS, LIMIT, OFFSET들은 별도 행에 입력한다.
                 SQL에서 OR 조건은 사용할 수 없다. (복잡한 경우이므로) pandas로 전환된 script 출력 후 &를 |로 변경하여 사용한다. 
        - SQL 예약어는 대문자 입력을 권장한다. ☞ 예: "COUNT(*)" 만 사용. "COUNT(field)" 또는 "COUNT(DISTINCT field)"는 안됨.
        - AS는 계산 Column에만 사용하며, 이 때 괄호 사용은 안된다.
        - column list를 '*'를 써서 제시하면 안되고 "table_name.*"와 같이 table(dataframe)도 지정해야 한다.
        - Join이나 COUNT(*) 외의 aggregate function은 지원하지 않는다. 이런 기능은 DB접속해서 실행하거나 pandas를 직접 활용한다.
      o 참조 URL
        - 【★ 착안】 How to rewrite your SQL queries in Pandas, and more
          ☞ https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
        - pandas documentation > Getting Started > Comparison with SQL 
          ☞ https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html
        - SQLite Homepage : https://www.sqlite.org ☞ https://www.sqlitetutorial.net 또는 https://www.tutorialspoint.com/sqlite
      """
      cnt = 1
      as_cnt = 0
      sql_list = []  # index, string
      opList = ['+', '-', '*', '/', '//', '%', '**']  # 수식 입력 시 함수에 붙는 괄호 외에 일반 괄호에 주의

      def opExist(str, op_list=opList): # str = string of sql_line
          return sum([(True if oStr.find(op) > 0 else False) for op in op_list])

      def splitStrWithOp(str, op_list=opList):
          op_location = []
          separated_fleld = []
          ptr = 0
          for ch in str:
              for op in op_list:
                  if ch == op:
                      op_location.append(ptr)
              ptr += 1

          fr=0
          from_to = []
          for oploc in op_location:
              separated_fleld.append(str[fr:oploc])
              from_to.append((fr, oploc))
              fr = oploc + 1
          else:
              separated_fleld.append(str[fr:])
              from_to.append((fr, -1))

          return op_location, from_to, separated_fleld

      for item in inputSQL.splitlines():
          if len(item.strip()) == 0: continue
          if item.strip()[0] == '#': continue
          if item.find('#') > 0: item = item[:item.find('#')]  # 주석 제외
          item = item.strip()             # 공백 문자 제외
          item = item.replace(' =', '==')  # 나중에 pandas 조건문에서 사용하도록 '='를 '=='로 변경
          item = item.replace('count(', 'COUNT(').replace('COUNT(', 'size('); item = item.replace('size(*', 'size(')   # 상동
          if len(item) > 0:
              if item.upper().startswith('FROM'):
                  sql_list.insert(0, [0, 'FROM', 'dataframe', item[4:].strip()] )
              elif item.upper().startswith('SELECT'):
                  if item[6:].strip() == '*':
                      pass
                  else:
                      sql_list.append([cnt, 'SELECT', 'columns', [x.strip() for x in item[6:].split(sep=',')]])  # SELECT
                      if item.upper().find('SIZE(') > 0:
                          sql_list.append([cnt, 'GROUP BY COUNT', 'size', 'size'])
                      if item.upper().find('AS') > 0:
                          as_cnt += 1
                          sql_list.append([as_cnt, 'AS', 'assign', [x.strip() for x in item.split(sep='AS')]])
              elif item.upper().startswith('WHERE'):
                  sql_list.append([cnt, 'WHERE', 'condition', item[5:].strip()])
              elif item.upper().startswith('AND'):
                  sql_list.append([cnt, 'AND', 'condition', item[3:].strip()])
              elif item.upper().startswith('OR '):
                  sql_list.append([cnt, 'OR', 'condition', item[2:].strip()])
              elif item.upper().startswith('GROUP BY'):
                  sql_list.append([cnt, 'GROUP BY', 'groupby', [x.strip() for x in item[8:].split(sep=',')]])
              elif item.upper().startswith('HAVING'):
                  sql_list.append([cnt, 'HAVING', '??having??', [x.strip() for x in item[6:].split(sep=',')]])
              elif item.upper().startswith('ORDER BY'):
                  sql_list.append([cnt, 'ORDER BY', 'sort_values', [x.strip() for x in item[8:].split(sep=',')]])
              elif item.upper().startswith('LIMIT'):
                  sql_list.append([cnt, 'LIMIT', 'slice', item[5:].strip()])
              # elif item.upper().startswith('OFFSET'):
              #    sql_list.append([cnt, 'OFFSET', '??offset??', item[6:].strip()])
              else:
                  if item.upper().find('AS') > 0:
                      as_cnt += 1
                      sql_list.append([as_cnt, 'AS', 'assign', [x.strip() for x in item.split(sep='AS')]])
                  else:
                      sql_list.append([cnt, 'SELECT', 'columns', [x.strip() for x in item.split(sep=',')]])

          cnt = cnt + 1  # End of Main for Loop

      tmp = pd.DataFrame(sql_list, columns=['SNo', 'SQLKeyword', 'pd_str', 'Obj']) #; if printDebugInfo: print(tmp) 
      df1 = tmp.Obj[0]

      def extract_columns(df=df1, SQLKW='SELECT'):
          colnames = ""
          col_cnt = 0
          for col_list in list(tmp[tmp.SQLKeyword == SQLKW][['SNo','Obj']].values):
              sno = col_list[0]
              if SQLKW=='AS': col_list[1].sort(reverse=True)
              for col in col_list[1]:
                  if len(col) > 0:
                      if col.upper().startswith('SIZE('):
                          pass
                      elif SQLKW=='AS': # col.upper().find("AS") > 0:  
                          col = col.replace(",", "")
                          op_loc = op_separated_col = []
                          op_loc, from_to, op_separated_col = splitStrWithOp(col)
                          if len(op_separated_col) == 1:
                              colnames = ".assign(" + (", " if sno > 1 else "") + col.strip() + "="
                          if len(op_separated_col) > 1:
                              op_loc_cnt = fr_ptr = 0
                              for ptr in op_loc:
                                  if op_loc_cnt == 0:
                                      colnames = colnames + df + "." + col[0:ptr]
                                  if op_loc_cnt > 0:
                                      colnames = colnames + col[fr_ptr] + df + "." + col[(1 + fr_ptr):ptr]  
                                  fr_ptr = ptr
                                  op_loc_cnt = op_loc_cnt + 1
                              else:
                                  colnames = colnames + col[fr_ptr] + df + "." + col[(1 + fr_ptr):] 
                      elif col.upper().startswith('DISTINCT'):
                          colnames += ",'" + col[8:].strip() + "',"
                          col_cnt += 1
                      else:
                          if col.strip().find('.') > 0:
                              colnames += "" + col + ","
                          else:
                              colnames += "'" + col + "',"
                          col_cnt += 1
              else:
                  if SQLKW=='SELECT':
                      pass
                  else:
                      if colnames[0]  == ',': colnames = colnames[1:]
                      if colnames[-1] == ',': colnames = colnames[:-1]

          return colnames, col_cnt

      def star2fields(str):
          str = str.strip()
          df_name = str[:str.find(".")].replace("'", "").replace('"', "")
          fld_str = ""
          for item in eval(df_name + '.columns'):
          # for item in [fld for fld in eval('tips.*'.replace(('*','columns'))]:
              fld_str = (fld_str + ", " if len(fld_str) > 0 else "") + "'" + item + "'"
          return fld_str

      str_cols, sel_col_cnt = extract_columns(df1, 'SELECT')
      if len(str_cols) > 0:
          if str_cols[0]  == ',': str_cols = str_cols[1:]
          if str_cols[-1] == ',': str_cols = str_cols[:-1]
          if str_cols.strip().find('.*') > 0:
              result = star2fields(str_cols.strip())
              if len(result) > 0: str_cols = result

      str_as, as_count = extract_columns(df1, 'AS')
      if len(str_as) > 0:
          str_as = str_as + ")"
      else:
          str_as = ""

      str_unique = ""
      if sel_col_cnt == 1:
          if inputSQL.upper().find('DISTINCT') > 0:  # SQL DISTINCT → df.unique()
              str_unique = ".unique()"

      str_condition = ""
      if inputSQL.upper().find('WHERE') > 0:
          str_condition = "[(" + df1 + "." + tmp[tmp.SQLKeyword == 'WHERE'].Obj.iloc[0] + ")"
          if inputSQL.upper().find('AND') > 0:
              for temp_cond in tmp[tmp.SQLKeyword == 'AND'].Obj:
                  str_condition += " & (" + ("" if temp_cond.find(df1) > 0 else df1 + ".") + temp_cond + ")"
          elif inputSQL.upper().find('OR') > 0:
              for temp_cond in tmp[tmp.SQLKeyword == 'OR'].Obj:
                  str_condition += " | (" + ("" if temp_cond.find(df1) > 0 else df1 + ".") + temp_cond + ")"
          str_condition = str_condition.replace(" IS NULL", ".isna()")
          str_condition = str_condition.replace(" IS NOT NULL", ".notna()")
      if len(str_condition) > 0: 
          str_condition += "]"

      temp_sort, col_cnt = extract_columns(df1, 'ORDER BY')
      if len(temp_sort) > 0:
          if temp_sort.find(".") > 0:
              temp_sort = "'" + temp_sort[1 + temp_sort.find("."):] + "'"
          str_orderby = ".sort_values([" + temp_sort + "], ascending=[True"
          comma_num = len(temp_sort) - len(temp_sort.replace(",",""))
          if comma_num > 0:
              str_orderby += ", True" * comma_num
          str_orderby += "])"
      else:
          str_orderby = ""

      temp_grp_cols, col_cnt = extract_columns(df1, 'GROUP BY')
      if len(temp_grp_cols) > 0:
          str_groupby = ".groupby([" + temp_grp_cols + "])"
      else:
          str_groupby = ""

      temp_having_cols, having_cnt = extract_columns(df1, 'HAVING')
      if len(temp_having_cols) > 0:
          str_having = ".groupby([" + temp_grp_cols + "])"
      else:
          str_having = ""
      str_having

      str_size = ""
      if inputSQL.upper().find('COUNT(') > 0:
          temp_size = tmp[tmp.SQLKeyword == 'GROUP BY COUNT'].Obj.iloc[0]
          if len(temp_size) > 0:
              str_size = ".size().to_frame('size').reset_index()" if len(temp_size) > 0 else ""

      str_limit_offset = ""
      if inputSQL.upper().find('LIMIT') > 0:
          temp_limit_slice = tmp[tmp.SQLKeyword == 'LIMIT'].Obj.iloc[0]
          if len(temp_limit_slice) > 0:
              if inputSQL.upper().find('OFFSET') > 0:
                  limit_offset = temp_limit_slice.split(sep='OFFSET ')
                  str_limit_offset = "[" + limit_offset[1] + ":" + str(sum([int(x) for x in limit_offset])) + "]"
              else:
                  str_limit_offset = "[:" + temp_limit_slice + "]"

      pd_str  = df1 + str_condition + ( '[' + str_cols + ']' if len(str_unique) > 0 else '[[' + str_cols + ']]' ) + str_as
      pd_str += str_unique + str_groupby + str_size + str_orderby + str_limit_offset

      pd_str = pd_str.replace('[[]]', '')
      if printPandasScript & printDebugInfo:
              print(tmp, '\n', pd_str)
      else:
          if printPandasScript: print(pd_str)
          if printDebugInfo:    print(tmp)

      return eval(pd_str)

  ##### 활용 예시 ##### 비교 : https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html
  # inputSQL = """    # 참조 : https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
  # SELECT PassengerId, Pclass, Name, COUNT(*),  # COUNT 외에 Aggregate Function은 사용할 수 없다. column은 table.* 식으로 할 수 있다.
  #        fld1 * fld2 - fld3 as calc_name       # 복잡한 계산식은 사용할 수 없다. 출력되는 script를 적당하게 수정해서 사용한다.
  #   FROM titanic_df                            # join은 사용할 수 없다. DB 연결하여 사용하거나 pandas를 사용한다.
  #  WHERE category = 'Setosa'                   #   ㄴ> pandas 예시 ☞ JCND = ['keyfld']; df1.merge(df2, left_on=JCND, right_on=JCND, how='inner', suffixes=('', '_2'), indicator=True)
  #    AND somefield > 10                        # BETWEEN과 같은 복잡한 조건 사용 불가
  #  GROUp BY PassengerId, Pclass, Name
  # HAVING ...
  #  ORDER BY PassengerId, Pclass, Name          # ORDER BY 정렬순서 지정 불가. 무조건 Ascending
  #  LIMIT 10 OFFSET 5 """      # 정렬순서 상 위에서 5째행(Nth Row)을 건너 뛰고(OFFSET), 10행 이내(LIMIT)에서 표시

  # sql2pd(inputSQL).sample(3)  # 출력하는 pandas script를 확인하고, 적절하게 수정하여 사용한다.

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def fum(cls): # Frequently Used Modules.
    FUM = '''
    %matplotlib inline
    import matplotlib.pyplot as plt
    import os, re, sys, importlib, sklearn, sqlite, sympy, matplotlib, time
    import numpy as np, scipy as sp, pandas as pd, seaborn as sns
    # import statsmodels.api as sm; import statsmodels.formula.api as smf
    # import tensorflow as tf; from tensorflow import keras
    from datetime import datetime
    from IPython.display import Markdown, display, Image
    from mpl_toolkits.mplot3d import Axes3D'''
    print(FUM)
  
  @classmethod
  def sayHello(cls):  
    cls.printcmd("""▣ 자주 사용하는 모듈 : np, sp, plt, sns, os, re, sys, [sklearn](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html), [rpy2](https://rpy2.github.io/doc.html), sqlite3→runSQL(,cursor), pd ☞ my.fum(); [pycaret](https://pycaret.org/functions), [tf](https://www.tensorflow.org/api_docs/python/tf), [keras](https://keras.io/api), [auto-keras](https://autokeras.com)<Br> &nbsp; &nbsp; ─ <font color='blue'>**my.LibInfo**</font> ★, help(), □? □?? Shift+Tab Shift+Tab(수회),[dir()](https://docs.python.org/3.7/tutorial/modules.html#the-dir-function),vars(),%whos,[List],(Tuple,),{Set},{'d':'Dict'}<Br> &nbsp; &nbsp; ─ %magic, %lsmagic %pinfo %env %store %%script ☞ [doc](https://ipython.readthedocs.io/en/stable/interactive/magics.html); python [1](https://docs.python.org) [2](https://en.wikipedia.org/wiki/Python_(programming_language)) [3](https://www.w3schools.com/python/default.asp) [4](https://www.python-course.eu/index.php) [5](https://wikidocs.net/book/1) [6](https://dojang.io/course/view.php?id=7); mathjax [1](https://www.onemathematicalcat.org/MathJaxDocumentation/MathJaxKorean/TeXSyntax_ko.html) [2](https://ko.wikipedia.org/wiki/위키백과:TeX_문법)""")
#     my.printbmd("""▣ 자주 사용하는 Python Module : np, sp, plt, sns, os, re, sys, sklearn, sqlite3→runSQL(,cursor), pd ☞ my.fum()  
#     - myLibInfo ★, help(), □? □?? Shift+Tab Shift+Tab(수회),dir(),%whos,[List],(Tuple,),{Set},{'d':'Dict'}  
#     - %magic, %lsmagic %pinfo %env %store %%script ☞ https://ipython.readthedocs.io/en/stable/interactive/magics.html""")
    # - https://docs.python.org/3/library/inspect.html ☞ class inspect.Parameter or function??
    # - Top 10 Magic Commands in Python to Boost your Productivity
    #   https://towardsdatascience.com/top-10-magic-commands-in-python-to-boost-your-productivity-1acac061c7a9

## =========================================================================================== ##
##                                       End of class my                                       ##
## =========================================================================================== ##
my.sayHello()

## ------------------------------------------------------------------------------------------- ##
my.LibInfo = pd.DataFrame( ### Class Variable LibInfo 동적으로 생성됨. 6개 Column으로 구성됨
  data = [ ['URL', 'Python', '', 1, 'What is a method in Python', 'https://stackoverflow.com/questions/3786881/what-is-a-method-in-python/3787670#3787670'],
           ['URL', 'DL', '', 1, '딥러닝 학습자료 모음', 'https://github.com/jwkcp/deeplearning'],
           ['URL', 'DL', 'Education', 1, '모두를 위한 딥러닝 시즌 2', 'https://deeplearningzerotoall.github.io/season2/'],
           ['URL', 'DL', '', 2, '쉽게 풀어쓴 딥 러닝의 거의 모든 것', 'https://slownews.kr/41461'],
           ['URL', 'DL', '', 9, '딥러닝 공부를 위한 책 교재', 'https://peanutcoders.com/how-to-study-deeplearning/'],
           ['URL', 'DL', '', 9, '내가 찾은 Deep Learning 공부 최단경로(?)', 'https://m.blog.naver.com/chesterroh/220920668374'],
           ['URL', 'DL', '', 5, '비전공자 공부 경험 공유, 도움되는 URL Link', 'https://theonly1.tistory.com/1564'],
           ['URL', 'Markdown', 'Math', 1, 'Writing Mathematic Fomulars in Markdown', 'https://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/'],
           ['URL', 'scikit-learn', 'mglearn', 1, 'scikit-learn 공부에 도움을 주는 자료', 'https://github.com/amueller/mglearn'],
           ['URL', 'scikit-learn', 'inflearn', 9, '권철민, 2020, 파이썬 머신러닝 완벽 가이드', "https://www.inflearn.com/course/파이썬-머신러닝-완벽가이드"],
           ['e-Book', 'Python', 'Language', 1, '파이썬 코딩 도장, 남재윤', "https://dojang.io/course/view.php?id=7"],
           ['e-Book', 'Python', 'Language', 1, '점프 투 파이썬, 박응용', 'https://wikidocs.net/book/1'],
           ['e-Book', 'SQLite', 'DB', 1, 'SQLite 책', 'http://www.devkuma.com/books/35'],
           ['myLib', 'Function', '', 1, 'pdHeadTail(df=None, n1=2, n2=2)', 'pandas dataframe을 대상으로 한 R의 psych::headTail 구현'],
           ['myLib', 'Function', '', 1, 'sPrintLog(dt=None)', 'datetime 출력'],
           ['myLib', 'Function', '', 1, 'npArrInfo(ndarrayObj, itemRelDesc=False)', 'np.info() 기능 확장'],
           ['myLib', 'Function', '', 1, 'printbmd(string)',     'print black & white text markdown print'],
           ['myLib', 'Function', '', 1, 'printcmd(string, color=None)', 'print color text markdown print'],
           ['myLib', 'Function', '', 1, 'isiterable(obj)', 'Wes McKinney, Python for Data Analysis'  ],
           ['myLib', 'Function', '', 1, 'ismutable(obj)',  '시퀀스 자료형에 대한 불변/가변 여부 회신'   ],
           ['myLib', 'Function', 'OOP',1, 'printSubClasses(getSubClasses(anyClass))', '지정된 Class에 대한 하위 Class를 찾아 보여준다'],
           ['myLib', 'Function', '', 1, 'hasproperty(strObj, rtnPropertyTF=False)', "유사 ≒ hasattr('object')"],
           ['myLib', 'Function', 'OOP', 1, 'descobj(strObj, show_property=True, pWidth=90)', 'Inheritance Hierarchy & Properties Info.'],
           ['myLib', 'Function', '', 1, 'compobj(strObj1, strObj2, pWidth=45)', 'Comparison of 2 Objects'],
           ['myLib', 'Function', '', 1, 'typelen(obj)', "Object's Short Information : type + len"],
           ['myLib', 'Function', '', 1, 'viewitems(obj, frPtr=0, toPtr=-1, dict_key=True)', "View Object's Data, from~to 모두 포함"],
           ['myLib', 'Function', 'matplotlib', 1, 'plot2d', 'y = x**2과 같은 1변수 함수의 평면 그래프'],
           ['myLib', 'Function', 'matplotlib', 1, 'plot3d', 'z = x**2 + 3*y와 같은 2변수 함수의 입체 그래프'],
           ['myLib', 'Function', 'sklearn', 1, 'train_val_test_split', 'X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(X, y, np.array([70, 20, 10]) / 100)'],
           ['myLib', 'Function', 'sklearn', 1, 'ChooseRightSklearnEstimator', "print(ChooseRightSklearnEstimator(1000, 'C', True)[1])"],
           ['myLib', 'Function', 'pandas', 1, 'sql2pd', "sql2pd(inputSQL, True)[:10]"],
           ['myLib', 'Function', 'sqlite3', 1, 'runSQL(sqlstr, cursor)', 'DML 실행 지원, pandas DataFrame 반환']
         ],
  columns = ['Category1',     'Category2',     'Category3', 'ValueRank', 'SubjectDescription', 'url_etc'] )

# https://stackoverflow.com/questions/17232013/how-to-set-the-pandas-dataframe-data-left-right-alignment
my.LibInfo = my.LibInfo.style.set_properties(**{'text-align': 'left'}).set_table_styles([ dict(selector='th', props=[('text-align', 'left')] ) ])

## rpy2 사용 설정
if importlib.util.find_spec("rpy2"):
    import rpy2
    import rpy2.robjects as ro  # 이름 충돌 방지를 위해 ro 사용. 즉, 『 rstr = "R 명령어"; ro.r(rstr)』와 같은 방식으로 사용

    print('【rpy2】', rpy2.__version__, ": 최초⇒'%load_ext rpy2.ipython', 다시 load(내부 R 세션 시작)⇒'%reload_ext rpy2.ipython'; %Rㆍ%%R == ro.r('R Script')")
    print(" %Rget,%R -i,%Rpush ⇔ %R -o,%Rpull ☞『df』 ①py⇒r:ro.r.assign('R.df',ro.pandas2ri.py2ri(PYdf)),②r⇒py:PYdf=ro.pandas2ri.ri2py(R.df)")
    
