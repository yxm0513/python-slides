title: Python from scratch
speaker: yangxinming
transition: cards
prismTheme: dark
css:
    - css/base.css
js:
    - js/zoom.js
    - js/base.js
    - https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css 
plugins:
    - echarts
    - mermaid
    - katex


<slide class="bg-black-blue aligncenter zoomIn">

# Python From Scratch {.text-shadow}

By ![](https://avatars3.githubusercontent.com/u/73510?s=60&u=200063d372fefbd51de767b8e258de0024d45e52&v=4){.avatar-40} YangXinMing \[SCG-NP-IDEA\] {.text-intro} 

<slide class="aligncenter fullscreen">
## Agenda {.zoomIn}
<br>
:::div {.mydiv}
 * basics {.bounceInRight}
 * data types {.bounceInRight}
 * functions {.bounceInRight}
 * classes {.bounceInRight}
 * module & package & namespace {.bounceInRight}
 * q&a {.bounceInRight}
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### basics - general {.zoomIn}
<br>
:::div {.mydiv}
* 强类型 {.animated.zoomIn}
* 动态语言 {.animated.zoomIn}
* 解释型(bytecode -> vm) {.animated.zoomIn}
{.build.description.text-intro}
:::
<img src="/img/java.png" class="aligncenter fadeInUp size-20" onclick="myfunction(this)">

<slide class="aligncenter fullscreen">
### basics - bytecode {.zoomIn}
<br>
:::div {.mydiv}
* Bytecode is nothing more than an instruction set for a VM
* The source is compiled the first time it is encountered  ==> pyc pyo {.animated.zoomIn}
* The interpreter reads the binary file and executes the instructions (opcodes) one at a time {.animated.zoomIn}
{.build.description.text-intro}
:::
<img src="/img/dis.png" class="aligncenter fadeInUp size-90" onclick="myfunction(this)">

<slide class="aligncenter fullscreen">
### basics - get helps {.zoomIn}
:::div {.mydiv}
* pydoc -k <keyword> -p <port> {.animated.zoomIn}  
* help(module or function name obj) {.animated.zoomIn}
* print(obj.\_\_doc\_\_) {.animated.zoomIn}
* google, stackoverflow {.animated.zoomIn}
* source code {.animated.zoomIn}
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### basics - installations & run {.zoomIn}

:::column {.mycolumn}
##### installations{.content-left.tobuild}
  * python/venv {.animated.zoomIn.tobuild}
  * libraries {.animated.zoomIn.tobuild}
{.description.tobuild}
----

##### run {.content-left.tobuild}
  * interupter {.animated.zoomIn.tobuild}
  * python xxx.py {.animated.zoomIn.tobuild}


<slide class="aligncenter fullscreen">
### basics - editing & debugging {.zoomIn}
* vim, vistual code, pycharm
* pdb
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### data types {.zoomIn}
<br>
:::div {.mydiv}
 * bool、int、long、float 和 complex 
 * 字符串、元组、列表、集合，字典{.animated.zoomIn}
 * 定义，方法，转换, inspect {.animated.zoomIn}
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### conditionals and loops {.zoomIn}
<br>
:::div {.mydiv}
 * if x\:  or if not x\:
 * for x in \: {.animated.zoomIn}
 * while xxx \: {.animated.zoomIn}
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### functions {.zoomIn}

### def xxx_name()\:
 * 默认参数
 * \* 表示tuple参数 \*\* 表示dict, 参数都是a 或者 a=val的形式
 * \*args表示任何多个无名参数，它是一个tuple；\*\*kwargs表示关键字参数，它是一个dict。并且同时使用\*args和\*\*kwargs时，必须\*args参数列要在\*\*kwargs前
 * 函数定义时：\*p 不管什么参数传进来，就转换成tuple\*\*p是转换成dict
 * 如果同时出现，看调用的时候的格式=来标识dict开始

![](/imge/dearch.png)

![](/img/dearch2.png)



<slide class="aligncenter fullscreen">
### functions as objects {.zoomIn}

:::div {.mydiv}
* have types {.bounceInRight}
* can be sent as arguments to another function{.bounceInRight}
* can be used in expression{.bounceInRight}
* can become part of various data structures like dictionaries{.bounceInRight}
:::
![](/img/func.png)


<slide class="aligncenter fullscreen">
### functions {.zoomIn}
<br>

:::div {.mydiv}
 * a code object, containing the bytecode for a particular object {.bounceInRight}
 * a globals dictionary, containing the global variables necessary {.bounceInRight}
 * 一个函数是一个被它自己定义而执行的对象;默认参数是一种"成员数据",所以它们的状态和其他对象一样,会随着每一次调用而改变. {.bounceInRight}
{.build.description.text-intro}
:::


<slide class="aligncenter fullscreen">
### 装饰器

:::div {.mydiv}
 * @ is syntactic sugar for closing over a function {.bounceInRight}
 * 装饰器要实现的效果就是给不同的函数插入相同的功能 {.bounceInRight}
 * 制造函数的函数 {.bounceInRight}
:::
![](/img/decorator.png)
func = decorator(args)(func) 


<slide class="aligncenter fullscreen">
### class 

:::div {.mydiv}
* namepace : Class -- define a boxed set of data and functions {.bounceInRight}
* Classes provide a means of bundling data and functionality together.{.bounceInRight}
* Creating a new class creates a new type of object, allowing new instances of that type to be made.{.bounceInRight}
* Classes are just basically custom types.{.bounceInRight}
:::
<slide class="aligncenter fullscreen">
### class 

:::div {.mydiv}
* c = classname() \: --> 实例化， 
  * \_\_init\__(self, *args)  \: 初始化方法
  * \_\_new\_\_(cls, *args, \*\*kwargs) \: 构造函数
  * \_\_new\_\_方法用于创建对象并返回对象，当返回对象时会自动调用\_\_init\_\_方法进行初始化。\_\_new\_\_方法是静态方法，而\_\_init\_\_是实例方法
  * \_\_new\_\_() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.
* python的类没有访问权限的问题，也就是说所有的变量都是可访问的,私有的机制，就是在属性前加__，但是这种私有机制实际上也是伪私有，因为它其实是用一个别名来保存这个属性
* 允许多重继承，类似C++,不同于java
* 多态Polymorphism \: 通过参数的不同来区分不同的func
:::


<slide class="aligncenter fullscreen">
### class \: object {.zoomIn}

:::div {.mydiv}
* .func() {.bounceInRight}
* type(object){.bounceInRight}
* isinstance(object, class){.bounceInRight}
* callable(object){.bounceInRight}
* getattr(object, name[, default]){.bounceInRight}
* hasattr(object, name){.bounceInRight}
* setattr(object, name, value){.bounceInRight}
* is / is not{.bounceInRight}
:::

<slide class="aligncenter fullscreen">
### class \: 继承 {.zoomIn}

:::div {.mydiv}
* class classname (parent,):  --> MRO序列 {.bounceInRight}
* issubclass(A, B) {.bounceInRight}
* 继承关系本质上是设置 sub.\_\_bases\_\_ = (super, ) {.bounceInRight}
* 子类中需要调用父类的函数\：super(P, self).func(arg) {.bounceInRight}
* sub会继承所有super的变量和函数，需要overwrite的时候，使用相同名称在sub里定义一遍就行了。 {.bounceInRight}
:::

<slide class="aligncenter fullscreen">
###  class \: \_\_dict\_\_ & \_\_slot\_\_ {.zoomIn}
#### \_\_dict\_\_ 
:::div {.mydiv}
* 用来存属性
* class的存在 ClassName.__dict__里   -> Class 也是type的一个instance
* object 的存在 object.__dict__里
* 查找是先查object的，再查class的，查不到AttributeError
* 修改属性的时候，mutable的list,dict需要特别小心，因为从instance修改，class的也就被修改了，和inmutable的不一样，因为是reference. (avoid class variables unless you have a reason to use them)
__dict__是dir()的子集，dir()包含__dict__中的属性。
* object 的属性存在.__dict__
* object对应的class的属性存在于obj.__class__.__dict__
每一个方法都有一个方法__get__用来绑定
* func.__get__(t,Test)  
    * 第一个参数是object
    * 第二个参数是Class
:::

![](/img/dict.png)

![](/img/dict2.png)


#### \_\_slot\_\_
:::div {.mydiv}
* __dict__ 来存属性，当属性和实例特别多的时候，特别浪费内存， {.bounceInRight} 
* Python 是一门动态语言，可以在运行过程中，修改对象的属性和增删方法。任何类的实例对象包含一个字典__dict__, Python通过这个字典将任意属性绑定到对象上。有时候我们只想使用固定的对象，而不想任意绑定对象，这时候我们可以定义一个属性名称集合，只有在这个集合里的名称才可以绑定。__slots__就是完成这个功能的。 {.bounceInRight} 
:::


<slide class="aligncenter fullscreen">
###  class \: 属性 

类属性
```python
class ClassName:
attr = “test”;
```
实例属性
```
class ClassName:
def __init__(self, name):
    self.name = name
```
<slide class="aligncenter fullscreen">
###  class \: 特殊属性 
    * C.__name__ 类C的字符串名字
    * C.__doc__ 类C的文档字符串
    * C.__bases__ 类C的父类的列表
    * C.__dict__ 类C的属性
    * C.__module__ 对类C进行定义的模块
    * 实例有些属性提供给对象模型使用的
        * __dict__ : 实例名字空间的字典变量
        * __class__ : 生成该实例的类
        * __methods__ : 实例所有方法的列表
<slide class="aligncenter fullscreen">
###  class : \@property {.zoomIn}
* \@property 可以将python定义的函数“当做”属性访问，从而提供更加友好访问方式，但是有时候setter/getter也是需要的 
```python
class C(object):
  def __init__(self):
      self._x = None
  def getx(self):
      return self._x
  def setx(self, value):
      self._x = value
  def delx(self):
      del self._x

x = property(getx, setx, delx, "I'm the 'x' property.")
```

<slide class="aligncenter fullscreen">
###  class : method {.zoomIn}
:::div {.mydiv}
* 和一般的方法没有差别，创建了一个方法的实例，使用class的namespace. 
* 实例方法 :def function_name(self, ): ⇒ Class().function_name()
  * 初始化方法 def __init__(self, name):
  * 析构函数 def __del__(self):
* 类方法 :  
  * @classmethod 
  * def function_name(cls, ):  ⇒ Class.function_name()
  * 一个类方法就可以通过类或它的实例来调用的方法, 不管你是用类来调用这个方法还是类实例调用这个方法,该方法的第一个参数总是定义该方法的类。
* 静态方法 ： 
  * @staticmethod
  * def function_name():    ⇒ Class.function_name()  --> 可直接用class后跟的这个名字，也可是传入的cls
  * 好处是，不需要定义实例即可使用这个方法。另外，多个实例共享此静态方法。  -->相当于package带的一个方法
:::

<slide class="aligncenter fullscreen">
### Module & Package {.zoomIn}
  * .py 单文件表示模块，目录下__init__.py表示package
  * import packge 会先import \_\_init\_\_.py, 如果使用import package相当于import了package下的\_\_init\_\_.py。
  * \_\_all\_\_ import * 对应package 下 __init__.py 中 __all__释出的函数，

<slide class="aligncenter fullscreen">
### import {.zoomIn}
    * 只要import一个文件，这个文件就从头到尾执行一遍
    * import folder 只是导入package，相当于执行__init__.py文件
    * from folder import abcd则执行了__init__.py文件文件与abcd.py文件
    * from folder1.abcd import b其实也执行了__init__.py文件文件与abcd.py文件
    * import path.file.func 使用时需要全路径
    * from path import file 使用file.func
    * from fir.file import func 直接使用funtion
	* The __import__() function can be used to import modules where the name is only known at runtime
        * os = __import__("os")
        * mod = __import__(r"C:/path/to/file/anywhere/on/computer/module.py")
	* dir() is used to find out which names a module defines

<slide class="aligncenter fullscreen">
### \_\_main\_\_ module 
* for i in sys.modules: print(i)   --> \_\_main\_\_
* dir(\_\_main\_\_)
* if __name__ == '\_\_main\_\_': 判断是本脚步运行，而非做为模块被使用搜索路径sys.path



```python
>>> print(__name__)
__main__
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> import sys
>>> sys.modules

>>> import __main__
>>> dir(__main__)
['__annotations__', '__builtins__', '__doc__', '__loader__', '__main__', '__name__', '__package__', '__spec__', 'i', 'os', 'sys']
>>> print(__main__.__spec__)
None
>>> print(__main__.i)
rlcompleter
>>> print(__main__.os)
<module 'os' from '/usr/local/bin/../../../Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py'>
>>> print(__main__.sys)
<module 'sys' (built-in)>
>>> import re
>>> dir(__main__)
['__annotations__', '__builtins__', '__doc__', '__loader__', '__main__', '__name__', '__package__', '__spec__', 'i', 'os', 're', 'sys']

>>> def a():
...     pass
...
>>> dir(__main__)
['__annotations__', '__builtins__', '__doc__', '__loader__', '__main__', '__name__', '__package__', '__spec__', 'a', 'i', 'os', 're', 'sys']
>>> def b():
...     print("haha")
...
>>> __main__.b()
haha
>>> import re as c
>>> dir(__main__)
['__annotations__', '__builtins__', '__doc__', '__loader__', '__main__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'i', 'os', 're', 'sys']
>>> dir(c)
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'Pattern', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pickle', '_special_chars_map', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
>>> c == re
True
```


```python
~ cat d.py
import re

def f():
    pass
```

```
>>> import d
>>> d.f
<function f at 0x7f966fb3a730>
>>> dir(d)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'f', 're']
>>> for i in sys.
KeyboardInterrupt
>>> import sys
>>> sys.path
['', '/Library/Python/3.7/site-packages', '/usr/local/lib/python3.7/site-packages', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages', '/Users/yangxinming', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/yangxinming/Library/Python/3.7/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/psycopg2-2.8.3-py3.7-macosx-10.9-x86_64.egg']
>>> for i in sys.path:
...     print(i)
...

/Library/Python/3.7/site-packages
/usr/local/lib/python3.7/site-packages
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
/Users/yangxinming
/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload
/Users/yangxinming/Library/Python/3.7/lib/python/site-packages
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/psycopg2-2.8.3-py3.7-macosx-10.9-x86_64.egg
```

```
import re

test = True

def f():
    pass


class A():
    def __init__(self):
        pass

    def name(self):
        pass
```



```
>>> import d
>>> dir(d)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'f', 're']
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> reload(d)   ==> python2.x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reload' is not defined
>>> import importlib
>>> importlib.reload(d)
<module 'd' from '/Users/yangxinming/d.py'>
>>> dir(d)
['A', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'f', 're', 'test']
```


<slide class="aligncenter fullscreen">
### namespace {.zoomIn}
LEGB\: LOCAL>ENCLOSING>global>built in

    * locals:函数内部的名字空间，一般包括函数的局部变量以及形式参数
    * enclosing function:在嵌套函数中外部函数的名字空间, 对fun2来说， fun1的名字空间就是.
    * globals:当前的模块空间，模块就是一些py文件。也就是说，globals()类似全局变量。
    * __builtins__: 内置模块空间，也就是内置变量或者内置函数的名字空间。
    * locals是只读的(不能改变)，globals不是（可以改变）
    * locals()没有返回局部命名空间，它返回的是一个拷贝。所以对它进行改变，对局部命名空间中的变量值没有影响
    * globals()返回全部实际命名空间，而非拷贝。所以globals返回的dict任何改动都会影响到全局变量

<slide class="aligncenter fullscreen">
### Python的命名空间 {.zoomIn}
    * Python 一切皆对象，每个对象都具有 一个ID、一个类型、一个值；对象一旦建立，ID 便不会改变，可以直观的认为 ID 就是对象在内存中的地址
    * 标识符:  各类对象的名称，比如函数名、方法名、类名，变量名、常量名等。 identifier（注意不要与 ID 混淆了），中文名为“标识符”
        * 在 Python 中赋值并不会直接复制数据，而只是将名称绑定到对象
    * 命名空间：（英语：Namespace）表示标识符（identifier）的可见范围。 简而言之，命名空间可以被简单的理解为：存放和使用对象名字的抽象空间。
    * 与命名空间相对的一个概念就是“作用域”，那么什么又是作用域呢？作用域：（英文 Scope）是可以直接访问到命名空间的文本区域。


<slide class="aligncenter fullscreen">
### errors and exceptions {.zoomIn}
```python
try:
  <statements>
expect <异常>:
<>
else:
<>

finally:
<>
raise
```

<slide class="aligncenter fullscreen">
### errors and exceptions {.zoomIn}

    * 所有异常 expect Expection, e: or expect:
    * 抛出异常使用
        * raise
        * raise Exception("message")    对象
    * 异常层次体系：
        * Exception
            * SystemExit
            * StandardError
                * KeyboardInterrupt
                * ImportError
                * EnvirobmentError
                * IOError
                * OSError
                * EOFError
            * RuntimeError
                * NotImplementedError
            * NameError
                * UnboundLocalError
            * AttributeError
            * SyntaxError
            * TypeError
            * AssertionError
            * LookupError
                * IndexError
                * KeyError
            * ArithmeticError
                * OverflowError
                * ZeroDivisionError
                * FloatingPointError
            * ValueError
            * SystemError
            * MemoryError


<slide class="aligncenter fullscreen">
### builtins {.zoomIn}
* 查看所有keywords
```python
import keyword
print(keyword.kwlist)
```
* 查看builtins
```python
dir(__builtins__)
```

<slide class="aligncenter fullscreen">
### eval, exec, compile {.zoomIn}
<br>
:::div {.mydiv}
 * eval -> expression, expr{.animated.zoomIn}
 * exec -> python code string {.animated.zoomIn}
 * compile -> python file {.animated.zoomIn}
{.build.description.text-intro}
:::


<slide class="aligncenter fullscreen">
### re {.zoomIn}
```python
import re
patterns = ''
r = re.compile(patterns)
r.match("string")
* 正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。正则表达式被编译成 `RegexObject` 实例，可以为不同的操作提供方法。
match和search
* match从开头匹配字符串，第一个不匹配就返回none,相当于re.search('^want',string)
#!python
>>> import re
>>> p = re.compile('ab*')
>>> print p
<re.RegexObject instance at 80b4150>
* re.compile() 也接受可选的标志参数，常用来实现不同的特殊功能和语法变更。
#!python
>>> p = re.compile('ab*', re.IGNORECASE)
* DOTALL, S 使.匹配包括换行在内的所有字符
    * IGNORECASE, I 使匹配对大小写不敏感
    * LOCALE, L 做本地化识别（locale-aware）匹配
    * MULTILINE, M 多行匹配，影响 ^ 和 $
    * VERBOSE, X 能够使用 REs 的 verbose 状态，使之被组织得更清晰易懂
    * p.match("")
    * P.search("")
        * 和match的区别，match只搜索第一个，search搜索所有的。
        * match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default).
    * p.findall()
    * p.split() 分割
    * p.sub, subn 替换
返回的是re.MatchObject,常用方法有group,groups,span
* group (?P<组名>Patterns):
    * 和perl 一样partens中()表示组，p.group(n) 来取出相应的组，
    * (?P<组名>Patterns) 来命名组,命名组可以用p.group(“组名”)取得。
    * p.groupdict获取所有组。
    * start([group]), end([group]) 分别返回第一个和最后一个。
* 注意group(0)是所有匹配的字符串，group(1)才是第一个匹配的group
escape(string)
* Escapes all special regexp characters in string
span([group])
* Returns both the beginning and ending positions of a group
patterns
* \d 匹配任何十进制数；它相当于类 [0-9]。
    * \D 匹配任何非数字字符；它相当于类 [^0-9]。
    * \s 匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
    * \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
    * \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
    * \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]。
fnmatch
* fnmatch.fnmatch(name, pattern)方法：测试name是否匹配pattern，返回true/false, fnmatch.fnmatch('tlie.py','*.py')fnmatch.filter(names, pat)实现列表特殊字符的过滤或筛选,返回符合匹配模式的字符列表,当然names表示的是列表;
    * fnmatch.fnmatchcase(name, pat) 类似
* *表示匹配任何单个或多个字符.?表示匹配单个字符;[seq] 匹配单个seq中的字符;[!seq]匹配单个不是seq中的字符.
```


<slide class="aligncenter fullscreen">
### system commands {.zoomIn}
```
* os.system() 返回命令的返回值，如果在shell里执行，显示出执行的output
* os.popen()不但执行命令还返回执行后的文件对象， os.popen('ls *.py').readlines()os.spawn*
    * stdout = os.popen(cmd)
    * msg = stdout.read()
* popen2.*
* commands.*
* subprocess ：
    * p = subprocess.Popen(args) (args ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"])
        * Popen可以指定参数如stderr=subprocess.PIPE,这样可以通过p.stderr.read()拿到output
    * subprocess.call('command')
* execfile() 执行磁盘上的文件
```

<slide class="aligncenter fullscreen">
### 输出输出 {.zoomIn}
* raw_input()/input : string / number
* print / write(sys.stdout)sys.stderr.write()
    * “%s”% str
    * %r raw data,调试比较有用处，区别%d,%s,'\n'类的转义，%r不会转义
* print >> sys.stderr, msg

<slide class="aligncenter fullscreen">
### 输出输出 {.zoomIn}
* sys.stdin - Standard input
* sys.stdout - Standard output
* sys.stderr - Standard error
```python
import sys
for line in sys.stdin:
    process(line)
```

<slide class="aligncenter fullscreen">
### 文件操作 {.zoomIn}
    * files = glob.glob('*.py')
    * f= open(name[, mode[, buffering]])
        * 'r' Read mode
        * 'w' Write mode
        * 'a' Append mode
        * 'b' Binary mode (added to other mode)
        * '+' Read/write mode (added to other mode)
    * f.read()
        * f.readline()
        * f.readlines()
    * f.write()f.close()
        * f.writeline()
        * f.writelines()

    * f.closed()open().write(msg)
        * for eachline in f:
        * for eachline in f.readline():

<slide class="aligncenter fullscreen">
### 目录操作 {.zoomIn}
    * for (dirpath, dirnames, filenames) in os.walk(basedir):
    * os.path.join(,)
    * os.path.abspath()
    * os.listdir

<slide class="aligncenter fullscreen">
### Process {.zoomIn}
    * Process Creation and DestructionCanonical Example
        * fork-exec-wait
            * os.fork() # Create a child process.
            * os.execv(path,args) # Execute a process
            * os.execve(path, args, env)
            * os.execvp(path, args) # Execute process, use default path
            * os.execvpe(path,args, env)
            * os.wait([pid)] # Wait for child process
            * os.waitpid(pid,options) # Wait for change in state of child
            * os.system(command) # Execute a system command
            * os._exit(n) # Exit immediately with status n.
    import os
    pid = os.fork()      # Create child
    if pid == 0:
        # Child process
        os.execvp("ls", ["ls","-l"])
    else:
        os.wait()        # Wait for child


<slide class="aligncenter fullscreen">
### Thread {.zoomIn}
    * start_new_thread(func, args, [kwargs])

<slide class="aligncenter fullscreen">
### 其他常用 {.zoomIn}
    * sys 系统相关（解释器，):
        * sys.argv 参数列表
        * sys.exit 终止程序
        * sys.stdin/stdout/stderr 三个文件描述符
        * sys.modules 所加载的模块
            * 模块也是对象。只要导入了，总可以用全局 dictionary sys.modules 来得到一个模块的引用
        * sys.platforms os类型
        * sys.path 查找lib的路径
        * sys.builtin_module_names 内建的模块名称
        * sys.exc_info 当前处理异常的信息
        * sys.exc_type, sys.exc_value, sys.exc_traceback 获取当前异常信息的另种方法 (上一次，sys.last_type, sys.last_value, sys.last_traceback)
        * sys.version_info
<slide class="aligncenter fullscreen">
### 其他常用 {.zoomIn}
    * os 操作系统:
        * os.environ
        * os.chdir(path)
        * os.fchdir(fd)
        * os.getcwd()
        * os.path
        * os.abspath(path)
        * os.basename(path)
        * os.commonprefix(list)
        * os.dirname(path)
        * os.exists(path)
        * os.environ
        * os.name
        * os.getcwd
        * os.curdir
        * os.listdir
        * os.rename
        * os.chmod
        * os.system(cmd)
        * os.remove
        * os.mkdir
        * os.rmdir
        * os.removedirs
        * os.path.exists()
        * os.path.isfile()
        * os.path.isdir()
        * os.path.split()

<slide class="aligncenter fullscreen">
### 其他常用 {.zoomIn}
    * time
        * 一般有两种表示时间的方式:
            * 第一种是时间戳的方式(相对于1970.1.1 00:00:00以秒计算的偏移量),时间戳是惟一的
            * 第二种以数组的形式表示即(struct_time),共有九个元素，分别表示，同一个时间戳的struct_time会因为时区不同而不同
        * time
            * time.time() # 返回秒数
            * time.ctime(seconds) -> string 返回字符串
                * 将一个时间戳(默认为当前时间)转换成一个时间字符串
            * localtime([secs]) seconds --> a date tuple 返回tuple结构
            * asctime([tuple]) tuple --> string
            * clock()
                * 在第一次调用的时候，返回的是程序运行的实际时间；
                * 以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
            * mktime(tuple) tuple -> local time
            * sleep(secs)
            * strptime(string[, format]) Parses a string into a time tuple
            * time.clock() # Current CPU time in seconds
            * time.localtime(secs) # Convert time to local time (returns a tuple).
            * time.gmtime(secs) # Convert time to GMT (returns a tuple)
            * time.asctime(tuple) # Creates a string representing the time
            * time.ctime(secs) # Create a string representing local time
            * time.mktime(tuple) # Convert time tuple to seconds
            * time.sleep(secs) # Go to sleep for awhile

<slide class="aligncenter fullscreen">
### misc {.zoomIn}

    find . -type f -name "*.py" | xargs python reindent.py --nobackup   -->  python2.6-examples
    pip install autopep8
    autopep8 your_script.py # dry-run, only print
    autopep8 -i your_script.py # replace content
    autopep8 --in-place --aggressive --aggressive foo.py

    find . -type f -name "*.py" |  autopep8 --in-place --aggressive --aggressive {}

pylint可以看写的合不合规范

    * pip install pylint
    * pylint xxx.py

<slide class="aligncenter fullscreen">
### monkey patching {.zoomIn}

"monkey patching" means adding a new variable or method to a class after it's been defined. 
```python

class A(object):
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return A(self.num + other.num)

def get_num(self): 
    return self.num

A.get_num = get_num
```

<slide class="aligncenter fullscreen">
### Pythonic 就是很 Python 的 Python 代码 {.zoomIn}

```python
c = a if a > b else b


with open(path, mode) as fp:
    pass  # do something
```

<slide class="aligncenter fullscreen">
### Zen of Python {.zoomIn}
```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```