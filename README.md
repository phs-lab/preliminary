<details><summary>Prompt Template</summary><div markdown="3"> <!-- https://https://naver.me/G3PQfKXA "이석현, 2025, 일잘러의 챗GPT 프롬프트 74가지" -->

<pre># 프롬프트 이력
【프롬프트 이력 : 2025-11-21 (금) 20:50:37】

# 질문 내용

# 답변 지침
  o 대화 상대로서 나는 당신을 CoPilot으로, 당신은 나를 Pilot으로 지칭한다.
  o 위 질문(들)에 대한 답변  내용은 가급적 표(Table)로 제시하면 좋다. 
  o 표를 포함한 내용에는 HTML이나 마크다운 예약어(예: '<br />', '**' 등)가 보이면 안된다. 
  o 답변이 중도에 끊어지는 경우를 인지하기 위해, 답변이 정상적으로 완료된 경우 
     답변의 제일 아래에 질문의 '프롬프트 이력' 정보를 그대로 재활용하여 답변의 정상 완료 여부를 명시한다.
     - 예: 질문에서 '프롬프트 이력 : 2025-10-15 (수) 16:26:05'으로 지정된 경우, 
          정상 답변 완료 시 '【`프롬프트 이력 : 2025-10-15 (수) 16:26:05`의 답변 정상 완료】'로 명시.
  o 질문에 '프롬프트 이력' 정보가 없는 경우 '【답변 정상 완료】'로 명시한다.
  o 근거에 의한 주장, 정보 및 수치를 제시하는 경우에는 다음 단계로 검증하여 제시해야 한다: 
    1. 먼저 제공된 CONTEXT에서만 답변.
    2. 해당 정보가 있다면 인용 시 정확한 참조 URL, INDEX 번호 및 인용된 원문 위치를 hyperlink로 제시.
    3. 해당 정보가 없다면 '정보 없음'이라고 명시.
    4. 추측이나 일반적인 지식은 답변에 포함하지 말고 근거에 기반하여 답변의 논리 구성.
    5. IT 시스템 내의 구성 항목에 대한 답변의 경우 실제 시스템에서 검증 가능한 내용만 제시.
      - 예: SAP Function에 대한 답변인 경우, 기능 화면 'SE37'에서 조회 가능함을 검증 후 제시.

////////////////////////////////////////// Tip //////////////////////////////////////////
o 일반적으로는 질문이나 답변을 5W1H(Who, Whom, What/Which, How-to, How many/much/extent, Where, When, Why)로 하는 것이 좋다.
  (다음은 "SAP Design Studio"에 대해 문의하는 Prompt의 사례)
* (한마디로 설명한다면) 『SAP Design Studio』(이)란 무엇인가?
* 어떻게 구성되어 있나?
  + 하위 Component들이 있다면 무엇들인가? 
  + 각각의 관계는 어떻게 되나?
    - 구조(포함(ERD Parent/Child),부분/전체,계층), 
    - 시간(동시, 선후, 주기), 
    - 논리(대립, 모순, 함의, 인과(원인/결과, 조건/결과, 필요/충분/필요충분)), 
    - 기능/상호작용(상관, 상호작용, Feedback)
    - 기타
  + 각각의 순서는 어떻게 되나? 순서 부여 기준은?
* 어떤 조건(예: License, 권한, 자료·문서 수령 등을 득한 후에) 하에 
* 누가, 누구를 위해, 무엇을, 어떻게(어떤 방식이나 절차로, 만약 해당된다면, 어떤 비용/Resource를 대가로), 얼마나(어느 정도로), 어떤 (수행) 환경에서, 어떤 시점에, 왜 하는 것인가?</pre>
* LLM(Large Language Model) Chatbot Service
  - https://gemini.google.com ; https://notebooklm.google
* 참조 : https://naver.me/G3PQfKXA - 이석현 지음, 제이펍 · 2025-10-23, 일잘러의 챗GPT 프롬프트 74가지
  - [Prompt Engineering Guide](https://www.promptingguide.ai)
  - Google [프롬프트 엔지니어링: 개요 및 가이드](https://cloud.google.com/discover/what-is-prompt-engineering), [6 Tips, 2023-08-15](https://cloud.google.com/blog/products/application-development/five-best-practices-for-prompt-engineering "Tips to enhance your prompt-engineering abilities"), [Prompting Guide 101 PDF File](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf "https://workspace.google.com/learning/content/gemini-prompt-guide"), [Gemini API 프롬프트 설계 전략](https://ai.google.dev/gemini-api/docs/prompting-strategies)
  - https://github.blog/developer-skills/github/how-to-write-better-prompts-for-github-copilot 
  - https://docs.github.com/en/copilot/get-started/best-practices 
</div></details>

* Temporary Memo
  + Excel <a href="https://support.microsoft.com/en-us/office/keyboard-shortcuts-in-excel-1798d9d5-842a-42b8-9c99-9b7213f0040f" target="_blank">단축키</a>
  + SAP AG
    - TechEd
    - Developers<sup><a href="https://www.youtube.com/@sapdevs" target="_blank">YouTube Home</a></sup>
      - 2022.05.13, Back to basics: <a href="https://www.youtube.com/watch?v=O3OU2rSUqs0&list=PL6RpkC85SLQDYLiN1BobWXvvnhaGErkwj" target="_blank">OData</a><SUP><a href="https://github.com/SAP-samples/odata-basics-handsonsapdev" target="_blank">Github</a>, <a href="https://www.youtube.com/watch?v=O3OU2rSUqs0" target="_blank">1. Intro</a>, <a href="https://www.youtube.com/watch?v=f9w61GxMztY" target="_blank">2. Basic Operations</a>, <a href="https://www.youtube.com/watch?v=Bln2A0_OauY" target="_blank">3. System Query Options</a>, <a href="https://www.youtube.com/watch?v=R9JyaPYtWKs" target="_blank">4. $filter</a>, <a href="https://www.youtube.com/watch?v=tmwglig2mbw" target="_blank">5. Actions & Functions</a>, <a href="https://www.youtube.com/watch?v=PhA_VS4-lUw" target="_blank">6. Wrap-up</a></SUP>
      - 2019.01, SAP HANA Basics For Developers<sup><a href="https://www.youtube.com/watch?v=ljdvqRtSHd4&list=PL6RpkC85SLQAPHYG1x6IEu_exE5pa0UK_" target="_blank">URL</a></sup>
      - 2019, ABAP Object Oriented Concepts<sup><a href="https://www.youtube.com/watch?v=GUh7QyCwxGk&list=PL6RpkC85SLQCGjMBsoQYlMrLmbZaEWM6U" target="_blank">URL</a>, <a href="https://github.com/SAP-samples/abap-oo-basics" target="_blank">Github</a></sup>
  + SAP ABAP COMPLETE TUTORIAL by Alpha Tutorials - Finance
    - SAP ABBP TRAINING COURSE - Part 1<sup><a href="https://www.youtube.com/watch?v=SmVcwjLtM0s&t=21s" target="_blank">URL</a></sup>, Part 2<sup><a href="https://www.youtube.com/watch?v=-_7rZKGdxwQ" target="_blank">URL</a></sup>
    - SAP Debugging Tutorial for Functional Consultants<sup><a href="https://www.youtube.com/watch?v=lNHOKNgmGiw" target="_blank">URL</a></sup>
    - SAP MM Training PART 1<sup><a href="https://www.youtube.com/watch?v=zqgL9v6rCy4" target="_blank">URL</a></sup>, Part 2<sup><a href="https://www.youtube.com/watch?v=8W2_noRSs2E" target="_blank">URL</a></sup>, Part 3<sup><a href="https://www.youtube.com/watch?v=MyGLdRB-uMw" target="_blank">URL</a></sup>
    - SAP SD Interview Question & Answers<sup><a href="https://www.youtube.com/watch?v=8Ap76UsHbow" target="_blank">URL</a></sup>
  + SAP Yard (or ZAP Yard)
    - SAP ABAP 7.40<sup>URL <a href="https://www.youtube.com/watch?v=FvbBpxufBjU&list=PLQHTTlL0gF_cf47ovXvoXC114ImJkLfH5" target="_blank">Ver 1</a>, <a href="https://www.youtube.com/watch?v=hAVNAFtf6rQ&list=PLQHTTlL0gF_dz94aMvENrgj5uqCBEYKeZ" target="_blank">Ver 2</a>, <a href="https://www.youtube.com/watch?v=PkOdOd6t54w&list=PLQHTTlL0gF_f33SIxVwEt9qn9gOR9N8eN" target="_blank">Ver 3</a></sup>, Debugging<sup><a href="https://www.youtube.com/watch?v=9ViRrBSz9gA&list=PLQHTTlL0gF_ed1FdjApXmf7d1v5hCp4_b" target="_blank">URL</a></sup>, 7.4 Inline Declaration<sup><a href="https://www.youtube.com/watch?v=o2-TTx_YWN0&list=PLQHTTlL0gF_cLJpedzhRFVjSShPZSLalg" target="_blank">URL</a></sup>, ADBC<sup><a href="https://www.youtube.com/watch?v=dnr-Dj1rLEw&list=PLQHTTlL0gF_fOBe6vpOSoRsiVCGSyr73k" target="_blank">URL</a></sup>, ABAP for Fiori<sup><a href="https://www.youtube.com/watch?v=M3BAgWyGkUY&list=PLQHTTlL0gF_ceG4UKxb0FXUfIKZuWDqaQ" target="_blank">URL</a></sup>
    - SAP HANA DB<sup><a href="https://www.youtube.com/watch?v=hO26ZgQQxhc&list=PLQHTTlL0gF_cIWPw77I4nZ7mPWzZjU9Cr" target="_blank">URL</a></sup>
  , Netweaver Gateway & OData<sup><a href="https://www.youtube.com/watch?v=vpRYQV1sZR4&list=PLQHTTlL0gF_d86LX5xbGj4jqUAIT7nsPr" target="_blank">URL</a></sup>
  , HANA Models<sup><a href="https://www.youtube.com/watch?v=-QXYMgbtJEg&list=PLQHTTlL0gF_eJQfIuYp1pYAXgIVbOElh8" target="_blank">URL</a></sup>
  , HANA View Proxy<sup><a href="https://www.youtube.com/watch?v=w0APQ5xlk28&list=PLQHTTlL0gF_dBtZohIeUx0_BpcIRgbOxY" target="_blank">URL</a></sup>
    - ABAP CDS<sup><a href="https://www.youtube.com/watch?v=OnItCMTPpMw&list=PLQHTTlL0gF_dqEDJ3wjDDik-WyaTOpCTo" target="_blank">Access Control</a>, <a href="https://www.youtube.com/watch?v=q7bep8j6pCM&list=PLQHTTlL0gF_eGsBAWidhKIzf4Tw6MhBJQ" target="_blank">with Parameters</a>, <a href="https://www.youtube.com/watch?v=wpZ-DFf2MJw&list=PLQHTTlL0gF_fOJTY78a-TDeAGEgqQpx_O" target="_blank">Associations</a>, <a href="https://www.youtube.com/watch?v=714gRY-ktT0&list=PLQHTTlL0gF_e8knLSv3jDfotxHj26zhVu" target="_blank">Fiori Elements</a></sup>
  + 캘거리 SAP 아저씨 : SAP FICO Overview <a href="https://www.youtube.com/watch?v=l3V7wsgOX_A" target="_blank">Part 1</a>, <a href="https://www.youtube.com/watch?v=BOhr--BquAc" target="_blank">Part 2</a>, <a href="https://www.youtube.com/watch?v=V-hic8mZxS8" target="_blank">Part 3</a>, <a href="https://www.youtube.com/watch?v=1wg2prl-_kI" target="_blank">Part 3 Demo</a>, <a href="https://www.youtube.com/watch?v=F2N-2tIQ_Tw" target="_blank">Part 4</a>
* CheatSheets
  + Python 일반 <!--  <sup><a href="" target="_blank">URL</a></sup>                       <a href="" target="_blank">URL</a> -->
    - DataCamp : CheatSheets<sup><a href="https://www.datacamp.com/cheat-sheet/category/python" target="_blank">URL</a></sup>, Tutorials<sup><a href="https://www.datacamp.com/tutorial/category/python" target="_blank">URL</a></sup> 
      - for Beginners<sup><a href="https://www.datacamp.com/cheat-sheet/getting-started-with-python-cheat-sheet" target="_blank">URL</a></sup>, for Beginners in Data Science<sup><a href="https://www.datacamp.com/cheat-sheet/python-for-data-science-a-cheat-sheet-for-beginners" target="_blank">URL</a></sup>, Dates & Times<sup><a href="https://www.datacamp.com/cheat-sheet/working-with-dates-and-times-in-python-cheat-sheet" target="_blank">URL</a></sup>
      - Jupyter Notebook<sup><a href="https://www.datacamp.com/cheat-sheet/jupyter-notebook-cheat-sheet" target="_blank">URL</a></sup> 
    - Python Cheatsheet<sup><a href="https://www.pythoncheatsheet.org" target="_blank">URL</a></sup>, Based on the book <a href="https://automatetheboringstuff.com" target="_blank">Automate the Boring Stuff with Python</a> and many other sources.
    - Comprehensive Python Cheatsheet<sup><a href="https://github.com/gto76/python-cheatsheet/blob/main/README.md" target="_blank">URL</a></sup>
  + Math : Numpy<sup><a href="https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python" target="_blank">Data Analysis</a></sup>, SciPy<sup><a href="https://www.datacamp.com/cheat-sheet/scipy-cheat-sheet-linear-algebra-in-python" target="_blank">Linear Algebra</a></sup>
  + EDA : Data Import & Export<sup><a href="https://www.datacamp.com/cheat-sheet/importing-data-in-python-cheat-sheet" target="_blank" title="importing your data, from flat files to files native to other software and relational databases">URL</a></sup>, Pandas<sup><a href="https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python" target="_blank" title="Basics for Data Science">Basics</a>, <a href="https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-data-wrangling-in-python" target="_blank">Data Wrangling</a></sup>, SQL<sup><a href="https://www.datacamp.com/cheat-sheet/sql-basics-cheat-sheet" target="_blank">Basics</a>, <a href="https://www.datacamp.com/cheat-sheet/sql-joins-cheat-sheet" target="_blank">Joins</a>, <a href="https://www.datacamp.com/cheat-sheet/sql-window-functions-cheat-sheet" target="_blank">Window Functions</a></sup> 
  + Visualization : Matplotlib<sup><a href="https://www.datacamp.com/cheat-sheet/matplotlib-cheat-sheet-plotting-in-python" target="_blank">URL</a></sup>, Seaborn<sup><a href="https://www.datacamp.com/cheat-sheet/python-seaborn-cheat-sheet" target="_blank">URL</a></sup>, Bokeh<sup><a href="https://www.datacamp.com/cheat-sheet/python-data-visualization-bokeh-cheat-sheet" target="_blank">URL</a></sup>, Plotly Express<sup><a href="https://www.datacamp.com/cheat-sheet/category/python" target="_blank">URL</a></sup> 
  + Text : Text Data<sup><a href="https://www.datacamp.com/cheat-sheet/text-data-in-python-cheat-sheet" target="_blank">URL</a></sup>, Regular Expressions<sup><a href="https://www.datacamp.com/cheat-sheet/regular-expresso" target="_blank">URL</a></sup>, spaCy<sup><a href="https://www.datacamp.com/cheat-sheet/spacy-cheat-sheet-advanced-nlp-in-python" target="_blank">URL</a></sup> &nbsp; ☞ Blog Article : GPT<sup><a href="https://www.datacamp.com/blog/a-beginners-guide-to-gpt-3" target="_blank" title="A Beginner's Guide to GPT-3 written by Mr. Shubham Saboo and Ms. Sandra Kublik">May 18, 2022</a>, <a href="https://www.datacamp.com/blog/what-we-know-gpt4" target="_blank" title="Everything We Know About GPT-4 written by Mr. Abid Ali Awan">October 14, 2022</a></sup>
  + ML, DL : Scikit-Learn<sup><a href="https://www.datacamp.com/cheat-sheet/scikit-learn-cheat-sheet-python-machine-learning" target="_blank">URL</a></sup>, Keras<sup><a href="https://www.datacamp.com/cheat-sheet/keras-cheat-sheet-neural-networks-in-python" target="_blank">URL</a></sup> 
  + Others : PySpark<sup><a href="https://www.datacamp.com/cheat-sheet/pyspark-cheat-sheet-spark-in-python" target="_blank">Basics</a>, <a href="https://www.datacamp.com/cheat-sheet/pyspark-cheat-sheet-spark-dataframes-in-python" target="_blank">DataFrame</a></sup>
* 자주 사용
  + MathJax : MathJax에서 유용한 TEX 명령어 <a href="https://www.onemathematicalcat.org/MathJaxDocumentation/MathJaxKorean/TeXSyntax_ko.html" target="_blank">KO</a>, <a href="https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm" target="_blank">EN</a> ; <a href="https://ko.wikipedia.org/wiki/위키백과:TeX_문법" target="_blank">위키백과:TeX_문법</a>
  + html ☞ https://blog.naver.com/lenj1/221854809536
    - 주석 : `<!-- 주석 문구 -->`
    - 요약 : `<details><summary>제목</summary><div markdown="3"> 한 행 띄고 내용 </div></details>`  
      &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ☞ 참고 [1](https://blog.kalkin7.com/2014/02/05/wordpress-markdown-quick-reference-for-koreans/) [2](https://css-tricks.com/little-stuff-markdown-always-forget-google/) : `div는 안 써도 될 듯` → 간략형 : `<details><summary>제목</summary> 한 행 띄고 내용 </details>`
    - hyper link ① 마크다운 일반 `[연결 설명](URL)` ② 별도 탭 `<a href="URL" target="_blank">연결 설명</a>`  
* 구글 코랩에서 구글 드라이브 연결  
  ① (연결을 원하는 구글 드라이브가 있는) 구글 계정에 로긴  
  ② Python code 실행 : <B>from google.colab import drive; drive.mount('/content/gdrive')</B> #, force_remount=True)  
  ③ 위 2의 코드 실행 결과 나타나는 URL 클릭  
  ④ (허용 버튼이 나타나면 허용 클릭하고) 나타나는 'authorization code' 복사  
  ⑤ 위 4에서 복사된 문자열을 위 2 실행 결과 나타나는 입력란에 붙여 넣기  
* 코랩 연동  
  + https://colab.research.google.com/github/ +  phs-lab/이하_주소  
  + colab 사용법, github 연동 조사  
    - colab 사용법 일반  
      https://theorydb.github.io/dev/2019/08/23/dev-ml-colab/  
      https://zzsza.github.io/data/2018/08/30/google-colab/  
    - Google Colab 초기 세팅 : 구글드라이브와 연동하는 법, 깃 클론하는 법  
      https://mylifemystudy.tistory.com/70  
      https://tykimos.github.io/2019/01/22/colab_getting_started/  
    - colab 사용법 ★  
      사용법1 : https://blog.naver.com/beyondlegend/221612116017  
      사용법2 : https://blog.naver.com/beyondlegend/221633263276  
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

|T-Code|Action|Dir. 1|Dir. 2|MvT|SSI|비고, SSI Possible Entries|
|:--:|:--|:--|:--|:--:|:--:|:--|
|MB1A|소비(Q)|To|From|||MB11 = MB1A + MB1B + MB1C|
|MB1A|소비(Q)|코스트센터(T)  |출고 창고(F)  |201||MIGO_GI|
|MB1A|소비(Q)|코스트센터(T)  |위탁점포(R)  |201|K|▣ Special Stock Indicators(Table: T148):|
|MB1A|소비(Q)|코스트센터(T)  |파이프라인(I)|201|K|B : 고객 재고 - Customer Stock|
|MB1A|소비(Q)|프로젝트(P)  |출고 창고(F)  |221||C : SC 고객 재고 - SC Customer Stock|
|MB1A|소비(Q)|프로젝트(P)  |위탁점포(R)  |221|K|E : 미결 오더 - Orders on Hand|
|MB1A|소비(Q)|프로젝트(P)  |프로젝트(P)  |221|Q|F : SC 고객 주문 재고 - SCCustomerOrderStock|
|MB1A|소비(Q)|판매오더(S)  |출고 창고(F)  |231||I : SC RTP - SC RTP|
|MB1A|소비(Q)|판매오더(S)  |위탁점포(R)  |231|K|J : SC 공급업체 위탁품 - SC Vendor consignmnt|
|MB1A|소비(Q)|판매오더(S)  |판매오더재고|231|E|K : 공급업체 위탁 - Supplier Consignment|
|MB1A|소비(Q)|판매오더(S)  |프로젝트(P)  |231|Q|M : 공급업체반환용포장재 - Ret.trans.pkg vendor|
|MB1A|소비(Q)|자산(E)  |출고 창고(F)  |241||O : 외주 재고 - Subcontracting Stock|
|MB1A|소비(Q)|자산(E)  |위탁점포(R)  |241|K|P : 파이프라인 자재 - Pipeline material|
|MB1A|소비(Q)|영업(V)  |출고 창고(F)  |251||Q : 프로젝트 재고 - Project Stock|
|MB1A|소비(Q)|영업(V)  |위탁점포(R)  |251|K|R : SC 프로젝트 재고 - SC Project Stock|
|MB1A|소비(Q)|오더(R)  |출고 창고(F)  |261||T : 운송 중 재고 - Stock in Transit|
|MB1A|소비(Q)|오더(R)  |위탁점포(R)  |261|K|V : 고객 반환용포장재 - Ret. pkg w. customer|
|MB1A|소비(Q)|오더(R)  |판매오더재고(A)  |261|E|W : 고객 위탁 - Customer Consignment|
|MB1A|소비(Q)|오더(R)  |프로젝트(P)  |261|Q|Y : 출하단위 (창고) - Shipping unit (warehouse)|
|MB1A|소비(Q)|오더(R)  |파이프라인(I)  |261|P||
|MB1A|소비(Q)|오더(R)  |고객위탁(U)|261|W||
|MB1A|소비(Q)|네트워크(N)  |출고 창고(A)  |281|||
|MB1A|소비(Q)|네트워크(N)  |위탁점포(F)  |281|K||
|MB1A|소비(Q)|네트워크(N)  |판매오더재고(S)  |281|E||
|MB1A|소비(Q)|네트워크(N)  |프로젝트재고(R)  |281|Q||
|MB1A|소비(Q)|네트워크(N)  |파이프라인(E)  |281|P||
|MB1A|소비(Q)|모든 계정 지정(C)|출고 창고(F)  |271|||
|MB1A|소비(Q)|모든 계정 지정(C)|위탁점포(R)  |271|K||
|MB1A|소비(Q)|모든 계정 지정(C)|판매오더재고(A)  |271|E||
|MB1A|소비(Q)|모든 계정 지정(C)|프로젝트(P)  |271|Q||
|MB1A|소비(Q)|모든 계정 지정(C)|파이프라인(O)  |271|P||
|MB1A|검사표본(C)|From|To||||
|MB1A|검사표본(C)|창고재고(F)  |사용가능 재고(U)  |333|||
|MB1A|검사표본(C)|창고재고(F)  |품질 검사(Q)  |331|||
|MB1A|검사표본(C)|창고재고(F)  |보류 재고(B)|335|||
|MB1A|검사표본(C)|위탁재고(R)  |사용가능 재고(U)  |333|K||
|MB1A|검사표본(C)|위탁재고(R)  |품질 검사(Q)  |331|K||
|MB1A|검사표본(C)|위탁재고(R)  |보류 재고(B)|335|K||
|MB1A|검사표본(C)|판매오더 재고(S)  |사용가능 재고(N)  |333|E||
|MB1A|검사표본(C)|판매오더 재고(S)  |품질 검사(U)  |331|E||
|MB1A|검사표본(C)|판매오더 재고(S)  |보류 재고(S)|335|E||
|MB1A|검사표본(C)|프로젝트 재고(P)|사용가능 재고(U)  |333|Q||
|MB1A|검사표본(C)|프로젝트 재고(P)|품질 검사(Q)  |331|Q||
|MB1A|검사표본(C)|프로젝트 재고(P)|보류 재고(B)|335|Q||
|MB1A|스크래핑(R)|From|To||||
|MB1A|스크래핑(R)|창고재고(F)  |사용가능 재고(I)  |551|||
|MB1A|스크래핑(R)|창고재고(F)  |품질 검사(T)  |553|||
|MB1A|스크래핑(R)|창고재고(F)  |보류 재고(L)|555|||
|MB1A|스크래핑(R)|위탁재고(R)  |사용가능 재고(R)  |551|K||
|MB1A|스크래핑(R)|위탁재고(R)  |품질 검사(A)  |553|K||
|MB1A|스크래핑(R)|위탁재고(R)  |보류 재고(O)|555|K||
|MB1A|스크래핑(R)|SC 재고  |사용가능 재고(C)  |551|O||
|MB1A|스크래핑(R)|SC 재고  |품질 검사(Q)  |553|O||
|MB1A|스크래핑(R)|판매오더 재고(M)  |사용가능 재고(D)  |551|E||
|MB1A|스크래핑(R)|판매오더 재고(M)  |품질 검사(Y)  |553|E||
|MB1A|스크래핑(R)|판매오더 재고(M)  |보류 재고(S)|555|E||
|MB1A|스크래핑(R)|고객 빈용기(C)  |사용가능 재고(E)  |551|V||
|MB1A|스크래핑(R)|고객 빈용기(C)  |품질 검사(Q)  |553|V||
|MB1A|스크래핑(R)|고객위탁재고(O)  |사용가능 재고(N)  |551|W||
|MB1A|스크래핑(R)|고객위탁재고(O)  |품질 검사(T)  |553|W||
|MB1A|스크래핑(R)|프로젝트 재고(P)|사용가능 재고(U)  |551|Q||
|MB1A|스크래핑(R)|프로젝트 재고(P)|품질 검사(Q)  |553|Q||
|MB1A|스크래핑(R)|프로젝트 재고(P)|보류 재고(B)|555|Q||
|MB1B|이전전기(A)|플랜트->플랜트(O)|저장소에서 반출/반입(M)|301||MIGO_TR|
|MB1B|이전전기(A)|플랜트->플랜트(O)|반출->플랜트(A)|303|||
|MB1B|이전전기(A)|플랜트->플랜트(O)|플랜트로 반입(E)|305|||
|MB1B|이전전기(A)|플랜트->플랜트(O)|운송중 재고(종료)(I)|351|||
|MB1B|이전전기(A)|플랜트->플랜트(O)|반품->반품|455|||
|MB1B|이전전기(A)|저장 위치->저장 위치(L)|가용재고->가용재고(U)|311|||
|MB1B|이전전기(A)|저장 위치->저장 위치(L)|품질검사 -> 품질검사(Q)|323|||
|MB1B|이전전기(A)|저장 위치->저장 위치(L)|보류재고->보류재고(B)|325|||
|MB1B|이전전기(A)|저장 위치->저장 위치(L)|반품->반품(R)|455|||
|MB1B|이전전기(A)|저장 위치->저장 위치(L)|저장위치에서 반출(A)|313|||
|MB1B|이전전기(A)|저장 위치->저장 위치(L)|저장위치로 반입(I)|315|||
|MB1B|이전전기(A)|자재->자재(M)||309|||
|MB1B|이전전기(A)|재고->재고(S)|QI -> 가용재고|321|||
|MB1B|이전전기(A)|재고->재고(S)|보류재고 -> 가용재고(B)|343|||
|MB1B|이전전기(A)|재고->재고(S)|보류재고 -> QI재고(L)|349|||
|MB1B|이전전기(A)|재고->재고(S)|반품 -> 자체재고(E)|453|||
|MB1B|이전전기(A)|재고->재고(S)|반품 -> QI재고(U)|457|||
|MB1B|이전전기(A)|재고->재고(S)|반품 -> 보류재고(O)|459|||
|MB1B|이전전기(A)|공급업체 위탁품(V)|저장위치 가용재고->가용재고(C)|311|K||
|MB1B|이전전기(A)|공급업체 위탁품(V)|SLoc 품질검사->품질검사|323|K||
|MB1B|이전전기(A)|공급업체 위탁품(V)|SLoc 보류재고->보류재고(B)|325|K||
|MB1B|이전전기(A)|공급업체 위탁품(V)|QI ->가용재고|321|K||
|MB1B|이전전기(A)|공급업체 위탁품(V)|보류재고->가용재고(D)|343|K||
|MB1B|이전전기(A)|공급업체 위탁품(V)|보류재고->QI재고(I)|349|K||
|MB1B|이전전기(A)|공급업체 위탁품(V)|위탁재고->자체재고(J)|411|K||
|MB1B|이전전기(A)|공급업체 위탁품(V)|위탁재고->판매오더재고(N)|413|K||
|MB1B|이전전기(A)|공급업체 위탁품(V)|위탁재고->프로젝트재고(O)|415|K||
|MB1B|이전전기(A)|외주업체 재고(C)|가용재고->외주업체재고(E)|541||출발지 541, 도착지 541 O|
|MB1B|이전전기(A)|외주업체 재고(C)|SC 품질검사->SC 가용재고(Q)|321|O||
|MB1B|이전전기(A)|외주업체 재고(C)|플랜트->플랜트(P)|301|O||
|MB1B|이전전기(A)|외주업체 재고(C)|자재->자재(M)|309|O||
|MB1B|이전전기(A)|RTP 재고|저장위치->저장위치(L)|311|M||
|MB1B|이전전기(A)|프로젝트 재고(P)|플랜트->플랜트(A)|301|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|자재->자재(M)|309|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|저장위치 가용재고->가용재고(C)|311|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|SLoc 품질검사->품질검사|323|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|SLoc 보류재고->보류재고(B)|325|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|품질검사->가용재고(Q)|321|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|보류재고->가용재고(K)|343|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|보류재고->QI 재고(D)|349|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|프로젝트 재고 -> 자체 재고(J)|411|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|프로젝트 재고 -> 판매오더 재고(P)|413|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|프로젝트 재고 -> 프로젝트 재료(R)|415|Q||
|MB1B|이전전기(A)|프로젝트 재고(P)|프로젝트 -> 고객위탁(O)|||메뉴 선택 불가|
|MB1B|이전전기(A)|판매 오더 재고(Q)|플랜트->플랜트(P)|301|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|자재->자재(A)|309|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|저장위치 가용재고->가용재고(Q)|311|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|SLoc 품질검사->품질검사|323|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|SLoc 보류재고->보류재고|325|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|QI ->가용재고|321|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|보류재고->가용재고(B)|343|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|보류재고->QI 재고(T)|349|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|판매오더재고->자체재고(R)|411|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|판매오더재고->판매오더재고(,)|413|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|판매오더재고->프로젝트 재고(D)|415|E||
|MB1B|이전전기(A)|판매 오더 재고(Q)|판매오더 -> 고객위탁(U)|||메뉴 선택 불가|
|MB1B|이전전기(A)|고객 위탁(U)|플랜트 -> 플랜트(P)|301|W||
|MB1B|이전전기(A)|고객 위탁(U)|자재 -> 자재(M)|309|W||
|MB1B|이전전기(A)|고객 위탁(U)|고객위탁 -> 판매오더(C)|||메뉴 선택 불가|
|MB1B|이전전기(A)|고객 위탁(U)|고객위탁 -> 프로젝트(U)|||메뉴 선택 불가|
|MB1B|이전전기(A)|고객 위탁(U)|고객 위탁 반입(I)|63C|W||
|MB1B|이전전기(A)|고객 반납용 포장재(N)|플랜트 -> 플랜트(P)|301|V||
|MB1B|이전전기(A)|고객 반납용 포장재(N)|자재 -> 자재(M)|309|V||
|MB1C|입고(E)|From|To|||MIGO_GR|
|MB1C|입고(E)|구매오더없이(W)|가용재고(I)|501|||
|MB1C|입고(E)|구매오더없이(W)|품질검사(Q)|503|||
|MB1C|입고(E)|구매오더없이(W)|보류재고(B)|505|||
|MB1C|입고(E)|구매오더없이(W)|위탁 가용재고(C)|501|K||
|MB1C|입고(E)|구매오더없이(W)|위탁 QI 재고(E)|503|K||
|MB1C|입고(E)|구매오더없이(W)|위탁 보류재고(N)|505|K||
|MB1C|입고(E)|구매오더없이(W)|판매오더 가용재고(A)|501|E||
|MB1C|입고(E)|구매오더없이(W)|판매오더 QI 재고(S)|503|E||
|MB1C|입고(E)|구매오더없이(W)|판매오더 보류재고(L)|505|E||
|MB1C|입고(E)|구매오더없이(W)|프로젝트 가용재고(P)|501|Q||
|MB1C|입고(E)|구매오더없이(W)|프로젝트 QI 재고(R)|503|Q||
|MB1C|입고(E)|구매오더없이(W)|프로젝트 보류재고(J)|505|Q||
|MB1C|입고(E)|구매오더없이(W)|RTP 가용재고(E)|501|M||
|MB1C|입고(E)|무상납품(D)||511|||
|MB1C|입고(E)|생산오더없이(J)|가용재고(I)|521|||
|MB1C|입고(E)|생산오더없이(J)|품질검사재고(Q)|523|||
|MB1C|입고(E)|생산오더없이(J)|보류재고(Q)|525|||
|MB1C|입고(E)|생산오더없이(J)|판매오더 가용재고(S)|521|E||
|MB1C|입고(E)|생산오더없이(J)|판매오더 QI 재고(D)|523|E||
|MB1C|입고(E)|생산오더없이(J)|판매오더 보류재고(A)|525|E||
|MB1C|입고(E)|생산오더없이(J)|프로젝트 가용재고(P)|521|Q||
|MB1C|입고(E)|생산오더없이(J)|프로젝트 QI 재고(R)|523|Q||
|MB1C|입고(E)|생산오더없이(J)|프로젝트 보류재고(J)|525|Q||
|MB1C|입고(E)|부산물(Y)|가용재고(T)|531|||
|MB1C|입고(E)|부산물(Y)|판매오더 가용재고(O)|531|E||
|MB1C|입고(E)|부산물(Y)|프로젝트 가용재고(P)|531|Q||
|MB1C|입고(E)|부산물(Y)|네트워크 -> 가용재고(R)|581|||
|MB1C|입고(E)|부산물(Y)|네트워크 -> 판매오더(M)|581|E||
|MB1C|입고(E)|부산물(Y)|네트워크 -> 프로젝트(N)|581|Q||
|MB1C|입고(E)|초기재고입력(자체)(E)|가용재고로(T)|561|||
|MB1C|입고(E)|초기재고입력(자체)(E)|품질검사재고(Q)|563|||
|MB1C|입고(E)|초기재고입력(자체)(E)|보류재고(C)|565|||
|MB1C|입고(E)|초기재고입력(자체)(E)|외주가공 가용재고로(W)|561|O||
|MB1C|입고(E)|초기재고입력(자체)(E)|외주 QI 재고로(B)|563|O||
|MB1C|입고(E)|초기재고입력(자체)(E)|고객반환용포장재 가용재고로(K)|561|V||
|MB1C|입고(E)|초기재고입력(자체)(E)|고객반환용포장재 QI 재고로(R)|563|V||
|MB1C|입고(E)|초기재고입력(자체)(E)|고객위탁 가용재고로(O)|561|W||
|MB1C|입고(E)|초기재고입력(자체)(E)|고객위탁 QI 재고로(S)|563|W||
|MB1C|입고(E)|초기재고입력(외부)(I)|위탁 가용재고(I)|561|K||
|MB1C|입고(E)|초기재고입력(외부)(I)|위탁 QI 재고로|563|K||
|MB1C|입고(E)|초기재고입력(외부)(I)|위탁 보류재고(G)|565|K||
|MB1C|입고(E)|초기재고입력(외부)(I)|판매오더 가용재고(O)|561|E||
|MB1C|입고(E)|초기재고입력(외부)(I)|판매오더 QI 재고(D)|563|E||
|MB1C|입고(E)|초기재고입력(외부)(I)|판매오더 보류재고(A)|565|E||
|MB1C|입고(E)|초기재고입력(외부)(I)|프로젝트 가용재고(P)|561|Q||
|MB1C|입고(E)|초기재고입력(외부)(I)|프로젝트 QI 재고(R)|563|Q||
|MB1C|입고(E)|초기재고입력(외부)(I)|프로젝트 보류재고(J)|565|Q||
|MB1C|입고(E)|초기재고입력(외부)(I)|RTP 가용재고(U)|561|M||
|MB1C|입고(E)|고객 반품(R)||451|||
|MB1C|입고(E)|재고이전에서(Q)|플랜트로 반입(P)|305|||
|MB1C|입고(E)|재고이전에서(Q)|저장위치로 반입(I)|315|||
|MB31|구매오더에 대한 입고|구매오더 -> 창고재고(Q)||101||MIGO_GO|
|MB31|구매오더에 대한 입고|창고재고 -> 구매오더(A)||102|||
|MB31|구매오더에 대한 입고|업체반품 -> 구매오더(R)||122||취소: 123|
|MB01|구매오더에 대한 입고|구매오더 -> 창고재고(P)||101||MIGO_GR|
|MB01|구매오더에 대한 입고|구매오더 -> GR보류재고(S)||103|||
|MB01|구매오더에 대한 입고|GR보류재고 -> 창고재고(B)||105|||
|MB01|구매오더에 대한 입고|업체반품 -> 공급업체(R)||122||취소: 123|
|MB01|구매오더에 대한 입고|GR보류재고 -> 업체반품(E)||124||취소: 125|
|MB04|외주가공 차후조정|완성품||121||MIGO_GS|
|MB04|외주가공 차후조정|구성부품 추가 출고 처리||543|O|계획 대비 구성부품 과다 소비에 따른 추가 "재고 소비" 처리|
|MB04|외주가공 차후조정|구성부품 출고 취소 처리||544|O|계획 대비 구성부품 과소 소비에 따른 추가 "투입 취소" 처리|
  
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
  - 원문자 : https://ilsang2.tistory.com/122
    - ⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳​㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵​㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿
    - ❶❷❸❹❺❻❼❽❾❿⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴
    - ⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾
    - ㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉     ㊊㊋㊌㊍㊎㊏㊐     ㊤㊥㊦ ㊧㊨
    - ㉠㉡㉢㉣㉤㉥㉦㉧㉨㉩㉪㉫㉬㉭㉮㉯㉰㉱㉲㉳㉴㉵㉶㉷㉸㉹㉺㉻
    - ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ
    - ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ
 
  </div></details>
