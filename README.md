# TinyVM

This tinyVM is an implementation of [GenTiradentes' TinyVM][tvm] in Python (the original is written in C).

This is my first attempt at a VM, so huge thanks to GenTiradentes for making a minimal one, easy to grasp. Also, [Specter][specter](the Go version) inspired me much, thanks to its author. 

## Run

`python ./main.py ./examples/fib.vm`

Attention: tinyVM is written in Python3. No compatibility to Python2. 

## License

The [BSD 2-Clause license][bsd].

[bsd]: http://opensource.org/licenses/BSD-2-Clause
[tvm]: https://github.com/GenTiradentes/tinyvm
[specter]: https://github.com/PuerkitoBio/specter
