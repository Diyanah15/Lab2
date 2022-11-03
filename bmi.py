height = float(input('enter height in cm : '))
weight = float(input('enter weight in kg : '))

def BMI(height, weight) :
    bmi = weight/(height**2) * 703
    if (bmi < 18.5) :
        return 'underweight', bmi

    elif (bmi >= 18.5 and bmi <= 25.0) :
        return 'underweight', bmi

    elif (bmi > 25.0) :
        return 'overweight', bmi
quote, bmi = BMI(height, weight)
print('Your BMI is {} and yor are : {}' .format(bmi, quote))