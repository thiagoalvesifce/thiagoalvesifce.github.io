valor = input()

n100 = valor//100
resto = valor%100
n50 = resto//50
resto = resto%50
n20 = resto//20
resto = resto%20
n10 = resto//10
resto = resto%10
n5 = resto//5
resto = resto%5
n2 = resto//2
resto = resto%2

print "NOTAS:"
print "%i nota(s) de R$ 100.00" %n100
print "%i nota(s) de R$ 50.00" %n50
print "%i nota(s) de R$ 20.00" %n20
print "%i nota(s) de R$ 10.00" %n10
print "%i nota(s) de R$ 5.00" %n5
print "%i nota(s) de R$ 2.00" %n2

print 'resto moedas1real:', resto
m1 = resto//1
resto = resto%1
print 'resto moedas50:', resto
m050 = resto//0.50
resto = resto%0.50
print 'resto moedas25:', resto
m025 = resto//0.25
resto = resto%0.25
print 'resto moedas10:', resto
m010 = resto//0.10
resto = resto%0.10
print 'resto moedas5:', resto
m05 = resto//0.05
resto = resto%0.05
print 'resto moedas1centavo:', resto
m01 = resto//0.01
print 'moedas1centavo:', m01

print "MOEDAS:"
print "%f moeda(s) de R$ 1.00" %m1
print "%f moeda(s) de R$ 0.50" %m050
print "%f moeda(s) de R$ 0.25" %m025
print "%f moeda(s) de R$ 0.10" %m010
print "%f moeda(s) de R$ 0.05" %m05
print "%f moeda(s) de R$ 0.01" %m01
