# Método de Ordenação Quick Sort.
# Integrantes:
#
# Enzo Ribeiro – 32342853
# enzo.ribeiro@mackenzista.com.br
#
# Lucas Pires Camargo Sarai – 32336888
# 32336888@mackenzista.com.br
#
# Ismael de Souza Silva – 42280321
# 42280321@mackenzista.com.br
#
# Vitor Alves Pereira – 42280079
# 42280079@mackenzista.com.br
#
# Gabriel Lazareti Cardoso – 32322844
# 32322844@mackenzista.com.br
# ----------------------------------------------------------------------------------------------------------------
import turtle
import time

wn = turtle.Screen()

#Shows the main title Quick Sort
t_title = turtle.Turtle()
t_title.penup()
t_title.setpos(-300, 100)
t_title.fd(200)
t_title.write("Quick Sort:", False, "center", ("Arial", 20, "bold"))


def quad(t, a):
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.left(90)
    t.end_fill()


#Function to draw Mario's mushrooms
def cogumelo(t, xpos, ypos, color):
    t.penup()
    t.setpos(xpos, ypos)
    t.pendown()
    t._tracer(False)
    cogumelo = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 0, 0],
                [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                [1, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1],
                [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1],
                [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1],
                [1, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1],
                [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1],
                [0, 1, 1, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 1, 1, 0],
                [0, 0, 1, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 1, 0, 0],
                [0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 0, 0],
                [0, 0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]

    t.speed(0)
    for l in range(16):
        for c in range(16):
            if cogumelo[l][c] == 0:
                t.color("#ffffff")
            elif cogumelo[l][c] == 1:
                t.color("#000000")
                quad(t, 2)
            elif cogumelo[l][c] == 2:
                t.color(color)
                quad(t, 2)
            elif cogumelo[l][c] == 3:
                t.color("#F7C192")
                quad(t, 2)
            t.fd(2)
        t.penup()
        t.setpos(xpos, t.ycor() - 2)
        t.pendown()


t3 = turtle.Turtle()


#Function to draw Mario
def mario(x, y, a, t3):
    t3.shape("turtle")
    t3.penup()
    t3.setpos(x, y)
    t3.pendown()
    pixels2 = [[0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
               [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
               [0, 0, 6, 6, 6, 3, 3, 3, 1, 3, 0, 0, 0],
               [0, 6, 3, 6, 3, 3, 3, 3, 1, 3, 3, 3, 0],
               [0, 6, 3, 6, 6, 3, 3, 3, 3, 1, 3, 3, 3],
               [0, 6, 6, 3, 3, 3, 3, 3, 1, 1, 1, 1, 0],
               [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0],
               [0, 0, 2, 2, 5, 2, 2, 2, 2, 0, 0, 0, 0],
               [0, 2, 2, 2, 5, 2, 2, 5, 2, 2, 2, 0, 0],
               [2, 2, 2, 2, 5, 5, 5, 5, 2, 2, 2, 2, 0],
               [3, 3, 2, 5, 4, 5, 5, 4, 5, 2, 3, 3, 0],
               [3, 3, 3, 5, 5, 5, 5, 5, 5, 3, 3, 3, 0],
               [3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 0],
               [0, 0, 5, 5, 5, 0, 0, 5, 5, 5, 0, 0, 0],
               [0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 0],
               [6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0]]

    t3._tracer(False)
    t3.speed(0)
    for l in range(16):
        for c in range(13):
            if pixels2[l][c] == 0:
                t3.color("#ffffff")
            elif pixels2[l][c] == 1:
                t3.color("#000000")
                quad(t3, a)
            elif pixels2[l][c] == 2:
                t3.color("#F80500")
                quad(t3, a)
            elif pixels2[l][c] == 3:
                t3.color("#F7C192")
                quad(t3, a)
            elif pixels2[l][c] == 4:
                t3.color("#FDFD11")
                quad(t3, a)
            elif pixels2[l][c] == 5:
                t3.color("#0071C1")
                quad(t3, a)
            elif pixels2[l][c] == 6:
                t3.color("#9D4700")
                quad(t3, a)
            t3.fd(a)
        t3.penup()
        t3.setpos(x, t3.ycor() - a)
        t3.pendown()

#Draw Mario on home screen, with a speech bubble written "Vamos organizar cogumelos?"
mario(0, 50, 10, t3)
t3._tracer(True)
t_title.color("black")
t_title.shape("arrow")
t_title.setpos(100, 100)
t_title.speed(0)
t_title.pendown()
t_title.circle(95)
t_title.penup()
t_title.sety(180)
t_title.hideturtle()
t_title.write("Vamos organizar cogumelos? ", False, 'center', ('Arial', 10, 'bold'))
t_title.setpos(80, 80)
t_title.pendown()
t_title.circle(10)
time.sleep(5)
t_title.clear()
t3.clear()

#Receives an unsorted array
data = []
tamanho = int(input('Digite o tamanho do vetor: '))
for i in range(tamanho):
    data.append(int(input('Número [{}]: '.format(i))))

#Words turtle
t1 = turtle.Turtle()


y = -250
x = -60

xcog = x - 16
ycog = y + 32

#Mushroom's colors array
cores = ["yellow", "honeydew", "brown", "dark turquoise", "red", "green", "blue", "pink", "orange", "grey",
         'dark green', 'light blue', 'magenta', "#FFC09F", "#FFEE93", "#FCF5C7", "#A0CED9", "#ADF7B6"
        "#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51", "#BEE9E8", "#62B6CB", "#1B4965",
         "#CAE9FF", "#5FA8D3"]

#Match numbers with mushroom's colors
cogu_numbers = {}
for d in range(len(data)):
    cogu_numbers[data[d]] = cores[d]

# registering the image into turtle library
turtle.register_shape('mario_reduzido_maior.gif')

# setting the image as cursor
t1.shape('mario_reduzido_maior.gif')


def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]
    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    for k in range(len(array)):
        global xcog
        global ycog
        t1.color('black')
        cogumelo(t2, xcog, ycog, cogu_numbers[data[k]])
        t2._tracer(True)
        xcog += 40
        t1.write(array[k], False, 'center', ('Arial', 20, 'bold'))
        t1.penup()
        t1.forward(40)
        t1.pendown()
        if k == (len(array) - 1):
            ycog += 50
            xcog -= len(array) * 40
    t1.penup()
    t2.penup()
    global y
    y += 50
    t1.setpos(x, y)
    t1.pendown()
    t2.pendown()

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)

print("Unsorted Array")
print(data)

#Show the original array
t1.penup()
t1.setpos(x - 40, y)
t1.write('Array Original:', False, 'right', ('Arial', 20, 'bold'))
t1.setpos(x, y)
t1.pendown()

#Mushroom's turtle
t2 = turtle.Turtle()

cogumelo(t2, xcog, ycog, 'red')

#Show the process while quick sorting
for i in range(len(data)):
    cogumelo(t2, xcog, ycog, cogu_numbers[data[i]])
    t2._tracer(True)
    xcog += 40
    t1.color('black')
    t1.write(data[i], False, 'center', ('Arial', 20, 'bold'))
    t1.penup()
    t1.forward(40)
    t1.pendown()
ycog += 50
xcog -= len(data) * 40
t1.penup()
t1.color('black')
y += 50
t1.setpos(x - 40, y)
t1.write('QuickSorting Array:', False, 'right', ('Arial', 20, 'bold'))
t1.setpos(x, y)
t1.pendown()

size = len(data)

#Execute the Quick Sort with the given array
quickSort(data, 0, size - 1)

t1.penup()
t1.color('black')
t1.setpos(x - 40, y)
t1.write('Array organizado:', False, 'right', ('Arial', 20, 'bold'))
t1.setpos(x, y)
t1.pendown()

#Show the sorted array
for i in range(len(data)):
    cogumelo(t2, xcog, ycog, cogu_numbers[data[i]])
    t2._tracer(True)
    xcog += 40
    t1.color('black')
    t1.write(data[i], False, 'center', ('Arial', 20, 'bold'))
    t1.penup()
    t1.forward(40)
    t1.pendown()

print('Sorted Array in Ascending Order:')
print(data)

#Fixes the screen
wn.mainloop()
