##############################################
# Point 1 - 2
# Overall max & min life expectancy
##############################################
lowest = 999
highest = -1
max_country = ""
high_country = ""
low_country = ""
data_A_historical_period = int
data_B_historical_period = int

##############################################
# Point 3
# lowest & highest  value for life expectancy
##############################################
min_life = 999
max_life = -1

min_country = ""
max_year = ""

##############################################

i = 0
avg = 0
x = 0

year_interest = int(input('Enter the year of interest: '))

#with open("life-expectancy.csv") as data_file:
with open("C:/Users/Fernando Cardozo/OneDrive/BYU/Web & Computer Programming/Winter 2023/CSE110/w11/life-expectancy.csv") as data_file:
    for line in data_file:
        #print("Entity: {0}, Code: {1}, Year: {2}, Life expectancy (years): {3}".format(row[0], row[1], row[2], row[3]))
        i = i + 1
        cleanline = line.strip()
        data = cleanline.split(',')

        if i > 1:
            entity = data[0]
            code = data[1]
            year = int(data[2])
            life_expectancy = float(data[3])

            if life_expectancy < lowest:
                lowest = life_expectancy
                low_country = entity
                data_A_historical_period = year
            
            if life_expectancy > highest:
                highest = life_expectancy
                high_country = entity
                data_B_historical_period = year

            if year_interest == year:
                avg = avg + life_expectancy
                x = x + 1 
                average = avg / x

                if life_expectancy < min_life:
                    min_life = life_expectancy
                    min_country = entity

                if life_expectancy > max_life:
                    max_life = life_expectancy
                    max_country = entity

    print(f"The overall max life expectancy is: {highest}, from {high_country} in {data_B_historical_period}")
    print(f"The overall min life expectancy is: {lowest}, from {low_country} in {data_A_historical_period}")
    print()
    print(f"For the year {year_interest}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The maximum life expectancy was in {max_country} with {max_life}")
    print(f"The minimum life expectancy was in {min_country} whit {min_life}")
    print()

print('The file is closed now')