* 자주 사용
  + MathJax : MathJax에서 유용한 TEX 명령어 <a href="https://www.onemathematicalcat.org/MathJaxDocumentation/MathJaxKorean/TeXSyntax_ko.html" target="_blank">KO</a>, <a href="https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm" target="_blank">EN</a> ; <a href="https://ko.wikipedia.org/wiki/위키백과:TeX_문법" target="_blank">위키백과:TeX_문법</a>
  + html ☞ https://blog.naver.com/lenj1/221854809536
    - 주석 : `<!-- 주석 문구 -->`
    - 요약 : `<details><summary>제목</summary><div markdown="3"> 한 행 띄고 내용 </div></details>`
    - hyper link ① 마크다운 일반 `[연결 설명](URL)` ② 별도 탭 `<a href="URL" target="_blank">연결 설명</a>`  
* 구글 코랩에서 구글 드라이브 연결  
  ① (연결을 원하는 구글 드라이브가 있는) 구글 계정에 로긴  
  ② Python code 실행 : <B>from google.colab import drive; drive.mount('/content/gdrive')</B> #, force_remount=True)  
  ③ 위 2의 코드 실행 결과 나타나는 URL 클릭  
  ④ (허용 버튼이 나타나면 허용 클릭하고) 나타나는 'authorization code' 복사  
  ⑤ 위 4에서 복사된 문자열을 위 2 실행 결과 나타나는 입력란에 붙여 넣기  
* Orange3 중심으로 Python 환경 구축
  + ⑴ openjdk 설치 [github](https://github.com/ojdkbuild/ojdkbuild) ( ☜ 참조 [Blog](https://blog.naver.com/vixlee/222285976728) ) 
    - JRE Zip file 내려받아 압축 풀고, %JAVA_HOME% "C:\Program Files\Java\jre-1.8.0.292" 설정함
    - %JAVA_HOME% 이하에 bin, legal, lib 폴더 위치함
  + ⑵ R 설치
    - jamovi를 활용하거나, R을 설치, 이후 %R_HOME% "C:\Program Files\R\R-4.0.4" 설정함
  + ⑶ [오렌지3](https://orangedatamining.com/) 3.28.0 Portable 내려받고 설치 및 실행 "C:\DS\Orange3-3.28.0>Scripts\\<B>orange-canvas</B>"
    - 참고
      - Orange3 [Homepage](https://orangedatamining.com/), [docs](https://orangedatamining.com/docs/), [pip](https://pypi.org/project/Orange3/), [YouTube Tutorial](https://www.youtube.com/watch?v=HXjnDIgGDuI&list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy)
      - Blog [AI오디세이](http://www.aio.world/news/articleView.html?idxno=258), [ML야학 소개](https://blog.naver.com/adler0912/222202689101) ☞ [ML야학](https://yah.ac/orange3) 및 [YouTube 목록](https://www.youtube.com/playlist?list=PLuHgQVnccGMAwnfp3Ml-XY1WNx1MPgrQ4)
    - 권장 설치 : Oragne3를 설치하면서 miniconda를 설치하고 env 생성 후 아래처럼 ③ pycaret[full],⑤ tensorflow 위주로 설치
    - Portable Orange3 설치 세부 사항(cf: Data 파일 위치 = C:\DS\Orange3-3.28.0\Lib\site-packages\Orange\datasets)
      - ① C:\DS\Orange3-3.28.0>python --version # Python 3.8.8 ; 이하 prompt "C:\DS\Orange3-3.28.0" 생략
      - ② prompt>python -m pip install --upgrade pip
      - ③ prompt>python -m pip install graphviz statsmodels sympy pycaret # https://pycaret.org/
        - prompt>python -m pip install catboost # pycaret 설치 시 graphviz 없다고 설치 안 됨
      - ④ prompt>python -m pip install rpy2
      - ⑤ prompt>python -m pip install tensorflow tensorflow-datasets tensorflow-lattice
      - ⑥ prompt>python -m pip install pydot pydotplus beautifulsoup4 db-sqlite3 sqlite-utils JPype1 mglearn bokeh plotnine tpot
      - ⑦ prompt>python -m pip install opencv-python opencv-contrib-python opencv-python-headless scikit-mdr scikit-image scikit-fuzzy tzlocal vpython
      - ⑧ prompt>python -m pip install hdbcli hana_ml
      - ⑨ prompt>pip install -U plaidml-keras plaidbench # https://github.com/plaidml/plaidml 참조, Visual C++ 2015 설치 필요
      - ⑩ prompt>Scripts\plaidml-setup # 이후 설정 사항 : ① Device Support : Y , ② 2 , ③ (저장) Y
      - ⑪ prompt>python -m pip install keras-tuner autokeras # https://github.com/keras-team/keras-tuner ; https://autokeras.com/install/
      - ⑫ prompt>python -m pip install Orange-Spectroscopy Orange3-**모듈명** # 모듈명 = Associate Bioinformatics Educational Explain Geo ImageAnalytics Network Prototypes Survival-Analysis Text Textable Timeseries

<details><summary>★★★책갈피★★★</summary><div markdown="3">
  
<font size=4>**소제목**</font>  

⏰ **여기서 잠깐** : 경고(Warning)가 나타납니다. 정상인가요?  

**【Note】** 넘파이 로그 함수는 np.log( )와 np.log10( )이 있습니다. 

⛱️ **확인 문제** : 과대적합과 과소적합에 대한 이해를 돕기 위해

📝 훈련 세트와 테스트 세트의 점수를 비교했을 때 훈련 세트가 너무 높으면 과대적합, 그 반대이거나 두 점수가 모두 낮으면 과소적합입니다.

+ 자주 사용되는 기능
  - my.printCheatSheet('sklearn', [0,None]) # 0:차례, 1:Data, 2:Model, 3:훈련, 4:예측, 5:평가, 6:개량, 7:기본 예시
  - Tex [MathJax](https://www.onemathematicalcat.org/MathJaxDocumentation/MathJaxKorean/TeXSyntax_ko.html), [koWiki](https://ko.wikipedia.org/wiki/위키백과:TeX_문법) ☞ MathJax에서 유용한 TEX 명령어 <a href="https://www.onemathematicalcat.org/MathJaxDocumentation/MathJaxKorean/TeXSyntax_ko.html" target="_blank">KO</a>, <a href="https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm" target="_blank">EN</a> ; <a href="https://ko.wikipedia.org/wiki/위키백과:TeX_문법" target="_blank">위키백과:TeX_문법</a>
+ CheatSheet, Usefule Blog, ... (cf: tensorflow privacy https://github.com/tensorflow/privacy )

|ⓟypi,ⓦiki|Python|numpy|scipy|sympy|matplotlib|pandas|sklearn|pycaret|Tensorflow|statsmodels|rpy2|sqlite|postgresql|re(gexp)|spacy|
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Homepage|[1](https://docs.python.org/3) [2](https://www.python.org/doc/) <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank">ⓦ</a>|[○](https://numpy.org/) [ⓦ](https://en.wikipedia.org/wiki/NumPy)|[○](https://scipy.org) [ⓦ](https://en.wikipedia.org/wiki/SciPy)|[○](https://www.sympy.org) [ⓦ](https://en.wikipedia.org/wiki/SymPy)|[○](https://matplotlib.org) [ⓦ](https://en.wikipedia.org/wiki/Matplotlib)|[○](https://pandas.pydata.org/) <a href="https://en.wikipedia.org/wiki/Pandas_(software)" target="_blank">ⓦ</a>|[○](https://www.sklearn.org) [ⓦ](https://en.wikipedia.org/wiki/Scikit-learn)|[○](https://pycaret.org),[ⓖ](https://github.com/pycaret/pycaret)|[ⓣ](https://www.tensorflow.org/) [ⓚ](https://keras.io) [ⓦ](https://en.wikipedia.org/wiki/TensorFlow)|[○](https://www.statsmodels.org) [ⓖ](https://github.com/statsmodels/statsmodels) [ⓟ](https://pypi.org/project/statsmodels)|[○](https://rpy2.github.io/)|[1](https://www.sqlite.org) [2](https://docs.python.org/3/library/sqlite3.html) [ⓦ](https://en.wikipedia.org/wiki/SQLite)|[○](https://www.postgresql.org) [○](https://www.psycopg.org) [ⓦ](https://en.wikipedia.org/wiki/PostgreSQL)|[○](https://docs.python.org/3/library/re.html) [○](https://pypi.org/project/regex) [ⓦ](https://en.wikipedia.org/wiki/Regular_expression)|[○](https://spacy.io/) [ⓟ](https://pypi.org/project/spacy/) [ⓦ](https://en.wikipedia.org/wiki/SpaCy)|
|Tutorial|[○](https://docs.python.org/3/tutorial/)|[○](https://numpy.org/doc/stable/user/tutorials_index.html)|[○](https://docs.scipy.org/doc/scipy/reference/tutorial)|[○](https://docs.sympy.org/latest/tutorial/index.html)|[○](https://matplotlib.org/stable/tutorials/index.html)|[○](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html)|[○](https://www.sklearn.org/tutorial/index.html) [map](https://www.sklearn.org/tutorial/machine_learning_map/index.html)|[○](https://pycaret.readthedocs.io/en/latest/tutorials.html)||[○](https://www.statsmodels.org/stable/user-guide.html)|[○](https://rpy2.github.io/doc/latest/html/introduction.html)|||[○](https://docs.python.org/3/howto/regex.html)|[○](https://spacy.io/usage/spacy-101)|
|(API)Ref.|[lib](https://docs.python.org/3/library) [ref](https://docs.python.org/3.9/reference)|[○](https://numpy.org/doc/stable/reference/)|[○](https://docs.scipy.org/doc/scipy/reference/)|[○](https://docs.sympy.org/latest/index.html)|[○](https://matplotlib.org/stable/contents.html)|[○](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)|[○](https://www.sklearn.org/modules/classes.html)|[○](https://pycaret.readthedocs.io/en/latest/api/classification.html)||[○](https://www.statsmodels.org/stable/api.html)|[○](https://rpy2.github.io/doc/latest/html/index.html)||||[○](https://spacy.io/api)|
|CheatSheet||[1](https://github.com/rougier/numpy-100) [2](https://www.kaggle.com/utsav15/100-numpy-exercises) [3](http://taewan.kim/post/numpy_cheat_sheet)||||[1](https://towardsdatascience.com/pandas-cheat-sheet-7e2ea6526be9) [2](https://www.dataquest.io/blog/pandas-cheat-sheet/) [3](https://www.educative.io/blog/python-pandas-tutorial) [4](https://github.com/corazzon/cracking-the-pandas-cheat-sheet)|[○](https://www.datacamp.com/community/blog/scikit-learn-cheat-sheet)|[Guide](https://pycaret.org/guide/)|||||||[①](https://www.datacamp.com/community/blog/spacy-cheatsheet)|
|Web Ref.|[①](https://www.tutorialspoint.com/python)|[①](https://www.tutorialspoint.com/numpy)|[①](https://www.tutorialspoint.com/scipy)|[①](https://www.tutorialspoint.com/sympy)|[1](https://www.tutorialspoint.com/matplotlib) [seaborn](https://www.tutorialspoint.com/seaborn)|[①](https://www.tutorialspoint.com/python_pandas)|[①](https://www.tutorialspoint.com/scikit_learn) [②](https://www.datacamp.com/community/tutorials/machine-learning-python)||[ⓣ](https://www.tutorialspoint.com/tensorflow) [ⓚ](https://www.tutorialspoint.com/keras) [ⓚ2](https://www.tutorialspoint.com/deep_learning_with_keras)|[통계](https://www.tutorialspoint.com/statistics) [patsy](https://github.com/pydata/patsy)||[1](https://www.sqlitetutorial.net/) [2](https://www.tutorialspoint.com/sqlite) [3](https://www.tutorialspoint.com/python_sqlite)|[①](https://www.postgresqltutorial.com/) [②](https://www.tutorialspoint.com/postgresql) [③](https://www.tutorialspoint.com/python_postgresql)|[①](https://regexone.com/)|[nltk](https://www.nltk.org) [nlp](https://www.tutorialspoint.com/natural_language_processing)|

ㅇ 마크다운 일반 사항   
  - https://ko.wikipedia.org/wiki/마크다운 및 [마크다운 문법](https://simhyejin.github.io/2016/06/30/Markdown-syntax/) 참조 
  - https://www.tablesgenerator.com/markdown_tables  
  - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet  
  
ㅇ 마크다운 수식 입력에 대한 참고 URL, [Local PC Daum Equation Editor](http://s1.daumcdn.net/editor/fp/service_nc/pencil/Pencil_chromestore.html)로 Chrome에서 입력함  
  - https://www.mathjax.org/  
  - https://en.wikibooks.org/wiki/LaTeX/Mathematics  
  - [MathJax basic tutorial and quick reference](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)  
  - [MathJax 연습 가능한 곳](http://jsbin.com/zimuxulawu/edit?html,output), [MathJax 코드 제안](http://detexify.kirelabs.org/classify.html)

ㅇ 키보드 특수문자
  - ㉮ ㉯ ㉰ ㉱ ㉲ ㉳ ㉴ ㉵ ㉶ ㉷ ㉸ ㉹ ㉺ ㉻ ㉠ ㉡ ㉢ ㉣ ㉤ ㉥ ㉦ ㉧ ㉨ ㉩ ㉪ ㉫ ㉬ ㉭ ─ ㆍ  
  - α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ    σ τ υ φ    χ ψ ω  
  - Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ    Σ Τ Υ Φ    Χ Ψ Ω  
  - ⓐlpha ⓑeta ⓖamma ⓓelta ⓔpsilon ⓩeta eta(≒i) THeta ⓘota ⓚappa ⓛambda ⓜu   
  - ⓝu ⓧi ⓞmicron ⓟi ⓡho ⓢigma ⓣau ⓤpsilon phi(≒f) CHi PSi ⓞmega  
  - ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ   
  - ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⅰ ⅱ ⅲ ⅳ ⅴ ⅵ ⅶ ⅷ ⅸ ⅹ Ⅰ Ⅱ Ⅲ Ⅳ Ⅴ Ⅵ Ⅶ Ⅷ Ⅸ Ⅹ   
 
  </div></details>
