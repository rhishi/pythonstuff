"""
Convenient wrapper for running a IPython demo.

To run a demo, execute the following:

    import ipydemo; ipydemo.run('script.py')

Suffix .py can be dropped.  "_ipydemo.py" is another suffix
that can be dropped.

See ipydemodemo.py for an example demo script.
"""
import os
import IPython.lib.demo as Demo

def run(script):
    """
    Creates and runs an IPython demo given a script.
    Examples:
        run('ipydemo.py') or just run('ipydemo')
        run('gaussian_ipydemo.py') or just run('gaussian')
    """
    if not os.path.exists(script):
        if os.path.exists(script + "_ipydemo.py"):
            script += "_ipydemo.py"
        elif os.path.exists(script + ".py"):
            script += ".py"
        else:
            print "Error: cannot find script:", script
            return
    demo = Demo.Demo(script)
    while not demo.finished: demo()
    demo.reset()
    return demo


