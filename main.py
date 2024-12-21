import random
con = ['+','-','/','*','!','&','$','#','?','=','@','a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
num = int(input("Introduzca la longitud de la contrasena: "))
clave = ''

for i in range (num):
    ch = random.choice(con)
    contra = clave + ch
    clave = contra

print ('La contrasena resultante es:',contra)