def reverseString1(str):
  return str[::-1]

# also possible to use list(str) to get array of characters from string
def reverseString2(str):
    chars = [letter for letter in str]

    for i in range(0,len(str)//2):
      chars[i],chars[-1-i] = chars[-1-i], chars[i]

    return ''.join(chars)

def main():
    result = reverseString2("apple")
    print(result)

main()