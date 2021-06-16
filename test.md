# 1. 일정 계획
<details open><summary> Details ============================================================================</summary><div> 

<!-- ---------- ---------- 주석 시작 : 이 영역은 "오늘의 업무"를 기록하는 영역임 ---------- ---------- --> 
<!-- mathjax 9개 font size : \tiny \scriptsize \small \normalsize \large \Large \LARGE \huge \Huge -->
## 오늘의 일정
※ 이동 : [오늘](#오늘의-일정), [향후 일정](#12-향후-일정), [과거 이력](#13-과거-이력), [책갈피-장기](#111-장기), [책갈피-단기](#112-단기), [책갈피-이력](#113-이력), [2. DS정리](#2-데이터-과학-정리), [3. Links](#3-useful-links)  
※ 상태 : 【○】 등록-일반, 【㉾】 등록-우선, 【⊙】【$\odot$】 선행 미완/대기, 【◐】【$\ominus$】【$\oslash$】 진행, 【◑】 F/up 진행, 【●】【$\oplus$】【$\otimes$】 완료, 【↗】 이관 전달, 【↙】 이관 수신, 【Ｘ】 취소  
> $\boxed{일일~업무(이력) ~~ \xleftrightarrow[~~단기~실행~~]{~~책갈피~반영~~} ~~ \boxed{책갈피(이력)~~ \boxed{단기_{제목+내용}} \leftrightarrows \boxed{\boxed{단기_{제목}} ~~ 장기} ~~ } ~~ } \longleftrightarrow \boxed{상태~관리}$  
<!-- <font color='cyan'>【○】</font> --> 
<!-- <details open><summary>제목</summary><div>한 행 띄고 내용</div></details> --> 

▣ 2021-06-16, 수  
* 염소제거샤워기 알아보기 : 몽디에스(32,800), 닥터피엘(34,800)
* 회사 업무 : 한화솔루션/케미칼 SAP 고도화 Planning Project > 금주에는 SCM 개선과제 상세 내역 살펴보기 【$\ominus$】 ; 구매담당 업무분장 [게시글](https://snc.eagleoffice.co.kr/neo/bbs/C/19662/002373305)
* Job, Q2 Task  
  + jupyter notebook에서 graphviz 사용 방법 확인, myLib.py에 function 등록 ☞ 이는 ipynb에서 Orange3의 [workflows](https://orangedatamining.com/workflows/)를 기록하기 위함임. 
    ```python
    import graphviz # 설치 : https://pypi.org/project/graphviz ; Attribute : https://graphviz.org/doc/info/attrs.html
    from IPython.display import display, SVG, Image           # User guide : https://graphviz.readthedocs.io/en/stable/manual.html
    def view_graphviz(gvSourceCode):
        graph = graphviz.Source(gvSourceCode)
        # display(Image(graph.pipe(format='png')))  # 내용 복사가 안되므로 좋지 않음
        display(SVG(graph.pipe(format='svg')))      # 내용 복사가 되므로 좋음   ```
  + Orange workflow [사례 "ML with Orange"](https://medium.com/@jackmaughan_50251/machine-learning-with-orange-8bc1a541a1d7), scikit-learn [모델 전환](https://stackoverflow.com/questions/57003285/how-to-get-scikit-learn-model-output-from-orangeml-model) 검토
* Navigation Memo 
  * Job, Q2 Task  
    + Orange Data Mining [url](https://orangedatamining.com/), [Wiki](https://en.wikipedia.org/wiki/Orange_(software)) : ODM [Doc](https://orangedatamining.com/docs/) > Python Library [Tutorial](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/#tutorial) > "[Data](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/data.html "Tutorial > Data") 【$\oplus$, 6/14】, [Classification](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/classification.html "Tutorial > Classification") & [Regression](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/regression.html "Tutorial > Regression") 【$\oplus$, 6/15】"
    + [sps3](https://open.sap.com/courses/sps3) `Using SAP Screen Personas for Advanced Scenarios` 20210611∼, 훑어보기 진행
  * openSAP fiori3 6/4 【$\oplus$】 → SAP Screen Personas 아래 학습 경로대로 학습(+ SAP TechED 'Screen PERSONAS' Session) → 아래 BackLog → [책갈피-단기](#112-단기)  
    + SAP [Screen Personas](http://www.sapscreenpersonas.com/) 학습 경로 : openSAP [fiori3](https://open.sap.com/courses/fiori3) Week 3 참조  
    &nbsp; ☞ [Screen Personas](http://www.sapscreenpersonas.com/) : SCN [Roadmap](https://blogs.sap.com/2020/01/07/sap-screen-personas-roadmap-update-january-2020-accelerating-sap-fiori-adoption/) & [SP12 소개](https://blogs.sap.com/2020/12/14/sap-screen-personas-3.0-sp12-now-available.-sapui5-applets-easier-sap-fiori-launchpad-integration-native-barcode-scanning/) 및 [비교](https://wiki.scn.sap.com/wiki/display/Img/Compare+SAP+Screen+Personas+versions) → openSAP [sps2](https://open.sap.com/courses/sps2), [sps3](https://open.sap.com/courses/sps3), [sps4](https://open.sap.com/courses/sps4) → SCN [Topic](https://community.sap.com/topics/screen-personas), [Wiki](https://wiki.scn.sap.com/wiki/display/Img/SAP+Screen+Personas+Product+Support) & [Help Portal](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US)
---  
* Data Science
  + Orange Data Mining(이하 ODM), [Workflow](https://orangedatamining.com/workflows/) 훑어 봄. 다음은 생각해 본 학습 경로(기반 → 활용 → Python재현)임.
    - ① 초보자용 동영상［[엘리셈](https://www.youtube.com/playlist?list=PL3geb_qrBQYfOmGuHtnf0RZMMXaev-Zvr)］ → ② ODM Tutorial 동영상 → ③ ODM `Workflow + 동영상` <Br>&nbsp; &nbsp; → ④ ML 관련 책(Andreas Muller, Mark Fenner, 주머니 속의...)이나 경진대회 책을 Orange로 해 보기 → (수시로) S/4HANA에서 ML 활용할 것을 생각하고 실행해 보기<Br>&nbsp; &nbsp; → ⑤ ODM [Doc](https://orangedatamining.com/docs/) > Python Library [Tutorial](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/#tutorial) ([Data](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/data.html) 【$\oplus$】 → [분류](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/classification.html) → [회귀](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/regression.html)) → ⑥ ODM [Doc](https://orangedatamining.com/docs/) > [Widget Development](https://orange3.readthedocs.io/projects/orange-development/en/latest/) → ⑦ Orange3에 Pycaret이나 Pytorch Widget 개발
* System Conversion to SAP S/4HANA 검토 ☞ 5/28 시작, [책갈피-단기](#112-단기)로 이동됨
* BSG Fiori 전문가 참석 회의(6/1, 화, 15-17시, RM413) 대비 Fiori 검토 (Resource 검색, 정리ㆍ요약) ☞ 5/28 시작, [책갈피-단기](#112-단기)로 이동됨 <details open><summary>Details</summary><div>
  + openSAP 'fiori' course 검색(아래 [`3 > 3.2 SAP`의 openSAP fiori 관련 과정](#32-sap) 참조) : [fiori3](https://open.sap.com/courses/fiori3) → s/4h18 (기타 : [ieux1](https://open.sap.com/courses/ieux1) Intelligent Enterprise User Experience with SAP Fiori 3)
    - https://ui5.sap.com ; SCN [Fiori](https://community.sap.com/topics/fiori), [Fiori Wiki Home](https://wiki.scn.sap.com/wiki/display/Fiori/SAP+Fiori+Home) ; **<font color='gold'>Fiori Design Guidelines</font>** [URL](https://experience.sap.com/fiori-design-web/sap-fiori), SCN [Blog](https://blogs.sap.com/2019/05/25/get-ready-for-sap-fiori-3/) Get Ready for SAP Fiori 3
    - [fiori3](https://open.sap.com/courses/fiori3), 20200609, `SAP Fiori Overview: Design, Develop and Deploy` **for SAP Fiori Experts** → 20210531 ∼ 20210604, 1회 훑어보기 완료 【$\oplus$】<details><summary>Details</summary><div>
      |구분|내역|완료 일자|비고(내용 요약, 주요 HyperLink)|
      |:--|:--|:--:|:--|
      |Week 1 |SAP Fiori Overview|2021-05-31|SAP [Fiori Apps Reference Library](https://fioriappslibrary.hana.ondemand.com/) (S-ID S0023118924 사용)|
      |&nbsp; &nbsp; Unit 1|Introducing SAP Fiori|2021-05-31||
      |&nbsp; &nbsp; Unit 2|Designing a Great User Experience|2021-05-31|SAP Fiori [Design Guidelines](https://experience.sap.com/fiori-design/) → [Web](https://experience.sap.com/fiori-design-web/sap-fiori)|
      |&nbsp; &nbsp; Unit 3|Architecture Overview|2021-05-31|ㆍ8쪽, UI Compoenets 4가지: LPD, Apps, Elements, UI5|
      |&nbsp; &nbsp; Unit 4|Development Tools Overview|2021-05-31|ASUG [A Practical Guide for Senior IT Leadership](https://www.sap.com/documents/2019/05/44b3ebd5-4b7d-0010-87a3-c30de2ffd8ff.html)|
      |&nbsp; &nbsp; Unit 5|How to Get SAP Fiori Up and Running|2021-05-31|Users who click on a business object link get options for what they intend to do.|
      |Week 2<Br><Br>|Designing SAP Fiori Apps<Br><Br>|2021-06-01<Br><Br>|DLD(Design-Led Development): Discover → Design → Develop<Br>&nbsp; &nbsp; ☞ Scope, Research, Synthesize → Ideate, Prototype, Validate → Implement, Test, Deploy|
      |&nbsp; &nbsp; Unit 1|Why Good Design Matters|2021-05-31|cf: https://open.sap.com/courses?q=design|
      |&nbsp; &nbsp; Unit 2|Exploring the SAP [Fiori Design System](https://experience.sap.com/fiori-design/)|2021-05-31||
      |&nbsp; &nbsp; Unit 3<Br><Br><Br>|Designing with SAP Fiori<Br><Br><Br>|2021-05-31<Br><Br><Br>|Building Blocks : UI Elements, Patterns, Gestures, Colors, Typography, Floorplans,<Br>&nbsp; &nbsp; &nbsp; Dynamic Page, Flexible Column Layout, Layouts, Draft Handling, Edit Flow,<Br>&nbsp; &nbsp; &nbsp; Situation Handling, Message Handling, Notifications, Concepts|
      |&nbsp; &nbsp; Unit 4<Br><Br>|Hands-On Design 1<Br><Br>|2021-05-31<Br><Br>|ㆍUser stories with scenes(= pre-drawn images), Download free at [Toolkit](https://experience.sap.com/designservices/resource/scenes)<Br>ㆍTask Type for your jump start : Routine, Reactive, Monitoring, Analytical, Expert|
      |&nbsp; &nbsp; Unit 5|Hands-On Design 2|2021-05-31|Whiteboard 권장 : 특별한 기술 불필요 → 누구나 큰 노력 없이 사용 가능하며 변경하기 쉽다.|
      |&nbsp; &nbsp; Unit 6<Br><Br>|Best Practices and Tools<Br>for SAP Fiori Design|2021-06-01<Br><Br>|ㆍ10쪽 : [ut1-2](https://open.sap.com/courses/ut1-2) Basics of Design Testing (Edition Q2/2019), [dr1](https://open.sap.com/courses/dr1) Basics of Design Research<Br>ㆍ17쪽 : [Icon Explorer](https://sapui5.hana.ondemand.com/test-resources/sap/m/demokit/iconExplorer/webapp/index.html#/overview/SAP-icons/); UI Theme Designer [URL](https://themedesigner-themedesigner.dispatcher.hanatrial.ondemand.com/index.html), [Help](https://help.sap.com/viewer/8ec2dae34eb44cbbb560be3f9f1592fe/1709.latest/en-US/a118094264684230bb6510045b5b5b7c.html), [SCN](https://community.sap.com/topics/ui-theme-designer), [Theme 설정](https://blogs.sap.com/2019/10/23/sap-fiori-theme-customization/)|
      |Week 3 |Developing SAP Fiori Apps|2021-06-03|[Screen Personas](http://www.sapscreenpersonas.com/) : SCN [Roadmap](https://blogs.sap.com/2020/01/07/sap-screen-personas-roadmap-update-january-2020-accelerating-sap-fiori-adoption/) & [SP12 소개](https://blogs.sap.com/2020/12/14/sap-screen-personas-3.0-sp12-now-available.-sapui5-applets-easier-sap-fiori-launchpad-integration-native-barcode-scanning/) 및 [비교](https://wiki.scn.sap.com/wiki/display/Img/Compare+SAP+Screen+Personas+versions) → openSAP sps[2](https://open.sap.com/courses/sps2), [3](https://open.sap.com/courses/sps3), [4](https://open.sap.com/courses/sps4) → SCN [Topic](https://community.sap.com/topics/screen-personas), [Wiki](https://wiki.scn.sap.com/wiki/display/Img/SAP+Screen+Personas+Product+Support) & [Help Portal](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US)|
      |&nbsp; &nbsp; Unit 1<Br><Br>|Using SAP [Business Application Studio](https://www.sap.com/appstudio)<Br>to Develop SAP Fiori Apps|2021-06-01<Br><Br>|ㆍ11쪽 : Reference URLs<Br><Br>|
      |&nbsp; &nbsp; Unit 2<Br><Br>|Building Modern Web Applications<Br>with [SAPUI5](https://sapui5.hana.ondemand.com/) `=HTML+CSS+JavaScript`|2021-06-01<Br><Br>|ㆍSAPUI5: 5쪽 Portfolio, [환경](https://ui5.sap.com/#/topic/74b59efa0eef48988d3b716bd0ecc933 "SAP UI5 Browser and Platform Support"), <font color='gold'>★</font>[Demo Apps](https://ui5.sap.com/#/demoapps), <font color='gold'>★</font>[Web Components](https://sap.github.io/ui5-webcomponents/ "16쪽, UI5 Web technology brings scalability and flexibility to SAP Fiori app development; React, Angular, or Vue와 같은 것들은 SAP UI5 Web Components를 사용할 수 있다"), [Card Explorer](https://ui5.sap.com/#/tools), [Dev](https://developers.sap.com/topics/ui5.html), [SCN](https://community.sap.com/topics/ui5)<Br>ㆍ[OpenUI5](https://openui5.org/): [SDK](https://openui5.hana.ondemand.com/), [Github](https://github.com/SAP/openui5), [YouTube](https://www.youtube.com/c/openui5videos/featured), [Markdown Docs](https://sap.github.io/openui5-docs), [Blog](https://velog.io/@rumblekat/series/OpenUI5), [Wiki](https://en.wikipedia.org/wiki/OpenUI5), 비교 [EN](https://blogs.sap.com/2013/12/11/what-is-openui5-sapui5/) [KO](https://blog.daum.net/rightvoice/984); CSS [KO](https://ko.wikipedia.org/wiki/CSS) [EN](https://en.wikipedia.org/wiki/CSS), wikidocs [JavaScript](https://wikidocs.net/book/5373)|
      |&nbsp; &nbsp; Unit 3<Br><Br>|Accelerating App Development<Br>with SAP Fiori Elements `and metadata`|2021-06-01<Br>2021-06-02|ㆍ5-6쪽 : Page Type(Overview, List Report, Analytical List, Worklist, Object), Standard UI Logic<Br>ㆍ8-13쪽 : Fiori Tools (`MS VS Code Extension` or SAP Biz. Application Studio), 12쪽 Demo|
      |&nbsp; &nbsp; Unit 4<Br><Br><Br>|Developing OData Services<Br>for SAP Fiori Applications<Br>`UI5/Fiori→OData,REST→Model→CDS`|2021-06-02<Br><Br><Br>|ㆍ5~7쪽 : SAP CAP(Cloud Application Programming) Model for Java & JavaScript(Node.js)-*based OData services*<Br>ㆍ9~12쪽 : ABAP RAP(RESTful Application Programming) Model for ABAP-*based OData services*<Br>ㆍ14쪽 : 여기서 다룬 2개의 RESTful Model에 대해, <font color='gold'>**Get Started**</font> Today - [CAP](https://cap.cloud.sap/docs/get-started/); [ABAP](https://community.sap.com/topics/abap) [RAP](https://blogs.sap.com/2019/10/25/getting-started-with-the-abap-restful-programming-model/) [Dev](https://www.sapinsideronline.com/a-developers-guide-to-the-abap-restful-programming-model/), [ABAP](https://community.sap.com/topics/abap) [CDS](https://blogs.sap.com/2016/02/01/getting-started-with-abap-core-data-services/)|
      |&nbsp; &nbsp; Unit 5<Br><Br>|Simplifying Classic Transaction Screens<Br>with SAP [Screen Personas](http://www.sapscreenpersonas.com/) ☞ [Flavor Gallery](http://link.personas.help/SAPScreenPersonasFlavorGallery)|2021-06-03<Br><Br>|ㆍ10쪽 : Choose a Path to the SAP Fiori User Experience ☞ 비교 [①](https://www.fingent.com/blog/top-3-ui-offerings-from-sap-fiori-screen-personas-and-lumira/) [② 3.0 SP06, Slipstream Engine](https://www.avelon.be/news-blog/sap-screen-personas-versus-fiori) [③ 사용 소감](https://www.linkedin.com/pulse/sap-ux-grand-unification-theory-how-screen-personas-sp06-dan-barton) <font color='gold'>★</font><Br>ㆍ11쪽 : SAP [Screen Personas](https://help.sap.com/viewer/20993a0c28654a26beb2b63b722d74f2/Current/en-US/0036f15101d9445ee10000000a423f68.html) > [구축 고려 사항](https://help.sap.com/viewer/9db44532734f4718b91e460c020307fe/Current/en-US "SAP Help Portal, Implementation Considerations"), 3.0 [Guide](https://blogs.sap.com/2020/06/16/managing-sapui5-dependencies-in-sap-screen-personas-new-guide-available/) SP12 [①](https://blogs.sap.com/2020/12/14/sap-screen-personas-3.0-sp12-now-available.-sapui5-applets-easier-sap-fiori-launchpad-integration-native-barcode-scanning/ "Peter Spielvogel, 2020-12-14") [②](https://www.youtube.com/playlist?list=PLo17W6sWsxWMMli_i5rCCChLbYstVmMpF "YouTube, Productivity Power Play 목록"), 오늘 시작 ([Help Q&A](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US); [SCN](https://community.sap.com/topics/screen-personas) [문의](https://answers.sap.com/questions/ask.html?primaryTagId=67838200100800005412); Add-on)|
      |&nbsp; &nbsp; Unit 6|Building iOS Apps|2021-06-03||
      |&nbsp; &nbsp; Unit 7<Br><Br>|Creating Android Apps Natively<Br>or with the Mobile Development Kit|2021-06-03<Br><Br>|ㆍ10쪽 : Mobile Development Kit = Low Code + Fiori Designs + Enterprise Mobility<Br><Br>|
      |Week 4 |Managing SAP Fiori|2021-06-04||
      |&nbsp; &nbsp; Unit 1<Br><Br>|Understanding SAP Fiori Content<Br><Br>|2021-06-04<Br><Br>|ㆍ3쪽 : [SAP Fiori deployment options](https://www.sap.com/documents/2018/02/f0148939-f27c-0010-82c7-eda71af511fa.html "SAP Fiori Deployment Options and System Landscape Recommendations")<Br>ㆍ6∼9쪽 : FLP content entries → Tiles/Links, Target Mappings, Catalogs, Gourps, Roles(PFCG) + intent(8쪽)|
      |&nbsp; &nbsp; Unit 2<Br><Br><Br>|Activating SAP Fiori Out-of-the-Box<Br>ㆍ3∼4쪽 : Biz Role Template, Role 찾기 @ [Lib](https://www.sap.com/fiori-apps-library)<Br>ㆍ6쪽 : [ⓒ Mgr](https://help.sap.com/viewer/d4650bf68a9f4f67a1fda673f09926a9/753.04/en-US) Demo, 7쪽 : Tools & Links : [ⓣ](https://blogs.sap.com/2019/03/16/fiori-for-s4hana-new-rapid-content-activation-on-s4hana-1809-1709-part-1-overview/)|2021-06-04<Br><Br><Br>|$\small \begin{matrix} \text{Initial~Scoping} \\ 관련~ⓡ~선택(Lib) \end{matrix} \rightarrow \begin{matrix} \text{Sandbox} \\ 빠른~ⓕ~활성화(ⓣ~실행) \end{matrix} \rightarrow \begin{matrix} \text{Fit/Gap Analysis} \\ \text{SAP~Fiori~경험} \end{matrix} \rightarrow \begin{matrix} \text{구축~:~ⓒ~및~ⓡ~조정} \\ ⓒ~Mgr + ⓣ~Cⓒ~활성화 \end{matrix}$<Br>☞ 5쪽 참조 : ⓡ : Role, Lib : Fiori App [Reference Library](https://www.sap.com/fiori-apps-library),  ⓒ : FLP Content, Cⓒ : Customer Content,  [ⓣ Task List](https://blogs.sap.com/2019/03/16/fiori-for-s4hana-new-rapid-content-activation-on-s4hana-1809-1709-part-1-overview/)|
      |&nbsp; &nbsp; Unit 3<Br><Br><Br><Br><Br>|Configuring SAP Fiori Launchpad<Br>ㆍ3쪽 : Managing Scope (= CONF + CUST)<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; when creating custom FLP content<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - scope CONF : client-independent<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - scope CUST : client-dependent|2021-06-04<Br><Br><Br><Br><Br>|ㆍ2∼4쪽 : $\scriptsize \boxed{\text{App}} \xleftarrow{refer} \boxed{\boxed{\text{Target~Mapping}} ~~ \text{Tech~Catalog}} \xleftarrow{refer} \boxed{\boxed{\text{Target~Mapping}} ~~ \text{Biz~Catalog}} \xrightarrow{assign} \boxed{\text{Roles}} \xrightarrow{assign} \boxed{\text{User}}$<Br>ㆍ5쪽 : Tools to further refine SAP Fiori launchpad content and (9쪽 : Demo) app-to-app navigations ☞ [Help Portal](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/08683e5409b74ced8705b2856c96c63b.html)<Br>&nbsp; &nbsp; ① FLP Content Mgr, ② FLP Designer (6쪽 : Demo), ③ App Descriptor Mass Maintenance (7쪽 : Demo)<Br>ㆍ12쪽 : Things you can configure in the SAP Fiori launchpad ☞ 참조 : SCN [Blog](https://blogs.sap.com/2017/11/19/sap-fiori-ui5-app-configuration-in-sap-fiori-launchpad/ "Fiori app configuration in SAP Fiori Launchpad")<Br>ㆍ13쪽 : How to assign SAP Fiori launchpad features to users - ① 전체 사용자 → [IMG](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/6107ee41f89a43c9af0aa279fe039cca.html "Help Portal : Launchpad Configuration Parameters"), ② 개별 Role → FLP Designer|
      |&nbsp; &nbsp; Unit 4<Br><Br><Br>|Supporting SAP Fiori<Br>ㆍ9쪽 : Diagnotics 『 Ctrl + Alt + Shift + S 』<Br><Br>|2021-06-04<Br><Br><Br>|ㆍ5쪽 : SAP Web Analytics(SAP Cloud Platform solution) [Demo](https://www.youtube.com/watch?v=bXMtor_AmPE) ☞ On-Premise는 어떻게 하는가?<Br>ㆍ6쪽 : In-App Help(09:01, no additional charge) - SCN [Blog 'How to Setup'](https://blogs.sap.com/2020/01/07/sap-fiori-for-sap-s-4hana-how-to-setup-the-user-assistant-in-your-s-4hana-fiori-launchpad/ "How to setup the User Assistant in your S/4HANA Fiori launchpad"), Enable Now [SAP Kore URL](https://www.sap.com/korea/products/enable-now.support.html) [YouTube](https://www.youtube.com/watch?v=TDmy27wEw4s)<Br>ㆍ[FLP](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/f951b50a07ce41deb08ced62711fe8b5.html) guide/문서 : [7쪽 the Option to Contact Support](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/599d9ad10f614a09bbc5324f340c64e7.html), [10쪽 Support Tools](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/af641fa4a8ba41379ca8c33f27ef35e9.html), [11쪽 Data Admin](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/f171990f82494b7cb57f3be4d2d011f9.html), [7쪽 SCN Topic](https://community.sap.com/topics/fiori)|
      |&nbsp; &nbsp; Unit 5|Establishing a Central SAP Fiori Launchpad|2021-06-04|| <!-- </div></details>  『 'fiori3' SAP Fiori Overview: Design, Develop and Deploy 』 과정 세부 사항 -->
  + SAP [Screen Personas](http://www.sapscreenpersonas.com/) 학습 경로 : openSAP [fiori3](https://open.sap.com/courses/fiori3) Week 3 참조  
    &nbsp; &nbsp; ☞ [Screen Personas](http://www.sapscreenpersonas.com/) : SCN [Roadmap](https://blogs.sap.com/2020/01/07/sap-screen-personas-roadmap-update-january-2020-accelerating-sap-fiori-adoption/) & [SP12 소개](https://blogs.sap.com/2020/12/14/sap-screen-personas-3.0-sp12-now-available.-sapui5-applets-easier-sap-fiori-launchpad-integration-native-barcode-scanning/) 및 [비교](https://wiki.scn.sap.com/wiki/display/Img/Compare+SAP+Screen+Personas+versions) → openSAP [sps2](https://open.sap.com/courses/sps2), [sps3](https://open.sap.com/courses/sps3), [sps4](https://open.sap.com/courses/sps4) → SCN [Topic](https://community.sap.com/topics/screen-personas), [Wiki](https://wiki.scn.sap.com/wiki/display/Img/SAP+Screen+Personas+Product+Support) & [Help Portal](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US)
    - [sps2](https://open.sap.com/courses/sps2), 20170222, `Introduction to SAP Screen Personas`  → 20210607∼20210610, 1회 훑어보기 완료 【$\oplus$】<Br>by Peter Spielvogel, Sebastian Steinhauer, Sylvia Barnard and Vandana Deep <details><summary>Details</summary><div>
      - Week 1. `Basics`
        - Unit 1. Introducing SAP Screen Personas : High-Leel Overview of SAP Screen Personas
          - How SAP Screen Personas works in combination with SAP Fiori
        - Unit 2. Touring the Product
        - Unit 3. Simplifying Business Processes
        - Unit 4. Building a Dashboard
        - Unit 5. Merging Tabs
          - When merging tabs, Consider the amount of information being pulled from the back end.
          - Which factors should you consider when merging tabs?  
            The presence of required fields spread across merged tabs and The number of tabs being merged
          - What happens when the SAP Screen Personas client requests the content of the merged tabs?  
            The server simulates clicking on each merged tab and sends back only the fields that appear on the merged screen.
      - Week 2. `Simplifying SAP ERP Screens`
        - Unit 1. Using Themes
          - 6쪽, Visual Layering : The Original SAP GUI for HTML Screen → The SAP Screen Personas Theme → The Flavor
        - Unit 2. Working with Tables
          - 4쪽, Table formatting options : <font color='gold'>supported</font>(GUI Table Control, GUI Grid View Control) vs. not supported(ABAP List)
          - 5쪽, Optimizing performance with table variants : Reduce the amount of data transferred from the back end
        - Unit 3. Building a Simple Script
        - Unit 4. Using Events
        - Unit 5. Simplifying Web Dynpro ABAP Applications
          - 4쪽, Enablement of SAP Screen Personas for WD4A requires minimum releases<Br>☞ SAP Screen Personas 3.0 SP01, NetWeaver SAP_UI 7.50 SP00
          - 5∼6쪽, Adaption Layers
          - 7쪽, Current limitations
            - In Scripting Editor: Script recorder is currently not available
            - In SAP Screen Personas Editor:  
              Relative alignment in forms is currently missing  
              Tab merging in the Object Identification Floorplan (OIF) and for tab strips is missing  
              For a detailed list of current limitations, see SAP Note [2181980](https://launchpad.support.sap.com/#/notes/0002181980)
          - 11쪽, Where to learn more :  [SAP Help](http://help.sap.com/saphelp_nw75/helpdata/en/eb/4a0c86eee64d0281), [Floorplan Manager Applications](https://blogs.sap.com/2016/03/21/how-to-create-enhance-and-adapt-floorplan-manager-applications-on-sap-netweaver-750/),[Scripting, Logging and Validation](https://blogs.sap.com/2016/01/15/sap-screen-personas-for-web-dynpro-abap-scripting-logging-and-validation/)
      - Week 3. `Accelerating Flavor Development`
        - Unit 1. Design Thinking : [fiori3](https://open.sap.com/couses/fiori3) Week3 Unit5 10쪽 `Choose a Path to the SAP Fiori User Experience` 참조
          - 3쪽, Process Steps : Individual phases of Design Thinking <Br> `Understand` → `Ovserve` → `Define PoV` → `Ideate` → Iterate `『 Prototype → Test 』` → Implement, Test & Deliver → Manage Changes  
            ① Understand (7∼8쪽) : Outputs - Project plan, timeline, milestones, responsibilities, focus transactions, interview schedule, workshop dates, etc.  
            ② Observe (9∼10쪽) : Outputs - Transcripts of your user interviews, User story maps with existing screen flow, steps, and current issues after the workshop  
            &nbsp; &nbsp; &nbsp; 문제, What are some results of the observation phase of design thinking? - An understanding of users’ workflows, A “persona” of your average user  
            ③ Define PoV(Point-of-View, 11∼12쪽) : define user needs from the user’s perspective(PoV) for creating ideas for your wireframes later on  
            &nbsp; &nbsp; &nbsp; 12쪽, Point of View = user + user needs + your insights  
            ④ Ideate (13쪽) : Start with How-Might-We (HMW), Output - Ideas how to overcome issues  
            ⑤ Prototype (14쪽) : Outputs - Wireframes that can be validated with pilot users  
            ⑥ Test Wireframes (15~16쪽) : Test your wireframes with pilot users and include feedback  
            ⑦ Implement Flavors (17쪽) : Implement flavors in SAP Screen Personas  
            ⑧ Manage Changes – Continuous approach (18쪽)  
            Core Principles of Design Thinking : Involving your users, coming up with a broad set of ideas based on your user feedback,<Br>&nbsp; &nbsp; &nbsp; then creating early prototypes that you iterate with your users until you finally get it right. "`Fail early and often`" is the motto here.
          - 6쪽, SAP Screen Personas <font color='gold'>**project plan**</font> : Task, Activities and Deliverables
        - Unit 2. Accelerating Development with the [Flavor Gallery](https://personasgallery-imagineering.dispatcher.us1.hana.ondemand.com/)
          - Who can access it? : No login required. Customers & Partners.
          - What is it? How it can be leveraged to accelerate SAP Screen Personas project development.
            - SAP [Screen Personas Flavor Gallery](https://personasgallery-imagineering.dispatcher.us1.hana.ondemand.com/) is designed to provide our customers and partners with a place to share flavors that they have built.  
              The premade content available in the gallery is meant to provide guidance and inspiration to others seeking to simplify similar scenarios and transactions.
            - 웹 화면 구성 - **목록**으로 살펴보고, 필요 시 **필터 Icon**클릭하여 Filter기능을 활용해 볼 것  
              ⑤ ABAP Function Module, ① Flavor(specific to a transaction), ④ Image Collection, ⑥ JavaScript Library, ⑦ Quick Styles, ③ Template, ② Theme
            - Flavor를 사용하려면 Template도 같이 내려 받아야 한다 ☞ 일괄 처리는 안되고, 각각의 화면에서 내려 받아야 함
          - Question 1 : What is the relationship among assets in the Flavor Gallery?
            - Assets from the image collection can be used with any transaction.
            - Flavors in the Flavor Gallery can list templates, images, and themes as related assets.
          - Question 2 : What must you do after downloading content from the Flavor Gallery?
            - Contact your administrator to receive permissions for content import.
            - Further personalize it based on your project needs.
          - SAP Screen Personas Flavor Gallery 참고 정보, [SCN](https://community.sap.com/search/?ct=all&q=Screen%20Personas%20Flavor%20Gallery) 위주
            - [SCN](https://blogs.sap.com/2015/09/02/announcing-sap-screen-personas-flavor-gallery/), Vandana Deep, 2015-09-02, updated 2017-07-12, Announcing SAP Screen Personas Flavor Galler
            - [SCN](https://blogs.sap.com/2016/09/26/getting-started-with-templates-in-sap-screen-personas-flavor-gallery/), 2016-09-26, Getting Started with Templates in SAP Screen Personas Flavor Gallery
        - Unit 3. Using SAP Screen Personas with the Belize Theme (This theme was instroduced with S/4HANA 1609.)
          - The Belize theme provides an SAP Fiori-inspired appearance; SAP Screen Personas is required to simplify these screens further.
          - How can you use SAP Screen Personas with the Belize theme?  
            Remove controls from the screen that you do not need.  
            Use scripts to automate user actions to streamline the business process flow.
        - Unit 4. Running Flavors in SAP GUI
          - Advantages
            - Maintaining cherished user habits: If your users are simply used to working in SAP GUI for Windows.
            - General advantages of SAP GUI for Windows: Better interactivity, Better performance, More features, ABAPer 활용
            - Some transactions only work in SAP GUI for Windows, e.g. Office Integration
          - Compatibility & Limitations : SAP Note 2080071 [EN](https://launchpad.support.sap.com/#/notes/2080071) [KO](https://userapps.support.sap.com/sap/support/notes/translate/0002080071?targetLanguage=KO) SAP GUI for Windows: Support for SAP Screen Personas 3.0
          - What is one of the reasons why the editor for SAP Screen Personas 3.0 was built into SAP GUI for HTML?<Br>☞  GUI for HTML does not require a separate client installation and is aligned with current industry standards.
        - Unit 5. Finding More Information and What's Next?
          - 10쪽, Available resources : Youtube [SAP UX Engineering](https://www.youtube.com/channel/UC4FRdP-pm8mwIRbqOQwnPJQ) > [Productivity Power Play](http://videos.personas.help), [Knowledge Base](http://link.personas.help/KnowledgeBase) (SAP [Help](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US)), SAP Press [E-Bite](www.sap-press.com/3975), [SCN](http://link.personas.help/blogs)
          - 기타 : Going Mobile with SAP Screen Personas – 2019-08-13 [Part 1](https://itpfed.com/going-mobile-with-sap-screen-personas-part-1/), 2019-10-21 [Part 2](https://itpfed.com/going-mobile-with-sap-screen-personas-part-2/)
    - [sps3](https://open.sap.com/courses/sps3), 20170919, `Using SAP Screen Personas for Advanced Scenarios` <font color='gold'>**현재 W2U4 진행**</font> <Br>by Sebastian Steinhauer, Tobias Queck, Vandana Deep, Peter Spielvogel, Regina Sheynblat, Klaus Keller, Tamas Hoznek <details><summary>Details</summary><div>
      - Week 1. Beyond the Basics
        - Unit 1: Introduction
        - Unit 2: Understanding the Architecture
          - 2쪽, SAP Screen Personas 3.0 requires an SAP NetWeaver ABAP stack and does not modify any other SAP or custom component.
          - 3쪽, Simplified Architecture behind SAP Screen Personas <Br> ☞ 상위버전(ECC → S/4HANA)으로 Upgrade해도 Screen Personas에 영향은 없다(your flavors stay the same). 그러나, Look & Feel을 맞추려면 일부 변경은 필요하다.
          - 6쪽, The SAP Screen Personas team releases a new service pack every 6 to 9 months. In between, there’s a release of the updated client sources every two weeks.
          - 7쪽, the SAP Screen Personas client relies heavily on the SAP GUI for HTML for rendering as well as its meta data for editing.
        - Unit 3: Acommodating Real-World Business Processes
          - 2쪽, SAP Screen Personas helps you build role-based screens, which we call flavors.
        - Unit 4: Fine-Tuning with Advanced Features
          - What can you do to reduce the nesting levels of containers? Extract objects.
          - How can you access the Advanced Property editor from the Flavor editor? Use the shortcut: CTRL + ALT + E or ALT + H + S + M + A
          - Why do you need to be careful when using the Advanced Property editor?  
            Because you can still enter invalid values, which might harm your flavor if you ignore the warning.
        - Unit 5: Going Beyond Basic Scripting
          - Session cache `session.utils.put` and `session.utils.get` are executed client-side. A trip to the back end will not occur.
        - Unit 6: Creating an F4 Lookup
          - 4쪽, SAP support two types of help: modal and amodal.<Br>&nbsp; &nbsp; SAP Screen Personas prefers that F4 help is set to the modal setting.
          - 5∼6쪽, F4 구현 방안  
            ① `Admin > Whitelist 등재 필수`  
            ② (방안.1) `Inawer > Text Field > F4 Text Field` 또는 (방안.2) `Script에서 showF4Help Property 사용`
      - Week 2. Intermediate Scripting
        - Unit 1: Handling Context-Dependent Scenarios → `Expand/Collapse Area` Icon
          - How can you build a collapsable area in SAP Screen Personas?<Br>→ By hiding, showing, moving, and resizing controls through scripting.
          - What does the following script call do? `session.utils.findById(<controlID>).hide()`<Br>→ It identifies a control by its ID and hides it.
        - Unit 2: Working with Advanced Events
          - 3쪽, Screen Events(onAfterRefresh, onBeforeRefresh, onEnter, onLoad, onResize) vs. Control Events ☞ [Wiki](https://wiki.scn.sap.com/wiki/display/Img/Available+Events+for+Scripting), [Help Portal](https://help.sap.com/viewer/20993a0c28654a26beb2b63b722d74f2/Current/en-US/aad021f7696044e1bdecfee2c967c52b.html?q=digital%20painting%20for%2068m), [web](https://sapinaminute.com/sap-screen-personas-understanding-the-script-events/)
          - 5쪽, Suppressible and not Suppressible Events  
            Suppressible means that the standard event processing can be stopped in SAP Screen Personas script.
          - 7∼8쪽 : To suppress a standard action, set the return value to “true”.
          - ⓟ → Show Help : [Quick Start Guide](https://wiki.scn.sap.com/wiki/display/Img/Getting+Started+-+Personas+Runtime), [Help Portal](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US), Scripting API [Local](https://hqchanadb1.hanwha.co.kr:44310/sap/bc/personas3/core/resources/generated/documentation/PersonasScriptingAPIDoc.html) vs. [Community Wiki](https://wiki.scn.sap.com/wiki/display/Img/Scripting+API) ☞ 참조 : [Tutorial](https://github.com/SAPDocuments/Tutorials/blob/master/tutorials/personas-access-learning-sys/personas-access-learning-sys.md)
        - Unit 3: Using Remote Function Calls
          - 2쪽, RFCs are commonly used independently of SAP Screen Personas to enable function calls between two SAP systems.  
            &nbsp; &nbsp; &nbsp; &nbsp; Moreover, they can be used to execute functions on the same system but in a different session.
          - T-Code `/PERSONAS/ADMIN`을 `/n/PERSONAS/ADMIN`과 같이 실행하여 Function Module을 Whitelist에 등재해야 Editor에서 사용 가능함.
        - Unit 4: Working with Tables
          - 3쪽 : Optimizing Performance = `Table Variants`(to reduce the amount of data transferred from the backend) + `Further Personalization`
        - Unit 5: Debugging
        - Unit 6: Managing Scripts
      - Week 3. Building a Consistent Experience
        - Unit 1: Establishing Corporate Branding
        - Unit 2: Creating Quick Styles
        - Unit 3: Using Templates
        - Unit 4: Building Templates
        - Unit 5: Integrating Flavors with the SAP Fiori Launchpad
        - Unit 6: Managing Flavor Groups
      - Week 4. Rollout and Administration
        - Unit 1: User and Role Administration
        - Unit 2: Object Maintenance
        - Unit 3: Additional Administrative Tasks
        - Unit 4:Translating Flavors
        - Unit 5: Deploying Objects Across the Landscape
      - Week 5. Best Practices
        - Unit 1: General Performance Considerations
        - Unit 2: Tuning Performance
        - Unit 3: Building Adaptive Designs
        - Unit 4: Building Responsive Designs
        - Unit 5: Versioning and Testing Flavors
        - Unit 6: Using Analytics
        - Unit 7: Summarizing and Next Steps
    - [sps4](https://open.sap.com/courses/sps4), 20180926, Building Mobile Applications with SAP Screen Personas  
      by Sylvia Barnard, Conrad Bernal, Vandana Deep, Tamas Hoznek, Tobias Queck, Regina Sheynblat, Peter Spielvogel, Sebastian Steinhauer, Ashley Tung
  + SAP [TechEd](https://pages.sapteched.com/) 2020 - 'fiori' session 검색(37 Sessions), 'fiori elements' 39 Sessions, 'Screen Personas' 5 Sessions  
    - 'Screen Personas' 5 Sessions
<!-- ---------- ---------- 주석 종료 : 이 영역은 "오늘의 업무"를 기록하는 영역임 ---------- ---------- -->

## 1.1 책갈피
<details><summary> Details ────────────────────────────────────────────────────</summary><div> <Br>

### 1.1.1 장기
<details><summary> Details - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</summary><div>

※ 참고 : [오늘](#오늘의-일정), [향후 일정](#12-향후-일정), [과거 이력](#13-과거-이력), [책갈피-장기](#111-장기), [책갈피-단기](#112-단기), [책갈피-이력](#113-이력), [2. DS정리](#2-데이터-과학-정리), [3. Links](#3-useful-links)  

<details><summary>책갈피-장기 > Personal > Details</summary><div> 

* 생의 지침
  * Live, Love, Learn and Leave a Legacy – The Four Human Dimensions, by [Stephen Covey](https://en.wikipedia.org/wiki/Stephen_Covey)  
    &nbsp; &nbsp; ![https://brevedy.com/2015/03/12/live-love-learn-and-leave-a-legacy-the-four-human-dimensions/](https://brevedy.com/wp-content/uploads/2015/03/LiveLoveLearnLegacy.png)
  * 지난 2020년 7월 1일 동기(백진욱, 차동진) 모임 시 하고 싶은 3가지에 대해 생각한 바를 명확히 제시하지 못하여 정리해 봄<details><summary>Details</summary><div>
    - 지(智, 定ㆍ慧) ~ 지혜 ☜ 불교식 명상(위빠사나, 마음챙김, 선수행, MBSR, ...)
    - 덕(德, 戒) ~ Stephen Covey **자아실현(To 5x
    L)** ☜ AI, 쉬운 학습 실현&안내, 소통비용↓
    - 체(體, 正精進) ~ 내 몸에 대한 통제, 실행의 기반 마련 ☜ 극기 맨손 체조(요가, 기공체조, 태극권, ...)  
      ※ 지덕체가 계정혜와 1:1은 아니다. 음미할 부분이 있어서 묶어 봤다.  
      &nbsp; &nbsp; 阿含經 → 독립&유기적인 실천 수행법 "三十七菩提分法" 또는 [三十七助道品](http://www.hyunbulnews.com/news/articleView.html?idxno=296738) 또는 [삼십칠도품](https://ko.wikipedia.org/wiki/삼십칠도품)  
      &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; → 구성 : ① 四念處, ② 四正勤, ③ 四神足, ④ 五根, ⑤ 五力, ⑥ 七覺支, ⑦ [八正道](http://www.hyunbulnews.com/news/articleView.html?idxno=296221)  
      &nbsp; &nbsp; [四聖諦](https://ko.wikipedia.org/wiki/사성제) ─ 苦集滅道 (집→고, 도→멸)  
      &nbsp; &nbsp; &nbsp; └─ 道聖諦 : [八正道](https://ko.wikipedia.org/wiki/팔정도) ─ [戒定慧](http://www.hyunbulnews.com/news/articleView.html?idxno=272114) [三學](http://www.hyunbulnews.com/news/articleView.html?idxno=272114 "세 가지 불교 수행법")  
      &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; └─ = 正精進(Continuous Improvements) + 戒(Check) : 正語ㆍ正業ㆍ正命 + 定(Do) : 正念ㆍ正定 + 慧(Plan) : 正見ㆍ正思惟
    - Stephen Covey's 5Ls vs. [Noble Eightfold Path](https://en.wikipedia.org/wiki/Noble_Eightfold_Path)  

      | The Four Human Dimensions|[三學](http://www.hyunbulnews.com/news/articleView.html?idxno=272114 "세 가지 불교 수행법")|[四聖諦](https://ko.wikipedia.org/wiki/사성제 "사성제")의 道聖諦와 [팔정도](https://ko.wikipedia.org/wiki/팔정도 "八正道")|비고|
      |:---|:---|:---|:---|
      |체(體) : To **L**ive - Physical|Act Continuously: 계속 수행|[正精進](https://ko.wikipedia.org/wiki/불교_용어_목록_(정) )ㆍ[正勤](https://ko.wikipedia.org/wiki/불교_용어_목록_(구)#근)|삼학 전체에서 유지|
      |덕(德)|Check : 戒(의지) → 善|口 - 正語 : 바르게 말하기, Right speech||
      |||身 - 正業 : 바르게 행동하기, Right action||
      |&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; : To **L**ove - Social||意 - 正命 : 바르게 생활하기, Right livelihood||
      |지(知識ㆍ智慧) : To **L**earn|Do : 定(감정) → 집중|正念 : 바르게 깨어 있기, Right mindfulness||
      |||正定 : 바르게 집중(삼매)하기, Right concentration||
      ||Plan: 慧 → 眼斷|正見 : 바르게 보기, Right view||
      |||正思惟ㆍ正思 : 바르게 생각하기, Right resolve||
      |率先垂範ㆍ貢獻 : To **L**eave a **L**egacy|||공유된 경험의 흔적| 
* 실천 방안
  * 수용ㆍ습득ㆍ실천【To Learn】 → 체화【To Live, To Love and To Leave a Legacy】 
  ```tinymind
  $5L_s$  
    $체(體,戒):~To~Live \\ ~~-~Physical$  
      스트레칭
      맨손 체조
      기공 체조
    $덕(德):~To~Love \\ ~~-~SocialㆍEmotional~Relationships$  
      잔소리 하지 말고 맥을 집기
      설겆이
      한길이와 산책하기
    $지(知識~習得):~To~Learn \\ ~~-~MentalㆍOcupational$  
      읽고 정리하기
        [일반](Readings_General.md)
        [$Data~Science$](DataScience.md)
      단련
        스트레칭
        맨손 체조
        기공 체조
      (불교식) 수행
      처세술
        Stephen Covey
        Spencer Johnson
      재테크, 투자
      [$Data~Science$](DataScience.md)
        활용 도구
          R & Jamovi
          Python
        통계
        머신러닝
        딥러닝
      $Digital~Twin$
    $혜(智慧):~To~Leave~a~Legacy \\ ~~-~Spiritual$  
      $불교식~명상$
  ```
* 다락방
  * 나에게 영향을 준 글들, 책들…
    + 국민학교 2~3학년(큰댁에서) : 불교설화자경문 “사나운 말”
    + 고등학생 : 백범일지
    + 대학생 : 돌베개 (장준하), Song of Ariran(김산(장지락))
    + 20대 후반, 30대
      - 성공하는 사람들의 7가지 습관 (Stephen R. Covey)
      - First Things First(Stephen R. Covey, A. Roger Merrill, Rebecca R. Merrill)
    + 40대 : 반야심경 (틱 낫 한 스님 해설)
  * 좋은 말들 <details><summary>Details</summary><div>
    + William James, 심리학자, 미국 ☞ 『思 → 行 → 習 → 人 → 運』 善循環  
      - 생각(思)이 바뀌면 행동(行)이 바뀌고, (바뀌게 되고)
      - 행동(行)이 바뀌면 습관(習)이 바뀌고,  ( “ )
      - 습관(習)이 바뀌면 인격(人)이 바뀌고,  ( “ )
      - 인격(人)이 바뀌면 운명(運)까지도 바뀐다.   ( “ 된다.)
    + 나태주 『 사랑에 답함 』  
      &nbsp; &nbsp; 예쁘지 않은 것을 예쁘게 보아주는 것이 사랑이다.<Br>&nbsp; &nbsp; 좋지 않은 것을 좋게 생각해 주는 것이 사랑이다.<Br>&nbsp; &nbsp; 싫은 것도 잘 참아 주면서 처음만 그런 것이 아니라,<Br>&nbsp; &nbsp; 나중까지 아주 나중까지 그렇게 하는 것이 사랑이다.
    + 작자 미상  
      &nbsp; &nbsp; 하늘에 있는<Br>&nbsp; &nbsp; 별에 이르지 못하는 것이<Br>&nbsp; &nbsp; 부끄러운 일이 아니라<Br>&nbsp; &nbsp; 도달해야 할<Br>&nbsp; &nbsp; 별이 없는 것이<Br>&nbsp; &nbsp; 부끄러운 일이다.
    + 카일 챈들러  
      &nbsp; &nbsp; 기회는 절대 노크하지 않는다.<Br>&nbsp; &nbsp; 당신이 문을 밀어<Br>&nbsp; &nbsp; 넘어뜨릴 때 비로소<Br>&nbsp; &nbsp; 모습을 드러낸다. <!-- <details><summary>Details</summary><div> 좋은 말들 </div></details> -->
</div></details> <Br> <!-- 책갈피-장기 > Personal > Details -->

<details><summary>책갈피-장기 > Job > Details</summary><div> 

* 회사 인사평가 업무 목표 <details><summary>세부 사항</summary><div>
  |No|업무명|목표|측정 지표|%|일정 계획|
  |:--:|:---|:---|:---|:--:|:---|
  |1<Br><Br>|상위 목표 연계<Br>(품질)|변경관리 프로세스 준수율<Br><Br>|B+ : 준수율 95%<Br>B : 준수율 90%|20<Br><Br>|품질업무 관련 일정에 따름<Br><Br>|
  |2<Br><Br>|상위목표연계<Br>(협업지표)|프로젝트 지원 수행<Br><Br>    |B+ : 일정 준수 & 적시보고<Br>B : 일정 미준수 or 적시보고 누락|20<Br><Br>|한화솔루션/케미칼 SAP 고도화<Br>Planning 프로젝트(2월~5월)|
  |3<Br><Br>|상위목표연계<Br>(협업지표)|프로젝트 지원 수행<Br><Br>    |B+ : 일정 준수 & 적시보고<Br>B : 일정 미준수 or 적시보고 누락|20<Br><Br>|한화솔루션/케미칼 SAP 고도화<Br>(Conversion Project, 21년 하반기 예정)|
  |4<Br><Br><Br><Br><Br><Br><Br>|개인과제<Br><Br><Br><Br><Br><Br><Br>|▣ 선제안 - 한화에너지 뉴스 클리핑<Br>&nbsp; &nbsp; &nbsp; 자동화 및 분석 시스템 구축<Br>&nbsp; - ML / Web Crawling 기반 시스템 구현<Br>&nbsp; - 2020년 PoC 수행 후속 진행 건임<Br><Br><Br><Br>|A : 1.5억 & B+<Br>B+ : 구축 완료 또는 제안 완료<Br>B : 미수행<Br><Br><Br><Br><Br>|20<Br><Br><Br><Br><Br><Br><Br>|[~2월]<Br>&nbsp; - PoC 수행 완료<Br>[2~4월]&nbsp; - AWS 서버 환경 구축(클라우드 사업팀 지원)<Br>&nbsp; - 다중 사용자 환경 구축 및 자동 메일링 기능 구현<Br>[5~6월]&nbsp; - Machine Learning 기반 뉴스 데이터 분석 및 UI 구현<Br>[7~10월]&nbsp; - 기능 수정 및 보완<Br>[11월~]&nbsp; - 고객사 제안|
  |5<Br><Br><Br><Br><Br><Br><Br><Br>|개인과제<Br><Br><Br><Br><Br><Br><Br><Br>|▣ 선제안 - SAP ML 활용<Br>☞ 예: 적정 재고 산출,<Br>&nbsp; &nbsp; Early Warning,<Br>&nbsp; &nbsp; 납품일 예측 등 (항목 미정)<Br>&nbsp; - SAP HANA에서 제공하는<Br>&nbsp; &nbsp; ML 활용 기능을 B/M 대상으로 참조 구현<Br><Br><Br>|A : 1.5억 & B+<Br>B+ : 구축 완료 또는 제안 완료<Br>B : 미수행<Br><Br><Br><Br><Br><Br>|20<Br><Br><Br><Br><Br><Br><Br><Br>|1분기 - 역량 확보<Br>&nbsp; &nbsp; ☞ On/Offline 교육 수강 및 자체 습득 노력<Br>2분기 - 역량 확보<Br>&nbsp; &nbsp; ☞ 1분기 지속 + 주요 패키지 tutorial & guide 숙지<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;- 항목 발굴 : SAP 사례, 고객 운영 시 인터뷰 등 참조<Br>3분기 - 가능 항목에 대한 실제 구현<Br>&nbsp; &nbsp; ☞ Test 구현 후 실Data로 PoC 구현<Br>4분기 - PoC 프로토타입 수행 결과 고객 제안| </div></details>
* https://open.sap.com/courses
  + [s4h18](https://open.sap.com/courses/s4h18) : How to Deliver a Great User Experience with SAP S/4HANA 
* 선후행 과정 연계가 잘 되어 있는 [Learning Journeys](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE/2020/en-US?task=learn_task)의 [SAP Activate](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/5001ff287a26101484fbc62f9283839d.html) 학습 실행 ☞ 가입 필요? [SAP Learning Hub](https://learninghub.sap.com/)
  + 검색어 'Activate' ☞ SAP S/4HANA - Implementation Tools and Methodology ( [SAP Activate](https://help.sap.com/doc/221f8f84afef43d29ad37ef2af0c4adf/HP_2.0/en-US/5001ff287a26101484fbc62f9283839d.html) ) ☞ YouTube [Overview](https://www.youtube.com/watch?v=L2LGdK_2Feg)
    - Start with an overview
      - openSAP Course [s4h19](https://open.sap.com/courses/s4h19) Guide Your SAP S/4HANA Project to Success ☞ [s4h19-1](https://open.sap.com/courses/s4h19-1) <details><summary>실행 내역</summary><div>
        - General documentation to access a CAL(Cloud Appliance Library) system / Cost Management
          - What is SAP Cloud Appliance Library? [YouTube 동영상](https://www.youtube.com/watch?v=PZIKgMat8Fw) @ https://cal.sap.com/ 
          - Access to Hands-on Landscape for course participants [URL](https://open.sap.com/pages/openSAP_General_System_Access_Documentation?tracking_course_id=4242011a-b2c7-4e92-9c4e-e47285f115ec&tracking_id=e5ff8367-d807-4661-9e59-198637aee555&tracking_type=rich_text_item_link&url=https%3A%2F%2Fopen.sap.com%2Fpages%2FopenSAP_General_System_Access_Documentation)
        - S-User ID 또는 S-ID : 한화솔루션/케미칼 S0023118924
        - Information about CAL and link to the system
          - CAL(Cloud Appliance Library) allows you to convert an SAP ERP 6.0 EHP6 SPS03 system to SAP S/4HANA 1909 FPS01.
          - Follow the steps described in the hands-on materials referenced in the Getting Started Guide.
          - After accessing the CAL system, please read the “Welcome to the SAP S/4HANA system conversion landscape” page carefully.
          - Access to CAL : System Conversion Landscape SAP ERP to SAP S/4HANA [URL1](https://open.sap.com/go/link?url=https%3A%2F%2Fcal.sap.com%2Fsubscription%3Fsguid%3D0338bff7-e1c2-4a97-8099-37a22ce4308a&checksum=b67fab0&tracking_type=rich_text_item_link&tracking_id=45626188-68e4-4bd5-beee-0bca5e201e9b&tracking_course_id=4242011a-b2c7-4e92-9c4e-e47285f115ec) → 접속 잘 안되면.. [URL2](https://open.sap.com/go/link?url=https%3A%2F%2Fcal.sap.com%2Fsubscription%3Fsguid%3D0338bff7-e1c2-4a97-8099-37a22ce4308a&checksum=b67fab0&tracking_type=rich_text_item_link&tracking_id=45626188-68e4-4bd5-beee-0bca5e201e9b&tracking_course_id=4242011a-b2c7-4e92-9c4e-e47285f115ec)
        - CAL System Conversion Material, 최초 접속 시 [900MB 내려받기](https://d.dam.sap.com/s/p/a/x7YNGC7) @ SAP Digital [Library](https://dam.sap.com)
        - Unit 1: First Steps when Moving to SAP S/4HANA
          - 20쪽, What can be done today to prepare for a project? : BSR(Business Scenario Recommendations)
          - 22쪽, more info : Blogs tagged **[S/4HANA RIG](https://blogs.sap.com/tag/s4hana-rig)**, [Fiori Wiki](https://wiki.scn.sap.com/wiki/display/Fiori/SAP+Fiori+for+S4HANA)
        - Unit 2: SAP S/4HANA – Finance Essentials ☞ 적용 대상 Notes와 변화 개괄 소개  
        - Unit 3: Steps to Business Partner and Customer Vendor Integration (CVI)  
          ☞ 단계, 도구(예: CVI_Migration_PreChk, BP_CVI_IMG_CHK, CVI_Cockpit)와 Report 소개
        - Unit 4: Logistics Essentials and Changes in SAP S/4HANA
        - Unit 5: Enriching SAP S/4HANA with New Logistics Features
          - [SAP BPs Explorer](https://rapid.sap.com/bp/]), [Model Company](https://rapid.sap.com/bp/#/browse/categories/sap_model_company)
          - What is the difference between SAP Best Practices and an SAP Model Company? [Blog](https://blogs.sap.com/2019/06/03/what-is-the-difference-between-sap-best-practices-and-sap-model-companies/), [Solution Builder](https://help.sap.com/viewer/S4HANA2020_AdminGuide/17d958a88d244ee293aed687f9bfe37f.html)
        - Unit 6: Moving to SAP S/4HANA – Technical Considerations and Guidance
          - Tools : SAP Transformation Navigator [URL](https://go.support.sap.com/transformationnavigator/#/welcome), Roadmap Viewer [URL](https://go.support.sap.com/roadmapviewer/#), Readiness Check 2.0 [URL](https://help.sap.com/viewer/product/SAP_READINESS_CHECK)
          - Companions for your SAP S/4HANA Journey 
            - New Implementation : Improved Data Migration with SAP S/4HANA Migration Cockpit, Reduced Integration Efforts
            - System Conversion &nbsp;: Data Volume Management → Maintenance Planner → Custom Code → Simplification Check → Upgrade Depedency Analyzer
            - cf) Simplification List
          - SAP Fiori Landscape Deployment Options ☞ [Recommendations](https://www.sap.com/documents/2018/02/f0148939-f27c-0010-82c7-eda71af511fa.html)
          - Custom Code Remediation Process for SAP S/4HANA ☞ [Custom Code Adaptation Process](https://blogs.sap.com/2017/02/15/sap-s4hana-system-conversion-custom-code-adaptation-process/)
            - Custom Code Scoping : T-Code SCMON, SUSG
            - Set up and run the ATC(ABAP test cockpit) to scan custom code and check for SAP S/4HANA-related changes.
            - Use ADT(ABAP Development Tools) to adapt custom code to ensure it works in SAP S/4HANA.
          - Downtime-optimized DMO Procedure
        - Unit 7: Transforming Your SAP User Experience with SAP Fiori
          - 의견 : "[s4h18](https://open.sap.com/courses/s4h18) How to Deliver a Great User Experience with SAP S/4HANA" 추천
        - Unit 8: Reporting and Analytics – Starting the Journey
          - Embeded Analytics 사례
            - Smart BUsiness KPIs, Overview Pages, Analytical List Page
            - In-App Analytics and ML, Multidimensional Reports, Dashboards
            - Manage KPIs and Reports, View Browser, Custom CDS Views
            - Custom Analytical Queries, Manage Date Functions, Predictive ML Scenarios
          - 14쪽 : Given embedded analytics, do I still need an EDW system?
          - 17쪽 : Blog URL Link 
          - 문제 : BW Extractors currently used in SAP ERP may no longer be supported in SAP S/4HANA.
        - Unit 9: Making the Intelligent Enterprise a Reality
        - Unit 10: SAP S/4HANA Innovation Examples in Action : Demo [7쪽 - Sales RPA](https://www.youtube.com/watch?v=AV_BLAjWgTs)
          - 10쪽 : ML Implementation in SAP S/4HANA ( [검색](https://rapid.sap.com) ) 
            - $\boxed{Idea} \rightarrow \boxed{Search} \rightarrow \boxed{Adopt/Config} \rightarrow \boxed{Train} \rightarrow \boxed{Consume}$  
              【생각】 Come up with a Use Case Idea  
              【검색】 Existing ML for Use Case  
              【적용】 Model Adaption and Configuration  
              【훈련】 Train Use Case's ML Model  
              【사용】 Consume ML-enabled SAP Fiori Application  
          - 12쪽 : PAI(Predictive Analytics Integrator) ☞ 1909에서 한 번 실행해 볼 것 
            - Monitor Purchase Order Items [F2358](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F2358')/S19OP) 실행
            - Predictive Models **F????** ☞ cf. Predictive Scenarios [F2033](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F2033')/S19OP), Configure the Consumption of Predictive Models [F1837](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F1837')/S19OP)
              - Catalog APPL_MM_PUR_DLVPRED_ML, Predictive Scenario SUPLRDELIVPREDICT, Description Supplier Delivery Prediction
              - "Ready"인 상태 -> Retrain (버전 생성) -> Activate -> "Active" 상태
            - Monitor Purchase Order Items [F2358](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F2358')/S19OP) 재실행 : 결과 "Predict Delivery Date" 활성화 안 됨 <!-- </div></details>  "실행 내역" 끝 -->
    - Become competent
      - Implementation Methodology (Cloud and On Premise)
        - ACT100 : SAP Activate Methodology
        - ACT200 : Agile Project Delivery
        - C_ACTIVATE : SAP Activate Project Manager
      - Implementation Tools
        - E2E600 : Implementation Projects with SAP Solution Manager 7.2
        - E2E220 : Test Management Overview
    - Stay Current
      - S4H2020SCOPE : SAP S/4HANA 2020 for Scope, Innovationand Technical Highlights - Stay Current
    - Expand your skills
      - Focused Build for SAP Solution Manager
        - WSMFB : Focused Build for SAP Solution Manager
      - SAP S/4HANA - System Conversion and Data Migration
        - openSAP Course [s4h11-1](https://open.sap.com/courses/s4h11-1) System Conversion to SAP S/4HANA (Repeat)
        - openSAP Course [s4h14-1](https://open.sap.com/courses/s4h14-1) Key Technical Topics in a System Conversion to SAP S/4HANA (Repeat)
        - openSAP Course [s4h15-1](https://open.sap.com/courses/s4h15-1) Key Functional Topics in a System Conversion to SAP S/4HANA (Repeat)
        - openSAP Course [s4h16](https://open.sap.com/courses/s4h16) Migrating Your Business Data to SAP S/4HANA – New Implementation Scenario
        - s4d445 : Data Migration Using The SAP S/4HANAMigration Cockpit
  + Design Thinking and Business Model Innovation - Methodology and Tools
  + 검색어 'conversion' → Software Lifecycle Management Tools
</div></details> <Br>
</div></details> <!-- 책갈피-장기 > Job > Details -->

### 1.1.2 단기
<details><summary> Details - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</summary><div>

※ 참고 : [오늘](#오늘의-일정), [향후 일정](#12-향후-일정), [과거 이력](#13-과거-이력), [책갈피-장기](#111-장기), [책갈피-단기](#112-단기), [책갈피-이력](#113-이력), [2. DS정리](#2-데이터-과학-정리), [3. Links](#3-useful-links)  

* SAP Embedded Analytics에 대한 Web Resources 조사 : Web, YouTube, ...
* SAP [TechEd](https://pages.sapteched.com/) 2020 (id/pwd : `wellorg@hanmail.net` / 2019 흔히 쓰는 것) ☞ 소개 [Blog](https://blogs.sap.com/2021/01/21/sap-community-welcomes-sap-teched/), [SCN](https://community.sap.com/topics/teched-in-2020)
  + Track: Digital Transformation with Intelligent ERP
    - Subtrack: (DT) How to move to SAP S/4HANA​
      - 참고 : Free Tools to Support a Move to SAP S/4HANA [CM101](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/16037323007010014MzZ)
      - Paths for Transitioning to SAP S/4HANA, [DT100](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555755681001uqlQ) Lecture [YouTube](https://www.youtube.com/watch?v=I9zs9C881Vo)
        - 12쪽 : SCN [Blog ★](https://blogs.sap.com/2016/11/02/sap-s4hana-system-conversion-at-a-glance/) <font color='gold'>**SAP S/4HANA System Conversion – At a glance**</font> vs. <font color='gold'>**Conversion Guide 2020**</font> [pdf](https://help.sap.com/doc/2b87656c4eee4284a5eb8976c0fe88fc/2020/en-US/CONV_OP2020.pdf)
        - 13쪽 : SAP S/4HANA Conversion Project - An Overview of a conversion project and the key tools
        - 31쪽 : More Information (TechEd Sessions), 35쪽 : Transition to SAP S/4HANA Roadmap, 38쪽 이후 : Additional Resources
      - Expert Q&A on Your Transition Path to SAP S/4HANA, DT921, DT922
      - System Conversion (Part 1) – Get Your Road Map to SAP S/4HANA, [DT101](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555755744001uI3s) Lecture
      - System Conversion (Part 2) – Latest News for Experts, DT102 Lecture (Expert) [DT102](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555755808001uc8n)
      - Reduce Downtime for a System Conversion to SAP S/4HANA, [DT103](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555755870001uWzC) Lecture (Advanced)
      - Custom Code Adaptation for SAP S/4HANA, [DT104](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555755937001umSF) Lecture, [DT125](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602217241381001Khul) Breakout <font color='gold'>**Demo**</font>
        - DT104 Blog [① Process](https://blogs.sap.com/2017/02/15/sap-s4hana-system-conversion-custom-code-adaptation-process/), [② ATC](https://blogs.sap.com/2016/12/12/remote-code-analysis-in-atc-one-central-check-system-for-multiple-systems-on-various-releases/), [③ Fiori App](https://blogs.sap.com/2019/02/27/custom-code-analysis-for-sap-s4hana-with-sap-fiori-app-custom-code-migration/), [④ Semi-Auto](https://blogs.sap.com/2018/10/02/semi-automatic-custom-code-adaptation-after-sap-s4hana-system-conversion/), [⑤ ADT Quick Fixes](https://blogs.sap.com/2020/05/18/comments-for-the-adt-quick-fixes/)
        - DT104 16쪽 : Custom Code Analysis Options 3가지
        - SAP SCN **[ABAP Testing and Analysis](https://community.sap.com/topics/abap-testing-analysis)**
        - ABAP Strategy [DEV200](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555753134001up73), ABAP Roadmap [DEV825](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555755095001u6im)
      - 참고 : Using SAP S/4HANA Migration Cockpit for a New Implementation, DT105 Lecture
      - Future-Proof Your Extensibility Strategy Across SAP Solutions in 2021, [ST104](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1603382155119001uS7o) Strategy Talk
      - Deliver End-to-End Intelligent Business Processes with SAP S/4HANA, [ST105](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1603382155221001uXgu) Strategy Talk
      - SAP S/4HANA Movement – New Tools and Features for System Conversions, [DT114](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555756576001uieM) Lecture
      - Operating SAP S/4HANA with Hyperscalers, [DT117](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555756762001usHh) Lecture
      - Data Volume Management in SAP S/4HANA – Tools and Customer Experiences, [DT127](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602217241549001KnCJ) Breakout <font color='gold'>**Demo**</font>
      - Moving from SAP ERP on Premise to SAP S/4HANA in Microsoft Azure, [DT128](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555757372001ujrU) Lecture
      - SAP Customer Geberit’s Journey to SAP S/4HANA, [DT129](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1603382152867001ueXH) Breakout Demo
      - Move to SAP S/4HANA Faster with Intelligent Testing from Tricentis and SAP, [DT130](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1603382152967001uCRe) Breakout <font color='gold'>**Demo**</font>
      - Explore How Siemens Is Implementing New Finance Processes with SAP S/4HANA, [DT131](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1603834511546001vmc2) Lecture (Advanced)
      - News in Table Management for SAP S/4HANA, [DT200](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602217241741001KgNR) Breakout <font color='gold'>**Demo**</font> (Advanced)
        - 11쪽 : Inverted Individual Indexes - SAP Note [2600076](https://launchpad.support.sap.com/#/notes/2600076), [Perf. Guide](https://help.sap.com/viewer/9de0171a6027400bb3b9bee385222eff/2.0.05/en-US/b40bea1feb934ae78bd8bb267505b004.html), What's New [Data Tiering](https://event.on24.com/eventRegistration/EventLobbyServlet?target=reg20.jsp&referrer=&eventid=2427836&sessionid=1&key=4AAFD3A3D369650123640A433A1B4C27&regTag=1152343&sourcepage=register)
      - SAP S/4HANA Lessons Learned: Best Practices Migrating Your Security Concept, [DT207](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1603382153067001uDx4) Breakout <font color='gold'>**Demo**</font> (Advanced)
      - Moving to SAP S/4HANA with Process Intelligence and Connective Automation, [DT210](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1603723813491001mGQ5) Breakout <font color='gold'>**Demo**</font> (Advanced)
      - SAP Fiori for SAP S/4HANA – Rapid Activation and Content Management, [DT267](https://events.sapteched.com/widget/sap/sapteched2020/Catalog/session/1602555757968001uF8o) on-Demand Workshop (Advanced), [Github](https://github.com/SAP-samples/teched2020-DT267), [YouTube 참조](https://www.youtube.com/watch?v=GR8Ek6-ppmY&list=PLI96yWErnX_qBy3iwcozXzeNGF-zPxX9L)
      - Road Map: SAP S/4HANA, DT809 Road Map
  + YouTube 동영상 : 검색어 "SAP TechEd 2020 System Conversion to SAP S/4HANA"
    - 20200602 Paths for Transitioning to SAP S/4HANA, [SAP TechEd Lecture](https://www.youtube.com/watch?v=a5rf056EuJs)
    - 20201215 System Conversion – Get Your Road Map to SAP S/4HANA | SAP TechEd in 2020 [Part 1](https://www.youtube.com/watch?v=iaM6w9GDr38), [Part 2](https://www.youtube.com/watch?v=0AmQ1mbVIY0)
    - 20200518 System Conversion to SAP S/4HANA SAP TechEd Lecture [Part 1](https://www.youtube.com/watch?v=X78G2n5ttR0), [Part 2](https://www.youtube.com/watch?v=2WVQVUuQX04), [참고](https://www.youtube.com/watch?v=LT-y8bwLMPI)
    - SAP Readiness Check 2.0 for SAP S/4HANA Conversion [Live Demo](https://www.youtube.com/watch?v=-A66NASBxEk), SAP TechEd Lecture 
    - SAP S/4HANA - Custom Code Adaptation [Live Demo](https://www.youtube.com/watch?v=mtCFB4_Lgto), SAP TechEd Lecture
    - Optimize Your Custom ABAP Code for SAP HANA, [SAP TechEd Lecture](https://www.youtube.com/watch?v=S2Fx_mcTIO8)
    - SAP S/4HANA Migration Cockpit for a New SAP S/4HANA Implementation [LIVE DEMO](https://www.youtube.com/watch?v=eHyR5BgP_qM), SAP TechEd Lecture
    - Transitioning from ABAP Programmer to Developer | SAP TechEd in 2020 [URL](https://www.youtube.com/watch?v=UJIN0hIpEX4)
    - 20210519 Learn how to use SAP Screen Personas | SAP TechEd in 2020 [URL](https://www.youtube.com/watch?v=gkrd-xQIfmM)
  + System Conversion to SAP S/4HANA 검토
    - (SCN [Blog](https://blogs.sap.com/2016/11/02/sap-s4hana-system-conversion-at-a-glance/) Conversion at a Glance → ) SCN [Blog ★](https://blogs.sap.com/2021/03/30/sap-s-4hana-2020-system-conversion-steps-details-how-to-be-prepared/) 2021-03-30 Conversion Steps & Details vs. <font color='gold'>**Conversion Guide 2020**</font> [pdf](https://help.sap.com/doc/2b87656c4eee4284a5eb8976c0fe88fc/2020/en-US/CONV_OP2020.pdf)
  + BSG Fiori 전문가 참석 회의(6/1, 15시) 대비 Fiori 검토 (Resource 검색, 정리ㆍ요약)
    - openSAP 'fiori' course 검색(아래 [`3 > 3.2 SAP`의 openSAP fiori 관련 과정](#32-sap) 참조) : fiori3 → s/4h18
      - https://ui5.sap.com ; SCN [Fiori](https://community.sap.com/topics/fiori), [Fiori Wiki Home](https://wiki.scn.sap.com/wiki/display/Fiori/SAP+Fiori+Home) ; **<font color='gold'>Fiori Design Guidelines</font>** [URL](https://experience.sap.com/fiori-design-web/sap-fiori)
      - SCN [Blog](https://blogs.sap.com/2019/05/25/get-ready-for-sap-fiori-3/) Get Ready for SAP Fiori 3
    - SAP [TechEd](https://pages.sapteched.com/) 2020 'fiori' session 검색 : 37 Sessions  
      |Ser. No|Session Desc. (ID 오름차순 정렬)|ID|Level|Time|
      |:--:|:---|:--:|:--:|:--:|
      |1|Uniper using SAP Cloud Platform for Integration Scenarios with SAP ERP |ANA122|Beginner||
      |2|Simplified Account and Rewards Management |CT107|N/A||
      |3|Major Updates on ABAP RESTful Application Programming Model |DEV102|Advanced||
      |4|SAPUI5 – All You Need to Know |DEV108|Beginner||
      |5|Central Workflow Inbox as a Key Intelligent Enterprise Quality |DEV112|Beginner||
      |6|Extend SAP S/4HANA with a Custom UI on SAP Cloud Platform |DEV161|Beginner||
      |7|Recommendations for Building a Central Entry Point on SAP Cloud Platform |DEV211|Advanced||
      |8|Build SAP Fiori Apps with the ABAP RESTful Application Programming Model |DEV260|Advanced||
      |9|Automated SAP Fiori Apps Testing with Continuous Delivery |DEV267|Advanced||
      |10|Road Map: SAPUI5 |DEV804|Beginner||
      |11|Custom Code Adaptation for SAP S/4HANA |DT104|Beginner||
      |12|Using SAP S/4HANA Migration Cockpit for a New SAP S/4HANA Implementation |DT105|Beginner||
      |13|Custom Code Adaptation for SAP S/4HANA |DT125|Beginner||
      |14|Vistaprint: Automating Agile Transformation and SAP S/4HANA Transition |DT132|Beginner||
      |15|SAP S/4HANA Lessons Learned: Best Practices Migrating Your Security Concept |DT207|Advanced||
      |16|SAP Fiori for SAP S/4HANA – Rapid Activation and Content Management |DT267|Advanced||
      |17|Road Map: SAP S/4HANA |DT809|Beginner||
      |18|SAP Fiori Launchpad: What's Hot and What's New |IIS102|Beginner||
      |19|Beyond SAPUI5 and SAP Fiori Elements |IIS114|Beginner||
      |20|The Future of Mobile Work |IIS126|Beginner||
      |21|SAP Fiori 3: SAP's Consistent, Integrated, and Intelligent UX |IIS128|Beginner||
      |22|Learn About SSO and MFA and Their Effect on User Productivity |IIS133|Beginner||
      |23|Bring the Full SAP Fiori User Experience to Your Screens in SAP GUI |IIS201|Advanced||
      |24|Modernize SAP Fiori App Development Using SAP Fiori Tools |IIS204|Advanced||
      |25|Yorkshire Water Uses SAP Fiori Elements to Build SAP Fiori Apps Quickly |IIS208|Advanced||
      |26|Design-Led Development at SAP: How to Meet the Needs of Your Users |IIS261|Beginner||
      |27|Implement SAP Fiori Efficiently for SAP S/4HANA |IIS268|Advanced||
      |28|Simplify Development of SAP Fiori Apps with OData v4 |IIS360|Expert||
      |29|Create Analytical SAP Fiori Apps Quickly and Efficiently |IIS361|Expert||
      |30|Classify and Extract Business Document Information |INT166|Beginner||
      |31|Implement and Run Business Scenarios at the Edge Using SAP Edge Services |INT167|Beginner||
      |32|Industry Cloud Innovations for a New World of Retail and Consumer Products |PAR837|Beginner||
      |33|Taking Integration to the Next Level: Update on SAP’s Integration Strategy |ST106|Beginner||
      |34|Create a Future-Proof User Experience for Your Intelligent Enterprise |ST110|Beginner||
</div></details> <Br>

### 1.1.3 이력
<details><summary> Details - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</summary><div>

※ 참고 : [오늘](#오늘의-일정), [향후 일정](#12-향후-일정), [과거 이력](#13-과거-이력), [책갈피-장기](#111-장기), [책갈피-단기](#112-단기), [책갈피-이력](#113-이력), [2. DS정리](#2-데이터-과학-정리), [3. Links](#3-useful-links)  

</div></details>

</div></details> <Br>

## 1.2 향후 일정
<details><summary> Details ────────────────────────────────────────────────────</summary><div>

※ 참고 : [오늘](#오늘의-일정), [향후 일정](#12-향후-일정), [과거 이력](#13-과거-이력), [책갈피-장기](#111-장기), [책갈피-단기](#112-단기), [책갈피-이력](#113-이력), [2. DS정리](#2-데이터-과학-정리), [3. Links](#3-useful-links)  

▣ 2021-06-15, 화
* openSAP 과정 시작
  + 20210615-20210804 [ds3](https://open.sap.com/courses/ds3) Getting Started with Data Science (Edition 2021)

▣ 2021-06-16, 수
* openSAP 과정 시작
  + 20210616-20210722 [s4h19-1](https://open.sap.com/courses/s4h19-1) Guide Your SAP S/4HANA Project to Success (Repeat)
* 회의 일정
  + **<font color='gold'>SAPPHIRE NOW Korea</font> Supply Chain** Webinar 참석 : 오전 9시 (id/pwd : phs20210526 / sapphire20210616)

▣ 2021-06-17, 목
* 회의 일정
  + 한화 장교빌딩 4층 RM410, 오후 2시~4시, SAP Korea 이정현 상무, Tricentis 설명회

▣ 2021-06-22, 화
* 회사 교육 : 데이터 분석 입문 II 2차수

▣ 2021-06-23, 수
* 한화솔루션/케미칼 SAP 고도화 Planning 프로젝트 종료

▣ 2021-06-24, 목
* [AI·DX SUMMIT KOREA 2021, 6/24 목 오전10시](https://conference.etnews.com/)

▣ 2021-06-25, 금
* 프로젝트 공수 입력

</div></details> <Br>

## 1.3 과거 이력
<details><summary> Details ────────────────────────────────────────────────────</summary><div>

※ 참고 : [오늘](#오늘의-일정), [향후 일정](#12-향후-일정), [과거 이력](#13-과거-이력), [책갈피-장기](#111-장기), [책갈피-단기](#112-단기), [책갈피-이력](#113-이력), [2. DS정리](#2-데이터-과학-정리), [3. Links](#3-useful-links)  

▣ 2021-06-15, 화  
* Job, Q2 Task : Orange Data Mining [url](https://orangedatamining.com/), [Wiki](https://en.wikipedia.org/wiki/Orange_(software)) : ODM [Doc](https://orangedatamining.com/docs/) > Python Library [Tutorial](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/#tutorial) > "[Data](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/data.html "Tutorial > Data") 【$\oplus$, 6/14】, [Classification](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/classification.html "Tutorial > Classification") & [Regression](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/regression.html "Tutorial > Regression") 【$\oplus$, 6/15】"

▣ 2021-06-14, 월  
* 회사 업무
  + 한화솔루션/케미칼 SAP 고도화 Planning Project > 금주에는 SCM 개선과제 상세 내역 살펴보기 【$\ominus$】
* Job, Q2 Task 
  + Orange Data Mining [url](https://orangedatamining.com/), [Wiki](https://en.wikipedia.org/wiki/Orange_(software)) : ODM [Doc](https://orangedatamining.com/docs/) > Python Library [Tutorial](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/#tutorial) > [Data](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/data.html) 【$\oplus$】
  + [sps3](https://open.sap.com/courses/sps3) `Using SAP Screen Personas for Advanced Scenarios` 20210611∼, 훑어보기 진행

▣ 2021-06-11, 금  
* Data Science > VS Code Upgrade to 1.57.0
  - Remote Repositories : [blog post](https://code.visualstudio.com/blogs/2021/06/10/remote-repositories), [YouTube video](https://www.youtube.com/watch?v=wHsmaXoGIXI)
* 회사 업무
  + 게시판 확인
    - [게시글](http://snc.eagleoffice.co.kr/neo/bbs/C/19662/002373280) : ［공지］ 구매3팀 변경 조직도 안내 드립니다.
    - [게시글](http://snc.eagleoffice.co.kr/neo/bbs/C/19662/002373272) : ［재공지］ PC 자료유출 방지 솔루션 적용 안내
    - [게시글](http://snc.eagleoffice.co.kr/neo/bbs/C/19662/002373239) : ［단체상해보험］보험금 청구 양식 변경 안내('21.6.1일자)
  + 한화솔루션/케미칼 SAP 고도화 Planning Project > 차주에는 SCM 개선과제 상세 내역 살펴보기 
   
▣ 2021-06-10, 목  
* Job, Q2 Task : [sps2](https://open.sap.com/courses/sps2) `Introduction to SAP Screen Personas`, 20210607∼20210610, 1회 훑어보기 완료 【$\oplus$】
* 회사 업무 처리
  + `글로벌 어학 프로그램` 수강 신청 【$\oplus$】 ☞ 참조 : 21년 3분기 수강신청 안내 [게시물](http://snc.eagleoffice.co.kr/neo/bbs/C/19662/002373246)
    - 오늘도 동사, 내일도 동사랑♡해요! ［1편］ : 7월부터 [수강](http://apply.imooc.co.kr/start/hanwhasystems), 당근영어 선소화 매니저(02-518-2603) 담당 
  + 통신비 전표 처리 (5월 사용 6월 청구) 【$\oplus$】  @ 회계관리 > 개인경비 > 통신비 > (조건 설정 후) 조회 클릭 > 작성 > 상신
* 회의(권기범 부장) : 한화솔루션/케미칼 SAP 고도화 Planning 프로젝트 업무 협의, 2021-06-09 (수) 13:00∼14:00, 장소 RM430 
  + 과업지시서 작성 【$\oplus$】 : Fiori, MDG
    - Fiori : 공수 산출 부분 추가  【$\oplus$】
    - MDG : 정의준 위원의 "과제정의서" 기반 작성  【$\oplus$】

▣ 2021-06-09, 수  
* Job, Q2 Task : [sps2](https://open.sap.com/courses/sps2), 20210607부터 진행.
* 회사 업무 처리
  + 5월 공수 실적 보고 (장용원 차장님) 【$\oplus$】
* 회의(권기범 부장) : 한화솔루션/케미칼 SAP 고도화 Planning 프로젝트 업무 협의, 오늘(6/9) 13:00∼14:00, 장소 RM430 
  + 과업지시서 작성 : Fiori 부분 1차 완료 및 메일 송부 【$\oplus$】
  + 참조 URL
    - Comparing ABAP Restful Application Programming (RAP) model with the Cloud Application Programming (CAP) model, 2020-10-05, [URL](https://www.nl4b.com/cloud-development/comparing-sap-rap-model-with-sap-cap-model/)
    - A Developer’s Guide to the ABAP RESTful Programming Model [URL](https://www.sapinsideronline.com/a-developers-guide-to-the-abap-restful-programming-model/)
    - CAP, Consume External Service Part [3](https://blogs.sap.com/2020/07/27/cap-consume-external-service-part-3/)
    - SAP Tutorial: Serving Data from an On Premise System in a CAP Java Application - Part [1](https://bnheise.medium.com/sap-tutorial-serving-data-from-an-on-premise-system-in-a-cap-java-application-part-1-2426175ad4fa)
    - YouTubeㆍSAP Developers : SAP HANA Basics for Developers
      - https://www.youtube.com/watch?v=JYxL7MrFAGM
      - https://www.youtube.com/watch?v=zNE2jGSem2M
* 어제 수신 메일 `2021-06-08 112000_권기범_FW SAP Fiori Apps 권장사항 보고서 요청사항의 건.msg`의 첨부 File 3건 검토 <details><summary>Details</summary><div>
  + 코오롱(2018.09) : Standard 기반 은행계좌 정보 화면 사용, Fashion ERP
    - 7쪽, 업무 생산성 향상 조사된 수치
    - 8쪽, 1차 리허설 후 [39](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#?appId=F0348A,F0431,F0752,F1061,F1062,F1240,F1708,F1745,F1749,F1750,F1873,F1957,F1993,F1996,F2058,F2217,F2218,F2449,F2650,F2651,F2652,FAGLL03,FAGLL03H,FBL1N,FBL5N,WSOA2,F0512A,F0735,F1366A,F2092,F2057,F1488,F1243,SP01_SIMPLE,F1063,F1431,F2050,F2258,F1765)건 선정 : [FI 10건](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#?appId=F1745,F1749,F1750,F1993,F2217,F2218,FAGLL03,FAGLL03H,FBL1N,FBL5N), [TR 4건](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#?appId=F0512A,F0735,F1366,F2092), [MM 5건](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#?appId=F0348A,F1061,F1062,F1957,F1996), [SD 8건](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#?appId=F1240,F1708,F1873,F2058,F2650,F2651,F2652,WSOA2), [LE 3건](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#?appId=F0431,F0752,F2449), Alternatives 1건, Dependent Apps 9건
  + 태광(2020.02) : 프로젝트 시 검토를 했으나 최종 사용하지는 않음
    - 7쪽, Fiori App Type : Transactional, Analytical, Factsheet
    - 10쪽, On-Premise에서의 기본적인 SAP Fiori Architecture ☞ 참고 : SAP Help [SADL Models](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/be/cb201641804877bca7c21b619fbc3c/frameset.htm)
    - 11쪽, PFCG, LaunchPad Designer를 통한 권한ㆍ개인화 설정 및 <font color='gold'>**ERD**</font>
    - 20쪽, Fiori LaunchPad 접속 방법 : ① 웹 브라우저를 통한 URL 접속, ② SAP GUI의 T-Code `/n/ui2/flp`를 활용한 접속
  + 두산(2020.06) : Standard 기반 은행계좌 정보 화면 사용
    - 12∼13쪽, Fiori App Setup, Rapid Activation
    - 14∼17쪽, Fiori LaunchPad 활용 : Home, Personalization
    - 12∼13쪽, Fiori App 기능 : 검색 정보 저장, 사용자 타일 저장

▣ 2021-06-08, 화  
* Job, Q2 Task : [sps2](https://open.sap.com/courses/sps2), 20210607부터 진행.
* openSAP 과정 시작
  + 20210608-20210714 [fiori-ea1](https://open.sap.com/courses/fiori-ea1) Developing and Extending SAP Fiori Elements Apps
* 수출입 관련 개선과제 산출물 추가 작성
  + Hibiz에서 조회&출력되는 화면으로서 SAP에서 조회&출력하기를 원하는 화면(Screen Copy)을 산출물로 추가
* 회사교육 `글로벌 어학 프로그램` 조사 : 21년 3분기 수강신청 안내 [게시물](http://snc.eagleoffice.co.kr/neo/bbs/C/19662/002373246) 첨부 Excel File 확인할 것
  + 어학 > 영어 : Communication, Biz English, Biz Skill, Test Preparation

▣ 2021-06-07, 월  
* Job, Q2 Task : [sps2](https://open.sap.com/courses/sps2), 20210607부터 진행. 
* 임대 Notebook PC에 [mBlock](https://www.mblock.cc/) 설치
* BSG Fiori 전문가 참석 회의(6/1, 15-17시, RM413) 후속 처리 : 추가 질문 【$\oplus$】, 산출물 갱신 【$\oplus$】 (타사 fiori 공수 투입 사례 대기중 → 참조할 것 없음)
  + 김경호 과장, Readiness check 결과 6/1 메일 검토 (S/4HANA 2020 SPS01) 【$\ominus$】 (타사 fiori 반영 사례 대기중) ☞ 확인 [URL](https://rc.cfapps.eu10.hana.ondemand.com/comsaprcweb/index.html#)
    - Readiness check 결과 추천 App : 전체 1,828건, **Lighthouse Apps 80**, **Fiori Apps 1,166**, **Classic UI Apps 582**
  + Decompose-Recompose 질문 관련 [Blog](https://blogs.sap.com/2017/04/05/sapui5-how-to-reuse-parts-of-a-sapui5-application-in-othermultiple-sapui5-applications/) - SAPUI5 How To: Reuse parts of a SAPUI5 application in other/multiple SAPUI5 applications
  + 구글 검색 : sap fiori launchpad on enterprise portal ☞ https://securedgateways.com/sap-flp/

▣ 2021-06-04, 금  
* SAP Korea 이정현 상무(jung.hyun.lee@sap.com)께 메일로 내방 및 설명(1. Test 도구 Tricentis, 2. Screen Personas) 요청
* BSG Fiori 전문가 참석 회의(6/1, 화, 15-17시, RM413) 대비 Fiori 검토 (Resource 검색, 정리ㆍ요약)  
  → openSAP Course [fiori3](https://open.sap.com/courses/fiori3) - SAP Fiori Overview: Design, Develop and Deploy `for SAP Fiori Experts` 1회 훑어보기 완료 【$\oplus$】<details><summary>Details</summary><div>
  |구분|내역|완료 일자|비고(내용 요약, 주요 HyperLink)|
  |:--|:--|:--:|:--|
  |Week 1 |SAP Fiori Overview|2021-05-31|SAP [Fiori Apps Reference Library](https://fioriappslibrary.hana.ondemand.com/) (S-ID S0023118924 사용)|
  |&nbsp; &nbsp; Unit 1|Introducing SAP Fiori|2021-05-31||
  |&nbsp; &nbsp; Unit 2|Designing a Great User Experience|2021-05-31|SAP Fiori [Design Guidelines](https://experience.sap.com/fiori-design/) → [Web](https://experience.sap.com/fiori-design-web/sap-fiori)|
  |&nbsp; &nbsp; Unit 3|Architecture Overview|2021-05-31|ㆍ8쪽, UI Compoenets 4가지: LPD, Apps, Elements, UI5|
  |&nbsp; &nbsp; Unit 4|Development Tools Overview|2021-05-31|ASUG [A Practical Guide for Senior IT Leadership](https://www.sap.com/documents/2019/05/44b3ebd5-4b7d-0010-87a3-c30de2ffd8ff.html)|
  |&nbsp; &nbsp; Unit 5|How to Get SAP Fiori Up and Running|2021-05-31|Users who click on a business object link get options for what they intend to do.|
  |Week 2<Br><Br>|Designing SAP Fiori Apps<Br><Br>|2021-06-01<Br><Br>|DLD(Design-Led Development): Discover → Design → Develop<Br>&nbsp; &nbsp; ☞ Scope, Research, Synthesize → Ideate, Prototype, Validate → Implement, Test, Deploy|
  |&nbsp; &nbsp; Unit 1|Why Good Design Matters|2021-05-31|cf: https://open.sap.com/courses?q=design|
  |&nbsp; &nbsp; Unit 2|Exploring the SAP [Fiori Design System](https://experience.sap.com/fiori-design/)|2021-05-31||
  |&nbsp; &nbsp; Unit 3<Br><Br><Br>|Designing with SAP Fiori<Br><Br><Br>|2021-05-31<Br><Br><Br>|Building Blocks : UI Elements, Patterns, Gestures, Colors, Typography, Floorplans,<Br>&nbsp; &nbsp; &nbsp; Dynamic Page, Flexible Column Layout, Layouts, Draft Handling, Edit Flow,<Br>&nbsp; &nbsp; &nbsp; Situation Handling, Message Handling, Notifications, Concepts|
  |&nbsp; &nbsp; Unit 4<Br><Br>|Hands-On Design 1<Br><Br>|2021-05-31<Br><Br>|ㆍUser stories with scenes(= pre-drawn images), Download free at [Toolkit](https://experience.sap.com/designservices/resource/scenes)<Br>ㆍTask Type for your jump start : Routine, Reactive, Monitoring, Analytical, Expert|
  |&nbsp; &nbsp; Unit 5|Hands-On Design 2|2021-05-31|Whiteboard 권장 : 특별한 기술 불필요 → 누구나 큰 노력 없이 사용 가능하며 변경하기 쉽다.|
  |&nbsp; &nbsp; Unit 6<Br><Br>|Best Practices and Tools<Br>for SAP Fiori Design|2021-06-01<Br><Br>|ㆍ10쪽 : [ut1-2](https://open.sap.com/courses/ut1-2) Basics of Design Testing (Edition Q2/2019), [dr1](https://open.sap.com/courses/dr1) Basics of Design Research<Br>ㆍ17쪽 : [Icon Explorer](https://sapui5.hana.ondemand.com/test-resources/sap/m/demokit/iconExplorer/webapp/index.html#/overview/SAP-icons/); UI Theme Designer [URL](https://themedesigner-themedesigner.dispatcher.hanatrial.ondemand.com/index.html), [Help](https://help.sap.com/viewer/8ec2dae34eb44cbbb560be3f9f1592fe/1709.latest/en-US/a118094264684230bb6510045b5b5b7c.html), [SCN](https://community.sap.com/topics/ui-theme-designer), [Theme 설정](https://blogs.sap.com/2019/10/23/sap-fiori-theme-customization/)|
  |Week 3 |Developing SAP Fiori Apps|2021-06-03|[Screen Personas](http://www.sapscreenpersonas.com/) : SCN [Roadmap](https://blogs.sap.com/2020/01/07/sap-screen-personas-roadmap-update-january-2020-accelerating-sap-fiori-adoption/) & [SP12 소개](https://blogs.sap.com/2020/12/14/sap-screen-personas-3.0-sp12-now-available.-sapui5-applets-easier-sap-fiori-launchpad-integration-native-barcode-scanning/) 및 [비교](https://wiki.scn.sap.com/wiki/display/Img/Compare+SAP+Screen+Personas+versions) → openSAP sps[2](https://open.sap.com/courses/sps2), [3](https://open.sap.com/courses/sps3), [4](https://open.sap.com/courses/sps4) → SCN [Topic](https://community.sap.com/topics/screen-personas), [Wiki](https://wiki.scn.sap.com/wiki/display/Img/SAP+Screen+Personas+Product+Support) & [Help Portal](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US)|
  |&nbsp; &nbsp; Unit 1<Br><Br>|Using SAP [Business Application Studio](https://www.sap.com/appstudio)<Br>to Develop SAP Fiori Apps|2021-06-01<Br><Br>|ㆍ11쪽 : Reference URLs<Br><Br>|
  |&nbsp; &nbsp; Unit 2<Br><Br>|Building Modern Web Applications<Br>with [SAPUI5](https://sapui5.hana.ondemand.com/) `=HTML+CSS+JavaScript`|2021-06-01<Br><Br>|ㆍSAPUI5: 5쪽 Portfolio, [환경](https://ui5.sap.com/#/topic/74b59efa0eef48988d3b716bd0ecc933 "SAP UI5 Browser and Platform Support"), <font color='gold'>★</font>[Demo Apps](https://ui5.sap.com/#/demoapps), <font color='gold'>★</font>[Web Components](https://sap.github.io/ui5-webcomponents/ "16쪽, UI5 Web technology brings scalability and flexibility to SAP Fiori app development; React, Angular, or Vue와 같은 것들은 SAP UI5 Web Components를 사용할 수 있다"), [Card Explorer](https://ui5.sap.com/#/tools), [Dev](https://developers.sap.com/topics/ui5.html), [SCN](https://community.sap.com/topics/ui5)<Br>ㆍ[OpenUI5](https://openui5.org/): [SDK](https://openui5.hana.ondemand.com/), [Github](https://github.com/SAP/openui5), [YouTube](https://www.youtube.com/c/openui5videos/featured), [Markdown Docs](https://sap.github.io/openui5-docs), [Blog](https://velog.io/@rumblekat/series/OpenUI5), [Wiki](https://en.wikipedia.org/wiki/OpenUI5), 비교 [EN](https://blogs.sap.com/2013/12/11/what-is-openui5-sapui5/) [KO](https://blog.daum.net/rightvoice/984); CSS [KO](https://ko.wikipedia.org/wiki/CSS) [EN](https://en.wikipedia.org/wiki/CSS), wikidocs [JavaScript](https://wikidocs.net/book/5373)|
  |&nbsp; &nbsp; Unit 3<Br><Br>|Accelerating App Development<Br>with SAP Fiori Elements `and metadata`|2021-06-01<Br>2021-06-02|ㆍ5-6쪽 : Page Type(Overview, List Report, Analytical List, Worklist, Object), Standard UI Logic<Br>ㆍ8-13쪽 : Fiori Tools (`MS VS Code Extension` or SAP Biz. Application Studio), 12쪽 Demo|
  |&nbsp; &nbsp; Unit 4<Br><Br><Br>|Developing OData Services<Br>for SAP Fiori Applications<Br>`UI5/Fiori→OData,REST→Model→CDS`|2021-06-02<Br><Br><Br>|ㆍ5~7쪽 : SAP CAP(Cloud Application Programming) Model for Java & JavaScript(Node.js)-*based OData services*<Br>ㆍ9~12쪽 : ABAP RAP(RESTful Application Programming) Model for ABAP-*based OData services*<Br>ㆍ14쪽 : 여기서 다룬 2개의 RESTful Model에 대해, <font color='gold'>**Get Started**</font> Today - [CAP](https://cap.cloud.sap/docs/get-started/); [ABAP](https://community.sap.com/topics/abap) [RAP](https://blogs.sap.com/2019/10/25/getting-started-with-the-abap-restful-programming-model/) [Dev](https://www.sapinsideronline.com/a-developers-guide-to-the-abap-restful-programming-model/), [ABAP](https://community.sap.com/topics/abap) [CDS](https://blogs.sap.com/2016/02/01/getting-started-with-abap-core-data-services/)|
  |&nbsp; &nbsp; Unit 5<Br><Br>|Simplifying Classic Transaction Screens<Br>with SAP [Screen Personas](http://www.sapscreenpersonas.com/) ☞ [Flavor Gallery](http://link.personas.help/SAPScreenPersonasFlavorGallery)|2021-06-03<Br><Br>|ㆍ10쪽 : Choose a Path to the SAP Fiori User Experience ☞ 비교 [①](https://www.fingent.com/blog/top-3-ui-offerings-from-sap-fiori-screen-personas-and-lumira/) [② 3.0 SP06, Slipstream Engine](https://www.avelon.be/news-blog/sap-screen-personas-versus-fiori) [③ 사용 소감](https://www.linkedin.com/pulse/sap-ux-grand-unification-theory-how-screen-personas-sp06-dan-barton) <font color='gold'>★</font><Br>ㆍ11쪽 : SAP [Screen Personas](https://help.sap.com/viewer/20993a0c28654a26beb2b63b722d74f2/Current/en-US/0036f15101d9445ee10000000a423f68.html) > [구축 고려 사항](https://help.sap.com/viewer/9db44532734f4718b91e460c020307fe/Current/en-US "SAP Help Portal, Implementation Considerations"), 3.0 [Guide](https://blogs.sap.com/2020/06/16/managing-sapui5-dependencies-in-sap-screen-personas-new-guide-available/) SP12 [①](https://blogs.sap.com/2020/12/14/sap-screen-personas-3.0-sp12-now-available.-sapui5-applets-easier-sap-fiori-launchpad-integration-native-barcode-scanning/ "Peter Spielvogel, 2020-12-14") [②](https://www.youtube.com/playlist?list=PLo17W6sWsxWMMli_i5rCCChLbYstVmMpF "YouTube, Productivity Power Play 목록"), 오늘 시작 ([Help Q&A](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US); [SCN](https://community.sap.com/topics/screen-personas) [문의](https://answers.sap.com/questions/ask.html?primaryTagId=67838200100800005412); Add-on)|
  |&nbsp; &nbsp; Unit 6|Building iOS Apps|2021-06-03||
  |&nbsp; &nbsp; Unit 7<Br><Br>|Creating Android Apps Natively<Br>or with the Mobile Development Kit|2021-06-03<Br><Br>|ㆍ10쪽 : Mobile Development Kit = Low Code + Fiori Designs + Enterprise Mobility<Br><Br>|
  |Week 4 |Managing SAP Fiori|2021-06-04||
  |&nbsp; &nbsp; Unit 1<Br><Br>|Understanding SAP Fiori Content<Br><Br>|2021-06-04<Br><Br>|ㆍ3쪽 : [SAP Fiori deployment options](https://www.sap.com/documents/2018/02/f0148939-f27c-0010-82c7-eda71af511fa.html "SAP Fiori Deployment Options and System Landscape Recommendations")<Br>ㆍ6∼9쪽 : FLP content entries → Tiles/Links, Target Mappings, Catalogs, Gourps, Roles(PFCG) + intent(8쪽)|
  |&nbsp; &nbsp; Unit 2<Br><Br><Br>|Activating SAP Fiori Out-of-the-Box<Br>ㆍ3∼4쪽 : Biz Role Template, Role 찾기 @ [Lib](https://www.sap.com/fiori-apps-library)<Br>ㆍ6쪽 : [ⓒ Mgr](https://help.sap.com/viewer/d4650bf68a9f4f67a1fda673f09926a9/753.04/en-US) Demo, 7쪽 : Tools & Links : [ⓣ](https://blogs.sap.com/2019/03/16/fiori-for-s4hana-new-rapid-content-activation-on-s4hana-1809-1709-part-1-overview/)|2021-06-04<Br><Br><Br>|$\small \begin{matrix} \text{Initial~Scoping} \\ 관련~ⓡ~선택(Lib) \end{matrix} \rightarrow \begin{matrix} \text{Sandbox} \\ 빠른~ⓕ~활성화(ⓣ~실행) \end{matrix} \rightarrow \begin{matrix} \text{Fit/Gap Analysis} \\ \text{SAP~Fiori~경험} \end{matrix} \rightarrow \begin{matrix} \text{구축~:~ⓒ~및~ⓡ~조정} \\ ⓒ~Mgr + ⓣ~Cⓒ~활성화 \end{matrix}$<Br>☞ 5쪽 참조 : ⓡ : Role, Lib : Fiori App [Reference Library](https://www.sap.com/fiori-apps-library),  ⓒ : FLP Content, Cⓒ : Customer Content,  [ⓣ Task List](https://blogs.sap.com/2019/03/16/fiori-for-s4hana-new-rapid-content-activation-on-s4hana-1809-1709-part-1-overview/)|
  |&nbsp; &nbsp; Unit 3<Br><Br><Br><Br><Br>|Configuring SAP Fiori Launchpad<Br>ㆍ3쪽 : Managing Scope (= CONF + CUST)<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; when creating custom FLP content<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - scope CONF : client-independent<Br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - scope CUST : client-dependent|2021-06-04<Br><Br><Br><Br><Br>|ㆍ2∼4쪽 : $\scriptsize \boxed{\text{App}} \xleftarrow{refer} \boxed{\boxed{\text{Target~Mapping}} ~~ \text{Tech~Catalog}} \xleftarrow{refer} \boxed{\boxed{\text{Target~Mapping}} ~~ \text{Biz~Catalog}} \xrightarrow{assign} \boxed{\text{Roles}} \xrightarrow{assign} \boxed{\text{User}}$<Br>ㆍ5쪽 : Tools to further refine SAP Fiori launchpad content and (9쪽 : Demo) app-to-app navigations ☞ [Help Portal](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/08683e5409b74ced8705b2856c96c63b.html)<Br>&nbsp; &nbsp; ① FLP Content Mgr, ② FLP Designer (6쪽 : Demo), ③ App Descriptor Mass Maintenance (7쪽 : Demo)<Br>ㆍ12쪽 : Things you can configure in the SAP Fiori launchpad ☞ 참조 : SCN [Blog](https://blogs.sap.com/2017/11/19/sap-fiori-ui5-app-configuration-in-sap-fiori-launchpad/ "Fiori app configuration in SAP Fiori Launchpad")<Br>ㆍ13쪽 : How to assign SAP Fiori launchpad features to users - ① 전체 사용자 → [IMG](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/6107ee41f89a43c9af0aa279fe039cca.html "Help Portal : Launchpad Configuration Parameters"), ② 개별 Role → FLP Designer|
  |&nbsp; &nbsp; Unit 4<Br><Br><Br>|Supporting SAP Fiori<Br>ㆍ9쪽 : Diagnotics 『 Ctrl + Alt + Shift + S 』<Br><Br>|2021-06-04<Br><Br><Br>|ㆍ5쪽 : SAP Web Analytics(SAP Cloud Platform solution) [Demo](https://www.youtube.com/watch?v=bXMtor_AmPE) ☞ On-Premise는 어떻게 하는가?<Br>ㆍ6쪽 : In-App Help(09:01, no additional charge) - SCN [Blog 'How to Setup'](https://blogs.sap.com/2020/01/07/sap-fiori-for-sap-s-4hana-how-to-setup-the-user-assistant-in-your-s-4hana-fiori-launchpad/ "How to setup the User Assistant in your S/4HANA Fiori launchpad"), Enable Now [SAP Kore URL](https://www.sap.com/korea/products/enable-now.support.html) [YouTube](https://www.youtube.com/watch?v=TDmy27wEw4s)<Br>ㆍ[FLP](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/f951b50a07ce41deb08ced62711fe8b5.html) guide/문서 : [7쪽 the Option to Contact Support](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/599d9ad10f614a09bbc5324f340c64e7.html), [10쪽 Support Tools](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/af641fa4a8ba41379ca8c33f27ef35e9.html), [11쪽 Data Admin](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/202009.002/en-US/f171990f82494b7cb57f3be4d2d011f9.html), [7쪽 SCN Topic](https://community.sap.com/topics/fiori)|
  |&nbsp; &nbsp; Unit 5|Establishing a Central SAP Fiori Launchpad|2021-06-04|| <!-- </div></details>  『 'fiori3' SAP Fiori Overview: Design, Develop and Deploy 』 과정 세부 사항 -->

▣ 2021-06-03, 목 
* `SAP Screen Personas Practitioner Forum` e-Mail List [가입](https://www.sap.com/cmp/nl/sap-screen-personas-practitioner-forum/index.html) ☞ Learn more about [SAP Screen Personas](http://www.sapscreenpersonas.com/)
  + T-Code : /PERSONAS/ADMIN `SAP Screen Personas Administration`
  + 학습 경로 : SCN Blog [Roadmap](https://blogs.sap.com/2020/01/07/sap-screen-personas-roadmap-update-january-2020-accelerating-sap-fiori-adoption/) & [SP12 소개](https://blogs.sap.com/2020/12/14/sap-screen-personas-3.0-sp12-now-available.-sapui5-applets-easier-sap-fiori-launchpad-integration-native-barcode-scanning/)(`Support through 2040`) 및 Wiki [버전 간 비교](https://wiki.scn.sap.com/wiki/display/Img/Compare+SAP+Screen+Personas+versions) → openSAP 과정 [sps2](https://open.sap.com/courses/sps2), [sps3](https://open.sap.com/courses/sps3), [sps4](https://open.sap.com/courses/sps4) → SCN [Topic](https://community.sap.com/topics/screen-personas), [Wiki](https://wiki.scn.sap.com/wiki/display/Img/SAP+Screen+Personas+Product+Support) & [Help Portal](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US)
* [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw)의 manim library 설치 ☜ `파이썬 마님 엔진으로 수학 동영상 만들기` 『 Wikidocs [책](https://wikidocs.net/book/4381)』 참조 <details><summary>Details</summary><div>  
  1. 사전 설치
     1. 파이썬 설치
     2. FFmpeg : 동영상 파일을 생성해주는 라이브러리 - ffmpeg-2021-06-02-git-071930de72-full_build.7z 압축 풀고 User 변수에 Path 신규 삽입 ☞ 참조 [Site](https://www.wikihow.com/Install-FFmpeg-on-Windows)
     3. pycairo : 그래픽 처리 라이브러리 - pip install pycairo
     4. MikTex : 수식 문자 입력을 위한 LaText 프로그램 - EXE 다운(네트웍 설치) > 실행하여 설치 ☞ 참조 [Site](https://miktex.org/download) 또는 [Mirror Site](http://mirrors.ibiblio.org/CTAN/systems/windows/miktex/setup/windows-x64/)
     5. Sox : 사운드 변환 라이브러리 - EXE 다운 > 실행하여 설치 ☞ 참조 [Site](https://sourceforge.net/projects/sox/files/sox/)
  2. manim library 설치 (참조 : pypi manim, manimlib)
     1. pip install manimgl # https://github.com/3b1b/manim
        - 설치 후 실행 확인 : (예시) `C:\DS\Orange3-3.28.0>scripts\manimgl` 또는 `manimgl example_scenes.py OpeningManimExample`
     2. 한글 사용이 가능하도록 `Lib\site-packages\manimlib\tex_templates\tex_template.tex` file에 아래 내용 추가  
        > $\cdots$  
        > `\usepackage{microtype}`  
        > `\usepackage{kotex}` &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # <font color='gold'>한 줄</font> 추가된 내용  
        > `\DisableLigatures{encoding = *, family = * }`  
        > $\cdots$  
     3. 추가 설치 : ~~pip install manim_notebook~~ ☞ [pypi](https://pypi.org/project/manim-notebook/), Basic Usage [Tutorial](https://htmlpreview.github.io/?https://github.com/AkashKarnatak/manim_notebook/blob/master/Tutorial.html)
        - (실제로는 위와 같이 하지 않고) github [source](https://github.com/AkashKarnatak/manim_notebook)를 내려받은 후 setup.py와 requirements.txt의 manimlib을 manimgl로 변경 후 다음 명령 실행  
          C:\DS\manim_notebook-master>C:\DS\Orange3-3.28.0\Scripts\pip install -r requirements.txt
        - 위와 같이 해도 안되어서 우측과 같이 재실행 : `C:\DS\manim_notebook-master>C:\DS\Orange3-3.28.0\Scripts\pip install .`

▣ 2021-06-02, 수  
* 이정현 상무 문의 사항 【$\oplus$】
  + AI 관련 어떤 기능이 `내장(Embedded Analytics)`되어 있고 어떤 기능이 `별도 License` 또는 `환경(Analytics Cloud)`이 필요한지<Br>정리된 `자료/Site/확인 방법`
  + Fiori3 > Unit2, UI Type vs. Task Type - 자체적으로 확인할 사항
* SAP S/4HANA 1909 Fully Activated Appliance 접속
  + Hosts File  
    `172.16.28.45` &nbsp; &nbsp; `hqchanadb1` &nbsp; &nbsp; `hqchanadb1.hanwha.co.kr`
  + 안되는 경우
    - `https://hqchanadb1:44310/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html`
    - `https://172.16.28.45:44310/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html`
  + 되는 경우
    - https://hqchanadb1.hanwha.co.kr:44310/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html#Shell-home  
* MS VS Code Extension 설치 - SAP Fiori Tools 【$\oplus$】 ☜ [fiori3](https://open.sap.com/courses/fiori3) > Week3 > Unit3 > 10∼13쪽<details><summary>Details</summary><div>
  - SAP Fiori Tools - Extension Pack
    - Application Wizard
    - Application Modeler
    - Guided Development
    - Service Modeler
    - XML Annotation Language Server
    - XML Toolkit
  - SAP Mobile Services - Mobile Back-End Tools
  - Mobile Development Kit Extension for Visual Studio Code
  - SAP CDS Language Support
  - SAP HANA Driver for SQL Tools
  - SQL Analyzer Tools for SAP HANA <!-- MS VS Code Extension 설치 -->

▣ 2021-06-01, 화
* BSG Fiori 전문가 참석 회의(6/1, 15-17시, RM413) 
  - 산출물 Review
  - angular, View 등을 web component로 사용 가능. 케미칼에 많이 개발된 java는 사용 가능?
  - 사용자가 바꾸면 초기화는 어떻게? : 초기화 가능함

▣ 2021-05-31, 월 
* 5/31 수신된 "ERP Conversion 일정 초안 공유" 메일 검토 【●】
* Microsoft VS Studio Community 2019 오프라인 설치 [Blog](http://blog.naver.com/lidaxi043682/221856158439), MS [Doc](https://docs.microsoft.com/ko-kr/visualstudio/install/create-an-offline-installation-of-visual-studio?view=vs-2019)
* pycaret 관련 URL 모음 (구글 검색 결과) - 나중에 시간 날 때 하는 것으로, 묻어 둠.
  + https://blog.naver.com/dalgoon02121/222340409616
  + Machine Learning Made Easier with [PyCaret](https://towardsdatascience.com/machine-learning-made-easier-with-pycaret-907e7124efe6) 
  + Multiple Time Series Forecasting with [PyCaret](https://www.kdnuggets.com/2021/04/multiple-time-series-forecasting-pycaret.html)

▣ 2021-05-28, 금  
* System Conversion to SAP S/4HANA 검토 : [책갈피-단기](#112-단기)로 이동됨
* BSG Fiori 전문가 참석 회의(6/1, 15시) 대비 Fiori 검토 (Resource 검색, 정리ㆍ요약) : [책갈피-단기](#112-단기)로 이동됨
  + openSAP 'fiori' course 검색(아래 [`3 > 3.2 SAP`의 openSAP fiori 관련 과정](#32-sap) 참조) : fiori3 → s/4h18
  + SAP [TechEd](https://pages.sapteched.com/) 2020 'fiori' session 검색 : 37 Sessions  
* 수출입 RPA 전환 검토 - 수출입 외 영역 잔여 검토 8건에 대한 RPA 산출물(PPD)을 통한 검토 
  + 순서 : ① 자체 검토 <font color='cyan'>【●】</font>→ ② 오후 3시, RM406, 한만형 차장님과 같이 검토 <font color='cyan'>【●】</font>
  + Markdown 설명 자료를 같은 폴더 위치에 `[Example.md](Example.md)` 작성 및 위 회의 시 설명. 
    - 하나의 문서에서 다른 문서로 링크 [URL](https://docs.microsoft.com/ko-kr/contribute/how-to-write-links) 
* [VS Code 확장 마켓플레이스](https://marketplace.visualstudio.com/vscode)에서 mindmap for markdown 검색 'TinyMind for Markdown' 설치

▣ 2021-05-27, 목
* Fiori PMO Review, QA Review
* TechEd 2020 동영상, PDF File 확인
  - (SCN [Blog](https://blogs.sap.com/2016/11/02/sap-s4hana-system-conversion-at-a-glance/) Conversion at a Glance → ) SCN [Blog ★](https://blogs.sap.com/2021/03/30/sap-s-4hana-2020-system-conversion-steps-details-how-to-be-prepared/) 2021-03-30 Conversion Steps & Details vs. <font color='gold'>**Conversion Guide 2020**</font> [pdf](https://help.sap.com/doc/2b87656c4eee4284a5eb8976c0fe88fc/2020/en-US/CONV_OP2020.pdf)
  - Track: Digital Transformation with Intelligent ERP > Subtrack: (DT) How to move to SAP S/4HANA
  - 참고 : 구글 "sap s/4hana conversion guide 2020" 검색 ☞ SCN [Blog ★](https://blogs.sap.com/2021/03/30/sap-s-4hana-2020-system-conversion-steps-details-how-to-be-prepared/) 2021-03-30 Conversion Steps & Details
* 회사(ICT) 업무 : 5/21 법인카드 전표 처리, FastCampus 수강 신청
* 한화케미칼 RPA 운영 담당자 조사, 메일로 RPA 산출물 전달 요청함 
  + 유지보수 계약구조 : 한화시스템/ICT - SDCIT - 가도시스템즈
  + 유지보수 담당 : 가도시스템즈 박철근 팀장(책임, cgpark@gadosys.co.kr, 010-2307-9160)
  + 기타 요청사항 : 메일 문의하실 때 여승구(부장, skyeo0805@sdcit.co.kr, 010-3738-5201)도 참조 부탁드려요.

▣ 2021-05-26, 수
* 업무 영역별 마스터 페이지 작성 - 수출입 : AS-IS 기존 47쪽 참조, TO-BE 신규 작성
* Fully Activated Appliance (S/4HANA 1909)에서 https://open.sap.com/s4h19 > unit 10 실행해 보기
  + 10쪽 : ML Implementation, 11쪽 Example Scenario, 12쪽 PAi(Predictive Analytics Integrator) Demo
* **<font color='gold'>SAPPHIRE NOW Korea</font> Supply Chain** Webinar 참가 신청 (id/pwd : phs20210526 / sapphire20210616)
* SAP Learning Hub 접속 ☞ 나중에 가입 필요한 듯. 유료 교육 Cloud

▣ 2021-05-25, 화
* 회의 약속
  + 오전 10시, RPA 전환 방안, 지난 주 금요일(5/21) Online 회의에서 연기됨, 장병환 이사와 회의함.

▣ 2021-05-24, 월
* 회사 공지사항 및 업무 처리
  + [업무공유시스템](https://def.cp.hanwha.com) 오픈 : 사내망이나 VDI를 통해 접속 가능
    - ID, Password는 서클 계정과 같음. 크롬에 최적화되어 크롬 접속 권장(IE "호환성 보기 설정" 해제 필수).
    - 업무공유시스템 안내 [써클 게시글](http://snc.eagleoffice.co.kr/neo/bbs/C/125801/002373126)
  + 통신비(4월 사용, 5월 청구) 전표 처리, 주제별 회의비(5/21, 금, 중간보고 후 저녁 식사), 모니터 대여 연장 신청
* 회의 약속
  + RPA 전환 방안, 지난 주 금요일(5/21) Online 회의에서 연기됨
  + 지난 주 금요일(5/21) 수출입 패키지 관련 보낸 메일에 대한 후속 회의 : 5/25 오전 
  + 지난 5/4 메일(Readiness check, FAR report)에 대한 진행 상황 문의(김경호 과장) 
* 재고자산 재고관리(1년이상 비유동 자산) 검토
  + 참조 : 한국회계기준원 [K-IFRS](http://www.kasb.or.kr/fe/accstd/NR_list.do?sortCd=K-IFRS&divCd=01) ; 삼일회계법인 K-IFRS [재고자산](https://www.samili.com/acc/IfrsKijun.asp?bCode=1978-1002) ; 국세청 [저장품](https://txsi.hometax.go.kr/docs_new/customer/dictionary/view.jsp?word=&word_id=1271) ; Wiki백과 [재무상태표](https://ko.wikipedia.org/wiki/재무상태표); Blog [자산의 종류](https://1gold.tistory.com/27)
* 수출입 패키지 고도화 방안 (초안) : 가능한 항목에 대한 RPA 전환 공수, EDI I/F 추가 포함 수출입 고도화 공수  
  $\boxed{RPA~전환~가능~문의} \rightarrow \boxed{RPA~전환~가능~검토} \rightarrow \boxed{RPA~전환~공수} + \boxed{수출입~고도화~공수}$

▣ 2021-05-21, 금
* "한화솔루션/케미칼 SAP 고도화" 프로젝트 중간 보고
* 회의 약속
  + 09:00, 수출입 패키지 설명회, RM304 → 불광 C603, BizTech Partners 최승우 이사, 김연중 이사
    - 중립 질문 
      - 10년 정도의 시간이 지났는데, (이후 프로젝트 사례 등이 반영된) 추가 기능이 있다면 소개 요청
      - 패키지 장단점, 특장점, 신기술(S/4HANA, Fiori, AI... 관련)  
      ☞&nbsp; 김연중 이사가 정리해서 메일로 보낼 예정임. 향후 김연중 이사와 직접 컨택할 것.  
       &nbsp; &nbsp; &nbsp; ??
    - 패키지 내용 유지된다면 
      - SAP S/4HANA 고도화 시 특히 수정해야 하는 부분은? 대략 양(공수)은 어느 정도인지? : 1명, 3~4 M/M
    - 패키지 내용에 변화가 많다면 .. : 해당 사항 없음.
      - 패키지 구축 공수는? (패키지가 많이 바뀌었기 때문에) Data Migration은?
  + 13:30, RPA 전환 방안, RM421 → 온라인 미팅, 조성근 차장 → 차주로 연기함
  + 
▣ 2021-05-20, 목 
* 09:00, 수출입 패키지 설명회, RM406, ㈜에이에스이지 강석봉 대표 ☜ 5/17 보낸 메일 참조
  - License : Company Code License 
  - 중립 질문 
    - 10년 정도의 시간이 지났는데, (이후 프로젝트 사례 등이 반영된) 추가 기능이 있다면 소개 요청
    - 패키지 장단점, 특장점, 신기술(S/4HANA, Fiori, AI... 관련)  
      ☞&nbsp; config & 유연한 프로세스 구성, 진행관리 (480여개 t-code 연계, 삭제 마법사, 일괄 갱신 마법사), 4세대 EDI  
       &nbsp; &nbsp; &nbsp; 문서관리(T-DMS) 서버  
       &nbsp; &nbsp; &nbsp; 협력사 포탈 (웹 화면 - 진행관리 포함 수출, 수입 각 10개 이내, 모바일 용도는 아님)
  - 패키지 내용 유지된다면 
    - SAP S/4HANA 고도화 시 특히 수정해야 하는 부분은? 대략 양(공수)은 어느 정도인지? 
  - 패키지 내용에 변화가 많다면
    - 패키지 구축 공수는? (패키지가 많이 바뀌었기 때문에) Data Migration은?  
      ☞ 기존 CBO(수출입 패키지, 이력 조회용) 수정 2 M/M 정도
* 수출입 패키지 설명회 이후, 한화 장교동 빌딩 13층 확진자 발생으로 불광동 거점으로 이동하여 근무함

▣ 2021-05-18, 화
* 1단계 적용 대상 Fiori App 추출 방안 PPTx 장표 작성
* RPA 관련 조성근 차장 회의 - 오전 → 5/21 (금) 13:30 RM421
* SAP 디지털 트윈 실제 사례 공유 세미나, 오후 2시 : [URL](https://www.eventservice.kr/2021/sap/webinar/DSC/0518/index.php)

▣ 2021-05-17, 월  
* RPA 관련 조성근 차장 회의 - 내일 오전
* 수출입 관련하여 최승호 이사(010-3862-7057, 비즈텍 파트너스, swchoi@biztechpartners.co.kr) 연락해 봄
* 회사 노트북에 [오렌지3](https://orangedatamining.com/) 3.28.0 Portable 내려받고 설치
* 작성 산출물(Fiori 관련) Review
  + 보강 사항
    - 전체가 아닌 "일부" App 대상, 단계별 강조점(FLP, 개인화타일 → 기능 분할 및 재조합 → )
  + 별도 장표 : $\boxed{SAP~도구~추천} \rightarrow \boxed{설명~및~실행~확인} \rightarrow \boxed{적용~대상~추출}$
    - SAP 도구 : Readiness Check 또는 FAR Report
    - "조회ㆍ현황ㆍ개요" App 대상으로 설명 확인 및 실행
      - 설명 확인 : Lighthouse App, Fiori Reference Library, Online Documentation
      - 실행 확인 : S/4HANA 1909 Fully Activated Appliance 실행을 통한 확인

▣ 2021-05-14, 금
* openSAP Course [di1](https://open.sap.com/courses/di1) : SAP Data Intelligence for Enterprise AI 
  + 2020-05-13
    - Unit 6: Machine Learning Scenario Manager
    - Unit 7: Data Science Experiments in Jupyter Notebook ([PAL](https://help.sap.com/viewer/2cfbc5cf2bc14f028cfbe2a2bba60a50/2.0.05/en-US/c9eeed704f3f4ec39441434db8a874ad.html), [APL](https://help.sap.com/viewer/cb31bd99d09747089754a0ba75067ed2/3.3/en-US/5db34eae84ed44e49ec1f0f78dfb52a1.html), [Python SDK](https://help.sap.com/viewer/5ac15e8fccb447199fda4509e813bf9f/Cloud/en-US/12f7abac63844d4293a339a8effb3521.html) for SAP Data Intelligence)
      - 8쪽, SAP HANA Predictive Analysis Library ([PAL](https://help.sap.com/viewer/2cfbc5cf2bc14f028cfbe2a2bba60a50/2.0.05/en-US/c9eeed704f3f4ec39441434db8a874ad.html)) – Functional overview
      - 10쪽, SAP HANA [ML](https://help.sap.com/viewer/5ac15e8fccb447199fda4509e813bf9f/Cloud/en-US/c6ee16d6ee8a4648b07e329803bc7c59.html) – Automated Predictive Library ([APL](https://help.sap.com/viewer/cb31bd99d09747089754a0ba75067ed2/3.3/en-US/5db34eae84ed44e49ec1f0f78dfb52a1.html))
      - [Blog](https://blogs.sap.com/2019/04/23/automate-machine-learning-with-apl-now-part-of-sap-hana-sps04/), Automate machine learning with APL, now part of SAP HANA SPS04
  + 2020-05-14
    - Unit 8: Working with the SAP Data Intelligence Pipeline Modeler
    - Unit 9: Operationalizing Python and R with the Pipeline Modeler
    - Unit 10: Intelligent Services
    - Unit 11: Summary and Outlook ☞ 후행 과정, Hyper Links 소개
* [비즈텍 파트너스](http://biztechpartners.co.kr)에 Biz-Trade 솔루션 설명 요청
  + 지난 10년 이상의 기간 동안 변화된 것은? (신규 기능/프로세스), S/4HANA 관련, Data 이관, AI/RPA 등 신기술 관련.
  + 도입의 효과는 무엇인가? 자랑하고 싶은 점은?
* KSUG 패널 토크 "SAP S/4HANA 실 적용 기대 효과를 낱낱이 파헤쳐 보기" [게시글](https://www.ksug.kr/bbs/board.php?bo_table=free&wr_id=561&&#c_603) 질문 등록
  + 일시 : 오늘 14시. (접속 [Link](https://www.youtube.com/watch?v=U-Ejq-xBlsQ)는 1시간 전에 문자 및 메일로 전달됨)  
    ☞ 참고 : 5/13, 케미칼 프로젝트하면서 wellorg@hanmail.net으로 가입함(短)
  + 질문1 : 현재는 SAP ECC나 Suite on HANA를 사용하고 있는 경우 S/4HANA 2020으로 Upgrade(New Installation 또는 System Conversion)를 위한 프로젝트를 하는 것을 볼 수 있습니다.<Br>주변에서 "이제 S/4HANA 2020을 (프로젝트를 해서) 쓰게 됐으니 이런 프로젝트를 하지 않아도 되겠다"라는 감상을 간혹 듣습니다. 정말 그런가요? 예를 들어, S/4HANA 2020을 사용하다가 필요에 의해서 S/4HANA 2030을 사용해야 한다면, 그 때도 지금 했듯이 Upgrade(New Installation 또는 System Conversion)를 위한 프로젝트를 해야 하는 것인지요?  
  + 질문2 : Fiori App을  SAP는 "T-Code : Fiori App = 1 : N"이 될 수도 있도록 설계&작성했다고 합니다. Fiori LaunchPad를 통해 IT자원에 대한 "Single Point of Entry"를 제공하고 기존 IT 자원에 대해 Decomposition(분할)/Recomposition(조합)을 통해 Best-of-Breed인 Fiori App을 사용할 수 있다고 하는데, 컴포넌트 방식으로 이러한 "분할/조합"할 수 있는 것은 SAP Product에만 국한된 것 같습니다(ABAP, WD4A, SAPUI5, Fiori, ...). 그러나 Best-of-Breed인 App을 사용자에게 제공하려면 SAP 외 IT 자원을 고려하지 않을 수 없습니다.<Br>현재는 SAP Product만 가능한 이러한 Component를 활용한 "분할/조합"을 Java나 .net과 같은 언어로 작성된 일반 웹 프로그램까지 포괄하여 가능하게 될 시점은 언제일까요? Fiori App을 통해 Best-of-Breed인 App을 설계/작성/제공하기 위해서는 SAP는 이러한 것도 목표로 하고 있을 것이라고 생각됩니다.  
  + 질문3 : 대부분 SAP Gui를 사용해도 S/4HANA의 “기존+신규” 기능을 활용할 수 있을 것입니다.<Br>어떤 기능은 SAP Gui로는 사용할 수 없고 꼭 Fiori App에서만 사용 가능하다면, Fiori 사용이 필수인 해당 기능 목록을 어떻게 알 수 있을까요? 
  + 질문4 : SAP GUI용 프로그램, SAPUI5용 프로그램 및 Fiori App을 포괄하여 테스트를 하려면 eCATT로는 안 된다고 들었습니다(확실하지는 않습니다). 이러한 프로그램을 포괄하는 SAP의 Testing Tool이 있을까요? 있다면 무엇인지요? 

▣ 2021-05-13, 목
* UI/UX (Fiori) 과제 정의서 작성본 보강 : 사례 Backup 장표 보강
  + 관련 자료 검색 결과
    - SAP S/4HANA on premise edition: FPS versus SPS [Blog](https://blogs.sap.com/2016/04/08/sap-s4hana-on-premise-edition-fps-versus-sps/)  
      → SAP S/4HANA : Product Version "2020", '분기/년'별로 FPS(Feature Pack Stack), 4번째부터 SPS(Support Pack Stack) 
* 회사 사업부 프로젝트 수행 관련 교육 : 14시~15시, 지대환 과장

▣ 2021-05-12, 수
* 엄승세 대리에게 "SAP S/4HANA 2020 SP00 Fully Activated Appliance" 설치 가능 여부 문의  
  ☞ Getting Started Guide [PDF](https://caldocs.hana.ondemand.com/caldocs/help/7a3ebd3e-d005-4c70-ae35-40a167aed981_Getting_Started_Guide_v1.pdf)
* Readiness Check, FAR 리포트 관련 문의 사항(20210504, 김경호 과장) 확인 ☞ 결과 : 아직 확인 안 된 상태임.
  |Tool / Resource|【 대상|Scenario 】|Remark ([s4h18](https://open.sap.com/courses/s4h18), W1 Unit 4, 15~16쪽)|
  |:---|--:|:--|:---|
  |1. SAP Fiori Apps Reference Library [URL](https://fioriappslibrary.hana.ondemand.com/)|New Implementation|System Conversion||
  |2. Best Practices Explorer [URL](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/on-premise)|New Implementation|||
  |3. SAP Readiness Check [URL](http://www.sap.com/readinesscheck)||System Conversion|SAP ERP 및 S/4HANA에서 실행 가능|
  |4. FAR(Fiori Apps Recommendations) Report [URL](http://www.sap.com/FAR)||System Conversion|SAP ERP 및 S/4HANA에서 실행 가능|
* UI/UX (Fiori) 과제 정의서 작성 및 전달
  + 3단계 : $\boxed{UI/UX~Baseline~aligned~with~Sys.~Conv.} \rightarrow \boxed{UI/UX~Extension} \rightarrow \boxed{Level-up~to~UI/UX~Integration}$
    - ① 기반 : 기존 Role 활용, 조회용, Manager용 ☞ SAP Conversion 진도 맞춤
    - ② 확장 : ① + "SAP GUI + Fiori' Program" 대상 "기능 분할(DeCompose) + 재조합(ReCompose)" <Br>&nbsp; &nbsp; ☞ Fiori 기반 사내 SAP Resource 통합 제공
    - ③ 도약 : ① + ② + "DT + SAP(Fiori)" 대상 "기능 분할(DeCompose) + 재조합(ReCompose)" + Look & Feel <Br>&nbsp; &nbsp; ☞ Fiori 기반 사내 Web IT Resource 통합 제공(DT, RPA, ML, ...)

▣ 2021-05-11, 화  
* TOC 장현태 사무총장께 종신회비 50만원 입금, 농협 1203-01-004211 (사단법인한국티오시협회)
* MS Visual Studio Code 설치 ☞ 참고 : [공식 Web Site](https://code.visualstudio.com/), [github](https://github.com/Microsoft/vscode), [Blog](https://www.44bits.io/ko/keyword/visual-studio-code)
  + 확장 기능 설치 : Microsoft에서 제공하는 Freeware 위주로 설치함
    - Hex Editor
    - Jupyter : Jupyter Extension for Visual Studio Code
    - Keras 2.4.0 Code Snippets
    - VS Code용 한국어 팩(Korean Language Pack for Visual Studio Code)
    - Markdown All in One : Markdown Support for Visual Studio Code
    - Microsoft Graph Theme
    - PostgreSQL : PostgreSQL for Visual Studio Code
    - Pylance
    - Python : Python extension for Visual Studio Code
    - PyTorch Snippets : PyTorch Code Snippets for VSCode
    - Tensorflow 2.0 Snippets : Tensorflow 2.0 Snippets for VS Code
    - Graphviz Markdown Preview
    - TinyMind for Markdown
* Daily Meeting
  + 내일부터는 한화빌딩으로 출근
* Hibiz 참조하여 Fiori 향후 계획(3단계 정도) 만들 것 (작성 진행 중)
  + fiori 관련 SAP 기술 Roadmap 확인할 것
    - SAP Road Maps [URL](https://www.sap.com/products/roadmaps.html)
    - SAP Fiori Road Map Highlights Webcast Summary, 20200316 [Blog](https://blogs.sap.com/2020/03/16/sap-fiori-road-map-highlights-webcast-summary/)
    - 구글 검색 "sap fiori component container reuse" → SAPUI5 How To: Reuse parts of a SAPUI5, 20170405 [Blog](https://blogs.sap.com/2017/04/05/sapui5-how-to-reuse-parts-of-a-sapui5-application-in-othermultiple-sapui5-applications/) 
  + 우선 https://open.sap.com 강의 중 UI/UX 관련 Course ⑤[s4h18](https://open.sap.com/courses/s4h18)과 ⑥[fiori3](https://open.sap.com/courses/fiori3)을 읽어 볼 것 <!-- 2021년4월 한화케미칼 SAP 고도화 프로젝트를 하면서 수강 시작함(長), wellorg@hanmail.net -->

▣ 2021-05-10, 월  
* 업무량 마감 입력 및 상신
* 건강 관련 [신문 기사](https://health.chosun.com/site/data/html_dir/2015/03/16/2015031601020.html)
* Daily Meeting
  + 오후 산출물 Review : 14시 -> Hibiz 참조하여 Fiori 향후 계획(3단계 정도) 만들 것 (작성 진행 중)

▣ 2021-05-04, 화
* 현황 장표 중 "ERP 업무 영역 별 주요 이슈 분석 > UI/UX"를 위한 사례 취합 (2)
  + https://open.sap.com/courses/s4h18 : How to Deliver a Great User Experience with SAP S/4HANA
    - Week 1: Plan – SAP Fiori UX for SAP S/4HANA
      - Unit 1 (01/87): Understanding SAP's User Experience Strategy and Benefits
      - Unit 2 (20/87): Executing Business Processes in SAP S/4HANA Using SAP Fiori
        - 016쪽
          - SAP Best Practices Explorer [URL](https://rapid.sap.com/bp/#/browse/packageversions/BP_OP_ENTPR) 
          - SAP Fiori apps reference library [URL](https://fioriappslibrary.hana.ondemand.com)
          - SAP S/4HANA Tutorials [URL ★★★](https://education.hana.ondemand.com/education/pub/s4/index.html)
      - Unit 3 (39/87): Planning the UX Strategy
      - Unit 4 (54/87): Planning the UX Scope and Budget
        - 012쪽 : Tools and resources for roles and apps scoping  ( ★★★ ) 
          - SAP Fiori apps reference library : New Implementation, System Conversion
          - SAP Best Practices Explorer : New Implementation  
            ☞ Process Flow 등을 생각한다면, Conversion에도 쓸 수 있을 듯...
          - SAP [Readiness Check](http://www.sap.com/readinesscheck) 2.0 : System Conversion
            - cf) web resources : [URL1](https://blogs.sap.com/2020/11/26/sap-readiness-check-for-sap-s-4hana-whats-new-in-november-2020/), [URL2](https://blogs.sap.com/2019/05/16/sap-readiness-check-2.0-details-about-the-topic-of-sap-fiori/)
          - [FAR(Fiori Apps Recommendations)](http://www.sap.com/FAR) Report : System conversion
      - Unit 5 (74/87): Recognizing UX as an Embedded Track in SAP S/4HANA Projects ☞ way of working, working together, collaboration, ...
    - Week 2: Deliver - SAP Fiori UX for SAP S/4HANA
      - Unit 1 (001/118): Building a UX Track in an SAP S/4HANA Implementation Plan
      - Unit 2 (031/118): UX Technical Activities That Everyone Should Know
        - 016쪽 : Troubleshooting Tips and Tricks 
        - 017쪽 : Fiori Performance ☞ Community Wiki > [S/4HANA Documents](https://blogs.sap.com/2017/06/08/fiori-for-s4hana-performance-tips-and-tricks-in-s4hana-1610-on-premise/)
        - 019쪽 : Fiori content and authorizations  
          ☞ Best Practices for Content Configuration : [URL](https://help.sap.com/viewer/a7b390faab1140c087b8926571e942b7/201809.002/en-US/6ceb3b39e4af4241acde015fece66e26.html)
        - 022쪽 : Fiori Wiki ☞ https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=449910787
      - Unit 3 (057/118): The Role of the Functional Team Within the SAP S/4HANA UX Track
        - 005쪽 : Understanding new concepts ☞ Decomposition & Recomposition
        - 008쪽 : Tools for Selecting Business Roles  ( ★★★ ) 
          - SAP Fiori lighthouse scenarios ☞ [PDF](https://www.sap.com/corporate/en/documents/2018/01/12b3dec4-ec7c-0010-82c7-eda71af511fa.html)
          - SAP Fiori apps reference library [URL](https://fioriappslibrary.hana.ondemand.com)
          - Simplification List [URL](https://launchpad.support.sap.com/#/sic)
          - SAP Readiness Check 2.0 &nbsp; &nbsp; ☞ 위 W1, U4, 012쪽 참조
          - SAP Best Practices Explorer ☞ 위 W1, U4, 012쪽 참조
        - 009쪽 : Decisions based on UX strategy
      - Unit 4 (075/118): Designing the Best UX with Fit/Gap Analysis
        - 009쪽 : Best Practices Explorer를 활용한 Fit/Gap Analysis 사례, "Test Script"와 "Process Flow"를 활용함.
      - Unit 5 (099/118): Realizing the Best UX with SAP S/4HANA Extensibility
        - 005쪽 : SAP S/4HANA extensibility spectrum - Layering vs. Functional Scope
        - 006쪽 : SAP S/4HANA extensibility – Big Picture
        - 008쪽 : Using the Guided Answers tool – demo ☞ [URL](https://ga.support.sap.com/dtp/viewer/#/tree/1910/actions/24709)
        - 015쪽 : Addressing gaps – technology and effort, Extensibility Pattern Matrix
    - Week 3: Innovate - Creating Intelligent UX
      - Unit 1: Currently Available Tools and Future Outlook for Intelligent Experience
      - Unit 2: Intelligent Experience with Process Automation and Chatbots
      - Unit 3: Intelligent Experience with Intelligent Apps
        - 010쪽 : Intelligent apps available in SAP S/4HANA
        - 014쪽 : Embedded scenario – goods receipt / invoice receipt account reconciliation (7020103, 8007847) – on-premise cockpit only
          - Sneak peek into S/4HANA 1909 Finance Innovations [URL](https://s4hanablog.com/2019/08/16/sneak-peek-into-s-4hana-1909-finance-innovations/)
          - Sneak peek into S/4HANA 1909 Finance Innovations – Part 2 [URL](https://blogs.sap.com/2020/09/11/sneak-peek-into-s-4hana-1909-finance-innovations-part-2/)
          - SAP Leonardo Artificial Intelligence : Webinar PDF [2020-02-27](https://assets.dm.ux.sap.com/webinars/it-sap-dbs-italy-for-intelligent-enterprise/pdfs/w9_sap_services_webinar_series_s4intell.pdf), [2020-07-30](https://assets.dm.ux.sap.com/it-sap-dbs-italy-for-intelligent-enterprise/pdfs/32_sap_services_webinar_intell2_20200728.pdf)
        - 015쪽 : Delivered and upcoming ML scenarios for SAP S/4HANA Cloud 1908 & SAP S/4HANA 1909
          - [Product Description ★★](https://www.sap.com/products/data-intelligence.html), [SAP Data Intelligence, trial edition 3.0](https://blogs.sap.com/2020/05/15/sap-data-intelligence-trial-edition-3.0/)
          - [Product Documentation](https://www.sap.com/products/data-intelligence/technical-information.html)
        - 019쪽
          - How can you start your journey to the Intelligent Enterprise?
          - MOVE to SAP S/4HANA, START with SAP Fiori embedded ML apps, EXPAND by considering side-by-side ML apps
      - Unit 4: Intelligent Experience with Intelligent Technologies
        - 007쪽 : Plant Maintenance 사례 - Integrate with SAP S/4HANA PM notifications
      - Unit 5: Identifying Intelligent Experience Opportunities
        - 004쪽 : How do we create an Intelligent Experience? - Innovation Opportunities from "Fit/Gap Analysis and Design Thinking"
        - 006,7쪽 : What is design thinking?
          - Design thinking is a human-centered method for solving complex problems and generating new ideas.
          - Design thinking is an approach to innovation by fostering multi-disciplinary collaboration.
        - 010쪽 : Elements of design thinking = Persona + Journey Maps + Prototyping
  + https://open.sap.com/courses/s4h11-1 : System Conversion to SAP S4HANA (Repeat)
    - Week 4: Technical Topics and Project Management
      - Unit 4: Preparing for SAP Fiori and the New UI Innovations
  + https://open.sap.com/courses/s4h14-1 : Key Technical Topics in a System Conversion to SAP S/4HANA (Repeat)
    - Week 3: Development Recommendations for SAP S/4HANA
      - Unit 4: The ABAP Programming Model for SAP Fiori
        - 014쪽
          - ABAP Programming Model for SAP Fiori - [Documentation](https://help.sap.com/viewer/cc0c305d2fab47bd808adcad3ca7ee9d/7.52.4/en-US/3b77569ca8ee4226bdab4fcebd6f6ea6.html) in SAP Help Portal
          - Be prepared for the ABAP Programming Model for SAP Fiori [URL](https://blogs.sap.com/2017/12/07/be-prepared-for-the-new-abap-programming-model-in-sap-s4hana/)
          - Getting Started with the ABAP Programming Model for SAP Fiori [URL](https://blogs.sap.com/2016/04/04/getting-started-abap-programming-model/)
          - ABAP RESTful Programming Model - [Documentation](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/31367ef6c3e947059e0d7c1cbfcaae93.html) in SAP Help Portal 
      - Unit 6: Extensibility Use Cases - Entending CDS Views
        - 006쪽 : Analytics Extensibility Overview
        - 007쪽 : Virtual Data Model (VDM)
  + https://open.sap.com/courses/s4h14-1 : Key Functional Topics in a System Conversion to SAP S/4HANA (Repeat)
    - Week 1: SAP S/4HANA Project Management
      - Unit 1: Overview of the SAP Transformation Navigator
      - Unit 2: Project Management: Overview
      - Unit 3: Project Management: Architecture-Related Impact
      - Unit 4: Project Management: Conversion-Related Impact
      - Unit 5: Project Management: Readiness Check Overview
      - Unit 6: Introduction of the Simplification List
      - Unit 7: Project Planning with SAP Activate and Roadmap Viewer
        - 009쪽
          - Transition roadmap – What’s in it for SAP customers and partners?
          - SAP Transformation Navigator [URL](https://go.support.sap.com/transformationnavigator/)
      - Unit 8: Understanding the SAP S/4HANA User Experience
        - 006쪽
          - Selecting SAP Fiori apps and classic UIs for your business role and business process
          - SAP Fiori Apps Reference Library, SAP Fiori Lighthouse Scenarios, SAP Fiori App Recommendations([FAR](https://www.sap.com/far) )
        - 008쪽 : Selecting SAP Fiori apps and classic UIs for your business role and business process
        - 010쪽 : Configuring, adapting, and extending your SAP Fiori apps via special SAP Fiori Apps
        - 011쪽 : Extending your SAP Fiori Apps as a Key User
  + https://open.sap.com/courses/fiori3 : SAP Fiori Overview

▣ 2021-05-03, 월
* SAP 이정현 상무(jung.hyun.lee@sap.com)께 문의 메일 발신
  - ① Fiori App에서 예전 SAP GUI를 띄울 수 있는가?
  - ② Role 활용 : SAP Gui용으로 T-Code PFCG에서 정의한 Role을 Fiori에서도 사용할 수 있는가?
  - ③ S/4HANA 도입 시 필수로 사용해야 하는 Fiori App은?
* 현황 장표 중 "ERP 업무 영역 별 주요 이슈 분석 > UI/UX"를 위한 사례 취합 (1)
  + SAP Fiori | SAP Community : https://community.sap.com/topics/fiori
  + Leading SAP S/4HANA UX – Selecting SAP Fiori apps [URL](https://blogs.sap.com/2017/08/16/leading-sap-s4hana-ux-selecting-sap-fiori-apps/)
    - Your Business Priorities and Strategic Direction
    - Your Business Roles
    - Your SAP S/4HANA Version
  + How to Understand Why Fiori Most Likely Won't be Able to Survive [URL](https://www.brightworkresearch.com/understand-fiori-wont-able-survive/)
  + C:\Users\heesang.p\Desktop\ERP_Planning\참조 정보\SAP S4HANA Conversion 제안서_20191002_두산인프라코어,두산산업차량_코오롱베니트.pptx
    - 012쪽 : 기대효과 - 새로운 UX/UI 플랫폼인 Fiori를 활용하여 멀티 디바이스 환경 지원이 가능한 반응형 SAP 데이터 기반의 Web 구성이 가능하며  (이하 생략)
    - 049쪽 : SAP Fiori에서 제공되는 1만여 개의 다양한 화면을 통해 개발하여 사용 중인 CBO를 대체할 수 있습니다.
  + C:\Users\heesang.p\Desktop\ERP_Planning\참조 정보\SAP S4HANA Conversion 사례_두산인프라코어_코오롱베니트.pdf
    - 2-019쪽 : SAP Fiori 기능 소개 = 단일 엔트리 포인트 + 도메인 고유 정보 및 액션 + 상세 내역 관리 및 분석  
      ☞ SAP Fiori Object Page Element [URL](https://sapui5.hana.ondemand.com/sdk/#/topic/645e27ae85d54c8cbc3f6722184a24a1)a
    - 2-027쪽 : 2020기능, ISLM(Intelligent Scenario Lifecycle Management), 머신러닝 시나리오 관리
    - 2-032쪽 : Remake of the SAP ERP vs. SAP S/4HANA Comparison Video Series  
      ☞ PDF File 65(2-032)쪽의 왼쪽에 있는 동영상 [HyperLink](https://blogs.sap.com/2020/09/25/remake-of-the-sap-erp-vs.-sap-s-4hana-comparison-video-series/) 확인  
        YouTube에서 "Experience Transformation SAP Fiori UX" 검색하면 여러 건의 관련 동영상 나타남.

▣ 2021-04-20, 화
* 태양광 모니터링 시스템 소개 : 14:00, Teams Online 회의
  - grafana 소개 : 참조 [자료1](https://medium.com/finda-tech/grafana란-f3c7c1551c38), [자료2](https://www.44bits.io/ko/keyword/grafana)
  - https://pypi.org/project/grafana-api/
    - [Create Grafana Dashboards With Python](https://medium.com/swlh/create-grafana-dashboards-with-python-14a6962eb06c)
    - [Visualize almost anything with Grafana and Python](https://oz123.github.io/writings/2019-06-16-Visualize-almost-anything-with-Grafana-and-Python/index.html)
  - [Jupyter Dashboards Layout Extension](https://jupyter-dashboards-layout.readthedocs.io/en/latest/)
* 현황 자료 우측 문구  
  (2) CBO 및 I/F 개선  
    - 마감, 정산 및 느린 Report 속도 개선  
    &nbsp; &nbsp; cf) 현업에서 느리다고 의견을 주지는 않았으나, 이 부분(마감, 정산)을 개선 Point로 잡아 봤습니다.
  (3) 업무 개선  
    - 분산된 Report의 통합 조회  
    &nbsp; &nbsp; cf) 사례: 수출 "L/C 정보 조회, 매입/추심 영수증 조회, ..."
* 이정현(jung.hyun.lee@sap.com) 상무 전달 자료 검토 : SAP S/4HANA 1909 신규 기능 Scenario - Demo 21
  + 참고 URL : SAP S/4HANA Fully-Activated Appliance: Demo Guides | SAP Blogs [URL](https://blogs.sap.com/2019/04/23/sap-s4hana-fully-activated-appliance-demo-guides/)
  + 짧은 소개
    ㆍ기존 ECC 이전 버전에서 프로토타이핑 용으로 사용된 IDES Scenario에 대응되는  
    &nbsp; &nbsp; S/4HANA 버전의 자료를 요청한 결과로 SAP에서 받은 자료임.  
    ㆍ파일의 시나리오는 S/4HANA 1909에서 변경된 기능 위주의 프로세스에 대한 것임.
  + 회사 Basis 담당자 : 함희석 차장, 엄승세 대리
  + Demo 21 파일들 : 관심 9건(1&24.분석, 3.DDMRP, 8.구매+EWM, 11&12.데이터 이관, 16.Overview, 19.pMRP, 20.Rapid Activation) ☞ S4H_MM_DEM / Welcome1  
    01．Demo Script for SAP S_4HANA 1909 FPS00_01_02 Fully-Activated Appliance_Analytics.pdf  
    02．Demo Script for SAP S_4HANA 1909 FPS00_01_02 Fully-Activated Appliance_Basic Transportation Management.pdf  
    03．Demo Script for SAP S_4HANA 1909 FPS00_01_02 Fully-Activated Appliance_Demand-driven Replenishment.pdf  
    04．Demo Script for SAP S_4HANA 1909 FPS00_01_02 Fully-Activated Appliance_Extensibility – SAP Fiori custom fields & applications.pdf  
    05．Demo Script for SAP S_4HANA 1909 FPS00_01_02 Fully-Activated Appliance_Print Form Customization.pdf  
    06．Demo Script for SAP S_4HANA 1909 FPS00_01_02 Fully-Activated Appliance_SAP Screen Personas.pdf  
    07．Demo Script for SAP S_4HANA 1909 FPS01 Fully-Activated Appliance_ Sell from Stock with Outbound Delivery Processing.pdf  
    08．Demo Script for SAP S_4HANA 1909 FPS01 Fully-Activated Appliance_ Warehouse Ibound Processing from Supplier.pdf  
    09．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Accounting, Financial Close & Financial Closing Cockpit.pdf  
    10．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Data Migration - File Approach (Bank Data).pdf  
    11．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Data Migration - File Approach Materials.pdf  
    12．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Data Migration - Staging Approach.pdf  
    13．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Group Reporting.pdf  
    14．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Investments.pdf  
    15．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Lease-in Accounting.pdf  
    16．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Overview Pages for Finance, Procurement and Sales.pdf  
    17．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Plan to Produce using Advanced Planning for Capacity Utilization.pdf  
    18．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Portfolio and Project Management.pdf  
    19．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Predictive Material and Resource Planning (pMRP).pdf  
    20．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ SAP Fiori Rapid Activation.pdf  
    21．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Service Management.pdf  
    22．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Simplified self-service HCM tasks using SAP Fiori.pdf  
    23．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Universal Allocation for Finance and Controlling.pdf  
    24．Demo Script for SAP S_4HANA 1909 FPS02 Fully-Activated Appliance_ Working with predictive applications and models.pdf  
    25．DEMO Scripts for Finance Procurement Sales.pdf ☞ 16번과 같음. 볼 필요 없을 듯.  
    설정01. Demo21 Living Company Guide July 2020_V2.0.pdf  
    설정02. Interaction Center.pdf  
    설정03. SAP S_4HANA Fully-Activated Appliance_ Fully-Qualified Domain Name & SSL Certificates.pdf  
    기타01. Import files 1.4.zip  
    기타02. Pasted Image.png  
    MDG (폴더)  
    &nbsp; &nbsp; MDG01. MDG\Data Processing in SAP MDG on S_4HANA with Integrated SAP Cloud Platform Data Enrichment.pdf  
    &nbsp; &nbsp; MDG02. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Central Governance of Custom Objects.pdf  
    &nbsp; &nbsp; MDG03. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Central Governance of Customer Data.pdf  
    &nbsp; &nbsp; MDG04. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Central Governance of Financial Data (G_L Accounts).pdf  
    &nbsp; &nbsp; MDG05. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Central Governance of Financial Data (Internal Order).pdf  
    &nbsp; &nbsp; MDG06. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Central Governance of Financial Data (Maintaining Profit Center Data).pdf  
    &nbsp; &nbsp; MDG07. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Central Governance of Material Data.pdf  
    &nbsp; &nbsp; MDG08. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Central Governance of Supplier Data.pdf  
    &nbsp; &nbsp; MDG09. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Consolidating Business Partner Data.pdf  
    &nbsp; &nbsp; MDG10. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Data Quality Management for Product Data.pdf  
    &nbsp; &nbsp; MDG11. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Mass Processing of Product Data.pdf  
    &nbsp; &nbsp; MDG12. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Multi-Records Processing in Central Governance of Material Data.pdf  
    &nbsp; &nbsp; MDG13. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Parallel Change Requests in Central Governance of Customer Data.pdf  
    &nbsp; &nbsp; MDG14. MDG\Demo Script for SAP S_4HANA 1809 FPS01 Fully-Activated Appliance_ Process Analytics in Master Data Governance.pdf  
    &nbsp; &nbsp; MDG15. MDG\Mining data quality rules for product data.pdf  
    &nbsp; &nbsp; MDG16. MDG\Using data quality rules in change request processing of business partner data.pdf  
	☞ 신규 약어 : FPS = Feature Package Stack

▣ 2021-04-19, 월
* 회사 세미나 : SAP S4 HANA 기반 차세대 ERP 추진 전략 세미나  
  ㆍMS Teams 온라인 회의 ☞ 4/19 김영진 부장 메일 참조  
  ㆍ시간 : 2021년 4월 19일 월요일 오후 2:00-오후 4:00  
  ㆍ위치 : Microsoft Teams 모임, 컨퍼런스룸(15층)
* [완료] I/F 문서 하나로 합할 것.
* "현황분석 및 방향성 수립" 보고서 꼭지  
  ①마감&무거운Report, ②수출EDI, ③Download&분석  (선급금, 취소, GRIR은 현황과 무관한 개선항목으로 제안)  
  
  ||속도|Process|I/F|Report 한 곳에서…|
  |:---|:--:|:--:|:--:|:--:|
  |MM (구매ㆍ자재)|마감, 무거운 Report|취소 최소화<Br>선급금 계정 분할||○|
  |수입|마감, 무거운 Report|취소 최소화|||
  |수출|마감, 무거운 Report||EDI|○|
  |PM (설비관리)|마감, 무거운 Report||||

▣ 2021-04-16, 금
* 인터뷰 : 15시-17시,  MM 울산 기자재; 울산 물류팀 진종형 사원 (유승우 대리)
* 어제 인터뷰 결과 정리할 것

▣ 2021-04-15, 목
* 인터뷰 
  + 10시-11:30, MM 여수 기자재;   여수 물류팀 김석원 과장 (김종균 사원)
  + 13시-15시, &nbsp; MM 울산 원부자재; 유승우 대리 -> 4/16 금, 오후 3시 회의와 합함.
  + 15시-17시, &nbsp; 수출; 오소정 사원, 강민정 사원
* ★ https://www.sap.com/korea/products/s4hana-movement.html > 밑으로 이동(Scroll down) > ★ IT 부서를 위한 셀프 서비스 툴
  - 문서 : 비즈니스 시나리오 추천(BSR: Business Scenario Recommendations) : Your Personalized Journey to SAP S_4HANA.pdf (☞ "Desktop\ERP_Planning\참조 정보"에 저정함)
    ☞ Start your Transformation Journey to SAP S/4HANA with Process Discovery [URL](https://msmproda7afccce3.hana.ondemand.com/Request/BSN/)
  - 헬프 문서 : 준비 상황 체크(SAP Readiness Check)
    ☞ 1 page 설명 : [인포그래픽](https://www.sap.com/korea/documents/2018/10/d2092cc2-217d-0010-87a3-c30de2ffd8ff.html?campaigncode=CRM-SH20-DGC-TRCK_RC) → [자세한 내용](https://help.sap.com/viewer/product/SAP_READINESS_CHECK/200/en-US)
  - 헬프 [문서](https://www.sap.com/korea/documents/2019/05/44b3ebd5-4b7d-0010-87a3-c30de2ffd8ff.html) : SAP S/4HANA로 가는 여정 매핑  
    ☞ Mapping Your Journey to SAP S_4HANA - A Practical Guide for Senior IT Leadership.pdf
  - 웨비나 시리즈 : SAP S/4HANA 프로젝트 성공에 필요한 서비스 이용하기  
    ㆍWhat You Need to Know About SAP S/4HANA Projects  
    ㆍ★Build User Acceptance with an SAP S/4HANA Trial  
    ㆍLearn from Successful SAP S/4HANA Customers  
    ㆍ★Engage the Services You Need for a Successful SAP S/4HANA Project

▣ 2021-04-14, 수
* SAP 요청 사항
  + On-Premise, SAP S/4HANA 2020에 맞는 현행화된 그리고 SAP Activate 방법론에 맞는 SAP Service Offerings/Tools : 표로 정리되었으면 좋겠음
  + (고객 대상 설명이 가능한) SAP S/4HANA 기반 표준기능으로 프로토타이핑이 가능한 환경, 자료, ...?
  + 한국 환경에 S/4HANA 적용된 사례 및 Lessons Learned 공유 (S/4HANA 전체, FIORI, Analytics, …)
  + FIORI에 대해서는 많은 정보가 일괄 제공되는 URL(FIORI WIKI)이 있는 것 같습니다.  
    S/4HANA New Installation이나 Conversion에 대해서는 이러한 Site가 있는지요?
* 인터뷰  
  + 10시-11:30, 수출(국제금융); 이동근 대리
    - EDI 데이터 중 몇몇 은행들로부터 수신받지 못하는 불편함이 있고, (지난 4/6 수출 IT담당자 인터뷰 내용)  
      해당 은행으로부터 메일을 통해 따로 데이터를 확인하는 것으로 알고 있습니다. (윤지호 과장, 김조홍 사원)  
      ☞ "수출입은행, 국민은행"으로부터는 EDI Data를 못 받고 있음.  
      - 국민은행의 경우 법인 전체로 전달(그래서 한화솔루션 전략부문에서 받고 있음). 자금운영팀 컨택포인트.  
        수출입은행의 경우 EDI를 보내 줄 수 없는 구조. : 수출입은행에서 전송 Service를 하고 있지 않음. 메일 정보 전달만 가능.  
        KT넷에서 회사 내의 부문으로 구분 전달할 수 있는 것으로 알고 있음. (은행 --> KTNet --> 수신회사)  
        → 관련 현업 인터뷰(국제금융팀 이동근 대리) 시 확인 필요  
        &nbsp; &nbsp; cf) 잘 되는 은행 예: 우리, SC제일, 농협,...  
        &nbsp; &nbsp; ☞ 메모 : 우리은행 웹EDI 서비스(무료, 기업 인터넷뱅킹 가입 후 사용 가능)  
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; https://spot.wooribank.com/pot/Dream?withyou=FXEIM0009  
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; https://spot.wooribank.com/pot/Dream?withyou=CQFNT0053  
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 메모 : 부산은행 https://www.busanbank.co.kr/ib20/mnu/FPMFRX200004001  
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 메모 : Utrade Hub - https://www.utradehub.or.kr/  
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; KTNet 전자무역 솔루션 - https://webcs.ktnet.com/service/UTradePartner_tab1.do 
  + 13시-15시,  PM; 김성민 과장, 박상원 과장
  + 15시-17시,  MM 여수 원부자재; 여수 물류팀 김종균 사원 -> 4/15 오전 10시 회의와 합함.
* SAP 대상 요청 사항 (Mail 발송함)
  + On-Premise, SAP S/4HANA 2020에 맞는 현행화된 그리고 SAP Activate 방법론에 맞는 SAP Service Offerings/Tools : 표로 정리되었으면 좋겠음.  
    FIORI에 대해서는 많은 정보가 일괄 제공되는 URL(FIORI WIKI)이 있는 것 같습니다.  
    S/4HANA New Installation이나 Conversion에 대해서는 이러한 Site가 있는지요?
  + (고객 대상 설명이 가능한) SAP S/4HANA 기반 표준기능으로 프로토타이핑이 가능한 “환경, 자료, ...”는 무엇?
    고객은 실사례를 기반으로 대화하기를 원하는데, 예전에는 IDES Scenario를 SAP ECC에서 보여줄 수 있었다면  
    새로운 표준인 S/4HANA, Fiori UI/UX는 어떤 시나리오에 대해 어디에서 경험할 수 있는지?  
    &nbsp; &nbsp; -> 현재 Fully Activated Appliance(용어 부정확할 수 있음) 설치된 상태인데, SAP S/4HANA 2020에 맞는 Scenario의 프로토타이핑은 어떻게?
  + 한국 환경에 S/4HANA 적용된 사례 및 Lessons Learned 공유 (S/4HANA 전체, FIORI, Analytics, …)

▣ 2021-04-13, 화
* 출근하자마자, 변동된 인터뷰 일정에 대해 기준정보 담당 정희준 위원님과 논의하고, 기준정보 및 구매ㆍ자재 인터뷰 질의서 File 보낼 것.
* 인터뷰 일정
  + 10시-11:30, MM 공급사/원부자재(수입포함); 박지윤 과장, 장은실 대리
  + 13시-15시,  MM 연구소 원부자재(수입포함); 송신섭 차장(喪), 이승희 대리
  
▣ 2021-04-12, 월
* 한화시스템/ICT 자체 행사(SAP S/4HANA 기반 차세대 ERP 추진 전략 세미나) 차주 4/19, 14~16時로 연기, 4/12 김영진 부장 메일 알림.

▣ 2021-04-06, 화
* 오전 9시, 수출 IT 담당자 대상 Interview
* WBS 검토 결과 회신(박재민 부장님)

▣ 2021-04-05, 월
* Interview 일정
  + 오전 9시, 구매ㆍ자재 및 수입 IT 담당자 대상 Interview
  + 오후 14시, 설비 IT 담당자 대상 Interview

▣ 2021-04-01, 목
* 매주 목요일 오후 4시까지 주간보고 작성할 것. 주간보고서 Template은 ECM에 있음.
* Note 검토 : 2313884 - Simplification List for SAP S/4HANA
  - SAP Readiness Check for SAP S/4HANA [URL](https://help.sap.com/viewer/product/SAP_READINESS_CHECK/200/en-US)에 연결
  - 제대로 환경을 갖춰 Readiness Check를 수행하며, 이 때의 Input이 XML File임.  
    Readiness Check 결과물 중에 고객사 환경에 맞는 Simplification Item Catalog가 있으며 Excel로 받을 수 있음.

▣ 2021-03-31, 수
* 현황 분석(최초 2021-03-30 계획)
  - ITO 담당자에게 Data 요청 메일 발송( → 김정기 차장) 
  - 4Level Process 중심으로 Process Flow 최대한 1장으로 그리기
* Simplification Item Catalog 확인 ( Support Portal 로긴 후 접속할 것. https://launchpad.support.sap.com/#/sic/ )
  - 초기화면 Item 갯수  
    SAP S/4HANA 2020 661 Items, 1909 655 Items, 1809 646 Items, 1709 578 Items, 1610 494 Items  
	  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; On-Premise Edition 1,511 Items  
	  &nbsp; &nbsp; BW/4HANA 2.0 85 Items, 1.0 87 Items

▣ 2021-03-30, 화
* 08:30 Daily Meeting
  - ECM에 인터뷰 일정 오전에 적어 줄 것
  - Conversion 시 BAPI 변경은?
* 현황 분석 (Data -> Process : Botton-up Approach)
  - ㉮ Transaction 데이터 분석
    - ㉠ Process 분석 (= Transaction 데이터 구조 분석)
	    - 4레벨 이상의 프로세스와 4레벨 이하의 Activity 파악. 이때 개선점을 구성할 수 있는 벽돌(질문) 만들 것.
    - ㉡ Transaction 데이터 구성 분석(아래 SQL 참조)
  - ㉯ 기준정보 분석( = 마스터 데이터 분석)
    - ㉠ 기준정보 구조 분석
    - ㉡ 기준정보 구성 분석
  - ㉰ Interface 분석(System Communication 파악; 위 ㉮,㉯의 결과 참조)
    - ㉠ 구성 시스템 파악
    - ㉡ 연결 상태 파악 : 방향, 주기, 양(예:?건/日), CRUD종류, 방식(EAI, 직접), 기술(RFC, Web Service), <Br> &nbsp; &nbsp; 관계(Trxn 흐름, 마스터 복사), 재실행 필요성, 로그 보유 여부
* 참조 SQL - PR, SAP S/4HANA T-Code "ST04 > Diagnostics > SQL Editor" -> 다른 file로 이관함

▣ 2021-03-29, 월
* 08:30 Daily Meeting
  - 권부장님이 보낸 메일 "수행과제 리스트 공유" Review
    - 가. ERP > SCM  
	  ㆍ 업무 범위 분석  
	  ㆍ 업무 Process 관점의 고도화, 개선사항 도출  
	  ㆍ UI/UX 도입 방향 수립(Fiori)  
	  ㆍ DT I/F 변경 영향도 분석  
      ㆍ 상세 수행 로드맵 제시	
    - 나. ERP > PI > 수출입 패키지  
	  ㆍ 수출입 Process 재검토 및 고도화 방안 수립
* Daily Task Planning
  - open.sap.com 정리
  - 현행 Process 정리된 자료 입수 (분석의 Baseline으로서...)
  - (오전 리뷰) 인터뷰 계획서(PPTx), 인터뷰 대상 리스트(Excel) 작성  
    우선 초안을 작성하고 내일 내부 수준 조정하자.  
	ITO를 먼저 만나서 힌트를 얻고 그 이후에 (수준 조정, 내용 세부화 하여) 현업을 만나자.  
* SAP Con. 초빙을 위한 질문 목록 정리 : 메일 이송 완료 (권부장님)
* pm4py : https://pypi.org/project/pm4py/ https://pm4py.fit.fraunhofer.de/docs https://github.com/pm4py
  - 설치 : https://process-mining.tistory.com/3
  - 사용해 보니 불편함이 있고, 그냥 Graphviz를 사용하는 것이 더 나음.

▣ 2021-03-26, 금
* 케미칼 메신저 조직도 확인
  + 한화솔루션/케미칼 > 기획부문 > Digital Core팀 > Partner > Partner_SAP : 이 이하에 Planning Project 인원 및 다른 프로젝트 인원들이 있음.
  + 한화솔루션/케미칼 > 기획부문 > Digital Core팀 > 케미칼ITO팀 : 한만형 차장
* SAP Activate Methodology 확인  
  1) open.sap.com > s4h19 "Guide Your SAP S/4HANA Project to Success" 참조
* Kick-off Meeting : 14시, 22층 대회의실
* Notepad++ 설치(압축해제)  
  참조 Site : 설치 - https://notepad-plus-plus.org/downloads ; 정보 - https://bigboy7.tistory.com/19
* 현행화된 To-Be Process 요청함
  + ECM에 있는 To-Be Process 관련 URL
    ECM\부서문서함\10. DT_통합PI (PwC 공유 폴더)\06. 프로세스 및 시스템 설계\Procurement PI\01.To-Be 프로세스

▣ 2021-03-24, 수
* SAP Activate Methodology
  - Overview 부분 읽기 [URL](https://go.support.sap.com/roadmapviewer/#/group/AAE80671-5087-430B-9AA7-8FBE881CF548/roadmapOverviewPage/S4HANATRANSONPRE)

▣ 2021-03-23, 화
* 10시 : 수행계획서 검토, 전인원 참석
* 보안서약서 제출
* 한화케미칼 Mail 계정 신청 처리됨 : heesang.p@hanwha.com 사용 등록
* Network 및 PC 설정
  + 기소유 PC : 아래 절차에서 "iii) Network 접속"만 설정
  + 임대 PC : 아래 절차 모두 실행
    - i) CMOS 암호 : 사용자이름(영문모드에서 한글 성명 그대로 입력)
    - ii) Window 로긴 암호 : 영 7개 (☞ 0000000), 메일 pwd와 같음
    - iii) Network 접속 : HCC_SECURED 선택, 계정 및 암호 : 사번 / 사번
* 21층 프로젝트룸 복합기 설치
  - ㄱ. 드라이버 설치 : http://172.19.106.250/191009.htm
  - ㄴ. 2번 프린터 설치하기 - 기종 : Cannon ImageRUNNER ADVANCE C3525
  - ㄷ. 프린터 IP Address : 172.19.117.55
* ERP 영역 수행에 대한 의견 교환 (w/ PM) ☞ 아래 ㄱ과 ㄴ은 목요일 전 인원 합류 후 전달 예정
  - ㄱ. ERP 영역 담당자들에게 Conversion Project에 대한 의견 및 정보 요청
    - (과거 경험에 근거한) Planning+Conv. Project "WBS/Task, 산출물/Template, Lessons Learned"
  - ㄴ. 같은 인원 대상으로 (차주 실행 예상되는) SAP Consultant에게 문의할 사항 요청 : SAP Consultant 대상 질문 List  
    &nbsp; &nbsp; (요청 시 다른 분들과의 소통 고도화를 위해 아래와 같은 '질문 목록"의 사례 제시)
    - 기존에 작성했던 표 참조 : Task vs R&R, 시기, 준비 및 결과물, 선제시 사항은?
    - 참조할 Support Portal Notes 안내
    - 기능 리스트들 중에 Guide할 사항은?  
      → 신규, 변경, 삭제 중 변경ㆍ삭제는 이관 오류 해결 시 걸러질 것 같은데, 신규를 얼마나 감안해야 할지가 문제임.  
      &nbsp; &nbsp; 국내 실정을 고려하여 '신규' 기능/Process 중에 도입 추천하는 기능/Process는 있는가?
* SAP Jam 로긴 관련 “https://www.sap.com” Site에서 문의 (3/30 sungmin.hwang@sap.com 다시 문의함)  
  2021-04-09 현재, park.heesang@hanwha.com <--연결--> S0023118924  (hwcs/4hanaplanning)  
  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; wellorg@hanmail.net     <--연결--> P2003707882  (자주 사용하는...  )
  + 자사의 BC담당자로부터 S-ID(S0023118924)를 부여받아 다음 Site들을 접속했습니다.
    - https://support.sap.com 
    - https://community.sap.com 
    - https://go.support.sap.com/roadmapviewer 
  + S/4HANA Conversion에 관심이 많아 roadmap viewer를 보던 중 우측 화면에 소개된 Site인 SAP Jam에도 가 봤으며  
    ID가 필요한 것 같아 Guest ID를 사용하고 있는 메일 ID로 등록했습니다. ☞ Roadmap Viewer에서 연결된 SAP Jam Site [URL](https://jam4.sapjam.com/groups/about_page/764DdnIM50owQEj5mc5bW4)
  + S-ID로 로긴된 상태에서 SAP Jam에 접속하여 최초 나오는 Popup에서 Guest를 선택하고  
    등록 시 설정한 Mail ID와 비밀번호를 입력하면 다음과 같은 Popup 메시지가 나타납니다.
    - SAP - SAP Jam  
      SAP ID로 등록된 이메일 주소 'park.heesang@hanwha.com'(이)가 이 시스템에 초대되지 않았습니다.  
      원래 그룹 초대장을 보낸 사람에게 연락하여 'park.heesang@hanwha.com' 주소로 초대해 주도록 요청하십시오.
  + https://support.sap.com 에서 로그아웃하고 https://jam4.sapjam.com 에 접속하여 위 mail ID와 기억하고 있는 비밀번호로  
    로긴 시도하면 다음과 같은 메시지가 나타납니다.
    - 사용자 이름과 암호가 일치하지 않습니다.  
      다른 SuccessFactors 모듈이 활성화되어 있는지 확인하십시오(예: 목표 관리, 성과 관리 또는 채용).  
      회사의 SuccessFactors 포털을 통해 Jam에 로그인해야 할 수 있습니다.
  + 상황은 위와 같으며, 결론적으로 여쭤보고 싶은 것은 다음과 같습니다.
    1. 활성화(Activate) 처리한 제 Mail ID park.heesang@hanwha.com 으로 SAP Jam에 로긴하려면 어떻게 해야 하는지요?  
      SAP에서 뭔가 처리해 주실 일이 있다면 처리 부탁드립니다.  
      또는 제가 뭔가 해야한다면 적절하게 안내해 주시면 좋겠습니다.  
    2. 추가적으로, 위의 메시지 중 "원래 그룹 초대장을 보낸 사람"은 누구를 말하는 것인가요?  
      S-ID를 부여한 BC 담당자를 말하는 것인가요?
  + 답변 및 처리 부탁드립니다. 감사합니다.

▣ 2021-03-22, 월  
* 한화 시스템 행정처리 요약  
  - P210143	: 한화솔루션/케미칼 SAP 고도화 Planning  
    3/29 도서인쇄비-도서구입비 처리 : SAP S/4HANA Planning 시 활용(참조-도서명: SAP HANA 2.0 공식 가이드북)  
  - 게시글 : 사외위탁/사내교육 신청 방법 안내 [20200211](http://snc.eagleoffice.co.kr/neo/bbs/C/19662/002369625), 온라인 교육 [20210119](http://snc.eagleoffice.co.kr/neo/bbs/C/19722/002372158)
* 시스템 환경  
  + Local 폴더  
    내 PC\로컬 디스크 (C:)\사용자\heesang.p\바탕 화면\ERP_Planning\Temp  
    C:\Users\heesang.p\Desktop\ERP_Planning\Temp  
  + ECM  
    - Project 폴더 : ECM\부서문서함\37. SAP 고도화  
  	- 참조 정보  
  	  - MDM PI 산출물 : ECM\부서문서함\10. DT_통합PI (PwC 공유 폴더)\08. 산출물\Master Data Management(MDM)  
  	  - Commodity Mgmt: ECM\부서문서함\10. DT_통합PI (PwC 공유 폴더)\00. 컨설팅사 사전 제공 자료\09. SAP material\DT related SAP@한화토탈  
          → 3.SAP Commodity Mgmt 소개_20190422_전달.pdf
  + 사용 메일(Mail) 계정 : 프로젝트=Chemical Mail, 회사업무=System Mail  
    - System Mail   : MS Outlook 사용 또는 https://snc.eagleoffice.co.kr 또는 https://owa.hsnc.hanwha.com  
    - Chemical Mail : MS Outlook 사용 또는 https://owa.hcc.hanwha.com  
  + 접속 가능한 SAP System  
    - 가. 자사 S/4HANA 1909 Fully Activated Appliance (S4H_SCM_19 또는 SAP_MM_DEM / Welcome1), 172.16.28.45 / 10 / S4H
      - Fiori LaunchPad : https://172.16.28.45:44310/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html
      - WebGui(웹구이, Web Gui) : https://172.16.28.45:44310/sap/bc/gui/sap/its/webgui 
  	- 나. 한화 솔루션/케미칼 : SAP ERP 6.0 EHP4 (BASIS: SAP Netweaver 7.01) 
  	  - QAS (S4P02 / hwcs/4hana), 172.19.116.162 / 02 / HEQ ☞ (S-User ID 또는 S-ID : S0023118924 / PWD : hwcs/4hanaplanning)
  	  - 2020년 11월 4일 복사함. ∴ 2020년10월 물류 Data까지는 유효한 것임.
  	  - SE43을 통해 확인한 영역 메뉴 : ZAMM, ZASD, ZAPM, ZCMMS (I/F관리메뉴), ZIM01, ZIM02
  + 한화 솔루션/케미칼 VPN
    - 접속URL : https://hcc-vpn.hanwha.co.kr (로긴 후 OTP인증번호 수신대기 약 10초 내외)
    - 계정 및 패스워드 
      - ㄱ. ID : 이메일 ID (park.heesang)
      - ㄴ. 최초 pwd : 1q2w3e4r! ☞ 12월에 변경한 itc mail 계정의 pwd와 같은 것 사용
    - 해외 사용자(OTP 수신 불가) 경우 Region 을 Outside of Korea 변경 후 로그인
    - 최초 사용 PC에서 프로그램 1회 설치 필요 
      - ㄱ. 2차 인증 후 설치 진행 수락 필요, 설치에 수 분 소요
      - ㄴ. 최초 접속/설치 시 인터넷 익스플로어 사용 권고
  + 한화시스템 게스트사용자 HSNC 네트워크 인증  
    http://www.msftconnecttest.com/redirect → https://hsnc-a.smart.hanwha.com/pc/first_page_2.jsp
  + Notepad++ 다중 백업 설정 : C:\DS\Tools\npp.7.9.5.portable.x64\backup\
  + 윈도우용 Vim 설치( https://www.vim.org/ ) ; 참조 [site](https://kevin0960.tistory.com/entry/VIM-Vi-iMproved-의-명령어-모음)
* 14시 : 수행계획서 검토, 14시, 고현득 차장, HSys. 인원 참석

▣ Memo  
* (학생용) 영어 정리 : 영어는 화가(사진 작가)의 언어다.  
  + Tip  
    - 암기 및 숙달용으로 정리는 했지만, 제2외국어로 배우는 것이므로 읽기, 듣기, 쓰기, 말하기를 될수록 많이 하는 것이 좋다.  
      특히 책을 강세를 살려 소리내어 읽는 것이 도움이 되며, 읽을 때 구지 해석하기 보다는 단어의 대표적인 뜻에 기반하여 십자말풀이 하듯이 읽는 것이 좋다.  
      십자말 풀이식 직독직해가 가능한 이유는 우리말이 영어에 비해 자유도가 높기 때문인 듯 하다(영어는 영사기로 영화 필름을 돌려 상영하는 것과 같이 순서가 정해져 있다).  
    - 때로 문장을 바꿔 써보기(Paraphrase)해 보면 이해도를 깊게 하는데 도움이 된다.
    - 영어식 어순으로 우리말 단어를 나열해 보는 것, 이것은 Paraphrase의 일종이며 머리 속에서 `우리말↔영어`하는 것은 언어 간 말하기·쓰기·읽기의 중간 지대라고 생각된다.
  + 품사 
    - 기존 : 8품사 - 명사, 대명사, 동사, 형용사, 부사, 전치사, 접속사, 감탄사
    - PHS : 4품사 - 문장 구성을 위한 용도로서 구분
      - 결합 사용 : 이름말, 동작말, 묘사말, 연결말  
        이름(명사, 대명사), 동작(동사), 모습·상태_묘사(형용사), 세기·정도·방향_강조(부사), 연결(`5W1H`나 `순서`를 나타냄 : 전치사 = 문장 내 연결, 접속사 = 문장 간 연결)  
        ☞ 읽을 때 잘 이해 안되는 연결어는 그리고(동시 상황, and)로 해석해도 된다(가장 무난한 뜻이며 읽으면서 보정 가능).
      - 단독 사용 : 감탄사
  + 문장 구조 
    - 문장 내 품사 사용 : $\boxed{\text{문장}~:~\text{주어(이름)} + \text{동사} + \text{보충}(\text{이름}_{SC~or~VO} ~ ㆍ ~ \text{묘사}_{SC})} + \text{강조} + \text{내ㆍ간~연결} \rightarrow \boxed{문장} + \text{강조} + \text{내ㆍ간~연결} + \cdots$ 
    - 5형식 : **주어** + **동사** + (주어 또는 동사의)보충어
      - 1,2,3,5형식 : **S** + **V** + 보충어(SC or VO) $= \boxed{Subject} + \boxed{Verb} + \boxed{ ~ \boxed{Subject's~Complement} ~or~ \boxed{Verb's~Object} ~ }$
      - 4형식 : **S** + **V** + 동사보충어(<font color='gray'>IO</font> + DO)
      - 5형식의 C∼O 내에서 C는 주어(S) 역할을 한다.
  + 시제 : 과거 ∼ 현재 ∼ 미래(가정, 추측·의지)
    - 동사 형태와 시제 : 과거(∼ed), 현재(기본, ∼ing : 현재 동작·발생 진행), 미래(to do : (현재)→미래)
    - 완료시제 : 기억 속 영화나 사진 한 장면을 떠올리듯이 `(~한 경험을) 가진다`로 해석하여 일반 시제와 같이 취급할 수 있다.  
      $주어 + have + \boxed{주어 + pp} \longrightarrow ( ~ \boxed{종속절} ~주어~생략~및~결합) \longrightarrow 주어 + have + pp$
  + 가정법과 조동사

</div></details>

</div></details> <Br>

# 2. 데이터 과학 정리
<details><summary> Details ============================================================================</summary><div>

※ 이동 : [오늘](#오늘의-일정), [향후 일정](#12-향후-일정), [과거 이력](#13-과거-이력), [책갈피-장기](#111-장기), [책갈피-단기](#112-단기), [책갈피-이력](#113-이력), [2. DS정리](#2-데이터-과학-정리), [3. Links](#3-useful-links)

## 2.1 Web Resources
CheatSheets, Usefule Blogs, Web Resources... (cf: tensorflow privacy https://github.com/tensorflow/privacy ) <details><summary> Details </summary><div> 

|ⓟypi,ⓦiki|Python|numpy|scipy|sympy|matplotlib|pandas|sklearn|pycaret|Tensorflow|statsmodels|rpy2|sqlite|postgresql|re(gexp)|spacy|pytorch|Orange3|
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Homepage|[1](https://docs.python.org/3) [2](https://www.python.org/doc/) <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank">ⓦ</a>|[○](https://numpy.org/) [ⓦ](https://en.wikipedia.org/wiki/NumPy)|[○](https://scipy.org) [ⓦ](https://en.wikipedia.org/wiki/SciPy)|[○](https://www.sympy.org) [ⓦ](https://en.wikipedia.org/wiki/SymPy)|[○](https://matplotlib.org) [ⓦ](https://en.wikipedia.org/wiki/Matplotlib)|[○](https://pandas.pydata.org/) <a href="https://en.wikipedia.org/wiki/Pandas_(software)" target="_blank">ⓦ</a>|[○](https://www.sklearn.org) [ⓦ](https://en.wikipedia.org/wiki/Scikit-learn)|[○](https://pycaret.org),[ⓖ](https://github.com/pycaret/pycaret)|[ⓣ](https://www.tensorflow.org/) [ⓚ](https://keras.io) [ⓦ](https://en.wikipedia.org/wiki/TensorFlow)|[○](https://www.statsmodels.org) [ⓖ](https://github.com/statsmodels/statsmodels) [ⓟ](https://pypi.org/project/statsmodels)|[○](https://rpy2.github.io/)|[1](https://www.sqlite.org) [2](https://docs.python.org/3/library/sqlite3.html) [ⓦ](https://en.wikipedia.org/wiki/SQLite)|[○](https://www.postgresql.org) [○](https://www.psycopg.org) [ⓦ](https://en.wikipedia.org/wiki/PostgreSQL)|[○](https://docs.python.org/3/library/re.html) [○](https://pypi.org/project/regex) [ⓦ](https://en.wikipedia.org/wiki/Regular_expression)|[○](https://spacy.io/) [ⓟ](https://pypi.org/project/spacy/) [ⓦ](https://en.wikipedia.org/wiki/SpaCy)|[EN](https://pytorch.org) [KO](https://pytorch.kr/get-started/locally/)||
|Tutorial|[○](https://docs.python.org/3/tutorial/)|[○](https://numpy.org/doc/stable/user/tutorials_index.html)|[○](https://docs.scipy.org/doc/scipy/reference/tutorial)|[○](https://docs.sympy.org/latest/tutorial/index.html)|[○](https://matplotlib.org/stable/tutorials/index.html)|[○](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html)|[○](https://www.sklearn.org/tutorial/index.html) [map](https://www.sklearn.org/tutorial/machine_learning_map/index.html)|[○](https://pycaret.readthedocs.io/en/latest/tutorials.html)||[○](https://www.statsmodels.org/stable/user-guide.html)|[○](https://rpy2.github.io/doc/latest/html/introduction.html)|||[○](https://docs.python.org/3/howto/regex.html)|[○](https://spacy.io/usage/spacy-101)|[EN](https://pytorch.org/tutorials/) [KO](https://tutorials.pytorch.kr/)||
|(API)Ref.|[lib](https://docs.python.org/3/library) [ref](https://docs.python.org/3.9/reference)|[○](https://numpy.org/doc/stable/reference/)|[○](https://docs.scipy.org/doc/scipy/reference/)|[○](https://docs.sympy.org/latest/index.html)|[○](https://matplotlib.org/stable/contents.html)|[○](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)|[○](https://www.sklearn.org/modules/classes.html)|[○](https://pycaret.readthedocs.io/en/latest/api/classification.html)||[○](https://www.statsmodels.org/stable/api.html)|[○](https://rpy2.github.io/doc/latest/html/index.html)||||[○](https://spacy.io/api)|[○](https://pytorch.org/docs/stable/index.html)||
|CheatSheet||[1](https://github.com/rougier/numpy-100) [2](https://www.kaggle.com/utsav15/100-numpy-exercises) [3](http://taewan.kim/post/numpy_cheat_sheet)||||[1](https://towardsdatascience.com/pandas-cheat-sheet-7e2ea6526be9) [2](https://www.dataquest.io/blog/pandas-cheat-sheet/) [3](https://www.educative.io/blog/python-pandas-tutorial) [4](https://github.com/corazzon/cracking-the-pandas-cheat-sheet)|[○](https://www.datacamp.com/community/blog/scikit-learn-cheat-sheet)|[Guide](https://pycaret.org/guide/)|||||||[①](https://www.datacamp.com/community/blog/spacy-cheatsheet)|[○](https://tutorials.pytorch.kr/beginner/ptcheat.html)||
|Web Ref.|[1](https://edu.dojang.io/course/view.php?id=11 "코딩도장, wellorg/6월-한화케미칼-長") [2](https://dojang.io/course/view.php?id=7 "코딩도장 - 일반") [3](https://wikidocs.net/book/1 "Jump to Python, 박응용") [4](https://wikidocs.net/book/4606 "Practical Python Programming, David Beazley") [5](https://wikidocs.net/book/5445 "파이썬 필수 Library, 박응용") [6](https://wikidocs.net/book/4542 "Jump to Flask, 박응용") [7](https://wikidocs.net/book/4223 "Jump to django, 박응용") [T](https://www.tutorialspoint.com/python)|[①](https://www.tutorialspoint.com/numpy)|[①](https://www.tutorialspoint.com/scipy)|[①](https://www.tutorialspoint.com/sympy)|[1](https://www.tutorialspoint.com/matplotlib) [seaborn](https://www.tutorialspoint.com/seaborn)|[①](https://www.tutorialspoint.com/python_pandas)|[①](https://www.tutorialspoint.com/scikit_learn) [②](https://www.datacamp.com/community/tutorials/machine-learning-python)||[ⓣ](https://www.tutorialspoint.com/tensorflow) [ⓚ](https://www.tutorialspoint.com/keras) [ⓚ2](https://www.tutorialspoint.com/deep_learning_with_keras)|[통계](https://www.tutorialspoint.com/statistics) [patsy](https://github.com/pydata/patsy)||[1](https://www.sqlitetutorial.net/) [2](https://www.tutorialspoint.com/sqlite) [3](https://www.tutorialspoint.com/python_sqlite)|[①](https://www.postgresqltutorial.com/) [②](https://www.tutorialspoint.com/postgresql) [③](https://www.tutorialspoint.com/python_postgresql)|[①](https://regexone.com/)|[nltk](https://www.nltk.org) [nlp](https://www.tutorialspoint.com/natural_language_processing)|||
</div></details> <Br> <!-- 2.1 Web Resources -->

## 2.2 환경 설정
<details><summary> Details ────────────────────────────────────────────────────</summary><div>

* 회사 노트북(ITC)  
  + tf2 environment (2021-05-17)  
    - Orange 설치 : 실행 "orange-canvas" 또는 "orange-canvas --help"
      - conda install -c anaconda anaconda-navigator # 참조 : anaconda navigator 설치  
      - conda install -c conda-forge orange3 # 참조 : https://anaconda.org/ales-erjavec/orange3
        - 오류 발생 : ImportError: DLL load failed while importing QtCore: 지정된 모듈을 찾을 수 없습니다.
* 회사 노트북(케미칼)
  + openjdk 설치 [github](https://github.com/ojdkbuild/ojdkbuild) ( ☜ 참조 [Blog](https://blog.naver.com/vixlee/222285976728) ) 
    - JRE Zip file 내려받아 압축 풀고, %JAVA_HOME% "C:\Program Files\Java\jre-1.8.0.292"와 같이 설정함
  + R 설치 : jamovi를 활용하거나, R을 설치, 이후 %R_HOME% "C:\Program Files\R\R-4.0.4"와 같이 설정함
  + [오렌지3](https://orangedatamining.com/) : <font color='gold'><B>workflow 위주로 scikit-learn이나 pycaret과 비교하며 학습 실행</B></font>
    - 실행 방법
      - foreground : C:\DS\Orange3-3.28.0>Scripts\orange-canvas 또는 C:\DS\Orange3-3.28.0>python -m Orange.canvas
      - background : C:\DS\Orange3-3.28.0>start /b scripts\orange-canvas 또는 C:\DS\Orange3-3.28.0>start /b python -m Orange.canvas
    - 권장 설치 : anaconda → 가상 환경 생성 → "**pip install pycaret → TF & Keras**" → (...) → [pip](https://pypi.org/project/Orange3/) install Orange3 및 Add-Ons
      - $\boxed{Java,~R,~VC} \rightarrow \boxed{Anaconda~~ \boxed{conda~cuda~2EA} \rightarrow \boxed{pip~pycaret[full]} \rightarrow \boxed{pip~tensorflow} \rightarrow \boxed{pip~Orange3}}$
      - conda create -n orange python # python 3.9.5 설치됨
      - pip install pycaret[full] # https://pycaret.org/ 2021-05-21 실행
      - pip install tensorflow tensorflow-datasets tensorflow-lattice
      - pip install rpy2 sympy pydot pydotplus mglearn beautifulsoup4 bokeh plotnine tpot
      - pip install scikit-image scikit-fuzzy scikit-optimize scikit-plot
      - pip install scikit-surprise scikit-survival
      - pip install hdbcli hana_ml
      - pip install -U plaidml-keras plaidbench 
      - plaidml-setup # Prompt : ① Device Support : Y , ② 2 , ③ (저장) Y
      - pip install keras-tuner autokeras
      - pip install Orange3 Orange-Spectroscopy
      - pip install Orange3-Associate Orange3-Bioinformatics Orange3-Educational Orange3-Explain Orange3-Geo Orange3-ImageAnalytics Orange3-Prototypes Orange3-Survival-Analysis Orange3-Text Orange3-Textable Orange3-Timeseries `# Orange3-Network`
      - conda install -c anaconda pywin32
      - jupyter notebook> !dir c:\Users\user\AppData\Local\r-miniconda\envs\orange\Lib\site-packages\Orange\widgets\*.py /b
      - jupyter notebook> !dir c:\Users\user\AppData\Local\r-miniconda\envs\orange\Lib\site-packages\Orange\widgets\model\*.py /b
    -  참고
       - Orange3 [Homepage](https://orangedatamining.com/), [docs](https://orangedatamining.com/docs/), [pip](https://pypi.org/project/Orange3/), [YouTube Tutorial](https://www.youtube.com/watch?v=HXjnDIgGDuI&list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy)
       - Blog [AI오디세이](http://www.aio.world/news/articleView.html?idxno=258), [ML 야학 소개](https://blog.naver.com/adler0912/222202689101) ☞ [ML 야학](https://yah.ac/orange3) 및 [YouTube 목록](https://www.youtube.com/playlist?list=PLuHgQVnccGMAwnfp3Ml-XY1WNx1MPgrQ4)
    - Portable Orange **<font color='gold'>설치 세부 사항</font>** (cf: Data 파일 위치 : C:\DS\Orange3-3.28.0\Lib\site-packages\Orange\datasets)
      - C:\DS\Orange3-3.28.0>python --version # Python 3.8.8
      - C:\DS\Orange3-3.28.0>python -m pip install --upgrade pip
      - C:\DS\Orange3-3.28.0>python -m pip install pycaret # https://pycaret.org/ → pip install pycaret[full]
      - C:\DS\Orange3-3.28.0>python -m pip install graphviz
      - C:\DS\Orange3-3.28.0>python -m pip install catboost # pycaret 설치 시 graphviz 없다고 설치 안 됨
      - C:\DS\Orange3-3.28.0>python -m pip install statsmodels sympy
      - C:\DS\Orange3-3.28.0>python -m pip install rpy2
      - C:\DS\Orange3-3.28.0>python -m pip install tensorflow tensorflow-datasets tensorflow-lattice
      - C:\DS\Orange3-3.28.0>python -m pip install pydot pydotplus
      - C:\DS\Orange3-3.28.0>python -m pip install beautifulsoup4 db-sqlite3 sqlite-utils JPype1 mglearn bokeh plotnine tpot
      - C:\DS\Orange3-3.28.0>python -m pip install opencv-python opencv-contrib-python opencv-python-headless scikit-mdr scikit-image scikit-fuzzy scikit-optimize tzlocal vpython  
        ☞ conda의 경우  scikit-surprise scikit-survival 설치 가능 # error: Microsoft Visual C++ 14.0 is required.
      - C:\DS\Orange3-3.28.0>python -m pip install hdbcli   # pip install hdbcli-2.7.23-cp36-cp36m-win_amd64.whl
      - C:\DS\Orange3-3.28.0>python -m pip install hana_ml  # pip install hana_ml-2.6.21012600-py3-none-any.whl
      - C:\DS\Orange3-3.28.0>pip install -U plaidml-keras plaidbench # https://github.com/plaidml/plaidml 참조, Visual C++ 2015 설치 필요
      - C:\DS\Orange3-3.28.0>Scripts\plaidml-setup # Prompt : ① Device Support : Y , ② 2 , ③ (저장) Y
      - C:\DS\Orange3-3.28.0>python -m pip install keras-tuner # https://github.com/keras-team/keras-tuner
      - C:\DS\Orange3-3.28.0>python -m pip install autokeras # https://autokeras.com/install/
      - C:\DS\Orange3-3.28.0>python -m pip install Orange-Spectroscopy Orange3-모듈명  
        ☞ 모듈명 = Associate Bioinformatics Educational Explain Geo ImageAnalytics Network Prototypes Survival-Analysis Text Textable Timeseries
      - C:\DS\Orange3-3.28.0>python -m pip install jupyterlab # (jupyter notebook 실행해도) win32api.dll 찾지 못하는 오류때문에 설치했으나, 해결되지 않음.<Br>☞ 필요 시 `pip install -U pywin32` 실행 후 [pywin32 homepage](https://github.com/mhammond/pywin32) 방문하여 script `python Scripts/pywin32_postinstall.py -install` 확인 및 실행 
</div></details> <Br> <!-- 2.2 환경 설정 -->

## 2.3 Machine Learning
<details><summary> Details ────────────────────────────────────────────────────</summary><div>

### 2.3.1 Orange3
* Orange3 YouTube 동영상 <details><summary>Details</summary><div>
  |[Orange Data Mining](http://orange.biolab.si/)|Status|Web Resources|Status|
  |:---|:--:|:---|:--:|
  |Tutorial - [Getting Started with Orange](https://www.youtube.com/playlist?list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy)||엘리쌤의 [Orange3 데이터 분석, 머신러닝](https://www.youtube.com/playlist?list=PL3geb_qrBQYfOmGuHtnf0RZMMXaev-Zvr)||
  |&nbsp; &nbsp; 01: Welcome to Orange Data mining ||&nbsp; &nbsp; 01 : 설치하기 (install)|20210612|
  |&nbsp; &nbsp; 02: Data Workflows||&nbsp; &nbsp; 02 : 오렌지 살펴보기|20210612|
  |&nbsp; &nbsp; 03: Orange Widgets and Channels||&nbsp; &nbsp; 03 : 위젯 추가하기 (Add-on)|20210612|
  |&nbsp; &nbsp; 04: Loading Your Data||&nbsp; &nbsp; 04 : 데이터준비, 머신러닝 과정|20210612|
  |&nbsp; &nbsp; 05: Hierarchical Clustering||&nbsp; &nbsp; 05 : 선형회귀 (Linear Regression)|20210612|
  |&nbsp; &nbsp; 06: Making Predictions||&nbsp; &nbsp; 06 : 데이터 가져오기|20210616|
  |&nbsp; &nbsp; 07: Model Evaluation and Scoring||&nbsp; &nbsp; 07 : 주택가격예측 (1)|20210616|
  |&nbsp; &nbsp; 08: Add-ons||&nbsp; &nbsp; 08 : 주택가격예측 (2) - MSE, RMSE, MAE, R2|20210616|
  |&nbsp; &nbsp; 09: Principal Component Analysis||&nbsp; &nbsp; 09 : Test and Score (1) Train, Test, Evaluate|20210616|
  |&nbsp; &nbsp; 10: Feature Scoring and Ranking||&nbsp; &nbsp; 10 : Test and Score (2)|20210616|
  |&nbsp; &nbsp; 11: k-Means||&nbsp; &nbsp; 11 : iris 분류 (1)|20210616|
  |&nbsp; &nbsp; 12: k-Means Clustering||&nbsp; &nbsp; 12 : iris 분류 (2)|20210616|
  |&nbsp; &nbsp; 13: Silhouette||&nbsp; &nbsp; 13 : iris 분류 (3) - test and score 위젯 `AUC,CA,F1,Precision,Recall` ☞ 참조 [1](https://pacientes.github.io/posts/2021/01/ml_precision_recall/) [2](https://wooono.tistory.com/232)|20210616|
  |&nbsp; &nbsp; 14: Image Analytics - Clustering||&nbsp; &nbsp; 14 : Tree, Tree View  (1)|20210616|
  |&nbsp; &nbsp; 15: Image Analytics - Classification||&nbsp; &nbsp; 15 : Tree, Tree View  (2)|20210616|
  |&nbsp; &nbsp; 16: Text Preprocessing||&nbsp; &nbsp; 16 : Data Sampler (1)|20210616|
  |&nbsp; &nbsp; 17: Text Clustering||&nbsp; &nbsp; 17 : Data Sampler (2) - <font color='gold'>Load → Table → Sampler $\rightrightarrows$ **Test and Score** ← model(s)</font>|20210616|
  |&nbsp; &nbsp; 18: Text Classification||&nbsp; &nbsp; 18 : Box Plot  (1)|20210616|
  |&nbsp; &nbsp; 19: How to Import Text Documents||&nbsp; &nbsp; 19 : Box Plot  (2)|20210616|
  |&nbsp; &nbsp; 20: Multivariate Projection - Freeviz||&nbsp; &nbsp; 20 : 계층적 군집화||
  |&nbsp; &nbsp; [All Tutorial](https://www.youtube.com/watch?v=NEEEUOmYRd8)||&nbsp; &nbsp; 21 : Hierarchical Clustering 위젯||
  |||&nbsp; &nbsp; 22 : k-means 군집화||
  |생활코딩 [Orange3 지도학습](https://www.youtube.com/playlist?list=PLuHgQVnccGMCIA_MXFcS-IWrqKnx62Iwp)||&nbsp; &nbsp; 23 : 이미지 군집화||
  |&nbsp; &nbsp; 1. 수업소개||&nbsp; &nbsp; 24 : 이미지 분류||
  |&nbsp; &nbsp; 2. 지도학습의 기본방법||&nbsp; &nbsp; 25 : 유사 이미지 찾기||
  |&nbsp; &nbsp; 3.1. 보다 현실적인 사례||&nbsp; &nbsp; 26 : neighbors 위젯||
  |&nbsp; &nbsp; 3.2. 경쟁시키기||&nbsp; &nbsp; 27 : 텍스트데이터 전처리, 워드클라우드||
  |&nbsp; &nbsp; 3.3. 평가하기||&nbsp; &nbsp; 28 : 워드클라우드 (2)||
  |&nbsp; &nbsp; 3.4. 공정하게 평가하기||&nbsp; &nbsp; 29 : 텍스트 군집화||
  |&nbsp; &nbsp; 4.1. 분류문제 소개||&nbsp; &nbsp; 30 : 텍스트 분류||
  |&nbsp; &nbsp; 4.2. 분류학습방법선발전||&nbsp; &nbsp; 31 : 텍스트 문서 가져오기||
  |&nbsp; &nbsp; 4.3. 모델비교||&nbsp; &nbsp; 32 : 코로나 (COVID-19) 확진자 현황 데이터 살펴보기 (JHU)||
  |&nbsp; &nbsp; 5. 수업을 마치며||&nbsp; &nbsp; 33 : 코로나 (COVID-19) 확진자 현황 데이터를 Line Plot으로 살펴보기||
  |||&nbsp; &nbsp; 34 : 코로나 (COVID-19) 확진자 현황 데이터를 지도(Map)에 표시하기||
  |`CyVerse.org` [Machine Learning](https://www.youtube.com/playlist?list=PL38WPXpo-ZW3uaGT98nxB2cryoUNTbOu1) [1](https://www.youtube.com/watch?v=s9DOBPlDZ3U) [5](https://www.youtube.com/watch?v=zCksDE5e2Lc&list=PL38WPXpo-ZW3uaGT98nxB2cryoUNTbOu1&index=5)||&nbsp; &nbsp; 35 : 코로나 (COVID-19) 확진자 현황 데이터를 지도에 애니메이션으로 나타내기||
  |Nathan Humphrey, Time-Series Forecasting with [Orange](https://www.youtube.com/watch?v=bpPwDMmouyU)||&nbsp; &nbsp; 36 : 코로나 (COVID-19) 데이터에 HDI 데이터를 추가해서 함께 살펴보기||
  |Orange walkthrough with [Dr. Chreston Miller](https://www.youtube.com/watch?v=_yK93gPdTew)||&nbsp; &nbsp; 참고 : Anaconda Navigator에서 Orange 실행하기|20210612|
  |Orange and Python [URL](https://www.youtube.com/watch?v=GKuarDoHo44)||&nbsp; &nbsp; 참고 : 통합데이터지도 `bigdata-map.kr`||
  |Dr. Juan Klopper [Modelling using Orange](https://www.youtube.com/watch?v=L32c8CLq9SU), [Python Scripts](https://www.youtube.com/watch?v=vyeJ3MicrBg)||||
</div></details> <Br> <!-- 2.3 Machine Learning -->
</div></details> <Br> <!-- 2. 데이터 과학 정리 -->

# 3. Useful Links
<details><summary> Details ============================================================================</summary><div>

※ 이동 : [오늘](#오늘의-일정), [향후 일정](#12-향후-일정), [과거 이력](#13-과거-이력), [책갈피-장기](#111-장기), [책갈피-단기](#112-단기), [책갈피-이력](#113-이력), [2. DS정리](#2-데이터-과학-정리), [3. Links](#3-useful-links)

## 3.1 Books & References
<details><summary> Details </summary><div>  <!-- https://hanwhasystemsict.dkyobobook.co.kr/ 사번/써클비번 -->

|저자|출간일|제목|위치|읽은 날|내역|
|:---|:--:|:---|:--:|:---|:---|
|Aurélien Géron|2019-10-15|Hands-On Machine Learning, 2/E|ⓜ⒣⒮|||
|최건호|2019-06-07|파이토치 첫걸음|⒣|||
|김기현|2019-07-01|자연어 처리 딥러닝 캠프: 파이토치편|⒣|||
|김건우|2019-11-01|펭귄브로의 3분 딥러닝 파이토치맛|⒣|||
|기운|2020-12-15|p5 자바스크립트와 ml5 머신러닝라이브러리|[⒲](https://wikidocs.net/book/5373)|||
|양식-저자|양식-일자|양식-제목|양식-위치|양식-읽은 날|내역, github위치 등... 행삽입 Template|

ⓜ 소장 도서 『⒨ 괄호=e-Book』, ⒣ 회사 e-Book, ⓢ 서울도서관, ⓔ 서울교육청, ⓓ 양천구 도서관, ⒲ [wikidocs](https://wikidocs.net/)
</div></details> <Br> 

## 3.2 SAP
* [SAP S/4HANA Tutorial](https://education.hana.ondemand.com/education/pub/s4/index.html) 
  + 2020 - On-Premise [Tutorials Library](https://education.hana.ondemand.com/education/pub/s4/index.html#group!GR_B1F7108C1B4D3086)<details><summary>Details</summary><div>
    - Getting Started
      - Working with the Launchpad (한국어 번역)
      - Working with Apps (한국어 번역)
    - Task 
      - Finance
      - Supply Chain
      - Manufacturing
      - Sales
      - Application Platform and Infrastructure
      - Sourcing and Procurement
      - R&D / Engineering
    - Implementation and Configuration
      - SAP S/4HANA Data Migration
      - SAP Best Practices Explorer for SAP S/4HANA
      - Getting Access to an SAP S/4HANA Trial System
      - Conerting to SAP S/4HANA
      - Master Data Governance and Data Quality Management <!-- </div></details> 2020 - On-Premise Tutorials Library -->
* SAP [Help Portal](https://help.sap.com/) > [S/4HANA](https://help.sap.com/viewer/8308e6d301d54584a33cd04a9861bc52/2020.002/en-US/2c0e7c571fbeb576e10000000a4450e5.html) [On-Premise](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE), [제품 버전 2020 모두 보기](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE/2020/en-US?expandAll=true) ☞ 과거 버전 참조 : [4.6C](https://help.sap.com/doc/saphelp_46c/4.6C/en-US/e1/8e51341a06084de10000009b38f83b/frameset.htm), [4.7](https://help.sap.com/doc/saphelp_470/4.7/en-US/e1/8e51341a06084de10000009b38f83b/frameset.htm), [ECC 6.0](https://help.sap.com/viewer/9cba3865dd7248f5abd4330b4e7cfc84/6.17.17/en-US) <details><summary>TAB Pages</summary><div>
  + [Discover](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE/2020/en-US?task=discover_task) : [Cloud 제품 소개](https://www.sap.com/products/s4hana-erp.html), [S/4HANA Trials](https://help.sap.com/viewer/disclaimer-for-links?q=https://www.sap.com/cmp/oth/crm-s4hana/index.html), S/4HANA 및 DB FAQ [PDF](https://help.sap.com/doc/9125f26bceff4fe39e197740e5c6aeb0/1511%20000/en-US/FAQ_HANA2_S4H.pdf)
    - Getting Started Guide [pdf](https://help.sap.com/doc/819cdef021e44d7aad27b31c8bb1ebfc/2020/en-US/START_OP2020.pdf), Feature Scope Description [pdf](https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2020.latest/en-US/FSD_OP2020_latest.pdf)
    - Product Assistance [SAP Help URL](https://help.sap.com/viewer/8308e6d301d54584a33cd04a9861bc52/2020.001/en-US)
    - SAP Best Practices [Explorer](https://rapid.sap.com/bp/#/browse/packageversions/BP_OP_ENTPR)
    - Compatibility Packs : [PDF](https://help.sap.com/doc/pdfac0fa9551dd88809f10000000b441570/1511%20000/en-US/MATRIX_OP1511.pdf), [FAQ](https://help.sap.com/doc/7a02948aad1141429024a449a4bb14b9/1511%20000/en-US/CP_FAQ.pdf), [Note](https://help.sap.com/viewer/disclaimer-for-links?q=https://launchpad.support.sap.com/#/notes/2269324)
  + [What's New](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE/2020/en-US?task=whats_new_task)
  + [Implement](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE/2020/en-US?task=implement_task)
    - Guides PDF : [Installation](https://help.sap.com/doc/6b11678926d3409bbfea8897cb34d10f/2020/en-US/INST_OP2020.pdf), [Upgrade](https://help.sap.com/doc/760ce610a2af4174a329d2d8315378e2/2020/en-US/UPGR_OP2020.pdf), [Conversion](https://help.sap.com/doc/2b87656c4eee4284a5eb8976c0fe88fc/2020/en-US/CONV_OP2020.pdf), [Security](https://help.sap.com/doc/d7c2c95f2ed2402c9efa2f58f7c233ec/2020/en-US/SEC_OP2020.pdf), [Operations](https://help.sap.com/doc/6c3b63ec437f421cbfd92d10131cd685/2020/en-US/OPS_OP2020.pdf), UI Technologies [URL](https://help.sap.com/viewer/22bbe89ef68b4d0e98d05f0d56a7f6c8/2020.latest/en-US/4c1048feb4ea4f7d81ccbc47233a0d68.html)
    - Conversion & Upgrade Assets  
      - Simplification Item Catalog(=Online List) [URL](https://help.sap.com/viewer/disclaimer-for-links?q=https://launchpad.support.sap.com/#/sic/), Simplification List for SAP S/4HANA [PDF](https://help.sap.com/doc/e8f908b4892d44ad90e8c582b0cd1866/2020/en-US/SIMPL_OP2020.pdf) ; SAP Readiness Check [URL](https://help.sap.com/viewer/p/SAP_READINESS_CHECK)
      - Custom Code Migration Guide [PDF](https://help.sap.com/doc/9dcbc5e47ba54a5cbb509afaa49dd5a1/latest/en-US/CustomCodeMigration_EndToEnd.pdf), 『Custom Code Mgmt (CCM) [PDF](https://help.sap.com/doc/ef38cd96e03f4c51baf36348ca52b825/1.0/en-US/CCM_CONV.pdf) & Data Volume Mgmt (DVM) [PDF](https://help.sap.com/doc/195dd7408c7447388c1bb9e54a5f6a31/1.0/en-US/DMV_CONV.pdf)』 During an SAP S/4HANA Conversion Project  
    - Data Migration [URL](https://help.sap.com/viewer/29193bf0ebdd4583930b2176cb993268/2020.latest/en-US/a4d4119a2cc9448a98e5d17e6dd0eac4.html)
    - SAP Best Practices : SAP [Best Practices](https://help.sap.com/viewer/disclaimer-for-links?q=https://rapid.sap.com/bp/#/browse/packageversions/BP_OP_ENTPR) for SAP S/4HANA, [Administration Guide](https://help.sap.com/viewer/S4HANA2020_AdminGuide/17d958a88d244ee293aed687f9bfe37f.html) for Implementation, SAP [Roadmap Viewer](https://help.sap.com/viewer/disclaimer-for-links?q=https://go.support.sap.com/roadmapviewer/)
    - Additional Information  
      - SAP Fiori App Reference Library [URL](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/)
      - SAP S/4HANA – FAQs for Release and Maintenance Strategy [PDF](https://help.sap.com/doc/fb3ee8b026b9468890aedd443afb9aae/1511%20000/en-US/ReleaseMainStratS4.pdf)
      - SAP S/4HANA Custom Code Adaption [URL](https://help.sap.com/viewer/disclaimer-for-links?q=https://blogs.sap.com/2017/02/15/sap-s4hana-system-conversion-custom-code-adaptation-process/)
      - SAP S/4HANA Requirements for Partner Solutions: On Premise Guide [PDF](https://help.sap.com/doc/984c8571a7fd49928260294b9e5bd6b2/PG%201.0/en-US/PG_S4HANA.pdf)
      - Tutorials Library [URL](https://education.hana.ondemand.com/education/pub/s4/index.html), S/4HANA On-Premise 2020 [Tutorials](https://education.hana.ondemand.com/education/pub/s4/index.html#group!GR_B06D29AAEF1CFBC)
    - 참고 : [s4h18](https://open.sap.com/courses/s4h18), Week 1, Unit 2, 12 및 15~16쪽  
      ㅇ Planning the UX Scope and Budget > Tools and Resoures for Roles and Apps Scoping
      |Tool / Resource|【 대상|Scenario 】|Remark|
      |:---|--:|:--|:---|
      |1. SAP Fiori Apps Reference Library [URL](https://fioriappslibrary.hana.ondemand.com/)|New Implementation|System Conversion||
      |2. Best Practices Explorer [URL](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/on-premise)|New Implementation|||
      |3. SAP Readiness Check [URL](http://www.sap.com/readinesscheck)||System Conversion|SAP ERP 및 S/4HANA에서 실행 가능|
      |4. FAR(Fiori Apps Recommendations) Report [URL](http://www.sap.com/FAR)||System Conversion|SAP ERP 및 S/4HANA에서 실행 가능|  
  + [Integrate](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE/2020/en-US?task=integrate_task) : 41 Items, Products with Integration Capability (Add-ons and products that can be integrated with SAP S/4HANA)
    - Integration of SAP Mobile Platform into SAP Fiori Landscape
    - SAP [Business Partner Screening](https://help.sap.com/bps_s4) for SAP S/4HANA
    - SAP [Screen Personas](https://help.sap.com/viewer/product/SAP_SCREEN_PERSONAS/Current/en-US)
  + [Use](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE/2020/en-US?task=use_task) : [Product Assistance](https://help.sap.com/viewer/8308e6d301d54584a33cd04a9861bc52/2020.latest/en-US)  
  + [Learn and Get Certified](https://help.sap.com/viewer/product/SAP_S4HANA_ON-PREMISE/2020/en-US?task=learn_task) : 46 Learning Journeys
    - [ABAP](https://help.sap.com/doc/abapdocu_751_index_htm/7.51/en-US/index.htm?file=abenabap.htm) Programming - Upskilling from SAP ERP to SAP S/4HANA, SAP S/4HANA - Programming
    - Design Thinking and Business Model Innovation - Methodology and Tools
    - SAP S/4HANA - Analytics
    - SAP S/4HANA - Sourcing and Procurement, SAP S/4HANA - Sourcing and Procurement Upskilling for SAP ERP Experts
    - SAP S/4HANA - Technical Implementation and Operations
    - SAP S/4HANA - Scope and Business Processes
    - SAP S/4HANA - Implementation Tools and Methodology (SAP Activate)
    - SAP User Experience Management by Knoa
    - SAPUI5 and SAP Fiori Applications <!-- </div></details>  SAP Help Portal Tab Pages -->
* openSAP : Open Online [Courses](https://open.sap.com/courses) by SAP <details><summary>과정 및 내역</summary><div> <!-- 2021년4월 한화케미칼 SAP 고도화 프로젝트를 하면서 수강 시작함(長), wellorg@hanmail.net -->
  |구분|과정|시작일|과정명|완료 여부|
  |:--|:--|:--:|:--|:--:|
  |S/4HANA|[s4h1](https://open.sap.com/courses/s4h1)|20150325|SAP S/4HANA in a Nutshell||
  ||[s4h2](https://open.sap.com/courses/s4h2)|20150616|SAP S/4HANA – Deep Dive||
  ||[s4h3](https://open.sap.com/courses/s4h3)|20151104|SAP S/4HANA – Use Cases||
  ||[s4h4](https://open.sap.com/courses/s4h4)|20160308|Implementation of SAP S/4HANA||
  ||[s4h5](https://open.sap.com/courses/s4h5)|20170125|Find Your Path to SAP S/4HANA||
  ||[s4h6](https://open.sap.com/courses/s4h6)|20170607|How to Best Leverage SAP S/4HANA Cloud for Your Company||
  ||[s4h7](https://open.sap.com/courses/s4h7)|20171025|Extending SAP S/4HANA Cloud and SAP S/4HANA||
  ||[s4h8](https://open.sap.com/courses/s4h8)|20180124|Data Migration to SAP S/4HANA||
  ||[wtc1](https://open.sap.com/courses/wtc1)|20180313|Writing Testable Code for ABAP ☞ [Ref](https://community.sap.com/topics/abap-testing-analysis)||
  ||[s4h9](https://open.sap.com/courses/s4h9)|20181010|Two-Tier ERP with SAP S/4HANA Cloud||
  ||[s4h10](https://open.sap.com/courses/s4h10)|20180911|Integration with SAP S/4HANA Cloud||
  ||[s4h11-1](https://open.sap.com/courses/s4h11-1)|20190206|<font color='gold'><B>System Conversion</B></font> to SAP S/4HANA (Repeat)||
  ||[s4h12](https://open.sap.com/courses/s4h12)|20181107|Intelligent ERP with SAP S/4HANA Cloud||
  ||[s4h13](https://open.sap.com/courses/s4h13)|20181114|Create and Deliver Cloud-Native SAP S/4HANA Extensions||
  ||[s4h14-1](https://open.sap.com/courses/s4h14-1)|20201007|Key Technical Topics in a <font color='gold'><B>System Conversion</B></font> to SAP S/4HANA (Repeat)||
  ||[hanasql1](https://open.sap.com/courses/hanasql1)|20201110|A First Step Towards SAP HANA Query Optimization||
  ||[s4h15-1](https://open.sap.com/courses/s4h15-1)|20201111|Key Functional Topics in a <font color='gold'><B>System Conversion</B></font> to SAP S/4HANA (Repeat)||
  ||[s4h16](https://open.sap.com/courses/s4h16)|20200325|Migrating Your Business Data to SAP S/4HANA – New Implementation Scenario||
  ||[s4h17](https://open.sap.com/courses/s4h17)|20200311|Implementing SAP S/4HANA Cloud with the Central Business Configuration Capability||
  ||[s4h18](https://open.sap.com/courses/s4h18)|20200504|How to Deliver a Great User Experience with SAP S/4HANA ☞ 아래 Fiori 영역 참조||
  ||[s4h19](https://open.sap.com/courses/s4h19)|20200909|Guide Your SAP S/4HANA Project to Success|20210525 ①|
  ||[s4h19-1](https://open.sap.com/courses/s4h19-1)|<font color='green'>20210616</font>|Guide Your SAP S/4HANA Project to Success (Repeat)||
  ||[s4h20](https://open.sap.com/courses/s4h20)|20210323|Integration Advisor Capability of SAP Integration Suite||
  ||[s4h21](https://open.sap.com/courses/s4h21)|20201019|Delivering Value with Intelligent Innovations in SAP S/4HANA||
  ||[s4h22](https://open.sap.com/courses/s4h22)|20210420|Discover SAP S/4HANA Movement||
  ||[s4h23](https://open.sap.com/courses/s4h23)|<font color='green'>20210505</font>|Implementing SAP S/4HANA Cloud with SAP Central Business Configuration||
  |Fiori|[uxn1](https://open.sap.com/courses/uxn1)|20140827|SAP's UX Strategy in a Nutshell by Sam Yen|20210511 ①|
  ||[ui51](https://open.sap.com/courses/ui51)|20160524|Developing Web Apps with SAPUI5||
  ||[fiops1](https://open.sap.com/courses/fiops1)|20180214|Understanding SAP Fiori Launchpad||
  ||[3dmv1](https://open.sap.com/courses/3dmv1)|20180313|Maps and 3D Made Easy with SAPUI5||
  ||[ui52](https://open.sap.com/courses/ui52)|20190508|Evolved Web Apps with SAPUI5||
  ||[ieux1](https://open.sap.com/courses/ieux1)|20190626|Intelligent Enterprise User Experience with SAP Fiori 3||
  ||[s4h18](https://open.sap.com/courses/s4h18)<Br><Br>|20200504<Br>20200602|How to Deliver a Great User Experience with SAP S/4HANA<Br>☞ [BP Explorer](https://rapid.sap.com/bp/#/browse/packageversions/BP_OP_ENTPR), Fiori Apps [Ref. Library](https://fioriappslibrary.hana.ondemand.com/), S/4HANA [Tutorial](https://education.hana.ondemand.com/education/pub/s4/index.html), [Wiki](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=449910787)|진행 중<Br><Br>|
  ||[fiori3](https://open.sap.com/courses/fiori3)<Br><Br>|20200609<Br><Br>|SAP Fiori Overview: Design, Develop and Deploy<Br>☞ SCN [Blog](https://blogs.sap.com/2019/05/25/get-ready-for-sap-fiori-3/) `Get Ready for SAP Fiori 3`|20210604 ①|
  ||[cp13](https://open.sap.com/courses/cp13)  |20201019|Building Apps with the ABAP RESTful Application Programming Model||
  ||[fiori-ea1](https://open.sap.com/courses/fiori-ea1)|<font color='green'>20210608</font>|Developing and Extending SAP Fiori Elements Apps||
  |Personas|[sps1](https://open.sap.com/courses/sps1)|20150531|~~SAP Screen Personas~~ ☞ [sps2](https://open.sap.com/courses/sps2), [sps3](https://open.sap.com/courses/sps3) 과정으로 <font color='gold'>대체</font>됨||
  ||[sps2](https://open.sap.com/courses/sps2)|20170222|Introduction to SAP Screen Personas|20210610 ①|
  ||[sps3](https://open.sap.com/courses/sps3)|20170919|Using SAP Screen Personas for Advanced Scenarios||
  ||[sps4](https://open.sap.com/courses/sps4)|20180926|Building Mobile Applications with SAP Screen Personas||
  |데이터 과학|[ds0](https://open.sap.com/courses/ds0)|20191008|Introduction to Statistics for Data Science||
  ||[ds1](https://open.sap.com/courses/ds1)|20170201|Getting Started with Data Science||
  ||[ds3](https://open.sap.com/courses/ds3)|<font color='green'>20210615</font>|Getting Started with Data Science (Edition 2021)||
  ||[ds2](https://open.sap.com/courses/ds2)|20171108|Data Science in Action - Building a Predictive Churn Model||
  ||[ml1](https://open.sap.com/courses/ml1)|20161114|Enterprise Machine Learning in a Nutshell||
  ||[ml2](https://open.sap.com/courses/ml2)|20171023|Enterprise Deep Learning with TensorFlow||
  ||[leo1](https://open.sap.com/courses/leo1)|20180717|SAP Leonardo - Enabling the Intelligent Enterprise||
  ||[leo2](https://open.sap.com/courses/leo2)|20181009|SAP Leonardo IoT for the Intelligent Enterprise||
  ||[leo4](https://open.sap.com/courses/leo4)|20181017|SAP Leonardo – An Introduction to Blockchain||
  ||[leo5](https://open.sap.com/courses/leo5)|20180925|SAP Leonardo Machine Learning Foundation – An Introduction||
  ||[dleo1](https://open.sap.com/courses/dleo1)|20180108|SAP Leonardo Design-Led Engagements Demystified||
  ||[dleo2](https://open.sap.com/courses/dleo2)|20180410|SAP Leonardo Design-Led Engagements Basics||
  ||[di1](https://open.sap.com/courses/di1)|20200129|SAP Data Intelligence for Enterprise AI|20210514 ①|
  ||[s4h21](https://open.sap.com/courses/s4h21)|20201019|Delivering Value with Intelligent Innovations in SAP S/4HANA|| 
  |Biz. by Design|[byd0](https://open.sap.com/courses/byd0)|20190917|Getting Started with SAP Business ByDesign||
  |☞ 검색어 [1](https://open.sap.com/courses?q=business%20by%20design), [2](https://open.sap.com/courses?q=design%20thinking)|[byd1](https://open.sap.com/courses/byd1)|20150603|Application Development for SAP Business ByDesign||
  ||[byd1-c](https://open.sap.com/courses/byd1-c)|20190716|Prepare for Your SAP Business ByDesign Certification – Application Associate ☞ 응시 전 `byd3∼7` 추천||
  ||[byd2](https://open.sap.com/courses/byd2)|20160120|Reporting with SAP Business ByDesign||
  ||[byd3](https://open.sap.com/courses/byd3)|20170301|SAP Business ByDesign Financials||
  ||[byd4](https://open.sap.com/courses/byd4)|20171010|SAP Business ByDesign Supply Chain Management||
  ||[byd5](https://open.sap.com/courses/byd5)|20180508|SAP Business ByDesign Project-Based Services||
  ||[byd6](https://open.sap.com/courses/byd6)|20180917|SAP Business ByDesign Customer Relationship Management||
  ||[byd7](https://open.sap.com/courses/byd7)|20190603|Built-In Analytics in SAP Business ByDesign||
  ||[byd8](https://open.sap.com/courses/byd8)|20190904|SAP Cloud Applications Studio for SAP Business ByDesign|| <!-- </div></details> openSAP 과정 및 내역 -->

<Br>

## 3.3 Markdown, Tex, MathJax
* 마크다운 <details><summary>일반 사항</summary><div>
  + 자주 사용 : `공백 &nbsp; , 행 띄기 <Br> , 문단 > 또는 >> , <font color='gold'>폰트 색</font>`
  + html ☞ [텍스트 서식](https://blog.naver.com/lenj1/221854809536) ; [HTML 요소](https://heropy.blog/2019/05/26/html-elements/)
    - 주석 : `<!-- 주석 문구 -->`
    - 요약 : `<details><summary>제목</summary><div> 한 행 띄고 내용 </div></details>`
  + hyper link : ① 마크다운 `[연결 설명](URL)`, ② 별도 탭 `<a href="URL" target="_blank">연결 설명</a>`
  + Wiki 마크다운 [KO](https://ko.wikipedia.org/wiki/마크다운), [EN](https://en.wikipedia.org/wiki/Markdown) 및 [마크다운 문법](https://simhyejin.github.io/2016/06/30/Markdown-syntax/), [CheatSheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 참조
  + 사용 사례 [① wikidocs.net](https://wikidocs.net/1678), [② Blog](https://theorydb.github.io/envops/2019/05/22/envops-blog-how-to-use-md/); [Table 생성기](https://www.tablesgenerator.com/markdown_tables)
* 마크다운 수식 입력에 대한 참고 URL, [Local PC Daum Equation Editor](http://s1.daumcdn.net/editor/fp/service_nc/pencil/Pencil_chromestore.html)로 Chrome에서 입력함 <details><summary>참조 정보</summary><div>
  + MathJax에서 유용한 TEX 명령어 [KO](https://www.onemathematicalcat.org/MathJaxDocumentation/MathJaxKorean/TeXSyntax_ko.html), [EN](https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm), [위키백과:TeX_문법](https://ko.wikipedia.org/wiki/위키백과:TeX_문법)
  + 기타 : https://www.mathjax.org/ ; https://en.wikibooks.org/wiki/LaTeX/Mathematics
  + MathJax basic tutorial and quick reference [URL](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)
  + MathJax 연습 가능한 곳 [URL](http://jsbin.com/zimuxulawu/edit?html,output), MathJax 코드 제안 [URL](http://detexify.kirelabs.org/classify.html)
* TinyMind for Markdown <details><summary>사례</summary><div>
  ```tinymind 
  $Mindmap\\사용~예시$    <!-- HTML 주석 -->
    Hyperlink <!-- Indentation으로 부모-자식 구분 -->
      Naver [News](https://news.naver.com)
      G/W [Circle](http://snc.eagleoffice.co.kr/) 
    Jump to [향후 일정](#12-향후-일정) <!-- 일반 마크다운 가능. "<details open><summary>제목</summary><div>한 행 띄고 내용</div></details>" 사용 불가 -->
    MathJax $y=f(x)=x^2$ <!-- 우측으로만 분기 가능 좌측 불가 -->
  ```
* GraphViz : https://graphviz.org/ <details><summary>사례</summary><div>
  - [Guide to Flowcharts in Graphviz](https://sketchviz.com/flowcharts-in-graphviz) <Br>
    ```graphviz
    digraph G {
      node [fontname = "Handlee"];
      edge [fontname = "Handlee"];

      splines=false;
      
      draw [label = "Draw a picture";      shape = rect;   ];
      win  [label = "You win!";            shape = oval;   ];
      guess[label = "Did they\nguess it?"; shape = diamond;];
      point[label = "Point repeatedly\nto the same picture."; shape = rect; ];

      draw  -> guess;
      win   -> guess [ label = "Yes"; dir=back ];
      guess -> point [ label = "No" ];

      {
        rank=same;
        guess; point; win;
      }
      
      {
        rank=same;
        guess2; point2; 
      }
      
      guess2 [
          label = "                     ";
          color= white ;
      ];
      point2 [
          label = "                       ";
          color=white;
      ];
      
      point:s -> point2:n [ arrowhead = none ];
      guess2:n -> point2:n [ arrowhead = none ];
      guess2:n -> guess:s;
    } 
    ```
  - [polygons](https://graphviz.org/Gallery/directed/crazy.html) 
  - Graphviz Markdown Preview<Br>
    ```graphviz
    digraph finite_state_machine {
        rankdir=LR;
        size="8,5"

        node [shape = doublecircle]; S;
        node [shape = point ]; qi

        node [shape = circle];
        qi -> S;
        S  -> q1 [ label = "a" ];
        S  -> S  [ label = "a" ];
        q1 -> S  [ label = "a" ];
        q1 -> q2 [ label = "ddb" ];
        q2 -> q1 [ label = "b" ];
        q2 -> q2 [ label = "b" ];
    }
    ``` 
</div></details>

<!--
<details><summary>Template</summary><div>              -- Indentation이 없으면 <details><div> ~ </div></details> 앞뒤 전부 사용  --

* 제목1 <details open><summary>상세</summary><div>      -- Indentation이 있으면 앞에만 사용 해도 되며 한 칸 띌 필요도 없다.        --
  + 제목1-1 <details open><summary>상세</summary><div>  -- Template : <details><summary>제목</summary><div> 한 행 띄고 내용 </div></details> --
    - 내용1-1-1
    - 내용1-1-2
  + 제목1-2 <details open><summary>상세</summary><div>
    - 내용1-2-1
    - 내용1-2-2
* 제목2 <details><summary>상세</summary><div>
  + 제목2-1 <details><summary>상세</summary><div>
    - 내용2-1-1
    - 내용2-1-2
  + 제목2-2 <details><summary>상세</summary><div>
    - 내용2-2-1
    - 내용2-2-2
</div></details> 

https://rgy0409.tistory.com/4140
<details>
    <summary>메뉴1</summary>
    <details>
        <summary>소메뉴1</summary>
        <p>소메뉴 1에 대한 설명</p>
    </details>
    <details>
        <summary>소메뉴2</summary>
        <details>
            <summary>소소메뉴1</summary>
            <p>소소메뉴 1에 대한 설명</p>
        </details>
        <details>
            <summary>소소메뉴2</summary>
            <p>소소메뉴 2에 대한 설명</p>
        </details>
        <details>
            <summary>소소메뉴3</summary>
            <p>소소메뉴 3에 대한 설명</p>
        </details>
    </details>
</details>
-->
