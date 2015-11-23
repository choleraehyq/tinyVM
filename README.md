# TinyVM

This tinyVM is an implementation of [GenTiradentes' TinyVM][tvm] in Python (the original is written in C).

This is my first attempt at a VM, so huge thanks to GenTiradentes for making a minimal one, easy to grasp. Also, [Specter][specter](the Go version) inspired me much, thanks to its author. 

## Run

This tinyVM depend on module enum. Module enum has already been a part of standard library in python 3.4+, if you are using other versions of python please run

`pip install enum34`

to install it.

`cd` to this directory

`python ./main.py --file /path/to/source`

## License

The [BSD 2-Clause license][bsd].

[bsd]: http://opensource.org/licenses/BSD-2-Clause
[tvm]: https://github.com/GenTiradentes/tinyvm
[specter]: https://github.com/PuerkitoBio/specter
