def is_disarium(n):
    digits = str(n)
    total = sum(int(digit) ** (i + 1) for i, digit in enumerate(digits))
    return total == n

# Example usage:
print(is_disarium(135)) 
print(is_disarium(123))  

print(is_disarium(89))   
print(is_disarium(518))  
print(is_disarium(100))  
