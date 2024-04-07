import debugpy

# Start listening for a debugger connection
debugpy.listen(('localhost', 5679))
print("Waiting for debugger to attach...")

# Wait for the client to attach
debugpy.wait_for_client()

# Now you can set breakpoints, step through code, etc.
print("Debugger attached")
