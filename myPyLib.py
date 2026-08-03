# -*- coding: utf-8 -*-
"""
myPyLib.py : Enhanced Python Object Inspection Library
=======================================================
myLib.py 의 descobj / compobj 개선판.

개선 사항
---------
* print 출력 대신 pandas DataFrame 으로 결과 반환
* eval(문자열) 방식 → 객체 직접 전달 방식으로 변경 (모든 환경 호환)
* 인스턴스 스타일(ins.기능)과 클래스 스타일(ClsChk.기능) 모두 지원
* Jupyter Notebook, JupyterLab, IPython, 일반 스크립트, REPL 모두 동작

Usage
-----
    # 인스턴스 스타일 (ins.기능) ─────────────────────────────────────
    ins = ClsChk(my_obj)
    ins.mro()               # 상속 계층(MRO) DataFrame
    ins.desc()              # 속성/메서드 목록 DataFrame
    ins.comp(other_obj)     # 두 객체 속성 비교 DataFrame

    # 클래스 스타일 (ClsChk.기능) ───────────────────────────────────────
    ClsChk.mro_of(my_obj)
    ClsChk.desc_of(my_obj)
    ClsChk.comp_of(obj1, obj2)

    # 기존 함수 방식 (하위 호환) ─────────────────────────────────────
    mro_df, props_df = descobj(my_obj)
    comp_df          = compobj(obj1, obj2)
"""

import pandas as pd


# ======================================================================
#  ClsChk  ─  핵심 클래스
# ======================================================================

class ClsChk:
    """
    Python 객체/클래스 분석 도구.

    결과를 pandas DataFrame 으로 반환하므로
    Jupyter 에서는 표 형태로 렌더링되고,
    스크립트/REPL 에서도 DataFrame 으로 그대로 활용할 수 있습니다.
    """

    def __init__(self, obj):
        """
        Parameters
        ----------
        obj : any
            분석할 객체 또는 클래스.
        """
        self._obj = obj
        self._cls = obj if isinstance(obj, type) else type(obj)
        _kind     = "class" if isinstance(obj, type) else "instance of"
        self._label = f"{_kind} '{self._cls.__name__}'"

    # ------------------------------------------------------------------
    #  인스턴스 메서드  (ins.기능 스타일)
    # ------------------------------------------------------------------

    def mro(self) -> pd.DataFrame:
        """
        상속 계층(MRO: Method Resolution Order) 정보를 DataFrame 으로 반환.

        Returns
        -------
        pd.DataFrame
            columns : ClassName, Module
            index   : Order (0 = 자기 자신, 마지막 = object)
        """
        return ClsChk._mro_impl(self._obj)

    def desc(
        self,
        show_dunder: bool = True,
        show_private: bool = True,
    ) -> pd.DataFrame:
        """
        속성/메서드 목록을 DataFrame 으로 반환.

        Parameters
        ----------
        show_dunder  : bool
            ``__xxx__`` 형태의 dunder 속성 포함 여부 (기본 True).
        show_private : bool
            ``_xxx``  형태의 private 속성 포함 여부 (기본 True).

        Returns
        -------
        pd.DataFrame
            columns : Property, Category, Type, Callable
            index   : 1-based sequential number
        """
        return ClsChk._desc_impl(self._obj, show_dunder, show_private)

    def comp(self, other) -> pd.DataFrame:
        """
        다른 객체/클래스와 속성을 비교한 DataFrame 반환.

        Parameters
        ----------
        other : any
            비교 대상 객체 또는 클래스.

        Returns
        -------
        pd.DataFrame
            각 속성에 대해 두 객체의 존재 여부·타입·callable 여부 비교.
            index : Property 이름
        """
        return ClsChk._comp_impl(self._obj, other)

    # ------------------------------------------------------------------
    #  클래스 메서드  (ClsChk.기능 스타일)
    # ------------------------------------------------------------------

    @classmethod
    def mro_of(cls, obj) -> pd.DataFrame:
        """
        ``ClsChk.mro_of(obj)``  ─  상속 계층 DataFrame.

        Parameters
        ----------
        obj : any
            분석할 객체 또는 클래스.
        """
        return cls._mro_impl(obj)

    @classmethod
    def desc_of(
        cls,
        obj,
        show_dunder: bool = True,
        show_private: bool = True,
    ) -> pd.DataFrame:
        """
        ``ClsChk.desc_of(obj)``  ─  속성/메서드 목록 DataFrame.

        Parameters
        ----------
        obj          : any   분석할 객체 또는 클래스.
        show_dunder  : bool  dunder 속성 포함 여부 (기본 True).
        show_private : bool  private 속성 포함 여부 (기본 True).
        """
        return cls._desc_impl(obj, show_dunder, show_private)

    @classmethod
    def comp_of(cls, obj1, obj2) -> pd.DataFrame:
        """
        ``ClsChk.comp_of(obj1, obj2)``  ─  두 객체 비교 DataFrame.

        Parameters
        ----------
        obj1, obj2 : any   비교할 객체 또는 클래스.
        """
        return cls._comp_impl(obj1, obj2)

    # ------------------------------------------------------------------
    #  __repr__
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"ClsChk({self._label})"

    # ------------------------------------------------------------------
    #  내부 헬퍼  (Private)
    # ------------------------------------------------------------------

    @staticmethod
    def _safe_getattr(obj, name: str):
        """
        getattr 호출 중 발생하는 모든 예외를 처리.

        Returns
        -------
        (success: bool, value: any | error_msg: str)
        """
        try:
            return True, getattr(obj, name)
        except Exception as exc:
            return False, str(exc)

    @staticmethod
    def _attr_type_name(obj, name: str) -> str:
        """속성의 type 이름 반환. 접근 실패 시 'N/A'."""
        ok, val = ClsChk._safe_getattr(obj, name)
        return type(val).__name__ if ok else "N/A"

    @staticmethod
    def _attr_callable(obj, name: str):
        """속성이 callable 이면 True, 접근 실패 시 None."""
        ok, val = ClsChk._safe_getattr(obj, name)
        return callable(val) if ok else None

    @staticmethod
    def _categorize(name: str) -> str:
        """속성 이름으로 카테고리 분류: 'dunder' | 'private' | 'public'."""
        if name.startswith("__") and name.endswith("__"):
            return "dunder"
        if name.startswith("_"):
            return "private"
        return "public"

    @staticmethod
    def _obj_label(obj) -> str:
        """비교 시 컬럼 이름에 쓸 간단한 레이블."""
        return obj.__name__ if isinstance(obj, type) else type(obj).__name__

    # ------------------------------------------------------------------

    @staticmethod
    def _mro_impl(obj) -> pd.DataFrame:
        cls = obj if isinstance(obj, type) else type(obj)
        records = [
            {
                "Order":     i,
                "ClassName": c.__name__,
                "Module":    getattr(c, "__module__", "?"),
            }
            for i, c in enumerate(cls.__mro__)
        ]
        df = pd.DataFrame(records)
        df = df.set_index("Order")
        return df

    @staticmethod
    def _desc_impl(obj, show_dunder: bool, show_private: bool) -> pd.DataFrame:
        records = []
        for name in sorted(dir(obj)):
            cat = ClsChk._categorize(name)
            if not show_dunder and cat == "dunder":
                continue
            if not show_private and cat == "private":
                continue

            ok, val = ClsChk._safe_getattr(obj, name)
            if ok:
                type_name  = type(val).__name__
                is_callable = callable(val)
            else:
                type_name  = "N/A"
                is_callable = None          # 접근 불가 → 판단 불가

            records.append(
                {
                    "Property": name,
                    "Category": cat,
                    "Type":     type_name,
                    "Callable": is_callable,
                }
            )

        df = pd.DataFrame(records)
        if df.empty:
            return df

        # 1-based 순번 인덱스
        df.index       = range(1, len(df) + 1)
        df.index.name  = "#"
        return df

    @staticmethod
    def _comp_impl(obj1, obj2) -> pd.DataFrame:
        # 컬럼 레이블: 같은 타입이면 (obj1)/(obj2) 접미사 추가
        lbl1 = ClsChk._obj_label(obj1)
        lbl2 = ClsChk._obj_label(obj2)
        if lbl1 == lbl2:
            lbl1, lbl2 = lbl1 + " (obj1)", lbl2 + " (obj2)"

        props1    = set(dir(obj1))
        props2    = set(dir(obj2))
        all_props = sorted(props1 | props2)

        records = []
        for name in all_props:
            in1 = name in props1
            in2 = name in props2

            type1  = ClsChk._attr_type_name(obj1, name) if in1 else "-"
            type2  = ClsChk._attr_type_name(obj2, name) if in2 else "-"
            call1  = ClsChk._attr_callable(obj1, name)  if in1 else "-"
            call2  = ClsChk._attr_callable(obj2, name)  if in2 else "-"

            in_both    = in1 and in2
            same_type  = (type1 == type2) if in_both else "-"
            exclusive  = "-" if in_both else (lbl1 if in1 else lbl2)

            records.append(
                {
                    "Property":              name,
                    "Category":              ClsChk._categorize(name),
                    f"In {lbl1}":            "✓" if in1 else "✗",
                    f"Type ({lbl1})":        type1,
                    f"Callable ({lbl1})":    call1,
                    f"In {lbl2}":            "✓" if in2 else "✗",
                    f"Type ({lbl2})":        type2,
                    f"Callable ({lbl2})":    call2,
                    "SameType":              same_type,
                    "Exclusive":             exclusive,
                }
            )

        df = pd.DataFrame(records)
        if df.empty:
            return df
        return df.set_index("Property")


# ======================================================================
#  하위 호환 래퍼 함수  (기존 myLib 스타일)
# ======================================================================

def descobj(obj, show_dunder: bool = True, show_private: bool = True):
    """
    기존 ``myLib.descobj`` 개선판.

    차이점
    ------
    * 인수: 문자열 대신 **객체 직접 전달**
    * 출력: print 대신 **(mro_df, props_df) 튜플 반환**

    Parameters
    ----------
    obj          : any   분석할 객체 또는 클래스
    show_dunder  : bool  dunder 속성 포함 여부 (기본 True)
    show_private : bool  private 속성 포함 여부 (기본 True)

    Returns
    -------
    mro_df   : pd.DataFrame  상속 계층(MRO)
    props_df : pd.DataFrame  속성/메서드 목록

    Examples
    --------
    >>> mro_df, props_df = descobj(pd.DataFrame())
    >>> mro_df
    >>> props_df[props_df['Category'] == 'public']
    """
    ins = ClsChk(obj)
    return ins.mro(), ins.desc(show_dunder, show_private)


def compobj(obj1, obj2) -> pd.DataFrame:
    """
    기존 ``myLib.compobj`` 개선판.

    차이점
    ------
    * 인수: 문자열 대신 **객체 직접 전달**
    * 출력: print 대신 **pd.DataFrame 반환**

    Parameters
    ----------
    obj1, obj2 : any   비교할 객체 또는 클래스

    Returns
    -------
    pd.DataFrame  두 객체의 속성 비교표
                  (index = Property 이름)

    Examples
    --------
    >>> comp_df = compobj(pd.DataFrame(), pd.Series(dtype=float))
    >>> comp_df[comp_df['Exclusive'] != '-']   # 한쪽에만 있는 속성
    >>> comp_df[comp_df['SameType'] == False]  # 타입이 다른 공통 속성
    """
    return ClsChk.comp_of(obj1, obj2)


# ======================================================================
#  help()  ─  사용법 안내
# ======================================================================

# Markdown 버전 (Jupyter 용)
_HELP_MD = """\
## myPyLib  —  사용법 안내

> `import myPyLib as my` 후 아래 방식으로 사용합니다.

---

### 이름 대응표

| myLib.py (기존) | myPyLib.py — 함수 방식 | myPyLib.py — 인스턴스 방식 | myPyLib.py — 클래스 방식 |
|---|---|---|---|
| `descobj('df')` | `my.descobj(df)` | `my.ClsChk(df).mro()` + `.desc()` | `my.ClsChk.desc_of(df)` |
| `compobj('df','s')` | `my.compobj(df, s)` | `my.ClsChk(df).comp(s)` | `my.ClsChk.comp_of(df, s)` |

---

### 사용 예시

#### ① 함수 방식 (기존과 가장 유사)
```python
import myPyLib as my
import pandas as pd

df = pd.DataFrame({'a': [1,2], 'b': [3,4]})
s  = pd.Series([1, 2, 3], dtype=float)

# descobj → (mro_df, props_df) 튜플 반환
mro_df, props_df = my.descobj(df)
mro_df                                               # 상속 계층
props_df[props_df['Category'] == 'public']           # public 속성만
props_df[props_df['Callable'] == True]               # 메서드만

# compobj → pd.DataFrame 반환
comp_df = my.compobj(df, s)
comp_df[comp_df['Exclusive'] != '-']                 # 한쪽에만 있는 속성
comp_df[comp_df['SameType'] == False]                # 타입이 다른 공통 속성
comp_df[comp_df['Category'] == 'public']             # public 속성 비교
```

#### ② 인스턴스 방식 (ins.기능)
```python
ins = my.ClsChk(df)                 # 객체 1회 지정

ins.mro()                        # 상속 계층 DataFrame
ins.desc()                       # 전체 속성 목록 DataFrame
ins.desc(show_dunder=False)      # dunder(__xx__) 제외
ins.desc(show_private=False)     # private(_xx)  제외
ins.comp(s)                      # s 와 비교 DataFrame
```

#### ③ 클래스 방식 (ClsChk.기능)
```python
my.ClsChk.mro_of(df)
my.ClsChk.desc_of(df, show_dunder=False)
my.ClsChk.comp_of(df, s)
```

---

### desc() / comp() 반환 DataFrame 구조

| 메서드 | index | columns |
|---|---|---|
| `mro()` | Order (0=자기자신) | `ClassName`, `Module` |
| `desc()` | # (1부터) | `Property`, `Category`, `Type`, `Callable` |
| `comp()` | Property 이름 | `Category`, `In X`, `Type(X)`, `Callable(X)`, `In Y`, `Type(Y)`, `Callable(Y)`, `SameType`, `Exclusive` |

> **Category 값** : `public` / `private` (`_xxx`) / `dunder` (`__xxx__`)
"""

# 텍스트 버전 (일반 스크립트/REPL 용)
_HELP_PLAIN = """
╔══════════════════════════════════════════════════════════════════╗
║              myPyLib  —  사용법 안내                             ║
║         import myPyLib as my  후 사용                            ║
╚══════════════════════════════════════════════════════════════════╝

■ 이름 대응표
  기존 myLib.py          myPyLib.py (함수)      인스턴스 / 클래스 방식
  ─────────────────────  ─────────────────────  ────────────────────────────────
  descobj('df')          my.descobj(df)         my.ClsChk(df).mro() + .desc()
  compobj('df','s')      my.compobj(df, s)      my.ClsChk(df).comp(s)

■ ① 함수 방식 (기존과 가장 유사)
  mro_df, props_df = my.descobj(df)
  props_df[props_df['Category'] == 'public']    # public 속성만
  props_df[props_df['Callable'] == True]        # 메서드만

  comp_df = my.compobj(df, s)
  comp_df[comp_df['Exclusive'] != '-']          # 한쪽에만 있는 속성
  comp_df[comp_df['SameType'] == False]         # 타입이 다른 공통 속성

■ ② 인스턴스 방식 (ins.기능)
  ins = my.ClsChk(df)
  ins.mro()
  ins.desc()
  ins.desc(show_dunder=False)
  ins.desc(show_private=False)
  ins.comp(s)

■ ③ 클래스 방식 (ClsChk.기능)
  my.ClsChk.mro_of(df)
  my.ClsChk.desc_of(df, show_dunder=False)
  my.ClsChk.comp_of(df, s)

■ 반환 DataFrame 구조
  mro()   index=Order,    columns=[ClassName, Module]
  desc()  index=#(1부터), columns=[Property, Category, Type, Callable]
  comp()  index=Property, columns=[Category, In X, Type(X), Callable(X),
                                    In Y, Type(Y), Callable(Y), SameType, Exclusive]

  Category 값: public / private(_xxx) / dunder(__xxx__)
"""


def _in_ipython() -> bool:
    """실제로 IPython / Jupyter 셸 안에서 실행 중인지 확인."""
    try:
        from IPython import get_ipython
        return get_ipython() is not None
    except ImportError:
        return False


def help():
    """
    myPyLib 사용법을 출력합니다.

    Jupyter / IPython 환경에서는 Markdown 표로,
    일반 스크립트 / REPL 에서는 텍스트로 출력됩니다.

    Examples
    --------
    >>> import myPyLib as my
    >>> my.help()
    """
    if _in_ipython():
        from IPython.display import display, Markdown
        display(Markdown(_HELP_MD))
    else:
        print(_HELP_PLAIN)
