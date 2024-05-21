greeting = "Hello World!"

def hello_world():
	return greeting

def hello_world_n(N):
    output = ''
    for cntr in range(N):
        if cntr > 0:
            output = output + ' ' # Add leading separating space
        output = output + greeting
    return output