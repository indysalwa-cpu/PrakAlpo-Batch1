nama_hero = "Dievyara"                                      
level = 10                                                  
health_point = 850.5                                        
is_alive = True                                             
inventory = ["Panah Gaib", "Tongkat Sihir", "Bola Kristal"] 
atribut = {
    "kekuatan": 80, 
    "kelincahan": 65
}                

print("Nama Hero    :", nama_hero)
print("Level        :", level)
print("Health Point :", health_point)
print("Status Hidup :", is_alive)
print("Inventory    :", inventory)
print("Atribut      :", atribut)

print("Nama Hero    :", type(nama_hero))
print("Level        :", type(level))
print("Health Point :", type(health_point))
print("Status Hidup :", type(is_alive))
print("Inventory    :", type(inventory))
print("Atribut      :", type(atribut))

inventory.append("Ramuan HP")
level = float(level) + 0.5

print("\n--- INFORMASI KARAKTER HERO TERBARU ---")
print("Nama Hero    :", nama_hero)
print("Level        :", level)
print("Health Point :", health_point)
print("Status Hidup :", is_alive)
print("Inventory    :", inventory)
print("Atribut      :", atribut)

input()