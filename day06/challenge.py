import time;

startingTime = time.time();

def fastPow(nombre : int, pow : int) :
    if pow == 1 :
        return nombre;
    elif pow%2 == 0 :
        return (fastPow(nombre*nombre, pow/2));
    else :
        return (nombre * fastPow(nombre*nombre, (pow-1)/2));

# def calc_power(number: int, power: int, result: int = 1) -> int:

#     if power % 2 == 1:
#         result = number
#     number= number
#     power //= 2

#     if power != 0:
#         return calc_power(number, power, result)

#     return result

#calc_power(42, 10000)
#print("Resultat :",float(fastPow(42, pow)));
fastPow(42, 168);

duration = time.time()- startingTime;
print("Temps :",duration);