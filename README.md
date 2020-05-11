## 关键字标识
1. 小标题标识,如:<font color='red' size=4>定理:</font>,<font color='red' size=4>定义:</font> ,<font color='red' size=4>证明:</font> $ ...... $
2. 算法伪代码标识,如:**for**  $ i=1,2,\dots, n $ **do**


## 符号说明
$ x $: 标量      
$ \mathbf{x}$:  向量  
$ X $: 矩阵/随机变量/数据集   
$ \mathcal{X} $: 样本空间或状态空间,也可以用来表示概率分布,如$\mathcal{D}$     
$ \mathbb{I}(*) $:  指示函数,在$*$为真/假时分别取值为1/0   
$ \mathrm{sign}(*) $:  符号函数,在$*$<,=0,>0时分别取值为-1,0,1  
$ E_{* \sim \mathcal{D}} [f(*)] $:函数$f(*)$对$*$在分布$\mathcal{D}$下的数学期望;明确意义时将省略$\mathcal{D}$和(或)$*$


## 知识点重要度标识
1. 非常重要:★★★★★
2. 很重要:★★★★
3. 重要:★★★
4. 相对重要:★★


## 模块使用惯例
1. numpy模块
    * 函数功能以np.\*为模板(统一,推荐)
    * 除\*.flatten,\*.ravel(必须);\*.reshape外
2. pandas模块
    * 函数功能以$*.*$为模板,如df.rename,df.fillna
    * 除定义功能函数外,如:
        * pd.DataFrame
        * pd.Series
        * pd.date_range
        * pd.read_excel
        * ......
  
  
## jupyter notebook目录功能配置
1. pip install jupyter_contrib_nbextensions   
2. pip install jupyter_nbextensions_configurator    
3. jupyter contrib nbextension install --user    
  
  
## 额外安装的包
1. xgboost: pip install xgboost
2. PyTorch: https://pytorch.org/ 查看
3. graphviz: pip install graphviz