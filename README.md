# savePBM
将图片文件转为PBM格式的文件

首先需要安装 pillow  

`pip install pillow`

## 使用方法 命令行

`python pbm.py a.png 128 64`  

生成128x64分辨率的PBM文件

`python pbm.py a.png`  

生成原始分辨率的PBM文件

## 使用方法 引入库

````
from pbm import savePBM
savePBM("a.png",128,64) #生成128x64分辨率的PBM文件
savePBM("a.png") #生成原始分辨率的PBM文件
````

