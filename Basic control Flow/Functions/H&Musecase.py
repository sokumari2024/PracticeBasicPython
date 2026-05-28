def size(height):
    if height < 150:
        return "s"
    elif height >= 150 and height < 180:
        return "m"
    else:
        return "l"
    
def sizecount(categoryheight):
    count={"s":0, "m":0, "l":0}
    for i in categoryheight:
        count[i] += 1
    return count
    
categoryheight=map(size, [144, 167, 189,170,190, 150,165,178,200,130])
print(sizecount(list(categoryheight)))  