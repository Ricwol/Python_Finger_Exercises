# Finger exercise, p.122
# What does the following code print?
L = [1, 2, 3]
L.append(L)
print(L is L[-1])

# As lists only keep the reference to the start of the list, appending the same
# list to itself will result in an infinite recursive reference. That is due to
# the nature of lists being mutable, so by appending a list to itself, the
# appended list gets also updated, thus creating an infinite loop.

# See python tutor: https://pythontutor.com/render.html#code=%23%20Unintentional%20aliasing%20example,%20p.122%0AL1%20%3D%20%5B%5B%5D%5D*2%0AL2%20%3D%20%5B%5B%5D,%20%5B%5D%5D%0Afor%20i%20in%20range%28len%28L1%29%29%3A%0A%20%20%20%20L1%5Bi%5D.append%28i%29%0A%20%20%20%20L2%5Bi%5D.append%28i%29%0Aprint%28'L1%20%3D',%20L1,%20'but',%20'L2%20%3D',%20L2%29%0A%23%20Delete%20variables%20to%20clean%20up%20screen%0Adel%20L1,%20L2,%20i%0A%0A%23%20Finger%20exercise,%20p.122%0Al%20%3D%20%5B1,%202,%203%5D%0Al.append%28l%29%0Aprint%28l%20is%20l%5B-1%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
