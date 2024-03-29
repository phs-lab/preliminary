#-*- coding:utf-8 -*-

# myLib.py : Personal Library on Jupyter Notebook Environment for python beginners
# - Python 초보자의 학습곡선 단축을 위한 '초보자가 직접 작성&사용'하는 Function이나 정보 모음. 
# - 본인이 만들어서 직접 사용하는 것으로, 오류 가능성 항상 있음에 유의.
# - 향후 『import ./myLib』으로 사용할 수 있도록 변경해야 하는 과제가 있음.

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

import os, re, sys, io, importlib, sqlite3, sympy, matplotlib, time, inspect, math, pydot, graphviz, random, imageio, IPython
# https://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it
from datetime import datetime
from IPython.display import Markdown, display, SVG, Image, IFrame # https://stackoverflow.com/questions/19470099/view-pdf-image-in-an-ipython-notebook
from mpl_toolkits.mplot3d import Axes3D

boldFR = '\033[1m'; boldTO = '\033[0m'  # myLib에서는 descobj 밖으로...

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
  @classmethod
  def pdDescribe(cls, df):  # pandas dataframe 합치기 : https://antilibrary.org/2483
    """pandas dataframe에서 수치 특성들에 대해 기술통계를 쉽게 산출하고자 describe()함수를 응용하여 만들었음.
    참고 : 유일한 것을 추출할 때는 pd.unique()를 써도 되고, 다음과 같이 groupby를 응용해도 됨.
    (lambda d,c:pd.DataFrame({'count':d.groupby(c).count()[eval('d.columns[-1]')]}).sort_values(by=['count'],ascending=False,na_position='first'))(fish, 'Species')
    """
    if type(pd.DataFrame()) == type(df):
      DESC = df.describe()  # 정규성 검정 https://data-newbie.tistory.com/442, https://bioinformaticsandme.tistory.com/37
      tcols = DESC.columns
      DESC = pd.concat([DESC, pd.DataFrame({'IQR': DESC.loc['75%'] - DESC.loc['25%'] }).T], axis=0) # IQR (Interquartile Range) 반영 : https://hungryap.tistory.com/69
      DESC = pd.concat([DESC, pd.DataFrame({'LOLcnt':pd.DataFrame([ df[c] < DESC[c].loc['25%'] - DESC[c].loc['IQR'] * 1.5 for c in tcols ]).T.sum()}).T], axis=0) # Outlier, Lower Bound
      DESC = pd.concat([DESC, pd.DataFrame({'UOLcnt':pd.DataFrame([ df[c] > DESC[c].loc['75%'] + DESC[c].loc['IQR'] * 1.5 for c in tcols ]).T.sum()}).T], axis=0) # Outlier, Upper Bound
      CV = pd.DataFrame({'CV': df[tcols].mean() / df[tcols].std()})
      MODE = df[tcols].mode().head(1).T; MODE.columns = ['mode']
      SnK = pd.concat({'skewness':df[tcols].skew(), 'kurtosis':df[tcols].kurtosis()}, axis=1)
      rtn = pd.concat([pd.concat([pd.concat([DESC.T, MODE], axis=1), CV], axis=1), SnK], axis=1)
      rtn = rtn.astype({'count': 'int'}).astype({'LOLcnt': 'int'}).astype({'UOLcnt': 'int'})
    else:
      rtn = pd.DataFrame({'Error': "Argument {0} != pd.DataFrame".format(type(df))}, index=[0])
    return rtn

  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def pdInfo(cls, df, show_additional=True): # df.info() 개선
    if type(pd.DataFrame()) == type(df):
      t_columns  = df.columns; df.columns = [cn.replace(" ", "") for cn in df.columns] # 열 이름에 공란이 있는 경우에 대한 처리 (1)
      buf = io.StringIO()
      df.info(buf=buf)
      s = buf.getvalue()
      lines = [line.split() for line in s.splitlines()[5:-2]]
      if show_additional: 
        print(s.splitlines()[1], '\t', s.splitlines()[-1], '\n', s.splitlines()[-2]) # display(s.splitlines()[1], s.splitlines()[-2:])
      df_info = pd.DataFrame(lines, columns=['#', 'Column', 'Non-Null', 'garbage', 'DataType'])
      df_info['isNullSum'] = df.isnull().sum().values
      # df_info.set_index('Column', inplace=True)
      # df_info.iloc[:,1:] # pd.concat([ df_info.iloc[:,1:], df.describe(include='all').T.iloc[:,1:] ], axis=1)
      rtn = df_info.loc[:,['Column', 'Non-Null', 'isNullSum', 'DataType']]
      rtn['Column'] = t_columns; df.columns = t_columns # 열 이름에 공란이 있는 경우에 대한 처리 (2)
    else:
      rtn = pd.DataFrame({'Error': "Argument {0} != pd.DataFrame".format(type(df))}, index=[0])
    return rtn
    
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
                    '\nrank:', rank_res, '\tsize:', ndarrayObj.size, '\t', 'no of bytes(nbytes):', ndarrayObj.nbytes)
              if itemRelDesc:
                  print(strItemRelDesc)
          else:
              print("Only numpy.ndarray is allowed!")
      except NameError:
          print("NameError : name not defined!")
      else:
          if orgObjClass in [type(pd.DataFrame()), type(pd.Series(dtype='int'))]:
              print('\n', orgObjClass.index, "\n ♣ If (or After converted to) df=pd.DataFrame, run \033[1mdf.info()\033[0m or \033[1mdf.describe() my.pdDescribe(df)\033[0m for detail info.!")

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

  books4AIStudy = pd.DataFrame(  # https://tensorflow.blog/book-roadmap/ 참조하였으며, 이를 기반으로 관심 서적을 보강함. 데이터 과학 일반 및 자연어 처리 보강 필요
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
  # books4AIStudyGraph = my.makeTreeGraph(my.books4AIStudy, "TB") # LR: Left to Right, RL: Right to Left
  # my.viewPyDotGraph(books4AIStudyGraph)                         # TB: Top to Bottom ( = UD: Up Down), BT: Bottom to Top  

  # https://danbi-ncsoft.github.io/study/2018/05/04/study-regression_model_summary.html : 회귀 모델들을 특징에 따라 분류
  featureRegModel = pd.DataFrame(
      columns= [ 'TreeWBS', 'SrcNode', 'DstNode'],
      data = [ [ '0',   'Regression Model',          'No. of Independent Var.'],
               [ '0.1', 'No. of Independent Var.',   'Simple'],
               [ '0.2', 'No. of Independent Var.',   'Multiple'],
               [ '1',   'Regression Model',          'No. of Dependent Var.'],
               [ '1.1', 'No. of Dependent Var.',     'UniVariate'],
               [ '1.2', 'No. of Dependent Var.',     'MultiVariate'],
               [ '2',   'Regression Model',          'Combined Form of\nthe Regression Coefficients'],
               [ '2.1', 'Combined Form of\nthe Regression Coefficients', 'Linear'],
               [ '2.2', 'Combined Form of\nthe Regression Coefficients', 'NonLinear'],
               [ '3',   'Regression Model',          'Outlier Problem'],
               [ '3.1', 'Outlier Problem',           'Robust'],
               [ '3.2', 'Outlier Problem',           'Quantile'],
               [ '4.1', 'Regression Model',          'Characteristics of Dependent Var.'],
               [ '4.2', 'Characteristics of Dependent Var.', 'GLM'],
               [ '4.3', 'Characteristics of Dependent Var.', 'Survival Regression'],
               [ '4.4', 'Characteristics of Dependent Var.', 'Auto-Regression'],
               [ '5',   'Regression Model',          '"Inde/De"pendent Var.\nRelationship'],
               [ '5.1', '"Inde/De"pendent Var.\nRelationship', 'GAM'],
               [ '5.2', '"Inde/De"pendent Var.\nRelationship', 'Polynomial'],
               [ '6',   'Regression Model',          'MultiColLinearity Problem'],
               [ '6.1', 'MultiColLinearity Problem', 'Lasso / Ridge'],
               [ '6.2', 'MultiColLinearity Problem', 'PCR / PLS']
             ] )
  # featureRegModelGraph = my.makeTreeGraph(my.featureRegModel, "TB") # LR: Left to Right, RL: Right to Left
  # my.viewPyDotGraph(featureRegModelGraph)                           # TB: Top to Bottom ( = UD: Up Down), BT: Bottom to Top 

  # https://danbi-ncsoft.github.io/study/2018/05/04/study-regression_model_summary.html : 회귀 모델을 일반화 수준에 따라 계층적으로 정리
  hierarchyRegModel = pd.DataFrame(
      columns= [ 'TreeWBS', 'SrcNode', 'DstNode'],
      data = [ [ '0',        'Regression Model','Linear' ],
               [ '0.1',      'Linear',          'MultiVariate' ],
               [ '0.1.1',    'MultiVariate',    'SUR, VAR, Panel, …' ],
               [ '0.2',      'Linear',          'UniVariate' ],
               [ '0.2.1',    'UniVariate',      'Simple' ],
               [ '0.2.2',    'UniVariate',      'Multiple' ],
               [ '0.2.2.1',  'Multiple',        'Quantile' ],
               [ '0.2.2.2',  'Multiple',        'Robust' ],
               [ '0.2.2.3',  'Multiple',        'Lasso / Ridge' ],
               [ '0.2.2.4',  'Multiple',        'PCR / PLS' ],
               [ '0.2.2.5',  'Multiple',        'GLM' ],
               [ '0.2.2.5.1','GLM',             'Poisson Regression' ],
               [ '0.2.2.5.2','GLM',             'Ordinal Regression' ],
               [ '0.2.2.5.3','GLM',             'Logistic Regression' ],
               [ '0.2.2.6',  'Multiple',        'GAM' ],
               [ '0.2.2.6.1','GAM',             'Polynomial Regression' ],
               [ '0.2.3',    'UniVariate',      'Auto-Regression' ],
               [ '0.2.3.1',  'Auto-Regression', 'ARIMA, ARCH, …' ],
               [ '1',        'Regression Model','Non-Linear' ],
               [ '1.1',      'Non-Linear',      'DNN, CNN, RNN, …' ]
             ] )
  # hRegModelGraph = my.makeTreeGraph(my.hierarchyRegModel, "TB") # LR: Left to Right, RL: Right to Left
  # my.viewPyDotGraph(hRegModelGraph)                             # TB: Top to Bottom ( = UD: Up Down), BT: Bottom to Top 

  ## ------------------------------------------------------------------------------------------- ## 2021-06-16 (수) Orange3의 workflow 요약ㆍ정리에 사용하기 위해 작성
  @classmethod 
  def view_graphviz(cls, gvSourceCode):           # 설치 : https://pypi.org/project/graphviz ; Attribute : https://graphviz.org/doc/info/attrs.html
      graph = graphviz.Source(gvSourceCode)       # User guide : https://graphviz.readthedocs.io/en/stable/manual.html
      # display(Image(graph.pipe(format='png')))  # node 안의 내용 복사가 안되므로 좋지 않음
      display(SVG(graph.pipe(format='svg')))      # node 안의 내용 복사가 되므로 좋음 

  # 사례 : graphviz pocket reference - https://graphs.grevian.org/example
  # src = """
  # graph simple_graph { // graph가 아닌 digraph인 경우 `--` 대신 `->` 사용
  #     label = "Pocket Reference - Example 1: Simple Graph";
  #     labelloc = t;   // t: top, b: bottom
  #     rankdir = LR;   // LR: Left to Right, RL: Right to Left
  #     a -- b; b -- c; // TB: Top to Bottom ( = UD: Up Down), BT: Bottom to Top
  #     a -- c; c -- d;
  #     a -- e; e -- c;
  # }"""
  # my.view_graphviz(src)

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
      elif 'accuracy' in hist.columns:
        plt.plot(hist['epoch'], hist['accuracy'],     label='Trn Accuracy')
        plt.plot(hist['epoch'], hist['val_accuracy'], label='Val Accuracy')
        # plt.ylim([0, plt_ylim * hist['accuracy'].quantile(0.75)])  # plt.ylim([0,20])
        tMin1 = hist['accuracy'].quantile(0);          tMax1 = hist['accuracy'].quantile(1)
        tMin2 = hist['val_accuracy'].quantile(0);      tMax2 = hist['val_accuracy'].quantile(1)
      else:
        plt.plot(hist['epoch'], hist['sparse_categorical_accuracy'],     label='Trn Accuracy')
        plt.plot(hist['epoch'], hist['val_sparse_categorical_accuracy'], label='Val Accuracy')
        # plt.ylim([0, plt_ylim * hist['accuracy'].quantile(0.75)])  # plt.ylim([0,20])
        tMin1 = hist['sparse_categorical_accuracy'].quantile(0);          tMax1 = hist['sparse_categorical_accuracy'].quantile(1)
        tMin2 = hist['val_sparse_categorical_accuracy'].quantile(0);      tMax2 = hist['val_sparse_categorical_accuracy'].quantile(1)
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
  def make_confusion_matrix(cls, matrix, cols, np_dec=2):  # cols : 음성(Negative, 0), 양성(Positive, 1) 순서로 지정
      """사용법(2021-08-26) ① Library 임포트, ② 혼동행렬 작성, ③ 함수 호출
      from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support
      cmat = confusion_matrix(y_test, y_pred)
      cm = my.make_confusion_matrix(matrix=cmat, cols=['음성', '양성'], np_dec=6)  # cols : 음성(Negative, 0), 양성(Positive, 1) 순서로 지정
      cm
      
      # 참고1 - 정밀도, 재현율, F-점수 계산
      precision, recall, fscore, _ = precision_recall_fscore_support(y_test, predicted, average='binary')
      print(f'정밀도: {precision:.4f}\t\t', f'재현율: {recall:.4f}\t\t', f'F1-점수: {fscore:.4f}') # 계산 결과 확인
      
      # 참고2 - classification_report 확인
      print(classification_report(y_test, predicted))
      """
      total_population = matrix.sum()
      TN = matrix[0,0]; TP = matrix[1,1]; FP = matrix[0,1]; FN = matrix[1,0]
      accuracy = np.round(100 * (TP + TN) / total_population, np_dec); accuracy_str = '정분류율(%) ' + str(accuracy)
      tmp1 = np.concatenate((matrix, matrix.sum(axis=0).reshape((1,-1))), axis=0)
      matrix2 = np.concatenate((tmp1, tmp1.sum(axis=1).reshape((-1,1))), axis=1)
    
      rows = cols.copy()
      cnt = 0
      for item in cols:
          cols[cnt] = ('★' if cnt else '') + item + '(' + str(cnt) +')'
          rows[cnt] = item + '(' + str(cnt) +')' + ( ' - FN TP' if cnt else ' - TN FP' )
          cnt += 1
    
      cols.extend(['합계']); rows.extend(['합계'])
      n = len(cols)

      # '정답 데이터'가 n번 반복되는 리스트를 생성
      act = ['① 정답 데이터 (F/T)'] * n
      pred = ['② 예측 결과 (Negative, Positive) - 건수'] * n
    
      # 데이터프레임을 생성
      cm1 = pd.DataFrame(matrix2, columns=[pred, cols], index=[act, rows])
    
      # %값을 갖는 DataFrame 생성을 위해 위에서 한 것을 반복 실행
      matrix3 = np.round(100 * matrix2 / total_population, np_dec)
      pred = ['② 예측 결과 (Negative, Positive) - %'] * n
      cm2 = pd.DataFrame(matrix3, columns=[pred, cols], index=[act, rows])
      cm3 = pd.concat((cm1, cm2), axis=1)
    
      # 평가지표 계산 : 정밀도, 재현율, F-점수 계산
      # precision, recall, fscore, _ = precision_recall_fscore_support(y_test, y_pred, average='binary')
      # precision, recall, fscore = np.round((precision * 100, recall * 100, fscore * 100), np_dec)
      precision = np.round(100 * TP / (TP + FP), np_dec)
      recall    = np.round(100 * TP / (TP + FN), np_dec)
      fscore    = np.round(2 / (1/recall + 1/precision), np_dec)
      cm4 = pd.DataFrame([precision, recall, fscore], columns=[[accuracy_str], ['정밀도/재현율/F1-점수']], index=[act, rows])
    
      cm = pd.concat((cm3, cm4), axis=1)
    
      # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.set_properties.html
      return cm.style.set_properties(**{'text-align': 'right'}) 
    
  ## ------------------------------------------------------------------------------------------- ##
  @classmethod
  def chooseRightSklearnEstimator(cls,
                                  data_cnt=0,
                                  prediction_for_what=None,
                                  label_exist=None,
                                  data_scarce=None,
                                  print_sklearn_url=False):

      """인자 사용 호출 예시 : print(chooseRightEstimator(1000, 'C', True)[1])
                               print(chooseRightEstimator(1001, 'E', False, False, True)[1])
                               print(chooseRightEstimator(...))
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
    cls.printcmd("""▣ <sup>자주 사용하는</sup>모듈 : <a href="https://numpy.org" target="_blank">np</a>, <a href="https://scipy.org" target="_blank">sp</a>, <a href="https://matplotlib.org" target="_blank">plt</a>, <a href="https://seaborn.pydata.org" target="_blank">sns</a>, <a href="https://docs.python.org/3/library/os.html" target="_blank">os</a>, <a href="https://docs.python.org/ko/3/howto/regex.html" target="_blank">re</a>, <a href="https://docs.python.org/3/library/sys.html" target="_blank">sys</a>, <a href="https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html" target="_blank">sklearn</a>, <a href="https://rpy2.github.io/doc.html" target="_blank">rpy2</a>, <a href="https://www.sqlite.org/lang.html" target="_blank">sqlite3</a><sup><a href="https://www.sqlitetutorial.net" target="_blank">Tutorial</a></sup>→runSQL(,cursor), <a href="https://pandas.pydata.org" target="_blank">pd</a> ☞ my.fum(); <a href="https://pycaret.org/functions" target="_blank">pycaret</a>, <a href="https://www.tensorflow.org/api_docs/python/tf" target="_blank">tf</a>, <a href="https://keras.io/api" target="_blank">keras</a>, <a href="https://autokeras.com" target="_blank">auto-keras</a><Br> &nbsp; &nbsp; ─ <font color='blue'>**my.printCheatSheet('sklearn', [0,None])**</font> : print sklearn CheatSheet ToC ☞ ('**패키지**', **시작인덱스**, 종료인덱스, '검색문자열')<Br> &nbsp; &nbsp; ─ <font color='blue'>**my.LibInfo**</font> ★, help(), □? □?? Shift+Tab Shift+Tab(수회),[dir()](https://docs.python.org/3.7/tutorial/modules.html#the-dir-function),vars(),%whos,[List],(Tuple,),{Set},{'d':'Dict'}<Br> &nbsp; &nbsp; ─ %magic, %lsmagic %pinfo %env %store %%script ☞ <a href="https://ipython.readthedocs.io/en/stable/interactive/magics.html" target="_blank" title="IPython Built-in magic commands">Magic</a>; python <a href="https://docs.python.org" target="_blank" title="Python 공식 문서">1</a><sup>Python 공식 문서</sup> <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank" title="Python (programming language)">2</a><sup>Wiki</sup> <a href="https://www.w3schools.com/python/default.asp" target="_blank" title="Python Tutorial">3</a> <a href="https://www.python-course.eu/index.php" target="_blank" title="Python Courses and Tutorials">4</a> <a href="https://wikidocs.net/book/1" target="_blank" title="Jump to Python">5</a><sup>Jump to Python</sup> <a href="https://dojang.io/course/view.php?id=7" target="_blank" title="코딩 도장">6</a><sup>코딩 도장</sup>; mathjax <a href="https://www.onemathematicalcat.org/MathJaxDocumentation/MathJaxKorean/TeXSyntax_ko.html" target="_blank" title="MathJax에서 유용한 TEX 명령어">1</a> <a href="https://ko.wikipedia.org/wiki/위키백과:TeX_문법" target="_blank" title="위키백과:TeX_문법">2</a>""")
#   cls.printcmd("""▣ 자주 사용하는 모듈 : np, sp, plt, sns, os, re, sys, [sklearn](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html), [rpy2](https://rpy2.github.io/doc.html), sqlite3→runSQL(,cursor), pd ☞ my.fum(); [pycaret](https://pycaret.org/functions), [tf](https://www.tensorflow.org/api_docs/python/tf), [keras](https://keras.io/api), [auto-keras](https://autokeras.com)<Br> &nbsp; &nbsp; ─ <font color='blue'>**my.printCheatSheet('sklearn', [0,None])**</font> : print sklearn CheatSheet ToC ☞ ('**패키지**', **시작인덱스**, 종료인덱스, '검색문자열')<Br> &nbsp; &nbsp; ─ <font color='blue'>**my.LibInfo**</font> ★, help(), □? □?? Shift+Tab Shift+Tab(수회),[dir()](https://docs.python.org/3.7/tutorial/modules.html#the-dir-function),vars(),%whos,[List],(Tuple,),{Set},{'d':'Dict'}<Br> &nbsp; &nbsp; ─ %magic, %lsmagic %pinfo %env %store %%script ☞ [doc](https://ipython.readthedocs.io/en/stable/interactive/magics.html); python [1](https://docs.python.org) [2](https://en.wikipedia.org/wiki/Python_(programming_language)) [3](https://www.w3schools.com/python/default.asp) [4](https://www.python-course.eu/index.php) [5](https://wikidocs.net/book/1) [6](https://dojang.io/course/view.php?id=7); mathjax [1](https://www.onemathematicalcat.org/MathJaxDocumentation/MathJaxKorean/TeXSyntax_ko.html) [2](https://ko.wikipedia.org/wiki/위키백과:TeX_문법)""")
#     my.printbmd("""▣ 자주 사용하는 Python Module : np, sp, plt, sns, os, re, sys, sklearn, sqlite3→runSQL(,cursor), pd ☞ my.fum()  
#     - myLibInfo ★, help(), □? □?? Shift+Tab Shift+Tab(수회),dir(),%whos,[List],(Tuple,),{Set},{'d':'Dict'}  
#     - %magic, %lsmagic %pinfo %env %store %%script ☞ https://ipython.readthedocs.io/en/stable/interactive/magics.html""")
    # - https://docs.python.org/3/library/inspect.html ☞ class inspect.Parameter or function??
    # - Top 10 Magic Commands in Python to Boost your Productivity
    #   https://towardsdatascience.com/top-10-magic-commands-in-python-to-boost-your-productivity-1acac061c7a9
  
  class pkgCheatSheet:
    str_python = "" # numpy, pandas, sqlite, matplotlib, sklearn, pycaret and tfkeras(tensorflow and keras)

  @classmethod
  def printCheatSheet(cls, argPkg='sklearn', argIdx = [0, None], argSearchStr=[None, None]): # argIdxFr=0, argIdxTo=None
    rtn = False
    if argSearchStr[0] != None and argSearchStr[1] != None:    # 문자열 ['from', 'to')로 위치 찾기
      rtn = 'string search'
      strIdxFr = eval('cls.pkgCheatSheet.str_' + argPkg).lower().find(argSearchStr[0].lower()) # string.find(search, start, end)
      if strIdxFr == -1:
        rtn = 'SE0'
      else:
        strIdxTo = eval('cls.pkgCheatSheet.str_' + argPkg).lower().find(argSearchStr[1].lower(), strIdxFr + 1)
        if strIdxTo == -1:
          rtn = 'SE1'
    elif argSearchStr[0] != None and argSearchStr[1] == None:  # 문자열 argSearchStr[0]로 dictionary index 찾기 
      ptr = eval('cls.pkgCheatSheet.str_' + argPkg).lower().find(argSearchStr[0].lower())
      tmpPtr = None
      if ptr == -1:
        rtn = 1 # return "String '{}' not found!".format(argSearch)
      else:
        # index()는 문자열 안에서 문자 또는 문자열을 찾는 면에서 find()와 거의 비슷하지만 index()는 못 찾을 경우 예외를 발생시킵니다.
        for cnt in range(len(eval('cls.pkgCheatSheet.dct_' + argPkg))):
          dct_start = eval('cls.pkgCheatSheet.str_' + argPkg).find(eval('cls.pkgCheatSheet.dct_' + argPkg)[cnt])
          dct_range = dct_start + len(eval('cls.pkgCheatSheet.dct_' + argPkg)[cnt])
          if ptr >= dct_start and ptr < dct_range: tmpPtr = cnt
        if tmpPtr == None:
          rtn = 2 # 알 수 없는 논리 오류 발생
        else:
          argIdxTo = argIdxFr = tmpPtr
          rtn = 'dictionary key'
    else:  # Dictionary key를 인자로 직접 지정하여 검색
      rtn = 'dictionary key'
      argIdxFr = argIdx[0]; argIdxTo = argIdx[1]
      if argIdxTo == None:    argIdxTo = argIdxFr
      if argIdxTo < argIdxFr: rtn = 3
        
    if   rtn == 1: return "Error(1): While Searching, the string '{0}' is not found!".format(argSearchStr[0])
    elif rtn == 2: return "Error(2): While Searching, an unexplainable logic error has occurred."
    elif rtn == 3: return "Error(3): Without searching, the Dictionary to-index should be greater than or equal to the from-index."
    elif rtn == 'SE0' or rtn == 'SE1':
      error_str = argSearchStr[0] if rtn == 'SE0' else argSearchStr[1]
      return "Error(String Search): While Searching, the string '{0}' is not found!".format(error_str)
    else: 
      if rtn == 'dictionary key':
        cls.viewitems(eval('cls.pkgCheatSheet.dct_' + argPkg), argIdxFr, argIdxTo, False)
      else:  # rtn == 'string search'
        return eval('cls.pkgCheatSheet.str_' + argPkg)[strIdxFr:strIdxTo]
    
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
           ['myLib', 'Function', 'sklearn', 1, 'chooseRightSklearnEstimator', "print(chooseRightSklearnEstimator(1000, 'C', True)[1])"],
           ['myLib', 'Function', 'pandas', 1, 'sql2pd', "sql2pd(inputSQL, True)[:10]"],
           ['myLib', 'Function', 'sqlite3', 1, 'runSQL(sqlstr, cursor)', 'DML 실행 지원, pandas DataFrame 반환']
         ],
  columns = ['Category1',     'Category2',     'Category3', 'ValueRank', 'SubjectDescription', 'url_etc'] )

# https://stackoverflow.com/questions/17232013/how-to-set-the-pandas-dataframe-data-left-right-alignment
my.LibInfo = my.LibInfo.style.set_properties(**{'text-align': 'left'}).set_table_styles([ dict(selector='th', props=[('text-align', 'left')] ) ])

## =========================================================================================== ##
##                                        rpy2 사용 설정                                        ##
## =========================================================================================== ##
if importlib.util.find_spec("rpy2"):
    import rpy2
#   import rpy2.robjects as ro  # 이름 충돌 방지를 위해 ro 사용. 즉, 『 rstr = "R 명령어"; ro.r(rstr)』와 같은 방식으로 사용 # 2022-04-03 Comment 처리

    print('【rpy2】', rpy2.__version__, ": 최초⇒'%load_ext rpy2.ipython', 다시 load(내부 R 세션 시작)⇒'%reload_ext rpy2.ipython'; %Rㆍ%%R == ro.r('R Script')")
    print(" %Rget,%R -i,%Rpush ⇔ %R -o,%Rpull ☞『df』 ①py⇒r:ro.r.assign('R.df',ro.pandas2ri.py2ri(PYdf)),②r⇒py:PYdf=ro.pandas2ri.ri2py(R.df)")

## =========================================================================================== ##
##                                        pycaret usage                                        ##
## =========================================================================================== ##
# import pycaret  # utils 모듈만 포함되어 있음.
# from pycaret import datasets
# print(pycaret.__version__)

# from pycaret import classification as pyc_cls, regression  as pyc_reg, clustering as pyc_clstr
# from pycaret import nlp as pyc_nlp, anomaly as pyc_anom, arules as pyc_arules

# def pycaret_rough_ml_flow(PyCO=None, DataSet=None, Target=None, TrainSize=0.7, 
#                           CreModel=None, Sort=None, nSelect=5, automlOptimize=None,
#                           Normalize=False, IgnoreFeatures=None,
#                           NumClusters=4,                                          # pycaret.clustering
#                           Fraction=0.05,                                          # pycaret.anomaly > svm
#                           TransactionID=None, ItemID=None, IgnoreItems=None,    # pycaret.arules: Association Rule Mining
#                           CustomStopWords=None, MultiCore=True, NumTopics=None, # pycaret.nlp
#                           UseGPU=True, LogExperiment=False, ExpName=None):
#     """분류나 회귀의 "모델 성능 분석(Analyze model performance)" 부분을 제외하고 전체를 거의 한 번에 실행하도록 함수화한 것이며,
#     간단하게 실행해 보는데 좋으며, 개괄을 파악하고 pycaret이나 sklearn에서 매개변수 미세조정하면서 trial and error로 진행해야 할 듯하다.  
#       ㅇ 지원 algorithm : classification, regression, clustering, anomaly detection, association rule mining, nlp
#       ㅇ 확인 : Tutorial( https://pycaret.readthedocs.io/en/latest/tutorials.html ) 위주로 확인함
#       ㅇ ★순서★  
#          ㆍ『환경 설정 → 훈련ㆍ앙상블 → 성능 분석 → 자동 수행:predict(& check_metric) → "환경 설정ㆍFinalize" 분기』수회 진행 가능
#             ☞ 환경→훈련→분석→예측(& 평가)→분기→Finalize Model for Deployment→predict on unseen data(& check_metric)→Save the Model
#          ㆍfinalize( ) : 최종 예측 전에 train/valid로 나뉘어 사용된 "Data 전부를 이용하여 학습" 진행
#       ㅇ 분류 활용 예시 
#           pycaret.classification.models() # 사용 가능한 모델(Algorithm) 확인
#         
#           dataset = pycaret.datasets.get_data('juice')
#           df = dataset.sample(frac=0.9) # 0.95도 좋을 듯...
#           df_unseen = dataset.drop(data.index)
#           df.reset_index(drop=True, inplace=True)
#           df_unseen.reset_index(drop=True, inplace=True)
#           print('Data for Modeling: ' + str(df.shape), '\tUnseen Data For Predictions: ' + str(df_unseen.shape))
#
#           ctebsaf_results = pycaret_rough_ml_flow(PyCO=pyc_cls, DataSet=df, Target='Purchase', Sort='AUC', nSelect=5) 
#           pred_results = pyc_cls.predict_model(estimator=ctebsaf_results[-1], data=df_unseen) 
#           pycaret.utils.check_metric(pred_results['Purchase'], pred_results['Label'], metric = 'AUC') # 'Purchase': Target
#       ㅇ get_config() # setup으로 설정된 환경 확인.
#          예시 : get_config('X_train')[:3] # X: Transformed dataset (X), y: Transformed dataset (y), X_train, X_test, y_train, y_test
#     """
#     b1 = '\033[1m'; b2 = '\033[0m' # print 함수에서 "굵은 글씨" 출력
#     strExpName = ExpName if ExpName else "Exp_" + datetime.now().strftime("%Y%m%d%H%M%S")
#     if PyCO in [pycaret.classification, pycaret.regression]:
#         if Sort:
#             strSort = Sort
#         else:  # https://pycaret.org/compare-models/
#             if PyCO == pycaret.classification:
#                 strSort = 'Accuracy' # Classification: Accuracy, AUC, Recall, Precision, F1, Kappa, MCC
#             elif PyCO == pycaret.regression:
#                 strSort = 'R2'       # Regression: MAE, MSE, RMSE, R2, RMSLE, MAPE
#         strOptimize = automlOptimize if automlOptimize else strSort
#         step1 = "【 1 / 5 】 Setup Env." ; print(b1 + strExpName + b2 + ",", "▼" * 20, b1 + step1 + b2)
#         setup_env = PyCO.setup(data = DataSet, target = Target, train_size = TrainSize,
#                                normalize = Normalize, ignore_features = IgnoreFeatures,
#                                use_gpu = UseGPU, log_experiment = LogExperiment, experiment_name = strExpName)
#         step2 = "【 2 / 5 】 Train: Create & Compare Models" ; print(b1 + strExpName + b2 + ",", step1, "△" * 3, "▼" * 3, b1 + step2 + b2)
#         if CreModel:
#             cc_M = PyCO.create_model(model = CreModel)
#         else: # top_n_compared_M
#             cc_M = PyCO.compare_models(sort = strSort, n_select = nSelect) # default 'n_select=1' 사용 시 create_model과 같음
#         step3 = "【 3 / 5 】 Train: Tune every Models" ; print(b1 + strExpName + b2 + ",", step2, "△" * 3, "▼" * 3, b1 + step3 + b2)
#         tuned_M = [PyCO.tune_model(estimator = i) for i in cc_M]
#         step4 = "【 4 / 5 】 Ensemble/Blend/Stack/automl tuned Models" ; print(b1 + strExpName + b2 + ",", step3, "△" * 3, "▼" * 3, b1 + step4 + b2)
#         ensembled_M = [PyCO.ensemble_model(estimator = i) for i in tuned_M]
#         blended_M = PyCO.blend_models(estimator_list = tuned_M)
#         stacked_M = PyCO.stack_models(estimator_list = tuned_M)
#         automlBest_M = PyCO.automl(optimize = strOptimize) # This function returns the best model out of all trained models in current session
#         print("※ 모델 성능 분석 생략: PyCO.evaluate_model(blended_M); PyCO.interpret_model(TreeBasedModel,plot='reason',observation=0)")
#         step5 = "【 5 / 5 】 Finalize Model - DataSet 전체 재학습";print(b1 + strExpName + b2 + ",", step4, "△"*3, "▼"*3, b1 + step5 + b2)
#         finalized_M = PyCO.finalize_model(estimator = automlBest_M) # blended_M)
#         print("※ F/up: pred_res = PyCO.predict_model(final_M, df_unseen); pycaret.utils.check_metric(pred_res['?'], pred_res['Label'], metric='AUC')")
#         return setup_env, cc_M, tuned_M, ensembled_M, blended_M, stacked_M, automlBest_M, finalized_M
#     elif PyCO in [pycaret.clustering, pycaret.anomaly]: 
#         setup_env = PyCO.setup(data = DataSet, normalize = Normalize, ignore_features = IgnoreFeatures, 
#                                use_gpu = UseGPU, log_experiment = LogExperiment, experiment_name = strExpName)
#         if PyCO == pycaret.clustering:
#             cc_M = PyCO.create_model(model = CreModel, num_clusters = NumClusters)  # tuned_M = PyCO.tune_model(CreModel)
#         if PyCO == pycaret.anomaly:
#             cc_M = PyCO.create_model(CreModel, fraction=Fraction)
#         df_assigned_result = PyCO.assign_model(cc_M)
#         return setup_env, cc_M, df_assigned_result
#     elif PyCO == pycaret.arules:
#         setup_env = PyCO.setup(data = DataSet, transaction_id = TransactionID, item_id = ItemID, ignore_items = IgnoreItems)
#         df_result = PyCO.create_model()
#         return setup_env, df_result
#     elif PyCO == pycaret.nlp:
#         setup_env = PyCO.setup(data = DataSet, target = Target, 
#                                custom_stopwords=CustomStopWords, log_experiment = LogExperiment, experiment_name = strExpName)
#         cc_M = PyCO.create_model(model = CreModel, multi_core = MultiCore, num_topics = NumTopics)
#         df_assigned_result = PyCO.assign_model(cc_M)
#         return setup_env, cc_M, df_assigned_result
#     else:  # 여기까지 올 일은 거의 없으며, NameError 발생하기가 더 쉽다.
#         print("N/A, no suitable pycaret module exists!", 
#               'Please, run "' + b1 + PyCO.__name__ + b2 + '.models( )"', "and verify you input.")
## ====================================================================================================== ## End of Pycaret Usage

## CheatSheet =================================================================================== Begin : Dictionary 초기화 함수 ↓
def initCheatSheetDict(csNameStr): # argStr, argDict):
  ptr_fr = 0; cnt=0; # argStr = my.pkgCheatSheet.str_sklearn; argDict = my.pkgCheatSheet.dct_sklearn
  argStr = eval('my.pkgCheatSheet.str_' + csNameStr)
  argDict= eval('my.pkgCheatSheet.dct_' + csNameStr)
  while True:
    ptr_to = argStr.find('▣ CH', ptr_fr + 1)
    if ptr_to > 0:
      argDict.setdefault(cnt, argStr[ptr_fr : ptr_to])
      cnt += 1
      ptr_fr = ptr_to
    else:
      argDict.setdefault(cnt, argStr[ptr_fr:-1])
      break
  return len(argDict)

## ------------------------------------------------------------------------------------------- ## Dictionary 초기화 함수 ↑, ??? ↓

## ------------------------------------------------------------------------------------------- ## ??? 초기화 함수 ↑, python 일반 ↓
my.pkgCheatSheet.str_python = """▣ dct id : [0] ToC, [n] 이하는 주제별로 아래 정수 참조
  - my.printcmd(my.pkgCheatSheet.mdStr_python_toc)

▣ CH01. 환경 구성 ☞ 참조 : 코딩 도장 https://dojang.io/mod/page/view.php?id=2470  
  1.1 자주 사용하는 conda 명령어 ☞ https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/index.html
    - conda create --name MyEnv         # 가상환경 "MyEnv" 생성, 필요 시 "python=3.5 numpy=1.1"과 같이 패키지와 버전 지정 가능
      # 예시 : conda create -n TF2Keras tensorflow numpy scipy sympy matplotlib seaborn pandas pandas-profiling scikit-learn jupyterlab tensorflow-gpu gensim bokeh jedi jpype1 kiwisolver nltk spacy statsmodels tqdm pydot
    - conda env list                    # conda 가상환경 확인
    - conda info                        # 현재 환경 정보 출력
    - conda activate 접속할_가상환경이름 
    - conda deactivate                  # 현재 conda 환경에서 이탈
    - conda list | find /N /I "scikit"  # 윈도우에서 설치된 Module 확인
    - conda search package_name         # 패키지 검색
    - conda install package_name=ver    # 패키지 설치
    - conda update conda                # 패키지 conda 갱신 (Base 환경에서 실행, 아니면 "conda update -n base conda" 실행)
    - conda update package_name         # 패키지 업데이트
    - conda list --export > pkg_lst.txt # 패키지 목록 및 버전 정보 저장
    - conda install --file  pkg_lst.txt # 패키지 목록으로 설치
    - conda env export --name MyEnv > MyEnv.yml
    - conda env create -f MyEnv.yml     # MyEnv.yml에 저장된 정보로 환경 생성, 필요 시 사전에 yml file 내의 "환경 이름" 변경.
    - conda remove package_name
    - conda remove --name MyEnv --all   # 환경 "MyEnv" 전체 삭제
    - start /b jupyter notebook
    
  1.2 환경 확인을 위한 Python 구문
    - local device(CPU, GPU) 정보 확인
      from tensorflow.python.client import device_lib
      device_lib.list_local_devices()
    - python keyword 확인
      import this
      import keyword
      keyword.kwlist.sort()
      for cnt, item in zip(range(1,len(keyword.kwlist)+1), keyword.kwlist):
        print(item) if cnt%9 == 0 else print(item, end='\t')
      else:
        print('☞ Total', cnt, 'items')

  1.3 자주 사용하는 jupyter notebook magic command
    - %run -i ./preliminary/myLib.py
  
▣ CH02. 자료형 ☞ 참조 : 코딩 도장 https://dojang.io/mod/page/view.php?id=2189  
  - my.printcmd(my.pkgCheatSheet.mdStr_python_sequence)  
  
▣ CH03. 숫자, 변수, 연산자 : https://dojang.io/mod/page/view.php?id=2189 
  - 연산자 우선 순위 : https://dojang.io/mod/page/view.php?id=2461 # help('%')
  - 실수 값의 오차 : https://dojang.io/mod/page/view.php?id=2466
  
▣ CH04. 불과 비교ㆍ논리 연산자 : https://dojang.io/mod/page/view.php?id=2218 
  - 비트 연산자 : https://dojang.io/mod/page/view.php?id=2460

▣ CH05. 문자열 : https://dojang.io/mod/page/view.php?id=2218 
  - 이스케이프 시퀀스 : https://dojang.io/mod/page/view.php?id=2465
  
▣ CH06. if 조건문 : https://dojang.io/mod/page/view.php?id=2239
  - my.printcmd(my.pkgCheatSheet.mdStr_python_control)  
  
▣ CH07. Loop : https://dojang.io/mod/page/view.php?id=2279
  - my.printcmd(my.pkgCheatSheet.mdStr_python_control)  

▣ CH08. 시퀀스 자료형, 리스트, 튜플, 딕셔너리 : https://dojang.io/mod/page/view.php?id=2218
  - my.printcmd(my.pkgCheatSheet.mdStr_python_sequence)  

▣ CH09. 리스트 및 문자열 메서드 : https://dojang.io/mod/page/view.php?id=2305

▣ CH10. 딕셔너리 및 세트 메서드 : https://dojang.io/mod/page/view.php?id=2323

▣ CH11. 파일 : https://dojang.io/mod/page/view.php?id=2335

▣ CH12. 함수 : https://dojang.io/mod/page/view.php?id=2357

▣ CH13. 람다 : https://dojang.io/mod/page/view.php?id=2370

▣ CH14. 클로저 : https://dojang.io/mod/page/view.php?id=2370

▣ CH15. 클래스 : https://dojang.io/mod/page/view.php?id=2396
  - 프로퍼티 사용하기 : https://dojang.io/mod/page/view.php?id=2476
  - 메타 클래스 사용하기 : https://dojang.io/mod/page/view.php?id=2468
  - "with as"에 사용 가능한 클래스 만들기 : https://dojang.io/mod/page/view.php?id=2467
  
▣ CH16. 예외 : https://dojang.io/mod/page/view.php?id=2425
  - my.printcmd(my.pkgCheatSheet.mdStr_python_control)  

▣ CH17. 이터레이터 : https://dojang.io/mod/page/view.php?id=2425

▣ CH18. 제너레이터 : https://dojang.io/mod/page/view.php?id=2425

▣ CH19. 코루틴 : https://dojang.io/mod/page/view.php?id=2425
  - asyncio : https://dojang.io/mod/page/view.php?id=2469

▣ CH20. 데코레이터 : https://dojang.io/mod/page/view.php?id=2454

▣ CH21. 정규표현식 : https://dojang.io/mod/page/view.php?id=2454
     
▣ CH22. 모듈, 패키지 : https://dojang.io/mod/page/view.php?id=2454
  - 내장 함수 : https://dojang.io/mod/page/view.php?id=2464
"""  # my.pkgCheatSheet.str_python

# str_python의 추가 정보. my.printcmd()를 통해 markdown으로 출력. ☞ mdStr = markdown string
my.pkgCheatSheet.mdStr_python_toc = """[파이썬 코딩 도장](https://dojang.io/course/view.php?id=7) 핵심정리 중심 요약  

|주제|URL|관련 사항|
|:--|:--:|:---|
|1. 환경 구성|[○](https://dojang.io/mod/page/view.php?id=2470)|conda [User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html), rpy2 [Homepage](https://rpy2.github.io)|
|2. 자료형<Br>&nbsp; &nbsp; - byte, bytearray|[○](https://dojang.io/mod/page/view.php?id=2462)|my.printcmd(my.pkgCheatSheet.mdStr_python_sequence)|
|3. 숫자, 변수, 연산자|[○](https://dojang.io/mod/page/view.php?id=2189)||
|&nbsp; &nbsp; - 연산자 우선 순위|[○](https://dojang.io/mod/page/view.php?id=2461)|help('%')|
|&nbsp; &nbsp; - 실수 값의 오차|[○](https://dojang.io/mod/page/view.php?id=2466)||
|4. 불과 비교ㆍ논리 연산자|[○](https://dojang.io/mod/page/view.php?id=2218)|help('is')|
|&nbsp; &nbsp; - 비트 연산자|[○](https://dojang.io/mod/page/view.php?id=2460)||
|5. 문자열|[○](https://dojang.io/mod/page/view.php?id=2218)|help(':')|
|&nbsp; &nbsp; - 이스케이프 시퀀스|[○](https://dojang.io/mod/page/view.php?id=2465)||
|6. if 조건문|[○](https://dojang.io/mod/page/view.php?id=2239)|my.printcmd(my.pkgCheatSheet.mdStr_python_control)|
|7. Loop|[○](https://dojang.io/mod/page/view.php?id=2279)|my.printcmd(my.pkgCheatSheet.mdStr_python_control)|
|8. 시퀀스 자료형, 리스트, 튜플, 딕셔너리|[○](https://dojang.io/mod/page/view.php?id=2218)|my.printcmd(my.pkgCheatSheet.mdStr_python_sequence)|
|9. 리스트 및 문자열 메서드|[○](https://dojang.io/mod/page/view.php?id=2305)||
|10. 딕셔너리 및 세트 메서드|[○](https://dojang.io/mod/page/view.php?id=2323)||
|11. 파일|[○](https://dojang.io/mod/page/view.php?id=2335)||
|12. 함수|[○](https://dojang.io/mod/page/view.php?id=2357)|help('FUNCTIONS'); help('@')|
|13. 람다|[○](https://dojang.io/mod/page/view.php?id=2370)|help('lambda')|
|14. 클로저|[○](https://dojang.io/mod/page/view.php?id=2370)||
|15. 클래스|[○](https://dojang.io/mod/page/view.php?id=2396)|help('class'); help('.')|
|&nbsp; &nbsp; - 프로퍼티 사용하기|[○](https://dojang.io/mod/page/view.php?id=2476)||
|&nbsp; &nbsp; - 메타 클래스 사용하기|[○](https://dojang.io/mod/page/view.php?id=2468)||
|&nbsp; &nbsp; - "with as"에 사용 가능한 클래스 만들기|[○](https://dojang.io/mod/page/view.php?id=2467)||
|16. 예외|[○](https://dojang.io/mod/page/view.php?id=2425)|my.printcmd(my.pkgCheatSheet.mdStr_python_control)|
|17. 이터레이터|[○](https://dojang.io/mod/page/view.php?id=2425)||
|18. 제너레이터|[○](https://dojang.io/mod/page/view.php?id=2425)||
|19. 코루틴|[○](https://dojang.io/mod/page/view.php?id=2425)||
|&nbsp; &nbsp; - asyncio|[○](https://dojang.io/mod/page/view.php?id=2469)||
|20. 데코레이터|[○](https://dojang.io/mod/page/view.php?id=2454)||
|21. 정규표현식|[○](https://dojang.io/mod/page/view.php?id=2454)||
|22. 모듈, 패키지|[○](https://dojang.io/mod/page/view.php?id=2454)||
|&nbsp; &nbsp; - 내장 함수|[○](https://dojang.io/mod/page/view.php?id=2464)|[Library Reference > Built-in Functions](https://docs.python.org/3/library/functions.html)|
"""

my.pkgCheatSheet.mdStr_python_sequence = """

|구분1   |구분2          |자료형    |컬렉션<Br>(컨테이너)|이질/등질|가변/불변|예시|
|:-------|:--------------|:---------|:---------:|:---:|:---:|:----------|
|숫자형  |               |bool      | Χ | Χ |불변|    |
|        |               |int       | Χ | Χ |불변|    |
|        |               |float     | Χ | Χ |불변|    |
|        |               |complex   | Χ | Χ |불변|    |
|시퀀스형|문자형-텍스트  |str       | ○ |등질|불변|'1행', "1행", '''복수 행''', \"\"\"복수 행\"\"\"|
|        |문자형-바이너리|bytes     | ○ |등질|불변|    |
|        |문자형-바이너리|bytearray | ○ |등질|***가변***|    |
|시퀀스형|               |range     | ○ |등질|불변|range(start,stop,step) `#` start $\le$ value $\lt$ stop|
|        |               |tuple ( , ) | ○ |***이질***|불변|    |
|        |               |list  [ ] | ○ |***이질***|***가변***|    |
|매핑형  |               |dict {key:value}| ○ |***이질***|***가변***|    |
|집합형  |               |set   { } | ○ |***이질***|***가변***|    |
|        |               |frozenset | ○ |***이질***|불변|    |
"""  # my.pkgCheatSheet.str_python_sequence

my.pkgCheatSheet.mdStr_python_control = """▣ Python control structures  

|if - else|for|while|<a href="https://dojang.io/mod/page/view.php?id=2398" target="_blank" title="코딩도장 38.1 try except로 사용하기">try</a>|
|:----|:----|:----|:----|
|**if** condition:<Br>&nbsp; &nbsp; expression<Br>**elif** condition:<Br>&nbsp; &nbsp; expression<Br>**else**:<Br>&nbsp; &nbsp; expression<Br><Br>|**for** item **in** *collection*:<Br>&nbsp; &nbsp; expression<Br>**else:** `#` 항상 실행<Br>&nbsp; &nbsp; expression<Br><Br><Br><Br>|**while** condition:<Br>&nbsp; &nbsp; expression<Br>**else:** `#` 항상 실행<Br>&nbsp; &nbsp; expression<Br><Br><Br><Br>|**try:**<Br>&nbsp; &nbsp; expression<Br>**except:** `#` 예외 有, 이름 특정 가능<Br>&nbsp; &nbsp; expression<Br>**else:** `#` 예외 無<Br>&nbsp; &nbsp; expression<Br>**finally:** `#` 항상 실행<Br>&nbsp; &nbsp; expression|
"""  # my.pkgCheatSheet.str_python_control

# my.pkgCheatSheet.dct_python 초기화
my.pkgCheatSheet.dct_python = dict()
_ = initCheatSheetDict('python')

## ------------------------------------------------------------------------------------------- ## python 일반 ↑, python > numpy ↓

## ------------------------------------------------------------------------------------------- ## python > numpy ↑, python > pandas & Wrangling ↓
my.pkgCheatSheet.str_pandas = """pandas Cheat Sheet : https://pandas.pydata.org/
▣ dct id : 아래 ToC 참조

  * Asking for Help  
    help(pd.Series.loc) 
      - pandas documentation : http://pandas.pydata.org/pandas-docs/stable/index.html
      - https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html  
      - https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html
      - https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html
    
  * ToC 
    - 0. Help, ToC                      6. Reshaping Data
    - 1. Data Structures                7. Advanced Indexing
    - 2. Selection                      8. Duplicate / Missing / Grouping & Combining Data
    - 3. Drop, Sort & Rank              9. Miscellaneous Functions
    - 4. View Series/DataFrame Info.    10. pandas ↔ SQL 
    - 5. Data Alignment & 산술 연산
        
▣ CH01. Pandas Data Structures
  1.1 Series : A one-dimensional labeled/indexed array capable of holding any data type
    s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
  1.2 DataFrame : A two-dimensional labeled data structure with columns of potentially different types
    data = {'Country'   : ['Belgium', 'India', 'Brazil'],
            'Capital'   : ['Brussels', 'New Delhi', 'Brasília'],
            'Population': [11190846, 1303171035, 207847528]}
    df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])

▣ CH02. Selection ☞ Also see NumPy Arrays
  2.0 Summary of Indexing & Slicing : my.printcmd(my.pkgCheatSheet.mdStr_pandasIndexingSlicing)
  2.1 Getting subset of a Series/DataFrame
    Get one element of Series : s['b'] 
    Get subset of a DataFrame : df[1:] 

  2.2 Selecting, Boolean Indexing & Setting
    By Position
      df.iloc([0],[0])           # Select single value by row & column
      df.iat ([0],[0])
    By Label
      df.loc([0], ['Country'])   # Select single value by row & column labels
      df.at ([0], ['Country']) 
    By Label/Position
      df.ix[2]                   # Select single row of subset of rows
      df.ix[:,'Capital']         # Select a single column of subset of columns
      df.ix[1,'Capital']         # Select row and column
    Boolean Indexing
      s[~(s > 1)]                # Series s where value is not >1
      s[(s < -1) | (s > 2)]      # s where value is <-1 or >2
      df[df['Population']>1200]  # Use filter to adjust DataFrame
    Setting : s['a'] = 6         # Set index a of Series s to 6

▣ CH03. Drop, Sort & Rank
  3.1 Drop
    s.drop(['a', 'c'])           # Drop values from rows   (axis=0)
    df.drop('Country', axis=1)   # Drop values from columns(axis=1)

  3.2 Sort & Rank
    df.sort_index()              # Sort by labels along an axis
    df.sort_values(by='Country') # Sort by the values along an axis
    df.rank()                    # Assign ranks to entries

▣ CH04. Retrieving Series/DataFrame Information
  4.1 Basic Information
    df.shape                     # (rows,columns)
    df.index                     # Describe index
    df.columns                   # Describe DataFrame columns
    df.info()                    # Info on DataFrame
    df.count()                   # Number of non-NA values

  4.2 Summary (using axis)
    df.sum()                     # Sum of values
    df.cumsum()                  # Cummulative sum of values
    df.min() or df.max()         # Minimum or Maximum values
    df.idxmin() or df.idxmax()   # Minimum/Maximum index value
    df.describe()                # Summary statistics ☞ cf) my.pdDescribe(df)
    df.mean()                    # Mean of values
    df.median()                  # Median of values
    df.std()                     # Standard Deviation
    df.var()                     # Variance
    df.corr()                    # Correlation

  4.3 Applying Functions
    f = lambda x: x*2
    df.apply(f)                  # Apply function
    df.applymap(f)               # Apply function element-wise

▣ CH05. Data Alignment & Arithmetic Operations
  5.1 Internal Data Alignment
    NA values are introduced in the indices that don't overlap:
    s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
    s + s3

  5.2 Arithmetic Operations with Fill Methods
    You can also do the internal data alignment yourself with the help of the fill methods:
    s.add(s3, fill_value=0)
    s.sub(s3, fill_value=2)
    s.div(s3, fill_value=4)
    s.mul(s3, fill_value=3)

▣ CH06. Reshaping Data
    pdata = {'Date' : ['2016-03-01', '2016-03-02', '2016-03-01', '2016-03-03', '2016-03-02', '2016-03-03'],
             'Type' : ['a', 'b', 'c', 'a', 'a', 'c'],
             'Value': [11.432, 13.031, 20.784, 99.906, 1.303, 20.784]}
    df2 = pd.DataFrame(pdata, columns=['Date', 'Type', 'Value'])

  6.1 Pivot
    df3= df2.pivot(index='Date', # Spread rows into columns
                   columns='Type',
                   values='Value')

  6.2 Pivot Table
    df4 = pd.pivot_table(df2,    # Spread rows into columns
                         values='Value',
                         index='Date',
                         columns='Type'])

  6.3 Stack / Unstack
    stacked = df5.stack()        # Pivot a level of column labels
    stacked.unstack()            # Pivot a level of index labels

  6.4 Melt
    pd.melt(df2,                 # Gather columns into rows
            id_vars=["Date"],
            value_vars=["Type", "Value"],
            value_name="Observations")

▣ CH07. Advanced Indexing ☞ Also see NumPy Arrays
  7.0 Summary of Indexing & Slicing : my.printcmd(my.pkgCheatSheet.mdStr_pandasIndexingSlicing)
  7.1 Selecting
    df3.loc[:,(df3>1).any()]         # Select cols with any vals >1
    df3.loc[:,(df3>1).all()]         # Select cols with vals > 1
    df3.loc[:,df3.isnull().any()]    # Select cols with NaN
    df3.loc[:,df3.notnull().all()]   # Select cols without NaN

  7.2 Indexing With isin
    df[df.Country.isin(df2.Type)]    # Find same elements
    df[~df.Country.isin(df2.Type)]   # ~ : Negation
    df3.filter(items='a', 'b'])      # Filter on values
    df.select(lambda x: not x%5)     # Select specific elements

  7.3 Subset rows : Where & Query
    s.where(s > 0)                   # Subset the data
    df6.query('second > first')      # Query DataFrame

  7.4 Setting/Resetting Index
    df.set_index('Country') Set the index
    df4 = df.reset_index() Reset the index
    df = df.rename(index=str, Rename DataFrame
                   columns={"Country":"cntry",
                            "Capital":"cptl",
                            "Population":"ppltn"})

  7.5 Reindexing
    s2 = s.reindex(['a','c','d','e','b'])

        Forward Filling                            Backward Filling
    df.reindex(range(4), method='ffill')   s3 = s.reindex(range(5), method='bfill')
        Country Capital   Population            0  3
      0 Belgium Brussels    11190846            1  3
      1 India   New Delhi 1303171035            2  3
      2 Brazil  Brasilia   207847528            3  3
      3 Brazil  Brasilia   207847528            4  3

  7.6 MultiIndexing
    arrays = [np.array([1,2,3]), np.array([5,4,3])]
    df5 = pd.DataFrame(np.random.rand(3, 2), index=arrays)
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    df6 = pd.DataFrame(np.random.rand(3, 2), index=index)
    df2.set_index(["Date", "Type"])

▣ CH08. Duplicate / Missing / Grouping & Combining Data
  8.1 Duplicate Data
    s3.unique()                               # Return unique values
    df2.duplicated('Type')                    # Check duplicates
    df2.drop_duplicates('Type', keep='last')  # Drop duplicates
    df.index.duplicated()                     # Check index duplicates

  8.2 Missing Data
    df.dropna()                               # Drop NaN values
    df3.fillna(df3.mean())                    # Fill NaN values with a predetermined value
    df2.replace("a", "f")                     # Replace values with others

  8.3 Grouping Data
    a. Aggregation
      df2.groupby(by=['Date','Type']).mean()
      df4.groupby(level=0).sum()
      df4.groupby(level=0).agg({'a':lambda x:sum(x)/len(x),'b': np.sum}) 
    b. Transformation
      customSum = lambda x: (x+x%2)
      df4.groupby(level=0).transform(customSum)

  8.4 Combining Data
      cb1 = {'X1' : ['a', 'b', 'c'], 'X2': [11.432, 1.303, 99.906], 'Source':[1,1,1]}
      cb2 = {'X1' : ['a', 'b', 'd'], 'X3': [20.784, 'NaN', 20.784], 'Source':[2,2,2]}
      data1 = pd.DataFrame(cb1, columns=['X1', 'X2', 'Source'])
      data2 = pd.DataFrame(cb2, columns=['X1', 'X3', 'Source'])
    a. Merge  # how : {'left', 'right', 'outer', 'inner'}, default 'inner'
      # https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
      pd.merge(data1, data2, how='left', on=['X1'])
    b. Concatenate
      Series : Vertical
        s.append(s2)
      DataFrame : Vertical → axis=0 / Horizontal → axis=1
        pd.concat([s, s2],axis=1, keys=['One','Two'])
        pd.concat([data1, data2], axis=1, join='inner')

▣ CH09. Miscellaneous Functions
  9.1 Iteration
    df.iteritems() (Column-index, Series) pairs
    df.iterrows() (Row-index, Series) pairs

  9.2 Visualization ☞ Also see Matplotlib
    s.plot();   plt.show()  # Series
    df2.plot(); plt.show()  # DataFrame

  9.3 Dates
    df2['Date']= pd.to_datetime(df2['Date'])
    df2['Date']= pd.date_range('2000-1-1', periods=6, freq='M')
    dates = [datetime(2012,5,1), datetime(2012,5,2)]
    index = pd.DatetimeIndex(dates)
    index = pd.date_range(datetime(2012,2,1), end, freq='BM')  
    
▣ CH10. pandas ↔ SQL 
  - cf: https://www.sqlite.org/ https://www.sqlitetutorial.net/
        https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html
        https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
  - my.printcmd(my.pkgCheatSheet.mdStr_pandasSqliteComparisonSummary)
  - my.printcmd(my.pkgCheatSheet.mdStr_pandasSqliteComparisonTable)
  - my.printcmd(my.pkgCheatSheet.mdStr_pandasSqliteComparisonExample)

▣ CH11. Python & R 동시 사용(pd.DataFrame, sqlite3, rpy2 활용)
  - my.printcmd(my.pkgCheatSheet.mdStr_pandasSqliteOnRpy2PythonR)
"""

# my.pkgCheatSheet.dct_pandas 초기화
my.pkgCheatSheet.dct_pandas = dict()
_ = initCheatSheetDict('pandas')

# str_python의 추가 정보. my.printcmd()를 통해 markdown으로 출력. ☞ mdStr = markdown string
my.pkgCheatSheet.mdStr_pandasIndexingSlicing = """**▣ Indexing(지정) & Slicing(범위 자르기) 요약** 
+ <font color='red'>**i**</font>loc, loc은 모두 **인덱스**를 사용하는데, <font color='red'>**i**</font>loc은 위치를 가리키는 정수(<font color='red'>**i**</font>nteger) **Index**를, loc은 이름 **Index**를 사용한다.
+ dataframe은 위치 정수 인덱스나 이름 인덱스 모두를 사용하지만 적용 대상이 다르다.
  - Indexing(지정) : 열에 적용 - df[[열이름]] 방식으로 이름 인덱스를 사용하여 열을 지정하여 추출.
  - Slicing(범위 자르기) : 행에 적용 - df[인덱스:인덱스] 방식으로 위치 정수 또는 이름 인덱스 모두를 사용하여 자르기를 함.  
    Slicing 적용 범위 : From ≤ 위치 < To, From ≤ 이름 < To
+ 여러 건 지정 시 **[ ]**로 묶어 준다.

||||① dataframe (df=data_df)|||② df.iloc (위치 정수Index)|||③ df.loc (이름Index) ☞ '행=<font color="blue">숫자</font>'가 <font color="blue">일반</font>적|||
|:---|:---|:---|:---|:---:|:---:|:---|:---:|:---:|:---|:---:|:---:|
|<font color="blue">**Indexing**</font>|||<font color="blue">**df[ [ 열이름 ] ]**</font>|||<font color="blue">**df.iloc[행수치Index, 열수치Index]**</font>|||<font color="blue">**df.loc[행이름Index, 열이름]**</font>|||
||행(▤) [ ]|L|df[0]||<font color="red">Χ</font>|df.iloc[0] 또는 df.iloc[[0,2]]||<font color="blue">O</font>|df.loc[0]||<font color="red">Χ</font>|
|||N|df['one']||<font color="red">Χ</font>|df.iloc['one']||<font color="red">Χ</font>|df.loc['one'] ☞ 행 Series 반환||<font color="blue">O</font>|
||열(▥) [[ ]]|L|df[[0]]||<font color="red">Χ</font>|df.iloc[[0]] ☞ 행 추출됨||<font color="black">△</font>|df.loc[[0]]||<font color="red">Χ</font>|
|||N|df[['Name', 'Gender']]||<font color="blue">O</font>|df.iloc[['Name', 'Gender']]||<font color="red">Χ</font>|df.loc[['Name', 'Gender']]||<font color="red">Χ</font>|
||[행, 열] numpy|L|df[0, 0]||<font color="red">Χ</font>|df.iloc[0, 0]<Br>또는 df.iloc[[0,2], [0,2]]||<font color="blue">O</font>|df.loc[0, 0]||<font color="red">Χ</font>|
|||N|df['one', 'Name']||<font color="red">Χ</font>|df.iloc['one', 'Name']||<font color="red">Χ</font>|df.loc['one', 'Name']<Br>또는 df.loc[['one', 'three'], ['Name', 'Gender']]||<font color="blue">O</font>|
||[행][열] numpy|L|df[0][0]||<font color="red">Χ</font>|df.iloc[0][0] ☞ df.iloc[[0,2]][0] : 오류||<font color="blue">O</font>|df.loc[0][0]||<font color="red">Χ</font>|
|||N|df['one']['Name', 'Gender']||<font color="red">Χ</font>|df.iloc['one']['Name', 'Gender']||<font color="red">Χ</font>|df.loc['one']['Name', 'Gender']||<font color="red">Χ</font>|
||[행][[열]]|L|df[0][[0]]||<font color="red">Χ</font>|df.iloc[0][[0, 2]]||<font color="blue">O</font>|df.loc[0][[0]]||<font color="red">Χ</font>|
|||N|df['one'][['Name', 'Gender']]||<font color="red">Χ</font>|df.iloc['one'][['Name', 'Gender']]||<font color="red">Χ</font>|df.loc['one'][['Name', 'Gender']]<Br>또는 df.loc[['one','three']][['Name', 'Gender']]||<font color="blue">O</font>|
||[행, [열]]|L|df[0, [0,2]]||<font color="red">Χ</font>|df.iloc[0, [0,2]] ☞ 행 Series 추출됨||<font color="blue">O</font>|df.loc[0, [0,2]]||<font color="red">Χ</font>|
|||N|df['one', ['Name', 'Gender']]||<font color="red">Χ</font>|df.iloc['one', ['Name', 'Gender']]||<font color="red">Χ</font>|df.loc['one', ['Name', 'Gender']]<Br>또는 df.loc[['one','three'], ['Name', 'Gender']]||<font color="blue">O</font>|
||[L, [N]]|C|df[0, ['Name', 'Gender']]||<font color="red">Χ</font>|df.iloc[0, ['Name', 'Gender']]||<font color="red">Χ</font>|df.loc[0, ['Name', 'Gender']]||<font color="red">Χ</font>|
|<font color="blue">**Slicing**</font>|||<font color="blue">**df[행인덱스:행인덱스]**</font>|||<font color="blue">**df.iloc[수치:수치 ,수치:수치]**</font>|||<font color="blue">**df.loc[행이름:행이름, 열이름:열이름]**</font>|||
||행(▤) [ ]|L|df[:3]|O|<font color="blue">O</font>|df.iloc[:3]|O|<font color="blue">O</font>|df.loc[:3]||<font color="red">Χ</font>|
|||N|df[:'three']|●|<font color="blue">O</font>|df.iloc[:'three']||<font color="red">Χ</font>|df.loc[:'three']|●|<font color="blue">O</font>|
||열(▥) [[ ]]|L|df[[0:2]]||<font color="red">Χ</font>|df.iloc[[0:2]]||<font color="red">Χ</font>|df.loc[[0:2]]||<font color="red">Χ</font>|
|||N|df[['Name':'Gender']]||<font color="red">Χ</font>|df.iloc[['Name':'Gender']]||<font color="red">Χ</font>|df.loc[['Name':'Gender']]||<font color="red">Χ</font>|
||[행, 열] numpy|L|df[0:2, 0:2]||<font color="red">Χ</font>|df.iloc[0:2, 0:2]|O|<font color="blue">O</font>|df.loc[0:2, 0:2]||<font color="red">Χ</font>|
|||N|df['one':'three', 'Name':'Gender']||<font color="red">Χ</font>|df.iloc['one':'three', 'Name':'Gender']||<font color="red">Χ</font>|df.loc['one':'three', 'Name':'Gender']|●|<font color="blue">O</font>|
||[행][열] numpy|L|df[0:2][0:2] ☞ 행 Slicing 2회|O|<font color="black">△</font>|df.iloc[0:2][0:2] ☞ 행 Slicing 2회|O|<font color="black">△</font>|df.loc[0:2][0:2]||<font color="red">Χ</font>|
|||N|df['one':'three']['Name':'Gender']||<font color="red">Χ</font>|df.iloc['one':'three']['Name':'Gender']||<font color="red">Χ</font>|df.loc['one':'three']['Name':'Gender']||<font color="red">Χ</font>|
||[행][[열]]|L|df[0:2][[0:2]]||<font color="red">Χ</font>|df.iloc[0:2][[0:2]]||<font color="red">Χ</font>|df.loc[0:2][[0:2]]||<font color="red">Χ</font>|
|||N|df['one':'three'][['Name':'Gender']]||<font color="red">Χ</font>|df.iloc['one':'three'][['Name':'Gender']]||<font color="red">Χ</font>|df.loc['one':'three'][['Name':'Gender']]||<font color="red">Χ</font>|
||[행, [열]]|L|df[0:2, [0:2]]||<font color="red">Χ</font>|df.iloc[0:2, [0:2]]||<font color="red">Χ</font>|df.loc[0:2, [0:2]]||<font color="red">Χ</font>|
|||N|df['one':'three', ['Name':'Gender']]||<font color="red">Χ</font>|df.iloc['one':'three', ['Name':'Gender']]||<font color="red">Χ</font>|df.loc['one':'three', ['Name':'Gender']]||<font color="red">Χ</font>|
||[L, [N]]|C|df[0:2, ['Name':'Gender']]||<font color="red">Χ</font>|df.iloc[0:2, ['Name':'Gender']]||<font color="red">Χ</font>|df.loc[0:2, ['Name':'Gender']]||<font color="red">Χ</font>|
|||E|||||||df.loc['one':'three'][1:2] ☞ 행 slicing 2회||<font color="black">△</font>|
|주석|||L 위치, N 이름, C 혼합, E 기타||||||slicing to 포함: ● 포함, O 불포함|||"""

# str_python의 추가 정보. my.printcmd()를 통해 markdown으로 출력. ☞ mdStr = markdown string
my.pkgCheatSheet.mdStr_pandasSqliteComparisonSummary = """**▣ SQL과 pandas 구문 비교** 요약  
+ **DataFrame(이하 DF) 흐름을 살려 script를 작성한다. 『ㆍ, [Boolean], [[열]]』을 넘어 DF이 흐른다. DF을 SQL의 Cursor로 생각하면 쉽다.**
+ 적용 순서 : ① DF 기본 기능(ⓐ [[열]], ⓑ [Boolean], ⓒ Slicing) <font color='blue'>**>**</font> ② .loc (ⓐ, ⓑ + 이름index + ⓒTo포함) <font color='blue'>**>**</font> ③ .iloc (정수index + ⓒTo불포함)
+ Analytic, Aggregate Function, Case문 활용, 집합 개념 연산 등 **본격적인 Data 탐색 시에는 DB(SQL)를 사용**하고, 간단하게는 pandas를 사용한다.  
  - 중간에 학습곡선 단축을 위해 myLib의 sql2pd를 활용한다. : 복잡한 수식, 복잡한 조건, Join, Group by ... 안 됨
  - SQL Select 대응 pandas 구문으로는 이름 인덱스를 활용한 <font color='blue'>**df.loc[WhereBoolean</font>, [열]]** 방식을 사용한다. (cf: .iloc은 Boolean Indexing 안 됨)
+ Useful Links
  - pandas official doc. : [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html), [Cookbook](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html), [Essential basic functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html), [Comparison with SQL](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html)
  - Web Links : [Method Chaining in Pandas](https://towardsdatascience.com/the-unreasonable-effectiveness-of-method-chaining-in-pandas-15c2109e3c69), [Stackoverflow example](https://stackoverflow.com/questions/37155800/r-with-function-in-python), Wiki [SQL](https://en.wikipedia.org/wiki/SQL) & [SQL Syntax](https://en.wikipedia.org/wiki/SQL_syntax), [SQL → pandas](https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e)
"""

# str_python의 추가 정보. my.printcmd()를 통해 markdown으로 출력. ☞ mdStr = markdown string
my.pkgCheatSheet.mdStr_pandasSqliteComparisonTable = """**▣ 구조 요약** 
- 전체 : df1.merge()<font color='blue'>**.loc[WhereBoolean</font>, [열]]**.groupby(by=['열']).agg({열:[함수]}).sort_values(by=[열], ascending=[False])[Offset:Limit + Offset]
- Join : df1.merge(df2, left_on=['fld11', 'fld12'], right_on=['fld21', 'fld22'], how='inner/left/right/outer', suffixes=('', '_2'), indicator=True)

**▣ SQL과 pandas 구문 비교**

||SQL|Pandas ☞ SQL Select 대응 기본 구문: <font color='blue'>df.loc[WhereBoolean</font>, [열]]|
|:---|:---|:---|
|Select everything from …|SELECT `*` FROM table1|df|
||SELECT `*` FROM table1 LIMIT 3|df[:3] 또는 df.head(3) `#` 정렬 순서에 주의|
|Select specific columns|SELECT column1, column2<Br>FROM table1|`#` df[column_index_list] : [[ ]] 안에 열(이름 인덱스) 지정<Br>df[['column1', 'column2']]|
|WHERE clause<Br>And &, Or │, Not ~ 또는<Br>And, Or는 그대로 사용 가능|SELECT `*`<Br>FROM table1<Br>WHERE column1 > 1 AND column2 < 25|`#` SQL Where → Boolean Index<Br>`#` df[Condition] 또는 df.loc[Condition] 사용 가능<Br>df.loc[(df['column1'] > 1) & (df['column2'] < 25)]|
|WHERE clause, Between|SELECT `*`<Br>FROM table1<Br>WHERE column1 BETWEEN 1 and 5<Br>AND column2 IN (20,30,40,50)<Br>AND column3 LIKE '%arcelona%'|`#` 여러 건의 조건은 df[조건1][조건2][조건3] 방식으로 구현 가능<Br>df.loc[(df['column1'].between(1,5)) and <Br>&nbsp; &nbsp; &nbsp; &nbsp;(df['column2'].isin([20,30,40,50])) and <Br>&nbsp; &nbsp; &nbsp; &nbsp;(df['column3'].str.contains('arcelona'))]<Br>cf) ① % ≒ .str + .contains, .startswith, .endswith, ② Where ≒ <font color='blue'>**.query()**</font>|
|Table Join|SELECT t1.column1, t2.column1<Br>FROM table1 t1<Br>INNER JOIN table2 t2<Br>ON t1.column_id = t2.column_id|`#` 먼저 join 처리하고 열 조정/구성, 열名 같으면 on만 사용 가능<Br>단계① Join: df_joined=df1.merge(df2,left_on=[열],right_on=[열],how='inner')<Br>단계② Select: df_joined[['column1_df1', 'column2_df2']]<Br>cf) df1.merge(df2, on=[열...], how='inner')[['column1_df1', 'column2_df2']]|
|GROUP BY|SELECT column1, count(`*`)<Br>FROM table1<Br>GROUP BY column1|df.groupby(by=['column1'])['column1'].size( )<Br>DFGB=df.groupby(by=['column1']) ☞ DFGB[[열]].함수 또는 DFGB[열].함수<Br>또는 DFGB[[열]].agg([함수]) 또는 DFGB.agg({열:함수})|
|GROUP BY … HAVING|SELECT store, sum(sales)<Br>FROM table1<Br>GROUP BY store<Br>HAVING sum(sales) > 1000|df.groupby('store')['sales'].sum()<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .loc[df_grouped > 1000]|
|ORDER BY|SELECT `*`<Br>FROM table1<Br>ORDER BY column1 DESC|df.sort_values(by=['column1'], ascending=[False])<Br>cf) df.sort_index()|
|계산 열 추가|SELECT *, tip/total_bill as tip_rate from tips|tips<font color='green'>**.assign**</font>(tip_rate=tips['tip'] / tips['total_bill'])|
|UNION ALL|select ... from df1<Br>UNION ALL<Br>select ... from df2|pd.concat([df1, df2])|
|UNION|select ... from df1<Br>UNION<Br>select ... from df2|pd.concat([df1, df2]).drop_duplicates()|
|Window Functions<Br>☞ DB 사용 권장|SELECT *, SUM(field_name) OVER (<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; PARTITION BY url, service<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ORDER BY ts ) as total<Br>&nbsp; &nbsp; &nbsp; FROM df|(df.assign(total=df.sort_values(['ts'])<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .groupby(['url', 'service'])<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .field_name<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .cumsum())|
|Create Table<Br>*(cf: IF NOT EXISTS)*|create table df1 (id integer, name text)<Br>insert into df1 values (1, 'Harry Potter')<Br>insert into df1 values (2, 'Ron Weasley')|df1 = pd.DataFrame(<Br>&nbsp; &nbsp; { 'id': [1, 2], 'name': ['Harry Potter', 'Ron Weasley'] } )<Br>또는 df1.to_sql('df1', conn, if_exists='replace')|
|Update|update airports<Br>&nbsp; set home_link = 'string url'<Br>&nbsp;where ident == 'KLAX'|airports.loc[airports['ident'] == 'KLAX', 'home_link'] = 'string url'<Br>tips.loc[tips['tip'] < 2, 'tip'] *= 2 `#` 다른 예|
|Delete|delete from lax_freq<Br>&nbsp;where type = 'MISC'|방법① : lax_freq = lax_freq[lax_freq.type != 'MISC']<Br>방법② : lax_freq.drop(lax_freq[lax_freq.type == 'MISC'].index)|
"""

# str_python의 추가 정보. my.printcmd()를 통해 markdown으로 출력. ☞ mdStr = markdown string
my.pkgCheatSheet.mdStr_pandasSqliteComparisonExample = """**▣ SQL → pandas 예시**  
- 참조 URL : [SQL Syntax](https://en.wikipedia.org/wiki/SQL_syntax), [Comparison with SQL](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html), [SQL → pandas](https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e), [my Private Github](https://github.com/phs-lab/Packages/blob/master/Python/sqlite3/pandas_vs_sqlite3.ipynb)
<pre>
(5)  Select distinct                 (df1[['col1k', 'col2']]
            col1k, col2, col3
          , col2 / col3 as calc_col
(1)    from df1                                      
      inner join df2                     .merge(df2[['col2k', 'col3']],
         on df1.col1k = df2.col2k               on=[열...], (또는 left_on=['col1k'],right_on=['col2k'])
                                             how='inner/left/right/outer 중 택일' # , suffixes=('', '_2'), indicator=True
                                            )[['col1k', 'col2', 'col3']] # SQL (5) : SELECT col1k, col2, col3 
                                         .unique()            # SQL (5) : Select distinct 
                                         .assign(calc_col = col2 / col3)  # SQL (5) : AS 열 추가
(2)   where                              .query('condition')  # 또는 .loc['condition'] ☞ 같은 "기본 기능" 참고 : "df['condition']"
(3)   group by                           .groupby(by=['열'])   # 집계함수가 사용된 경우 : .groupby(by=['열']).agg({열:[함수]})
(4)  having                              .filter()
(6)   order by                           .sort_values(by=['col1k', 'col2'], ascending=[True, Flase])
(7)   Limit n offset m                   .nlargest(m + n)[Offset:Limit + Offset]  # offset, list은 아래와 같이 할 수도 있음
                                       # .head(n)             : offset 없이 Limit만 사용된 경우
                                       # .tail(n)             : offset + "order by 내림차순"
                                       # .head(m + n).tail(n) : offset + "order by 오름차순 또는 order by 없는 경우"
                                     ) </pre>"""

# str_python의 추가 정보. my.printcmd()를 통해 markdown으로 출력. ☞ mdStr = markdown string
my.pkgCheatSheet.mdStr_pandasSqliteOnRpy2PythonR = '''Python & R 동시 사용(pd.DataFrame, sqlite3, rpy2 활용)

|Python|Action|R in Jupyter Notebook & Python|
|:---|:---:|:---|
|import pandas as pd `#` myLib.py에 포함됨<Br>import sqlite3 &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp;`#` myLib.py에 포함됨<Br>%run -i myLib.py|Library|import rpy2<Br>from rpy2.robjects import r `#` 아래는 충돌 방지용<Br>`#` import rpy2.robjects as ro `#` r()대신 ro.r() 사용|
||R세션|&nbsp; &nbsp; 최초>> %load_ext rpy2.ipython<Br>재시작>> %reload_ext rpy2.ipython|
|DB = './sqlite3.db'<Br>pycon = sqlite3.connect(DB) `#` or ':memory:'<Br>① myLib.py runSQL 활용<Br>pycursor = pycon.cursor( ) `#` pd 활용 시 불필요<Br>② pd.read_sql_query 사용: 접속(connect)으로 충분|DB 연결|r('library(DBI); require(Tidyverse)')<Br>`#` memory SQLite DB는 `python - r` 공유 안 됨<Br>r("rcon <- dbConnect(RSQLite::SQLite(), '" + DB + "')")|
|①, ② : pycon, <font color="blue">**② : pycursor**</font>|연결 확인|r("rcon")|
|① myLib.py runSQL 활용<Br>def pysql(sqlstr=None, c=<font color="blue">**pycursor**</font>, p=None,<Br> &nbsp; &nbsp; s=None, m=False, l=False):<Br> &nbsp; &nbsp; return runSQL(sqlstr, c, p, s, m, l)<Br>② pd.read_sql_query 사용<Br>def pysql(sqlstr=None, dbcon=**pycon**):<Br> &nbsp; &nbsp; return pd.read_sql_query(sql=sqlstr, con=dbcon)|함수 선언|def rsql(sqlstr="""DML...""", con=rcon):<Br> &nbsp; &nbsp; return r("dbGetQuery(con, '" + sqlstr + "')")<Br>`#` 참고: pysql과 달리 <font color="blue">**SELECT**</font>만 가능함|
|iris_pydf.to_sql('iris_py', pycon) |DF→Table|r('dbWriteTable(rcon, "iris_r", iris_rdf)')|
|pysql("select * from sqlite_master")<Br>`)`外상동+"where tbl_name='특테' and type='table'")<Br>sqlstr="""select ... from 특정테이블"""; pysql(sqlstr)|DF←Table|r('dbListTables(rcon)') `#` rsql( ) 사용 가능<Br>r('dbListFields(con, "특정테이블")') `#` 필드명 조회 <Br>sqlstr = """Select ... from 특정테이블"""; rsql(sqlstr)|
|pycon.close( )|연결 해제|r('dbDisconnect(rcon)')|
|py2DArray = np.array([[1, 2, 3], [4, 5, 6]])<Br>pd.DataFrame(py2DArray))|DF 예시1|R예시1(예정)|
|pyDict = {"col1": [1,2], "col2": [3,4], "col3": [5,6]}<Br>pd.DataFrame(pyDict)|DF 예시2|R예시2(예정)|
|pydf = pd.DataFrame(data=[[1, 'a'],[2, 'b'],[3, 'c']],<Br>index=range(1,4), columns=['c1', 'c2'])|DF 예시3|R예시3(예정)|
||rpy2<Br>용례 ①|rcmdstr = """<Br>set.seed(100)<Br>x <- rnorm(100)<Br>y <- x + rnorm(100,sd=0.5)<Br>lmout <- lm(y~x)<Br>lmout$coefficients"""<Br>coef=r(rcmdstr)|
||rpy2<Br>용례 ②|rcmdstr = """<Br>iris %>% head(10) **%>%**<Br> &nbsp; &nbsp; tail(3) """<Br>r(rcmdstr)|
'''
my.pkgCheatSheet.str_pandasWrangling = """Data Wrangling with pandas Cheat Sheet
▣ dct id 
   - 0. ToC
   - 1. Tidy Data                    8. Group Data
   - 2. Syntax                       9. Windows
   - 3. Method Chaining              10. Handling Missing Data
   - 4. Reshaping Data               11. Make New Columns
   - 5. Subset Observations (Rows)   12. Combine Data Sets
   - 6. Subset Variables (Columns)   13. Plotting
   - 7. Summarize Data               99. Remark

▣ CH01. Tidy Data – A foundation for wrangling in pandas

▣ CH02. Syntax – Creating DataFrames

▣ CH03. Method Chaining
Most pandas methods return a DataFrame so that another pandas method can be applied to the result. 
This improves readability of code as follows:
df = (pd.melt(df)
        .rename(columns={
                'variable' : 'var',
                'value' : 'val'})
        .query('val >= 200')
     )

▣ CH04. Reshaping Data – Change the layout of a data set

▣ CH05. Subset Observations (Rows)

▣ CH06. Subset Variables (Columns)

▣ CH07. Summarize Data

▣ CH08. Group Data

▣ CH09. Windows

▣ CH10. Handling Missing Data

▣ CH11. Make New Columns

▣ CH12. Combine Data Sets
   - https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

▣ CH13. Plotting

▣ CH99. Remark : http://pandas.pydata.org/ This cheat sheet inspired by Rstudio Data Wrangling Cheatsheet 
(https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf) Written by Irv Lustig, Princeton Consultants

"""

# my.pkgCheatSheet.dct_pandasWrangling 초기화
my.pkgCheatSheet.dct_pandasWrangling = dict()
_ = initCheatSheetDict('pandasWrangling')

## ------------------------------------------------------------------------------------------- ## python > pandas & Wrangling ↑, python > sqlite ↓

## ------------------------------------------------------------------------------------------- ## python > sqlite ↑, python > matplotlib ↓

## ------------------------------------------------------------------------------------------- ## python > matplotlib ↑, python > scikit-learn ↓
my.pkgCheatSheet.str_sklearn = """scikit-learn Cheat Sheet @ https://www.datacamp.com/community/data-science-cheatsheets?tag=python
▣ dct id : [0] ToC, [1] Data, [2] Model, [3] Training, [4] Prediction, [5] Evaluation, [6] Tuning, [7] Basic Examples
    - (class pkgCheatSheet에서) 구분 조회 : print(str_sklearn[str_sklearn.index('구분1'):str_sklearn.index('구분2')])
    - User Guide : https://scikit-learn.org/stable/user_guide.html ☞ 파이썬 일반 : https://wikidocs.net/book/1
    - Choosing the Right Estimator : https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html
      ☞ udf 사용 사례 : print(chooseRightEstimator(1000, 'C', True)[1]); print(chooseRightEstimator(...))
    - ETC : https://medium.com/@chris_bour/an-extended-version-of-the-scikit-learn-cheat-sheet-5f46efc6cbb
             https://towardsdatascience.com/your-ultimate-data-mining-machine-learning-cheat-sheet-9fce3fa16
                  ☞ https://www.kdnuggets.com/2021/01/ultimate-scikit-learn-machine-learning-cheatsheet.html
             https://www.kdnuggets.com/2019/09/train-sklearn-100x-faster.html 
             https://www.quora.com/q/abcofdatascienceandml/Scikit-learn-Machine-Learning-packages-Syntax-Part-8
             data camp official blog : https://www.datacamp.com/community/blog/scikit-learn-cheat-sheet, 2017-01-04

▣ CH01. Handling the Data (Also see NumPy & Pandas)
  1.1 Loading the Data ☞ https://scikit-learn.org/stable/datasets/index.html
      - Your data needs to be numeric and stored as NumPy arrays or SciPy sparse matrices. 
        Other types that are convertible to numeric arrays, such as Pandas DataFrame, are also acceptable.
      import numpy as np
      X = np.random.random((10,5))
      y = np.array(['M','M','F','F','M','F','M','M','F','F','F'])
      X[X < 0.7] = 0

  1.2 Traning and Test Data Split
      from sklearn.model_selection import train_test_split
      X_train, X_test, y_train, y_test = train_test_split(X, y) #, random_state=33)

  1.3 Processing the Data ☞ https://scikit-learn.org/stable/data_transforms.html
    (1) Standardization
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler().fit(X_train)
        standardized_X = scaler.transform(X_train)
        standardized_X_test = scaler.transform(X_test)
    (2) Normalization
        from sklearn.preprocessing import Normalizer
        scaler = Normalizer().fit(X_train)
        normalized_X = scaler.transform(X_train)
        normalized_X_test = scaler.transform(X_test)
    (3) Binarization
        from sklearn.preprocessing import Binarizer
        binarizer = Binarizer(threshold=0.0).fit(X)
        binary_X = binarizer.transform(X)
    (4) Encoding Categorical Features
        from sklearn.preprocessing import LabelEncoder
        enc = LabelEncoder()
        y = enc.fit_transform(y)
    (5) Imputing Missing Values
        from sklearn.preprocessing import Imputer
        imp = Imputer(missing_values=0, strategy='mean', axis=0)
        imp.fit_transform(X_train)
    (6) Generating Polynomial Features
        from sklearn.preprocessing import PolynomialFeatures
        poly = PolynomialFeatures(5)
        poly.fit_transform(X)

▣ CH02. Create Your Model ☞ https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html
  ☞ 참고 - udf 사용 사례 : print(chooseRightEstimator(1000, 'C', True)[1]); print(chooseRightEstimator(...))
  2.1 Supervised Learning Estimators ☞ https://scikit-learn.org/stable/supervised_learning.html
    (1) Linear Regression
        from sklearn.linear_model import LinearRegression
        lr = LinearRegression(normalize=True)
    (2) Support Vector Machines (SVM)
        from sklearn.svm import SVC
        svc = SVC(kernel='linear')
    (3) KNN
        from sklearn import neighbors
        knn = neighbors.KNeighborsClassifier(n_neighbors=5)
    (4) Naive Bayes
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()

  2.2 Unsupervised Learning Estimators ☞ https://scikit-learn.org/stable/unsupervised_learning.html
    (1) K Means
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters=3, random_state=0)
    (2) Principal Component Analysis (PCA)
        from sklearn.decomposition import PCA
        pca = PCA(n_components=0.95)

▣ CH03. Model Fitting / Training
  3.1 Supervised Learning
      lr.fit(X, y)                        # Fit the model to the data
      svc.fit(X_train, y_train)
      knn.fit(X_train, y_train)

  3.2 Unsupervised Learning
      kmeans.fit(X_train)                 # Fit the model to the data
      pca = pca.fit_transform(X_train)    # Fit the model to the data, then transform it

▣ CH04. Prediction
  4.1 Supervised Estimators
      y_pred = lr.predict(X_test)         # predict : Predict labels
      y_pred = svc.predict(np.random.random((2,5)))
      y_pred = knn.predict_proba(X_test)  # predict_proba : Estimate probability of a label

  4.2 Unsupervised Estimators
      y_pred = k_means.predict(X_test)    # Predict labels in clustering algorithms

▣ CH05. Evaluate Your Model’s Performance ☞ https://scikit-learn.org/stable/model_selection.html
  5.1 Classification Metrics
    (1) Accuracy Score
        knn.score(X_test, y_test)         # Estimator score method
        from sklearn.metrics import accuracy_score
        accuracy_score(y_test, y_pred)    # Metric scoring function
    (2) Classification Report             # Precision, recall, f1-score and support
        from sklearn.metrics import classification_report
        print(classification_report(y_test, y_pred))
    (3) Confusion Matrix
        from sklearn.metrics import confusion_matrix
        print(confusion_matrix(y_test, y_pred))

  5.2 Regression Metrics
    (1) Mean Absolute Error
        from sklearn.metrics import mean_absolute_error
        y_true = [3, -0.5, 2]
        mean_absolute_error(y_true, y_pred)
    (2) Mean Squared Error
        from sklearn.metrics import mean_squared_error
        mean_squared_error(y_test, y_pred)
    (3) R² Score
        from sklearn.metrics import r2_score
        r2_score(y_true, y_pred)

  5.3 Clustering Metrics
    (1) Adjusted Rand Index
        from sklearn.metrics import adjusted_rand_score
        adjusted_rand_score(y_true, y_pred)
    (2) Homogeneity
        from sklearn.metrics import homogeneity_score
        homogeneity_score(y_true, y_pred)
    (3) V-measure
        from sklearn.metrics import v_measure_score
        metrics.v_measure_score(y_true, y_pred)

  5.4 Cross-Validation
      from sklearn.cross_validation import cross_val_score
      print(cross_val_score(knn, X_train, y_train, cv=4))
      print(cross_val_score(lr, X, y, cv=2))

▣ CH06. Tune Your Model
  6.1 Grid Search
      from sklearn.grid_search import GridSearchCV
      params = {"n_neighbors": np.arange(1,3), "metric": ["euclidean", "cityblock"]}
      grid = GridSearchCV(estimator=knn, param_grid=params)
      grid.fit(X_train, y_train)
      print(grid.best_score_)
      print(grid.best_estimator_.n_neighbors)

  6.2 Randomized Parameter Optimization
      from sklearn.grid_search import RandomizedSearchCV
      params = {"n_neighbors": range(1,5), "weights": ["uniform", "distance"]}
      rsearch = RandomizedSearchCV(estimator=knn, param_distributions=params, cv=4, n_iter=8, random_state=5)
      rsearch.fit(X_train, y_train)
      print(rsearch.best_score_)

▣ CH07. Basic Examples ☞ Help : import mglearn  # https://github.com/amueller/mglearn 
  7.1 Cheat Sheet ☞ ML Process : https://volcanohong.github.com/content/images/2016/ml_process.png
      from sklearn import neighbors, datasets, preprocessing
      from sklearn.model_selection import train_test_split
      from sklearn.metrics import accuracy_score

      iris = datasets.load_iris()  # load_breast_cancer, load_boston, load_iris
      X, y = iris.data[:, :-1], iris.target
      X_train, X_test, y_train, y_test = train_test_split(X, y) #, random_state=33)

      scaler = preprocessing.StandardScaler().fit(X_train)
      X_train = scaler.transform(X_train)
      X_test = scaler.transform(X_test)

      model = neighbors.KNeighborsClassifier(n_neighbors=5)
      model.fit(X_train, y_train)

      y_pred = model.predict(X_test)
      accuracy_score(y_test, y_pred)

  7.2 koipa.or.kr base class 강의 내용 (위 0.1의 module import 부분은 같기때문에 생략함)
      DataBunch = datasets.load_iris()
         # descobj('DataBunch'); print(DataBunch.DESCR); 
      pd_data   = pd.DataFrame(DataBunch.data,   columns=DataBunch.feature_names)
      pd_target = pd.DataFrame(DataBunch.target, columns=['target'])
      data = pd.concat([pd_data, pd_target], axis=1)

      # pandas function 사용한 EDA (Visualization 포함) 실행
      np.array(data).shape; data.info(); data.sample(5); data.describe() 
          # 정규성 검정을 위해 skewness(왜도), kurtosis(첨도) 확인
          # Skew = pd.DataFrame(data.skew(), columns=['Skewness'])
          # Kurt = pd.DataFrame(data.kurt(), columns=['Kurtosis'])
          # data.describe().T.join(Skew.join(Kurt, how='left'), how='left')
      data.boxplot(figsize=(10,8), rot=45)  # outliers 파악 및 필요 시 cleansing 처리
      import seaborn as sns
      sns.pairplot(data, vars=data.columns[:4], hue='target')  # regression인 경우에는 hue를 사용하지 않음
      plt.figure(figsize=(10,8)); sns.heatmap(data.corr(), annot=True, cbar=True)

      # Hold-out
      from sklearn.model_selection import train_test_split
      X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,:-1], data.iloc[:,-1])
         # X_train, X_test, y_train, y_test = train_test_split(data.loc[:,:'petal width (cm)'], data.target)

      from sklearn.neighbors import KNeighborsClassifier
      knn = KNeighborsClassifier()      # model building : instance 만들 때 하이퍼파라미터 설정
      # vars(knn); knn.fit(); vars(knn) # 설정된 하이퍼파라미터를 vars(모델명)으로 알 수 있음. fit 전ㆍ후에 실시
      knn.fit(X_train, y_train)         # training
      y_pred = knn.predict(X_test)      # prediction
      knn.score(X_test, y_test)         # evaluation
      accuracy_score(y_test, y_pred)

      from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold, ShuffleSplit
      import mglearn; mglearn.plot_cross_validation.plot_stratified_cross_validation()
      kf = KFold(Class고려 수치 지정) # StratifiedKFold(분류_좌동), ShuffleSplit()
      cv_knn = cross_val_score(KNeighborsClassifier(), 
                     data.loc[:,:"petal width (cm)"],  
                     data.target, # Fancy Indexing : data[data.columns[:-1]], data.[['target']]
                     cv=kf,       # cross validation, fold 수
                     n_jobs = -1) # 컴퓨터 성능 최대 활용
      cv_knn, cv_knn.mean(), cv_knn.std(), cv_knn.var(), cv_knn.std() / cv_knn.mean()

      from sklearn.model_selection import learning_curve # return : train_sizes_abs, train & test scores
      lc = learning_curve(KNeighborsClassifier(), data[data.columns[:-1]], data[['target']], cv=kf)
      from sklearn_evaluation import plot
      plt.figure(figsize=(8,5)); plot.learning_curve(lc[1], lc[2], lc[0])  # over-fitting 여부 파악
"""  # my.pkgCheatSheet.str_sklearn
# my.pkgCheatSheet.dct_sklearn = {
#    0 : my.pkgCheatSheet.str_sklearn[                                              :my.pkgCheatSheet.str_sklearn.index('▣ CH01.')],
#    1 : my.pkgCheatSheet.str_sklearn[my.pkgCheatSheet.str_sklearn.index('▣ CH01.'):my.pkgCheatSheet.str_sklearn.index('▣ CH02.')],
#    2 : my.pkgCheatSheet.str_sklearn[my.pkgCheatSheet.str_sklearn.index('▣ CH02.'):my.pkgCheatSheet.str_sklearn.index('▣ CH03.')],
#    3 : my.pkgCheatSheet.str_sklearn[my.pkgCheatSheet.str_sklearn.index('▣ CH03.'):my.pkgCheatSheet.str_sklearn.index('▣ CH04.')],
#    4 : my.pkgCheatSheet.str_sklearn[my.pkgCheatSheet.str_sklearn.index('▣ CH04.'):my.pkgCheatSheet.str_sklearn.index('▣ CH05.')],
#    5 : my.pkgCheatSheet.str_sklearn[my.pkgCheatSheet.str_sklearn.index('▣ CH05.'):my.pkgCheatSheet.str_sklearn.index('▣ CH06.')],
#    6 : my.pkgCheatSheet.str_sklearn[my.pkgCheatSheet.str_sklearn.index('▣ CH06.'):my.pkgCheatSheet.str_sklearn.index('▣ CH07.')],
#    7 : my.pkgCheatSheet.str_sklearn[my.pkgCheatSheet.str_sklearn.index('▣ CH07.'):-1] }

# my.pkgCheatSheet.dct_sklearn 초기화
my.pkgCheatSheet.dct_sklearn = dict()
_ = initCheatSheetDict('sklearn')

## ------------------------------------------------------------------------------------------- ## python > scikit-learn ↑, python > pycaret ↓

## ------------------------------------------------------------------------------------------- ## python > pycaret ↑, python > TF & keras ↓

## CheatSheet =================================================================================== End : python > TF & keras ↑ 
