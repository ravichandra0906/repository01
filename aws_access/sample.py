dict_1 = {"key1":"value1","key2":"value2","key3":"value3"}

# if "key1" in dict_1:
#     print("ok")
#
# print(type(None))

# def foo(temp=[]):
#     temp.append("b")
#     print(temp)
#
#
# foo()
# foo()

# print(len(set([1,1,2,3,3,3,4])))

# print(len(set([[1,2],[3,4]])))

# print(len(set([[1,1,2,3,3,3,4],[1,1,2,3,3,3,4]])))

# if "key1" in dict_1.keys():
#     print("ok")
# else:
#     print("not ok")
#
# for k,v in dict_1.items():
#     print(k,v)
#
# L1 = ["a", 2, "c"]
#
# L2 = ["b", 3]
#
# L1.extend(L2)
#
# print(L1)
# def my_func(*args):
#     for arg in args:
#         print(arg)
#
# my_func(1, 2, 3)

def dec_fun(fun):
    def latin(*args):
        for arg in args:
            b = arg.upper()
            print(fun(b))
    return latin

@dec_fun
def nrm(*args):
    return args

print(nrm("chandra","sekhar","madasu"))