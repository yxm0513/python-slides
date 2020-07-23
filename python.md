title: Python From Scratch
speaker: yangxinming
transition: cards
prismTheme: dark
css:
    - css/base.css
    - css/gh-fork-ribbon.min.css
js:
    - js/zoom.js
    - js/base.js
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
 * misc & environ{.bounceInRight}
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
:::column {.mycolumn}
![](/img/docs.png)


----
:::div {.mydiv}
* pydoc -k <keyword> -p <port> {.animated.zoomIn}  
* help(module or function name obj) {.animated.zoomIn}
* print(obj.\_\_doc\_\_) {.animated.zoomIn}
* docs.python.org{.animated.zoomIn}
* google, stackoverflow {.animated.zoomIn}
* source code {.animated.zoomIn}
{.build.description.text-intro}
:::
:::

<slide class="aligncenter fullscreen">
### basics - installations & run {.zoomIn}

:::column {.mycolumn}

![](/img/python.png)

----
##### installations{.content-left.tobuild}
  * python/venv {.zoomIn.tobuild}
  * libraries {.zoomIn.tobuild}
    * apt-get, python setup.py install {.zoomIn.tobuild}
    * easy_install {.zoomIn.tobuild}
    * pip -> pip install -r requirements.txt, pip freeze > requirements.txt {.zoomIn.tobuild}
##### run {.content-left.tobuild}
  * interupter {.zoomIn.tobuild}
  * python xxx.py {.zoomIn.tobuild}


<slide class="aligncenter fullscreen">
### basics - editing & debugging
<br>
:::div {.mydiv}
* vim, VS code, pycharm, sublimetext {.zoomIn.tobuild}
* pdb{.zoomIn.tobuild}
* vprof, python -m cProfile -m module | myscript.py{.zoomIn.tobuild}
* coverage.py {.zoomIn.tobuild}
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### data types {.zoomIn}
<br>
:::div {.mydiv}
 * bool、int、long、float 和 complex {.zoomIn.tobuild}
 * 字符串、元组、列表、集合，字典{.zoomIn.tobuild}
 * 定义，方法，转换, inspect {.zoomIn.tobuild}
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### conditionals and loops {.zoomIn}
<br>
:::div {.mydiv}
 * if x\:  or if not x\: {.zoomIn.tobuild}
 * for x in \: {.zoomIn.tobuild}
 * while xxx \: {.zoomIn.tobuild}
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### functions - def xxx_name()\: {.zoomIn}

:::div {.mydiv}
 * 函数定义时,三个类型参数 {.zoomIn.tobuild}
   * positioned arg {.zoomIn.tobuild}
   * \*args表示任何多个无名参数，它是一个tuple； --> \*p 不管什么参数传进来，就转换成tuple{.zoomIn.tobuild}
   * \*\*kwargs表示关键字参数，它是一个dict。并且同时使用\*args和\*\*kwargs时，必须\*args参数列要在\*\*kwargs前  --> \*\*p是转换成dict{.zoomIn.tobuild}
   * 如果同时出现，看调用的时候的格式=来标识dict开始{.zoomIn.tobuild}
 * 函数调用时候，\* \*\*相当于dearchive成tuple和key=value的形式，再传入{.zoomIn.tobuild}
 * 默认参数{.zoomIn.tobuild}
:::

<slide class="aligncenter fullscreen">
### functions \: arguments {.zoomIn}

![](/img/dearch.png)

![](/img/dearch2.png)



<slide class="aligncenter fullscreen">
### functions as objects {.zoomIn}

:::div {.mydiv}
* 一个函数是一个被它自己定义而执行的对象;{.zoomIn.tobuild}
* 默认参数是一种"成员数据",functions的状态和其他对象一样,会随着每一次调用而改变.{.zoomIn.tobuild}
	* have types{.zoomIn.tobuild}
	* can be sent as arguments to another function{.zoomIn.tobuild}
	* can be used in expression{.zoomIn.tobuild}
	* can become part of various data structures like dictionaries{.zoomIn.tobuild}
* 属性 {.zoomIn.tobuild}
    * '\_\_module\_\_' \: 函数模块{.zoomIn.tobuild}
    * '\_\_name\_\_' \: 函数名称{.zoomIn.tobuild}
    * '\_\_defaults\_\_' \: 默认参数{.zoomIn.tobuild}
    * '\_\_doc\_\_' \: 文档{.zoomIn.tobuild}
    * '\_\_code\_\_' \: code object{.zoomIn.tobuild}
:::
![](/img/func.png)


<slide class="aligncenter fullscreen">
### 装饰器

:::div {.mydiv}
 * @ is syntactic sugar for closing over a function
 * 装饰器 \: 要实现的效果就是给不同的函数插入相同的功能
 * 制造函数的函数
{.build.description.text-intro}
:::
![](/img/decorator.png)
func = decorator(args)(func)


<slide class="aligncenter fullscreen">
### class

:::div {.mydiv}
* namepace \: Class -- define a boxed set of data and functions.{.zoomIn.tobuild}
	* Classes provide a means of bundling data and functionality together.{.zoomIn.tobuild}
	* Creating a new class creates a new type of object, allowing new instances of that type to be made.{.zoomIn.tobuild}
	* Classes are just basically custom types.{.zoomIn.tobuild}
{.build.description.text-intro}
:::
<slide class="aligncenter fullscreen">
### class

:::div {.mydiv}
* c = classname() \: --> 实例化 {.zoomIn.tobuild}
  * \_\_init\_\_(self, *args)  \: 初始化方法 {.zoomIn.tobuild}
  * \_\_new\_\_(cls, *args, \*\*kwargs) \: 构造函数 {.zoomIn.tobuild}
  * \_\_new\_\_方法用于创建对象并返回对象，当返回对象时会自动调用\_\_init\_\_方法进行初始化。\_\_new\_\_方法是静态方法，而\_\_init\_\_是实例方法 {.zoomIn.tobuild}
  * \_\_new\_\_() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation. {.zoomIn.tobuild}
* python的类没有访问权限的问题，也就是说所有的变量都是可访问的,私有的机制，就是在属性前加__，但是这种私有机制实际上也是伪私有，因为它其实是用一个别名来保存这个属性 {.zoomIn.tobuild}
* 允许多重继承，类似C++,不同于java {.zoomIn.tobuild}
* 多态Polymorphism \: 通过参数的不同来区分不同的func {.zoomIn.tobuild}
{.build.description.text-intro}
:::

<slide class="aligncenter fullscreen">
### metaclass & \_\_new\_\_
:::column {.aligncenter}
<img src="/img/meta1.png" class='aligncenter' width=400 onclick="myfunction(this)">
<img src="/img/meta3.png" class='aligncenter' width=400 onclick="myfunction(this)">

----

<img src="/img/meta2.png" class='aligncenter' width=400  onclick="myfunction(this)">

:::

<slide class="aligncenter fullscreen">
### class \: object

:::div {.mydiv}
* .func()
* type(object)
* isinstance(object, class)
* callable(object)
* getattr(object, name[, default])
* hasattr(object, name)
* setattr(object, name, value)
* is / is not
{.bounceInRight.build}
:::

<slide class="aligncenter fullscreen">
### class \: 继承 {.zoomIn}

:::div {.mydiv}
* class classname (parent,)\:  super --> MRO序列 -> Method Resolution Order
* issubclass(A, B)
* 继承关系本质上是设置 sub.\_\_bases\_\_ = (super, )
* 子类中需要调用父类的函数：super(P, self).func(arg)
* sub会继承所有super的变量和函数，需要overwrite的时候，使用相同名称在sub里定义一遍就行了.
{.bounceInRight.build}
:::

```python
print(C.mro())
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```


<slide class="aligncenter fullscreen">
###  class \: 属性

#### 类属性
```python
class ClassName:
    attr = “test”;
```
#### 实例属性

```python
class ClassName:
def __init__(self, name):
    self.name = name
```

<slide class="aligncenter fullscreen">
###  class \: \_\_dict\_\_
:::div {.mydiv}
* 用来存属性 {.zoomIn.tobuild}
  * class的存在 obj.\_\_class\_\_.\_\_dict\_\_里   -> Class 也是type的一个instance {.zoomIn.tobuild}
  * object 的存在 object.\_\_dict\_\_里 {.zoomIn.tobuild}
* 查找是先查object的，再查class的，查不到AttributeError {.zoomIn.tobuild}
* 修改属性的时候，mutable的list,dict需要特别小心，因为从instance修改，class的也就被修改了，和inmutable的不一样，因为是reference. (avoid class variables unless you have a reason to use them) {.zoomIn.tobuild}
* __dict__是dir()的子集，dir()包含__dict__中的属性。{.zoomIn.tobuild}
{.bounceInRight.build}
:::

![](/img/dict.png)

<slide class="aligncenter fullscreen">
### class \: \_\_dict\_\_
:::column {.sm .aligncenter}
<img src="/img/dict1.png" class='aligncenter' width=400 onclick="myfunction(this)">

----

<img src="/img/dict2.png" class='aligncenter' width=600  onclick="myfunction(this)">

:::

<slide class="aligncenter fullscreen">
###  class \: \_\_slots\_\_
:::div {.mydiv}
* \_\_dict\_\_ 来存属性，当属性和实例特别多的时候，特别浪费内存，{.zoomIn.tobuild}
* 有时候我们只想使用固定的对象，而不想任意绑定对象，这时候我们可以定义一个属性名称集合，只有在这个集合里的名称才可以绑定。__slots__就是完成这个功能的。 {.zoomIn.tobuild}
{.bounceInRight.build}
:::
```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```
```    
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'

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
###  class \: \@property {.zoomIn}
:::div {.mydiv}
* \@property 可以将python定义的函数“当做”属性访问，从而提供更加友好访问方式，但是有时候setter/getter也是需要的 {.zoomIn.tobuild}
:::
:::column {.aligncenter}
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
----

```python
class Parrot(object):
    def __init__(self):
        self._voltage = 100000
 
    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage
```
:::

<slide class="aligncenter fullscreen">
###  class \: method
:::div {.mydiv}
* 和一般的方法没有差别，创建了一个方法的实例，使用class的namespace.  {.zoomIn.tobuild}
* 实例方法 \:def function_name(self, )\: ⇒ Class().function_name() {.zoomIn.tobuild}
  * 初始化方法 def \_\_init\_\_(self, name)\: {.zoomIn.tobuild}
  * 析构函数 def \_\_del\_\_(self)\: {.zoomIn.tobuild}
* 类方法 \:  {.zoomIn.tobuild}
  * @classmethod {.zoomIn.tobuild}
  * def function_name(cls, )\:  ⇒ Class.function_name(){.zoomIn.tobuild}
  * 一个类方法就可以通过类或它的实例来调用的方法, 不管你是用类来调用这个方法还是类实例调用这个方法,该方法的第一个参数总是定义该方法的类。{.zoomIn.tobuild}
* 静态方法 ： {.zoomIn.tobuild}
  * @staticmethod {.zoomIn.tobuild}
  * def function_name()\:    ⇒ Class.function_name()  --> 可直接用class后跟的这个名字，也可是传入的cls {.zoomIn.tobuild}
  * 有很多情况下一些函数与类相关，但不需要任何类或实例变量就可以实现一些功能 (.eg 环境相关，连接数据库等) {.zoomIn.tobuild}
  * 好处是，不需要定义实例即可使用这个方法。另外，多个实例共享此静态方法。  -->相当于package带的一个方法 {.zoomIn.tobuild}
{.bounceInRight.build}
:::

<slide class="aligncenter fullscreen">
### Module & Package
:::div {.mydiv}
* .py 单文件表示模块，目录下\_\_init\_\_.py表示package {.zoomIn.tobuild}
* import packge 会先import \_\_init\_\_.py, 如果使用import package相当于import了package下的\_\_init\_\_.py {.zoomIn.tobuild}
* import * 对应package 下 \_\_init\_\_.py 中 \_\_all\_\_释出的函数，{.zoomIn.tobuild}
{.bounceInRight.build}
:::

<slide class="aligncenter fullscreen">
### import
:::div {.mydiv}
* import主要是做了二件事 {.zoomIn.tobuild}
  1. 查找相应的module -> sys.modules -> sys.meta_path _>  sys.path_hooks, sys.path_importer_cache, sys.path -> ImportError{.zoomIn.tobuild}
  2. 加载module到module global namespace  --> import一个module，文件就从头到尾执行一遍,并形成关联 {.zoomIn.tobuild}
* sys.modules {.zoomIn.tobuild}
  1. 导入一个新的模块的时候,会在sys.module中插入一条key-value对，key是module名，value就是所导入的module对象。{.zoomIn.tobuild}
  2. 当下一次import相同模块的时候，会先在sys.module中查找该模块，如果存在则直接导入sys.module中的module对象。{.zoomIn.tobuild}
  3. 将module对象加入到global namespace中，当程序需要调用该模块时，会从global namespace中检索。{.zoomIn.tobuild}
* 语法 {.zoomIn.tobuild}
	* import folder 只是导入package，相当于执行\_\_init\_\_.py文件 {.zoomIn.tobuild}
	* from folder import abcd则执行了\_\_init\_\_.py文件文件与abcd.py文件{.zoomIn.tobuild}
	* from folder.abcd import b也执行了\_\_init\_\_.py文件文件与abcd.py文件{.zoomIn.tobuild}
	* import path.file.func 使用时需要全路径{.zoomIn.tobuild}
	* from path import file 使用file.func{.zoomIn.tobuild}
	* from path.file import func 直接使用func{.zoomIn.tobuild}
* \_\_import\_\_() {.zoomIn.tobuild}
    * function can be used to import modules where the name is only known at runtime --> 动态的导入（module层面）
    * using import somename will add somename to your namespace, but \_\_import\_\_('somename') instead returns the imported module {.zoomIn.tobuild}
    * xxx = \_\_import\_\_("xxx"){.zoomIn.tobuild}
    * mod = \_\_import\_\_(r"C:/path/to/file/anywhere/on/computer/module.py"){.zoomIn.tobuild}
* dir() is used to find out which names a module defines{.zoomIn.tobuild}
{.bounceInRight.build}
:::

<slide class="aligncenter fullscreen">
### \_\_main\_\_ module
:::div {.mydiv}
* for i in sys.modules\: print(i)   --> \_\_main\_\_
* dir(\_\_main\_\_)
* if \_\_name\_\_ == '\_\_main\_\_'\: 判断是本脚本运行，还是做为模块被使用，搜索路径sys.path
{.bounceInRight.build}
:::
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
>>> print(__main__.os)
<module 'os' from '/usr/local/bin/../../../Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py'>
>>> print(__main__.sys)
<module 'sys' (built-in)>
>>> import re
>>> dir(__main__)
['__annotations__', '__builtins__', '__doc__', '__loader__', '__main__', '__name__', '__package__', '__spec__', 'i', 'os', 're', 'sys']
```
<slide class="aligncenter fullscreen">
### \_\_main\_\_ module
```python
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

<slide class="aligncenter fullscreen">
###  module d.py
```python
~ cat d.py
import re

def f():
    pass
```
<slide class="aligncenter fullscreen">
###  module d.py
```python
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
...
```
<slide class="aligncenter fullscreen">
###  updated module d.py
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

<slide class="aligncenter fullscreen">
### \_\_main\_\_ module

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
### Namespace {.zoomIn}

:::div {.mydiv}
* 简单的讲就是：name到对象的映射 {.zoomIn.tobuild}
* LEGB\: LOCAL>ENCLOSING>global>built_in {.zoomIn.tobuild}
	* locals\:函数内部的名字空间，一般包括函数的局部变量以及形式参数 {.zoomIn.tobuild}
	* locals()是只读的(不能改变)，globals不是（可以改变）{.zoomIn.tobuild}
	* locals()没有返回局部命名空间，它返回的是一个拷贝。所以对它进行改变，对局部命名空间中的变量值没有影响{.zoomIn.tobuild}
	* enclosing\:在嵌套函数中外部函数的名字空间, 对fun2来说， fun1的名字空间就是.{.zoomIn.tobuild}
	* globals\:当前的模块空间，模块就是一些py文件。也就是说，globals()类似全局变量。{.zoomIn.tobuild}
	* globals()返回全部实际命名空间，而非拷贝。所以globals返回的dict任何改动都会影响到全局变量{.zoomIn.tobuild}
	* \_\_builtins\_\_\: 内置模块空间，也就是内置变量或者内置函数的名字空间。{.zoomIn.tobuild}
{.bounceInRight.build}
:::

<slide class="aligncenter fullscreen">
### Namespace {.zoomIn}
:::div {.mydiv}
* Python 一切皆对象，每个对象都具有 一个ID、一个类型、一个值；对象一旦建立，ID 便不会改变，可以直观的认为 ID 就是对象在内存中的地址{.zoomIn.tobuild}
* 标识符\:  各类对象的名称，比如函数名、方法名、类名，变量名、常量名等。 identifier，中文名为“标识符”{.zoomIn.tobuild}
* 在 Python 中赋值并不会直接复制数据，而只是将名称绑定到对象{.zoomIn.tobuild}
* 命名空间：（英语：Namespace）表示标识符（identifier）的可见范围。 简而言之，命名空间可以被简单的理解为：存放和使用对象名字的抽象空间。{.zoomIn.tobuild}
* 与命名空间相对的一个概念就是“作用域”，那么什么又是作用域呢？作用域：（英文 Scope）是可以直接访问到命名空间的文本区域。{.zoomIn.tobuild}
{.bounceInRight.build}
:::

<slide class="aligncenter fullscreen">
### containers vs. iterators vs. generators {.zoomIn}
:::div {.mydiv}
:::column {.sm .aligncenter}
 * container \:  {.zoomIn.tobuild}
   * list, deque, …. {.zoomIn.tobuild}
   * set, frozensets, ….{.zoomIn.tobuild}
   * dict, defaultdict, OrderedDict, Counter, ….{.zoomIn.tobuild}
   * tuple, namedtuple, ….{.zoomIn.tobuild}
   * str{.zoomIn.tobuild}
 * iterators \: \_\_iter\_\_ \_\_next\_\_   {.zoomIn.tobuild}
 * generators \: yield{.zoomIn.tobuild}
   * (i for i in range(10)) {.zoomIn.tobuild}
   * def func(data)\:  for i in data\: yield i {.zoomIn.tobuild}

----

<img src="/img/generator.png" class='aligncenter' width=700  onclick="myfunction(this)">
:::

<slide class="aligncenter fullscreen">
### containers vs. iterators vs. generators {.zoomIn}

```python
>>> a =[1, 2, 3, 4]
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> b = iter(a)
>>> type(b)
<class 'list_iterator'>
>>> dir(b)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
>>> b.__next__()
1
>>> b.__next__()
2
>>> b.__next__()
3

>>> (x for x in [1,2,3])
<generator object <genexpr> at 0x7f8177ad1ed0>


>>> def test_func():
...     for x in [1,2,3]:
...             yield x
...
>>> test_func()
<generator object test_func at 0x7f8177ad1ed0>

>>> for x in test_func():
...     print(x)
...
1
2
3


```


<slide class="aligncenter fullscreen">
### errors and exceptions
```python
try:
  <statements>
expect <异常>:
  <>
else:
  <>
finally:
  <>

```

<slide class="aligncenter fullscreen">
### errors and exceptions

    * 所有异常 expect Expection, e: or expect:
    * 抛出异常
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
:::div {.mydiv.content-left}
* 查看所有keywords
:::
```python
import keyword
print(keyword.kwlist)
```
:::div {.mydiv.content-left}
* 查看builtins
:::
```python
dir(__builtins__)
```

<slide class="aligncenter fullscreen">
### eval, exec, compile
<br>
:::div {.mydiv}
 * eval -> 输入expression, expr -> value {.zoomIn.tobuild}
 * exec -> python code string  --> ignore return value {.zoomIn.tobuild}
 * compile {.zoomIn.tobuild}
    * exec mode -> python file --> bytecode and return None{.zoomIn.tobuild}
    * eval mode -> python file --> bytecode and return value{.zoomIn.tobuild}
{.build.description.text-intro}
:::
![](/img/exec.png)

<slide class="aligncenter fullscreen">
### monkey patching {.zoomIn}
:::div {.mydiv}
 * "monkey patching" means adding a new variable or method to a class after it's been defined. {.zoomIn.tobuild}
 * 将新的module替换掉sys.modules中的对象，如果该module还未被导入，则先对进行加载。这样，当程序需要导入module的时候，就会从sys.modules中导入被修改后打module对象，也就实现了monkey patch。 {.zoomIn.tobuild}
:::
:::column {.aligncenter}
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
----

<img src="/img/monkey.png" class='aligncenter' width=400  onclick="myfunction(this)">

:::

<slide class="aligncenter fullscreen">
### regex {.zoomIn}
:::column {.aligncenter}


```python
import re
patterns = 'abc'
p = re.compile(patterns)
r = p.match(string)

or

result = re.match(patterns, string)
```
----


:::div {.mydiv}
* 是否匹配 ?{.zoomIn.tobuild}
	* MatchObject or None{.zoomIn.tobuild}
* 匹配的部分，和原字串的关系 ?{.zoomIn.tobuild}
	* a.string —>原始的需要匹配的字串{.zoomIn.tobuild}
	* a.group -> 匹配到的字符串{.zoomIn.tobuild}
:::

:::

<slide class="aligncenter fullscreen">
### re {.zoomIn}
:::div {.mydiv}
* 正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。正则表达式被编译成 `RegexObject` 实例，可以为不同的操作提供方法。
* compile  --> p object
  * DOTALL, S 使.匹配包括换行在内的所有字符
  * IGNORECASE, I 使匹配对大小写不敏感
  * LOCALE, L 做本地化识别（locale-aware）匹配
  * MULTILINE, M 多行匹配，影响 ^ 和 $
  * VERBOSE, X 能够使用 REs 的 verbose 状态，使之被组织得更清晰易懂
:::
<slide class="aligncenter fullscreen">
### re \: RegexObject & MatchObject{.zoomIn}
:::column {.aligncenter.build.zoomIn}

* .match 如果 string 开始的0或者多个字符匹配到了正则表达式样式，就返回一个相应的 匹配对象 。 如果没有匹配，就返回 None ；注意它跟零长度匹配是不同的。
* .search 扫描整个 字符串 找到匹配样式的第一个位置，并返回一个相应的 匹配对象。如果没有匹配，就返回一个 None ； 注意这和找到一个零长度匹配是不同的。
* .findall()
* .split() 分割
*  p.sub, subn 替换

----

* group (?P<组名>Patterns)\:
    * 和perl 一样partens中()表示组，p.group(n) 来取出相应的组，
    * (?P<组名>Patterns) 来命名组,命名组可以用p.group(“组名”)取得。
    * p.groupdict获取所有组。
    * start([group]), end([group]) 分别返回第一个和最后一个。
* 注意group(0)是所有匹配的字符串，group(1)才是第一个匹配的group
* groups
* span \: Returns both the beginning and ending positions of a group
* escape(string) : Escapes all special regexp characters in string




<slide class="aligncenter fullscreen">
### system commands
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
### 输出输出
:::column {.aligncenter}

```python
import sys
for line in sys.stdin:
    process(line)
```

----

:::div {.mydiv}
* raw_input()/input : string / number
* print / sys.stdout.write  sys.stderr.write()
    * “%s”% str
    * %r raw data,调试比较有用处，区别%d,%s,'\n'类的转义，%r不会转义
* sys.stdin - Standard input
* sys.stdout - Standard output
* sys.stderr - Standard error
:::



<slide class="aligncenter fullscreen">
### 文件&目录操作 {.zoomIn}
:::column {.aligncenter}

    * files = glob.glob('*.py')
    * f= open(name[, mode[, buffering]])
        * 'r' Read mode
        * 'w' Write mode
        * 'a' Append mode
        * 'b' Binary mode (added to other mode)
        * '+' Read/write mode (added to other mode)
        * open().write(msg)
    * f.read()
        * f.readline()
        * f.readlines()
        * for eachline in f\:
        * for eachline in f.readline()\:
    * f.write()
        * f.writeline()
        * f.writelines()
    * f.close()
    * f.closed()

----

    * for (dirpath, dirnames, filenames) in os.walk(basedir):
    * os.path.join(,)
    * os.path.abspath()
    * os.listdir

<slide class="aligncenter fullscreen">
### 并发 {.zoomIn}
:::column {.aligncenter}
![](/img/proc.png)

----

![](/img/proc1.png)


<slide class="aligncenter fullscreen">
### Process & Thread 使用方式 {.zoomIn}
:::div {.mydiv}
  * class 继承方式：实现run 方法， 实例化后一样使用.start(), .join()方法
  * 传入target参数直接实例化Thread or Process, 然后start(),.join()方法
  * Lock 或Event， Queue, 信号量都是外边创建好，传入Process、Thread 使用即可
{.build.description.text-intro}
:::

:::column {.aligncenter}
<img src="/img/process_target.png" class='aligncenter' width=300 onclick="myfunction(this)">

----
<img src="/img/process_class.png" class='aligncenter' width=300 onclick="myfunction(this)">

----

<img src="/img/asynic.png" class='aligncenter' width=400  onclick="myfunction(this)">

:::


<slide class="aligncenter fullscreen">
### Process {.zoomIn}
:::column {.aligncenter}
```python
    import os
    pid = os.fork()      # Create child
    if pid == 0:
        # Child process
        os.execvp("ls", ["ls","-l"])
    else:
        os.wait()        # Wait for child
```
----

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
:::

<slide class="aligncenter fullscreen">
### sys(python) 系统相关{.zoomIn}
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
###  os 操作系统{.zoomIn}
:::column  {.mycolumn}
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

----
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
:::
<slide class="aligncenter fullscreen">
#### time{.zoomIn}
:::column {.mycolumn}
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

----  
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
### Web Development
:::column {.mycolumn}

```python
# python3
python3 -m http.server

# python2
python -m SimpleHTTPServer
```

<img src="/img/http.jpg" class='aligncenter' width=500  onclick="myfunction(this)">

----

:::div {.mydiv}
 * Flask, Django
 * ORM
 * Database
 * WSGI
:::



<slide class="aligncenter fullscreen">
### Others
<br>
:::div {.mydiv}
 * 测试,系统管理相关 {.zoomIn.tobuild}
 * 网络， 爬虫 {.zoomIn.tobuild}
 * 数据分析，可视化{.zoomIn.tobuild}
 * GUI，图像处理 {.zoomIn.tobuild}
 * AI {.zoomIn.tobuild}
 * 其他语言交互 {.zoomIn.tobuild}
:::

<slide class="aligncenter fullscreen">
### misc
:::column {.mycolumn}

代码格式化

    find . -type f -name "*.py" | xargs python reindent.py --nobackup   -->  python2.6-examples
    pip install autopep8
    autopep8 your_script.py # dry-run, only print
    autopep8 -i your_script.py # replace content
    autopep8 --in-place --aggressive --aggressive foo.py

    find . -type f -name "*.py" |  autopep8 --in-place --aggressive --aggressive {}

    pip3 install black
    find ./ -name '*.py' | xargs black

----

pylint 编码规范

    * pip install pylint
    * pylint xxx.py



<slide class="aligncenter fullscreen">
### Pythonic 就是很 Python 的 Python 代码 {.zoomIn}
:::column {.mycolumn}

```python
c = a if a > b else b
```

----

<img src="/img/code1.png" class='aligncenter' width=400 onclick="myfunction(this)">

----

<img src="/img/code2.png" class='aligncenter' width=400  onclick="myfunction(this)">

:::


<slide class="aligncenter fullscreen">
### Zen of Python
:::column {.mycolumn}

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
----

```
美丽的比丑陋的更好。
显式的比隐式的更好。
简单的比复杂的更好。
复杂的比难以理解的更好。（不能简化，至少还要保证可理解）
平整的比嵌套的更好。
稀疏的比密集的更好。
可读性很有价值。
特殊情况并没有特殊到需要破坏规则的程度。
然而，实用性打败了纯粹的代码美学。（现实应用更重要）
错误永远不应该无声无息，
除非被显式地抑制。
面对模糊不清时，拒绝去猜测，
应该有且只有一个更好的明确清晰的方法，去解决问题。
虽然这个方法一开始可能并不明显，除非你是荷兰人（指Python之父Guido）。
现在开始做比永远不做更好。
虽然永远不做常常优于没有思考的直接行动。
如果实现方式很难解释，这就不是好的实现。
如果实现方式很容易解释，这可能是好的实现。
命名空间是一个超好的机制，我们需要多多地应用。
```

<slide class="aligncenter fullscreen">
### Thanks
