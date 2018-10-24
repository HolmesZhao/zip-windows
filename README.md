# zip-windows
解决 Windows 下压缩 zip 包给 Mac 使用时乱码问题的脚本

## 起因
开发过程中需要设计给予我设计图, 压缩包内很多中文路径导致乱码, Mac 和 Windows 系统之间互传 zip 文件, 打开之后会发现中文名称都是乱码。

Mac 下默认文字编码是 `utf-8`，而在 Windows 下是 `gbk`

## 解决
写一个 `Python` 脚本, 解决解压缩乱码问题

> 使用方法: 进入 `zip.windows.py` 目录, 使用 `python zip-windows.py /Users/Yesoul/Downloads/体脂秤.zip`

## 优化
脚本每次都要去我的 `iTerm2` 上跑很麻烦, 借助工具 `Alfred` 实现##复制路径##通过 `keyword` 方式来使用很快捷

```
query=$1  // 获取参数 也就是路径
path=$1   // 同上
array=(${path//// })  // 将路径通过 / 拆分成一个数组
unset array[${#array[@]}-1]  // 由于路径是要解压的文件路径, 需要拿到解压文件的目录
res=''  // 目录拼接用的结果
for var in ${array[@]}   // 遍历拼接
do
    res=$res'/'$var
done

query=`python zip-windows.py $query` // 执行 Python 脚本
echo -n $query  // 输出成功标志用于通知
open $res  // 打开要解压的文件目录
```
![image](https://user-images.githubusercontent.com/19728934/47402792-996ef300-d779-11e8-9481-41ee5a57b071.png)

![lzzip](https://user-images.githubusercontent.com/19728934/47403101-dc7d9600-d77a-11e8-9a25-37d33930424f.gif)
