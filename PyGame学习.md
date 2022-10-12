# PyGame学习

## 导入和初始化

```python
import pygame
from pygame.locals import *//另一种导入方法

pygame.init()//初始化
pygame.font.init()//字体的初始化

```



## 绘制图像

### 通过列表理解

```py
>>> background = [1, 1, 2, 2, 2, 1]        #背景
>>> screen = [0]*6                         #新的空白屏幕
>>> for i in range(6):                     
...     screen[i] = background[i]
>>> print screen
[1, 1, 2, 2, 2, 1]
>>> playerpos = 3 #player的位置
>>> screen[playerpos] = 8  #在英雄的位置绘制英雄
>>> print screen
[1, 1, 2, 8, 2, 1]

```



### Blit

基本上，blit意味着将图形从一个图像复制到另一个图像。 更正式的定义是将数据数组复制到位映射数组（bitmapped array）的目的地。 您可以将blit视为“赋值（assigning）”像素。 就像在上面的screen列表中设置值一样，blitting会指定图像中像素的颜色。

```python
background = [terrain1, terrain1, terrain2, terrain2, terrain2, terrain1]
screen = create_graphics_screen()
for i in range(6):
     screen.blit(background[i], (i*10, 0))
playerpos = 3
screen.blit(playerimage, (playerpos*10, 0))

# 移动玩家
screen.blit(background[playerpos], (playerpos*10, 0))
playerpos = playerpos - 1
screen.blit(playerimage, (playerpos*10, 0))

```





**屏幕坐标（Screen Coordinates）**
    要在屏幕上定位对象，我们需要告诉blit()函数放置图像的位置。在pygame中，我们总是将位置作为（X，Y）坐标传递。这表示向右的像素数，以及向下的像素数用来放置图像的。 Surface对象的左上角是坐标（0,0）。稍微向右移动（10,0），然后向下移动（10,10）。 当需要blitting时，position参数表示源的左上角应放在目标上的位置。
    Pygame为这些坐标提供了一个方便的容器，它是一个**Rect**。 Rect基本上代表这些坐标中的矩形区域。它有左上角以及大小。 Rect提供了许多方便的方法，可以帮助您移动和定位它们。在下面的例子中，我们将用Rect表示对象的位置。
    我们也知道pygame中的很多函数都需要Rect参数。**所有这些函数也可以接受4个元素（左，上，宽，高）【(left, top, width, height)】的简单元组**。您并不总是需要使用这些Rect对象，但您主要想要这样做。此外，blit()函数可以接受Rect作为它的位置参数，它只是使用Rect的左上角作为实际位置。





```python
>>> background = [terrain1, terrain1, terrain2, terrain2, terrain2, terrain1]
>>> screen = create_graphics_screen()
>>> for i in range(6):
...     screen.blit(background[i], (i*10, 0))
>>> playerpos = 3
>>> screen.blit(playerimage, (playerpos*10, 0))

```



### 平滑移动

```python
screen = create_screen()
>>> player = load_player_image()
>>> background = load_background_image()
>>> screen.blit(background, (0, 0))        #绘制背景
>>> position = player.get_rect()
>>> screen.blit(player, position)          #绘制玩家
>>> pygame.display.update()                #然后，把它们都展示出来
##下面的才是关键
 for x in range(100):                   #100帧
     screen.blit(background, position, position) #擦除上一帧的图像
     position = position.move(2, 0)     #移动玩家
     screen.blit(player, position)      #绘制新玩家
     pygame.display.update()            #然后，把它们都展示出来
     pygame.time.delay(100)             #暂停程序 1/10 秒
```



### Surface

理解surface对象的概念：可以填充一张纸或者任意图形等

```py
#也叫screen对象，本质上是一个Surface，大小400*400
screen = pygame.display.set_mode((400,400))

#创建一个包含文字的Surface对象
text = f.render("C语言中文网",True,(255,0,0),(0,0,0))
#通过blit方法将其绘制在主屏幕上，这里的textRect表示位置坐标
screen.blit(text,textRect)

surface_image =pygame.image.load("##图片路径##") 
```



## load函数（First, The Mystery Functions）

```python
player = pygame.image.load('player.bmp').convert()
background = pygame.image.load('liquid.bmp').convert()
```

- load()只需要一个文件名并返回一个带有加载图像的新Surface
- convert()生成一个新的surface并且转换为和当前显示器一致的像素



## 处理输入

```python
while 1:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
		move_and_draw_all_game_objects()
```

- 首先永远循环，然后检查用户是否有任何事件。

-  如果用户按下键盘或窗口上的关闭按钮，我们退出程序。

- 在我们检查了所有事件之后，我们移动并绘制了游戏对象。 （当然，我们也会在移动之前擦除它们）

## 事件组

```python
#游戏主循环(游戏循环)
while True:
    # 循环获取事件，监听事件
    for event in pygame.event.get():
        # 判断用户是否点了关闭按钮
        if event.type == pygame.QUIT:
            # 当用户关闭游戏窗口时执行以下操作
            # 这里必须调用quit()方法，退出游戏
            pygame.quit()
            #终止系统
            sys.exit()
    #更新并绘制屏幕内容
    pygame.display.flip() 
```

![image-20221011171143586](http://typora-yy.oss-cn-hangzhou.aliyuncs.com/img/image-20221011171143586.png)



## 精灵模块介绍

模块：`pygame.sprite`

API:[(104条消息) Pygame 官方文档 - pygame.sprite_小黑LLB的博客-CSDN博客_pygame spritecollide](https://blog.csdn.net/Enderman_xiaohei/article/details/88218773)

### 历史

 术语“精灵”是旧计算机和游戏机的延续。 这些旧盒子无法快速绘制和擦除普通图形，因此无法用作游戏。 这些机器具有特殊的硬件来处理这些游戏，里面对象需要非常快速地行动。 这些对象被称为“精灵”并具有特殊限制，但可以非常快速地绘制和更新。 它们通常存在于视频中的特殊叠加缓冲区中。 现在，**计算机已经变得足够快，可以在没有专用硬件的情况下处理精灵对象。 精灵术语仍然用于表示动画2D游戏中的任何内容。**



### 两种类：Sprite和Group

- Sprite类被设计为所有游戏对象的基类

1. 视为属于一个或多个组时的“有效（valid）”或“活着（alive）”。
2. kill()方法从它所属的所有组中删除sprite
3. alive()方法，如果它仍然是任何组的一个成员，则返回true。

- 组类（The Group Class）
  1. roup类只是一个简单的容器。与sprite类似，它有一个add()和remove()方法，可以更改属于该组的sprites。您还可以将一个精灵或精灵列表传递给构造函数（__init __()方法）以创建包含一些初始精灵的Group实例。
  2.  组类还有一些其他方法，如empty()，以从组中删除所有精灵，copy()将返回具有所有相同成员的组的副本。此外，has()方法将快速检查该组是否包含某个精灵或精灵列表。
  3. 另一个函数是sprites()方法。这将返回一个可以循环访问的对象，以访问该组包含的每个sprite。目前这只是精灵的列表，但在**更高版本的python中，这可能会使用迭代器来获得更好的性能。**
  4. pdate()方法，它将对组中的每个sprite调用update()方法。



### 混合使用

见教程

**关键的几个点**：

- Group就是对Sprite进行分类的快速简单方法。（每类游戏对象可以是一个组）

- 添加和删除Group和Sprite类在底层是经过优化的

- tips：**最好通过添加许多组来包含和组织游戏对象。对于添加许多组对于管理对象是没有任何坏处的**

  > You may be best off by adding many groups to contain and organize your game objects. Some could even be empty for large portions of the game, there isn't any penalties for managing your game like this.

### 多种类型的Group（自带的）

1.Group
    这是上面主要解释的标准“没有多余装饰的”组。 大多数其他组都来自这一组，但不是全部。
2.GroupSingle（单例模式的组）
    这与常规Group类完全相同，但它只包含最近添加的sprite。 因此，当您向该组添加一个精灵时，它会“忘记”它之前拥有的所有精灵。 因此它始终只包含一个或零个精灵。
3.RenderPlain
    这是从Group派生的标准组。 它有一个draw()方法，它将它包含的所有精灵都绘制到屏幕（或任何Surface）。为此，它需要它包含的**所有精灵都有一个“图像（image）”和“矩形（rect）”属性。 它使用这些来了解blit的内容以及blit的位置。**
4.RenderClear
    这是从RenderPlain组派生来的，并添加了一个名为`clear()`的方法。 这将删除所有绘制的精灵的先前位置。 它使用背景图像来填充精灵所在的区域。 当调用`clear()`方法时，它足够智能处理已删除的精灵并在屏幕上正确清除它们。
5.RenderUpdates
     这是渲染（rendering）组的凯迪拉克(????)。

> This is the Cadillac of rendering Groups. 

​	（这里的意思是最豪华，但是开销比较大的意思）

 	它继承自RenderClear，但更改**draw()方法也返回一个pygame Rects列表，它代表屏幕上已更改的所有区域。**



### 渲染组（render Group)



- 从上面我们可以看到有三种不同的渲染组。

  - RenderPlain
  - RenderClear
  - RenderUpdates

- 我们可能会放弃RenderUpdates，它增加的scrolling type game（滚动游戏）功能并不是我们真正需要的。

- 对于scrolling type game，每一帧背景会完全改变。我们显然不需要担心调用display.update()时python的更新矩形。**你必须使用RenderPlain组来管理你的渲染。**

  > You should definitely go with the `RenderPlain` group here to manage your rendering.

- 对于背景更稳定（每一帧不是全部改变）的游戏，你绝对不希望pygame更新整个屏幕（因为它不需要）。这种类型的游戏通常涉及擦除每个对象的旧位置，然后在每个帧的新位置绘制它。这样我们只会改变必要的东西。大多数情况下，您将仅想在此处使用RenderUpdates类。因为您还希望将此更改列表传递给display.update()函数。

- **RenderUpdates类还可以最大限度地减少更新矩形列表中的重叠区域**。如果对象的先前位置和当前位置重叠，则它将它们合并为单个矩形。将此与正确处理已删除对象的事实相结合，这是一个功能强大的Group类。如果你已经编写了一款游戏来管理游戏中对象的改变的矩形，你就会知道游戏中存在大量乱码的原因。特别是一旦你开始投入可以随时删除的对象。所有这些工作都缩减为使用此怪物类的clear()和draw()方法。加上重叠检查，它可能比你自己做的更快。

- **在游戏中应该混合使用和匹配这些渲染Group**。

  - 当想要使用你的精灵进行分层时，绝对应该使用多个渲染组。
  - 如果屏幕分为多个部分，屏幕的每个部分可能都应使用适当的渲染Group



### 碰撞检测（Collision Detection）

- 精灵模块还带有两个非常通用的碰撞检测功能。 
- 对于更复杂的游戏，通用的碰撞检测可能不适合，但获取它们的源代码，并根据需要进行修改。

以下是对它们的概述以及它们的作用：

- `spritecollide(sprite, group, dokill) -> list`

     这将检查单个精灵与组中精灵之间的冲突。 对于所有使用的精灵，它都需要“rect”属性。 它返回与第一个精灵重叠的所有精灵的列表。 **“dokill”参数是一个布尔参数。 如果True，则该函数将在所有Sprite上调用kill()方法。 这意味着每个Sprite的最后一个引用可能在返回的列表中。 一旦列表消失，Sprite就会消失。** 在循环中使用它的一个简单示例

```python
for bomb in sprite.spritecollide(player, bombs, True):
     boom_sound.play()
     Explosion(bomb, 0)
```



- `groupcollide(group1, group2, dokill1, dokill2) -> dictionary`

  这类似于`spritecollide`函数，但有点更加的复杂。 它检查一组中所有精灵的碰撞与另一组精灵的碰撞。 每个列表中的精灵都有一个dokill参数。 当dokill1为True时，group1中的碰撞精灵将会`kill`。 当`dokill2`为true时，group2的Sprite将会调用`kill`。 它返回的字典就像这样; 字典中的每个键都是来自group1的具有冲突的精灵。 该键的值是与之冲突的精灵列表：

  ```python
  for alien in sprite.groupcollide(aliens, shots, 1, 1).keys()#枚举外星人
  	boom_sound.play()# 爆炸声
      Explosion(alien, 0)#外星人爆炸函数
      kills += 1 #添加击杀外星人的数量
  
  ```

  此代码检查玩家子弹与他们可能交叉在一起的所有外星人之间的碰撞。 在这种情况下，我们只循环遍历字典键，但如果我们想对与外星人相撞的特定射击做一些事情，我们可以遍历values()或items()。 如果我们循环遍历values()，我们将循环遍历包含sprite的列表。 在这些不同的循环中，相同的精灵甚至可能出现不止一次，因为相同的“射击”可能与多个“外星人”相撞。



### 问题

**当您使用Sprite base派生新的sprite类时，必须从您自己的类`__init __()`方法中调用`Sprite .__ init __()`方法。 如果你忘记调用`Sprite .__ init __()`方法**



### 拓展

- **由于速度问题，当前的Group类只尝试完全满足他们的需求，而不是处理很多一般情况。 如果您确定需要额外功能，则可能需要创建自己的Group类。**
- Sprite和Group类被设计为可以扩展，因此您可以随意创建自己的Group类来执行特殊操作。 最好的起点可能是sprite模块的实际python源代码。 查看当前的Sprite组应该有关于如何创建您自己的组的足够的例子。
- 例如，下面是一个渲染组（rendering Group）的源代码，它为每个精灵调用一个render()方法，而不是只是从中调出一个“image”变量。 由于我们希望它也处理更新的区域，我们将从原始RenderUpdates组的副本开始，这里是代码：

​	

```python
class RenderUpdatesDraw(RenderClear):
    """调用sprite.draw(screen)来渲染Sprite对象"""
    def draw(self, surface):
        dirty = self.lostsprites #被修改过的Sprite
        self.lostsprites = [] #将修改过的重置为空
        for s, r in self.spritedict.items():#s是spirit，r是精灵类的rect
            newrect = s.draw(screen) #这里是大的改变
            if r is 0:
                dirty.append(newrect)
            else:
                dirty.append(newrect.union(r))
            self.spritedict[s] = newrect
        return dirty #修改过的对象
```



#### Sprite扩展

 `add_internal()”和“remove_internal()`。当这些类从它们自己移除一个精灵时，它们会被这些Group类调用。 add_internal()和remove_internal()有一个参数，它是一个组。你的精灵需要一些方法来跟踪它所属的组。您可能希望尝试将其他方法和参数与真正的Sprite类匹配，但如果您不打算使用这些方法，则你要确定不需要它们。



#### Group拓展

Group类的唯一其他要求是它们具有名为“_spritegroup”的虚拟属性。只要属性存在，值是什么并不重要。



****

关键在于浏览源码，sprite源码有注释是可以看懂的（虽然有点‘tuned')甚至源码还有TODO来等待这贡献者来完善