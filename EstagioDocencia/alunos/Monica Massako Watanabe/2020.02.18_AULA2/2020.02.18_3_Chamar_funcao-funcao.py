def PP(x: int)->int:
  return QQ(x) + QQ(x+1)

def QQ(y: int)->int:
  return y*2

print(PP(int(input())))

#http://donkirkby.github.io/live-py-plugin/demo/ --> se colocarmos o comando, ele explica o que foi feito; mas não esquecer de tirar o input() e colocar um valor