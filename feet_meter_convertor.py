def converter(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

def empty (feet, inches):
    if feet == '' and inches == '':
        return sg.popup('please provide two numbers')