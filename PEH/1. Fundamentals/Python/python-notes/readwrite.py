#!/bin/python3

months = open('months.txt')

print(months.read())
print(months.readlines())
months.close()

days = open('days.txt', "w") #r=read w=write a= append
print(days)
print(days.mode)


days.write("Monday")
days.write("\nTuesday")

days.close()