immutable_var=(1,2,True,"fghj")
print(immutable_var)
# immutable_var[1]=7 # при попытки изменить кортеж, пояувляется ошибка, так как смысл кортежа в его неизменности , что влияет на уменьшение размера информации в строке
# Но можно поместить в кортеж список и уже менять список внутри кортежа
immutable_var_1=([1,2,3],True,"fghj")
immutable_var_1[0][1]=7
print(immutable_var_1)# таким образом изменен объект "2" на "7" внутри списка,находящегося внутри кортэжа
mutable_list=[1,2,9,12,963]
mutable_list[0]=6
mutable_list.append(False)
mutable_list.extend("Roman")
mutable_list.remove(2)
mutable_list.remove(9)
mutable_list.remove(12)
mutable_list.remove(963)
print(mutable_list)
