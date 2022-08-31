from glance.cmd import cmd

def func1():
    print('我是api')
    cmd.func2()
    
if __name__ == '__main__':
    func1()