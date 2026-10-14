t1 = int(input("Enter the points earned:"))
t2 = int(input("Enter the points earned:"))
t3 = int(input("Enter the points earned:"))
t4 = int(input("Enter the points earned:"))
t5 = int(input("Enter the points earned:"))

total = t1 + t2 + t3 + t4 + t5
average = total / 5

print("Total points:", total)
print("Average per team:", average)

star_per_point = int(input("Enter the stars per point:"))
reward_stars = total * star_per_point
print("Total reward stars: Rs.",reward_stars)

boxes = reward_stars // 25
left = reward_stars % 25

print("Full boxes packed:",boxes)
print("Leftover stars:",left,"kg")

last_week = 500
print("Better than last year?", total > last_week)
print("Same as last year?:", total == last_week)
print("At least as good?:", total >= last_week)

total += int(input("Enter the bonus points:"))
print("After bonus points:", total)

total -= int(input("Enter the missed tasks:"))
print("After missed tasks:", total)

reward_stars = total * star_per_point
bags = reward_stars // 25
print("Final boxes packed:",bags)