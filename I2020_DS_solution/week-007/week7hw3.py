def script(*args):
    open_file = open('output.html', 'w')
    open_file.write("<body>")

    for s in args[1:]:
        open_file.write(s + ' ')

    open_file.write("</body>")
    open_file.close()

    return "You're done."


def other_steps(value):
    print(value)

    
if __name__ == '__main__':
    import sys
    script(*sys.argv)
