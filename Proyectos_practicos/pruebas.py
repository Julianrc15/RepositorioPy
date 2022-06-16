def vidas():
    num = 3
    while num in range(1,4):
        yield num
        print(f"Te quedan {num} vidas")
        num -= 1
print("Game Over")
 
generador = vidas()
print(next(generador))

