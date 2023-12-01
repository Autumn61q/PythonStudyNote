def mirror(s):
    # Your reflective code here
    s=s[-1:-1-len(s):-1]+s
    return s

#Test your function with this input
print(mirror("Python"))  # Let's reflect on this!