#-*- coding:utf-8 -*-

boldFR = '\033[1m'; boldTO = '\033[0m'  # myLib에서는 descobj 밖으로...

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

## ------------------------------------------------------------------------------------------- ## Dictionary 초기화 함수 ↑, LifePathCompass ↓


## ------------------------------------------------------------------------------------------- ## LifePathCompass 초기화 함수 ↑, python 일반 ↓
my.pkgCheatSheet.str_python = """파이썬 코딩 도장 중심 정리 : https://dojang.io/course/view.php?id=7
▣ dct id : [0] ToC, [n] 이하는 주제별로 아래 정수 참조
   * 파이썬 코딩 도장 '핵심 정리' 모음
     1. 환경 구성 : https://dojang.io/mod/page/view.php?id=2470
     2. 자료형
       - byte, bytearray : https://dojang.io/mod/page/view.php?id=2462
     3. 숫자, 변수, 연산자 : https://dojang.io/mod/page/view.php?id=2189 
       - 연산자 우선 순위 : https://dojang.io/mod/page/view.php?id=2461 # help('%')
       - 실수 값의 오차 : https://dojang.io/mod/page/view.php?id=2466
     4. 불과 비교ㆍ논리 연산자 : https://dojang.io/mod/page/view.php?id=2218 
       - 비트 연산자 : https://dojang.io/mod/page/view.php?id=2460
     5. 문자열 : https://dojang.io/mod/page/view.php?id=2218 
       - 정규표현식 : https://dojang.io/mod/page/view.php?id=2454
       - 이스케이프 시퀀스 : https://dojang.io/mod/page/view.php?id=2465
     6. if 조건문 : https://dojang.io/mod/page/view.php?id=2239
     7. Loop : https://dojang.io/mod/page/view.php?id=2279
     8. 시퀀스 자료형, 리스트, 튜플, 딕셔너리 : https://dojang.io/mod/page/view.php?id=2218
     9. 리스트 및 문자열 메서드 : https://dojang.io/mod/page/view.php?id=2305
     10. 딕셔너리 및 세트 메서드 : https://dojang.io/mod/page/view.php?id=2323
     11. 파일 : https://dojang.io/mod/page/view.php?id=2335
     12. 함수 : https://dojang.io/mod/page/view.php?id=2357
     13. 람다 : https://dojang.io/mod/page/view.php?id=2370
     14. 클로저 : https://dojang.io/mod/page/view.php?id=2370
     15. 클래스 : https://dojang.io/mod/page/view.php?id=2396
       - 프로퍼티 사용하기 : https://dojang.io/mod/page/view.php?id=2476
       - 메타 클래스 사용하기 : https://dojang.io/mod/page/view.php?id=2468
       - "with as"에 사용 가능한 클래스 만들기 : https://dojang.io/mod/page/view.php?id=2467
     16. 예외 : https://dojang.io/mod/page/view.php?id=2425
     17. 이터레이터 : https://dojang.io/mod/page/view.php?id=2425
     18. 제너레이터 : https://dojang.io/mod/page/view.php?id=2425
     19. 코루틴 : https://dojang.io/mod/page/view.php?id=2425
       - asyncio : https://dojang.io/mod/page/view.php?id=2469
     20. 데코레이터 : https://dojang.io/mod/page/view.php?id=2454
     21. 정규표현식 : https://dojang.io/mod/page/view.php?id=2454
     22. 모듈, 패키지 : https://dojang.io/mod/page/view.php?id=2454
       - 내장 함수 : https://dojang.io/mod/page/view.php?id=2464

▣ CH01. 환경 구성 ☞ 참조 : 코딩 도장 https://dojang.io/mod/page/view.php?id=2470  
  1.1 자주 사용하는 conda 명령어
    - conda create --name MyEnv         # 가상환경 "MyEnv" 생성, 필요 시 "python=3.5 numpy=1.1"과 같이 패키지와 버전 지정 가능
    - conda env list                    # conda 가상환경 확인
    - conda info                        # 현재 환경 정보 출력
    - conda activate 접속할_가상환경이름
    - conda deactivate                  # 현재 conda 환경에서 이탈
    - conda list | find /N /I "scikit"  # 윈도우에서 설치된 Module 확인
    - conda search package_name         # 패키지 검색
    - conda install package_name=ver    # 패키지 설치
    - conda update conda                # 패키지 conda 갱신
    - conda update package_name         # 패키지 업데이트
    - conda list --export > pkg_lst.txt # 패키지 목록 및 버전 정보 저장
    - conda install --file  pkg_lst.txt # 패키지 목록으로 설치
    - conda env export --name MyEnv > MyEnv.yml
    - conda env create -f MyEnv.yml     # MyEnv.yml에 저장된 정보로 환경 생성, 필요 시 사전에 yml file 내의 "환경 이름" 변경.
    - conda remove package_name
    - conda remove --name MyEnv --all   # 환경 "MyEnv" 전체 삭제
    
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

  1.3 (google colab에서 "!명령어" 방식으로 주로 사용하기 위한) linux 명령어
    (1) 일반 명령어
       - 폴더 포함 삭제 : rm -R path_n_folder_name
    (2) 압축 및 해제 : https://bosungs2y.tistory.com/418
      a. (설치 안되어 있다면) zip 설치
         CMD> yum -y install zip*
      b. zip으로 파일 압축 및 암호화 : file이 "zippedFile.zip"이고 암호가 "test1234"인 경우
         CMD> zip -P "password" zippedFile.zip file1 file2 file3
         CMD> zip -P "password" -r zippedFile.zip path_n_folder_name/*
      c. 압축 해제 : file 및 암호는 위 2와 같음.
         CMD> unzip -P test1234 zippedFile.zip

▣ CH02. 자료형 ☞ 참조 : 코딩 도장 https://dojang.io/mod/page/view.php?id=2189  
  - my.printcmd(my.pkgCheatSheet.mdStr_python_sequence)  
  
▣ CH03. 숫자, 변수, 연산자 : https://dojang.io/mod/page/view.php?id=2189 
  - 연산자 우선 순위 : https://dojang.io/mod/page/view.php?id=2461 # help('%')
  - 실수 값의 오차 : https://dojang.io/mod/page/view.php?id=2466
  
▣ CH04. 불과 비교ㆍ논리 연산자 : https://dojang.io/mod/page/view.php?id=2218 
  - 비트 연산자 : https://dojang.io/mod/page/view.php?id=2460

▣ CH05. 문자열 : https://dojang.io/mod/page/view.php?id=2218 
  - 정규표현식 : https://dojang.io/mod/page/view.php?id=2454
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

|if - else|for|while|[try](https://dojang.io/mod/page/view.php?id=2398)|
|:----|:----|:----|:----|
|**if** condition:<Br>&nbsp; &nbsp; expression<Br>**elif** condition:<Br>&nbsp; &nbsp; expression<Br>**else**:<Br>&nbsp; &nbsp; expression<Br><Br>|**for** item **in** *collection*:<Br>&nbsp; &nbsp; expression<Br>**else:** `#` 항상 실행<Br>&nbsp; &nbsp; expression<Br><Br><Br><Br>|**while** condition:<Br>&nbsp; &nbsp; expression<Br>**else:** `#` 항상 실행<Br>&nbsp; &nbsp; expression<Br><Br><Br><Br>|**try:**<Br>&nbsp; &nbsp; expression<Br>**except:** `#` 예외 有, 이름 특정 가능<Br>&nbsp; &nbsp; expression<Br>**else:** `#` 예외 無<Br>&nbsp; &nbsp; expression<Br>**finally:** `#` 항상 실행<Br>&nbsp; &nbsp; expression|
"""  # my.pkgCheatSheet.str_python_control

# my.pkgCheatSheet.dct_python 초기화
my.pkgCheatSheet.dct_python = dict()
_ = initCheatSheetDict('python')

## ------------------------------------------------------------------------------------------- ## python 일반 ↑, python > numpy ↓

## ------------------------------------------------------------------------------------------- ## python > numpy ↑, python > pandas ↓

## ------------------------------------------------------------------------------------------- ## python > pandas ↑, python > sqlite ↓

## ------------------------------------------------------------------------------------------- ## python > sqlite ↑, python > matplotlib ↓

## ------------------------------------------------------------------------------------------- ## python > matplotlib ↑, python > scikit-learn ↓
my.pkgCheatSheet.str_sklearn = """scikit-learn Cheat Sheet @ https://www.datacamp.com/community/data-science-cheatsheets?tag=python
▣ dct id : [0] ToC, [1] Data, [2] Model, [3] Training, [4] Prediction, [5] Evaluation, [6] Tuning, [7] Example
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

▣ CH07. A Basic Example ☞ Help : import mglearn  # https://github.com/amueller/mglearn 
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
