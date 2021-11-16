#import statistics 

def enrollment_stats(data):
    enrollment_values = []
    tuition_fees = []
    for value in data:
        enrollment_values.append(value[1])
        tuition_fees.append(value[2])
    return enrollment_values, tuition_fees

def mean(data):
    suma = sum(data)
    srednia = suma / len(data)
    return srednia
    
def median(data):
    data.sort()
    list_length = len(data)
    middle_index = int(list_length/2)
    if list_length % 2:
        #nieparzysta liczba elementów
        return data[middle_index]
    else:
        #parzysta liczba elementów
        return (data[middle_index-1] + data[middle_index])/2

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollment_values, tuition_fees = enrollment_stats(universities)

print("*****************************")
print(f"Total students:\t{sum(enrollment_values):,}")
print(f"Total tuition:\t$ {sum(tuition_fees):,}\n")

print(f"Student mean:\t{mean(enrollment_values):,.2f}")
print(f"Student median:\t{median(enrollment_values):,}\n")

print(f"Tuition mean:\t$ {mean(tuition_fees):,.2f}")
print(f"Tuition median:\t$ {median(tuition_fees):,}\n")
print("*****************************")

#print(statistics.median(enrollment_values))




