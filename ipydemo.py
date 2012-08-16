import IPython.lib.demo as Demo

def rundemo(script):
    demo = Demo.Demo(script)
    while not demo.finished: demo()
    demo.reset()
    return demo
