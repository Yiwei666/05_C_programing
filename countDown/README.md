### date.c

这段代码的功能是根据用户输入的未来时间点（格式为：天-小时-分钟），实时计算并显示当前时间与未来时间点之间的剩余时间。程序首先获取用户输入的未来时间点，然后计算当前时间与未来时间点之间的时间差，并将时间差转换为小时、分钟和秒的格式。最后，程序每隔5秒更新并显示剩余时间。

### 01_time.py
上述倒计时代码的python语言实现。

### TimeDifference.java
上述倒计时代码的java语言实现。
注意：对于普通的类文件，文件名必须与其中的公共类名一致。这是Java编译器的要求，以确保在编译和运行过程中能够正确找到和加载类。
编译和运行命令
```
javac TimeDifference.java
java TimeDifference
```

若想要在其他文件夹下运行D:\software\10_sft\01_time-CountDown\路径下的TimeDifference.class，可以按照以下步骤进行：  

打开命令行终端，进入你希望运行程序的目标文件夹。  
在命令行中使用以下命令运行程序：  
```
java -cp D:\software\10_sft\01_time-CountDown TimeDifference
```
在上述命令中，-cp 参数用于指定类路径（class path），后面紧跟着 D:\software\10_sft\01_time-CountDown，这是包含 TimeDifference.class 文件的路径。然后，在类名后面添加了 TimeDifference，指定要运行的类名。  

这样，Java虚拟机将在指定的类路径下查找并加载 TimeDifference.class 文件，并运行其 main 方法。  
