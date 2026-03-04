import turtle

def main():
    screen = turtle.Screen()  # Creates a graphics window
    screen.setup(600, 400) # Optional: set the window size
    alex = turtle.Turtle()    # Create a turtle named alex
    alex.forward(100)         # Tell alex to move forward
    alex.left(90)             # Turn by 90 degrees
    alex.forward(75)          # Draw a second side

    # This keeps the window open until you click on it
    screen.exitonclick() 

if __name__ == "__main__":
    main()
