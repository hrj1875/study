class MusicPlayer(object):
    #记录第一个对象被创建 时的引用
    istance=None
    #标记初始化动作
    init_flag=False
    def __new__(cls, *args, **kwargs):
        if cls.istance is None:
          #1.判断iStance是否为空
           cls.istance=super().__new__(cls)
          #2.若为空就要给类属性赋值，即调用父类，为第一个对象分配空间
        return cls.istance
          #3.返回类属性保存的对象引用
    def __init__(self):
        if MusicPlayer.init_flag is True:
             return
        print('播放器初始化')
        MusicPlayer.init_flag=True
music1=MusicPlayer()
print(music1)