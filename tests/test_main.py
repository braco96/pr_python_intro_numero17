import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_busqueda_binaria():
    a = [1,3,5,7,9]
    assert mod.busqueda_binaria(a,1) == 0
    assert mod.busqueda_binaria(a,9) == 4
    assert mod.busqueda_binaria(a,2) == -1
