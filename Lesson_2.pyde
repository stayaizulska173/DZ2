''' 
# Task 1

def setup():
    size(700, 300)
    noFill()
    frameRate(4)

def draw():
    background(255, 255, 255)
    for x in range(50, width - 50, 50):
        for y in range(50, height - 50, 50):
            for i in range(0, 8, 4):
                fill(random(255), random(255), random(255))
                stroke(random(255), random(255), random(255))
                square(x + i, y+i, 20)
            fill(255)
            stroke(0)
            line(x, y + random(0, 20), x + 20, y + random(0, 24))
'''
'''
add_library('svg')

def setup():
    size(480, 120)
    noLoop()
    beginRecord(SVG, "name.svg")

def draw():
    if  mousePressed:
        fill(0)
    else:
        fill(255)
    ellipse(mouseX, mouseY, 80, 80)
    endRecord()
'''   
''' 
def setup():
    size(700, 700)
    background(255, 255, 255)

def draw():
    strokeWeight(1)
    if (keyCode ==  UP):
        x = random(0, 700)
        y = random(0, 700)
        ellipse(y, x, 20, 20)
''' 
''' 
def setup():
    size(700, 300)
    noFill()
    frameRate(4)

def draw():
    background(255, 255, 255)

    for x in range(50, width - 50, 50):
        for y in range(50, height - 50, 50):
            for i in range(0, 16, 4):
                pushMatrix()
                translate(i, i)
                line(x, y, x, y + 12)
                popMatrix()
''' 
''' 
angle = 0
def setup():
    size(700, 300)
    fill(255, 255, 255)
    frameRate(40)
def draw():
    global angle
    background(255, 255, 255)
    for x in range(50, width - 50, 50):
        pushMatrix()
        for y in range(50, height - 50, 50):
            for i in range(0, 16, 4):
                translate(i, i)
                ellipse(x, y, x*0.1, y*0.1 + 12)
                rotate(radians(angle))
        popMatrix()
    angle = angle + 0.05
''' 
'''
angle = 0
def setup():
   size(700, 300)
   fill(0, 0, 0)
def draw():
    background(255, 255, 255)
    global angle
    push()
    translate(mouseX, mouseY)
    rotate(radians(angle))
    scale(2)
    line(-50, -50, 50, 50)
    line(50, -50, -50, 50)
    angle = angle + 1
    pop()
    noFill()
    rect(10, 10, width, height)
'''
'''
x = 0
y = 0
targetX = 0
targetY = 0

def setup():
   size(700, 300)
def draw():
    background(255, 255, 255)
    global x, y, targetX, targetY
    ellipse(x, y, 50, 50)
    easing = 0.125
    diffX = targetX - x
    x = x + diffX * easing
    diffY = targetY - y
    y = y + diffY * easing
def mousePressed():
    global targetX, targetY
    targetX = mouseX
    targetY = mouseY
'''
'''
# Task 2
angle = 0
coef=[0, 0.4, 0.5, 0.7, 0.9, 1.1, 1.4, 1.5, 1.7, 1.9, 2.0, 2.1, 2.3]
offset = 200
step = 100
speed = 0.05
num = 20
def setup():
    size(800, 400)
    fill(0)
    noStroke()
def draw():
    background(255, 255, 255)
    global angle 
    fill(255, 0,0)
    for i in range(13):        
        y = offset + sin(angle+coef[i]) * step
        ellipse(50*(i+1), y, 20, 20)  
    fill(0, 0,255)
    for i in range(13):        
        y = offset + cos(angle+coef[i]) * step
        ellipse(50*(i+1), y, 20, 20)    
    angle = angle + speed


'''

'''
# Task 3
numSegments = 20
x = [0.0] * numSegments
y = [0.0] * numSegments
angle = [0.0] * numSegments
segLength = 26
targetX = 0
targetY = 0

def setup():
    size(640, 360)
    strokeWeight(20.0)
    
    x[len(x) - 1] = width / 2  # Set base x-coordinate
    y[len(x) - 1] = height  # Set base y-coordinate


def draw():
    background(0)    
    reachSegment(0, mouseX, mouseY)    
    for i in range(1, numSegments):               
        reachSegment(i, targetX, targetY)
    for i in range(len(x) - 1, 0, -1):       
        positionSegment(i, i - 1)
    for i in range(len(x)):
        segment(x[i], y[i], angle[i], (i + 1) * 2)


def positionSegment(a, b):
    x[b] = x[a] + cos(angle[a]) * segLength
    y[b] = y[a] + sin(angle[a]) * segLength
    fill(random(255), random(255), random(255))

def reachSegment(i, xin, yin):
    dx = xin - x[i]
    dy = yin - y[i]
    angle[i] = atan2(dy, dx)
    global targetX, targetY
    targetX = xin - cos(angle[i]) * segLength
    targetY = yin - sin(angle[i]) * segLength


def segment(x, y, a, sw):
    strokeWeight(sw)
    stroke(random(255), random(255), random(255)) 
    with pushMatrix():
        translate(x, y)
        rotate(a)        
        line(0, 0, segLength, 0)

'''

# Task 4
rot = 0
speed = 0.00015
angle=0
def setup():   
    size(800, 600)
def draw():    
    background(0)
    #translate(mouseX-width/3 if mouseX>width/2 else mouseX, mouseY-height/3 if mouseY>height/2 else mouseY)
    translate(0, mouseY)
    #rotate(sin(mouseX%360))
    global rot, angle
    rotate(radians(rot))
    for i in range(200):
        
        fill(random(255), random(255),random(255))
        circle = 150 * sin(millis() * speed * i)
        y = circle + sin(angle+i/10) * speed
        ellipse(20*(i+1), y, 10, 10)  
        
        y = circle + cos(angle+i/10) * speed
        fill(random(255), random(255),random(255))
        ellipse(20*(i+1)-10, y+5, 5, 5) 
        
        y = circle + tan(angle+i/10) * speed
        fill(random(255), random(255),random(255))
        rect(20*(i+1)+10, y-5, 5, 10) 
        
    rot = rot + 0.0000005
    angle+=speed
