from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import ast

# VIEWS
## Main
def main(request, graphemes="", codepoints="", bits=""):
    
    return render(request, 'index.html', {"letter_val": graphemes,
                                          "number_val": codepoints, 
                                          "binary_val": bits})

## Json Convert Request
def convert(request):

    field = request.GET.get('field', None)
    value = request.GET.get('value', None)
    n_fmt = request.GET.get('num_format', None)

    print(" -- IN -- :")
    print("\t"+str(field)+": "+str(value)+" (fmt: "+str(n_fmt)+")")

    if (field == None or value == None or n_fmt == None):
        print("Cannot convert with None values.");
        return JsonResponse({});

    else:

        if field == "letter":
            letter = value
            number = letter_to_number(value)
            binary = letter_to_binary(value)

        elif field == "number":
            letter = number_to_letter(value)
            number = value
            binary = number_to_binary(value)

        elif field == "binary":
            letter = binary_to_letter(value)
            number = binary_to_number(value)
            binary = value
        else:
            # TODO: Check this shit!!!
            print("OH SHIT!")

        data = {
            'letter': letter,
            'number': number,
            'binary': binary
        }

        print(" -- OUT --")
        print("    letter: "+str(letter)+"\n    number: "+str(number)+"\n    binary: "+str(binary)+"\n")

        return JsonResponse(data)

## Deprecated POST Method
def submit(request):

    # Console Log Data
    print("\nPOST data (/submit/)\n<data>")
    for key, val in request.POST.items():
        print("    "+key+": "+val)
    print("</data>\n")

    # Conversion
    # 1 - Graphemes
    chars = request.POST['letter']
    char_count = len(chars)

    # 2 - Code Points
    nums = to_number(chars)
    num_count = len(nums)

    # 3 - Bits! (and Bytes)
    binary = to_binary(chars)
    bin_count = len(binary)

    # Console Logs
    print("letter: {} ({})".format(chars, char_count))
    print("bytes : {} ({})".format(nums, num_count))
    print("binary: {} ({})\n".format(binary, bin_count))


    letter_val = chars
    number_val = str(nums)
    binary_val = str(binary)

    return render(request, 'index.html', {"letter_val": letter_val,"number_val": number_val, "binary_val": binary_val})
    # return HttpResponseRedirect(reverse('main', args=(40, "hello")))


# CONVERSIONS
## Letter
def letter_to_number(letter, u_fmt=False):
    array = []
    # A = 'U+0041'
    if u_fmt:
        for s in letter:
            p = 'U+{:04x}'.format(ord(s))
            array.append(p)
    # A = '65'
    else: 
        for s in letter:
            array.append(ord(s))
    return array

def letter_to_binary(letter, encoding="utf-8", block_size=1):
    numbers = letter.encode(encoding)
    i = 0;
    bins   = []
    blocks = []
    for num in numbers:
        i += 1
        bins.append(int_to_bin(num))
        if i % block_size == 0:
            blocks.append(bins)
            bins = []

    return blocks

## Number
def number_to_letter(number, u_fmt=False):
    # Takes a string in format: "3432,23423,2343,01"
    arr = number.split(",")
    string = ""
    
    for num_str in arr:
        if u_fmt:
            hex_str = num_str[2:] # TODO: Check this
            num = int(hex_str, 16)
            string += chr(num)
        else:
            string += chr(int(num_str))
    return string

def number_to_binary(number, u_fmt=False, encoding="utf-8", block_size=1):
    letters = number_to_letter(number, u_fmt)
    binary  = letter_to_binary(letters, encoding, block_size)
    return binary

## Binary
def binary_to_letter(binary, encoding="utf-8", block_size=1):
    
    print(binary);

    arr = binary.split(",")

    b = bytes()

    for byte in arr:
        i = bin_to_int(byte)
        b += i.to_bytes(1, byteorder="big")
        print("BB: "+str(b))



    string = b.decode(encoding, "strict")
    return string

def binary_to_number(binary, encoding="utf-8", block_size=1, u_fmt=False):
    letters = binary_to_letter(binary, encoding, block_size)
    numbers = letter_to_number(letters, u_fmt)
    return numbers

## Bin String Converters
""" Turns integers into pretty binary strings """
def int_to_bin(int):
    byte = bin(int)[2:]
    assert len(byte) <= 8, "Byte longer than 8 bits. "+str(byte);
    padded = "{:0>8}".format(byte)
    # return padded[:4] + " " + padded[4:]
    return padded

def bin_to_int(bin_string):
    assert len(bin_string) <= 8, "Your bin string is too long! ("+str(len(bin_string))+")"
    return int(bin_string, 2)
